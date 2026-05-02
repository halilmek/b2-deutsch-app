package com.b2deutsch.app.ui.subject

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.fragment.app.viewModels
import androidx.navigation.fragment.findNavController
import androidx.recyclerview.widget.LinearLayoutManager
import com.b2deutsch.app.R
import com.b2deutsch.app.data.local.LocalQuestionBank
import com.b2deutsch.app.databinding.FragmentSubjectListBinding
import dagger.hilt.android.AndroidEntryPoint

@AndroidEntryPoint
class SubjectListFragment : Fragment() {

    private var _binding: FragmentSubjectListBinding? = null
    private val binding get() = _binding!!

    private val viewModel: SubjectListViewModel by viewModels()
    private lateinit var subjectAdapter: SubjectAdapter

    private var currentLevel: String = "B2"
    private var currentCategory: String? = null

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentSubjectListBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        
        // Get arguments from navigation
        currentLevel = arguments?.getString("level") ?: "B2"
        currentCategory = arguments?.getString("category")?.takeIf { it.isNotEmpty() }
        
        setupUI()
        observeViewModel()
        
        // Load based on category
        if (currentCategory != null) {
            // Load quizzes for the selected category
            viewModel.loadQuizzesForCategory(currentLevel, currentCategory!!)
            binding.tvHeader.text = when (currentCategory) {
                "reading" -> "📖 Reading"
                "listening" -> "🎧 Listening"
                "writing" -> "✍️ Writing"
                "speaking" -> "🎤 Speaking"
                else -> "📚 Quiz"
            }
        } else {
            // Load grammar topics as before
            viewModel.loadSubjectsForLevel(currentLevel)
            binding.tvHeader.text = "Themen"
        }
    }

    private fun setupUI() {
        binding.tvLevel.text = "Level: $currentLevel"

        subjectAdapter = SubjectAdapter { subject ->
            viewModel.selectSubject(subject)
            // For grammar topics, go to subject detail
            // For quiz categories, go directly to quiz
            if (currentCategory != null) {
                // Navigate to quiz directly
                val bundle = Bundle().apply {
                    putString("subjectId", subject.id)
                    putString("quizId", "${subject.id}_quiz_1")
                }
                findNavController().navigate(R.id.action_subjectList_to_quizActive, bundle)
            } else {
                // Navigate to subject detail (grammar flow)
                findNavController().navigate(
                    SubjectListFragmentDirections.actionSubjectListToSubjectDetail(
                        subjectId = subject.id,
                        subjectName = subject.name
                    )
                )
            }
        }

        binding.rvSubjects.apply {
            layoutManager = LinearLayoutManager(context)
            adapter = subjectAdapter
        }
    }

    private fun observeViewModel() {
        viewModel.subjects.observe(viewLifecycleOwner) { subjects ->
            if (subjects.isEmpty()) {
                binding.tvEmpty.visibility = View.VISIBLE
                binding.rvSubjects.visibility = View.GONE
                binding.tvEmpty.text = if (currentCategory != null) {
                    "No ${currentCategory} quizzes available yet"
                } else {
                    "No topics found"
                }
            } else {
                binding.tvEmpty.visibility = View.GONE
                binding.rvSubjects.visibility = View.VISIBLE
                // Dynamically compute questionCount and quizCount from actual question count in JSON files
                val updatedSubjects = subjects.map { subject ->
                    val totalQ = LocalQuestionBank.getTotalQuestionCount(requireContext(), subject.id)
                    val computedQuizCount = if (totalQ > 0) (totalQ + 9) / 10 else subject.quizCount
                    subject.copy(questionCount = totalQ, quizCount = computedQuizCount)
                }
                subjectAdapter.submitList(updatedSubjects)
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
