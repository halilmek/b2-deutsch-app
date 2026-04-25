package com.b2deutsch.app.ui.quiz

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.b2deutsch.app.data.model.Question
import com.b2deutsch.app.data.model.Quiz
import com.b2deutsch.app.data.model.QuizResult
import com.b2deutsch.app.data.model.ReadingPassage
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

    private val _currentReading = MutableLiveData<ReadingPassage?>()
    val currentReading: LiveData<ReadingPassage?> = _currentReading

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

    private val _quizPhase = MutableLiveData<QuizPhase>(QuizPhase.READING)
    val quizPhase: LiveData<QuizPhase> = _quizPhase

    private var timeRemaining = 0
    private var quizStartTime = 0L
    private var currentSubjectId: String = ""
    private var usedReadingIds = mutableSetOf<String>()

    enum class QuizPhase {
        READING,    // Showing the text passage
        QUESTIONS,  // Answering questions about the text
        RESULT      // Quiz completed
    }

    // Load quizzes for a level (used by QuizzesFragment)
    fun loadQuizzes(level: String = Constants.DEFAULT_LEVEL) {
        viewModelScope.launch {
            _isLoading.value = true
            contentRepository.getQuizzesByLevel(level)
                .onSuccess { quizList ->
                    _quizzes.value = quizList
                }
                .onFailure {
                    _quizzes.value = emptyList()
                }
            _isLoading.value = false
        }
    }

    // Map grammar topic ID to theme ID
    private fun subjectToTheme(subjectId: String): String {
        return when (subjectId) {
            "b2_01", "b2_02", "b2_03" -> "beruf"
            "b2_04", "b2_05", "b2_06" -> "gesundheit"
            "b2_07", "b2_08", "b2_09" -> "umwelt"
            "b2_10", "b2_11", "b2_12" -> "gesellschaft"
            "b2_13", "b2_14" -> "reisen"
            "b2_15", "b2_16" -> "medien"
            "b2_17", "b2_18" -> "bildung"
            "b2_19", "b2_20" -> "wirtschaft"
            "b2_21", "b2_22", "b2_23" -> "geschichte"
            else -> "beruf" // Default
        }
    }

    // Load a reading passage for this subject, then present questions
    fun startQuiz(subjectId: String) {
        currentSubjectId = subjectId
        viewModelScope.launch {
            _isLoading.value = true
            _selectedAnswers.value = mutableMapOf()
            _quizResult.value = null
            _quizPhase.value = QuizPhase.READING
            
            val themeId = subjectToTheme(subjectId)
            
            // Get readings for this theme (filtered by subjectId in the reading document)
            contentRepository.getReadingsByTheme(themeId)
                .onSuccess { readings ->
                    // Filter readings that are tagged with this subjectId
                    val subjectReadings = readings.filter { reading ->
                        reading.subjectIds?.contains(subjectId) == true || 
                        reading.id.contains(themeId)
                    }
                    
                    if (subjectReadings.isNotEmpty()) {
                        // Pick a random unread reading
                        val availableReadings = subjectReadings.filter { it.id !in usedReadingIds }
                        val readingToUse = if (availableReadings.isNotEmpty()) {
                            availableReadings.random()
                        } else {
                            usedReadingIds.clear()
                            subjectReadings.random()
                        }
                        
                        usedReadingIds.add(readingToUse.id)
                        _currentReading.value = readingToUse
                        
                        // Load questions for this specific reading
                        loadQuestionsForReading(readingToUse.id, subjectId)
                    } else if (readings.isNotEmpty()) {
                        // Fallback: use any reading from the theme
                        val availableReadings = readings.filter { it.id !in usedReadingIds }
                        val readingToUse = if (availableReadings.isNotEmpty()) {
                            availableReadings.random()
                        } else {
                            usedReadingIds.clear()
                            readings.random()
                        }
                        
                        usedReadingIds.add(readingToUse.id)
                        _currentReading.value = readingToUse
                        loadQuestionsForReading(readingToUse.id, subjectId)
                    } else {
                        createFallbackQuiz(subjectId)
                    }
                }
                .onFailure {
                    createFallbackQuiz(subjectId)
                }
            
            _isLoading.value = false
        }
    }

    private suspend fun loadQuestionsForReading(readingId: String, subjectId: String) {
        contentRepository.getQuestionsByReading(readingId)
            .onSuccess { questions ->
                if (questions.isNotEmpty()) {
                    createQuizFromQuestions(questions, readingId, subjectId)
                } else {
                    loadFromQuizBank(subjectId, readingId)
                }
            }
            .onFailure {
                loadFromQuizBank(subjectId, readingId)
            }
    }

    private suspend fun loadFromQuizBank(subjectId: String, readingId: String) {
        // Load questions from quizBank that are tagged with this subjectId
        contentRepository.getQuestionsBySubject(subjectId)
            .onSuccess { questions ->
                if (questions.isNotEmpty()) {
                    val shuffled = questions.shuffled().take(5)
                    createQuizFromQuestions(shuffled, readingId, subjectId)
                } else {
                    createFallbackQuiz(subjectId)
                }
            }
            .onFailure {
                createFallbackQuiz(subjectId)
            }
    }

    private fun createQuizFromQuestions(questions: List<Question>, readingId: String, subjectId: String) {
        val quiz = Quiz(
            id = "${subjectId}_${readingId}_quiz",
            level = "B2",
            category = Constants.Categories.READING,
            title = getSubjectTitle(subjectId),
            taskType = "reading",
            timeLimit = 15,
            passingScore = 60,
            questions = questions.take(5) // Max 5 questions per quiz
        )
        
        _currentQuiz.value = quiz
        _currentQuestionIndex.value = 0
        timeRemaining = quiz.timeLimit * 60
        quizStartTime = System.currentTimeMillis()
        
        _quizPhase.value = QuizPhase.READING
        _currentQuestion.value = null
    }

    private fun createFallbackQuiz(subjectId: String) {
        val sampleQuestions = listOf(
            Question(
                id = "sample_1",
                type = Constants.QuizTypes.MULTIPLE_CHOICE,
                questionText = "Lesen Sie den Text und beantworten Sie die Frage. Welche Aussage ist laut Text richtig?",
                options = listOf("A) Antwort A", "B) Antwort B", "C) Antwort C", "D) Antwort D"),
                correctAnswer = "A) Antwort A",
                explanation = "Überprüfen Sie den Text sorgfältig."
            ),
            Question(
                id = "sample_2",
                type = Constants.QuizTypes.TRUE_FALSE,
                questionText = "Der Text beschreibt die Situation korrekt.",
                options = listOf("Richtig", "Falsch"),
                correctAnswer = "Richtig",
                explanation = "Der Text erwähnt dieses Thema."
            ),
            Question(
                id = "sample_3",
                type = Constants.QuizTypes.MULTIPLE_CHOICE,
                questionText = "Was ist die Hauptaussage des Textes?",
                options = listOf(
                    "Die Situation hat sich verbessert.",
                    "Die Situation ist unverändert.",
                    "Die Situation hat sich verschlechtert.",
                    "Der Text gibt keine Information darüber."
                ),
                correctAnswer = "Die Situation hat sich verbessert.",
                explanation = "Der Text zeigt eine positive Entwicklung."
            ),
            Question(
                id = "sample_4",
                type = Constants.QuizTypes.FILL_BLANK,
                questionText = "Der Text handelt von ___ .",
                options = listOf("Beruf", "Gesundheit", "Umwelt", "Politik"),
                correctAnswer = "Beruf",
                explanation = "Das Thema wird im ersten Absatz eingeführt."
            ),
            Question(
                id = "sample_5",
                type = Constants.QuizTypes.MULTIPLE_CHOICE,
                questionText = "Welche Lösung wird im Text vorgeschlagen?",
                options = listOf(
                    "Lösung A",
                    "Lösung B",
                    "Lösung C",
                    "Keine Lösung wird genannt."
                ),
                correctAnswer = "Keine Lösung wird genannt.",
                explanation = "Der Text beschreibt das Problem nur."
            )
        )
        
        val quiz = Quiz(
            id = "${subjectId}_fallback",
            level = "B2",
            category = Constants.Categories.READING,
            title = getSubjectTitle(subjectId),
            taskType = "reading",
            timeLimit = 10,
            passingScore = 60,
            questions = sampleQuestions
        )
        
        _currentQuiz.value = quiz
        _currentQuestionIndex.value = 0
        _quizPhase.value = QuizPhase.READING
        _currentReading.value = ReadingPassage(
            id = "sample_reading",
            title = "Leseverstehen",
            content = "Dies ist ein Übungstext für das Leseverstehen. Lesen Sie den Text sorgfältig durch und beantworten Sie die Fragen. Der Text behandelt ein alltägliches Thema, das für das B2-Niveau relevant ist. Achten Sie auf die Hauptaussage und die Details im Text."
        )
    }

    fun proceedToQuestions() {
        _quizPhase.value = QuizPhase.QUESTIONS
        updateCurrentQuestion()
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
        
        _quizPhase.value = QuizPhase.RESULT
    }

    fun startNextQuiz() {
        startQuiz(currentSubjectId)
    }

    private fun getSubjectTitle(subjectId: String): String {
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
        return titles[subjectId] ?: "Quiz"
    }
}
