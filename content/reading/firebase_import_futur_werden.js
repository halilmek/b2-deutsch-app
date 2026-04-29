#!/usr/bin/env node
/**
 * Firebase Import: B2 Topic 5 (Futur mit werden) — 100 Questions
 * Collection: moduleQuizQuestions
 *
 * Run: node firebase_import_futur_werden.js
 * Requires: Firestore rules allow read/write
 */

const https = require('https');
const fs = require('fs');
const path = require('path');

const PROJECT_ID = 'b2-deutsch-app';
const API_KEY = 'AIzaSyDHUwnlKx-ArzA5yZD4WhXI5sfACTzkedc';

// Load b2_06.json from assets
const ASSETS_DIR = path.join(__dirname, '..', 'app', 'src', 'main', 'assets');
const data = JSON.parse(fs.readFileSync(path.join(ASSETS_DIR, 'b2_06.json'), 'utf8'));
const questions = data.questions;

console.log(`📦 Loaded ${questions.length} questions from b2_06.json: "${data.topicName}"\n`);

// Helper: POST to Firestore REST API
function firestorePost(collection, docId, fields) {
  return new Promise((resolve, reject) => {
    const body = JSON.stringify({ fields });
    const options = {
      hostname: 'firestore.googleapis.com',
      path: `/v1/projects/${PROJECT_ID}/databases/(default)/documents/${collection}?documentId=${docId}&key=${API_KEY}`,
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Content-Length': Buffer.byteLength(body) }
    };
    const req = https.request(options, res => {
      let d = '';
      res.on('data', c => d += c);
      res.on('end', () => {
        try {
          const parsed = JSON.parse(d);
          resolve({ status: res.statusCode, body: parsed });
        } catch {
          resolve({ status: res.statusCode, body: d });
        }
      });
    });
    req.on('error', reject);
    req.write(body);
    req.end();
  });
}

// Convert to Firestore field format
function toFields(obj) {
  const fields = {};
  for (const [k, v] of Object.entries(obj)) {
    if (Array.isArray(v)) {
      fields[k] = { arrayValue: { values: v.map(item => (typeof item === 'string' ? { stringValue: item } : { stringValue: String(item) })) } };
    } else if (typeof v === 'string') {
      fields[k] = { stringValue: v };
    } else if (typeof v === 'number') {
      fields[k] = { integerValue: v };
    } else if (typeof v === 'boolean') {
      fields[k] = { booleanValue: v };
    } else {
      fields[k] = { stringValue: String(v) };
    }
  }
  return fields;
}

async function main() {
  console.log('🚀 Importing B2 Topic 5 (Futur mit werden) — 100 questions to moduleQuizQuestions\n');

  // Step 1: Create topic metadata document
  console.log('📚 Step 1: Creating topic document...');
  const topicDoc = {
    id: 'b2_06',
    subjectId: 'b2_06',
    module: 'B2',
    topicNumber: '4. Topic',
    topicName: data.topicName,
    totalQuestions: questions.length,
    version: 1,
    level: 'B2'
  };
  const topicResult = await firestorePost('topics', 'b2_06', toFields(topicDoc));
  console.log(`  topics/b2_06 → ${topicResult.status}`);
  if (topicResult.body.error) console.log(`  ⚠️  ${topicResult.body.error.message}`);

  // Step 2: Push individual questions to moduleQuizQuestions collection
  console.log(`\n📝 Step 2: Pushing ${questions.length} questions to moduleQuizQuestions...`);

  const batchSize = 100;
  let success = 0;
  let errors = 0;

  for (let i = 0; i < questions.length; i += batchSize) {
    const batch = questions.slice(i, i + batchSize);
    const promises = batch.map(q => firestorePost('moduleQuizQuestions', q.id, toFields(q)));
    const results = await Promise.all(promises);

    for (const r of results) {
      if (r.status === 200 || r.status === 201) {
        success++;
      } else {
        errors++;
        if (errors <= 3) {
          console.log(`  ⚠️  Error ${r.status}: ${JSON.stringify(r.body).slice(0, 100)}`);
        }
      }
    }
    process.stdout.write(`  Progress: ${Math.min(i + batchSize, questions.length)}/${questions.length}  \r`);
  }

  console.log(`\n`);
  console.log(`  ✅ Success: ${success}/${questions.length} questions`);
  if (errors > 0) console.log(`  ❌ Errors: ${errors}`);

  console.log(`\n🎉 Done! View in Firebase Console:`);
  console.log(`  https://console.firebase.google.com/project/${PROJECT_ID}/firestore`);
  console.log(`  → moduleQuizQuestions/b2_06`);
  console.log(`  → topics/b2_06`);
  console.log(`\n  App will receive update within 7 days, or run FirebaseSyncService.forceSync() to get it now.\n`);
}

main().catch(e => { console.error('Error:', e.message); process.exit(1); });
