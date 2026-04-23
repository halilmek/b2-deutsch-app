package com.b2deutsch.app.data.model

data class Quiz(
    val id: String = "",
    val level: String = "B2",
    val lessonId: String = "",
    val category: String = "",
    val title: String = "",
    val description: String = "",
    val taskType: String = "", // reading, listening, writing, speaking
    val timeLimit: Int = 0, // minutes
    val passingScore: Int = 70,
    val questions: List<Question> = emptyList(),
    val isPremium: Boolean = false
)

data class Question(
    val id: String = "",
    val type: String = "multiple_choice", // multiple_choice, true_false, fill_blank
    val questionText: String = "",
    val options: List<String> = emptyList(),
    val correctAnswer: String = "",
    val explanation: String = ""
)

data class QuizResult(
    val quizId: String = "",
    val userId: String = "",
    val score: Int = 0,
    val totalQuestions: Int = 0,
    val correctAnswers: Int = 0,
    val passed: Boolean = false,
    val completedAt: Long = System.currentTimeMillis(),
    val timeSpent: Int = 0 // seconds
)
