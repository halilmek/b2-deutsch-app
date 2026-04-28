package com.b2deutsch.app.data.local

import android.content.Context
import android.content.SharedPreferences
import org.json.JSONArray
import org.json.JSONObject
import java.io.InputStreamReader

/**
 * Local question bank — per-topic JSON files for offline access.
 * 
 * HOW IT WORKS:
 * 1. Each topic has its own JSON file: b2_01.json, b2_02.json, etc.
 * 2. Active/Passive status tracked per topic in SharedPreferences
 * 3. On "Next Quiz": select 10 random from ACTIVE (unsolved) pool
 * 4. After quiz: mark those 10 as PASSIVE (solved)
 * 5. When 90+/100 solved: show completion OR reset oldest passive to active
 * 6. If topic JSON doesn't exist → topic is "coming soon" (0 questions)
 * 
 * File naming: {subjectId}.json  e.g.  b2_01.json
 * File structure:
 * {
 *   "version": "1.0",
 *   "subjectId": "b2_01",
 *   "topicName": "Konnektoren",
 *   "totalQuestions": 96,
 *   "questions": [...]
 * }
 */
object LocalQuestionBank {

    private const val PREFS_NAME = "quiz_progress_prefs_v5"
    private const val KEY_ACTIVE_PREFIX = "active_"      // unsolved question IDs
    private const val KEY_PASSIVE_PREFIX = "passive_"    // solved question IDs
    private const val KEY_TOPIC_COUNT_PREFIX = "count_" // total questions per topic
    private const val QUESTIONS_PER_QUIZ = 10

    // ============ PUBLIC API ============

    /**
     * Initialize ALL topics from per-topic JSON files.
     * Call once on app startup.
     * Only initializes topics that have a corresponding JSON file.
     */
    fun initializeFromAssets(context: Context) {
        val prefs = getPrefs(context)
        val topicIds = getAllB2TopicIds()

        topicIds.forEach { subjectId ->
            val fileName = "$subjectId.json"
            try {
                context.assets.open(fileName).use { inputStream ->
                    val reader = InputStreamReader(inputStream)
                    val jsonText = reader.readText()
                    reader.close()
                    val json = JSONObject(jsonText)
                    val total = json.getInt("totalQuestions")
                    val questions = json.getJSONArray("questions")

                    // Initialize if not already
                    if (!prefs.contains(KEY_ACTIVE_PREFIX + subjectId)) {
                        val allIds = (1..total).map {
                            "${subjectId}_q${it.toString().padStart(3, '0')}"
                        }
                        val activeArray = JSONArray(allIds)
                        prefs.edit()
                            .putString(KEY_ACTIVE_PREFIX + subjectId, activeArray.toString())
                            .putString(KEY_PASSIVE_PREFIX + subjectId, JSONArray().toString())
                            .putInt(KEY_TOPIC_COUNT_PREFIX + subjectId, total)
                            .apply()
                    }
                }
            } catch (e: Exception) {
                // Topic file doesn't exist yet → coming soon, skip
            }
        }
    }

    /**
     * Get the next quiz: 10 random questions from ACTIVE pool.
     */
    fun getNextQuiz(context: Context, subjectId: String): QuizResult {
        val prefs = getPrefs(context)
        val total = prefs.getInt(KEY_TOPIC_COUNT_PREFIX + subjectId, 0)

        // No questions for this topic?
        if (total == 0) {
            return QuizResult(
                questions = emptyList(),
                isComplete = false,
                isLooping = false,
                message = "📝 Coming soon! Questions for this topic are being prepared.",
                solvedCount = 0,
                remainingActive = 0,
                totalQuestions = 0
            )
        }

        val activeIds = getActiveIds(context, subjectId)
        val passiveIds = getPassiveIds(context, subjectId)

        if (activeIds.size < QUESTIONS_PER_QUIZ) {
            if (passiveIds.size >= (total * 0.9).toInt()) {
                return QuizResult(
                    questions = emptyList(),
                    isComplete = true,
                    isLooping = false,
                    message = "🎉 Congratulations! All $total questions completed for this topic!",
                    solvedCount = passiveIds.size,
                    remainingActive = 0,
                    totalQuestions = total
                )
            } else {
                val toReset = minOf(QUESTIONS_PER_QUIZ - activeIds.size, passiveIds.size)
                val idsToReset = passiveIds.take(toReset)
                val newActive = (activeIds + idsToReset).toMutableSet()
                val newPassive = passiveIds.drop(toReset).toSet()
                saveActivePassive(context, subjectId, newActive, newPassive)
                val selected = newActive.shuffled().take(QUESTIONS_PER_QUIZ)
                val questions = selected.mapNotNull { getQuestionDetails(context, it) }
                return QuizResult(
                    questions = questions,
                    isComplete = false,
                    isLooping = true,
                    message = "🔄 Loop restart! Oldest $toReset questions returned to active pool.",
                    solvedCount = passiveIds.size - toReset,
                    remainingActive = newActive.size - QUESTIONS_PER_QUIZ,
                    totalQuestions = total
                )
            }
        }

        val selected = activeIds.shuffled().take(QUESTIONS_PER_QUIZ)
        val questions = selected.mapNotNull { getQuestionDetails(context, it) }
        return QuizResult(
            questions = questions,
            isComplete = false,
            isLooping = false,
            message = "",
            solvedCount = passiveIds.size,
            remainingActive = activeIds.size - QUESTIONS_PER_QUIZ,
            totalQuestions = total
        )
    }

