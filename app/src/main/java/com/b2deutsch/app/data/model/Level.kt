package com.b2deutsch.app.data.model

data class Level(
    val id: String = "",
    val name: String = "",
    val description: String = "",
    val order: Int = 0,
    val isLocked: Boolean = false,
    val iconUrl: String = ""
)
