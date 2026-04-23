package com.b2deutsch.app.ui.lessons

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.fragment.app.activityViewModels
import androidx.navigation.fragment.findNavController
import androidx.recyclerview.widget.LinearLayoutManager
import com.b2deutsch.app.R
import com.b2deutsch.app.databinding.FragmentLessonsBinding
import com.b2deutsch.app.ui.home.HomeViewModel
import dagger.hilt.android.AndroidEntryPoint

@AndroidEntryPoint
class LessonsFragment : Fragment() {

    private var _binding: FragmentLessonsBinding? = null
    private val binding get() = _binding!!

    private val viewModel: LessonsViewModel by activityViewModels()
    private val homeViewModel: HomeViewModel by activityViewModels()

    private lateinit var lessonAdapter: LessonAdapter

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentLessonsBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        setupRecyclerView()
        observeViewModel()
    }

    private fun setupRecyclerView() {
        lessonAdapter = LessonAdapter { lesson ->
            // Navigate to lesson detail
            val bundle = Bundle().apply {
                putString("lessonId", lesson.id)
            }
            findNavController().navigate(R.id.action_lessons_to_detail, bundle)
        }

        binding.rvLessons.apply {
            layoutManager = LinearLayoutManager(context)
            adapter = lessonAdapter
        }
    }

    private fun observeViewModel() {
        homeViewModel.currentLevel.observe(viewLifecycleOwner) { level ->
            binding.tvLevel.text = "Level: $level"
            viewModel.loadLessons(level)
        }

        viewModel.lessons.observe(viewLifecycleOwner) { lessons ->
            lessonAdapter.submitList(lessons)
            binding.tvEmpty.visibility = if (lessons.isEmpty()) View.VISIBLE else View.GONE
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
