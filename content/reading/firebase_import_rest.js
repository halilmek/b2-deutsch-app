#!/usr/bin/env node
/**
 * Firebase Import: ALL LEVELS via REST API
 * 8300 questions across 83 topics (A1, A2, B1, B2, C1)
 * Uses Firestore REST API - no service account needed
 * 
 * Run: node firebase_import_rest.js
 */

const https = require('https');

const PROJECT_ID = 'b2-deutsch-app';
const BASE_URL = `firestore.googleapis.com/v1/projects/${PROJECT_ID}/databases/(default)/documents`;
const API_KEY = 'AIzaSyCbDjasex5EGlz94IUFRGzzspksTyr0OCA';

// Load question bank
const fs = require('fs');
const path = require('path');
const data = JSON.parse(
  fs.readFileSync(path.join(__dirname, 'all_levels_100_questions.json'), 'utf-8')
);

const { totalQuestions, topics, questionBank } = data;
console.log(`🚀 Firebase import: ${totalQuestions} questions\n`);

// Helper: make Firestore REST API call
function firestoreDocCreate(collection, docId, fields) {
  const body = JSON.stringify({ fields: toFirestoreFields(fields) });
  return new Promise((resolve, reject) => {
    const options = {
      hostname: BASE_URL,
      path: `/${collection}?documentId=${docId}&key=${API_KEY}`,
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Content-Length': Buffer.byteLength(body) }
    };
    const req = https.request(options, res => {
      let d = '';
      res.on('data', c => d += c);
      res.on('end', () => {
        if (res.statusCode >= 400) {
          console.log(`  ⚠️ ${collection}/${docId}: HTTP ${res.statusCode}`);
          reject(new Error(`HTTP ${res.statusCode}`));
        } else {
          resolve();
        }
      });
    });
    req.on('error', reject);
    req.write(body);
    req.end();
  });
}

// Convert to Firestore field format
function toFirestoreFields(obj) {
  const fields = {};
  for (const [k, v] of Object.entries(obj)) {
    if (typeof v === 'string') fields[k] = { stringValue: v };
    else if (typeof v === 'number') fields[k] = { integerValue: v };
    else if (typeof v === 'boolean') fields[k] = { booleanValue: v };
    else if (Array.isArray(v)) fields[k] = { arrayValue: { values: v.map(x => ({ stringValue: String(x) })) } };
    else fields[k] = { stringValue: String(v) };
  }
  return fields;
}

async function importTopics() {
  console.log('📚 Step 1: Importing topic metadata...');
  let count = 0;
  for (const [topicId, meta] of Object.entries(topics)) {
    await firestoreDocCreate('topics', topicId, {
      id: topicId,
      name: meta.name,
      level: meta.level,
      questionCount: meta.count,
      type: 'grammar',
      displayOrder: count++
    });
    process.stdout.write(`  ${topicId} ✓\n`);
  }
  console.log(`  ✅ ${count} topics imported\n`);
}

async function importQuestions() {
  console.log('📝 Step 2: Importing questions (8300 total)...\n');
  
  const levelOrder = ['A1', 'A2', 'B1', 'B2', 'C1'];
  let processed = 0;
  
  for (const level of levelOrder) {
    const levelQuestions = questionBank.filter(q => q.subjectId.startsWith(level.toLowerCase()));
    console.log(`  [${level}] ${levelQuestions.length} questions...`);
    
    for (const q of levelQuestions) {
      try {
        await firestoreDocCreate('grammarQuizBank', q.id, {
          id: q.id,
          subjectId: q.subjectId,
          type: q.type,
          questionText: q.questionText,
          options: q.options.join('|'),
          correctAnswer: q.correctAnswer,
          explanation: q.explanation,
          difficulty: q.difficulty,
          topicName: q.topicName,
          level: level
        });
        processed++;
        if (processed % 100 === 0) process.stdout.write(`  ${processed}/${totalQuestions}\n`);
      } catch (e) {
        // Skip duplicates (already imported)
      }
    }
    console.log(`  [${level}] ✅ done`);
  }
  
  console.log(`\n  ✅ ${processed} questions imported`);
}

async function main() {
  try {
    await importTopics();
    await importQuestions();
    console.log('\n🎉 Firebase import complete!');
    console.log('\n📊 View data at:');
    console.log('  Topics: https://console.firebase.google.com/project/b2-deutsch-app/firestore');
    console.log('  Questions: same link above, scroll to grammarQuizBank collection');
    process.exit(0);
  } catch (err) {
    console.error('❌ Error:', err.message);
    process.exit(1);
  }
}

main();