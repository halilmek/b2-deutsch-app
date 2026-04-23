package com.b2deutsch.app.data.repository

import com.b2deutsch.app.data.model.WritingSubmission
import com.b2deutsch.app.data.remote.FirebaseDataSource
import javax.inject.Inject
import javax.inject.Singleton

@Singleton
class WritingRepository @Inject constructor(
    private val dataSource: FirebaseDataSource
) {
    suspend fun submitWriting(submission: WritingSubmission): Result<String> {
        return dataSource.submitWriting(submission)
    }

    suspend fun getSubmission(submissionId: String): Result<WritingSubmission> {
        return dataSource.getWritingSubmission(submissionId)
    }
}
