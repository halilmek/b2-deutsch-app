package com.b2deutsch.app.ui.auth

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.b2deutsch.app.data.repository.UserRepository
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.launch
import javax.inject.Inject

@HiltViewModel
class AuthViewModel @Inject constructor(
    private val userRepository: UserRepository
) : ViewModel() {

    private val _authState = MutableLiveData<AuthState>()
    val authState: LiveData<AuthState> = _authState

    private val _isLoading = MutableLiveData<Boolean>()
    val isLoading: LiveData<Boolean> = _isLoading

    init {
        checkCurrentUser()
    }

    private fun checkCurrentUser() {
        if (userRepository.isLoggedIn) {
            _authState.value = AuthState.Authenticated(userRepository.currentUserId ?: "")
        } else {
            _authState.value = AuthState.Unauthenticated
        }
    }

    fun signIn(email: String, password: String) {
        viewModelScope.launch {
            _isLoading.value = true
            val result = userRepository.signIn(email, password)
            result.onSuccess { uid ->
                _authState.value = AuthState.Authenticated(uid)
            }.onFailure { error ->
                _authState.value = AuthState.Error(error.message ?: "Sign in failed")
            }
            _isLoading.value = false
        }
    }

    fun signUp(email: String, password: String, displayName: String) {
        viewModelScope.launch {
            _isLoading.value = true
            val result = userRepository.signUp(email, password, displayName)
            result.onSuccess { uid ->
                _authState.value = AuthState.Authenticated(uid)
            }.onFailure { error ->
                _authState.value = AuthState.Error(error.message ?: "Sign up failed")
            }
            _isLoading.value = false
        }
    }

    fun signInWithGoogle(idToken: String) {
        viewModelScope.launch {
            _isLoading.value = true
            val result = userRepository.signInWithGoogle(idToken)
            result.onSuccess { uid ->
                _authState.value = AuthState.Authenticated(uid)
            }.onFailure { error ->
                _authState.value = AuthState.Error(error.message ?: "Google sign in failed")
            }
            _isLoading.value = false
        }
    }

    fun signOut() {
        userRepository.signOut()
        _authState.value = AuthState.Unauthenticated
    }

    fun clearError() {
        _authState.value = AuthState.Unauthenticated
    }
}

sealed class AuthState {
    object Unauthenticated : AuthState()
    data class Authenticated(val userId: String) : AuthState()
    data class Error(val message: String) : AuthState()
}
