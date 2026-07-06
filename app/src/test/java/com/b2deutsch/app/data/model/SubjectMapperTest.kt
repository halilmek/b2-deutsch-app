package com.b2deutsch.app.data.model

import com.b2deutsch.app.util.Constants
import org.junit.Assert.assertEquals
import org.junit.Test

/**
 * Proves SubjectListViewModel's old hardcoded-per-level-list bug can't recur:
 * buildSubjectFromTopicMeta has no per-level or per-id branching, so a brand
 * new topic that no code in this repo has ever referenced maps correctly with
 * zero code changes required.
 */
class SubjectMapperTest {

    @Test
    fun `a topic never referenced anywhere in the codebase appears correctly`() {
        val meta = TopicMeta(
            id = "c2_99",
            level = "C2",
            name = "Ein brandneues Thema",
            type = "grammar",
            questionCount = 42L
        )

        val subject = buildSubjectFromTopicMeta(meta)

        assertEquals("c2_99", subject.id)
        assertEquals("C2", subject.level)
        assertEquals("Ein brandneues Thema", subject.name)
        assertEquals("Ein brandneues Thema", subject.nameShort)
        assertEquals(99, subject.order)
        assertEquals(42, subject.questionCount)
        assertEquals(Constants.Categories.GRAMMAR, subject.category)
    }

    @Test
    fun `order is derived from the numeric suffix of the topic id, not a hardcoded position`() {
        val meta = TopicMeta(id = "a1_07", level = "A1", name = "Irgendein Thema", type = "grammar", questionCount = 60L)
        assertEquals(7, buildSubjectFromTopicMeta(meta).order)
    }

    @Test
    fun `category is derived from topic type, not level`() {
        assertEquals(Constants.Categories.READING, categoryForTopicType("reading"))
        assertEquals(Constants.Categories.LISTENING, categoryForTopicType("listening"))
        assertEquals(Constants.Categories.WRITING, categoryForTopicType("writing"))
        assertEquals(Constants.Categories.SPEAKING, categoryForTopicType("speaking"))
        assertEquals(Constants.Categories.GRAMMAR, categoryForTopicType("grammar"))
        assertEquals(Constants.Categories.GRAMMAR, categoryForTopicType(null))
    }
}
