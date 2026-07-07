/**
 * sync_vocabulary.js — content/vocabulary/*.json -> Firestore `vocabulary` collection
 * ======================================================================================
 * Writes one doc per word, id = word.id, matching the VocabularyWord Kotlin data
 * class field-for-field (FirebaseDataSource.getVocabularyByLevel/getVocabularyByCategory
 * read this collection via snapshot.toObjects(VocabularyWord::class.java), which
 * requires exact field name matches - no reshaping needed here, just a straight
 * upload since content/vocabulary/*.json already uses the same field names).
 *
 * isLearned/reviewCount/lastReviewed are per-user progress, not content - always
 * written as their defaults (false/0/0) here. Real per-user state lives in
 * VocabularyProgressStore (local SharedPreferences on-device), never in Firestore,
 * so multiple users don't share the same "learned" state for a word.
 *
 * Usage:
 *   export GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json
 *   node scripts/sync_vocabulary.js --dry-run       # preview
 *   node scripts/sync_vocabulary.js                 # sync all categories
 *   node scripts/sync_vocabulary.js beruf gesundheit # sync specific categories
 */

const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');

const CONTENT_DIR = path.join(__dirname, '..', 'content', 'vocabulary');
const COLLECTION = 'vocabulary';

const args = process.argv.slice(2);
const DRY_RUN = args.includes('--dry-run');
const categoryArgs = args.filter(a => a !== '--dry-run');

if (!process.env.GOOGLE_APPLICATION_CREDENTIALS) {
  console.error('❌ Set GOOGLE_APPLICATION_CREDENTIALS to your Firebase service account key path first.');
  process.exit(1);
}

const serviceAccount = JSON.parse(fs.readFileSync(process.env.GOOGLE_APPLICATION_CREDENTIALS, 'utf8'));
admin.initializeApp({ credential: admin.credential.cert(serviceAccount) });
const db = admin.firestore();

async function main() {
  const files = fs.readdirSync(CONTENT_DIR).filter(f => f.endsWith('.json'));
  const allCategories = files.map(f => f.replace('.json', '')).sort();
  const targets = categoryArgs.length > 0 ? categoryArgs : allCategories;

  console.log(DRY_RUN ? '🔍 DRY RUN — no writes will be made\n' : '🚀 Syncing content/vocabulary/*.json -> vocabulary\n');

  let totalWords = 0;
  for (const category of targets) {
    const filePath = path.join(CONTENT_DIR, `${category}.json`);
    if (!fs.existsSync(filePath)) {
      console.log(`  ❌ ${category}: file not found`);
      continue;
    }
    const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));
    console.log(`  ${category}: ${data.words.length} words`);
    totalWords += data.words.length;

    if (DRY_RUN) continue;

    const batchSize = 400;
    for (let i = 0; i < data.words.length; i += batchSize) {
      const batch = db.batch();
      data.words.slice(i, i + batchSize).forEach(w => {
        batch.set(db.collection(COLLECTION).doc(w.id), w);
      });
      await batch.commit();
    }
  }

  console.log(`\n${DRY_RUN ? 'Would sync' : 'Synced'} ${totalWords} words across ${targets.length} categories.`);
}

main().catch(e => { console.error('Error:', e); process.exit(1); });
