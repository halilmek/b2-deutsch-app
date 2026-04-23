package com.b2deutsch.app

import android.app.Application
import dagger.hilt.android.HiltAndroidApp

@HiltAndroidApp
class B2DeutschApp : Application() {

    override fun onCreate() {
        super.onCreate()
        // Initialize any app-wide configurations here
    }
}
