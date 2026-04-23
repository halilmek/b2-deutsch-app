package com.b2deutsch.app.ui.quiz

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.b2deutsch.app.data.model.Question
import com.b2deutsch.app.data.model.Quiz
import com.b2deutsch.app.data.model.QuizResult
import com.b2deutsch.app.data.repository.ContentRepository
import com.b2deutsch.app.data.repository.UserRepository
import com.b2deutsch.app.util.Constants
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.launch
import javax.inject.Inject

@HiltViewModel
class QuizViewModel @Inject constructor(
    private val contentRepository: ContentRepository,
    private val userRepository: UserRepository
) : ViewModel() {

    private val _quizzes = MutableLiveData<List<Quiz>>()
    val quizzes: LiveData<List<Quiz>> = _quizzes

    private val _currentQuiz = MutableLiveData<Quiz?>()
    val currentQuiz: LiveData<Quiz?> = _currentQuiz

    private val _currentQuestionIndex = MutableLiveData(0)
    val currentQuestionIndex: LiveData<Int> = _currentQuestionIndex

    private val _currentQuestion = MutableLiveData<Question?>()
    val currentQuestion: LiveData<Question?> = _currentQuestion

    private val _selectedAnswers = MutableLiveData<MutableMap<Int, String>>(mutableMapOf())
    val selectedAnswers: LiveData<MutableMap<Int, String>> = _selectedAnswers

    private val _quizResult = MutableLiveData<QuizResult?>()
    val quizResult: LiveData<QuizResult?> = _quizResult

    private val _isLoading = MutableLiveData<Boolean>()
    val isLoading: LiveData<Boolean> = _isLoading

    private var timeRemaining = 0
    private var quizStartTime = 0L

    fun loadQuizzes(level: String = Constants.DEFAULT_LEVEL) {
        viewModelScope.launch {
            _isLoading.value = true
            contentRepository.getQuizzesByLevel(level)
                .onSuccess { quizList ->
                    _quizzes.value = quizList
                }
                .onFailure {
                    _quizzes.value = getSampleQuizzes(level)
                }
            _isLoading.value = false
        }
    }

    fun startQuiz(quizId: String) {
        viewModelScope.launch {
            _isLoading.value = true
            contentRepository.getQuiz(quizId)
                .onSuccess { quiz ->
                    _currentQuiz.value = quiz
                    _currentQuestionIndex.value = 0
                    _selectedAnswers.value = mutableMapOf()
                    _quizResult.value = null
                    timeRemaining = quiz.timeLimit * 60
                    quizStartTime = System.currentTimeMillis()
                    updateCurrentQuestion()
                }
                .onFailure {
                    // Try from cached list
                    val quiz = _quizzes.value?.find { it.id == quizId }
                    if (quiz != null) {
                        _currentQuiz.value = quiz
                        _currentQuestionIndex.value = 0
                        updateCurrentQuestion()
                    }
                }
            _isLoading.value = false
        }
    }

    fun selectAnswer(questionIndex: Int, answer: String) {
        val answers = _selectedAnswers.value ?: mutableMapOf()
        answers[questionIndex] = answer
        _selectedAnswers.value = answers
    }

    fun nextQuestion() {
        val currentIndex = _currentQuestionIndex.value ?: 0
        val quiz = _currentQuiz.value ?: return

        if (currentIndex < quiz.questions.size - 1) {
            _currentQuestionIndex.value = currentIndex + 1
            updateCurrentQuestion()
        }
    }

    fun previousQuestion() {
        val currentIndex = _currentQuestionIndex.value ?: 0
        if (currentIndex > 0) {
            _currentQuestionIndex.value = currentIndex - 1
            updateCurrentQuestion()
        }
    }

    private fun updateCurrentQuestion() {
        val quiz = _currentQuiz.value ?: return
        val index = _currentQuestionIndex.value ?: 0
        if (index < quiz.questions.size) {
            _currentQuestion.value = quiz.questions[index]
        }
    }

    fun submitQuiz() {
        val quiz = _currentQuiz.value ?: return
        val answers = _selectedAnswers.value ?: emptyMap()
        val userId = userRepository.currentUserId ?: "anonymous"

        var correctCount = 0
        quiz.questions.forEachIndexed { index, question ->
            if (answers[index] == question.correctAnswer) {
                correctCount++
            }
        }

        val totalQuestions = quiz.questions.size
        val score = if (totalQuestions > 0) (correctCount * 100) / totalQuestions else 0
        val timeSpent = ((System.currentTimeMillis() - quizStartTime) / 1000).toInt()

        _quizResult.value = QuizResult(
            quizId = quiz.id,
            userId = userId,
            score = score,
            totalQuestions = totalQuestions,
            correctAnswers = correctCount,
            passed = score >= quiz.passingScore,
            timeSpent = timeSpent
        )
    }

    private fun getSampleQuizzes(level: String): List<Quiz> {
        return listOf(
            Quiz(
                id = "${level.lowercase()}_quiz_1",
                level = level,
                category = Constants.Categories.GRAMMAR,
                title = "Grammar Quiz",
                taskType = "grammar",
                timeLimit = 10,
                passingScore = 70,
                questions = listOf(
                    Question(
                        id = "q1",
                        type = Constants.QuizTypes.MULTIPLE_CHOICE,
                        questionText = "Welches Wort ist korrekt? \"Er ___ das Buch gelesen.\"",
                        options = listOf("hat", "ist", "wird", "hatte"),
                        correctAnswer = "hat",
                        explanation = "Perfekt with 'haben' for verbs that don't show movement."
                    ),
                    Question(
                        id = "q2",
                        type = Constants.QuizTypes.TRUE_FALSE,
                        questionText = "Im Passiv wird das Subjekt zum Objekt.",
                        options = listOf("Wahr", "Falsch"),
                        correctAnswer = "Wahr",
                        explanation = "In passive voice, the object of the active sentence becomes the subject."
                    )
                )
            )
        )
    }
}
