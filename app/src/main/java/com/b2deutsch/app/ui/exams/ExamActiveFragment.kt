package com.b2deutsch.app.ui.exams

import android.os.Bundle
import android.os.CountDownTimer
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.LinearLayout
import android.widget.RadioButton
import android.widget.RadioGroup
import android.widget.TextView
import androidx.core.content.ContextCompat
import androidx.fragment.app.Fragment
import androidx.navigation.fragment.findNavController
import com.b2deutsch.app.R
import com.b2deutsch.app.databinding.FragmentExamActiveBinding
import dagger.hilt.android.AndroidEntryPoint

@AndroidEntryPoint
class ExamActiveFragment : Fragment() {

    private var _binding: FragmentExamActiveBinding? = null
    private val binding get() = _binding!!

    private lateinit var examId: String
    private lateinit var level: String
    private lateinit var examTitle: String

    private var currentQuestionIndex = 0
    private var totalQuestions = 10
    private var selectedAnswers = mutableMapOf<Int, String>()
    private var questions = listOf<ExamQuestion>()

    private var timer: CountDownTimer? = null
    private var timeRemainingSeconds = 0

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentExamActiveBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        
        examId = arguments?.getString("examId") ?: ""
        level = arguments?.getString("level") ?: "C1"
        examTitle = arguments?.getString("examTitle") ?: "Exam"
        
