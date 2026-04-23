package com.b2deutsch.app.ui.quiz

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.DiffUtil
import androidx.recyclerview.widget.ListAdapter
import androidx.recyclerview.widget.RecyclerView
import com.b2deutsch.app.data.model.Quiz
import com.b2deutsch.app.databinding.ItemQuizBinding

class QuizAdapter(
    private val onQuizClick: (Quiz) -> Unit
) : ListAdapter<Quiz, QuizAdapter.QuizViewHolder>(QuizDiffCallback()) {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): QuizViewHolder {
        val binding = ItemQuizBinding.inflate(
            LayoutInflater.from(parent.context),
            parent,
            false
        )
        return QuizViewHolder(binding)
    }

    override fun onBindViewHolder(holder: QuizViewHolder, position: Int) {
        holder.bind(getItem(position))
    }

    inner class QuizViewHolder(
        private val binding: ItemQuizBinding
    ) : RecyclerView.ViewHolder(binding.root) {

        fun bind(quiz: Quiz) {
            binding.tvQuizTitle.text = quiz.title
            binding.tvQuizDescription.text = quiz.description
            binding.tvQuestionCount.text = "${quiz.questions.size} questions"
            binding.tvTimeLimit.text = "${quiz.timeLimit} min"
            binding.tvPassingScore.text = "Pass: ${quiz.passingScore}%"

            binding.root.setOnClickListener {
                onQuizClick(quiz)
            }
        }
    }

    class QuizDiffCallback : DiffUtil.ItemCallback<Quiz>() {
        override fun areItemsTheSame(oldItem: Quiz, newItem: Quiz): Boolean {
            return oldItem.id == newItem.id
        }

        override fun areContentsTheSame(oldItem: Quiz, newItem: Quiz): Boolean {
            return oldItem == newItem
        }
    }
}
