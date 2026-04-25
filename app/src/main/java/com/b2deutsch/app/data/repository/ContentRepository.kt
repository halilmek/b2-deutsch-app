package com.b2deutsch.app.data.repository

import com.b2deutsch.app.data.model.*
import com.b2deutsch.app.data.remote.FirebaseDataSource
import javax.inject.Inject
import javax.inject.Singleton

@Singleton
class ContentRepository @Inject constructor(
    private val dataSource: FirebaseDataSource
) {
    // ============ LEVELS ============
    suspend fun getLevels(): Result<List<Level>> = dataSource.getLevels()

    // ============ LESSONS ============
    suspend fun getLessonsByLevel(level: String): Result<List<Lesson>> =
        dataSource.getLessonsByLevel(level)

    suspend fun getLesson(lessonId: String): Result<Lesson> =
        dataSource.getLesson(lessonId)

    // ============ QUIZZES ============
    suspend fun getQuizzesByLevel(level: String): Result<List<Quiz>> =
        dataSource.getQuizzesByLevel(level)

    suspend fun getQuiz(quizId: String): Result<Quiz> =
        dataSource.getQuiz(quizId)

    // ============ QUIZ QUESTIONS ============
    suspend fun getQuestionsByTheme(themeId: String): Result<List<Question>> =
        dataSource.getQuestionsByTheme(themeId)

    suspend fun getQuestionsByReading(readingId: String): Result<List<Question>> =
        dataSource.getQuestionsByReading(readingId)

    // ============ VOCABULARY ============
    suspend fun getVocabularyByLevel(level: String): Result<List<VocabularyWord>> =
        dataSource.getVocabularyByLevel(level)

    suspend fun getVocabularyByCategory(level: String, category: String): Result<List<VocabularyWord>> =
        dataSource.getVocabularyByCategory(level, category)

    // ============ READING ============
    suspend fun getReadingPassages(level: String): Result<List<ReadingPassage>> =
        dataSource.getReadingPassagesByLevel(level)

    // ============ LISTENING ============
    suspend fun getListeningExercises(level: String): Result<List<ListeningExercise>> =
        dataSource.getListeningExercisesByLevel(level)

    // ============ SUBJECTS ============
    suspend fun getSubjectsByLevel(level: String): Result<List<Subject>> =
        dataSource.getSubjectsByLevel(level)

    suspend fun getSubject(subjectId: String): Result<Subject> =
        dataSource.getSubject(subjectId)
}
