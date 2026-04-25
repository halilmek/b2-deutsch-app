package com.b2deutsch.app.ui.quiz

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.DiffUtil
import androidx.recyclerview.widget.ListAdapter
import androidx.recyclerview.widget.RecyclerView
import com.b2deutsch.app.R
import com.b2deutsch.app.databinding.ItemQuizResultBinding
import com.b2deutsch.app.ui.subject.QuestionResult

class QuizResultAdapter : ListAdapter<QuestionResult, QuizResultAdapter.ResultViewHolder>(ResultDiffCallback()) {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ResultViewHolder {
        val binding = ItemQuizResultBinding.inflate(
            LayoutInflater.from(parent.context),
            parent,
            false
        )
        return ResultViewHolder(binding)
    }

    override fun onBindViewHolder(holder: ResultViewHolder, position: Int) {
        holder.bind(getItem(position))
    }

    inner class ResultViewHolder(
        private val binding: ItemQuizResultBinding
    ) : RecyclerView.ViewHolder(binding.root) {

        fun bind(result: QuestionResult) {
            binding.tvQuestionNumber.text = "Frage ${result.questionNumber}"

            // Question text
            binding.tvQuestionText.text = result.questionText

            // Your answer
            if (result.userAnswer.isNotEmpty()) {
                binding.tvYourAnswer.text = "Deine Antwort: ${result.userAnswer}"
                binding.tvYourAnswer.setTextColor(
                    if (result.isCorrect) {
                        binding.root.context.getColor(R.color.green_600)
                    } else {
                        binding.root.context.getColor(R.color.red_500)
                    }
                )
            } else {
                binding.tvYourAnswer.text = "Keine Antwort gegeben"
                binding.tvYourAnswer.setTextColor(binding.root.context.getColor(R.color.gray_500))
            }

            // Correct answer
            if (!result.isCorrect) {
                binding.tvCorrectAnswer.text = "Richtige Antwort: ${result.correctAnswer}"
                binding.tvCorrectAnswer.visibility = android.view.View.VISIBLE
            } else {
                binding.tvCorrectAnswer.visibility = android.view.View.GONE
            }

            // Explanation
            if (result.explanation.isNotEmpty()) {
                binding.tvExplanation.text = "💡 ${result.explanation}"
                binding.tvExplanation.visibility = android.view.View.VISIBLE
            } else {
                binding.tvExplanation.visibility = android.view.View.GONE
            }

            // Result indicator
            binding.ivResult.setImageResource(
                if (result.isCorrect) android.R.drawable.presence_online
                else android.R.drawable.presence_busy
            )
        }
    }

    class ResultDiffCallback : DiffUtil.ItemCallback<QuestionResult>() {
        override fun areItemsTheSame(oldItem: QuestionResult, newItem: QuestionResult): Boolean {
            return oldItem.questionNumber == newItem.questionNumber
        }

        override fun areContentsTheSame(oldItem: QuestionResult, newItem: QuestionResult): Boolean {
            return oldItem == newItem
        }
    }
}
