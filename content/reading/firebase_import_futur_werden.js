#!/usr/bin/env node
/**
 * Firebase Import: B2 Topic 5 (Futur mit werden) — 100 Questions
 * Collection: moduleQuizQuestions
 *
 * Run: node firebase_import_futur_werden.js
 * Requires: GOOGLE_APPLICATION_CREDENTIALS env var pointing to service account JSON
 */

const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');

// ── Firebase Init ──────────────────────────────────────────────────────────
const serviceAccountPath = process.env.GOOGLE_APPLICATION_CREDENTIALS
  || path.join(__dirname, '..', '..', '..', 'b2-deutsch-app-firebase-adminsdk-fbsvc-4aa25c0ca2.json');

if (fs.existsSync(serviceAccountPath)) {
  const serviceAccount = JSON.parse(fs.readFileSync(serviceAccountPath, 'utf8'));
  admin.initializeApp({ credential: admin.credential.cert(serviceAccount) });
  console.log('✅ Firebase Admin initialized\n');
} else {
  console.error(`❌ Service account key not found at:\n   ${serviceAccountPath}`);
  console.error('   Set GOOGLE_APPLICATION_CREDENTIALS env var, or place the JSON file there.\n');
  process.exit(1);
}

const db = admin.firestore();
const FIELD = admin.firestore.FieldValue;

// ── Load b2_06.json ───────────────────────────────────────────────────────
// Correct path: running from content/reading/ → go up 3 levels to project root
const ASSETS_DIR = path.join(__dirname, '..', '..', 'app', 'src', 'main', 'assets');
const b2_06_path = path.join(ASSETS_DIR, 'b2_06.json');
const data = JSON.parse(fs.readFileSync(b2_06_path, 'utf8'));
const questions = data.questions;

console.log(`📦 Loaded ${questions.length} questions from b2_06.json: "${data.topicName}"\n`);

// ── Helpers ────────────────────────────────────────────────────────────────
async function pushTopicDoc() {
  const docData = {
    id: 'b2_06',
    subjectId: 'b2_06',
    module: 'B2',
    topicNumber: '4. Topic',
    topicName: data.topicName,
    totalQuestions: questions.length,
    version: 1,
    updatedAt: FIELD.serverTimestamp(),
    level: 'B2'
  };
  await db.collection('topics').doc('b2_06').set(docData, { merge: true });
  console.log(`✅ topics/b2_06 created`);
}

async function pushQuestions() {
  console.log(`\n📝 Pushing ${questions.length} questions to moduleQuizQuestions...`);

  // Batch write — Firestore limit is 500 writes/batch
  const batchSize = 400;
  let success = 0;

  for (let i = 0; i < questions.length; i += batchSize) {
    const batch = db.batch();
    questions.slice(i, i + batchSize).forEach(q => {
      const qRef = db.collection('moduleQuizQuestions').doc(q.id);
      batch.set(qRef, q, { merge: true });
    });
    await batch.commit();
    success += Math.min(batchSize, questions.length - i);
    process.stdout.write(`  Progress: ${success}/${questions.length}  \r`);
  }

  console.log(`\n✅ ${success} questions pushed to moduleQuizQuestions`);
}

// ── Main ───────────────────────────────────────────────────────────────────
async function main() {
  try {
    await pushTopicDoc();
    await pushQuestions();

    console.log(`\n🎉 Done! View in Firebase Console:`);
    console.log(`  https://console.firebase.google.com/project/b2-deutsch-app/firestore`);
    console.log(`  → moduleQuizQuestions/b2_06`);
    console.log(`  → topics/b2_06`);
    console.log(`\n  App will receive update within 7 days (or force sync).\n`);

    process.exit(0);
  } catch (err) {
    console.error('\n❌ Error:', err.message);
    process.exit(1);
  }
}

main();
