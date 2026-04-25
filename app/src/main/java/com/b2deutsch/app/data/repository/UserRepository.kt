package com.b2deutsch.app.data.repository

import com.b2deutsch.app.data.model.User
import com.b2deutsch.app.data.model.UserProgress
import com.b2deutsch.app.data.model.SubjectProgress
import com.b2deutsch.app.data.remote.FirebaseDataSource
import com.b2deutsch.app.util.Constants
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.flow
import javax.inject.Inject
import javax.inject.Singleton

@Singleton
class UserRepository @Inject constructor(
    private val dataSource: FirebaseDataSource
) {
    val currentUserId: String? get() = dataSource.currentUserId
    val isLoggedIn: Boolean get() = dataSource.isLoggedIn

    suspend fun signIn(email: String, password: String): Result<String> {
        return dataSource.signInWithEmail(email, password)
    }

    suspend fun signUp(email: String, password: String, displayName: String): Result<String> {
        return dataSource.signUpWithEmail(email, password, displayName)
    }

    suspend fun signInWithGoogle(idToken: String): Result<String> {
        return dataSource.signInWithGoogle(idToken)
    }

    fun signOut() = dataSource.signOut()

    suspend fun getCurrentUser(): Result<User> {
        val uid = dataSource.currentUserId ?: return Result.failure(Exception("Not logged in"))
        return dataSource.getUser(uid)
    }

    suspend fun getUserProgress(userId: String, level: String): Result<UserProgress> {
        return try {
            val result = dataSource.getUser(userId)
            result.map { user ->
                UserProgress(
                    userId = user.uid,
                    level = user.currentLevel,
                    streak = user.streak
                )
            }
        } catch (e: Exception) {
            Result.failure(e)
        }
    }

    suspend fun updateProgress(progress: UserProgress): Result<Unit> {
        return dataSource.updateUserProgress(progress)
    }

    suspend fun getSubjectProgress(userId: String, subjectId: String): Result<SubjectProgress> {
        // For now, return empty progress - will be implemented when Firestore collection is ready
        return Result.success(
            SubjectProgress(
                userId = userId,
                subjectId = subjectId,
                level = "B2",
                quizzesCompleted = 0,
                bestScore = 0,
                lastAttemptAt = 0,
                isCompleted = false
            )
        )
    }

    fun observeAuthState(): Flow<Boolean> = flow {
        // Simple implementation - in production use FirebaseAuth#addAuthStateListener
        emit(dataSource.isLoggedIn)
    }
}
