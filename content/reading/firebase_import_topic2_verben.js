#!/usr/bin/env node
/**
 * Firebase Import: B2 Topic 2 — Verben und Ergänzungen (Reflexive Verben)
 * 10 Questions
 * Collection: moduleQuizQuestions
 * 
 * Run: node firebase_import_topic2_verben.js
 */

const https = require('https');
const PROJECT_ID = 'b2-deutsch-app';
const API_KEY = 'AIzaSyDHUwnlKx-ArzA5yZD4WhXI5sfACTzkedc';

const questions = [
  {
    id: 'b2_02_q001',
    module: 'B2',
    topicNumber: '2. Topic',
    topicName: 'Verben und Ergänzungen',
    subTopic: 'Reflexive Verben: Akkusativ',
    questionText: 'Ich muss ___ beeilen, sonst verpasse ich den Zug.',
    options: ['mir', 'mich', 'uns', 'dich'],
    correctAnswer: 'mich',
    explanation: '"sich beeilen" = to hurry. Akkusativ: ich → mich. "Ich muss mich beeilen."',
    difficulty: 'easy',
    level: 'B2'
  },
  {
    id: 'b2_02_q002',
    module: 'B2',
    topicNumber: '2. Topic',
    topicName: 'Verben und Ergänzungen',
    subTopic: 'Reflexive Verben: Akkusativ',
    questionText: 'Er hat ___ sehr über die Nachricht gefreut.',
    options: ['sich', 'mir', 'ihn', 'ihm'],
    correctAnswer: 'sich',
    explanation: '"sich freuen (über)" = to be happy (about). Reflexivpronomen im Akkusativ: er → sich.',
    difficulty: 'easy',
    level: 'B2'
  },
  {
    id: 'b2_02_q003',
    module: 'B2',
    topicNumber: '2. Topic',
    topicName: 'Verben und Ergänzungen',
    subTopic: 'Reflexive Verben: Akkusativ',
    questionText: 'Kannst du ___ bitte nicht so aufregen?',
    options: ['dir', 'dich', 'sich', 'mir'],
    correctAnswer: 'dich',
    explanation: '"sich aufregen" = to get excited/nervous. Akkusativ: du → dich. "Kannst du dich bitte nicht so aufregen?"',
    difficulty: 'easy',
    level: 'B2'
  },
  {
    id: 'b2_02_q004',
    module: 'B2',
    topicNumber: '2. Topic',
    topicName: 'Verben und Ergänzungen',
    subTopic: 'Reflexive Verben: Akkusativ',
    questionText: 'Wir haben ___ bei der Party sehr gut amüsiert.',
    options: ['uns', 'euch', 'sich', 'mir'],
    correctAnswer: 'uns',
    explanation: '"sich amüsieren" = to enjoy oneself. Akkusativ: wir → uns. "Wir haben uns bei der Party sehr gut amüsiert."',
    difficulty: 'medium',
    level: 'B2'
  },
  {
    id: 'b2_02_q005',
    module: 'B2',
    topicNumber: '2. Topic',
    topicName: 'Verben und Ergänzungen',
    subTopic: 'Reflexive Verben: Akkusativ',
    questionText: 'Sie (Pl.) müssen ___ beim Arzt anmelden.',
    options: ['sich', 'euch', 'uns', 'mir'],
    correctAnswer: 'uns',
    explanation: '"sich anmelden" = to register. Akkusativ: wir → uns. "Sie müssen sich beim Arzt anmelden." oder Plural: "Wir müssen uns anmelden."',
    difficulty: 'medium',
    level: 'B2'
  },
  {
    id: 'b2_02_q006',
    module: 'B2',
    topicNumber: '2. Topic',
    topicName: 'Verben und Ergänzungen',
    subTopic: 'Reflexive Verben: Akkusativ',
    questionText: 'Ich erinnere ___ nicht mehr an seinen Namen.',
    options: ['mir', 'mich', 'sich', 'uns'],
    correctAnswer: 'mich',
    explanation: '"sich erinnern (an)" = to remember. Akkusativ: ich → mich. "Ich erinnere mich nicht mehr an seinen Namen."',
    difficulty: 'medium',
    level: 'B2'
  },
  {
    id: 'b2_02_q007',
    module: 'B2',
    topicNumber: '2. Topic',
    topicName: 'Verben und Ergänzungen',
    subTopic: 'Reflexive Verben: Akkusativ',
    questionText: 'Das Kind hat ___ beim Spielen verletzt.',
    options: ['mir', 'sich', 'ihm', 'mich'],
    correctAnswer: 'sich',
    explanation: '"sich verletzen" = to injure oneself. Akkusativ: das Kind → sich. "Das Kind hat sich beim Spielen verletzt."',
    difficulty: 'medium',
    level: 'B2'
  },
  {
    id: 'b2_02_q008',
    module: 'B2',
    topicNumber: '2. Topic',
    topicName: 'Verben und Ergänzungen',
    subTopic: 'Reflexive Verben: Akkusativ',
    questionText: 'Hast du ___ schon für die Stelle beworben?',
    options: ['mir', 'dir', 'dich', 'sich'],
    correctAnswer: 'dich',
    explanation: '"sich bewerben (um)" = to apply (for). Akkusativ: du → dich. "Hast du dich schon für die Stelle beworben?"',
    difficulty: 'medium',
    level: 'B2'
  },
  {
    id: 'b2_02_q009',
    module: 'B2',
    topicNumber: '2. Topic',
    topicName: 'Verben und Ergänzungen',
    subTopic: 'Reflexive Verben: Akkusativ',
    questionText: 'Er konnte ___ nicht entscheiden, welche Option besser ist.',
    options: ['sich', 'ihm', 'mir', 'ihn'],
    correctAnswer: 'sich',
    explanation: '"sich entscheiden (für)" = to decide (on). Akkusativ: er → sich. "Er konnte sich nicht entscheiden."',
    difficulty: 'medium',
    level: 'B2'
  },
  {
    id: 'b2_02_q010',
    module: 'B2',
    topicNumber: '2. Topic',
    topicName: 'Verben und Ergänzungen',
    subTopic: 'Reflexive Verben: Akkusativ',
    questionText: 'Wir sollten ___ auf die Prüfung vorbereiten.',
    options: ['uns', 'sich', 'euch', 'mir'],
    correctAnswer: 'uns',
    explanation: '"sich vorbereiten (auf)" = to prepare (for). Akkusativ: wir → uns. "Wir sollten uns auf die Prüfung vorbereiten."',
    difficulty: 'medium',
    level: 'B2'
  }
];

