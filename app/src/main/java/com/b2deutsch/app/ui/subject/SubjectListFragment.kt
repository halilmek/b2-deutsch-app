package com.b2deutsch.app.ui.subject

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
import com.b2deutsch.app.databinding.FragmentSubjectListBinding
import com.b2deutsch.app.ui.home.HomeViewModel
import dagger.hilt.android.AndroidEntryPoint

@AndroidEntryPoint
class SubjectListFragment : Fragment() {

    private var _binding: FragmentSubjectListBinding? = null
    private val binding get() = _binding!!

    private val viewModel: SubjectListViewModel by viewModels()
    private val homeViewModel: HomeViewModel by activityViewModels()

    private lateinit var subjectAdapter: SubjectAdapter

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
        setupRecyclerView()
        observeViewModel()
        loadData()
    }

    private fun setupRecyclerView() {
        subjectAdapter = SubjectAdapter { subject ->
            viewModel.selectSubject(subject)
            // Navigate to subject detail
            val bundle = Bundle().apply {
                putString("subjectId", subject.id)
                putString("subjectName", subject.name)
            }
            findNavController().navigate(R.id.action_subjectList_to_subjectDetail, bundle)
        }

        binding.rvSubjects.apply {
            layoutManager = LinearLayoutManager(context)
            adapter = subjectAdapter
        }
    }

    private fun observeViewModel() {
        homeViewModel.currentLevel.observe(viewLifecycleOwner) { level ->
            binding.tvLevel.text = "Level: $level"
            viewModel.loadSubjectsForLevel(level)
        }

        viewModel.subjects.observe(viewLifecycleOwner) { subjects ->
            subjectAdapter.submitList(subjects)
            binding.tvEmpty.visibility = if (subjects.isEmpty()) View.VISIBLE else View.GONE
        }

        viewModel.isLoading.observe(viewLifecycleOwner) { isLoading ->
            binding.progressBar.visibility = if (isLoading) View.VISIBLE else View.GONE
        }
    }

    private fun loadData() {
        val level = homeViewModel.currentLevel.value ?: "B2"
        viewModel.loadSubjectsForLevel(level)
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}
