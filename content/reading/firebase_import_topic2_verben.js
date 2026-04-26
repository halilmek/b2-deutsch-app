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
  // === AKKUSATIV ===
  { id: 'b2_02_q001', module: 'B2', topicNumber: '2. Topic', topicName: 'Verben und Erg\u00e4nzungen', subTopic: 'Reflexive Verben: Akkusativ', questionText: 'Ich muss ___ beeilen, sonst verpasse ich den Zug.', options: ['mir', 'mich', 'uns', 'dich'], correctAnswer: 'mich', explanation: '"sich beeilen" = to hurry. Akkusativ: ich \u2192 mich. "Ich muss mich beeilen."', difficulty: 'easy', level: 'B2' },
  { id: 'b2_02_q002', module: 'B2', topicNumber: '2. Topic', topicName: 'Verben und Erg\u00e4nzungen', subTopic: 'Reflexive Verben: Akkusativ', questionText: 'Er hat ___ sehr \u00fcber die Nachricht gefreut.', options: ['sich', 'mir', 'ihn', 'ihm'], correctAnswer: 'sich', explanation: '"sich freuen (\u00fcber)" = to be happy (about). Reflexivpronomen im Akkusativ: er \u2192 sich.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_02_q003', module: 'B2', topicNumber: '2. Topic', topicName: 'Verben und Erg\u00e4nzungen', subTopic: 'Reflexive Verben: Akkusativ', questionText: 'Kannst du ___ bitte nicht so aufregen?', options: ['dir', 'dich', 'sich', 'mir'], correctAnswer: 'dich', explanation: '"sich aufregen" = to get excited/nervous. Akkusativ: du \u2192 dich.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_02_q004', module: 'B2', topicNumber: '2. Topic', topicName: 'Verben und Erg\u00e4nzungen', subTopic: 'Reflexive Verben: Akkusativ', questionText: 'Wir haben ___ bei der Party sehr gut am\u00fasiert.', options: ['uns', 'euch', 'sich', 'mir'], correctAnswer: 'uns', explanation: '"sich am\u00fcsieren" = to enjoy oneself. Akkusativ: wir \u2192 uns.', difficulty: 'medium', level: 'B2' },
  { id: 'b2_02_q005', module: 'B2', topicNumber: '2. Topic', topicName: 'Verben und Erg\u00e4nzungen', subTopic: 'Reflexive Verben: Akkusativ', questionText: 'Sie m\u00fcssen ___ beim Arzt anmelden.', options: ['sich', 'euch', 'uns', 'mir'], correctAnswer: 'uns', explanation: '"sich anmelden" = to register. Akkusativ: wir \u2192 uns. "Sie m\u00fcssen sich anmelden."', difficulty: 'medium', level: 'B2' },
  { id: 'b2_02_q006', module: 'B2', topicNumber: '2. Topic', topicName: 'Verben und Erg\u00e4nzungen', subTopic: 'Reflexive Verben: Akkusativ', questionText: 'Ich erinnere ___ nicht mehr an seinen Namen.', options: ['mir', 'mich', 'sich', 'uns'], correctAnswer: 'mich', explanation: '"sich erinnern (an)" = to remember. Akkusativ: ich \u2192 mich.', difficulty: 'medium', level: 'B2' },
  { id: 'b2_02_q007', module: 'B2', topicNumber: '2. Topic', topicName: 'Verben und Erg\u00e4nzungen', subTopic: 'Reflexive Verben: Akkusativ', questionText: 'Das Kind hat ___ beim Spielen verletzt.', options: ['mir', 'sich', 'ihm', 'mich'], correctAnswer: 'sich', explanation: '"sich verletzen" = to injure oneself. Akkusativ: das Kind \u2192 sich.', difficulty: 'medium', level: 'B2' },
  { id: 'b2_02_q008', module: 'B2', topicNumber: '2. Topic', topicName: 'Verben und Erg\u00e4nzungen', subTopic: 'Reflexive Verben: Akkusativ', questionText: 'Hast du ___ schon f\u00fcr die Stelle beworben?', options: ['mir', 'dir', 'dich', 'sich'], correctAnswer: 'dich', explanation: '"sich bewerben (um)" = to apply (for). Akkusativ: du \u2192 dich.', difficulty: 'medium', level: 'B2' },
  { id: 'b2_02_q009', module: 'B2', topicNumber: '2. Topic', topicName: 'Verben und Erg\u00e4nzungen', subTopic: 'Reflexive Verben: Akkusativ', questionText: 'Er konnte ___ nicht entscheiden, welche Option besser ist.', options: ['sich', 'ihm', 'mir', 'ihn'], correctAnswer: 'sich', explanation: '"sich entscheiden (f\u00fcr)" = to decide (on). Akkusativ: er \u2192 sich.', difficulty: 'medium', level: 'B2' },
  { id: 'b2_02_q010', module: 'B2', topicNumber: '2. Topic', topicName: 'Verben und Erg\u00e4nzungen', subTopic: 'Reflexive Verben: Akkusativ', questionText: 'Wir sollten ___ auf die Pr\u00fcfung vorbereiten.', options: ['uns', 'sich', 'euch', 'mir'], correctAnswer: 'uns', explanation: '"sich vorbereiten (auf)" = to prepare (for). Akkusativ: wir \u2192 uns.', difficulty: 'medium', level: 'B2' },
  // === DATIV ===
  { id: 'b2_02_q011', module: 'B2', topicNumber: '2. Topic', topicName: 'Verben und Erg\u00e4nzungen', subTopic: 'Reflexive Verben: Dativ', questionText: 'Ich muss ___ die Haare waschen.', options: ['mich', 'mir', 'sich', 'uns'], correctAnswer: 'mir', explanation: '"sich (Dat.) + Akkusativobjekt": Ich wasche mir die Haare. Both a Dativ pronoun AND an Akkusativ object exist.', difficulty: 'medium', level: 'B2' },
  { id: 'b2_02_q012', module: 'B2', topicNumber: '2. Topic', topicName: 'Verben und Erg\u00e4nzungen', subTopic: 'Reflexive Verben: Dativ', questionText: 'Er hat ___ einen neuen Laptop gekauft.', options: ['ihn', 'sich', 'ihm', 'mir'], correctAnswer: 'sich', explanation: '"sich (Dat.) + Akkusativobjekt": Er kauft sich einen Laptop. Dativ reflexive + Akkusativ object.', difficulty: 'medium', level: 'B2' },
  { id: 'b2_02_q013', module: 'B2', topicNumber: '2. Topic', topicName: 'Verben und Erg\u00e4nzungen', subTopic: 'Reflexive Verben: Dativ', questionText: 'Kannst du ___ das vorstellen?', options: ['dich', 'dir', 'sich', 'mir'], correctAnswer: 'dir', explanation: '"sich (Dat.) vorstellen": imagination/role-play. Du \u2192 dir. "Kannst du dir das vorstellen?"', difficulty: 'medium', level: 'B2' },
  { id: 'b2_02_q014', module: 'B2', topicNumber: '2. Topic', topicName: 'Verben und Erg\u00e4nzungen', subTopic: 'Reflexive Verben: Dativ', questionText: 'Wir haben ___ gedacht, das w\u00e4re einfacher.', options: ['uns', 'sich', 'euch', 'mir'], correctAnswer: 'uns', explanation: '"sich (Dat.) denken": to think/to have an opinion. Wir \u2192 uns. "Wir haben uns gedacht..."', difficulty: 'medium', level: 'B2' },
  { id: 'b2_02_q015', module: 'B2', topicNumber: '2. Topic', topicName: 'Verben und Erg\u00e4nzungen', subTopic: 'Reflexive Verben: Dativ', questionText: 'Sie hat ___ die H\u00e4nde gewaschen.', options: ['sich', 'ihr', 'sie', 'ihm'], correctAnswer: 'sich', explanation: '"sich (Dat.) + Akkusativobjekt": Sie w\u00e4scht sich die H\u00e4nde. Dativ reflexive + Akkusativ object.', difficulty: 'medium', level: 'B2' },
  { id: 'b2_02_q016', module: 'B2', topicNumber: '2. Topic', topicName: 'Verben und Erg\u00e4nzungen', subTopic: 'Reflexive Verben: Dativ', questionText: 'Ich m\u00f6chte ___ etwas merken, was er gesagt hat.', options: ['mich', 'mir', 'sich', 'dich'], correctAnswer: 'mir', explanation: '"sich (Dat.) merken": to remember/keep in mind. Ich \u2192 mir. "Ich merke mir etwas."', difficulty: 'medium', level: 'B2' },
  { id: 'b2_02_q017', module: 'B2', topicNumber: '2. Topic', topicName: 'Verben und Erg\u00e4nzungen', subTopic: 'Reflexive Verben: Dativ', questionText: 'Du solltest ___ das gut \u00fcberlegen, bevor du antwortest.', options: ['dich', 'dir', 'sich', 'mir'], correctAnswer: 'dir', explanation: '"sich (Dat.) \u00fcberlegen": to think carefully/consider. Du \u2192 dir. "Du solltest dir das gut \u00fcberlegen."', difficulty: 'medium', level: 'B2' },
  { id: 'b2_02_q018', module: 'B2', topicNumber: '2. Topic', topicName: 'Verben und Erg\u00e4nzungen', subTopic: 'Reflexive Verben: Dativ', questionText: 'Er hat ___ die neue Ausstellung angesehen.', options: ['sich', 'ihm', 'ihn', 'mir'], correctAnswer: 'sich', explanation: '"sich (Dat.) ansehen": to look at/examine. Er \u2192 sich. "Er sieht sich die Ausstellung an."', difficulty: 'medium', level: 'B2' },
  { id: 'b2_02_q019', module: 'B2', topicNumber: '2. Topic', topicName: 'Verben und Erg\u00e4nzungen', subTopic: 'Reflexive Verben: Dativ', questionText: 'Ich leihe ___ kein Geld mehr von ihm.', options: ['mir', 'mich', 'sich', 'uns'], correctAnswer: 'mir', explanation: '"sich (Dat.) leihen": to borrow. Ich \u2192 mir. "Ich leihe mir Geld."', difficulty: 'medium', level: 'B2' },
  { id: 'b2_02_q020', module: 'B2', topicNumber: '2. Topic', topicName: 'Verben und Erg\u00e4nzungen', subTopic: 'Reflexive Verben: Dativ', questionText: 'Haben Sie ___ schon etwas vorgenommen f\u00fcr heute?', options: ['sich', 'Ihnen', 'ihr', 'mich'], correctAnswer: 'sich', explanation: '"sich (Dat.) vornehmen": to plan/to resolve to do something. Sie (formal) \u2192 sich.', difficulty: 'medium', level: 'B2' }
