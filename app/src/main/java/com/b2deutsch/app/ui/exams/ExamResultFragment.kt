package com.b2deutsch.app.ui.exams

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.navigation.fragment.findNavController
import com.b2deutsch.app.R
import com.b2deutsch.app.databinding.FragmentExamResultBinding
import dagger.hilt.android.AndroidEntryPoint

@AndroidEntryPoint
class ExamResultFragment : Fragment() {

    private var _binding: FragmentExamResultBinding? = null
    private val binding get() = _binding!!

    private lateinit var examId: String
    private lateinit var level: String

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentExamResultBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        
        examId = arguments?.getString("examId") ?: ""
        level = arguments?.getString("level") ?: "C1"
        
        setupUI()
        displayResults()
    }

    private fun setupUI() {
        binding.btnRetry.setOnClickListener {
            findNavController().navigateUp()
        }
        
        binding.btnBackToExams.setOnClickListener {
            findNavController().popBackStack()
        }
        
        binding.btnShare.setOnClickListener {
            shareResults()
        }
    }

    private fun displayResults() {
        // Sample score - in real app, this would come from the exam submission
        val score = 85
        val passed = score >= 70
        
        binding.tvScore.text = "${score}%"
        binding.tvCorrectCount.text = "8 von 10 richtig"
        binding.tvTimeSpent.text = "Zeit: 45 min"
        
        if (passed) {
            binding.tvPassFail.text = "🎉 Bestanden!"
            binding.cardScore.setCardBackgroundColor(requireContext().getColor(R.color.green_100))
        } else {
            binding.tvPassFail.text = "😅 Nicht bestanden"
            binding.cardScore.setCardBackgroundColor(requireContext().getColor(R.color.red_100))
        }
        
        binding.tvEncouragement.text = getEncouragementMessage(score)
    }

    private fun getEncouragementMessage(score: Int): String {
        return when {
            score >= 90 -> "Ausgezeichnet! Du beherrschst dieses Examensformat sehr gut! 🌟"
            score >= 70 -> "Gut gemacht! Du hast bestanden! 👍"
            score >= 50 -> "Nicht schlecht! Übung macht den Meister! 💪"
            else -> "Keine Sorge! Versuche es noch einmal, du schaffst es! 📚"
        }
    }

    private fun shareResults() {
        // Share functionality would go here
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}
