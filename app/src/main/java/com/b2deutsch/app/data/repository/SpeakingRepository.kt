package com.b2deutsch.app.data.repository

import com.b2deutsch.app.data.model.SpeakingSession
import com.b2deutsch.app.data.remote.FirebaseDataSource
import javax.inject.Inject
import javax.inject.Singleton

@Singleton
class SpeakingRepository @Inject constructor(
    private val dataSource: FirebaseDataSource
) {
    suspend fun createSession(session: SpeakingSession): Result<String> {
        return dataSource.createSpeakingSession(session)
    }

    suspend fun getSession(sessionId: String): Result<SpeakingSession> {
        return dataSource.getSpeakingSession(sessionId)
    }

    suspend fun uploadRecording(
        userId: String,
        sessionId: String,
        fileName: String,
        audioBytes: ByteArray
    ): Result<String> {
        return dataSource.uploadSpeakingRecording(userId, sessionId, fileName, audioBytes)
    }
}
