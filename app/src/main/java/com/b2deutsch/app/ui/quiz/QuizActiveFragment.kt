package com.b2deutsch.app.ui.quiz

import android.os.Bundle
import android.text.InputType
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.EditText
import android.widget.RadioButton
import android.widget.TextView
import android.widget.Toast
import androidx.core.view.children
import androidx.fragment.app.Fragment
import androidx.fragment.app.activityViewModels
import androidx.navigation.fragment.findNavController
import com.b2deutsch.app.R
import com.b2deutsch.app.databinding.FragmentQuizActiveBinding
import dagger.hilt.android.AndroidEntryPoint

@AndroidEntryPoint
class QuizActiveFragment : Fragment() {

    private var _binding: FragmentQuizActiveBinding? = null
    private val binding get() = _binding!!

    private val viewModel: QuizViewModel by activityViewModels()

    private var isSubmitting = false
    private var fillBlankAnswer1: EditText? = null
    private var fillBlankAnswer2: EditText? = null

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentQuizActiveBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        val quizId = arguments?.getString("quizId") ?: run {
            Log.e("QuizActive", "No quizId provided")
            return
        }
        val subjectId = arguments?.getString("subjectId") ?: quizId.substringBeforeLast("_quiz")

        // Only start a new quiz if one isn't already in progress
        // This prevents restart when rotating the device
        if (viewModel.currentQuiz.value == null) {
            Log.d("QuizActive", "Starting fresh quiz: subjectId=$subjectId")
            viewModel.startQuiz(subjectId)
        } else {
            Log.d("QuizActive", "Resuming existing quiz (rotation safe)")
        }

