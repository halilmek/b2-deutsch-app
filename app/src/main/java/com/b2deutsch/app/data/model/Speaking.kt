package com.b2deutsch.app.data.model

data class SpeakingSession(
    val id: String = "",
    val userId: String = "",
    val level: String = "B2",
    val partnerType: String = "ai", // "ai" or "peer"
    val peerUserId: String = "",
    val topic: String = "",
    val duration: Int = 0, // seconds
    val recordingUrls: List<String> = emptyList(),
    val transcript: String = "",
    val evaluation: SpeakingEvaluation? = null,
    val score: Int = 0,
    val startedAt: Long = 0,
    val completedAt: Long = 0
)

data class SpeakingEvaluation(
    val overallScore: Int = 0,
    val pronunciationScore: Int = 0,
    val fluencyScore: Int = 0,
    val grammarScore: Int = 0,
    val vocabularyScore: Int = 0,
    val taskAchievementScore: Int = 0,
    val strengths: List<String> = emptyList(),
    val improvements: List<String> = emptyList(),
    val overallFeedback: String = ""
)

data class PeerExamRoom(
    val id: String = "",
    val level: String = "B2",
    val examinerId: String = "",
    val candidateId: String = "",
    val topic: String = "",
    val questions: List<String> = emptyList(),
    val status: String = "waiting", // waiting, in_progress, completed
    val createdAt: Long = System.currentTimeMillis(),
    val expiresAt: Long = 0
)
