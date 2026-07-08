/**
 * import_and_sync.js — content/grammar/*.json -> moduleQuizQuestions (Step 2/3 of data-integrity fix)
 * =====================================================================================================
 * CORRECTED 2026-07-06: an earlier version of this fix retargeted this script at
 * `grammarQuizBank`, based on the assumption that's what the app reads live. That
 * assumption was WRONG — a full trace of every read/write call in
 * LocalQuestionBank.kt showed `getQuestionDetails()` only ever reads the bundled
 * APK asset file, and `ContentRepository.getGrammarQuestionsBySubject()` (which
 * reads grammarQuizBank) has zero callers anywhere in the app.
 *
 * The collection that's ACTUALLY read at runtime is `moduleQuizQuestions`, via
 * FirebaseSyncService.syncIfNeeded() (gated: only runs if >7 days since last sync,
 * and only picks up docs where `version` > the client's last-synced version). That
 * downloads into LocalQuestionBank.updateTopicFromFirebase(), which writes a
 * "{subjectId}_fb.json" cache file to internal storage via openFileOutput — and
 * (separately fixed, see LocalQuestionBank.kt) getQuestionDetails() now reads that
 * cache file first, falling back to the bundled asset file when absent.
 *
 * So the real, now fully wired-up pipeline is:
 *   content/grammar/<subjectId>.json (git, source of truth)
 *     -> this script -> Firestore moduleQuizQuestions/<subjectId>
 *     -> FirebaseSyncService (on next app open, if sync is due)
 *     -> LocalQuestionBank writes {subjectId}_fb.json
 *     -> LocalQuestionBank.getQuestionDetails() reads it
 *
 * moduleQuizQuestions doc shape (one doc per subjectId, matching what
 * FirebaseSyncService.syncIfNeeded() and LocalQuestionBank.saveQuestionsJson()
 * expect):
 *   { id, subjectId, topicName, totalQuestions, version (int), updatedAt,
 *     questions: [ { id, subjectId, type, questionText, options: [...] (real
 *     array, NOT pipe-delimited - this collection's schema is different from
 *     grammarQuizBank's), correctAnswer, explanation, difficulty, topicName } ] }
 *
 * VERSIONING: FirebaseSyncService keeps a single GLOBAL version counter on the
 * client (SharedPreferences), not per-topic. It queries
 * `.whereGreaterThan("version", currentVersion)` across the whole collection,
 * and after any non-empty sync just does `currentVersion + 1` client-side. That
 * means: every doc touched in a given sync run must be stamped with a version
 * STRICTLY GREATER than every version used in any previous run, or clients who
 * already synced past that point will silently never see the update. This
 * script computes newVersion = (max existing version in the collection) + 1 and
 * stamps every topic being synced in this run with that same value - simple and
 * safe as long as this script is the only writer.
 *
 * Usage:
 *   export GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json
 *   node scripts/import_and_sync.js --dry-run                # preview all topics
 *   node scripts/import_and_sync.js --dry-run c2_12           # preview one topic
 *   node scripts/import_and_sync.js c2_12                     # sync one topic
 *   node scripts/import_and_sync.js                           # sync ALL topics
 *
 * This script never deletes anything.
 */

const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');

const CONTENT_DIR = path.join(__dirname, '..', 'content', 'grammar');
const COLLECTION = 'moduleQuizQuestions';

const args = process.argv.slice(2);
const DRY_RUN = args.includes('--dry-run');
const subjectArgs = args.filter(a => a !== '--dry-run');

if (!process.env.GOOGLE_APPLICATION_CREDENTIALS) {
  console.error('❌ Set GOOGLE_APPLICATION_CREDENTIALS to your Firebase service account key path first.');
  process.exit(1);
}

const serviceAccount = JSON.parse(fs.readFileSync(process.env.GOOGLE_APPLICATION_CREDENTIALS, 'utf8'));
admin.initializeApp({ credential: admin.credential.cert(serviceAccount) });
const db = admin.firestore();
const FIELD = admin.firestore.FieldValue;

