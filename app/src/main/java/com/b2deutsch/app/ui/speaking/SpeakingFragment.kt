package com.b2deutsch.app.ui.speaking

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.fragment.app.activityViewModels
import com.b2deutsch.app.databinding.FragmentSpeakingBinding
import com.b2deutsch.app.ui.home.HomeViewModel
import dagger.hilt.android.AndroidEntryPoint

@AndroidEntryPoint
class SpeakingFragment : Fragment() {

    private var _binding: FragmentSpeakingBinding? = null
    private val binding get() = _binding!!

    private val homeViewModel: HomeViewModel by activityViewModels()

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentSpeakingBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        homeViewModel.currentLevel.observe(viewLifecycleOwner) { level ->
            binding.tvLevel.text = "Level: $level"
        }

        binding.btnAIPartner.setOnClickListener {
            // TODO: Navigate to AI speaking partner
        }

        binding.btnPeerExam.setOnClickListener {
            // TODO: Find peer partner for exam
        }

        binding.tvInfo.text = "Practice your German speaking with:\n" +
                "• AI Partner - Unlimited practice with an AI\n" +
                "• Peer Exam - Practice with another user"
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}