,
  { id: 'b2_02_q021', module: 'B2', topicNumber: '2. Topic', topicName: 'Verben und Erg\u00e4nzungen', subTopic: 'Verben mit Pr\u00e4positionen', questionText: 'Sie wartet schon seit einer Stunde ___ ihren Freund.', options: ['auf', 'f\u00fcr', 'an', '\u00fcber'], correctAnswer: 'auf', explanation: '"warten auf + Akkusativ": to wait for. "Sie wartet auf ihren Freund."', difficulty: 'easy', level: 'B2' },
  { id: 'b2_02_q022', module: 'B2', topicNumber: '2. Topic', topicName: 'Verben und Erg\u00e4nzungen', subTopic: 'Verben mit Pr\u00e4positionen', questionText: 'Er interessiert sich sehr ___ klassische Musik.', options: ['an', 'f\u00fcr', 'mit', '\u00fcber'], correctAnswer: 'f\u00fcr', explanation: '"sich interessieren f\u00fcr + Akkusativ": to be interested in. "Er interessiert sich f\u00fcr klassische Musik."', difficulty: 'easy', level: 'B2' },
  { id: 'b2_02_q023', module: 'B2', topicNumber: '2. Topic', topicName: 'Verben und Erg\u00e4nzungen', subTopic: 'Verben mit Pr\u00e4positionen', questionText: 'Wir haben uns ___ dem Ergebnis gefreut.', options: ['f\u00fcr', 'an', '\u00fcber', 'von'], correctAnswer: '\u00fcber', explanation: '"sich freuen \u00fcber + Akkusativ": to be happy about. "Wir haben uns \u00fcber das Ergebnis gefreut."', difficulty: 'easy', level: 'B2' },
  { id: 'b2_02_q024', module: 'B2', topicNumber: '2. Topic', topicName: 'Verben und Erg\u00e4nzungen', subTopic: 'Verben mit Pr\u00e4positionen', questionText: 'Sie tr\u00e4umt ___ einer Reise nach Japan.', options: ['\u00fcber', 'an', 'von', 'f\u00fcr'], correctAnswer: 'von', explanation: '"tr\u00e4umen von + Dativ": to dream of. "Sie tr\u00e4umt von einer Reise nach Japan."', difficulty: 'easy', level: 'B2' },
  { id: 'b2_02_q025', module: 'B2', topicNumber: '2. Topic', topicName: 'Verben und Erg\u00e4nzungen', subTopic: 'Verben mit Pr\u00e4positionen', questionText: 'Er hat sich ___ seinem alten Freund gestritten.', options: ['mit', '\u00fcber', 'an', 'f\u00fcr'], correctAnswer: 'mit', explanation: '"sich streiten mit + Dativ": to argue with. "Er hat sich mit seinem alten Freund gestritten."', difficulty: 'medium', level: 'B2' },
  { id: 'b2_02_q026', module: 'B2', topicNumber: '2. Topic', topicName: 'Verben und Erg\u00e4nzungen', subTopic: 'Verben mit Pr\u00e4positionen', questionText: 'Ich bitte dich ___ deine Hilfe.', options: ['f\u00fcr', 'an', 'um', 'von'], correctAnswer: 'um', explanation: '"bitten um + Akkusativ": to ask for. "Ich bitte dich um deine Hilfe."', difficulty: 'medium', level: 'B2' },
  { id: 'b2_02_q027', module: 'B2', topicNumber: '2. Topic', topicName: 'Verben und Erg\u00e4nzungen', subTopic: 'Verben mit Pr\u00e4positionen', questionText: 'Sie hat sich ___ ihren Fehler entschuldigt.', options: ['\u00fcber', 'f\u00fcr', 'an', 'von'], correctAnswer: 'f\u00fcr', explanation: '"sich entschuldigen f\u00fcr + Akkusativ": to apologize for. "Sie hat sich f\u00fcr ihren Fehler entschuldigt."', difficulty: 'medium', level: 'B2' },
  { id: 'b2_02_q028', module: 'B2', topicNumber: '2. Topic', topicName: 'Verben und Erg\u00e4nzungen', subTopic: 'Verben mit Pr\u00e4positionen', questionText: 'Er denkt oft ___ seine Kindheit.', options: ['\u00fcber', 'von', 'an', 'f\u00fcr'], correctAnswer: 'an', explanation: '"denken an + Akkusativ": to think about. "Er denkt oft an seine Kindheit."', difficulty: 'easy', level: 'B2' },
  { id: 'b2_02_q029', module: 'B2', topicNumber: '2. Topic', topicName: 'Verben und Erg\u00e4nzungen', subTopic: 'Verben mit Pr\u00e4positionen', questionText: 'Ich verlasse mich ___ dich.', options: ['an', 'auf', 'mit', '\u00fcber'], correctAnswer: 'auf', explanation: '"sich verlassen auf + Akkusativ": to rely on. "Ich verlasse mich auf dich."', difficulty: 'easy', level: 'B2' },
  { id: 'b2_02_q030', module: 'B2', topicNumber: '2. Topic', topicName: 'Verben und Erg\u00e4nzungen', subTopic: 'Verben mit Pr\u00e4positionen', questionText: 'Sie hat sich ___ dem langen Weg erholt.', options: ['von', '\u00fcber', 'f\u00fcr', 'an'], correctAnswer: 'von', explanation: '"sich erholen von + Dativ": to recover from. "Sie hat sich von dem langen Weg erholt."', difficulty: 'medium', level: 'B2' }

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
    subTopics: 'Reflexive Verben: Akkusativ (Q1-10), Reflexive Verben: Dativ (Q11-20), Verben mit Präpositionen (Q21-30)',
    questionCount: 30,
    type: 'module'
  }));
  console.log('  ✅ Topic b2_02 created\n');

  // Import questions
  console.log('📝 Importing 30 questions...\n');
  for (const q of questions) {
    const result = await firestorePost(q.id, toFields(q));
    const status = result.status === 200 || result.status === 409 ? '✅' : '⚠️';
    console.log(`  ${status} ${q.id}: ${q.questionText.substring(0, 50)}...`);
  }

  console.log('\n🎉 Done! 30 questions imported to moduleQuizQuestions');
  console.log('\n📊 View in Firebase Console:');
  console.log('  https://console.firebase.google.com/project/b2-deutsch-app/firestore');
}

main().catch(console.error);
