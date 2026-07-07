package com.b2deutsch.app.data.model

data class VocabularyWord(
    val id: String = "",
    val level: String = "B2",
    val german: String = "",
    val english: String = "",
    val turkish: String = "",
    val partOfSpeech: String = "", // noun, verb, adjective, adverb
    val exampleSentence: String = "",
    val category: String = "",
    val audioUrl: String = "",
    val isLearned: Boolean = false,
    val reviewCount: Int = 0,
    val lastReviewed: Long = 0
)

data class FlashcardStudySession(
    val wordId: String,
    val result: String // "correct", "hard", "wrong"
)

/**
 * A vocabulary topic category (Firestore `themes` collection - the same
 * taxonomy already used for B2 reading topics: beruf, gesundheit, umwelt...).
 * Level-agnostic and content-driven: adding a new theme document makes it
 * appear here with no code change, same principle as SubjectMapper.kt.
 */
data class VocabularyTheme(
    val id: String = "",
    val name: String = "",
    val iconEmoji: String = "📚",
    val wordCount: Int = 0
)
