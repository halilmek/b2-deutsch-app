package com.b2deutsch.app.ui.subject

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.recyclerview.widget.DiffUtil
import androidx.recyclerview.widget.ListAdapter
import androidx.recyclerview.widget.RecyclerView
import com.b2deutsch.app.R
import com.b2deutsch.app.data.model.Subject
import com.b2deutsch.app.databinding.ItemSubjectBinding

class SubjectAdapter(
    private val onSubjectClick: (Subject) -> Unit
) : ListAdapter<Subject, SubjectAdapter.SubjectViewHolder>(SubjectDiffCallback()) {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): SubjectViewHolder {
        val binding = ItemSubjectBinding.inflate(
            LayoutInflater.from(parent.context),
            parent,
            false
        )
        return SubjectViewHolder(binding)
    }

    override fun onBindViewHolder(holder: SubjectViewHolder, position: Int) {
        holder.bind(getItem(position))
    }

    inner class SubjectViewHolder(
        private val binding: ItemSubjectBinding
    ) : RecyclerView.ViewHolder(binding.root) {

        fun bind(subject: Subject) {
            binding.tvSubjectIcon.text = subject.iconEmoji
            binding.tvSubjectName.text = subject.name
            binding.tvSubjectDescription.text = subject.description
            binding.tvQuizCount.text = "${subject.questionCount} Fragen · ${subject.quizCount} Quiz"

            // Category badge
            binding.tvCategory.text = getCategoryLabel(subject.category)
            binding.tvCategory.setBackgroundColor(getCategoryColor(subject.category))

            // Premium indicator
            binding.ivPremium.visibility = if (subject.isPremium) View.VISIBLE else View.GONE

            // Lock icon hidden — topics without quizzes are still clickable (user can read tips/explanation)
            binding.ivLock.visibility = View.GONE

            binding.root.setOnClickListener {
                onSubjectClick(subject)
            }
        }

        private fun getCategoryLabel(category: String): String {
            return when (category) {
                "grammar" -> "Grammatik"
                "vocabulary" -> "Wortschatz"
                "reading" -> "Lesen"
                "listening" -> "Hören"
                "writing" -> "Schreiben"
                "speaking" -> "Sprechen"
                else -> category
            }
        }

        private fun getCategoryColor(category: String): Int {
            val context = binding.root.context
            return when (category) {
                "grammar" -> context.getColor(R.color.purple_500)
                "vocabulary" -> context.getColor(R.color.purple_700)
                "reading" -> context.getColor(R.color.teal_700)
                "listening" -> context.getColor(R.color.orange_500)
                "writing" -> context.getColor(R.color.blue_500)
                "speaking" -> context.getColor(R.color.green_500)
                else -> context.getColor(R.color.purple_500)
            }
        }
    }

    class SubjectDiffCallback : DiffUtil.ItemCallback<Subject>() {
        override fun areItemsTheSame(oldItem: Subject, newItem: Subject): Boolean {
            return oldItem.id == newItem.id
        }

        override fun areContentsTheSame(oldItem: Subject, newItem: Subject): Boolean {
            return oldItem == newItem
        }
    }
}
