/**
 * delete_orphaned_module_quiz_questions.js — DESTRUCTIVE, run manually only
 * ===========================================================================
 * `moduleQuizQuestions` was the Firestore collection the OLD (buggy) version of
 * import_and_sync.js wrote to. Nothing in the app reads this collection — the
 * app reads `grammarQuizBank` instead (see FirebaseDataSource.kt). It is dead
 * data (408 docs as of 2026-07-06).
 *
 * This script deletes the entire `moduleQuizQuestions` collection.
 *
 * SAFETY:
 *   - A full backup already exists in git at
 *     content/firestore_backup/moduleQuizQuestions.json (see the Step 1
 *     data-integrity commit). Do not run this script if that backup is
 *     missing or unverified.
 *   - This script is NEVER invoked automatically by import_and_sync.js or any
 *     other script. Run it yourself, deliberately, when you're ready.
 *   - Requires an explicit --yes-delete-moduleQuizQuestions flag; running
 *     without it only prints what would be deleted.
 *
 * Usage:
 *   export GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json
 *   node scripts/delete_orphaned_module_quiz_questions.js                          # dry run (prints count only)
 *   node scripts/delete_orphaned_module_quiz_questions.js --yes-delete-moduleQuizQuestions   # actually deletes
 */

const admin = require('firebase-admin');
const fs = require('fs');

const CONFIRM_FLAG = '--yes-delete-moduleQuizQuestions';
const confirmed = process.argv.includes(CONFIRM_FLAG);

if (!process.env.GOOGLE_APPLICATION_CREDENTIALS) {
  console.error('❌ Set GOOGLE_APPLICATION_CREDENTIALS to your Firebase service account key path first.');
  process.exit(1);
}

const serviceAccount = JSON.parse(fs.readFileSync(process.env.GOOGLE_APPLICATION_CREDENTIALS, 'utf8'));
admin.initializeApp({ credential: admin.credential.cert(serviceAccount) });
const db = admin.firestore();

async function main() {
  const snapshot = await db.collection('moduleQuizQuestions').get();
  console.log(`Found ${snapshot.size} docs in moduleQuizQuestions.`);

  if (!confirmed) {
    console.log(`\nDry run only. Re-run with ${CONFIRM_FLAG} to actually delete.`);
    console.log('Make sure content/firestore_backup/moduleQuizQuestions.json is committed first.');
    return;
  }

  const batchSize = 400;
  const docs = snapshot.docs;
  for (let i = 0; i < docs.length; i += batchSize) {
    const batch = db.batch();
    docs.slice(i, i + batchSize).forEach(d => batch.delete(d.ref));
    await batch.commit();
  }
  console.log(`✅ Deleted ${docs.length} docs from moduleQuizQuestions.`);
}

main().catch(e => { console.error('Error:', e); process.exit(1); });
