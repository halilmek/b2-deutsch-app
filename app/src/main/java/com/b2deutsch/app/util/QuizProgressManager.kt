package com.b2deutsch.app.util

import android.content.Context
import android.content.SharedPreferences

/**
 * Manages quiz progress and sequential question ordering per subject.
 * Ensures questions are shown in order (Q1-5, Q6-10, ...) rather than random.
 * Counter persists across app restarts via SharedPreferences.
 */
object QuizProgressManager {

    private const val PREFS_NAME = "quiz_progress_prefs"
    private const val KEY_POINTER_PREFIX = "quiz_pointer_"
    private const val QUESTIONS_PER_QUIZ = 5

    /**
     * Get the next batch of question indices for a quiz.
     * Returns indices [startIndex, startIndex + QUESTIONS_PER_QUIZ)
     * If all questions have been shown once, resets to 0.
     */
    fun getNextQuestionIndices(
        context: Context,
        subjectId: String,
        totalQuestions: Int
    ): IntRange {
        val prefs = getPrefs(context)
        val key = KEY_POINTER_PREFIX + subjectId
        val currentPointer = prefs.getInt(key, 0)

        // Check if we need to reset
        val startIndex = if (currentPointer >= totalQuestions) {
            // All questions shown once - reset
            prefs.edit().putInt(key, 0).apply()
            0
        } else {
            currentPointer
        }

        // Save new pointer position for next quiz
        val newPointer = (startIndex + QUESTIONS_PER_QUIZ).coerceAtMost(totalQuestions)
        prefs.edit().putInt(key, newPointer).apply()

        return startIndex until newPointer
    }

    /**
     * Reset the quiz progress for a specific subject.
     * Call this when user completes a full cycle and wants to start over.
     */
    fun resetProgress(context: Context, subjectId: String) {
        val prefs = getPrefs(context)
        prefs.edit().remove(KEY_POINTER_PREFIX + subjectId).apply()
    }

    /**
     * Reset ALL quiz progress (for all subjects).
     */
    fun resetAllProgress(context: Context) {
        val prefs = getPrefs(context)
        val editor = prefs.edit()
        prefs.all.keys
            .filter { it.startsWith(KEY_POINTER_PREFIX) }
            .forEach { editor.remove(it) }
        editor.apply()
    }

    /**
     * Get current pointer position for a subject (for UI display).
     * Returns 0-based index of next question batch start.
     */
    fun getCurrentPointer(context: Context, subjectId: String): Int {
        val prefs = getPrefs(context)
        return prefs.getInt(KEY_POINTER_PREFIX + subjectId, 0)
    }

    /**
     * How many question sets remain for a subject.
     */
    fun getRemainingSets(context: Context, subjectId: String, totalQuestions: Int): Int {
        val pointer = getCurrentPointer(context, subjectId)
        return if (pointer >= totalQuestions) 0
               else ((totalQuestions - pointer) / QUESTIONS_PER_QUIZ) + 1
    }

    private fun getPrefs(context: Context): SharedPreferences {
        return context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)
    }
}