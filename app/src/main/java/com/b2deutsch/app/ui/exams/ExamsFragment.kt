package com.b2deutsch.app.ui.exams

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.LinearLayout
import android.widget.TextView
import androidx.fragment.app.Fragment
import androidx.navigation.fragment.findNavController
import com.b2deutsch.app.R
import com.b2deutsch.app.databinding.FragmentExamsBinding
import dagger.hilt.android.AndroidEntryPoint

@AndroidEntryPoint
class ExamsFragment : Fragment() {

    private var _binding: FragmentExamsBinding? = null
    private val binding get() = _binding!!

    private lateinit var currentLevel: String

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentExamsBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        currentLevel = arguments?.getString("level") ?: "C1"
        setupUI()
        loadExamTypes()
    }

    private fun setupUI() {
        binding.tvLevelInfo.text = "$currentLevel Exam Simulations"
        
        binding.btnBack.setOnClickListener {
            findNavController().navigateUp()
        }
    }

    private fun loadExamTypes() {
        val container = binding.examTypesContainer
        container.removeAllViews()

        // C1 Goethe/ÖSD exam structure
        val examTypes = listOf(
            ExamType(
                id = "leseverstehen",
                title = "📖 Leseverstehen (Reading Comprehension)",
                description = "Read German texts and answer comprehension questions. Tests your ability to understand texts from various sources.",
                questionCount = 10,
                duration = "60 min",
                topics = listOf("Academic texts", "Newspaper articles", "Formal letters", "Technical manuals")
            ),
            ExamType(
                id = "horverstehen",
                title = "🎧 Hörverstehen (Listening Comprehension)",
                description = "Listen to dialogues and announcements, then answer questions. Tests your understanding of spoken German.",
                questionCount = 10,
                duration = "40 min",
                topics = listOf("Everyday conversations", "Public announcements", "Interviews", "News broadcasts")
            ),
            ExamType(
                id = "schreiben",
                title = "✍️ Schreiben (Writing)",
                description = "Write a formal letter or essay on a given topic. Tests your ability to express yourself clearly in German.",
                questionCount = 1,
                duration = "75 min",
                topics = listOf("Formal letter", "Essay", "Email", "Opinion piece")
            ),
            ExamType(
                id = "sprechen",
                title = "🎤 Sprechen (Speaking)",
                description = "Part 1: Present a topic. Part 2: Discuss a scenario with examiner. Tests spontaneous spoken German.",
                questionCount = 2,
                duration = "15 min",
                topics = listOf("Topic presentation", "Role-play discussion", "Argumentation", "Opinion exchange")
            )
        )

        for (exam in examTypes) {
            val card = createExamCard(exam)
            container.addView(card)
        }
    }

    private fun createExamCard(exam: ExamType): View {
        val card = com.google.android.material.card.MaterialCardView(requireContext()).apply {
            layoutParams = LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT,
                LinearLayout.LayoutParams.WRAP_CONTENT
            ).apply {
                setMargins(0, 0, 0, 16)
            }
            radius = 16f
            cardElevation = 4f
            setCardBackgroundColor(requireContext().getColor(R.color.gray_100))
        }

        val content = LinearLayout(requireContext()).apply {
            orientation = LinearLayout.VERTICAL
            setPadding(16, 16, 16, 16)
        }

        content.addView(TextView(requireContext()).apply {
            text = exam.title
            textSize = 18f
            setTextColor(requireContext().getColor(R.color.black))
            setTypeface(typeface, android.graphics.Typeface.BOLD)
        })

        content.addView(TextView(requireContext()).apply {
            text = exam.description
            textSize = 14f
            setTextColor(requireContext().getColor(R.color.gray_600))
            setPadding(0, 8, 0, 8)
        })

        content.addView(TextView(requireContext()).apply {
            text = "📝 $questionCount questions  |  ⏱️ $duration"
            textSize = 12f
            setTextColor(requireContext().getColor(R.color.purple_700))
        })

        val topicsLabel = TextView(requireContext()).apply {
            text = "Topics: ${exam.topics.joinToString(", ")}"
            textSize = 12f
            setTextColor(requireContext().getColor(R.color.gray_500))
            setPadding(0, 8, 0, 0)
        }
        content.addView(topicsLabel)

        val startBtn = com.google.android.material.button.MaterialButton(requireContext()).apply {
            text = "Start Exam"
            layoutParams = LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT,
                LinearLayout.LayoutParams.WRAP_CONTENT
            ).apply { topMargin = 16 }
            setBackgroundColor(requireContext().getColor(R.color.purple_700))
            setOnClickListener {
                navigateToExam(exam)
            }
        }
        content.addView(startBtn)

        card.addView(content)
        return card
    }

    private fun navigateToExam(exam: ExamType) {
        val bundle = Bundle().apply {
            putString("examId", exam.id)
            putString("level", currentLevel)
            putString("examTitle", exam.title)
        }
        findNavController().navigate(R.id.action_exams_to_examActive, bundle)
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}

data class ExamType(
    val id: String,
    val title: String,
    val description: String,
    val questionCount: Int,
    val duration: String,
    val topics: List<String>
)