        setupUI()
        loadQuestions()
        startTimer()
    }

    private fun setupUI() {
        binding.tvExamTitle.text = examTitle
        
        binding.btnBack.setOnClickListener {
            timer?.cancel()
            findNavController().navigateUp()
        }
        
        binding.btnPrevious.setOnClickListener {
            saveCurrentAnswer()
            if (currentQuestionIndex > 0) {
                currentQuestionIndex--
                displayQuestion()
            }
        }
        
        binding.btnNext.setOnClickListener {
            saveCurrentAnswer()
            if (currentQuestionIndex < questions.size - 1) {
                currentQuestionIndex++
                displayQuestion()
            }
        }
        
        binding.btnSubmit.setOnClickListener {
            submitExam()
        }
    }

    private fun loadQuestions() {
        // Load sample questions based on exam type
        questions = getSampleQuestions(examId)
        totalQuestions = questions.size
        displayQuestion()
    }

    private fun displayQuestion() {
        val question = questions[currentQuestionIndex]
        
        // Update progress
        binding.tvProgress.text = "Question ${currentQuestionIndex + 1} of $totalQuestions"
        binding.progressBar.max = 100
        binding.progressBar.progress = ((currentQuestionIndex + 1) * 100) / totalQuestions
        
        // Display question text
        binding.tvQuestionText.text = question.questionText
        
        // Display answers
        binding.answersContainer.removeAllViews()
        
        val radioGroup = RadioGroup(requireContext())
        radioGroup.orientation = RadioGroup.VERTICAL
        
        for ((index, option) in question.options.withIndex()) {
            val radioButton = RadioButton(requireContext()).apply {
                id = View.generateViewId()
                text = option
                textSize = 16f
                setTextColor(ContextCompat.getColor(requireContext(), R.color.black))
                val padding = resources.getDimensionPixelSize(R.dimen.spacing_medium)
                setPadding(padding, padding, padding, padding)
                
                // Highlight previously selected answer
                if (selectedAnswers[currentQuestionIndex] == option) {
                    isChecked = true
                }
            }
            radioGroup.addView(radioButton)
        }
        
        radioGroup.setOnCheckedChangeListener { _, checkedId ->
            val selectedOption = (radioGroup.findViewById(checkedId) as? RadioButton)?.text?.toString()
            selectedAnswers[currentQuestionIndex] = selectedOption ?: ""
        }
        
        binding.answersContainer.addView(radioGroup)
        
        // Update navigation buttons
        binding.btnPrevious.isEnabled = currentQuestionIndex > 0
        
        if (currentQuestionIndex == questions.size - 1) {
            binding.btnNext.visibility = View.GONE
            binding.btnSubmit.visibility = View.VISIBLE
        } else {
            binding.btnNext.visibility = View.VISIBLE
            binding.btnSubmit.visibility = View.GONE
        }
    }

    private fun saveCurrentAnswer() {
        val radioGroup = binding.answersContainer.getChildAt(0) as? RadioGroup ?: return
        val selectedId = radioGroup.checkedRadioButtonId
        if (selectedId == View.NO_ID) return
        val selectedText = radioGroup.findViewById<RadioButton>(selectedId)?.text?.toString()
        selectedText?.let { selectedAnswers[currentQuestionIndex] = it }
    }

    private fun startTimer() {
        val durationMinutes = when (examId) {
            "leseverstehen" -> 60
            "horverstehen" -> 40
            "schreiben" -> 75
            "sprechen" -> 15
            else -> 60
        }
        timeRemainingSeconds = durationMinutes * 60
        
        timer = object : CountDownTimer(timeRemainingSeconds * 1000L, 1000L) {
            override fun onTick(millisUntilFinished: Long) {
                val minutes = (millisUntilFinished / 1000) / 60
                val seconds = (millisUntilFinished / 1000) % 60
                binding.tvTimer.text = String.format("%02d:%02d", minutes, seconds)
                
                if (millisUntilFinished < 5 * 60 * 1000) {
                    binding.tvTimer.setTextColor(
                        ContextCompat.getColor(requireContext(), R.color.red_500)
                    )
                }
            }

            override fun onFinish() {
                // Auto-submit when time is up
                submitExam()
            }
        }.start()
    }

    private fun submitExam() {
        timer?.cancel()
        saveCurrentAnswer()
        
        // Navigate to results
        val bundle = Bundle().apply {
            putString("examId", examId)
            putString("level", level)
        }
        findNavController().navigate(R.id.action_examActive_to_examResult, bundle)
    }

    private fun getSampleQuestions(examId: String): List<ExamQuestion> {
        return when (examId) {
            "leseverstehen" -> listOf(
                ExamQuestion(
                    "Lesen Sie den folgenden Text und beantworten Sie die Fragen.",
                    "Der Text handelt von einem jungen Mann, der in Berlin studiert.",
                    listOf("Das ist korrekt", "Das ist falsch", "Geht nicht aus dem Text hervor"),
                    0
                ),
                ExamQuestion(
                    "Warum hat der Autor den Artikel geschrieben?",
                    "Um über seine persönlichen Erfahrungen zu berichten.",
                    listOf("Um zu informieren", "Um zu unterhalten", "Um zu werben"),
                    0
                ),
                ExamQuestion(
                    "Was ist die Hauptthese des Textes?",
                    "Die Digitalisierung verändert die Arbeitswelt grundlegend.",
                    listOf("Die Wirtschaft wächst", "Die Klimakrise ist das größte Problem", "Technologie hat nur Vorteile"),
                    0
                ),
                ExamQuestion(
                    "Welche Informationen finden Sie im Text?",
                    "Statistiken und Forschungsergebnisse.",
                    listOf("Nur Meinungen", "Keine konkreten Daten", "Nur persönliche Geschichten"),
                    0
                ),
                ExamQuestion(
                    "Wie ist der Text strukturiert?",
                    "Einleitung, Hauptteil und Schluss.",
                    listOf("Nur ein Absatz", "Mehrere unabhängige Kapitel", "Als Dialog formatiert"),
                    0
                )
            )
            else -> listOf(
                ExamQuestion(
                    "Sample question for $examId?",
                    "This is a sample question text.",
                    listOf("Option A", "Option B", "Option C", "Option D"),
                    0
                ),
                ExamQuestion(
                    "Second sample question?",
                    "This is another sample question.",
                    listOf("Option A", "Option B", "Option C", "Option D"),
                    0
                )
            )
        }
    }

    override fun onDestroyView() {
        super.onDestroyView()
        timer?.cancel()
        _binding = null
    }
}

data class ExamQuestion(
    val questionText: String,
    val correctAnswer: String,
    val options: List<String>,
    val correctOptionIndex: Int
)
