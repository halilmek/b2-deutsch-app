/**
 * B2 Deutsch — Topic 3 Questions → Firestore Import
 * ======================================================
 * Imports b2_04.json (Zeitformen der Vergangenheit) into Firestore
 * 
 * Run: node firestore_import_topic3.js
 * 
 * Prerequisites:
 *   npm install firebase-admin
 *   Set GOOGLE_APPLICATION_CREDENTIALS environment variable
 */

const admin = require('firebase-admin');
const fs = require('fs');
const https = require('https');

// ============================================================
// FIREBASE INITIALIZATION
// ============================================================

const serviceAccount = process.env.GOOGLE_APPLICATION_CREDENTIALS 
  ? JSON.parse(fs.readFileSync(process.env.GOOGLE_APPLICATION_CREDENTIALS))
  : null;

if (!serviceAccount) {
  console.error('❌ Set GOOGLE_APPLICATION_CREDENTIALS first!');
  console.error('   Export your Firebase service account key:');
  console.error('   export GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json');
  process.exit(1);
}

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount)
});

const db = admin.firestore();
const FIELD = admin.firestore.FieldValue;

// ============================================================
// DOWNLOAD b2_04.json FROM GITHUB
// ============================================================

function downloadFromGithub(path) {
  return new Promise((resolve, reject) => {
    // Get token from env (never hardcode!)
const path = require('path');
const token = process.env.GITHUB_TOKEN;
if (!token) {
  console.error('❌ Set GITHUB_TOKEN environment variable first');
  process.exit(1);
}
    const req = https.request({
      hostname: 'api.github.com',
      path: '/repos/halilmek/b2-deutsch-app/contents/' + path,
      method: 'GET',
      headers: {'Authorization': 'token ' + token, 'User-Agent': 'Kara', 'Accept': 'application/json'}
    }, res => {
      let d = '';
      res.on('data', c => d += c);
      res.on('end', () => {
        try {
          const json = JSON.parse(d);
          const content = Buffer.from(json.content, 'base64').toString('utf8');
          resolve({sha: json.sha, data: JSON.parse(content)});
        } catch(e) { reject(e); }
      });
    });
    req.on('error', reject);
    req.end();
  });
}

// ============================================================
// IMPORT QUESTIONS TO FIRESTORE
// ============================================================

async function importTopic3Questions() {
  console.log('📥 Downloading b2_04.json from GitHub...');
  
  const { data } = await downloadFromGithub('app/src/main/assets/b2_04.json');
  
  console.log(`\n📋 Topic: "${data.topicName}"`);
  console.log(`   subjectId: ${data.subjectId}`);
  console.log(`   totalQuestions: ${data.totalQuestions}`);
  
  // Option A: Store all questions in ONE document (easier to query)
  console.log('\n🔄 Option A: Importing as single document in moduleQuizQuestions...');
  
  const docRef = db.collection('moduleQuizQuestions').doc('b2_04');
  
  // Build questions array without the subcollection complexity
  const questionsForFirestore = data.questions.map(q => ({
    id: q.id,
    module: 'B2',
    topicNumber: '3. Topic',
    topicName: data.topicName,  // "Zeitformen der Vergangenheit (Perfekt, Präteritum, Plusquamperfekt)"
    questionText: q.questionText,
    options: q.options,
    correctAnswer: q.correctAnswer,
    explanation: q.explanation,
    difficulty: q.difficulty,
    type: q.type,
    level: 'B2'
  }));
  
  const docData = {
    id: 'b2_04',
    subjectId: data.subjectId,
    module: 'B2',
    topicNumber: '3. Topic',
    topicName: data.topicName,
    totalQuestions: data.totalQuestions,
    questions: questionsForFirestore,
    updatedAt: FIELD.serverTimestamp()
  };
  
  await docRef.set(docData);
  console.log(`✅ Uploaded ${questionsForFirestore.length} questions as single document!`);
  
  // Option B: Import as individual documents (for per-question queries)
  console.log('\n🔄 Option B: Importing as individual documents...');
  
  const BATCH_SIZE = 400;
  let totalImported = 0;
  
  for (let i = 0; i < data.questions.length; i += BATCH_SIZE) {
    const batch = db.batch();
    const batchQuestions = data.questions.slice(i, i + BATCH_SIZE);
    
    for (const q of batchQuestions) {
      const qRef = db.collection('moduleQuizQuestions').doc(q.id);
      
      const qData = {
        id: q.id,
        subjectId: q.subjectId,
        module: 'B2',
        topicNumber: '3. Topic',
        topicName: q.topicName,
        type: q.type,
        questionText: q.questionText,
        options: q.options,
        correctAnswer: q.correctAnswer,
        explanation: q.explanation,
        difficulty: q.difficulty,
        level: 'B2'
      };
      
      batch.set(qRef, qData);
      totalImported++;
    }
    
    await batch.commit();
    console.log(`  Batch ${Math.floor(i/BATCH_SIZE)+1}: imported ${batchQuestions.length} questions`);
  }
  
  console.log(`\n✅ Option B: Imported ${totalImported} individual question documents`);
  console.log('\n🎉 Topic 3 questions are now in Firestore!');
  console.log('\n📍 Location: Firestore > moduleQuizQuestions > b2_04 (document)');
  console.log('   Or individual docs: moduleQuizQuestions > b2_04_q001 ... b2_04_q160');
}

// ============================================================
// RUN
// ============================================================

importTopic3Questions()
  .then(() => { console.log('\nDone!'); process.exit(0); })
  .catch(err => { console.error('Error:', err); process.exit(1); });