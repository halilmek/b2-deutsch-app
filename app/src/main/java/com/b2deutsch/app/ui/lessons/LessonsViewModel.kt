package com.b2deutsch.app.ui.lessons

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.b2deutsch.app.data.model.Lesson
import com.b2deutsch.app.data.repository.ContentRepository
import com.b2deutsch.app.util.Constants
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.launch
import javax.inject.Inject

@HiltViewModel
class LessonsViewModel @Inject constructor(
    private val contentRepository: ContentRepository
) : ViewModel() {

    private val _lessons = MutableLiveData<List<Lesson>>()
    val lessons: LiveData<List<Lesson>> = _lessons

    private val _selectedLesson = MutableLiveData<Lesson?>()
    val selectedLesson: LiveData<Lesson?> = _selectedLesson

    private val _isLoading = MutableLiveData<Boolean>()
    val isLoading: LiveData<Boolean> = _isLoading

    private val _error = MutableLiveData<String?>()
    val error: LiveData<String?> = _error

    fun loadLessons(level: String = Constants.DEFAULT_LEVEL) {
        viewModelScope.launch {
            _isLoading.value = true
            _error.value = null

            contentRepository.getLessonsByLevel(level)
                .onSuccess { lessonList ->
                    _lessons.value = lessonList
                }
                .onFailure { e ->
                    _error.value = e.message
                    // Use sample data for demo
                    _lessons.value = getSampleLessons(level)
                }

            _isLoading.value = false
        }
    }

    fun selectLesson(lessonId: String) {
        viewModelScope.launch {
            _isLoading.value = true
            contentRepository.getLesson(lessonId)
                .onSuccess { lesson ->
                    _selectedLesson.value = lesson
                }
                .onFailure {
                    // Try from cached list
                    _selectedLesson.value = _lessons.value?.find { it.id == lessonId }
                }
            _isLoading.value = false
        }
    }

    private fun getSampleLessons(level: String): List<Lesson> {
        return when (level) {
            "B2" -> listOf(
                Lesson(
                    id = "b2_gram_1",
                    level = "B2",
                    category = Constants.Categories.GRAMMAR,
                    title = "Passive Voice",
                    description = "Learn to use passive constructions in B2 German",
                    order = 1,
                    duration = 20
                ),
                Lesson(
                    id = "b2_gram_2",
                    level = "B2",
                    category = Constants.Categories.GRAMMAR,
                    title = "Subjunctive II",
                    description = "Conditional and hypothetical statements",
                    order = 2,
                    duration = 25
                ),
                Lesson(
                    id = "b2_vocab_1",
                    level = "B2",
                    category = Constants.Categories.VOCABULARY,
                    title = "Business German",
                    description = "Professional vocabulary for the workplace",
                    order = 3,
                    duration = 15
                ),
                Lesson(
                    id = "b2_read_1",
                    level = "B2",
                    category = Constants.Categories.READING,
                    title = "Technology & Society",
                    description = "Reading comprehension on modern technology",
                    order = 4,
                    duration = 30
                )
            )
            else -> listOf(
                Lesson(
                    id = "${level.lowercase()}_gram_1",
                    level = level,
                    category = Constants.Categories.GRAMMAR,
                    title = "Grammar Basics",
                    description = "Essential grammar for $level level",
                    order = 1,
                    duration = 20
                )
            )
        }
    }
}
