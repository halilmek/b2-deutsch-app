package com.b2deutsch.app.data.model

/**
 * Represents a learning subject/topic within a CEFR level.
 * For example, B2 level might have subjects like:
 * - Grammatik (Konjunktiv II, Passiv, Nebensätze...)
 * - Leseverstehen (Beruf, Gesundheit, Umwelt...)
 * - Wortschatz (topic-based vocabulary)
 * - etc.
 */
data class Subject(
    val id: String = "",
    val level: String = "B2",           // A1, A2, B1, B2, C1
    val name: String = "",               // e.g., "Grammatik: Konjunktiv II"
    val nameShort: String = "",          // e.g., "Konjunktiv II"
    val description: String = "",        // Short explanation (2-3 sentences)
    val category: String = "",           // grammar, vocabulary, reading, listening, writing, speaking
    val iconEmoji: String = "📚",
    val order: Int = 0,
    val quizCount: Int = 0,              // Number of available quizzes
    val isPremium: Boolean = false,
    val tips: List<String> = emptyList() // Learning tips for this subject
)
