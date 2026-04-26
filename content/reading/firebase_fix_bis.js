#!/usr/bin/env node
/**
 * Fix 3 wrong bis questions in Firebase:
 * - b2_01_bis_q003: konnektor bis->wenn, answer Bis->Wenn
 * - b2_01_bis_q008: konnektor bis->nachdem, answer Bis->Nachdem
 * - b2_01_bis_q010: konnektor bis->nachdem, answer Bis->Nachdem
 */

const https = require('https');
const PROJECT_ID = 'b2-deutsch-app';
const API_KEY = 'AIzaSyDHUwnlKx-ArzA5yZD4WhXI5sfACTzkedc';

function firestoreOp(method, path, body) {
  return new Promise((resolve, reject) => {
    const b = body ? JSON.stringify(body) : '';
    const opts = {
      hostname: 'firestore.googleapis.com',
      path: `/v1/projects/${PROJECT_ID}/databases/(default)/documents${path}?key=${API_KEY}`,
      method,
      headers: { 'Content-Type': 'application/json', 'Content-Length': Buffer.byteLength(b) }
    };
    const req = https.request(opts, res => {
      let d = '';
      res.on('data', c => d += c);
      res.on('end', () => resolve({ status: res.statusCode, body: d }));
    });
    req.on('error', reject);
    if (b) req.write(b);
    req.end();
  });
}

function toFields(obj) {
  const f = {};
  for (const [k, v] of Object.entries(obj)) {
    if (typeof v === 'string') f[k] = { stringValue: v };
    else if (typeof v === 'number') f[k] = { integerValue: v };
    else f[k] = { stringValue: String(v) };
  }
  return f;
}

const fixes = [
  {
    docId: 'b2_01_bis_q003',
    data: { id: 'b2_01_bis_q003', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'wenn', questionText: '___ ich Zeit habe, kann ich dir helfen.', options: ['Wahrend', 'Wenn', 'Bevor', 'Sobald'], correctAnswer: 'Wenn', explanation: '"Wenn" druckt eine Bedingung aus — wenn (when) ich Zeit habe, kann ich dir helfen.', difficulty: 'medium', level: 'B2' }
  },
  {
    docId: 'b2_01_bis_q008',
    data: { id: 'b2_01_bis_q008', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'nachdem', questionText: '___ alle Gaste gegangen waren, haben wir aufgeraumt.', options: ['Wahrend', 'Nachdem', 'Bevor', 'Sobald'], correctAnswer: 'Nachdem', explanation: '"Nachdem" zeigt, dass eine Handlung NACH einer anderen abgeschlossenen Handlung passiert.', difficulty: 'medium', level: 'B2' }
  },
  {
    docId: 'b2_01_bis_q010',
    data: { id: 'b2_01_bis_q010', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'nachdem', questionText: '___ das Spiel zu Ende war, haben wir geklatscht.', options: ['Wahrend', 'Nachdem', 'Bevor', 'Als'], correctAnswer: 'Nachdem', explanation: '"Nachdem" zeigt, dass eine Handlung NACH einer anderen passiert.', difficulty: 'medium', level: 'B2' }
  }
];

async function main() {
  for (const fix of fixes) {
    console.log(`\nFixing ${fix.docId}...`);
    const del = await firestoreOp('DELETE', `/moduleQuizQuestions/${fix.docId}`, null);
    console.log(`  Deleted: HTTP ${del.status}`);
    const create = await firestoreOp('POST', '/moduleQuizQuestions', { fields: toFields(fix.data) });
    console.log(`  Created: HTTP ${create.status}`);
  }
  console.log('\nAll 3 fixes applied!');
}

main().catch(console.error);
