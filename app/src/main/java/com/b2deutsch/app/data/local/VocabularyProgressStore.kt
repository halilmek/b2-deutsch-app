package com.b2deutsch.app.data.local

import android.content.Context
import android.content.SharedPreferences

/**
 * Per-device spaced-repetition progress for vocabulary words.
 *
 * VocabularyWord.isLearned/reviewCount/lastReviewed are per-USER progress, not
 * content - they must never be read from or written to the shared Firestore
 * `vocabulary` document (that would make one user's progress visible/shared
 * with every other user). This store keeps that state locally instead, the
 * same pattern LocalQuestionBank uses for grammar quiz active/passive pools.
 *
 * Simple Leitner-style spacing: each correct review increases the interval
 * before the word is due again (1 -> 2 -> 4 -> 8 -> 16 days); a "hard" or
 * "wrong" review resets it back to due-immediately.
 */
object VocabularyProgressStore {

    private const val PREFS_NAME = "vocabulary_progress_prefs"
    private const val KEY_REVIEW_COUNT_PREFIX = "review_count_"
    private const val KEY_LAST_REVIEWED_PREFIX = "last_reviewed_"
    private const val KEY_LEARNED_PREFIX = "learned_"

    private val INTERVAL_DAYS_BY_BOX = listOf(0, 1, 2, 4, 8, 16) // index = reviewCount, capped at last
    private const val DAY_MS = 24 * 60 * 60 * 1000L

    private fun getPrefs(context: Context): SharedPreferences =
        context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)

    fun getReviewCount(context: Context, wordId: String): Int =
        getPrefs(context).getInt(KEY_REVIEW_COUNT_PREFIX + wordId, 0)

    fun getLastReviewed(context: Context, wordId: String): Long =
        getPrefs(context).getLong(KEY_LAST_REVIEWED_PREFIX + wordId, 0L)

    fun isLearned(context: Context, wordId: String): Boolean =
        getPrefs(context).getBoolean(KEY_LEARNED_PREFIX + wordId, false)

    /**
     * A word is due for review if it's never been reviewed, or its spacing
     * interval (based on how many times it's been reviewed correctly in a
     * row) has elapsed since the last review.
     */
    fun isDue(context: Context, wordId: String): Boolean {
        val lastReviewed = getLastReviewed(context, wordId)
        if (lastReviewed == 0L) return true
        val reviewCount = getReviewCount(context, wordId)
        val intervalDays = INTERVAL_DAYS_BY_BOX.getOrElse(reviewCount) { INTERVAL_DAYS_BY_BOX.last() }
        return System.currentTimeMillis() - lastReviewed >= intervalDays * DAY_MS
    }

    /**
     * Record a review result: "correct" advances the spacing interval and
     * marks the word learned once it reaches the last box; "hard"/"wrong"
     * resets it back to daily review.
     */
    fun recordResult(context: Context, wordId: String, result: String) {
        val prefs = getPrefs(context)
        val currentCount = getReviewCount(context, wordId)
        val newCount = when (result) {
            "correct" -> (currentCount + 1).coerceAtMost(INTERVAL_DAYS_BY_BOX.size - 1)
            else -> 0
        }
        prefs.edit()
            .putInt(KEY_REVIEW_COUNT_PREFIX + wordId, newCount)
            .putLong(KEY_LAST_REVIEWED_PREFIX + wordId, System.currentTimeMillis())
            .putBoolean(KEY_LEARNED_PREFIX + wordId, newCount >= INTERVAL_DAYS_BY_BOX.size - 1)
            .apply()
    }

    fun resetCategory(context: Context, wordIds: List<String>) {
        val prefs = getPrefs(context)
        val editor = prefs.edit()
        wordIds.forEach { wordId ->
            editor.remove(KEY_REVIEW_COUNT_PREFIX + wordId)
            editor.remove(KEY_LAST_REVIEWED_PREFIX + wordId)
            editor.remove(KEY_LEARNED_PREFIX + wordId)
        }
        editor.apply()
    }
}
