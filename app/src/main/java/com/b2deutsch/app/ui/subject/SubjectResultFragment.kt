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
import com.b2deutsch.app.data.model.QuizResult
import com.b2deutsch.app.ui.quiz.QuizResultAdapter
import com.b2deutsch.app.ui.quiz.QuizViewModel
import com.google.android.material.dialog.MaterialAlertDialogBuilder
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

        // Retry button - retry SAME 10 questions
        binding.btnRetry.setOnClickListener {
            quizViewModel.retryQuiz()
            // Go back to quiz - SubjectDetailFragment will navigate to QuizActiveFragment
            findNavController().popBackStack(R.id.subjectDetailFragment, false)
        }

        // Next Quiz button - go back to subject list, user starts new quiz
        binding.btnNextQuiz.setOnClickListener {
            val level = arguments?.getString("level") ?: "B2"
            val bundle = Bundle().apply { putString("level", level) }
            findNavController().navigate(R.id.action_result_to_subjectList, bundle)
        }

        // Reset progress (when topic complete)
        binding.btnResetProgress.setOnClickListener {
            MaterialAlertDialogBuilder(requireContext())
                .setTitle("Fortschritt zurücksetzen?")
                .setMessage("Alle 100 Fragen werden wieder als ungeloest markiert.")
                .setPositiveButton("Ja, zurücksetzen") { _, _ ->
                    quizViewModel.resetTopicProgress()
                    val level = arguments?.getString("level") ?: "B2"
                    val bundle = Bundle().apply { putString("level", level) }
                    findNavController().navigate(R.id.action_result_to_subjectList, bundle)
                }
                .setNegativeButton("Abbrechen", null)
                .show()
        }

        // Share button
        binding.btnShare.setOnClickListener {
            shareResults()
        }
    }

    private fun observeViewModel() {
        quizViewModel.quizResult.observe(viewLifecycleOwner) { result ->
            result?.let { displayResults(it) }
        }

        quizViewModel.isComplete.observe(viewLifecycleOwner) { isComplete ->
            if (isComplete) {
                binding.cardComplete.visibility = View.VISIBLE
                binding.btnNextQuiz.visibility = View.GONE
            } else {
                binding.cardComplete.visibility = View.GONE
                binding.btnNextQuiz.visibility = View.VISIBLE
            }
        }

        quizViewModel.quizMessage.observe(viewLifecycleOwner) { message ->
            if (!message.isNullOrEmpty()) {
                binding.tvLoopMessage.text = message
                binding.tvLoopMessage.visibility = View.VISIBLE
            } else {
                binding.tvLoopMessage.visibility = View.GONE
            }
        }
    }

    private fun displayResults(result: QuizResult) {
        binding.tvScore.text = "${result.score}%"
        binding.tvCorrectCount.text = "${result.correctAnswers} von ${result.totalQuestions} richtig"

        if (result.passed) {
            binding.tvPassFail.text = "🎉 Bestanden!"
            binding.tvPassFail.setTextColor(requireContext().getColor(R.color.green_500))
            binding.cardScore.setCardBackgroundColor(requireContext().getColor(R.color.green_100))
        } else {
            binding.tvPassFail.text = "😅 Nicht bestanden"
            binding.tvPassFail.setTextColor(requireContext().getColor(R.color.red_500))
            binding.cardScore.setCardBackgroundColor(requireContext().getColor(R.color.red_100))
        }

        binding.tvEncouragement.text = getEncouragementMessage(result.score)

        val minutes = result.timeSpent / 60
        val seconds = result.timeSpent % 60
        binding.tvTimeSpent.text = "Zeit: ${minutes}:${String.format("%02d", seconds)}"

        // Progress
        val progressStr = quizViewModel.getProgressString()
        binding.tvProgress.text = progressStr
        val solved = progressStr.split("/").firstOrNull()?.toIntOrNull() ?: 0
        binding.progressQuiz.progress = solved
    }

    private fun getEncouragementMessage(score: Int): String {
        return when {
            score >= 90 -> "Ausgezeichnet! 🌟"
            score >= 70 -> "Gut gemacht! 👍"
            score >= 50 -> "Nicht schlecht! 💪"
            else -> "Keine Sorge! 📚"
        }
    }

    private fun shareResults() {
        val result = quizViewModel.quizResult.value ?: return
        val shareText = """
            🏆 B2 Deutsch Quiz Ergebnis
            Score: ${result.score}%
            ${result.correctAnswers} von ${result.totalQuestions} richtig
            ${if (result.passed) "🎉 Bestanden!" else "😅 Nicht bestanden"}
            ${quizViewModel.getProgressString()}
            Mit ❤️ von B2 Deutsch App
        """.trimIndent()

        val intent = android.content.Intent(android.content.Intent.ACTION_SEND).apply {
            type = "text/plain"
            putExtra(android.content.Intent.EXTRA_TEXT, shareText)
        }
        startActivity(android.content.Intent.createChooser(intent, "Teilen"))
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}
