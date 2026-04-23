const functions = require('firebase-functions');
const admin = require('firebase-admin');
const axios = require('axios');

admin.initializeApp();

const db = admin.firestore();

// ============ WRITING EVALUATION ============
// Evaluates German writing submissions using AI (MiniMax or Gemini)
exports.evaluateWriting = functions.https.onCall(async (data, context) => {
  // Verify authentication
  if (!context.auth) {
    throw new functions.https.HttpsError('unauthenticated', 'User must be authenticated');
  }

  const { submissionId, text, taskType, level } = data;

  if (!text || text.length < 20) {
    throw new functions.https.HttpsError('invalid-argument', 'Text is too short for evaluation');
  }

  try {
    // Build evaluation prompt for MiniMax/Gemini
    const prompt = buildWritingEvaluationPrompt(text, taskType || 'essay', level || 'B2');

    // Call AI API (replace with your MiniMax API endpoint)
    const aiResponse = await callAI(prompt);

    // Parse evaluation
    const evaluation = parseEvaluation(aiResponse);

    // Update submission in Firestore
    if (submissionId) {
      await db.collection('writingSubmissions').doc(submissionId).update({
        evaluation: evaluation,
        score: evaluation.overallScore,
        evaluatedAt: admin.firestore.FieldValue.serverTimestamp(),
        tokensUsed: estimateTokens(prompt + aiResponse)
      });
    }

    return {
      success: true,
      evaluation: evaluation
    };
  } catch (error) {
    console.error('Writing evaluation error:', error);
    throw new functions.https.HttpsError('internal', 'Evaluation failed: ' + error.message);
  }
});

// ============ SPEAKING EVALUATION ============
// Evaluates German speaking transcripts
exports.evaluateSpeaking = functions.https.onCall(async (data, context) => {
  if (!context.auth) {
    throw new functions.https.HttpsError('unauthenticated', 'User must be authenticated');
  }

  const { sessionId, transcript, level } = data;

  if (!transcript || transcript.length < 10) {
    throw new functions.https.HttpsError('invalid-argument', 'Transcript is too short');
  }

  try {
    const prompt = buildSpeakingEvaluationPrompt(transcript, level || 'B2');
    const aiResponse = await callAI(prompt);
    const evaluation = parseSpeakingEvaluation(aiResponse);

    if (sessionId) {
      await db.collection('speakingSessions').doc(sessionId).update({
        evaluation: evaluation,
        transcript: transcript,
        score: evaluation.overallScore,
        completedAt: admin.firestore.FieldValue.serverTimestamp()
      });
    }

    return {
      success: true,
      evaluation: evaluation
    };
  } catch (error) {
    console.error('Speaking evaluation error:', error);
    throw new functions.https.HttpsError('internal', 'Evaluation failed: ' + error.message);
  }
});

// ============ CONTENT GENERATION (ADMIN ONLY) ============
// Generates reading passages and quiz questions
exports.generateContent = functions.https.onCall(async (data, context) => {
  if (!context.auth) {
    throw new functions.https.HttpsError('unauthenticated', 'User must be authenticated');
  }

  // Check if user is admin (you should implement admin check)
  const userDoc = await db.collection('users').doc(context.auth.uid).get();
  if (!userDoc.data()?.isAdmin) {
    throw new functions.https.HttpsError('permission-denied', 'Admin access required');
  }

  const { type, level, category, count = 5 } = data;

  try {
    const generatedContent = [];

    for (let i = 0; i < count; i++) {
      const content = await generateContentItem(type, level, category);
      generatedContent.push(content);
    }

    return {
      success: true,
      content: generatedContent
    };
  } catch (error) {
    console.error('Content generation error:', error);
    throw new functions.https.HttpsError('internal', 'Generation failed: ' + error.message);
  }
});

// ============ HELPER FUNCTIONS ============

function buildWritingEvaluationPrompt(text, taskType, level) {
  return `You are an expert German language examiner for level ${level}.
Evaluate the following ${taskType} response and provide structured feedback.

Response to evaluate:
---
${text}
---

Provide your evaluation in this exact JSON format (no markdown, pure JSON):
{
  "overallScore": <0-100>,
  "strengths": [<array of 2-3 strengths>],
  "improvements": [<array of 2-3 areas to improve>],
  "grammarNotes": "<specific grammar issues>",
  "vocabularyNotes": "<vocabulary range and appropriateness>",
  "structureNotes": "<organization and coherence>",
  "overallFeedback": "<2-3 sentence summary>"
}

Scoring rubric for ${level}:
- 90-100: Excellent - near native fluency
- 75-89: Good - minor errors, communicates effectively
- 60-74: Satisfactory - some errors but understandable
- 40-59: Needs improvement - frequent errors impede communication
- Below 40: Insufficient - serious issues with communication`;
}

