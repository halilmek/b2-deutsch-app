package com.b2deutsch.app.ui.quiz

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.LinearLayout
import android.widget.TextView
import androidx.core.content.ContextCompat
import androidx.fragment.app.Fragment
import androidx.fragment.app.activityViewModels
import androidx.navigation.fragment.findNavController
import com.b2deutsch.app.R
import com.b2deutsch.app.data.model.WrongAnswer
import com.b2deutsch.app.databinding.FragmentQuizResultBinding
import dagger.hilt.android.AndroidEntryPoint

@AndroidEntryPoint
class QuizResultFragment : Fragment() {

    private var _binding: FragmentQuizResultBinding? = null
    private val binding get() = _binding!!

    private val viewModel: QuizViewModel by activityViewModels()

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentQuizResultBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        val score = arguments?.getInt("score", 0) ?: 0
        val passed = arguments?.getBoolean("passed", false) ?: false
        val correct = arguments?.getInt("correct", 0) ?: 0
        val total = arguments?.getInt("total", 0) ?: 0
        val subjectId = arguments?.getString("subjectId")

        binding.tvScore.text = "$score%"
        binding.tvCorrectCount.text = "$correct / $total correct answers"

        if (passed) {
            binding.tvResultStatus.text = "🎉 Passed!"
            binding.tvResultStatus.setTextColor(ContextCompat.getColor(requireContext(), R.color.success))
        } else {
            binding.tvResultStatus.text = "📚 Keep Practicing!"
            binding.tvResultStatus.setTextColor(ContextCompat.getColor(requireContext(), R.color.error))
        }

        // Observe progress (isComplete and quizMessage)
        observeViewModel()

        // Show wrong answers report
        showWrongAnswersReport()

        // Next Quiz button - gets 10 new questions from active pool
        binding.btnNextQuiz.setOnClickListener {
            subjectId?.let { id ->
                viewModel.startNextQuiz()
                val bundle = Bundle().apply {
                    putString("quizId", "${id}_quiz_1")
                    putString("subjectId", id)
                }
                findNavController().navigate(R.id.action_result_to_nextQuiz, bundle)
            }
        }

        // Retry button - retry SAME 10 questions
        binding.btnRetry.setOnClickListener {
            viewModel.retryQuiz()
            findNavController().popBackStack()
        }

        binding.btnHome.setOnClickListener {
            findNavController().navigate(R.id.homeFragment)
        }

        binding.btnBackToSubjects.setOnClickListener {
            findNavController().navigate(R.id.action_result_to_subjectList)
        }
    }

    private fun observeViewModel() {
        // Update progress bar
        val progressStr = viewModel.getProgressString()
        binding.tvProgress.text = progressStr
        val solved = progressStr.split("/").firstOrNull()?.toIntOrNull() ?: 0
        binding.progressQuiz.progress = solved

        // Observe completion state
        viewModel.isComplete.observe(viewLifecycleOwner) { isComplete ->
            if (isComplete) {
                binding.cardComplete.visibility = View.VISIBLE
                binding.btnNextQuiz.visibility = View.GONE
                binding.tvLoopMessage.visibility = View.GONE
            } else {
                binding.cardComplete.visibility = View.GONE
                binding.btnNextQuiz.visibility = View.VISIBLE
            }
        }

        // Observe messages (loop restart, etc.)
        viewModel.quizMessage.observe(viewLifecycleOwner) { message ->
            if (!message.isNullOrEmpty()) {
                binding.tvLoopMessage.text = message
                binding.tvLoopMessage.visibility = View.VISIBLE
            } else {
                binding.tvLoopMessage.visibility = View.GONE
            }
        }
    }

    private fun showWrongAnswersReport() {
        val result = viewModel.quizResult.value ?: return
        val wrongAnswers = result.wrongAnswers
        
        if (wrongAnswers.isEmpty()) {
            binding.tvWrongAnswersHeader.visibility = View.GONE
            return
        }
        
        binding.tvWrongAnswersHeader.visibility = View.VISIBLE
        binding.tvWrongAnswersHeader.text = "📋 Review Wrong Answers (${wrongAnswers.size})"
        
        val container = binding.wrongAnswersContainer
        container.removeAllViews()
        
        wrongAnswers.forEachIndexed { index, wrong ->
            val card = createWrongAnswerCard(index + 1, wrong)
            container.addView(card)
        }
    }
    
    private fun createWrongAnswerCard(number: Int, wrong: WrongAnswer): View {
        val card = LinearLayout(requireContext()).apply {
            orientation = LinearLayout.VERTICAL
            setBackgroundResource(R.drawable.card_background)
            setPadding(32, 24, 32, 24)
            layoutParams = LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT,
                LinearLayout.LayoutParams.WRAP_CONTENT
            ).apply {
                setMargins(0, 16, 0, 0)
            }
        }
        
        // Question number
        val numText = TextView(requireContext()).apply {
            text = "Question $number"
            textSize = 14f
            setTextColor(ContextCompat.getColor(context, R.color.purple_700))
        }
        
        // Question text
        val qText = TextView(requireContext()).apply {
            text = wrong.questionText
            textSize = 16f
            setTextColor(ContextCompat.getColor(context, R.color.black))
            setPadding(0, 16, 0, 0)
        }
        
        // Your answer (wrong)
        val yourAnswer = TextView(requireContext()).apply {
            text = "❌ Your answer: ${wrong.yourAnswer}"
            textSize = 14f
            setTextColor(ContextCompat.getColor(context, R.color.error))
            setPadding(0, 16, 0, 0)
        }
        
        // Correct answer
        val correctAnswer = TextView(requireContext()).apply {
            text = "✅ Correct answer: ${wrong.correctAnswer}"
            textSize = 14f
            setTextColor(ContextCompat.getColor(context, R.color.success))
            setPadding(0, 8, 0, 0)
        }
        
        // Explanation
        val explanation = TextView(requireContext()).apply {
            text = "💡 ${wrong.explanation}"
            textSize = 13f
            setTextColor(ContextCompat.getColor(context, android.R.color.darker_gray))
            setPadding(0, 8, 0, 0)
        }
        
        card.addView(numText)
        card.addView(qText)
        card.addView(yourAnswer)
        card.addView(correctAnswer)
        card.addView(explanation)
        
        return card
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}
