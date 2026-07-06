/**
 * export_firestore_content.js — Firestore → git backup (Step 1 of data-integrity fix)
 * =====================================================================================
 * PROBLEM: content exists in Firestore (grammarQuizBank topics `_11`-`_15` for
 * A1/A2/B1/C1, plus other collections) that has NO local JSON file and NO git
 * history. If Firestore is ever lost/corrupted, that content is gone forever.
 *
 * This script exports every non-user Firestore collection into content/ so it is
 * captured in git. It does NOT touch app/src/main/assets/ (the APK-bundled source)
 * and does NOT write to Firestore — read-only, backup-only.
 *
 * Two output shapes:
 *   1. grammarQuizBank -> content/grammar/<subjectId>.json, reshaped to match the
 *      existing app/src/main/assets/<subjectId>.json schema (array options,
 *      topicName, description, tips, totalQuestions) so it could later replace/seed
 *      an asset file. Firestore's grammarQuizBank docs have NO description/tips/
 *      explanation fields, so those are left empty and the file is marked
 *      "_importedFromFirestore": true / "_needsContentReview": true — this is
 *      flagged, not silently pretended to be complete.
 *   2. Every other content collection -> content/firestore_backup/<collection>.json,
 *      a raw array of { id, ...data } docs (no reshaping, just a safety copy).
 *
 * User-data collections (users, userProgress, writingSubmissions, speakingSessions)
 * are deliberately EXCLUDED — this is a content backup, not a PII export.
 *
 * Usage:
 *   export GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json
 *   node scripts/export_firestore_content.js
 */

const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');

const EXCLUDED_COLLECTIONS = new Set(['users', 'userProgress', 'writingSubmissions', 'speakingSessions']);
const CONTENT_ROOT = path.join(__dirname, '..', 'content');
const GRAMMAR_DIR = path.join(CONTENT_ROOT, 'grammar');
const BACKUP_DIR = path.join(CONTENT_ROOT, 'firestore_backup');

if (!process.env.GOOGLE_APPLICATION_CREDENTIALS) {
  console.error('❌ Set GOOGLE_APPLICATION_CREDENTIALS to your Firebase service account key path first.');
  process.exit(1);
}

const serviceAccount = JSON.parse(fs.readFileSync(process.env.GOOGLE_APPLICATION_CREDENTIALS, 'utf8'));
admin.initializeApp({ credential: admin.credential.cert(serviceAccount) });
const db = admin.firestore();

function ensureDir(dir) {
  fs.mkdirSync(dir, { recursive: true });
}

async function exportGrammarQuizBank(topicsMeta) {
  console.log('\n📚 Exporting grammarQuizBank (reshaped to asset schema)...');
  const snapshot = await db.collection('grammarQuizBank').get();

  const bySubject = {};
  snapshot.forEach(doc => {
    const data = doc.data();
    const subjectId = data.subjectId;
    if (!subjectId) return; // skip malformed docs
    if (!bySubject[subjectId]) bySubject[subjectId] = [];
    bySubject[subjectId].push(data);
  });

  ensureDir(GRAMMAR_DIR);
  const summary = {}; // level -> { topics, questions, missingLocally: [] }

  for (const [subjectId, questions] of Object.entries(bySubject)) {
    const level = questions[0].level || subjectId.split('_')[0].toUpperCase();
    const meta = topicsMeta[subjectId];
    const topicName = meta ? meta.name : subjectId;

    questions.sort((a, b) => a.id.localeCompare(b.id));

    const reshaped = {
      subjectId,
      topicName,
      level,
      description: '',
      tips: [],
      _importedFromFirestore: true,
      _needsContentReview: true,
      _importNote: 'description/tips/explanation are not stored in grammarQuizBank and could not be recovered from Firestore. Needs human content review before this replaces/seeds an asset file.',
      questions: questions.map(q => ({
        id: q.id,
        subjectId: q.subjectId,
        topicName,
        questionText: q.questionText,
        options: typeof q.options === 'string' ? q.options.split('|') : (q.options || []),
        correctAnswer: q.correctAnswer,
        explanation: q.explanation || '',
        difficulty: q.difficulty || 'medium',
        type: q.type || 'multiple_choice'
      })),
      totalQuestions: questions.length
    };

    fs.writeFileSync(
      path.join(GRAMMAR_DIR, `${subjectId}.json`),
      JSON.stringify(reshaped, null, 2),
      'utf8'
    );

    const localAssetPath = path.join(__dirname, '..', 'app', 'src', 'main', 'assets', `${subjectId}.json`);
    const existsLocally = fs.existsSync(localAssetPath);

    if (!summary[level]) summary[level] = { topics: 0, questions: 0, missingLocally: [] };
    summary[level].topics += 1;
    summary[level].questions += questions.length;
    if (!existsLocally) summary[level].missingLocally.push(subjectId);
  }

  return summary;
}

async function exportRawCollection(collectionName) {
  const snapshot = await db.collection(collectionName).get();
  if (snapshot.empty) return 0;
  const docs = snapshot.docs.map(d => ({ id: d.id, ...d.data() }));
  ensureDir(BACKUP_DIR);
  fs.writeFileSync(
    path.join(BACKUP_DIR, `${collectionName}.json`),
    JSON.stringify(docs, null, 2),
    'utf8'
  );
  return docs.length;
}

async function main() {
  console.log('🔍 Discovering Firestore collections...');
  const collections = await db.listCollections();
  const names = collections.map(c => c.id).filter(id => !EXCLUDED_COLLECTIONS.has(id));
  console.log('Collections to back up:', names.join(', '));

  // Load `topics` collection first (subjectId -> name) to label grammarQuizBank exports.
  const topicsMeta = {};
  if (names.includes('topics')) {
    const topicsSnap = await db.collection('topics').get();
    topicsSnap.forEach(doc => { topicsMeta[doc.id] = doc.data(); });
  }

  const grammarSummary = names.includes('grammarQuizBank')
    ? await exportGrammarQuizBank(topicsMeta)
    : {};

  console.log('\n📦 Exporting remaining collections as raw backups...');
  const rawCounts = {};
  for (const name of names) {
    if (name === 'grammarQuizBank') continue; // already handled above
    const count = await exportRawCollection(name);
    rawCounts[name] = count;
    console.log(`  ${name}: ${count} docs -> content/firestore_backup/${name}.json`);
  }

  console.log('\n================ SUMMARY: grammarQuizBank by level ================');
  console.log('Level | Topics | Questions | Missing locally (no app/src/main/assets file)');
  for (const [level, s] of Object.entries(grammarSummary).sort()) {
    console.log(`${level.padEnd(5)} | ${String(s.topics).padEnd(6)} | ${String(s.questions).padEnd(9)} | ${s.missingLocally.join(', ') || '(none)'}`);
  }
  console.log('=====================================================================');
  console.log('\nRaw collection backups:', JSON.stringify(rawCounts, null, 2));
  console.log('\n✅ Export complete. Review content/grammar/*.json and content/firestore_backup/*.json before committing.');
}

main().catch(e => { console.error('Error:', e); process.exit(1); });
