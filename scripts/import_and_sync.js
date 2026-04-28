/**
 * B2 Deutsch — Import & Sync Script (Option A)
 * ============================================
 * Reads local JSON → pushes to BOTH GitHub (assets) AND Firestore.
 * Use this whenever you add new questions to any topic.
 *
 * Usage:
 *   node scripts/import_and_sync.js                    # push all topics
 *   node scripts/import_and_sync.js b2_04             # push specific topic
 *   node scripts/import_and_sync.js b2_04 b2_05     # push multiple topics
 *
 * Prerequisites:
 *   npm install firebase-admin
 *   export GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json
 *
 * What it does:
 *   1. Reads local b2_XX.json from app/src/main/assets/
 *   2. Updates version number for that topic in Firestore
 *   3. Pushes updated JSON file to GitHub assets
 *   4. Users get the update within 7 days (or on next app open if forced)
 */

const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');
const https = require('https');

// ============================================================
// CONFIG
// ============================================================

const GITHUB_TOKEN = process.env.GITHUB_TOKEN || process.env.GITHUB_TOKEN;
const REPO = 'halilmek/b2-deutsch-app';
const ASSETS_DIR = path.join(__dirname, '..', 'app', 'src', 'main', 'assets');

// ============================================================
// FIREBASE INIT
// ============================================================

const serviceAccount = process.env.GOOGLE_APPLICATION_CREDENTIALS
  ? JSON.parse(fs.readFileSync(process.env.GOOGLE_APPLICATION_CREDENTIALS, 'utf8'))
  : null;

if (serviceAccount) {
  admin.initializeApp({ credential: admin.credential.cert(serviceAccount) });
  console.log('✅ Firebase Admin initialized');
} else {
  console.log('⚠️  Firebase not configured — will only push to GitHub');
}

const db = admin.firestore();
const FIELD = admin.firestore.FieldValue;

// ============================================================
// GITHUB HELPERS
// ============================================================

function githubGet(path) {
  return new Promise((resolve, reject) => {
    const req = https.request({
      hostname: 'api.github.com',
      path: '/repos/' + REPO + '/contents/' + path,
      method: 'GET',
      headers: { 'Authorization': 'token ' + GITHUB_TOKEN, 'User-Agent': 'B2DeutschImport', 'Accept': 'application/json' }
    }, res => {
      let d = '';
      res.on('data', c => d += c);
      res.on('end', () => {
        try { resolve(JSON.parse(d)); }
        catch(e) { reject(new Error('Parse error: ' + d.substring(0,100))); }
      });
    });
    req.on('error', reject);
    req.end();
  });
}

function githubPut(path, content, sha, message) {
  return new Promise((resolve, reject) => {
    const body = JSON.stringify({
      message: message,
      content: Buffer.from(content).toString('base64'),
      sha: sha,
      branch: 'main'
    });
    const req = https.request({
      hostname: 'api.github.com',
      path: '/repos/' + REPO + '/contents/' + path,
      method: 'PUT',
      headers: { 'Authorization': 'token ' + GITHUB_TOKEN, 'User-Agent': 'B2DeutschImport', 'Content-Type': 'application/json' }
    }, res => {
      let d = '';
      res.on('data', c => d += c);
      res.on('end', () => resolve({ status: res.statusCode, body: d }));
    });
    req.on('error', reject);
    req.write(body);
    req.end();
  });
}

// ============================================================
// FIRESTORE HELPERS
// ============================================================

