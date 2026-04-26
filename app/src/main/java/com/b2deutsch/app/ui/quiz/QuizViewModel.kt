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

    private val _errorMessage = MutableLiveData<String?>()
    val errorMessage: LiveData<String?> = _errorMessage

    private var quizStartTime = 0L
    private var currentSubjectId = ""
    private var currentQuizQuestionIds = listOf<String>()

    init {
        viewModelScope.launch {
            withContext(Dispatchers.IO) {
                LocalQuestionBank.initializeFromAssets(application)
            }
        }
    }

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
                _isComplete.value = true
                _quizMessage.value = result.message
                _isLoading.value = false
                return@launch
            }

            if (result.isLooping) {
                _quizMessage.value = result.message
            }

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

        viewModelScope.launch {
            withContext(Dispatchers.IO) {
                LocalQuestionBank.markQuizCompleted(application, currentSubjectId, currentQuizQuestionIds)
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

    fun startNextQuiz() {
        startQuiz(currentSubjectId)
    }

    fun resetTopicProgress() {
        viewModelScope.launch(Dispatchers.IO) {
            LocalQuestionBank.resetTopic(application, currentSubjectId)
        }
        _isComplete.value = false
        _quizMessage.value = null
    }

    fun retryQuiz() {
        val quiz = _currentQuiz.value ?: return
        _selectedAnswers.value = mutableMapOf()
        _quizResult.value = null
        _currentQuestionIndex.value = 0
        quizStartTime = System.currentTimeMillis()
        updateCurrentQuestion()
    }

    fun getProgressString(): String {
        return LocalQuestionBank.getProgressString(application, currentSubjectId)
    }

    fun getRemainingCount(): Int {
        return LocalQuestionBank.getRemainingCount(application, currentSubjectId)
    }

    private fun getSubjectTitle(subjectId: String): String {
        val titles = mapOf(
            "b2_01" to "1. Konnektoren",
            "b2_03" to "2. Verben und Ergänzungen",
            "b2_04" to "3. Zeitformen in der Vergangenheit",
            "b2_05" to "4. Zeitformen der Zukunft",
            "b2_06" to "5. Futur mit werden",
            "b2_07" to "6. Angaben im Satz",
            "b2_08" to "7. Verneinung mit nicht",
            "b2_09" to "8. Negationswörter",
            "b2_10" to "9. Passiv Präteritum",
            "b2_11" to "10. Konjunktiv II der Vergangenheit",
            "b2_12" to "11. Konjunktiv II mit Modalverben",
            "b2_13" to "12. Pronomen: einander",
            "b2_14" to "13. Weiterführende Nebensätze",
            "b2_15" to "14. Präpositionen mit Genitiv",
            "b2_16" to "15. je und desto/umso + Komparativ",
            "b2_17" to "16. Nomen-Verb-Verbindungen",
            "b2_18" to "17. Folgen ausdrücken",
            "b2_19" to "18. Ausdrücke mit Präpositionen",
            "b2_20" to "19. Irreale Konditionalsätze",
            "b2_21" to "20. Relativsätze im Genitiv",
            "b2_22" to "21. Konjunktiv I in der indirekten Rede",
            "b2_23" to "22. Konjunktiv II in irrealen Vergleichssätze"
        )
        return titles[subjectId] ?: subjectId
    }

    /**
     * Legacy: load quiz list for a level (used by QuizzesFragment).
     */
    fun loadQuizzes(level: String) {
        viewModelScope.launch {
            _isLoading.value = true
            val topicIds = LocalQuestionBank.getAllTopicIds(level)
            val quizList = topicIds.map { subjectId ->
                val progress = LocalQuestionBank.getProgressString(application, subjectId)
                Quiz(
                    id = subjectId,
                    level = level,
                    category = Constants.Categories.GRAMMAR,
                    title = getSubjectTitle(subjectId),
                    description = "$progress gelost",
                    taskType = "grammar",
                    timeLimit = 15,
                    passingScore = 60,
                    questions = emptyList()
                )
            }
            _quizzes.value = quizList
            _isLoading.value = false
        }
    }

    private val _quizzes = MutableLiveData<List<Quiz>>(emptyList())
    val quizzes: LiveData<List<Quiz>> = _quizzes
}
