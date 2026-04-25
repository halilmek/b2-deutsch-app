package com.b2deutsch.app.ui.quiz

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.fragment.app.activityViewModels
import androidx.navigation.fragment.findNavController
import com.b2deutsch.app.R
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
            binding.tvResultStatus.setTextColor(resources.getColor(R.color.success, null))
        } else {
            binding.tvResultStatus.text = "📚 Keep Practicing!"
            binding.tvResultStatus.setTextColor(resources.getColor(R.color.error, null))
        }

        // Next Quiz button - starts a new quiz with same subject
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

        binding.btnRetry.setOnClickListener {
            subjectId?.let { id ->
                viewModel.startNextQuiz()
                val bundle = Bundle().apply {
                    putString("quizId", "${id}_quiz_1")
                    putString("subjectId", id)
                }
                findNavController().navigate(R.id.action_result_to_nextQuiz, bundle)
            }
        }

        binding.btnHome.setOnClickListener {
            findNavController().navigate(R.id.homeFragment)
        }

        binding.btnBackToSubjects.setOnClickListener {
            findNavController().navigate(R.id.action_result_to_subjectList)
        }
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}
