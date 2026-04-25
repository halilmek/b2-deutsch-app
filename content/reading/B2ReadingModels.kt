package com.b2deutsch.app.content.reading

/**
 * B2 Reading Comprehension – Data Models
 * Ready for Firestore import
 */

// ============================================================
// TOPIC
// ============================================================
data class ReadingTopic(
    val id: String = "",
    val name: String = "",
    val nameEn: String = "",
    val description: String = "",
    val iconEmoji: String = "",
    val sourceBase: String = "",
    val textCount: Int = 0,
    val quizCount: Int = 0
)

// ============================================================
// READING TEXT (ReadingPassage)
// ============================================================
data class ReadingText(
    val id: String = "",
    val topicId: String = "",
    val title: String = "",
    val source: String = "",
    val sourceUrl: String = "",
    val wordCount: Int = 0,
    val readingTimeMinutes: Int = 0,
    val difficulty: String = "B2",
    val content: String = "",
    val questions: List<ReadingQuestion> = emptyList(),
    val keyVocabulary: List<VocabEntry> = emptyList(),
    val tipsForExam: String = "",
    val tags: List<String> = emptyList()
)

// ============================================================
// QUESTION TYPES
// ============================================================
sealed class ReadingQuestion {
    abstract val id: String
    abstract val questionText: String
    abstract val correctAnswer: String
    abstract val questionType: String
    abstract val explanation: String
}

data class QuestionMC(
    override val id: String,
    override val questionText: String,
    val options: List<String>,
    override val correctAnswer: String,
    override val questionType: String = "multiple_choice",
    override val explanation: String
) : ReadingQuestion()

data class QuestionTF(
    override val id: String,
    override val questionText: String,
    override val correctAnswer: Boolean,  // true = Richtig, false = Falsch
    override val questionType: String = "true_false",
    override val explanation: String
) : ReadingQuestion() {
    // For Firestore: store as string "true" or "false"
    fun correctAnswerAsString(): String = correctAnswer.toString()
}

data class QuestionFIB(
    override val id: String,
    override val questionText: String,  // Contains ___ as blank marker
    override val correctAnswer: String,
    override val questionType: String = "fill_blank",
    override val explanation: String
) : ReadingQuestion()

// ============================================================
// VOCABULARY ENTRY
// ============================================================
data class VocabEntry(
    val german: String = "",
    val english: String = "",
    val turkish: String = "",
    val partOfSpeech: String = ""  // noun, verb, adjective, adverb
)

// ============================================================
// FIRESTORE DOCUMENT WRAPPER
// ============================================================
data class ReadingTextFirestore(
    val id: String = "",
    val topicId: String = "",
    val level: String = "B2",
    val title: String = "",
    val source: String = "",
    val sourceUrl: String = "",
    val wordCount: Int = 0,
    val readingTimeMinutes: Int = 0,
    val difficulty: String = "B2",
    val content: String = "",
    val questionCount: Int = 0,
    val createdAt: Long = System.currentTimeMillis()
)

data class QuizFirestore(
    val id: String = "",
    val topicId: String = "",
    val level: String = "B2",
    val title: String = "",
    val description: String = "",
    val questionCount: Int = 0,
    val timeLimitMinutes: Int = 0,
    val passingScore: Int = 70,
    val isPremium: Boolean = false,
    val sourceTextId: String = "",
    val createdAt: Long = System.currentTimeMillis()
)
