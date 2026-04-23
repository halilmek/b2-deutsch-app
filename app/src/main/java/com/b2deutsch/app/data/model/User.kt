package com.b2deutsch.app.data.model

data class User(
    val uid: String = "",
    val email: String = "",
    val displayName: String = "",
    val currentLevel: String = "B2",
    val subscriptionTier: String = "free",
    val createdAt: Long = System.currentTimeMillis(),
    val lastActive: Long = System.currentTimeMillis(),
    val streak: Int = 0,
    val isAdmin: Boolean = false
)

data class UserProgress(
    val userId: String = "",
    val level: String = "B2",
    val lessonsCompleted: Int = 0,
    val quizzesTaken: Int = 0,
    val averageScore: Double = 0.0,
    val vocabularyLearned: Int = 0,
    val speakingMinutesUsed: Int = 0,
    val writingEvalsUsed: Int = 0,
    val peerExamsUsed: Int = 0,
    val streak: Int = 0,
    val lastActiveDate: String = ""
)
