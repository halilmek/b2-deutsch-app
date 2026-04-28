/**
 * B2 Deutsch — Topic 3 Questions → Firestore Import (LOCAL FILE VERSION)
 * ========================================================================
 * Reads from local b2_04.json — no GitHub token needed!
 * 
 * Run: node scripts/firestore_import_topic3.js
 * 
 * Prerequisites:
 *   npm install firebase-admin
 *   Set GOOGLE_APPLICATION_CREDENTIALS environment variable
 * 
 * Usage:
 *   export GOOGLE_APPLICATION_CREDENTIALS=/path/to/serviceAccountKey.json
 *   node scripts/firestore_import_topic3.js
 */

const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');

// ============================================================
// FIREBASE INITIALIZATION
// ============================================================

const serviceAccount = process.env.GOOGLE_APPLICATION_CREDENTIALS 
  ? JSON.parse(fs.readFileSync(process.env.GOOGLE_APPLICATION_CREDENTIALS))
  : null;

if (!serviceAccount) {
  console.error('❌ Set GOOGLE_APPLICATION_CREDENTIALS first!');
  console.error('   export GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json');
  process.exit(1);
}

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount)
});

const db = admin.firestore();
const FIELD = admin.firestore.FieldValue;

// ============================================================
// LOAD LOCAL JSON FILE
// ============================================================

const assetsDir = path.join(__dirname, '..', 'app', 'src', 'main', 'assets');
const jsonPath = path.join(assetsDir, 'b2_04.json');

if (!fs.existsSync(jsonPath)) {
  console.error('❌ File not found:', jsonPath);
  process.exit(1);
}

const data = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));

console.log('📋 Topic:', data.topicName);
console.log('   subjectId:', data.subjectId);
console.log('   totalQuestions:', data.totalQuestions);

// ============================================================
// IMPORT TO FIRESTORE
// ============================================================

async function importTopic3Questions() {
  
  // === Option A: Single document with all questions ===
  console.log('\n🔄 Importing as single document...');
  
  const questionsForFirestore = data.questions.map(q => ({
    id: q.id,
    module: 'B2',
    topicNumber: '3. Topic',
    topicName: q.topicName || data.topicName,
    questionText: q.questionText,
    options: q.options,
    correctAnswer: q.correctAnswer,
    explanation: q.explanation,
    difficulty: q.difficulty,
    type: q.type,
    level: 'B2'
  }));

  const docRef = db.collection('moduleQuizQuestions').doc('b2_04');
  await docRef.set({
    id: 'b2_04',
    subjectId: data.subjectId,
    module: 'B2',
    topicNumber: '3. Topic',
    topicName: data.topicName,
    totalQuestions: data.totalQuestions,
    questions: questionsForFirestore,
    updatedAt: FIELD.serverTimestamp()
  });
  console.log('✅ Option A: Uploaded', questionsForFirestore.length, 'questions as one document');

  // === Option B: Individual documents ===
  console.log('\n🔄 Importing as individual documents...');
  
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
        topicName: q.topicName || data.topicName,
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
    console.log('  Batch', Math.floor(i / BATCH_SIZE) + 1, ':', batchQuestions.length, 'questions');
  }

  console.log('✅ Option B: Imported', totalImported, 'individual documents');
  console.log('\n🎉 Done! Topic 3 questions are now in Firestore.');
  console.log('📍 Firestore > moduleQuizQuestions > b2_04 (and b2_04_q001 ... b2_04_q160)');
}

// ============================================================

importTopic3Questions()
  .then(() => { console.log('\nDone!'); process.exit(0); })
  .catch(err => { console.error('❌ Error:', err); process.exit(1); });