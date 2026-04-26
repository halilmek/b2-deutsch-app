package com.b2deutsch.app.data.local

import android.content.Context
import android.content.SharedPreferences
import org.json.JSONArray
import org.json.JSONObject
import java.io.InputStreamReader

/**
 * Local question bank for offline access + active/passive tracking.
 * 
 * HOW IT WORKS:
 * 1. Questions loaded from assets/b2_questions.json (bundled with app)
 * 2. Active/Passive status tracked per topic in SharedPreferences
 * 3. On "Next Quiz": select 10 random from ACTIVE (unsolved) pool
 * 4. After quiz: mark those 10 as PASSIVE (solved)
 * 5. When 90+/100 solved: show completion OR reset oldest passive to active
 * 
 * Topics: b2_01 through b2_23 (100 questions each)
 */
object LocalQuestionBank {

    private const val PREFS_NAME = "quiz_progress_prefs_v2"
    private const val KEY_ACTIVE_PREFIX = "active_"      // unsolved question IDs
    private const val KEY_PASSIVE_PREFIX = "passive_"    // solved question IDs
    private const val KEY_BANK_LOADED = "bank_loaded"    // if JSON was parsed
    private const val KEY_QUESTIONS = "questions_json"   // full question map
    private const val QUESTIONS_PER_QUIZ = 10

    // ============ PUBLIC API ============

    /**
     * Initialize the question bank from assets JSON.
     * Call once on app startup.
     */
    fun initializeFromAssets(context: Context) {
        val prefs = getPrefs(context)
        
        // Check if already loaded
        if (prefs.getBoolean(KEY_BANK_LOADED, false)) {
            return
        }
        
        try {
            val inputStream = context.assets.open("b2_questions.json")
            val reader = InputStreamReader(inputStream)
            val jsonText = reader.readText()
            reader.close()
            
            // Store compressed question data
            prefs.edit().putString(KEY_QUESTIONS, jsonText).apply()
            prefs.edit().putBoolean(KEY_BANK_LOADED, true).apply()
            
            // Initialize ALL topics: all 100 questions start as ACTIVE
            val json = JSONObject(jsonText)
            val topics = json.getJSONObject("topics")
            topics.keys().forEach { topicId ->
                initializeTopic(context, topicId)
            }
            
        } catch (e: Exception) {
            e.printStackTrace()
        }
    }

    /**
     * Initialize a specific topic: all 100 questions = active (unsolved)
     */
    fun initializeTopic(context: Context, subjectId: String) {
        val prefs = getPrefs(context)
        
        if (!prefs.contains(KEY_ACTIVE_PREFIX + subjectId)) {
            // 100 question IDs: subjectId_q001 ... subjectId_q100
            val allIds = (1..100).map { 
                "${subjectId}_q${it.toString().padStart(3, '0')}" 
            }
            val activeArray = JSONArray(allIds)
            prefs.edit()
                .putString(KEY_ACTIVE_PREFIX + subjectId, activeArray.toString())
                .putString(KEY_PASSIVE_PREFIX + subjectId, JSONArray().toString())
                .apply()
        }
    }

    /**
     * Get the next quiz: 10 random questions from ACTIVE pool.
     * Returns QuizResult with question details (not just IDs).
     */
    fun getNextQuiz(
        context: Context, 
        subjectId: String
    ): QuizResult {
        val prefs = getPrefs(context)
        
        val activeIds = getActiveIds(context, subjectId)
        val passiveIds = getPassiveIds(context, subjectId)
        
        // Not enough active questions?
        if (activeIds.size < QUESTIONS_PER_QUIZ) {
            if (passiveIds.size >= 90) {
                // Completed all 100!
                return QuizResult(
                    questions = emptyList(),
                    isComplete = true,
                    isLooping = false,
                    message = "🎉 Congratulations! All 100 questions completed for this topic!",
                    solvedCount = passiveIds.size,
                    remainingActive = 0,
                    totalQuestions = 100
                )
            } else {
                // Reset oldest passive back to active
                val toReset = minOf(QUESTIONS_PER_QUIZ - activeIds.size, passiveIds.size)
                val idsToReset = passiveIds.take(toReset)
                
                val newActive = (activeIds + idsToReset).toMutableSet()
                val newPassive = passiveIds.drop(toReset).toSet()
                
                saveActivePassive(context, subjectId, newActive, newPassive)
                
                // Pick 10 from new active pool
                val selected = newActive.shuffled().take(QUESTIONS_PER_QUIZ)
                val questions = selected.mapNotNull { getQuestionDetails(context, it) }
                
                return QuizResult(
                    questions = questions,
                    isComplete = false,
                    isLooping = true,
                    message = "🔄 Loop restart! Oldest ${toReset} questions returned to active pool.",
                    solvedCount = passiveIds.size - toReset,
                    remainingActive = newActive.size - QUESTIONS_PER_QUIZ,
                    totalQuestions = 100
                )
            }
        }
        
        // Normal case: pick 10 random from active
        val selected = activeIds.shuffled().take(QUESTIONS_PER_QUIZ)
        val questions = selected.mapNotNull { getQuestionDetails(context, it) }
        
        return QuizResult(
            questions = questions,
            isComplete = false,
            isLooping = false,
            message = "",
            solvedCount = passiveIds.size,
            remainingActive = activeIds.size - QUESTIONS_PER_QUIZ,
            totalQuestions = 100
        )
    }

