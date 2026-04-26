#!/usr/bin/env node
/**
 * Firebase: Delete old B2_01 and B2_02 questions from grammarQuizBank
 * 
 * Run: node firebase_delete_old_konnektoren.js
 */

const https = require('https');

const PROJECT_ID = 'b2-deutsch-app';
const API_KEY = 'AIzaSyDHUwnlKx-ArzA5yZD4WhXI5sfACTzkedc';

function firestoreDelete(docPath) {
  return new Promise((resolve, reject) => {
    const options = {
      hostname: 'firestore.googleapis.com',
      path: `/v1/projects/${PROJECT_ID}/databases/(default)/documents/${docPath}?key=${API_KEY}`,
      method: 'DELETE',
      headers: {}
    };
    const req = https.request(options, res => {
      let d = '';
      res.on('data', c => d += c);
      res.on('end', () => resolve({ status: res.statusCode, body: d }));
    });
    req.on('error', reject);
    req.end();
  });
}

// Get all docs matching subjectId b2_01 or b2_02
function firestoreQuery(collection, fieldPath, op, value) {
  return new Promise((resolve, reject) => {
    const body = JSON.stringify({
      structuredQuery: {
        from: [{ collectionId: collection }],
        where: { fieldFilter: { field: { fieldPath }, op, value: { stringValue: value } } }
      }
    });
    const options = {
      hostname: 'firestore.googleapis.com',
      path: `/v1/projects/${PROJECT_ID}/databases/(default)/documents:runQuery?key=${API_KEY}`,
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Content-Length': Buffer.byteLength(body) }
    };
    const req = https.request(options, res => {
      let d = '';
      res.on('data', c => d += c);
      res.on('end', () => {
        try { resolve(JSON.parse(d)); }
        catch { resolve([]); }
      });
    });
    req.on('error', reject);
    req.write(body);
    req.end();
  });
}

async function main() {
  console.log('🗑️  Deleting old B2_01 and B2_02 questions from grammarQuizBank...\n');

  const oldIds = ['b2_01', 'b2_02'];
  let totalDeleted = 0;

  for (const subjectId of oldIds) {
    console.log(`  Deleting ${subjectId}...`);
    const results = await firestoreQuery('grammarQuizBank', 'subjectId', 'EQUAL', subjectId);
    const docs = results.filter(r => r.document);
    
    console.log(`  Found ${docs.length} documents for ${subjectId}`);
    
    for (const doc of docs) {
      const path = doc.document.name.split('/').pop();
      const result = await firestoreDelete(`grammarQuizBank/${path}`);
      if (result.status === 200 || result.status === 404) {
        process.stdout.write('✓');
        totalDeleted++;
      } else {
        process.stdout.write(`✗(${result.status})`);
      }
    }
    console.log('');
  }

  console.log(`\n✅ Deleted ${totalDeleted} old questions`);
}

main().catch(console.error);
