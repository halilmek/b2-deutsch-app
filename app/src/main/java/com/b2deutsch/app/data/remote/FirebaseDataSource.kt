package com.b2deutsch.app.data.remote

import com.b2deutsch.app.data.model.*
import com.b2deutsch.app.util.Constants
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.firestore.FirebaseFirestore
import com.google.firebase.storage.FirebaseStorage
import kotlinx.coroutines.tasks.await
import javax.inject.Inject
import javax.inject.Singleton

@Singleton
class FirebaseDataSource @Inject constructor(
    private val auth: FirebaseAuth,
    private val firestore: FirebaseFirestore,
    private val storage: FirebaseStorage
) {
    // ============ AUTH ============
    val currentUserId: String? get() = auth.currentUser?.uid
    val isLoggedIn: Boolean get() = auth.currentUser != null

    suspend fun signInWithEmail(email: String, password: String): Result<String> {
        return try {
            val result = auth.signInWithEmailAndPassword(email, password).await()
            Result.success(result.user?.uid ?: "")
        } catch (e: Exception) {
            Result.failure(e)
        }
    }

    suspend fun signUpWithEmail(email: String, password: String, displayName: String): Result<String> {
        return try {
            val result = auth.createUserWithEmailAndPassword(email, password).await()
            val userId = result.user?.uid ?: throw Exception("User creation failed")
            // Create user document in Firestore
            saveUser(userId, email, displayName)
            Result.success(userId)
        } catch (e: Exception) {
            Result.failure(e)
        }
    }

    suspend fun signInWithGoogle(idToken: String): Result<String> {
        return try {
            val result = auth.signInWithCredential(
                com.google.firebase.auth.GoogleAuthProvider.getCredential(idToken, null)
            ).await()
            Result.success(result.user?.uid ?: "")
        } catch (e: Exception) {
            Result.failure(e)
        }
    }

    fun signOut() = auth.signOut()

    // ============ USER ============
    private suspend fun saveUser(uid: String, email: String, displayName: String) {
        val user = User(
            uid = uid,
            email = email,
            displayName = displayName,
            currentLevel = Constants.DEFAULT_LEVEL,
            subscriptionTier = Constants.SubscriptionTier.FREE
        )
        firestore.collection(Constants.Collections.USERS)
            .document(uid)
            .set(user)
            .await()
    }

    suspend fun getUser(uid: String): Result<User> {
        return try {
            val doc = firestore.collection(Constants.Collections.USERS)
                .document(uid)
                .get()
                .await()
            val user = doc.toObject(User::class.java) ?: throw Exception("User not found")
            Result.success(user)
        } catch (e: Exception) {
            Result.failure(e)
        }
    }

    suspend fun updateUserProgress(progress: UserProgress): Result<Unit> {
        return try {
            firestore.collection(Constants.Collections.USER_PROGRESS)
                .document("${progress.userId}_${progress.level}")
                .set(progress)
                .await()
            Result.success(Unit)
        } catch (e: Exception) {
            Result.failure(e)
        }
    }

    // ============ LEVELS ============
    suspend fun getLevels(): Result<List<Level>> {
        return try {
            val snapshot = firestore.collection(Constants.Collections.LEVELS)
                .orderBy("order")
                .get()
                .await()
            val levels = snapshot.toObjects(Level::class.java)
            Result.success(levels)
        } catch (e: Exception) {
            Result.failure(e)
        }
    }

    // ============ LESSONS ============
    suspend fun getLessonsByLevel(level: String): Result<List<Lesson>> {
        return try {
            val snapshot = firestore.collection(Constants.Collections.LESSONS)
                .whereEqualTo("level", level)
                .orderBy("order")
                .get()
                .await()
            val lessons = snapshot.toObjects(Lesson::class.java)
            Result.success(lessons)
        } catch (e: Exception) {
            Result.failure(e)
        }
    }

    suspend fun getLesson(lessonId: String): Result<Lesson> {
        return try {
            val doc = firestore.collection(Constants.Collections.LESSONS)
                .document(lessonId)
                .get()
                .await()
            val lesson = doc.toObject(Lesson::class.java) ?: throw Exception("Lesson not found")
            Result.success(lesson)
        } catch (e: Exception) {
            Result.failure(e)
        }
    }

    // ============ QUIZZES ============
    suspend fun getQuizzesByLevel(level: String): Result<List<Quiz>> {
        return try {
            val snapshot = firestore.collection(Constants.Collections.QUIZZES)
                .whereEqualTo("level", level)
                .get()
                .await()
            val quizzes = snapshot.toObjects(Quiz::class.java)
            Result.success(quizzes)
        } catch (e: Exception) {
            Result.failure(e)
        }
    }

    suspend fun getQuiz(quizId: String): Result<Quiz> {
        return try {
            val doc = firestore.collection(Constants.Collections.QUIZZES)
                .document(quizId)
                .get()
                .await()
            val quiz = doc.toObject(Quiz::class.java) ?: throw Exception("Quiz not found")
            Result.success(quiz)
        } catch (e: Exception) {
            Result.failure(e)
        }
    }

    // ============ QUIZ QUESTIONS FROM QUIZBANK ============
    suspend fun getQuestionsByTheme(themeId: String): Result<List<Question>> {
        return try {
            val snapshot = firestore.collection("quizBank")
                .whereEqualTo("themeId", themeId)
                .get()
                .await()
            val questions = snapshot.documents.mapNotNull { doc ->
                doc.toObject(Question::class.java)
            }
            Result.success(questions)
        } catch (e: Exception) {
            Result.failure(e)
        }
    }


    suspend fun getQuestionsByReading(readingId: String): Result<List<Question>> {
        return try {
            val snapshot = firestore.collection("readings")
                .document(readingId)
                .collection("questions")
                .get()
                .await()
            val questions = snapshot.toObjects(Question::class.java)
            Result.success(questions)
        } catch (e: Exception) {
            Result.failure(e)
        }
    }

    suspend fun getQuestionsBySubject(subjectId: String): Result<List<Question>> {
        return try {
            // Query quizBank for questions that have this subjectId in their array
            val snapshot = firestore.collection("quizBank")
                .whereArrayContains("subjectIds", subjectId)
                .get()
                .await()
            val questions = snapshot.documents.mapNotNull { doc ->
                doc.toObject(Question::class.java)
            }
            Result.success(questions)
        } catch (e: Exception) {
            Result.failure(e)
        }
    }

    // ============ VOCABULARY ============
    suspend fun getVocabularyByLevel(level: String): Result<List<VocabularyWord>> {
        return try {
            val snapshot = firestore.collection(Constants.Collections.VOCABULARY)
                .whereEqualTo("level", level)
                .get()
                .await()
            val words = snapshot.toObjects(VocabularyWord::class.java)
            Result.success(words)
        } catch (e: Exception) {
            Result.failure(e)
        }
    }

    suspend fun getVocabularyByCategory(level: String, category: String): Result<List<VocabularyWord>> {
        return try {
            val snapshot = firestore.collection(Constants.Collections.VOCABULARY)
                .whereEqualTo("level", level)
                .whereEqualTo("category", category)
                .get()
                .await()
            val words = snapshot.toObjects(VocabularyWord::class.java)
            Result.success(words)
        } catch (e: Exception) {
            Result.failure(e)
        }
    }

    // ============ READING ============
    suspend fun getReadingPassagesByLevel(level: String): Result<List<ReadingPassage>> {
        return try {
            val snapshot = firestore.collection(Constants.Collections.READING_PASSAGES)
                .whereEqualTo("level", level)
                .get()
                .await()
            val passages = snapshot.toObjects(ReadingPassage::class.java)
            Result.success(passages)
        } catch (e: Exception) {
            Result.failure(e)
        }
    }

    suspend fun getReadingsBySubject(subjectId: String): Result<List<ReadingPassage>> {
        return try {
            val snapshot = firestore.collection("readings")
                .whereEqualTo("subjectId", subjectId)
                .get()
                .await()
            val passages = snapshot.toObjects(ReadingPassage::class.java)
            Result.success(passages)
        } catch (e: Exception) {
            Result.failure(e)
        }
    }

    suspend fun getReadingsByTheme(themeId: String): Result<List<ReadingPassage>> {
        return try {
            val snapshot = firestore.collection("readings")
                .whereEqualTo("themeId", themeId)
                .get()
                .await()
            val passages = snapshot.toObjects(ReadingPassage::class.java)
            Result.success(passages)
        } catch (e: Exception) {
            Result.failure(e)
        }
    }

    // ============ LISTENING ============
    suspend fun getListeningExercisesByLevel(level: String): Result<List<ListeningExercise>> {
        return try {
            val snapshot = firestore.collection(Constants.Collections.LISTENING_EXERCISES)
                .whereEqualTo("level", level)
                .get()
                .await()
            val exercises = snapshot.toObjects(ListeningExercise::class.java)
            Result.success(exercises)
        } catch (e: Exception) {
            Result.failure(e)
        }
    }

    // ============ SUBJECTS ============
    // Subjects are generated locally in SubjectListViewModel.getDefaultSubjects()
    // This method can be used when subjects are stored in Firestore
    suspend fun getSubjectsByLevel(level: String): Result<List<Subject>> {
        return Result.failure(Exception("Subjects loaded from local defaults"))
    }

    suspend fun getSubject(subjectId: String): Result<Subject> {
        return Result.failure(Exception("Subject not found in Firestore"))
    }

    // ============ WRITING ============
    suspend fun submitWriting(submission: WritingSubmission): Result<String> {
        return try {
            val docRef = firestore.collection(Constants.Collections.WRITING_SUBMISSIONS)
                .document()
            val updatedSubmission = submission.copy(id = docRef.id)
            docRef.set(updatedSubmission).await()
            Result.success(docRef.id)
        } catch (e: Exception) {
            Result.failure(e)
        }
    }

    suspend fun getWritingSubmission(submissionId: String): Result<WritingSubmission> {
        return try {
            val doc = firestore.collection(Constants.Collections.WRITING_SUBMISSIONS)
                .document(submissionId)
                .get()
                .await()
            val submission = doc.toObject(WritingSubmission::class.java) ?: throw Exception("Submission not found")
            Result.success(submission)
        } catch (e: Exception) {
            Result.failure(e)
        }
    }

    // ============ SPEAKING ============
    suspend fun createSpeakingSession(session: SpeakingSession): Result<String> {
        return try {
            val docRef = firestore.collection(Constants.Collections.SPEAKING_SESSIONS)
                .document()
            val updatedSession = session.copy(id = docRef.id)
            docRef.set(updatedSession).await()
            Result.success(docRef.id)
        } catch (e: Exception) {
            Result.failure(e)
        }
    }

    suspend fun getSpeakingSession(sessionId: String): Result<SpeakingSession> {
        return try {
            val doc = firestore.collection(Constants.Collections.SPEAKING_SESSIONS)
                .document(sessionId)
                .get()
                .await()
            val session = doc.toObject(SpeakingSession::class.java) ?: throw Exception("Session not found")
            Result.success(session)
        } catch (e: Exception) {
            Result.failure(e)
        }
    }

    // ============ STORAGE ============
    suspend fun uploadAudioRecording(userId: String, fileName: String, audioBytes: ByteArray): Result<String> {
        return try {
            val ref = storage.reference
                .child("audio")
                .child(userId)
                .child(fileName)
            ref.putBytes(audioBytes).await()
            val downloadUrl = ref.downloadUrl.await().toString()
            Result.success(downloadUrl)
        } catch (e: Exception) {
            Result.failure(e)
        }
    }

    suspend fun uploadSpeakingRecording(userId: String, sessionId: String, fileName: String, audioBytes: ByteArray): Result<String> {
        return try {
            val ref = storage.reference
                .child("recordings")
                .child(userId)
                .child(sessionId)
                .child(fileName)
            ref.putBytes(audioBytes).await()
            val downloadUrl = ref.downloadUrl.await().toString()
            Result.success(downloadUrl)
        } catch (e: Exception) {
            Result.failure(e)
        }
    }
}
