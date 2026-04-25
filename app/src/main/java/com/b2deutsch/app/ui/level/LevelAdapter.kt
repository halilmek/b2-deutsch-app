package com.b2deutsch.app.ui.level

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.recyclerview.widget.DiffUtil
import androidx.recyclerview.widget.ListAdapter
import androidx.recyclerview.widget.RecyclerView
import com.b2deutsch.app.data.model.Level
import com.b2deutsch.app.databinding.ItemLevelBinding

class LevelAdapter(
    private val onLevelClick: (Level) -> Unit,
    private val onExamsClick: ((Level) -> Unit)? = null
) : ListAdapter<Level, LevelAdapter.LevelViewHolder>(LevelDiffCallback()) {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): LevelViewHolder {
        val binding = ItemLevelBinding.inflate(
            LayoutInflater.from(parent.context),
            parent,
            false
        )
        return LevelViewHolder(binding)
    }

    override fun onBindViewHolder(holder: LevelViewHolder, position: Int) {
        holder.bind(getItem(position))
    }

    inner class LevelViewHolder(
        private val binding: ItemLevelBinding
    ) : RecyclerView.ViewHolder(binding.root) {

        fun bind(level: Level) {
            binding.tvLevelName.text = level.name
            binding.tvLevelDescription.text = level.description
            binding.tvLevelOrder.text = "Level ${level.order}"

            // Show Exams button for C1 (or any level with hasExams = true)
            if (level.hasExams) {
                binding.btnExams.visibility = View.VISIBLE
                binding.btnExams.setOnClickListener {
                    onExamsClick?.invoke(level)
                }
            } else {
                binding.btnExams.visibility = View.GONE
            }

            // Visual indicator for locked levels
            binding.ivLock.visibility = if (level.isLocked) {
                View.VISIBLE
            } else {
                View.GONE
            }

            // Set color based on level
            val colorRes = when (level.id) {
                "A1" -> android.R.color.holo_green_light
                "A2" -> android.R.color.holo_green_dark
                "B1" -> android.R.color.holo_orange_light
                "B2" -> android.R.color.holo_orange_dark
                "C1" -> android.R.color.holo_red_light
                else -> android.R.color.darker_gray
            }
            binding.cardLevel.setCardBackgroundColor(
                binding.root.context.getColor(colorRes)
            )

            binding.root.setOnClickListener {
                if (!level.isLocked) {
                    onLevelClick(level)
                }
            }
        }
    }

    class LevelDiffCallback : DiffUtil.ItemCallback<Level>() {
        override fun areItemsTheSame(oldItem: Level, newItem: Level): Boolean {
            return oldItem.id == newItem.id
        }

        override fun areContentsTheSame(oldItem: Level, newItem: Level): Boolean {
            return oldItem == newItem
        }
    }
}
