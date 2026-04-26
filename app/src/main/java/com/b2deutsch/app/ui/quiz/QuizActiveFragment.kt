package com.b2deutsch.app.ui.quiz

import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.RadioButton
import android.widget.TextView
import android.widget.Toast
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
        
        Log.d("QuizActive", "Starting quiz: subjectId=$subjectId")
        viewModel.startQuiz(subjectId)

        observeViewModel()
        setupClickListeners()
    }

    private fun setupClickListeners() {
        binding.btnNext.setOnClickListener {
            if (isSubmitting) return@setOnClickListener
            
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

        binding.btnPrevious.setOnClickListener {
            if (isSubmitting) return@setOnClickListener
            viewModel.previousQuestion()
        }

        binding.btnSubmit.setOnClickListener {
            if (isSubmitting) return@setOnClickListener
            
            isSubmitting = true
            val selectedId = binding.rgOptions.checkedRadioButtonId
            if (selectedId != -1) {
                val selectedAnswer = binding.rgOptions.findViewById<RadioButton>(selectedId)?.text?.toString()
                if (!selectedAnswer.isNullOrEmpty()) {
                    viewModel.selectAnswer(selectedAnswer)
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
                
                // Get options safely - handle null from Firestore
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
                    // No options - show a placeholder
                    val infoText = TextView(requireContext()).apply {
                        text = "Keine Optionen verfügbar"
                        textSize = 14f
                        setPadding(32, 24, 32, 24)
                    }
                    binding.rgOptions.addView(infoText)
                }

                // Restore previously selected answer
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

                // Show/hide navigation buttons
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

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}
