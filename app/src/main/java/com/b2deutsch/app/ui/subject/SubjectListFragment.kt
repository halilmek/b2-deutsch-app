package com.b2deutsch.app.ui.subject

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.fragment.app.viewModels
import androidx.navigation.fragment.findNavController
import androidx.recyclerview.widget.LinearLayoutManager
import com.b2deutsch.app.databinding.FragmentSubjectListBinding
import dagger.hilt.android.AndroidEntryPoint

@AndroidEntryPoint
class SubjectListFragment : Fragment() {

    private var _binding: FragmentSubjectListBinding? = null
    private val binding get() = _binding!!

    private val viewModel: SubjectListViewModel by viewModels()
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
        setupUI()
        observeViewModel()
        viewModel.loadSubjectsForLevel("B2")
    }

    private fun setupUI() {
        binding.tvHeader.text = "Themen"
        binding.tvLevel.text = "Level: B2"

        subjectAdapter = SubjectAdapter { subject ->
            viewModel.selectSubject(subject)
            findNavController().navigate(
                SubjectListFragmentDirections.actionSubjectListToSubjectDetail(
                    subjectId = subject.id,
                    subjectName = subject.name
                )
            )
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
            } else {
                binding.tvEmpty.visibility = View.GONE
                binding.rvSubjects.visibility = View.VISIBLE
                subjectAdapter.submitList(subjects)
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
