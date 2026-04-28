package com.b2deutsch.app

import android.app.Application
import android.util.Log
import com.b2deutsch.app.data.local.LocalQuestionBank
import com.b2deutsch.app.data.sync.FirebaseSyncService
import dagger.hilt.android.HiltAndroidApp
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.SupervisorJob
import kotlinx.coroutines.launch

@HiltAndroidApp
class B2DeutschApp : Application() {

    private val applicationScope = CoroutineScope(SupervisorJob() + Dispatchers.Main)

    override fun onCreate() {
        super.onCreate()

        // Initialize LocalQuestionBank with bundled JSON assets (offline first)
        LocalQuestionBank.initializeFromAssets(this)
        Log.d("B2App", "LocalQuestionBank initialized")

        // Check Firebase for updates (admin push model — runs once per week)
        applicationScope.launch {
            val result = FirebaseSyncService.syncIfNeeded(applicationContext)
            when (result) {
                is FirebaseSyncService.SyncResult.SUCCESS -> {
                    Log.d("B2App", "Firebase sync: ${result.topicsUpdated} topics updated")
                }
                is FirebaseSyncService.SyncResult.UP_TO_DATE -> {
                    Log.d("B2App", "Firebase sync: content is up to date")
                }
                is FirebaseSyncService.SyncResult.SKIPPED -> {
                    Log.d("B2App", "Firebase sync: skipped (checked recently)")
                }
                is FirebaseSyncService.SyncResult.FAILED -> {
                    Log.w("B2App", "Firebase sync failed: ${result.error}")
                }
            }
        }
    }
}