    /**
     * Call AFTER user completes a quiz to mark those 10 as solved (passive).
     * Pass the list of question IDs that were shown in the quiz.
     */
    fun markQuizCompleted(context: Context, subjectId: String, questionIds: List<String>) {
        val prefs = getPrefs(context)
        
        val activeIds = getActiveIds(context, subjectId).toMutableSet()
        val passiveIds = getPassiveIds(context, subjectId).toMutableSet()
        
        // Move from active → passive
        questionIds.forEach { id ->
            activeIds.remove(id)
            passiveIds.add(id)
        }
        
        saveActivePassive(context, subjectId, activeIds, passiveIds)
    }

    /**
     * Reset ALL progress for a topic (all 100 back to active)
     */
    fun resetTopic(context: Context, subjectId: String) {
        val prefs = getPrefs(context)
        prefs.edit()
            .remove(KEY_ACTIVE_PREFIX + subjectId)
            .remove(KEY_PASSIVE_PREFIX + subjectId)
            .apply()
        initializeTopic(context, subjectId)
    }

    /**
     * Reset progress for ALL B2 topics
     */
    fun resetAllTopics(context: Context) {
        val b2Topics = (1..23).map { "b2_${it.toString().padStart(2, '0')}" }
        b2Topics.forEach { resetTopic(context, it) }
    }

    /**
     * Progress info string
     */
    fun getProgressString(context: Context, subjectId: String): String {
        val solved = getPassiveIds(context, subjectId).size
        return "$solved/100 gelöst"
    }

    /**
     * How many questions remaining (active)
     */
    fun getRemainingCount(context: Context, subjectId: String): Int {
        return getActiveIds(context, subjectId).size
    }

    /**
     * Check if topic is fully completed (90+ solved)
     */
    fun isTopicComplete(context: Context, subjectId: String): Boolean {
        return getPassiveIds(context, subjectId).size >= 90
    }

    /**
     * Get all question IDs for a topic (for reference)
     */
    fun getAllQuestionIds(subjectId: String): List<String> {
        return (1..100).map { "${subjectId}_q${it.toString().padStart(3, '0')}" }
    }

    // ============ PRIVATE HELPERS ============

    private fun getActiveIds(context: Context, subjectId: String): Set<String> {
        val prefs = getPrefs(context)
        val json = prefs.getString(KEY_ACTIVE_PREFIX + subjectId, null)
        if (json.isNullOrEmpty()) {
            initializeTopic(context, subjectId)
            return getActiveIds(context, subjectId)
        }
        val array = JSONArray(json)
        return (0 until array.length()).map { array.getString(it) }.toSet()
    }

    private fun getPassiveIds(context: Context, subjectId: String): Set<String> {
        val prefs = getPrefs(context)
        val json = prefs.getString(KEY_PASSIVE_PREFIX + subjectId, "[]")
        val array = JSONArray(json)
        return (0 until array.length()).map { array.getString(it) }.toSet()
    }

    private fun saveActivePassive(
        context: Context, 
        subjectId: String, 
        active: Set<String>, 
        passive: Set<String>
    ) {
        val prefs = getPrefs(context)
        prefs.edit()
            .putString(KEY_ACTIVE_PREFIX + subjectId, JSONArray(active.toList()).toString())
            .putString(KEY_PASSIVE_PREFIX + subjectId, JSONArray(passive.toList()).toString())
            .apply()
    }

    private fun getQuestionDetails(context: Context, questionId: String): Question? {
        val prefs = getPrefs(context)
        val jsonStr = prefs.getString(KEY_QUESTIONS, null) ?: return null
        
        return try {
            val json = JSONObject(jsonStr)
            val bank = json.getJSONArray("questionBank")
            for (i in 0 until bank.length()) {
                val q = bank.getJSONObject(i)
                if (q.getString("id") == questionId) {
                    val optionsArray = q.optJSONArray("options") 
                    val options = if (optionsArray != null) {
                        (0 until optionsArray.length()).map { optionsArray.getString(it) }
                    } else emptyList()
                    
                    return Question(
                        id = q.getString("id"),
                        subjectId = q.getString("subjectId"),
                        type = q.getString("type"),
                        questionText = q.getString("questionText"),
                        options = options,
                        correctAnswer = q.getString("correctAnswer"),
                        explanation = q.optString("explanation", ""),
                        difficulty = q.optString("difficulty", "medium"),
                        topicName = q.optString("topicName", "")
                    )
                }
            }
            null
        } catch (e: Exception) {
            e.printStackTrace()
            null
        }
    }

    private fun getPrefs(context: Context): SharedPreferences {
        return context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)
    }

    // ============ DATA CLASSES ============

    data class QuizResult(
        val questions: List<Question>,  // 10 questions or empty if complete
        val isComplete: Boolean,         // true if all 100 done (90+ solved)
        val isLooping: Boolean,          // true if we reset some back to active
        val message: String,              // display message to user
        val solvedCount: Int,             // how many solved so far
        val remainingActive: Int,         // how many active remain
        val totalQuestions: Int          // always 100
    )

    data class Question(
        val id: String,
        val subjectId: String,
        val type: String,
        val questionText: String,
        val options: List<String>,
        val correctAnswer: String,
        val explanation: String,
        val difficulty: String,
        val topicName: String
    )
}