async function updateFirestoreTopic(data) {
  const subjectId = data.subjectId; // e.g. "b2_04"
  const docId = subjectId; // doc ID matches subjectId

  // Build questions array for Firestore
  const questions = data.questions.map(q => ({
    id: q.id,
    subjectId: q.subjectId || subjectId,
    module: 'B2',
    topicNumber: subjectId.replace('b2_0', '').replace('b2_', '') + '. Topic',
    topicName: q.topicName || data.topicName,
    type: q.type || 'multiple_choice',
    questionText: q.questionText,
    options: q.options || [],
    correctAnswer: q.correctAnswer,
    explanation: q.explanation || '',
    difficulty: q.difficulty || 'medium',
    level: 'B2'
  }));

  // Get current version, increment
  const currentDoc = await db.collection('moduleQuizQuestions').doc(docId).get();
  const currentVersion = currentDoc.exists ? (currentDoc.get('version') || 0) : 0;
  const newVersion = currentVersion + 1;

  const docData = {
    id: docId,
    subjectId: subjectId,
    module: 'B2',
    topicName: data.topicName,
    totalQuestions: data.totalQuestions,
    version: newVersion,
    updatedAt: FIELD.serverTimestamp(),
    questions: questions
  };

  await db.collection('moduleQuizQuestions').doc(docId).set(docData, { merge: true });

  // Also push individual question docs (for granular queries)
  const batchSize = 400;
  for (let i = 0; i < questions.length; i += batchSize) {
    const batch = db.batch();
    questions.slice(i, i + batchSize).forEach(q => {
      const qRef = db.collection('moduleQuizQuestions').doc(q.id);
      batch.set(qRef, q, { merge: true });
    });
    await batch.commit();
  }

  console.log(`  ✅ Firestore: ${questions.length} questions, version ${newVersion}`);
  return newVersion;
}

// ============================================================
// PUSH SINGLE TOPIC
// ============================================================

async function pushTopic(subjectId) {
  console.log(`\n📦 Processing ${subjectId}...`);

  const fileName = subjectId + '.json';
  const filePath = path.join(ASSETS_DIR, fileName);

  if (!fs.existsSync(filePath)) {
    console.log(`  ❌ File not found: ${filePath}`);
    return;
  }

  // Read local JSON
  const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));
  console.log(`  📋 Topic: "${data.topicName}" | ${data.totalQuestions} questions`);

  // Step 1: Push to GitHub assets
  console.log(`  🔄 Pushing to GitHub...`);
  const githubPath = 'app/src/main/assets/' + fileName;
  const currentSHA = await githubGet(githubPath).then(r => r.sha).catch(() => null);

  if (!currentSHA) {
    console.log(`  ❌ Could not get SHA for ${githubPath}`);
    return;
  }

  const newContent = JSON.stringify(data, null, 2);
  const gitResult = await githubPut(githubPath, newContent, currentSHA, `Update ${subjectId}: ${data.topicName} (${data.totalQuestions} questions)`);

  if (gitResult.status === 200) {
    console.log(`  ✅ GitHub: ${fileName} updated`);
  } else {
    console.log(`  ❌ GitHub push failed: ${gitResult.status}`);
  }

  // Step 2: Push to Firestore
  if (serviceAccount) {
    console.log(`  🔄 Pushing to Firestore...`);
    try {
      await updateFirestoreTopic(data);
    } catch(e) {
      console.log(`  ❌ Firestore error: ${e.message}`);
    }
  } else {
    console.log(`  ⚠️  Skipped Firestore (no credentials)`);
  }

  console.log(`  ✅ ${subjectId} sync complete!`);
}

// ============================================================
// MAIN
// ============================================================

async function main() {
  const args = process.argv.slice(2);

  if (args.length === 0) {
    // Push all b2_XX.json files
    const files = fs.readdirSync(ASSETS_DIR)
      .filter(f => f.match(/^b2_0[1-9]\.json$/) || f.match(/^b2_[12][0-9]\.json$/))
      .sort();

    console.log(`\n🚀 Syncing ALL ${files.length} topics to GitHub + Firestore...\n`);

    for (const f of files) {
      const subjectId = f.replace('.json', '');
      await pushTopic(subjectId);
    }

    console.log(`\n🎉 All ${files.length} topics synced!`);
  } else {
    // Push specific topics
    for (const subjectId of args) {
      await pushTopic(subjectId);
    }
  }

  console.log(`\n📱 Users will receive updates when they open the app (within 7 days max).\n`);
}

main().catch(e => { console.error('Error:', e.message); process.exit(1); });