package com.b2deutsch.app.data.sync

import android.content.Context
import android.content.SharedPreferences
import android.util.Log
import com.b2deutsch.app.data.local.LocalQuestionBank
import com.google.firebase.firestore.FirebaseFirestore
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext

/**
 * Firebase Sync Service — Admin Push Model
 * =========================================
 * Syncs NEW or UPDATED questions from Firestore → SharedPreferences.
 * Only runs when:
 *   1. App opens AND last sync was > 7 days ago
 *   2. Manual trigger (future: pull-to-refresh)
 *
 * After sync: app goes fully OFFLINE — no more Firebase calls during quiz.
 * Admin controls content by running import scripts → Firestore.
 *
 * Firestore Structure Expected:
 *   moduleQuizQuestions/{subjectId}  → single doc with all questions for that topic
 *   moduleQuizQuestions/{questionId}  → individual question docs (optional)
 *   topicVersions/{subjectId}        → { version: Int, updatedAt: Timestamp }
 */
object FirebaseSyncService {

    private const val PREFS_NAME = "firebase_sync_prefs"
    private const val KEY_LAST_SYNC = "last_sync_timestamp"
    private const val KEY_SYNC_VERSION = "sync_version"
    private const val SYNC_INTERVAL_MS = 7 * 24 * 60 * 60 * 1000L // 7 days

    private const val TAG = "FirebaseSync"

    // Firestore collection for module quiz questions
    private const val COLLECTION_TOPICS = "moduleQuizQuestions"

    /**
     * Check if sync is needed (last sync > 7 days).
     * Call this on app launch.
     */
    fun shouldSync(context: Context): Boolean {
        val prefs = getPrefs(context)
        val lastSync = prefs.getLong(KEY_LAST_SYNC, 0L)
        val now = System.currentTimeMillis()
        return (now - lastSync) > SYNC_INTERVAL_MS
    }

    /**
     * Run full sync: check all topics, download updates.
     * Only syncs topics that have a newer version in Firestore.
     *
     * Runs on IO dispatcher — call from coroutine.
     */
    suspend fun syncIfNeeded(context: Context): SyncResult = withContext(Dispatchers.IO) {
        if (!shouldSync(context)) {
            Log.d(TAG, "Sync skipped — last sync was recent")
            return@withContext SyncResult.SKIPPED
        }

        Log.d(TAG, "Starting Firebase sync...")

        val db = FirebaseFirestore.getInstance()
        val prefs = getPrefs(context)
        val currentVersion = prefs.getInt(KEY_SYNC_VERSION, 0)

        try {
            // Get all topic documents from Firestore
            val snapshot = db.collection(COLLECTION_TOPICS)
                .whereGreaterThan("version", currentVersion)
                .get()
                .await()

            if (snapshot.isEmpty) {
                Log.d(TAG, "No updates found in Firestore")
                updateLastSync(context)
                return@withContext SyncResult.UP_TO_DATE
            }

            var updatedTopics = 0

            for (doc in snapshot.documents) {
                val subjectId = doc.id
                val totalQuestions = doc.getLong("totalQuestions")?.toInt() ?: 0
                val topicName = doc.getString("topicName") ?: ""

                // Get questions array from document
                val questionsArray = doc.get("questions") as? List<*>
                if (questionsArray.isNullOrEmpty()) {
                    Log.w(TAG, "Topic $subjectId has no questions — skipping")
                    continue
                }

                // Update SharedPreferences with new question data
                LocalQuestionBank.updateTopicFromFirebase(
                    context,
                    subjectId,
                    topicName,
                    totalQuestions,
                    questionsArray as List<Map<String, Any>>
                )

                updatedTopics++
                Log.d(TAG, "Updated topic: $subjectId ($totalQuestions questions)")
            }

            // Update sync metadata
            updateLastSync(context)
            prefs.edit().putInt(KEY_SYNC_VERSION, currentVersion + 1).apply()

            Log.d(TAG, "Sync complete: $updatedTopics topics updated")
            SyncResult.SUCCESS(updatedTopics)

        } catch (e: Exception) {
            Log.e(TAG, "Sync failed", e)
            SyncResult.FAILED(e.message ?: "Unknown error")
        }
    }

    /**
     * Force sync immediately (for manual refresh).
     */
    suspend fun forceSync(context: Context): SyncResult {
        Log.d(TAG, "Forcing immediate sync...")
        getPrefs(context).edit().putLong(KEY_LAST_SYNC, 0).apply()
        return syncIfNeeded(context)
    }

    /**
     * Get last sync time as human-readable string.
     */
    fun getLastSyncTime(context: Context): String {
        val prefs = getPrefs(context)
        val lastSync = prefs.getLong(KEY_LAST_SYNC, 0L)
        if (lastSync == 0L) return "Never"

        val diff = System.currentTimeMillis() - lastSync
        val days = diff / (24 * 60 * 60 * 1000)
        return if (days > 0) "$days day(s) ago" else "Today"
    }

    // ===== PRIVATE HELPERS =====

    private fun getPrefs(context: Context): SharedPreferences {
        return context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)
    }

    private fun updateLastSync(context: Context) {
        getPrefs(context).edit()
            .putLong(KEY_LAST_SYNC, System.currentTimeMillis())
            .apply()
    }

    // Extension to make Firestore suspend-compatible
    private suspend fun <T> com.google.android.gms.tasks.Task<T>.await(): T {
        return suspendCancellableCoroutine { continuation ->
            addOnSuccessListener { result -> continuation.resume(result, null) }
            addOnFailureListener { e -> continuation.resumeWithException(e) }
        }
    }

    // ===== RESULT CLASS =====

    sealed class SyncResult {
        object SKIPPED : SyncResult()      // Not due yet
        object UP_TO_DATE : SyncResult()   // Checked, nothing new
        data class SUCCESS(val topicsUpdated: Int) : SyncResult()
        data class FAILED(val error: String) : SyncResult()
    }
}