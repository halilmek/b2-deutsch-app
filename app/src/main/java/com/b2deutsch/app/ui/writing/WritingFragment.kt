package com.b2deutsch.app.ui.writing

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.fragment.app.activityViewModels
import com.b2deutsch.app.databinding.FragmentWritingBinding
import com.b2deutsch.app.ui.home.HomeViewModel
import dagger.hilt.android.AndroidEntryPoint

@AndroidEntryPoint
class WritingFragment : Fragment() {

    private var _binding: FragmentWritingBinding? = null
    private val binding get() = _binding!!

    private val homeViewModel: HomeViewModel by activityViewModels()

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentWritingBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        homeViewModel.currentLevel.observe(viewLifecycleOwner) { level ->
            binding.tvLevel.text = "Level: $level"
        }

        binding.btnSubmit.setOnClickListener {
            val text = binding.etWriting.text.toString()
            if (text.length < 50) {
                binding.tilWriting.error = "Please write at least 50 characters"
            } else {
                binding.tilWriting.error = null
                // TODO: Submit for AI evaluation
                binding.tvResult.visibility = View.VISIBLE
                binding.tvResult.text = "Evaluation feature coming soon!"
            }
        }
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}
