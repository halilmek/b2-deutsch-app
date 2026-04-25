/**
 * B2 Deutsch — Firebase Firestore Import Script
 * ============================================
 * Run: node firebase_import.js --file b2_reading_texts_part1.json
 * 
 * Prerequisites:
 *   npm install firebase-admin
 *   Set GOOGLE_APPLICATION_CREDENTIALS environment variable
 * 
 * Firestore Collection Structure:
 *   /readings/{readingId}       → Reading passage documents
 *   /topics/{topicId}           → Topic overview documents  
 *   /quizBank/{quizId}          → Quiz questions bank
 */

const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');

// Initialize Firebase Admin
const serviceAccount = process.env.GOOGLE_APPLICATION_CREDENTIALS 
  ? JSON.parse(fs.readFileSync(process.env.GOOGLE_APPLICATION_CREDENTIALS))
  : null;

if (!serviceAccount) {
  console.error('⚠️  Set GOOGLE_APPLICATION_CREDENTIALS environment variable');
  console.error('   Export your Firebase service account key as JSON and set:');
  console.error('   export GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json');
  process.exit(1);
}

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  storageBucket: 'b2-deutsch-app.firebasestorage.app'
});

const db = admin.firestore();

// ============================================================
// IMPORT FUNCTIONS
// ============================================================

async function importTopics(topicsFile) {
  console.log(`📚 Importing topics from ${topicsFile}...`);
  const data = JSON.parse(fs.readFileSync(topicsFile, 'utf8'));
  const topics = data.topics || [];
  
  let imported = 0;
  for (const topic of topics) {
    await db.collection('topics').doc(topic.id).set({
      name: topic.name,
      nameEn: topic.nameEn,
      description: topic.description || '',
      iconEmoji: topic.iconEmoji || '📖',
      sourceBase: topic.sourceBase || '',
      level: 'B2',
      type: 'reading',
      textCount: 0,
      quizCount: 0,
      createdAt: admin.firestore.FieldValue.serverTimestamp(),
      updatedAt: admin.firestore.FieldValue.serverTimestamp()
    });
    imported++;
    console.log(`  ✅ ${topic.iconEmoji} ${topic.name}`);
  }
  console.log(`\n✅ Imported ${imported} topics\n`);
}

async function importReadings(readingsFile) {
  console.log(`📖 Importing readings from ${readingsFile}...`);
  const data = JSON.parse(fs.readFileSync(readingsFile, 'utf8'));
  const readings = data.readings || [];
  
  // Batch write (Firestore limit: 500 docs/batch)
  const BATCH_SIZE = 400;
  let totalImported = 0;
  
  for (let i = 0; i < readings.length; i += BATCH_SIZE) {
    const batch = db.batch();
    const batchReadings = readings.slice(i, i + BATCH_SIZE);
    
    for (const reading of batchReadings) {
      const docRef = db.collection('readings').doc(reading.id);
      
      const docData = {
        id: reading.id,
        topicId: reading.topicId,
        level: reading.level || 'B2',
        title: reading.title,
        source: reading.source,
        sourceUrl: reading.sourceUrl || '',
        wordCount: reading.wordCount || 0,
        readingTimeMinutes: reading.readingTimeMinutes || 5,
        difficulty: reading.difficulty || 'B2',
        tags: reading.tags || [],
        content: reading.content,
        questionCount: reading.questions?.length || 0,
        hasVocabulary: (reading.keyVocabulary?.length || 0) > 0,
        hasExamTip: !!reading.examTip,
        createdAt: admin.firestore.FieldValue.serverTimestamp()
      };
      
      batch.set(docRef, docData);
      
      // Import questions as subcollection
      if (reading.questions && reading.questions.length > 0) {
        const questionsRef = docRef.collection('questions');
        for (const q of reading.questions) {
          const qData = {
            id: q.id,
            type: q.type,
            questionText: q.questionText,
            options: q.options || [],
            correctAnswer: q.correctAnswer,
            explanation: q.explanation || '',
            points: q.type === 'multiple_choice' ? 2 : 
                   q.type === 'true_false' ? 2 : 3
          };
          batch.set(questionsRef.doc(q.id), qData);
        }
      }
      
      // Import vocabulary
      if (reading.keyVocabulary && reading.keyVocabulary.length > 0) {
        const vocabRef = docRef.collection('vocabulary');
        for (const v of reading.keyVocabulary) {
          const vData = {
            german: v.german,
            english: v.english,
            turkish: v.turkish || '',
            partOfSpeech: v.pos || 'noun',
            level: 'B2'
          };
          batch.set(vocabRef.doc(), vData);
        }
      }
      
      totalImported++;
    }
    
    await batch.commit();
    console.log(`  Batch ${Math.floor(i/BATCH_SIZE)+1}: imported ${batchReadings.length} readings`);
  }
  
  console.log(`\n✅ Imported ${totalImported} readings with questions and vocabulary\n`);
}