    /**
     * Call AFTER user completes a quiz to mark those 10 as solved (passive).
     */
    fun markQuizCompleted(context: Context, subjectId: String, questionIds: List<String>) {
        val prefs = getPrefs(context)
        val activeIds = getActiveIds(context, subjectId).toMutableSet()
        val passiveIds = getPassiveIds(context, subjectId).toMutableSet()
        questionIds.forEach { id ->
            activeIds.remove(id)
            passiveIds.add(id)
        }
        saveActivePassive(context, subjectId, activeIds, passiveIds)
    }

    /**
     * Reset ALL progress for a topic (all back to active)
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
        getAllB2TopicIds().forEach { resetTopic(context, it) }
    }

    /**
     * Progress info string
     */
    fun getProgressString(context: Context, subjectId: String): String {
        val total = getPrefs(context).getInt(KEY_TOPIC_COUNT_PREFIX + subjectId, 0)
        val solved = getPassiveIds(context, subjectId).size
        if (total == 0) return "Coming soon"
        return "$solved/$total gelöst"
    }

    /**
     * How many questions remaining (active)
     */
    fun getRemainingCount(context: Context, subjectId: String): Int {
        return getActiveIds(context, subjectId).size
    }

    /**
     * Check if topic is fully completed
     */
    fun isTopicComplete(context: Context, subjectId: String): Boolean {
        val total = getPrefs(context).getInt(KEY_TOPIC_COUNT_PREFIX + subjectId, 0)
        if (total == 0) return false
        return getPassiveIds(context, subjectId).size >= (total * 0.9).toInt()
    }

    /**
     * Get total question count for a topic (from JSON file)
     */
    fun getTotalQuestionCount(context: Context, subjectId: String): Int {
        return getPrefs(context).getInt(KEY_TOPIC_COUNT_PREFIX + subjectId, 0)
    }

    // ============ PRIVATE HELPERS ============

    private fun initializeTopic(context: Context, subjectId: String) {
        val prefs = getPrefs(context)
        val total = prefs.getInt(KEY_TOPIC_COUNT_PREFIX + subjectId, 0)
        if (total == 0) return
        if (!prefs.contains(KEY_ACTIVE_PREFIX + subjectId)) {
            val allIds = (1..total).map {
                "${subjectId}_q${it.toString().padStart(3, '0')}"
            }
            val activeArray = JSONArray(allIds)
            prefs.edit()
                .putString(KEY_ACTIVE_PREFIX + subjectId, activeArray.toString())
                .putString(KEY_PASSIVE_PREFIX + subjectId, JSONArray().toString())
                .apply()
        }
    }

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

    /**
     * Read question details from the per-topic JSON file.
     * Opens {subjectId}.json directly — no shared cache.
     */
    private fun getQuestionDetails(context: Context, questionId: String): Question? {
        // Extract subjectId from questionId (e.g. "b2_01_q005" → "b2_01")
        val subjectId = questionId.substringBeforeLast("_q")
        val fileName = "$subjectId.json"

        return try {
            context.assets.open(fileName).use { inputStream ->
                val reader = InputStreamReader(inputStream)
                val jsonText = reader.readText()
                reader.close()
                val json = JSONObject(jsonText)
                val questions = json.getJSONArray("questions")
                for (i in 0 until questions.length()) {
                    val q = questions.getJSONObject(i)
                    if (q.getString("id") == questionId) {
                        val optionsArray = q.optJSONArray("options")
                        val options = if (optionsArray != null) {
                            (0 until optionsArray.length()).map { optionsArray.getString(it) }
                        } else emptyList()
                        return@use Question(
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
            }
        } catch (e: Exception) {
            e.printStackTrace()
            null
        }
    }

    private fun getPrefs(context: Context): SharedPreferences {
        return context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)
    }

    private fun getAllB2TopicIds(): List<String> {
        return (1..23).map { "b2_${it.toString().padStart(2, '0')}" }
    }

    /**
     * Get all topic IDs for a given level.
     */
    fun getAllTopicIds(level: String): List<String> {
        val levelUpper = level.uppercase()
        val count = when (levelUpper) {
            "A1" -> 15
            "A2" -> 15
            "B1" -> 15
            "B2" -> 22
            "C1" -> 15
            else -> 0
        }
        return (1..count).map { "${levelUpper.lowercase()}_${it.toString().padStart(2, '0')}" }
    }

    // ============ DATA CLASSES ============

    data class QuizResult(
        val questions: List<Question>,
        val isComplete: Boolean,
        val isLooping: Boolean,
        val message: String,
        val solvedCount: Int,
        val remainingActive: Int,
        val totalQuestions: Int
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
