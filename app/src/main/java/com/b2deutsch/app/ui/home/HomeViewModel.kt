package com.b2deutsch.app.ui.home

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.b2deutsch.app.data.model.Level
import com.b2deutsch.app.data.model.User
import com.b2deutsch.app.data.model.UserProgress
import com.b2deutsch.app.data.repository.ContentRepository
import com.b2deutsch.app.data.repository.UserRepository
import com.b2deutsch.app.util.Constants
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.launch
import javax.inject.Inject

@HiltViewModel
class HomeViewModel @Inject constructor(
    private val userRepository: UserRepository,
    private val contentRepository: ContentRepository
) : ViewModel() {

    private val _currentUser = MutableLiveData<User?>()
    val currentUser: LiveData<User?> = _currentUser

    private val _levels = MutableLiveData<List<Level>>()
    val levels: LiveData<List<Level>> = _levels

    private val _userProgress = MutableLiveData<UserProgress?>()
    val userProgress: LiveData<UserProgress?> = _userProgress

    private val _currentLevel = MutableLiveData(Constants.DEFAULT_LEVEL)
    val currentLevel: LiveData<String> = _currentLevel

    private val _isLoading = MutableLiveData<Boolean>()
    val isLoading: LiveData<Boolean> = _isLoading

    fun loadData() {
        viewModelScope.launch {
            _isLoading.value = true

            // Load user
            userRepository.getCurrentUser().onSuccess { user ->
                _currentUser.value = user
                _currentLevel.value = user.currentLevel
            }

            // Load levels
            contentRepository.getLevels().onSuccess { levelList ->
                if (levelList.isEmpty()) {
                    // Seed default levels if none exist
                    _levels.value = getDefaultLevels()
                } else {
                    _levels.value = levelList
                }
            }.onFailure {
                _levels.value = getDefaultLevels()
            }

            // Load progress
            val userId = userRepository.currentUserId
            if (userId != null) {
                userRepository.getUserProgress(userId, _currentLevel.value ?: Constants.DEFAULT_LEVEL)
                    .onSuccess { progress ->
                        _userProgress.value = progress
                    }
            }

            _isLoading.value = false
        }
    }

    fun setCurrentLevel(level: String) {
        _currentLevel.value = level
        // Reload progress for new level
        val userId = userRepository.currentUserId
        if (userId != null) {
            viewModelScope.launch {
                userRepository.getUserProgress(userId, level).onSuccess { progress ->
                    _userProgress.value = progress
                }
            }
        }
    }

    private fun getDefaultLevels(): List<Level> = listOf(
        Level("A1", "A1", "Elementary", 1, isLocked = false),
        Level("A2", "A2", "Pre-Intermediate", 2, isLocked = false),
        Level("B1", "B1", "Intermediate", 3, isLocked = false),
        Level("B2", "B2", "Upper-Intermediate", 4, isLocked = false),
        Level("C1", "C1", "Advanced", 5, isLocked = false)
    )
}
