#!/usr/bin/env node
/**
 * B2 Deutsch - Firebase Import: 100 Questions Per Topic
 * Imports ALL 2300 questions (100 per topic x 23 topics) to Firestore grammarQuizBank
 *
 * Usage:
 *   export GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json
 *   node firebase_import_100_questions.js
 */

const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');

const credPath = process.env.GOOGLE_APPLICATION_CREDENTIALS;
if (!credPath) {
    console.error('Error: GOOGLE_APPLICATION_CREDENTIALS not set');
    console.error('Run: export GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json');
    process.exit(1);
}

if (!fs.existsSync(credPath)) {
    console.error('Service account key not found at:', credPath);
    process.exit(1);
}

const serviceAccount = JSON.parse(fs.readFileSync(credPath));
admin.initializeApp({
    credential: admin.credential.cert(serviceAccount),
    storageBucket: 'b2-deutsch-app.firebasestorage.app'
});

const db = admin.firestore();
const BATCH_SIZE = 100; // Firestore batch limit

async function importQuestions() {
    const jsonPath = path.join(__dirname, 'b2_100_questions_per_topic.json');
    
    if (!fs.existsSync(jsonPath)) {
        console.error('Error: b2_100_questions_per_topic.json not found');
        console.error('Run: python3 gen_100_questions.py first');
        process.exit(1);
    }
    
    const data = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
    const questions = data.questionBank;
    
    console.log('');
    console.log('B2 Deutsch - Firebase Import: 100 Questions Per Topic');
    console.log('='.repeat(55));
    console.log('Total questions:', questions.length);
    console.log('Topics:', Object.keys(data.topics).length);
    console.log('');
    
    // Clear existing grammarQuizBank
    console.log('Clearing existing grammarQuizBank collection...');
    const existing = await db.collection('grammarQuizBank').listDocuments();
    let deleted = 0;
    for (const doc of existing) {
        await doc.delete();
        deleted++;
    }
    console.log('Deleted', deleted, 'existing documents\n');
    
    // Import in batches
    console.log('Importing questions to grammarQuizBank...');
    let imported = 0;
    let topicCounts = {};
    
    for (let i = 0; i < questions.length; i += BATCH_SIZE) {
        const batch = db.batch();
        const batchQuestions = questions.slice(i, i + BATCH_SIZE);
        
        for (const q of batchQuestions) {
            const ref = db.collection('grammarQuizBank').doc(q.id);
            batch.set(ref, {
                id: q.id,
                subjectId: q.subjectId,
                topicName: q.topicName,
                type: q.type,
                questionText: q.questionText,
                options: q.options || [],
                correctAnswer: q.correctAnswer,
                explanation: q.explanation || '',
                difficulty: q.difficulty || 'medium',
                createdAt: admin.firestore.FieldValue.serverTimestamp()
            });
            
            topicCounts[q.subjectId] = (topicCounts[q.subjectId] || 0) + 1;
        }
        
        await batch.commit();
        imported += batchQuestions.length;
        console.log(`  Imported ${imported}/${questions.length}...`);
    }
    
    console.log('');
    console.log('Per-topic breakdown:');
    for (const [tid, count] of Object.entries(topicCounts)) {
        const topicName = data.topics[tid]?.name || tid;
        console.log(`  ${tid}: ${count} questions - ${topicName}`);
    }
    
    console.log('');
    console.log('Firestore Collection: grammarQuizBank');
    console.log('Total documents:', imported);
    console.log('');
    console.log('Each document structure:');
    console.log('  id, subjectId, topicName, type, questionText,');
    console.log('  options[], correctAnswer, explanation, difficulty');
    console.log('');
    console.log('Query by subjectId:');
    console.log('  firestore.collection("grammarQuizBank")');
    console.log('    .where("subjectId", "==", "b2_01")');
    console.log('');
}

importQuestions()
    .then(() => { console.log('Done!'); process.exit(0); })
    .catch(e => { console.error('Error:', e); process.exit(1); });