function firestorePost(docId, fields) {
  return new Promise((resolve, reject) => {
    const body = JSON.stringify({ fields });
    const opts = {
      hostname: 'firestore.googleapis.com',
      path: `/v1/projects/${PROJECT_ID}/databases/(default)/documents/moduleQuizQuestions?documentId=${docId}&key=${API_KEY}`,
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Content-Length': Buffer.byteLength(body) }
    };
    const req = https.request(opts, res => {
      let d = '';
      res.on('data', c => d += c);
      res.on('end', () => resolve({ status: res.statusCode, docId }));
    });
    req.on('error', reject);
    req.write(body);
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

async function main() {
  console.log('🚀 Importing B2 Topic 2 — Verben und Ergänzungen (10 questions)\n');

  // First, create topic metadata
  console.log('📚 Creating topic document...');
  await firestorePost('b2_02', toFields({
    id: 'b2_02',
    module: 'B2',
    topicNumber: '2. Topic',
    topicName: 'Verben und Ergänzungen',
    subTopics: 'Reflexive Verben: Akkusativ, Reflexive Verben: Dativ, Verben mit Dativ, Verben mit Akkusativ und Dativ',
    questionCount: 10,
    type: 'module'
  }));
  console.log('  ✅ Topic b2_02 created\n');

  // Import questions
  console.log('📝 Importing 10 questions...\n');
  for (const q of questions) {
    const result = await firestorePost(q.id, toFields(q));
    const status = result.status === 200 || result.status === 409 ? '✅' : '⚠️';
    console.log(`  ${status} ${q.id}: ${q.questionText.substring(0, 50)}...`);
  }

  console.log('\n🎉 Done! 10 questions imported to moduleQuizQuestions');
  console.log('\n📊 View in Firebase Console:');
  console.log('  https://console.firebase.google.com/project/b2-deutsch-app/firestore');
}

main().catch(console.error);
