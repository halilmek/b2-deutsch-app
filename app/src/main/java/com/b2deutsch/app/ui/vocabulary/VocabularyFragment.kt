package com.b2deutsch.app.ui.vocabulary

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.fragment.app.activityViewModels
import androidx.fragment.app.viewModels
import androidx.navigation.fragment.findNavController
import androidx.recyclerview.widget.LinearLayoutManager
import com.b2deutsch.app.R
import com.b2deutsch.app.databinding.FragmentVocabularyBinding
import com.b2deutsch.app.ui.home.HomeViewModel
import dagger.hilt.android.AndroidEntryPoint

@AndroidEntryPoint
class VocabularyFragment : Fragment() {

    private var _binding: FragmentVocabularyBinding? = null
    private val binding get() = _binding!!

    private val homeViewModel: HomeViewModel by activityViewModels()
    private val viewModel: VocabularyViewModel by viewModels()
    private lateinit var themeAdapter: VocabularyThemeAdapter

    private var currentLevel: String = "B2"

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentVocabularyBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        themeAdapter = VocabularyThemeAdapter { theme ->
            val bundle = Bundle().apply {
                putString("level", currentLevel)
                putString("category", theme.id)
                putString("categoryName", theme.name)
            }
            findNavController().navigate(R.id.action_vocabulary_to_flashcard, bundle)
        }
        binding.rvThemes.layoutManager = LinearLayoutManager(requireContext())
        binding.rvThemes.adapter = themeAdapter

        homeViewModel.currentLevel.observe(viewLifecycleOwner) { level ->
            currentLevel = level
            viewModel.loadThemes(level)
        }

        viewModel.themes.observe(viewLifecycleOwner) { themes ->
            themeAdapter.submitList(themes)
            binding.tvEmpty.visibility = if (themes.isEmpty()) View.VISIBLE else View.GONE
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
