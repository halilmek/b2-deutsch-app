package com.b2deutsch.app.ui.subject

import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.fragment.app.viewModels
import androidx.navigation.fragment.findNavController
import com.b2deutsch.app.data.local.LocalQuestionBank
import com.b2deutsch.app.R
import com.b2deutsch.app.databinding.FragmentSubjectDetailBinding
import dagger.hilt.android.AndroidEntryPoint

@AndroidEntryPoint
class SubjectDetailFragment : Fragment() {

    private var _binding: FragmentSubjectDetailBinding? = null
    private val binding get() = _binding!!

    private val viewModel: SubjectListViewModel by viewModels()

    private var subjectId: String = ""
    private var subjectName: String = ""
    private var subjectLevel: String = "B2"

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        subjectId = arguments?.getString("subjectId") ?: ""
        subjectName = arguments?.getString("subjectName") ?: ""
        subjectLevel = arguments?.getString("level") ?: "B2"
        Log.d("SubjectDetail", "📥 Arguments — subjectId=$subjectId, subjectName=$subjectName, level=$subjectLevel")
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
        Log.d("SubjectDetail", "🎬 setupUI — subjectName=$subjectName")
        binding.tvSubjectTitle.text = subjectName

        // Back button — pass level to preserve in SubjectList
        binding.btnBack.setOnClickListener {
            val bundle = Bundle().apply {
                putString("level", subjectLevel)
            }
            findNavController().navigateUp()
        }

        // Start Quiz button - navigate to quiz with subjectId
        binding.btnStartQuiz.setOnClickListener {
            val bundle = Bundle().apply {
                putString("quizId", "${subjectId}_quiz_1")
                putString("subjectId", subjectId)
                putString("level", subjectLevel)
            }
            Log.d("SubjectDetail", "🎮 Starting quiz for subjectId=$subjectId")
            findNavController().navigate(R.id.action_subjectDetail_to_quizActive, bundle)
        }

        // Load subject details
        loadSubject(subjectId)
    }

    private fun observeViewModel() {
        Log.d("SubjectDetail", "👀 observeViewModel registered")
        viewModel.subjects.observe(viewLifecycleOwner) { subjects ->
            Log.d("SubjectDetail", "📨 subjects updated: ${subjects.size} subjects received")
            val subject = subjects.find { it.id == subjectId }
            if (subject != null) {
                Log.d("SubjectDetail", "✅ MATCHED subjectId=$subjectId | description len=${subject.description.length} | tips=${subject.tips.size}")
                Log.d("SubjectDetail", "📝 description[0..80]: ${subject.description.take(80)}")
            } else {
                Log.e("SubjectDetail", "❌ NO MATCH for subjectId=$subjectId")
                Log.d("SubjectDetail", "   Available ids: ${subjects.map { it.id }.joinToString()}")
            }
            subject?.let {
                val totalQ = LocalQuestionBank.getTotalQuestionCount(requireContext(), it.id)
                val computedQuizCount = if (totalQ > 0) (totalQ + 9) / 10 else it.quizCount
                Log.d("SubjectDetail", "📊 quizCount=$computedQuizCount, totalQ=$totalQ")
                bindSubject(it.copy(questionCount = totalQ, quizCount = computedQuizCount))
            }
        }
    }

    private fun loadSubject(id: String) {
        val level = subjectLevel
        Log.d("SubjectDetail", "📤 loadSubjectsForLevel($level) for subjectId=$id")
        viewModel.loadSubjectsForLevel(level)
    }

    private fun bindSubject(subject: com.b2deutsch.app.data.model.Subject) {
        Log.d("SubjectDetail", "🎨 bindSubject for ${subject.id}")
        binding.tvSubjectIcon.text = subject.iconEmoji
        binding.tvSubjectDescription.text = subject.description.ifEmpty {
            Log.e("SubjectDetail", "⚠️ description is EMPTY for ${subject.id}")
            "No description available"
        }

        // Show category
        binding.tvCategory.text = getCategoryLabel(subject.category)

        // Show tips
        Log.d("SubjectDetail", "💡 tips count: ${subject.tips.size}")
        if (subject.tips.isNotEmpty()) {
            binding.tvTipsTitle.visibility = View.VISIBLE
            binding.tvTips.visibility = View.VISIBLE
            binding.tvTips.text = subject.tips.joinToString("\n\n") { "• $it" }
        } else {
            Log.e("SubjectDetail", "⚠️ NO TIPS for ${subject.id}")
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