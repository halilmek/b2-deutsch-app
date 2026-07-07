package com.b2deutsch.app.ui.vocabulary

import android.app.Application
import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.b2deutsch.app.data.local.VocabularyProgressStore
import com.b2deutsch.app.data.model.VocabularyTheme
import com.b2deutsch.app.data.model.VocabularyWord
import com.b2deutsch.app.data.repository.ContentRepository
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.launch
import javax.inject.Inject

@HiltViewModel
class VocabularyViewModel @Inject constructor(
    private val contentRepository: ContentRepository,
    private val application: Application
) : ViewModel() {

    private val _themes = MutableLiveData<List<VocabularyTheme>>()
    val themes: LiveData<List<VocabularyTheme>> = _themes

    private val _words = MutableLiveData<List<VocabularyWord>>()
    val words: LiveData<List<VocabularyWord>> = _words

    private val _isLoading = MutableLiveData<Boolean>()
    val isLoading: LiveData<Boolean> = _isLoading

    private val _errorMessage = MutableLiveData<String?>()
    val errorMessage: LiveData<String?> = _errorMessage

    fun loadThemes(level: String) {
        viewModelScope.launch {
            _isLoading.value = true
            contentRepository.getVocabularyThemes(level)
                .onSuccess { _themes.value = it }
                .onFailure { _errorMessage.value = "Wortschatz konnte nicht geladen werden." }
            _isLoading.value = false
        }
    }

    fun loadWords(level: String, category: String) {
        viewModelScope.launch {
            _isLoading.value = true
            contentRepository.getVocabularyByCategory(level, category)
                .onSuccess { rawWords ->
                    // Overlay local per-device progress - never trust
                    // isLearned/reviewCount/lastReviewed from Firestore, since
                    // those fields on the shared content doc aren't per-user.
                    _words.value = rawWords.map { word ->
                        word.copy(
                            isLearned = VocabularyProgressStore.isLearned(application, word.id),
                            reviewCount = VocabularyProgressStore.getReviewCount(application, word.id),
                            lastReviewed = VocabularyProgressStore.getLastReviewed(application, word.id)
                        )
                    }
                }
                .onFailure { _errorMessage.value = "Wörter konnten nicht geladen werden." }
            _isLoading.value = false
        }
    }

    /** Words due for review right now, in a stable order (not-yet-learned first). */
    fun getDueWords(): List<VocabularyWord> {
        val all = _words.value ?: return emptyList()
        return all
            .filter { VocabularyProgressStore.isDue(application, it.id) }
            .sortedBy { it.reviewCount }
    }

    fun recordResult(wordId: String, result: String) {
        VocabularyProgressStore.recordResult(application, wordId, result)
    }

    fun resetCategory() {
        val ids = _words.value?.map { it.id } ?: return
        VocabularyProgressStore.resetCategory(application, ids)
    }
}
