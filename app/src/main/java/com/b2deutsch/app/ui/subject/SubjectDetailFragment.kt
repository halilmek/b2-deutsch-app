package com.b2deutsch.app.ui.subject

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.fragment.app.viewModels
import androidx.navigation.fragment.findNavController
import com.b2deutsch.app.R
import com.b2deutsch.app.data.local.LocalQuestionBank
import com.b2deutsch.app.databinding.FragmentSubjectDetailBinding
import dagger.hilt.android.AndroidEntryPoint

@AndroidEntryPoint
class SubjectDetailFragment : Fragment() {

    private var _binding: FragmentSubjectDetailBinding? = null
    private val binding get() = _binding!!

    private val viewModel: SubjectListViewModel by viewModels()

    private var subjectId: String = ""
    private var subjectName: String = ""

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        subjectId = arguments?.getString("subjectId") ?: ""
        subjectName = arguments?.getString("subjectName") ?: ""
    }

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentSubjectDetailBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        setupUI()
        observeViewModel()
    }

    private fun setupUI() {
        binding.tvSubjectTitle.text = subjectName

        // Back button
        binding.btnBack.setOnClickListener {
            findNavController().navigateUp()
        }

        // Start Quiz button - navigate to quiz with subjectId
        binding.btnStartQuiz.setOnClickListener {
            val bundle = Bundle().apply {
                putString("quizId", "${subjectId}_quiz_1")
                putString("subjectId", subjectId)
            }
            findNavController().navigate(R.id.action_subjectDetail_to_quizActive, bundle)
        }

        // Load subject details
        loadSubject(subjectId)
    }

    private fun observeViewModel() {
        viewModel.subjects.observe(viewLifecycleOwner) { subjects ->
            val subject = subjects.find { it.id == subjectId }
            subject?.let {
                // Dynamically compute quizCount from actual question count in JSON
                val totalQ = LocalQuestionBank.getTotalQuestionCount(requireContext(), it.id)
                val computedQuizCount = if (totalQ > 0) (totalQ + 9) / 10 else it.quizCount
                bindSubject(it.copy(questionCount = totalQ, quizCount = computedQuizCount))
            }
        }
    }

    private fun loadSubject(id: String) {
        val level = arguments?.getString("level") ?: "B2"
        viewModel.loadSubjectsForLevel(level)
    }

    private fun bindSubject(subject: com.b2deutsch.app.data.model.Subject) {
        binding.tvSubjectIcon.text = subject.iconEmoji
        binding.tvSubjectDescription.text = subject.description

        // Show category
        binding.tvCategory.text = getCategoryLabel(subject.category)

        // Show tips
        if (subject.tips.isNotEmpty()) {
            binding.tvTipsTitle.visibility = View.VISIBLE
            binding.tvTips.visibility = View.VISIBLE
            binding.tvTips.text = subject.tips.joinToString("\n\n") { "• $it" }
        } else {
            binding.tvTipsTitle.visibility = View.GONE
            binding.tvTips.visibility = View.GONE
        }

        // Quiz count — dynamically computed from JSON file (questions ÷ 10)
        val totalQ = LocalQuestionBank.getTotalQuestionCount(requireContext(), subject.id)
        val computedQuizCount = if (totalQ > 0) (totalQ + 9) / 10 else subject.quizCount
        binding.tvQuizCount.text = "$totalQ Fragen · $computedQuizCount Quiz verfügbar"

        // Start Quiz button
        binding.btnStartQuiz.isEnabled = computedQuizCount > 0
        binding.btnStartQuiz.text = if (computedQuizCount > 0) "Quiz starten" else "Bald verfügbar"
    }

    private fun getCategoryLabel(category: String): String {
        return when (category) {
            "grammar" -> "📝 Grammatik"
            "vocabulary" -> "🎴 Wortschatz"
            "reading" -> "📖 Lesen"
            "listening" -> "🎧 Hören"
            "writing" -> "✍️ Schreiben"
            "speaking" -> "🎤 Sprechen"
            else -> category
        }
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}