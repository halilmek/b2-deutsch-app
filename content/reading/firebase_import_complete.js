#!/usr/bin/env node
/**
 * B2 Deutsch - Firebase Import Script
 * Imports all themes, readings, and questions to Firestore
 * 
 * Usage:
 *   1. Download service account key from Firebase Console
 *   2. Run: export GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json
 *   3. Run: node firebase_import_complete.js --all
 */

const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');

// Get the directory where the script is located
const scriptDir = __dirname;

// Check if service account credentials are provided
const credPath = process.env.GOOGLE_APPLICATION_CREDENTIALS;
if (!credPath) {
    console.error('❌ Error: GOOGLE_APPLICATION_CREDENTIALS not set');
    console.error('');
    console.error('Steps to fix:');
    console.error('1. Go to https://console.firebase.google.com/');
    console.error('2. Select project: b2-deutsch-app');
    console.error('3. Go to Project Settings → Service Accounts');
    console.error('4. Click "Generate new private key"');
    console.error('5. Save the JSON file somewhere safe');
    console.error('6. Run: export GOOGLE_APPLICATION_CREDENTIALS=/path/to/your-key.json');
    console.error('7. Run this script again: node firebase_import_complete.js --all');
    process.exit(1);
}

if (!fs.existsSync(credPath)) {
    console.error(`❌ Error: Service account key not found at: ${credPath}`);
    console.error('Please check the path to your key file.');
    process.exit(1);
}

const serviceAccount = JSON.parse(fs.readFileSync(credPath));

admin.initializeApp({
    credential: admin.credential.cert(serviceAccount),
    storageBucket: 'b2-deutsch-app.firebasestorage.app'
});

const db = admin.firestore();

async function importThemes(data) {
    console.log('📥 Importing themes...');
    const batch = db.batch();
    
    for (const theme of data.themes) {
        const ref = db.collection('themes').doc(theme.id);
        batch.set(ref, {
            id: theme.id,
            name: theme.name,
            nameEn: theme.nameEn,
            iconEmoji: theme.iconEmoji,
            description: theme.description,
            tags: theme.tags,
            textCount: theme.textCount,
            createdAt: admin.firestore.FieldValue.serverTimestamp()
        });
    }
    
    await batch.commit();
    console.log(`✅ Imported ${data.themes.length} themes`);
}

async function importReadings(data) {
    console.log('📥 Importing readings...');
    let count = 0;
    const batchSize = 100;
    
    for (let i = 0; i < data.readings.length; i += batchSize) {
        const batch = db.batch();
        const batchReadings = data.readings.slice(i, i + batchSize);
        
        for (const reading of batchReadings) {
            const ref = db.collection('readings').doc(reading.id);
            batch.set(ref, {
                id: reading.id,
                themeId: reading.themeId,
                title: reading.title,
                content: reading.content,
                wordCount: reading.wordCount,
                readingTimeMinutes: reading.readingTimeMinutes,
                tags: reading.tags,
                createdAt: admin.firestore.FieldValue.serverTimestamp()
            });
            count++;
        }
        
        await batch.commit();
        console.log(`   Imported ${count}/${data.readings.length} readings...`);
    }
    console.log(`✅ Imported ${count} readings`);
}

async function importQuestions(data) {
    console.log('📥 Importing questions...');
    let count = 0;
    
    // Group questions by readingId
    const questionsByReading = {};
    for (const question of data.questions) {
        const readingId = question.id.replace(/_q\d+$/, '');
        if (!questionsByReading[readingId]) {
            questionsByReading[readingId] = [];
        }
        questionsByReading[readingId].push(question);
    }
    
    // Import questions to subcollection of each reading
    for (const [readingId, questions] of Object.entries(questionsByReading)) {
        const batch = db.batch();
        
        for (const question of questions) {
            const qId = question.id.replace(`${readingId}_`, '');
            const ref = db.collection('readings')
                .doc(readingId)
                .collection('questions')
                .doc(qId);
            
            batch.set(ref, {
                id: question.id,
                type: question.type,
                questionText: question.questionText,
                options: question.options || null,
                correctAnswer: question.correctAnswer,
                explanation: question.explanation,
                pairs: question.pairs || null,
                correctOrder: question.correctOrder || null,
                createdAt: admin.firestore.FieldValue.serverTimestamp()
            });
            count++;
        }
        
        await batch.commit();
    }
    
    // Also import all questions to quizBank for easy access
    const batch = db.batch();
    for (const question of data.questions) {
        const ref = db.collection('quizBank').doc(question.id);
        batch.set(ref, {
            ...question,
            createdAt: admin.firestore.FieldValue.serverTimestamp()
        });
    }
    await batch.commit();
    
    console.log(`✅ Imported ${count} questions to reading subcollections`);
    console.log(`✅ Imported ${data.questions.length} questions to quizBank`);
}

async function main() {
    const args = process.argv.slice(2);
    const action = args[0] || '--all';
    
    console.log('🚀 B2 Deutsch Firebase Import');
    console.log('=============================');
    console.log('');
    
    // Look for the JSON file in the same directory as this script
    const jsonPath = path.join(scriptDir, 'b2_all_themes_complete.json');
    
    if (!fs.existsSync(jsonPath)) {
        console.error(`❌ Error: Content file not found at: ${jsonPath}`);
        console.error('');
        console.error('Make sure b2_all_themes_complete.json is in the content/reading folder.');
        console.error('Pull the latest code from GitHub first:');
        console.error('   git pull origin main');
        process.exit(1);
    }
    
    const allData = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
    
    console.log(`📊 Total: ${allData.themes.length} themes, ${allData.readings.length} readings, ${allData.questions.length} questions`);
    console.log('');
    
    try {
        if (action === '--all' || action === '--themes') {
            await importThemes(allData);
        }
        
        if (action === '--all' || action === '--readings') {
            await importReadings(allData);
        }
        
        if (action === '--all' || action === '--questions') {
            await importQuestions(allData);
        }
        
        console.log('');
        console.log('🎉 Import complete!');
        console.log('');
        console.log('📁 Firestore Collections Created:');
        console.log('   /themes/{id}');
        console.log('   /readings/{id}');
        console.log('   /readings/{id}/questions/{id}');
        console.log('   /quizBank/{id}');
        
    } catch (error) {
        console.error('❌ Import failed:', error);
        process.exit(1);
    }
    
    process.exit(0);
}

main();