        observeViewModel()
        setupClickListeners()
    }

    private fun setupClickListeners() {
        binding.btnNext.setOnClickListener {
            if (isSubmitting) return@setOnClickListener

            val currentQuestion = viewModel.currentQuestion.value
            if (currentQuestion?.type == "fill_blank") {
                // For fill_blank: collect text from input fields
                val answer1 = fillBlankAnswer1?.text?.toString()?.trim() ?: ""
                val answer2 = fillBlankAnswer2?.text?.toString()?.trim() ?: ""
                val blanks = currentQuestion.questionText.windowed(5).count { it == "_____" }

                val combinedAnswer = if (blanks == 2) "$answer1 $answer2" else answer1
                if (combinedAnswer.isNotEmpty()) {
                    viewModel.selectAnswer(combinedAnswer)
                    viewModel.nextQuestion()
                } else {
                    Toast.makeText(context, "Bitte füllen Sie die Lücke(n) aus", Toast.LENGTH_SHORT).show()
                }
            } else {
                // MCQ / T/F: use RadioGroup selection
                val selectedId = binding.rgOptions.checkedRadioButtonId
                if (selectedId != -1) {
                    val selectedAnswer = binding.rgOptions.findViewById<RadioButton>(selectedId)?.text?.toString()
                    if (!selectedAnswer.isNullOrEmpty()) {
                        viewModel.selectAnswer(selectedAnswer)
                        viewModel.nextQuestion()
                    }
                } else {
                    Toast.makeText(context, "Bitte wählen Sie eine Antwort", Toast.LENGTH_SHORT).show()
                }
            }
        }

        binding.btnPrevious.setOnClickListener {
            if (isSubmitting) return@setOnClickListener
            viewModel.previousQuestion()
        }

        binding.btnSubmit.setOnClickListener {
            if (isSubmitting) return@setOnClickListener

            isSubmitting = true
            val currentQuestion = viewModel.currentQuestion.value

            if (currentQuestion?.type == "fill_blank") {
                val answer1 = fillBlankAnswer1?.text?.toString()?.trim() ?: ""
                val answer2 = fillBlankAnswer2?.text?.toString()?.trim() ?: ""
                val blanks = currentQuestion.questionText.windowed(5).count { it == "_____" }
                val combinedAnswer = if (blanks == 2) "$answer1 $answer2" else answer1
                if (combinedAnswer.isNotEmpty()) {
                    viewModel.selectAnswer(combinedAnswer)
                }
            } else {
                val selectedId = binding.rgOptions.checkedRadioButtonId
                if (selectedId != -1) {
                    val selectedAnswer = binding.rgOptions.findViewById<RadioButton>(selectedId)?.text?.toString()
                    if (!selectedAnswer.isNullOrEmpty()) {
                        viewModel.selectAnswer(selectedAnswer)
                    }
                }
            }
            viewModel.submitQuiz()
        }
    }

    private fun observeViewModel() {
        viewModel.currentQuiz.observe(viewLifecycleOwner) { quiz ->
            quiz?.let {
                binding.tvQuizTitle.text = it.title
                binding.tvTimeLimit.text = "Time: ${it.timeLimit} min"
                Log.d("QuizActive", "Quiz loaded: ${it.title}, ${it.questions.size} questions")
            }
        }

        viewModel.currentQuestion.observe(viewLifecycleOwner) { question ->
            if (question == null) {
                Log.d("QuizActive", "Question is null, waiting...")
                return@observe
            }

            try {
                binding.tvQuestionText.text = question.questionText ?: "No question text"
                binding.tvQuestionNumber.text = "Question ${(viewModel.currentQuestionIndex.value ?: 0) + 1}"

                binding.rgOptions.removeAllViews()
                fillBlankAnswer1 = null
                fillBlankAnswer2 = null

                if (question.type == "fill_blank") {
                    // Render fill-in-the-blank UI
                    renderFillBlankUI(question)
                } else {
                    // Render MCQ / T/F UI
                    val options: List<String> = question.options?.takeIf { it != null } ?: emptyList()

                    if (options.isNotEmpty()) {
                        options.forEach { option ->
                            val radioButton = RadioButton(requireContext()).apply {
                                id = View.generateViewId()
                                text = option
                                textSize = 16f
                                setPadding(32, 24, 32, 24)
                            }
                            binding.rgOptions.addView(radioButton)
                        }
                    } else {
                        binding.rgOptions.addView(TextView(requireContext()).apply {
                            text = "Keine Optionen verfügbar"
                            textSize = 14f
                            setPadding(32, 24, 32, 24)
                        })
                    }

                    // Restore previously selected answer
                    restoreRadioSelection()
                }

                Log.d("QuizActive", "Question displayed: ${question.questionText?.take(50)}")

            } catch (e: Exception) {
                Log.e("QuizActive", "Error displaying question: ${e.message}")
                Toast.makeText(context, "Error: ${e.message}", Toast.LENGTH_SHORT).show()
            }
        }

        viewModel.currentQuestionIndex.observe(viewLifecycleOwner) { index ->
            try {
                val quiz = viewModel.currentQuiz.value
                val total = quiz?.questions?.size ?: 1
                binding.tvProgress.text = "${index + 1} / $total"
                binding.progressBar.max = total
                binding.progressBar.progress = index + 1

                binding.btnPrevious.visibility = if (index > 0) View.VISIBLE else View.INVISIBLE

                if (index == total - 1) {
                    binding.btnNext.visibility = View.GONE
                    binding.btnSubmit.visibility = View.VISIBLE
                } else {
                    binding.btnNext.visibility = View.VISIBLE
                    binding.btnSubmit.visibility = View.GONE
                }
            } catch (e: Exception) {
                Log.e("QuizActive", "Error updating progress: ${e.message}")
            }
        }

        viewModel.quizResult.observe(viewLifecycleOwner) { result ->
            result?.let {
                isSubmitting = false
                Log.d("QuizActive", "Quiz completed: score=${it.score}%")
                val bundle = Bundle().apply {
                    putString("quizId", arguments?.getString("quizId"))
                    putString("subjectId", arguments?.getString("subjectId"))
                    putInt("score", it.score)
                    putBoolean("passed", it.passed)
                    putInt("correct", it.correctAnswers)
                    putInt("total", it.totalQuestions)
                }
                findNavController().navigate(R.id.action_quizActive_to_result, bundle)
            }
        }

        viewModel.errorMessage.observe(viewLifecycleOwner) { error ->
            error?.let {
                Log.e("QuizActive", "Error: $it")
                Toast.makeText(context, "Error: $it", Toast.LENGTH_LONG).show()
            }
        }

        viewModel.isLoading.observe(viewLifecycleOwner) { isLoading ->
            binding.progressBar.visibility = if (isLoading) View.VISIBLE else View.GONE
        }
    }

    private fun renderFillBlankUI(question: com.b2deutsch.app.data.model.Question) {
        val blanks = question.questionText.windowed(5).count { it == "_____" }

        // Label
        val label = TextView(requireContext()).apply {
            text = "Bitte füllen Sie die Lücke(n) aus:"
            textSize = 14f
            setPadding(0, 16, 0, 16)
        }
        binding.rgOptions.addView(label)

        if (blanks >= 1) {
            fillBlankAnswer1 = EditText(requireContext()).apply {
                id = View.generateViewId()
                hint = "Antwort"
                textSize = 18f
                setPadding(32, 24, 32, 24)
                setBackgroundResource(android.R.drawable.edit_text)
                inputType = InputType.TYPE_TEXT_FLAG_NO_SUGGESTIONS
            }
            binding.rgOptions.addView(fillBlankAnswer1)
        }

        if (blanks == 2) {
            val label2 = TextView(requireContext()).apply {
                text = "Zweite Antwort:"
                textSize = 14f
                setPadding(0, 16, 0, 8)
            }
            binding.rgOptions.addView(label2)

            fillBlankAnswer2 = EditText(requireContext()).apply {
                id = View.generateViewId()
                hint = "Antwort 2"
                textSize = 18f
                setPadding(32, 24, 32, 24)
                setBackgroundResource(android.R.drawable.edit_text)
                inputType = InputType.TYPE_TEXT_FLAG_NO_SUGGESTIONS
            }
            binding.rgOptions.addView(fillBlankAnswer2)
        }

        // Restore saved answers
        val questionIndex = viewModel.currentQuestionIndex.value ?: 0
        val savedAnswer = viewModel.selectedAnswers.value?.get(questionIndex)
        if (!savedAnswer.isNullOrEmpty()) {
            val parts = savedAnswer.split(" ", limit = 2)
            fillBlankAnswer1?.setText(parts.getOrNull(0) ?: "")
            if (parts.size > 1) {
                fillBlankAnswer2?.setText(parts.getOrNull(1) ?: "")
            }
        }
    }

    private fun restoreRadioSelection() {
        val questionIndex = viewModel.currentQuestionIndex.value ?: 0
        val savedAnswer = viewModel.selectedAnswers.value?.get(questionIndex)
        if (!savedAnswer.isNullOrEmpty()) {
            for (i in 0 until binding.rgOptions.childCount) {
                val rb = binding.rgOptions.getChildAt(i) as? RadioButton
                if (rb?.text == savedAnswer) {
                    rb.isChecked = true
                    break
                }
            }
        }
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}