package com.b2deutsch.app.data.model

data class WritingSubmission(
    val id: String = "",
    val userId: String = "",
    val level: String = "B2",
    val taskType: String = "", // formal_email, informal_letter, essay, etc.
    val prompt: String = "",
    val userText: String = "",
    val evaluation: WritingEvaluation? = null,
    val score: Int = 0,
    val submittedAt: Long = System.currentTimeMillis(),
    val evaluatedAt: Long = 0,
    val tokensUsed: Int = 0
)

data class WritingEvaluation(
    val overallScore: Int = 0,
    val strengths: List<String> = emptyList(),
    val improvements: List<String> = emptyList(),
    val grammarNotes: String = "",
    val vocabularyNotes: String = "",
    val structureNotes: String = "",
    val overallFeedback: String = ""
)
