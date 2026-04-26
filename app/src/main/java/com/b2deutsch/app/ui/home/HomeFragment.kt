package com.b2deutsch.app.ui.home

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.fragment.app.activityViewModels
import androidx.navigation.fragment.findNavController
import androidx.recyclerview.widget.GridLayoutManager
import com.b2deutsch.app.R
import com.b2deutsch.app.databinding.FragmentHomeBinding
import com.b2deutsch.app.ui.level.LevelAdapter
import dagger.hilt.android.AndroidEntryPoint

@AndroidEntryPoint
class HomeFragment : Fragment() {

    private var _binding: FragmentHomeBinding? = null
    private val binding get() = _binding!!

    private val homeViewModel: HomeViewModel by activityViewModels()

    private lateinit var levelAdapter: LevelAdapter

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentHomeBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        setupRecyclerView()
        setupClickListeners()
        observeViewModel()
        homeViewModel.loadData()
    }

    private fun setupRecyclerView() {
        levelAdapter = LevelAdapter(
            onLevelClick = { level ->
                homeViewModel.setCurrentLevel(level.id)
                val bundle = Bundle().apply {
                    putString("level", level.id)
                }
                findNavController().navigate(R.id.action_home_to_subjectList, bundle)
            },
            onExamsClick = { level ->
                homeViewModel.setCurrentLevel(level.id)
                findNavController().navigate(R.id.action_home_to_exams)
            }
        )

        binding.rvLevels.apply {
            layoutManager = GridLayoutManager(context, 2)
            adapter = levelAdapter
        }
    }

    private fun setupClickListeners() {
        // Exams card - goes to exams for selected level (default C1)
        binding.cardExams.setOnClickListener {
            findNavController().navigate(R.id.action_home_to_exams)
        }
    }

    private fun observeViewModel() {
        homeViewModel.currentUser.observe(viewLifecycleOwner) { user ->
            user?.let {
                binding.tvWelcome.text = "Welcome, ${it.displayName}!"
            }
        }

        homeViewModel.levels.observe(viewLifecycleOwner) { levels ->
            levelAdapter.submitList(levels)
        }

        homeViewModel.isLoading.observe(viewLifecycleOwner) { isLoading ->
            binding.progressBar.visibility = if (isLoading) View.VISIBLE else View.GONE
        }
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}
