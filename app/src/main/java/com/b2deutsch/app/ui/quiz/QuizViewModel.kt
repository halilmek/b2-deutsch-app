package com.b2deutsch.app.ui.quiz

import android.app.Application
import android.util.Log
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.viewModelScope
import com.b2deutsch.app.data.local.LocalQuestionBank
import com.b2deutsch.app.data.model.Question
import com.b2deutsch.app.data.model.Quiz
import com.b2deutsch.app.data.model.QuizResult
import com.b2deutsch.app.data.model.WrongAnswer
import com.b2deutsch.app.data.repository.UserRepository
import com.b2deutsch.app.util.Constants
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import javax.inject.Inject

@HiltViewModel
class QuizViewModel @Inject constructor(
    private val userRepository: UserRepository,
    private val application: Application
) : AndroidViewModel(application) {

    private val TAG = "QuizViewModel"

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

    private val _quizMessage = MutableLiveData<String?>()
    val quizMessage: LiveData<String?> = _quizMessage

    private val _isComplete = MutableLiveData(false)
    val isComplete: LiveData<Boolean> = _isComplete

    private var quizStartTime = 0L
    private var currentSubjectId = ""
    private var currentQuizQuestionIds = listOf<String>()  // track IDs for completion

    init {
        // Initialize question bank from assets on startup
        viewModelScope.launch {
            withContext(Dispatchers.IO) {
                LocalQuestionBank.initializeFromAssets(application)
            }
        }
    }

    /**
     * Start a quiz for a grammar topic (subjectId like "b2_01").
     * Uses LOCAL question bank (100 questions per topic, offline-capable).
     * Selects 10 random questions from ACTIVE (unsolved) pool.
     */
    fun startQuiz(subjectId: String) {
        currentSubjectId = subjectId
        viewModelScope.launch {
            _isLoading.value = true
            _selectedAnswers.value = mutableMapOf()
            _quizResult.value = null
            _quizMessage.value = null
            _isComplete.value = false

            val result = withContext(Dispatchers.IO) {
                LocalQuestionBank.getNextQuiz(application, subjectId)
            }

            if (result.isComplete) {
                // All 100 questions done!
                _isComplete.value = true
                _quizMessage.value = result.message
                _isLoading.value = false
                return@launch
            }

            if (result.isLooping) {
                _quizMessage.value = result.message
            }

            // Build Quiz object from question details
            val questions = result.questions.map { q ->
                Question(
                    id = q.id,
                    type = q.type,
                    questionText = q.questionText,
                    options = q.options,
                    correctAnswer = q.correctAnswer,
                    explanation = q.explanation
                )
            }

            // Track these IDs so we can mark them solved after quiz
            currentQuizQuestionIds = questions.map { it.id }

            val quiz = Quiz(
                id = "${subjectId}_quiz",
                level = "B2",
                category = Constants.Categories.GRAMMAR,
                title = getSubjectTitle(subjectId),
                taskType = "grammar",
                timeLimit = 15,
                passingScore = 60,
                questions = questions
            )

            _currentQuiz.value = quiz
            _currentQuestionIndex.value = 0
            quizStartTime = System.currentTimeMillis()
            updateCurrentQuestion()
            _isLoading.value = false

            Log.d(TAG, "Quiz started: ${questions.size} questions, ${result.remainingActive} remaining active")
        }
    }

    fun selectAnswer(answer: String) {
        val index = _currentQuestionIndex.value ?: 0
        val answers = _selectedAnswers.value ?: mutableMapOf()
        answers[index] = answer
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

    /**
     * Submit quiz: calculate score, mark questions as solved, save result.
     */
    fun submitQuiz() {
        val quiz = _currentQuiz.value ?: return
        val answers = _selectedAnswers.value ?: emptyMap()
        val userId = userRepository.currentUserId ?: "anonymous"

        var correctCount = 0
        val wrongAnswerList = mutableListOf<WrongAnswer>()

        quiz.questions.forEachIndexed { index, question ->
            val userAnswer = answers[index] ?: ""
            if (userAnswer == question.correctAnswer) {
                correctCount++
            } else {
                wrongAnswerList.add(WrongAnswer(
                    questionText = question.questionText,
                    yourAnswer = userAnswer.ifEmpty { "Keine Antwort" },
                    correctAnswer = question.correctAnswer,
                    explanation = question.explanation.ifEmpty { "Keine Erklärung verfügbar" }
                ))
            }
        }

        val totalQuestions = quiz.questions.size
        val score = if (totalQuestions > 0) (correctCount * 100) / totalQuestions else 0
        val timeSpent = ((System.currentTimeMillis() - quizStartTime) / 1000).toInt()

        // Mark these 10 questions as solved (passive) in local bank
        viewModelScope.launch {
            withContext(Dispatchers.IO) {
                LocalQuestionBank.markQuizCompleted(
                    application,
                    currentSubjectId,
                    currentQuizQuestionIds
                )
            }
        }

        _quizResult.value = QuizResult(
            quizId = quiz.id,
            userId = userId,
            score = score,
            totalQuestions = totalQuestions,
            correctAnswers = correctCount,
            passed = score >= quiz.passingScore,
            timeSpent = timeSpent,
            wrongAnswers = wrongAnswerList
        )
    }

    /**
     * Next Quiz: get next 10 random questions from active pool.
     */
    fun startNextQuiz() {
        startQuiz(currentSubjectId)
    }

    /**
     * Reset topic progress: all 100 back to active (unsolved).
     */
    fun resetTopicProgress() {
        viewModelScope.launch(Dispatchers.IO) {
            LocalQuestionBank.resetTopic(application, currentSubjectId)
        }
        _isComplete.value = false
        _quizMessage.value = null
    }

    /**
     * Retry same batch: reload last 10 questions (same IDs, same order).
     */
    fun retryQuiz() {
        val quiz = _currentQuiz.value ?: return
        _selectedAnswers.value = mutableMapOf()
        _quizResult.value = null
        _currentQuestionIndex.value = 0
        quizStartTime = System.currentTimeMillis()
        updateCurrentQuestion()
    }

    /**
     * Progress string like "70/100 gelöst"
     */
    fun getProgressString(): String {
        return LocalQuestionBank.getProgressString(application, currentSubjectId)
    }

    /**
     * Get remaining active questions count
     */
    fun getRemainingCount(): Int {
        return LocalQuestionBank.getRemainingCount(application, currentSubjectId)
    }

    private fun getSubjectTitle(subjectId: String): String {
        val titles = mapOf(
            "b2_01" to "1. Konnektoren: als, bevor, bis, seitdem, wahrend, wenn",
            "b2_02" to "2. Konnektoren: sobald, solange",
            "b2_03" to "3. Verben und Erganzungen",
            "b2_04" to "4. Zeitformen in der Vergangenheit",
            "b2_05" to "5. Zeitformen der Zukunft",
            "b2_06" to "6. Futur mit werden",
            "b2_07" to "7. Angaben im Satz",
            "b2_08" to "8. Verneinung mit nicht",
            "b2_09" to "9. Negationsworter",
            "b2_10" to "10. Passiv Prateritum",
            "b2_11" to "11. Konjunktiv II der Vergangenheit",
            "b2_12" to "12. Konjunktiv II mit Modalverben",
            "b2_13" to "13. Pronomen: einander",
            "b2_14" to "14. Weiterfuhrende Nebensatze",
            "b2_15" to "15. Prapositionen mit Genitiv",
            "b2_16" to "16. je und desto/umso + Komparativ",
            "b2_17" to "17. Nomen-Verb-Verbindungen",
            "b2_18" to "18. Folgen ausdrucken",
            "b2_19" to "19. Ausdrucke mit Prapositionen",
            "b2_20" to "20. Irreale Konditionalsatze",
            "b2_21" to "21. Relativsatze im Genitiv",
            "b2_22" to "22. Konjunktiv I in der indirekten Rede",
            "b2_23" to "23. Konjunktiv II in irrealen Vergleichssatzen"
        )
        return titles[subjectId] ?: "Quiz"
    }
}
