package com.b2deutsch.app.data.model

data class Level(
    val id: String = "",
    val name: String = "",
    val description: String = "",
    val order: Int = 0,
    val isLocked: Boolean = false,
    val iconUrl: String = ""
)

data class Lesson(
    val id: String = "",
    val level: String = "B2",
    val category: String = "",
    val title: String = "",
    val description: String = "",
    val order: Int = 0,
    val duration: Int = 0, // minutes
    val isPremium: Boolean = false,
    val sections: List<LessonSection> = emptyList()
)

data class LessonSection(
    val type: String = "text", // text, example, grammar, table
    val title: String = "",
    val content: String = ""
)
