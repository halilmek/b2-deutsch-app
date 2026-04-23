package com.b2deutsch.app.data.model

data class ReadingPassage(
    val id: String = "",
    val level: String = "B2",
    val category: String = "", // education, technology, health, society, etc.
    val title: String = "",
    val content: String = "", // German text (300-500 words for B2)
    val source: String = "AI_GENERATED",
    val questions: List<ReadingQuestion> = emptyList(),
    val createdAt: Long = System.currentTimeMillis()
)

data class ReadingQuestion(
    val id: String = "",
    val questionText: String = "",
    val type: String = "multiple_choice",
    val options: List<String> = emptyList(),
    val correctAnswer: String = "",
    val explanation: String = ""
)

data class ListeningExercise(
    val id: String = "",
    val level: String = "B2",
    val category: String = "",
    val title: String = "",
    val audioUrl: String = "",
    val transcript: String = "",
    val duration: Int = 0, // seconds
    val difficulty: String = "medium",
    val questions: List<ListeningQuestion> = emptyList()
)

data class ListeningQuestion(
    val id: String = "",
    val questionText: String = "",
    val type: String = "multiple_choice",
    val options: List<String> = emptyList(),
    val correctAnswer: String = "",
    val explanation: String = "",
    val audioTimestamp: Int = 0 // seconds into audio where answer is relevant
)
