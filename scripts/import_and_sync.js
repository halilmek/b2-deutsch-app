/**
 * import_and_sync.js — content/grammar/*.json -> grammarQuizBank (Step 2 of data-integrity fix)
 * ================================================================================================
 * PREVIOUS BUG: this script used to write to Firestore collection `moduleQuizQuestions`,
 * which nothing in the app reads. The live app reads grammar questions from
 * `grammarQuizBank` via FirebaseDataSource.getGrammarQuestionsBySubject(). Every
 * "synced" claim based on the old script was Firestore-unverified.
 *
 * NEW PIPELINE: content/grammar/<subjectId>.json (git, source of truth) -> this
 * script -> grammarQuizBank. GitHub asset-file pushing via REST API has been
 * removed entirely — commit content/ changes with normal `git commit` + `git push`
 * like everything else in this repo; don't maintain a second parallel content path.
 *
 * grammarQuizBank doc shape (matches what FirebaseDataSource.kt actually reads):
 *   { id, subjectId, level, questionText, options: "opt1|opt2|opt3|opt4" (STRING,
 *     pipe-delimited, not array), correctAnswer, difficulty, type }
 * NOTE: no `explanation` field yet — that's a separate, deliberate follow-up
 * (Step 3 of the data-integrity fix), not bundled into this script by default.
 *
 * Also writes/updates a lightweight `topics/<subjectId>` doc (name, level, type,
 * questionCount) so the `topics` collection stays accurate — currently dead code
 * in the app (FirebaseDataSource.getSubjectsByLevel() is hardcoded to fail), but
 * this is what Step 4 (killing hardcoded subject lists) will need to read from.
 *
 * Usage:
 *   export GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json
 *   node scripts/import_and_sync.js --dry-run                # preview all topics
 *   node scripts/import_and_sync.js --dry-run c2_12           # preview one topic
 *   node scripts/import_and_sync.js c2_12                     # sync one topic
 *   node scripts/import_and_sync.js                           # sync ALL topics
 *
 * This script never deletes anything. It does not touch the orphaned
 * `moduleQuizQuestions` collection — see scripts/delete_orphaned_module_quiz_questions.js
 * for that, which must be run separately and explicitly, never automatically.
 */

const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');

const CONTENT_DIR = path.join(__dirname, '..', 'content', 'grammar');

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

function toFirestoreQuestion(q, subjectId, level) {
  return {
    id: q.id,
    subjectId: q.subjectId || subjectId,
    level: q.level || level,
    questionText: q.questionText,
    options: Array.isArray(q.options) ? q.options.join('|') : q.options,
    correctAnswer: q.correctAnswer,
    difficulty: q.difficulty || 'medium',
    type: q.type || 'multiple_choice'
  };
}

async function planTopic(subjectId) {
  const filePath = path.join(CONTENT_DIR, `${subjectId}.json`);
  if (!fs.existsSync(filePath)) {
    return { subjectId, error: `File not found: ${filePath}` };
  }
  const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));
  const level = data.level || subjectId.split('_')[0].toUpperCase();

  const existingSnapshot = await db.collection('grammarQuizBank')
    .where('subjectId', '==', subjectId)
    .select()
    .get();
  const existingIds = new Set(existingSnapshot.docs.map(d => d.id));

  const localQuestions = data.questions.map(q => toFirestoreQuestion(q, subjectId, level));
  const localIds = new Set(localQuestions.map(q => q.id));

  const toCreate = localQuestions.filter(q => !existingIds.has(q.id));
  const toUpdate = localQuestions.filter(q => existingIds.has(q.id));
  const staleInFirestore = [...existingIds].filter(id => !localIds.has(id));

  return {
    subjectId,
    level,
    topicName: data.topicName,
    localTotal: localQuestions.length,
    firestoreTotal: existingIds.size,
    toCreate: toCreate.length,
    toUpdate: toUpdate.length,
    staleInFirestore, // present in Firestore but not in local file - NOT deleted, just reported
    questions: localQuestions,
    topicDoc: {
      id: subjectId,
      level,
      name: data.topicName,
      type: 'grammar',
      questionCount: localQuestions.length
    }
  };
}

async function applyTopic(plan) {
  const batchSize = 400;
  for (let i = 0; i < plan.questions.length; i += batchSize) {
    const batch = db.batch();
    plan.questions.slice(i, i + batchSize).forEach(q => {
      batch.set(db.collection('grammarQuizBank').doc(q.id), q, { merge: true });
    });
    await batch.commit();
  }
  await db.collection('topics').doc(plan.subjectId).set(plan.topicDoc, { merge: true });
}

async function main() {
  const files = fs.readdirSync(CONTENT_DIR).filter(f => /^(a1|a2|b1|b2|c1|c2)_[0-9]+\.json$/i.test(f));
  const allSubjectIds = files.map(f => f.replace('.json', '')).sort();
  const targetIds = subjectArgs.length > 0 ? subjectArgs : allSubjectIds;

  console.log(DRY_RUN ? '🔍 DRY RUN — no writes will be made\n' : '🚀 Syncing content/grammar/*.json -> grammarQuizBank\n');

  const plans = [];
  for (const subjectId of targetIds) {
    const plan = await planTopic(subjectId);
    plans.push(plan);
    if (plan.error) {
      console.log(`  ❌ ${subjectId}: ${plan.error}`);
      continue;
    }
    console.log(`  ${subjectId} (${plan.topicName}): local=${plan.localTotal}, firestore=${plan.firestoreTotal}, create=${plan.toCreate}, update=${plan.toUpdate}${plan.staleInFirestore.length ? `, stale-in-firestore=${plan.staleInFirestore.length} (not deleted)` : ''}`);
  }

  if (DRY_RUN) {
    console.log('\n✅ Dry run complete. Re-run without --dry-run to apply.');
    return;
  }

  for (const plan of plans) {
    if (plan.error) continue;
    console.log(`\n📦 Applying ${plan.subjectId}...`);
    await applyTopic(plan);
    console.log(`  ✅ ${plan.subjectId}: ${plan.questions.length} questions written, topics/${plan.subjectId} updated`);
  }

  console.log('\n🎉 Sync complete.');
}

main().catch(e => { console.error('Error:', e); process.exit(1); });