async function createQuizBank(readingsFile) {
  console.log(`📝 Creating quiz bank from ${readingsFile}...`);
  const data = JSON.parse(fs.readFileSync(readingsFile, 'utf8'));
  const readings = data.readings || [];
  
  let quizCount = 0;
  
  for (const reading of readings) {
    if (!reading.questions || reading.questions.length === 0) continue;
    
    // Create one quiz per reading
    const quizId = `quiz_${reading.id}`;
    const quizRef = db.collection('quizBank').doc(quizId);
    
    const quizData = {
      id: quizId,
      sourceReadingId: reading.id,
      topicId: reading.topicId,
      level: 'B2',
      title: `Quiz: ${reading.title}`,
      description: `Teste dein Leseverständnis zum Thema: ${reading.title}`,
      questionCount: reading.questions.length,
      timeLimitMinutes: Math.max(5, Math.ceil(reading.questions.length * 0.8)),
      passingScore: 70,
      isPremium: false,
      type: 'reading_comprehension',
      tags: reading.tags || [],
      examTip: reading.examTip || '',
      difficulty: 'B2',
      createdAt: admin.firestore.FieldValue.serverTimestamp()
    };
    
    await quizRef.set(quizData);
    quizCount++;
  }
  
  console.log(`\n✅ Created ${quizCount} quizzes in quizBank collection\n`);
}

async function updateTopicCounts() {
  console.log('📊 Updating topic counts...');
  const topicsSnapshot = await db.collection('topics').get();
  
  for (const topicDoc of topicsSnapshot.docs) {
    const readingsSnapshot = await db.collection('readings')
      .where('topicId', '==', topicDoc.id)
      .get();
    
    await topicDoc.ref.update({
      textCount: readingsSnapshot.size,
      updatedAt: admin.firestore.FieldValue.serverTimestamp()
    });
    console.log(`  ✅ ${topicDoc.id}: ${readingsSnapshot.size} readings`);
  }
  console.log('\n');
}

// ============================================================
// CLI INTERFACE
// ============================================================

const args = process.argv.slice(2);
const command = args[0];

async function main() {
  switch (command) {
    case '--topics':
      await importTopics(args[1] || 'b2_reading_topics.json');
      break;
    
    case '--readings':
      await importReadings(args[1] || 'b2_reading_texts_part1.json');
      break;
    
    case '--quiz':
      await createQuizBank(args[1] || 'b2_reading_texts_part1.json');
      break;
    
    case '--all':
      const topicsFile = args[1] || 'b2_reading_topics.json';
      const readingsFile = args[2] || 'b2_reading_texts_part1.json';
      await importTopics(topicsFile);
      await importReadings(readingsFile);
      await createQuizBank(readingsFile);
      await updateTopicCounts();
      console.log('🎉 All imports complete!');
      break;
    
    case '--update-counts':
      await updateTopicCounts();
      break;
    
    default:
      console.log(`
B2 Deutsch — Firebase Import Script
=====================================

Usage:
  node firebase_import.js --topics [file]      Import topics
  node firebase_import.js --readings [file]    Import readings + questions
  node firebase_import.js --quiz [file]        Create quizzes from readings
  node firebase_import.js --all [topics] [readings]  Import everything
  node firebase_import.js --update-counts      Recalculate topic text counts

Examples:
  node firebase_import.js --all b2_reading_topics.json b2_reading_texts_part1.json
  
Environment:
  GOOGLE_APPLICATION_CREDENTIALS=/path/to/serviceAccountKey.json
`);
  }
}

main().catch(console.error);
