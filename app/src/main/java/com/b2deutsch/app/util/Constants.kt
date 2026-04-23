package com.b2deutsch.app.util

object Constants {

    // CEFR Levels
    val CEFR_LEVELS = listOf("A1", "A2", "B1", "B2", "C1")
    const val DEFAULT_LEVEL = "B2"

    // Content Categories
    object Categories {
        const val GRAMMAR = "grammar"
        const val VOCABULARY = "vocabulary"
        const val READING = "reading"
        const val LISTENING = "listening"
        const val WRITING = "writing"
        const val SPEAKING = "speaking"
    }

    // Quiz Types
    object QuizTypes {
        const val MULTIPLE_CHOICE = "multiple_choice"
        const val MULTIPLE_CHOICE_MULTI = "multiple_choice_multi"
        const val TRUE_FALSE = "true_false"
        const val FILL_BLANK = "fill_blank"
    }

    // Subscription Tiers
    object SubscriptionTier {
        const val FREE = "free"
        const val STANDARD = "standard"
        const val PREMIUM = "premium"
    }

    // Usage Limits
    object UsageLimits {
        // Free tier
        const val FREE_SPEAKING_MIN_PER_DAY = 10
        const val FREE_WRITING_PER_WEEK = 1
        const val FREE_PEER_EXAMS_PER_WEEK = 1

        // Standard tier
        const val STANDARD_SPEAKING_MIN_PER_DAY = 20
        const val STANDARD_WRITING_PER_MONTH = 5
        const val STANDARD_PEER_EXAMS_PER_WEEK = 1

        // Premium tier
        const val PREMIUM_SPEAKING_UNLIMITED = -1
        const val PREMIUM_WRITING_PER_MONTH = 15
        const val PREMIUM_PEER_EXAMS_PER_WEEK = 2
    }

    // Firestore Collections
    object Collections {
        const val USERS = "users"
        const val LEVELS = "levels"
        const val LESSONS = "lessons"
        const val QUIZZES = "quizzes"
        const val VOCABULARY = "vocabulary"
        const val READING_PASSAGES = "readingPassages"
        const val LISTENING_EXERCISES = "listeningExercises"
        const val WRITING_SUBMISSIONS = "writingSubmissions"
        const val SPEAKING_SESSIONS = "speakingSessions"
        const val USER_PROGRESS = "userProgress"
    }

    // SharedPreferences Keys
    object Prefs {
        const val PREFS_NAME = "b2_deutsch_prefs"
        const val KEY_CURRENT_LEVEL = "current_level"
        const val KEY_SUBSCRIPTION_TIER = "subscription_tier"
        const val KEY_DAILY_SPEAKING_MINUTES = "daily_speaking_minutes"
        const val KEY_LAST_SPEAKING_DATE = "last_speaking_date"
    }
}
