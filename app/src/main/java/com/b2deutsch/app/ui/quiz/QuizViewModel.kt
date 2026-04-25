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

    // Keep track of available questions for the current subject
    private var availableQuestions = listOf<Question>()
    private var currentQuizIndex = 0

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
            _selectedAnswers.value = mutableMapOf()
            _quizResult.value = null
            
            // Extract theme ID from quizId (format: b2_01_quiz_1 -> b2_01)
            val themeId = quizId.replace("_quiz_${currentQuizIndex + 1}", "")
            
            // Load questions from Firestore for this theme
            contentRepository.getQuestionsByTheme(themeId)
                .onSuccess { questions ->
                    if (questions.isNotEmpty()) {
                        availableQuestions = questions.shuffled()
                        createQuizFromQuestions(themeId)
                    } else {
                        // Fall back to sample if no questions in DB
                        createSampleQuiz(themeId)
                    }
                }
                .onFailure {
                    createSampleQuiz(themeId)
                }
            
            _isLoading.value = false
        }
    }

    private fun createQuizFromQuestions(themeId: String) {
        // Take 5 questions for this quiz
        val quizQuestions = if (availableQuestions.size >= 5) {
            availableQuestions.take(5)
        } else {
            availableQuestions
        }
        
        // Remove used questions so next quiz is different
        if (availableQuestions.size >= 5) {
            availableQuestions = availableQuestions.drop(5)
        }
        
        val quiz = Quiz(
            id = "${themeId}_quiz_${currentQuizIndex + 1}",
            level = "B2",
            category = Constants.Categories.GRAMMAR,
            title = getSubjectTitle(themeId),
            taskType = "grammar",
            timeLimit = 10,
            passingScore = 70,
            questions = quizQuestions
        )
        
        _currentQuiz.value = quiz
        _currentQuestionIndex.value = 0
        currentQuizIndex++
        timeRemaining = quiz.timeLimit * 60
        quizStartTime = System.currentTimeMillis()
        updateCurrentQuestion()
    }

    private fun createSampleQuiz(themeId: String) {
        val sampleQuizzes = getSampleQuizzes("B2")
        val quiz = sampleQuizzes.firstOrNull() ?: sampleQuizzes.first()
        _currentQuiz.value = quiz
        _currentQuestionIndex.value = 0
        updateCurrentQuestion()
    }

    private fun getSubjectTitle(themeId: String): String {
        val titles = mapOf(
            "b2_01" to "1. Konnektoren: als, bevor, bis, seitdem, während, wenn",
            "b2_02" to "2. Konnektoren: sobald, solange",
            "b2_03" to "3. Verben und Ergänzungen",
            "b2_04" to "4. Zeitformen in der Vergangenheit",
            "b2_05" to "5. Zeitformen der Zukunft",
            "b2_06" to "6. Futur mit werden",
            "b2_07" to "7. Angaben im Satz",
            "b2_08" to "8. Verneinung mit nicht",
            "b2_09" to "9. Negationswörter",
            "b2_10" to "10. Passiv Präteritum",
            "b2_11" to "11. Konjunktiv II der Vergangenheit",
            "b2_12" to "12. Konjunktiv II mit Modalverben",
            "b2_13" to "13. Pronomen: einander",
            "b2_14" to "14. Weiterführende Nebensätze",
            "b2_15" to "15. Präpositionen mit Genitiv",
            "b2_16" to "16. je und desto/umso + Komparativ",
            "b2_17" to "17. Nomen-Verb-Verbindungen",
            "b2_18" to "18. Folgen ausdrücken",
            "b2_19" to "19. Ausdrücke mit Präpositionen",
            "b2_20" to "20. irreale Konditionalsätze",
            "b2_21" to "21. Relativsätze im Genitiv",
            "b2_22" to "22. Konjunktiv I in der indirekten Rede",
            "b2_23" to "23. Konjunktiv II in irrealen Vergleichssätzen"
        )
        return titles[themeId] ?: "Quiz"
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
                id = "${level.lowercase()}_quiz_sample",
                level = level,
                category = Constants.Categories.GRAMMAR,
                title = "Sample Quiz",
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
