package com.b2deutsch.app.ui.lessons

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.fragment.app.activityViewModels
import androidx.navigation.fragment.findNavController
import com.b2deutsch.app.databinding.FragmentLessonDetailBinding
import dagger.hilt.android.AndroidEntryPoint

@AndroidEntryPoint
class LessonDetailFragment : Fragment() {

    private var _binding: FragmentLessonDetailBinding? = null
    private val binding get() = _binding!!

    private val viewModel: LessonsViewModel by activityViewModels()

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentLessonDetailBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        val lessonId = arguments?.getString("lessonId") ?: return

        viewModel.selectLesson(lessonId)

        viewModel.selectedLesson.observe(viewLifecycleOwner) { lesson ->
            lesson?.let {
                binding.tvLessonTitle.text = it.title
                binding.tvLessonDescription.text = it.description
                binding.tvDuration.text = "${it.duration} min"
                binding.tvCategory.text = it.category.replaceFirstChar { c -> c.uppercase() }

                // Build content from sections
                val contentBuilder = StringBuilder()
                it.sections.forEach { section ->
                    contentBuilder.append("${section.title}\n${section.content}\n\n")
                }
                binding.tvContent.text = if (contentBuilder.isNotEmpty()) {
                    contentBuilder.toString()
                } else {
                    "Content coming soon..."
                }
            }
        }

        binding.btnMarkComplete.setOnClickListener {
            // TODO: Mark lesson as complete in Firestore
            findNavController().popBackStack()
        }
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}
