package com.b2deutsch.app.data.model

import com.b2deutsch.app.util.Constants

/**
 * Lightweight metadata read from a Firestore `topics/{subjectId}` document.
 * Pure data holder - no Firestore/Android dependency, so the mapping to
 * Subject below is unit-testable without mocking Firestore.
 */
data class TopicMeta(
    val id: String,
    val level: String,
    val name: String,
    val type: String?,
    val questionCount: Long?,
    val description: String? = null,
    val tips: List<String>? = null
)

/**
 * Level-agnostic: builds a Subject purely from what's in the `topics` document.
 * No per-level or per-id branching - a topic added to Firestore (any id, any
 * level) maps through this same code path with no code change.
 */
fun buildSubjectFromTopicMeta(meta: TopicMeta): Subject {
    val order = meta.id.substringAfterLast("_").toIntOrNull() ?: 0
    return Subject(
        id = meta.id,
        level = meta.level,
        name = meta.name,
        nameShort = meta.name,
        description = meta.description ?: "",
        category = categoryForTopicType(meta.type),
        iconEmoji = "📝",
        order = order,
        questionCount = (meta.questionCount ?: 0L).toInt(),
        tips = meta.tips ?: emptyList()
    )
}

fun categoryForTopicType(type: String?): String = when (type) {
    "reading" -> Constants.Categories.READING
    "listening" -> Constants.Categories.LISTENING
    "writing" -> Constants.Categories.WRITING
    "speaking" -> Constants.Categories.SPEAKING
    else -> Constants.Categories.GRAMMAR
}
