#!/usr/bin/env node
/**
 * B2 Deutsch - Firebase Import Script
 * Imports all themes, readings, and questions to Firestore
 * 
 * Usage:
 *   export GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json
 *   node firebase_import_complete.js --all
 */

const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');

const scriptDir = __dirname;

const credPath = process.env.GOOGLE_APPLICATION_CREDENTIALS;
if (!credPath) {
    console.error('❌ Error: GOOGLE_APPLICATION_CREDENTIALS not set');
    console.error('Run: export GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json');
    process.exit(1);
}

if (!fs.existsSync(credPath)) {
    console.error(`❌ Error: Service account key not found at: ${credPath}`);
    process.exit(1);
}

const serviceAccount = JSON.parse(fs.readFileSync(credPath));

admin.initializeApp({
    credential: admin.credential.cert(serviceAccount),
    storageBucket: 'b2-deutsch-app.firebasestorage.app'
});

const db = admin.firestore();

// Mapping: grammar topic ID -> theme ID
const GRAMMAR_TO_THEME = {
    'b2_01': 'beruf', 'b2_02': 'beruf', 'b2_03': 'beruf',
    'b2_04': 'gesundheit', 'b2_05': 'gesundheit', 'b2_06': 'gesundheit',
    'b2_07': 'umwelt', 'b2_08': 'umwelt', 'b2_09': 'umwelt',
    'b2_10': 'gesellschaft', 'b2_11': 'gesellschaft', 'b2_12': 'gesellschaft',
    'b2_13': 'reisen', 'b2_14': 'reisen',
    'b2_15': 'medien', 'b2_16': 'medien',
    'b2_17': 'bildung', 'b2_18': 'bildung',
    'b2_19': 'wirtschaft', 'b2_20': 'wirtschaft',
    'b2_21': 'geschichte', 'b2_22': 'geschichte', 'b2_23': 'geschichte'
};

// Get all grammar topic IDs that map to a theme
function getSubjectIdsForTheme(themeId) {
    return Object.entries(GRAMMAR_TO_THEME)
        .filter(([_, t]) => t === themeId)
        .map(([s, _]) => s);
}

async function importThemes(data) {
    console.log('📥 Importing themes...');
    const batch = db.batch();
    
    for (const theme of data.themes) {
        const ref = db.collection('themes').doc(theme.id);
        const subjectIds = getSubjectIdsForTheme(theme.id);
        batch.set(ref, {
            id: theme.id,
            name: theme.name,
            nameEn: theme.nameEn,
            iconEmoji: theme.iconEmoji,
            description: theme.description,
            tags: theme.tags,
            textCount: theme.textCount,
            subjectIds: subjectIds, // Array of grammar topic IDs that use this theme
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
            
            // Find grammar topics that map to this reading's theme
            const themeId = reading.themeId;
            const subjectIds = getSubjectIdsForTheme(themeId);
            
            batch.set(ref, {
                id: reading.id,
                themeId: reading.themeId,
                subjectIds: subjectIds, // Grammar topics that use this reading
                title: reading.title,
                content: reading.content,
                wordCount: reading.wordCount,
                readingTimeMinutes: reading.readingTimeMinutes,
                tags: reading.tags || [],
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
    console.log('📥 Importing questions to quizBank...');
    let count = 0;
    const batchSize = 100;
    
    for (let i = 0; i < data.questions.length; i += batchSize) {
        const batch = db.batch();
        const batchQuestions = data.questions.slice(i, i + batchSize);
        
        for (const question of batchQuestions) {
            const ref = db.collection('quizBank').doc(question.id);
            
            // Determine theme from question ID (e.g., "b2_beruf_01_q1" -> "beruf")
            let themeId = 'unknown';
            for (const theme of ['beruf', 'gesundheit', 'umwelt', 'gesellschaft', 'reisen', 'medien', 'bildung', 'wirtschaft', 'geschichte']) {
                if (question.id.includes(theme)) {
                    themeId = theme;
                    break;
                }
            }
            
            // Find grammar topics that map to this theme
            const subjectIds = getSubjectIdsForTheme(themeId);
            
            batch.set(ref, {
                id: question.id,
                themeId: themeId,
                subjectIds: subjectIds, // Grammar topics this question relates to
                type: question.type,
                questionText: question.questionText,
                options: question.options || null,
                correctAnswer: question.correctAnswer,
                explanation: question.explanation || null,
                pairs: question.pairs || null,
                correctOrder: question.correctOrder || null,
                createdAt: admin.firestore.FieldValue.serverTimestamp()
            });
            count++;
        }
        
        await batch.commit();
        if ((i + batchSize) % 500 === 0) {
            console.log(`   Imported ${count}/${data.questions.length} questions...`);
        }
    }
    
    console.log(`✅ Imported ${count} questions to quizBank`);
    
    // Also import to readings subcollections
    console.log('📥 Importing questions to readings subcollections...');
    count = 0;
    
    for (const reading of data.readings) {
        const readingQuestions = data.questions.filter(q => {
            // Match questions that start with reading theme
            const readingTheme = reading.themeId;
            return q.id.includes(readingTheme) && q.id.includes('_q');
        });
        
        if (readingQuestions.length > 0) {
            const batch = db.batch();
            
            for (let i = 0; i < readingQuestions.length; i++) {
                const question = readingQuestions[i];
                // Extract question number from ID
                const qMatch = question.id.match(/_q(\d+)$/);
                const qId = qMatch ? qMatch[1] : String(i + 1);
                
                const ref = db.collection('readings')
                    .doc(reading.id)
                    .collection('questions')
                    .doc(qId);
                
                batch.set(ref, {
                    id: question.id,
                    type: question.type,
                    questionText: question.questionText,
                    options: question.options || null,
                    correctAnswer: question.correctAnswer,
                    explanation: question.explanation || null,
                    createdAt: admin.firestore.FieldValue.serverTimestamp()
                });
                count++;
            }
            
            await batch.commit();
        }
    }
    
    console.log(`✅ Imported ${count} questions to reading subcollections`);
}

async function main() {
    const args = process.argv.slice(2);
    const action = args[0] || '--all';
    
    console.log('🚀 B2 Deutsch Firebase Import');
    console.log('=============================');
    console.log('');
    
    const jsonPath = path.join(scriptDir, 'b2_all_themes_complete.json');
    
    if (!fs.existsSync(jsonPath)) {
        console.error(`❌ Error: Content file not found at: ${jsonPath}`);
        console.error('Make sure b2_all_themes_complete.json is in the content/reading folder.');
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
        console.log('📁 Firestore Collections:');
        console.log('   /themes/{id} - 9 B2 themes with subjectIds mapping');
        console.log('   /readings/{id} - 90 readings with subjectIds mapping');
        console.log('   /readings/{id}/questions/{id} - Questions per reading');
        console.log('   /quizBank/{id} - All 450 questions with subjectIds');
        console.log('');
        console.log('💡 Quiz Flow: topic b2_01 → theme beruf → readings + questions');
        
    } catch (error) {
        console.error('❌ Import failed:', error);
        process.exit(1);
    }
    
    process.exit(0);
}

main();