function buildSpeakingEvaluationPrompt(transcript, level) {
  return `You are an expert German language examiner for level ${level}.
Evaluate the following speaking transcript and provide structured feedback.

Transcript:
---
${transcript}
---

Provide your evaluation in this exact JSON format (no markdown, pure JSON):
{
  "overallScore": <0-100>,
  "pronunciationScore": <0-100>,
  "fluencyScore": <0-100>,
  "grammarScore": <0-100>,
  "vocabularyScore": <0-100>,
  "taskAchievementScore": <0-100>,
  "strengths": [<array of 2-3 strengths>],
  "improvements": [<array of 2-3 areas to improve>],
  "overallFeedback": "<2-3 sentence summary>"
}`;
}

async function generateContentItem(type, level, category) {
  const prompts = {
    reading: `Generate a B2-level German reading passage about ${category || 'a general topic'}.
The passage should be 300-400 words.
After the passage, generate 4 comprehension questions in German (multiple choice with 4 options each).
Include the correct answer and a brief explanation.

Return as JSON:
{
  "title": "<German title>",
  "content": "<300-400 word German text>",
  "category": "${category || 'general'}",
  "level": "${level}",
  "questions": [
    {
      "questionText": "<question in German>",
      "options": ["<option A>", "<option B>", "<option C>", "<option D>"],
      "correctAnswer": "<A/B/C/D>",
      "explanation": "<brief explanation in German>"
    }
  ]
}`,

    quiz: `Generate a B2-level German quiz about ${category || 'grammar'}.
Create 5 questions in different formats: multiple choice, true/false, and fill-in-the-blank.

Return as JSON:
{
  "title": "<quiz title>",
  "category": "${category || 'grammar'}",
  "level": "${level}",
  "taskType": "grammar",
  "timeLimit": 10,
  "passingScore": 70,
  "questions": [
    {
      "type": "multiple_choice",
      "questionText": "<question>",
      "options": ["<A>", "<B>", "<C>", "<D>"],
      "correctAnswer": "<A/B/C/D>",
      "explanation": "<explanation>"
    }
  ]
}`
  };

  const prompt = prompts[type] || prompts.reading;
  const response = await callAI(prompt);
  return JSON.parse(response);
}

async function callAI(prompt) {
  // Replace with your MiniMax API endpoint
  const MINIMAX_API_URL = process.env.MINIMAX_API_URL || 'https://api.minimax.io/v1/text/chatcompletion';
  const MINIMAX_API_KEY = process.env.MINIMAX_API_KEY;

  try {
    const response = await axios.post(
      MINIMAX_API_URL,
      {
        model: 'MiniMax-Text-01',
        messages: [{ role: 'user', content: prompt }],
        temperature: 0.7
      },
      {
        headers: {
          'Authorization': `Bearer ${MINIMAX_API_KEY}`,
          'Content-Type': 'application/json'
        },
        timeout: 30000
      }
    );

    return response.data.choices[0].message.content;
  } catch (error) {
    console.error('AI API error:', error.response?.data || error.message);
    throw new Error('AI service unavailable');
  }
}

function parseEvaluation(responseText) {
  try {
    // Extract JSON from response (handle markdown code blocks if present)
    const jsonMatch = responseText.match(/\{[\s\S]*\}/);
    if (jsonMatch) {
      return JSON.parse(jsonMatch[0]);
    }
    throw new Error('Could not parse evaluation response');
  } catch (error) {
    console.error('Parse error:', error);
    // Return a safe default
    return {
      overallScore: 0,
      strengths: ['Unable to parse evaluation'],
      improvements: ['Please try again'],
      grammarNotes: '',
      vocabularyNotes: '',
      structureNotes: '',
      overallFeedback: 'Evaluation parsing failed'
    };
  }
}

function parseSpeakingEvaluation(responseText) {
  return parseEvaluation(responseText); // Same format
}

function estimateTokens(text) {
  // Rough estimate: ~4 characters per token for German
  return Math.ceil(text.length / 4);
}