function toSyncQuestion(q, subjectId, topicName) {
  return {
    id: q.id,
    subjectId: q.subjectId || subjectId,
    type: q.type || 'multiple_choice',
    questionText: q.questionText,
    options: Array.isArray(q.options) ? q.options : (typeof q.options === 'string' ? q.options.split('|') : []),
    correctAnswer: q.correctAnswer,
    explanation: q.explanation || '',
    difficulty: q.difficulty || 'medium',
    topicName: q.topicName || topicName,
    // ROLES.md: AI-generated content is DRAFT until a human sets reviewed:true.
    // Default true for older content that predates this field (already shipped
    // without issue), so only explicitly-flagged new batches show as drafts.
    reviewed: q.reviewed !== undefined ? q.reviewed : true
  };
}

async function getNextVersion() {
  const snapshot = await db.collection(COLLECTION).select('version').get();
  let max = 0;
  snapshot.forEach(doc => {
    const v = doc.get('version');
    if (typeof v === 'number' && v > max) max = v;
  });
  return max + 1;
}

async function planTopic(subjectId) {
  const filePath = path.join(CONTENT_DIR, `${subjectId}.json`);
  if (!fs.existsSync(filePath)) {
    return { subjectId, error: `File not found: ${filePath}` };
  }
  const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));

  // A "planned, not yet authored" topic (questionCount 0 - shown in the app as
  // "Wird vorbereitet") has an empty or absent `questions` array. Must not
  // throw here - default to [] so its metadata still syncs cleanly.
  const topicName = data.topicName || subjectId;
  const rawQuestions = Array.isArray(data.questions) ? data.questions : [];

  const existingDoc = await db.collection(COLLECTION).doc(subjectId).get();
  const existingVersion = existingDoc.exists ? (existingDoc.get('version') || null) : null;
  const existingCount = existingDoc.exists ? (existingDoc.get('totalQuestions') || 0) : 0;

  const questions = rawQuestions.map(q => toSyncQuestion(q, subjectId, topicName));

  return {
    subjectId,
    topicName,
    localTotal: questions.length,
    existingVersion,
    existingCount,
    questions
  };
}

async function applyTopic(plan, newVersion) {
  const docData = {
    id: plan.subjectId,
    subjectId: plan.subjectId,
    topicName: plan.topicName,
    totalQuestions: plan.questions.length,
    version: newVersion,
    updatedAt: FIELD.serverTimestamp(),
    questions: plan.questions
  };
  await db.collection(COLLECTION).doc(plan.subjectId).set(docData);

  // Keep the `topics` collection accurate - this is what
  // FirebaseDataSource.getSubjectsByLevel() reads to build the subject list
  // dynamically (no hardcoded per-level lists in the app anymore).
  const level = plan.subjectId.split('_')[0].toUpperCase();
  await db.collection('topics').doc(plan.subjectId).set({
    id: plan.subjectId,
    level,
    name: plan.topicName,
    type: 'grammar',
    questionCount: plan.questions.length
  });
}

async function main() {
  const files = fs.readdirSync(CONTENT_DIR).filter(f => /^(a1|a2|b1|b2|c1|c2)_[0-9]+\.json$/i.test(f));
  const allSubjectIds = files.map(f => f.replace('.json', '')).sort();
  const targetIds = subjectArgs.length > 0 ? subjectArgs : allSubjectIds;

  console.log(DRY_RUN ? '🔍 DRY RUN — no writes will be made\n' : '🚀 Syncing content/grammar/*.json -> moduleQuizQuestions\n');

  const plans = [];
  for (const subjectId of targetIds) {
    const plan = await planTopic(subjectId);
    plans.push(plan);
    if (plan.error) {
      console.log(`  ❌ ${subjectId}: ${plan.error}`);
      continue;
    }
    console.log(`  ${subjectId} (${plan.topicName}): local=${plan.localTotal}, existing-in-firestore=${plan.existingCount} (version ${plan.existingVersion ?? 'none'})`);
  }

  if (DRY_RUN) {
    console.log('\n✅ Dry run complete. Re-run without --dry-run to apply.');
    return;
  }

  const newVersion = await getNextVersion();
  console.log(`\n📌 New version for this sync run: ${newVersion}`);

  for (const plan of plans) {
    if (plan.error) continue;
    console.log(`\n📦 Applying ${plan.subjectId}...`);
    await applyTopic(plan, newVersion);
    console.log(`  ✅ ${plan.subjectId}: ${plan.questions.length} questions written at version ${newVersion}`);
  }

  console.log('\n🎉 Sync complete. Clients will pick this up next time FirebaseSyncService.syncIfNeeded() runs (app open, >7 days since last sync, or forceSync()).');
}

main().catch(e => { console.error('Error:', e); process.exit(1); });
