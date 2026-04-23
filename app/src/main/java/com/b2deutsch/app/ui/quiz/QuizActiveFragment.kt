package com.b2deutsch.app.ui.quiz

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.RadioButton
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

        val quizId = arguments?.getString("quizId") ?: return
        viewModel.startQuiz(quizId)

        observeViewModel()

        binding.btnNext.setOnClickListener {
            val selectedId = binding.rgOptions.checkedRadioButtonId
            if (selectedId != -1) {
                val selectedAnswer = binding.rgOptions.findViewById<RadioButton>(selectedId)?.text.toString()
                val questionIndex = viewModel.currentQuestionIndex.value ?: 0
                viewModel.selectAnswer(questionIndex, selectedAnswer)
                viewModel.nextQuestion()
            }
        }

        binding.btnPrevious.setOnClickListener {
            viewModel.previousQuestion()
        }

        binding.btnSubmit.setOnClickListener {
            // Save last answer first
            val selectedId = binding.rgOptions.checkedRadioButtonId
            if (selectedId != -1) {
                val selectedAnswer = binding.rgOptions.findViewById<RadioButton>(selectedId)?.text.toString()
                val questionIndex = viewModel.currentQuestionIndex.value ?: 0
                viewModel.selectAnswer(questionIndex, selectedAnswer)
            }
            viewModel.submitQuiz()
        }
    }

    private fun observeViewModel() {
        viewModel.currentQuiz.observe(viewLifecycleOwner) { quiz ->
            quiz?.let {
                binding.tvQuizTitle.text = it.title
                binding.tvTimeLimit.text = "Time: ${it.timeLimit} min"
            }
        }

        viewModel.currentQuestion.observe(viewLifecycleOwner) { question ->
            question?.let {
                binding.tvQuestionText.text = it.questionText
                binding.tvQuestionNumber.text = "Question ${(viewModel.currentQuestionIndex.value ?: 0) + 1}"

                binding.rgOptions.removeAllViews()
                it.options.forEachIndexed { index, option ->
                    val radioButton = RadioButton(context).apply {
                        id = View.generateViewId()
                        text = option
                        textSize = 16f
                        padding = 16
                    }
                    binding.rgOptions.addView(radioButton)
                }

                // Restore previously selected answer
                val savedAnswer = viewModel.selectedAnswers.value?.get(viewModel.currentQuestionIndex.value ?: 0)
                savedAnswer?.let { answer ->
                    for (i in 0 until binding.rgOptions.childCount) {
                        val rb = binding.rgOptions.getChildAt(i) as? RadioButton
                        if (rb?.text == answer) {
                            rb.isChecked = true
                            break
                        }
                    }
                }
            }
        }

        viewModel.currentQuestionIndex.observe(viewLifecycleOwner) { index ->
            val quiz = viewModel.currentQuiz.value
            val total = quiz?.questions?.size ?: 1
            binding.tvProgress.text = "${index + 1} / $total"
            binding.progressBar.max = total
            binding.progressBar.progress = index + 1

            // Show/hide navigation buttons
            binding.btnPrevious.visibility = if (index > 0) View.VISIBLE else View.INVISIBLE
            binding.btnSubmit.visibility = if (index == total - 1) View.VISIBLE else View.GONE
            binding.btnNext.visibility = if (index < total - 1) View.VISIBLE else View.GONE
        }

        viewModel.quizResult.observe(viewLifecycleOwner) { result ->
            result?.let {
                val bundle = Bundle().apply {
                    putString("quizId", arguments?.getString("quizId"))
                    putInt("score", it.score)
                    putBoolean("passed", it.passed)
                    putInt("correct", it.correctAnswers)
                    putInt("total", it.totalQuestions)
                }
                findNavController().navigate(R.id.action_quizActive_to_result, bundle)
            }
        }
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}
