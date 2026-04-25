package com.b2deutsch.app.ui.subject

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.fragment.app.activityViewModels
import androidx.navigation.fragment.findNavController
import androidx.recyclerview.widget.LinearLayoutManager
import com.b2deutsch.app.R
import com.b2deutsch.app.databinding.FragmentSubjectResultBinding
import com.b2deutsch.app.ui.quiz.QuizResult
import com.b2deutsch.app.ui.quiz.QuizResultAdapter
import com.b2deutsch.app.ui.quiz.QuizViewModel
import dagger.hilt.android.AndroidEntryPoint

@AndroidEntryPoint
class SubjectResultFragment : Fragment() {

    private var _binding: FragmentSubjectResultBinding? = null
    private val binding get() = _binding!!

    private val quizViewModel: QuizViewModel by activityViewModels()

    private lateinit var resultAdapter: QuizResultAdapter

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentSubjectResultBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        setupUI()
        observeViewModel()
    }

    private fun setupUI() {
        // Back to Subjects button
        binding.btnBackToSubjects.setOnClickListener {
            findNavController().navigate(R.id.action_result_to_subjectList)
        }

        // Retry button
        binding.btnRetry.setOnClickListener {
            findNavController().navigateUp()
        }

        // Share button (optional)
        binding.btnShare.setOnClickListener {
            shareResults()
        }
    }

    private fun observeViewModel() {
        quizViewModel.quizResult.observe(viewLifecycleOwner) { result ->
            result?.let { displayResults(it) }
        }
    }

    private fun displayResults(result: QuizResult) {
        // Score display
        binding.tvScore.text = "${result.score}%"
        binding.tvCorrectCount.text = "${result.correctAnswers} von ${result.totalQuestions} richtig"

        // Pass/Fail indicator
        if (result.passed) {
            binding.tvPassFail.text = "🎉 Bestanden!"
            binding.tvPassFail.setTextColor(requireContext().getColor(R.color.green_500))
            binding.cardScore.setCardBackgroundColor(requireContext().getColor(R.color.green_100))
        } else {
            binding.tvPassFail.text = "😅 Nicht bestanden"
            binding.tvPassFail.setTextColor(requireContext().getColor(R.color.red_500))
            binding.cardScore.setCardBackgroundColor(requireContext().getColor(R.color.red_100))
        }

        // Encouragement message
        binding.tvEncouragement.text = getEncouragementMessage(result.score)

        // Time spent
        val minutes = result.timeSpent / 60
        val seconds = result.timeSpent % 60
        binding.tvTimeSpent.text = "Zeit: ${minutes}:${String.format("%02d", seconds)}"

        // Show result details
        setupResultsRecyclerView()
    }

    private fun setupResultsRecyclerView() {
        resultAdapter = QuizResultAdapter()
        binding.rvResults.apply {
            layoutManager = LinearLayoutManager(context)
            adapter = resultAdapter
        }

        // Submit quiz to get detailed results
        quizViewModel.submitQuiz()

        // Observe submitted result
        quizViewModel.quizResult.observe(viewLifecycleOwner) { result ->
            result?.let {
                quizViewModel.currentQuiz.value?.let { quiz ->
                    val results = quiz.questions.mapIndexed { index, question ->
                        val userAnswer = quizViewModel.selectedAnswers.value?.get(index) ?: ""
                        QuestionResult(
                            questionNumber = index + 1,
                            questionText = question.questionText,
                            userAnswer = userAnswer,
                            correctAnswer = question.correctAnswer,
                            explanation = question.explanation,
                            isCorrect = userAnswer == question.correctAnswer
                        )
                    }
                    resultAdapter.submitList(results)
                }
            }
        }
    }

    private fun getEncouragementMessage(score: Int): String {
        return when {
            score >= 90 -> "Ausgezeichnet! Du beherrschst dieses Thema sehr gut! 🌟"
            score >= 70 -> "Gut gemacht! Du bist auf dem richtigen Weg! 👍"
            score >= 50 -> "Nicht schlecht! Übung macht den Meister! 💪"
            else -> "Keine Sorge! Versuche es noch einmal, du schaffst es! 📚"
        }
    }

    private fun shareResults() {
        val result = quizViewModel.quizResult.value ?: return
        val shareText = """
            🏆 B2 Deutsch Quiz Ergebnis
            
            Score: ${result.score}%
            ${result.correctAnswers} von ${result.totalQuestions} richtig
            
            ${if (result.passed) "🎉 Bestanden!" else "😅 Nicht bestanden"}
            
            Mit ❤️ von B2 Deutsch App
        """.trimIndent()

        // Share intent would go here
        // For now, just show a toast or copy to clipboard
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}

/**
 * Data class for displaying question results
 */
data class QuestionResult(
    val questionNumber: Int,
    val questionText: String,
    val userAnswer: String,
    val correctAnswer: String,
    val explanation: String,
    val isCorrect: Boolean
)
