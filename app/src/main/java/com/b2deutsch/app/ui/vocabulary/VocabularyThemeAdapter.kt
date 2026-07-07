package com.b2deutsch.app.ui.vocabulary

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.DiffUtil
import androidx.recyclerview.widget.ListAdapter
import androidx.recyclerview.widget.RecyclerView
import com.b2deutsch.app.data.model.VocabularyTheme
import com.b2deutsch.app.databinding.ItemVocabularyThemeBinding

class VocabularyThemeAdapter(
    private val onThemeClick: (VocabularyTheme) -> Unit
) : ListAdapter<VocabularyTheme, VocabularyThemeAdapter.ThemeViewHolder>(ThemeDiffCallback()) {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ThemeViewHolder {
        val binding = ItemVocabularyThemeBinding.inflate(
            LayoutInflater.from(parent.context),
            parent,
            false
        )
        return ThemeViewHolder(binding)
    }

    override fun onBindViewHolder(holder: ThemeViewHolder, position: Int) {
        holder.bind(getItem(position))
    }

    inner class ThemeViewHolder(
        private val binding: ItemVocabularyThemeBinding
    ) : RecyclerView.ViewHolder(binding.root) {

        fun bind(theme: VocabularyTheme) {
            binding.tvThemeIcon.text = theme.iconEmoji
            binding.tvThemeName.text = theme.name
            binding.tvThemeWordCount.text = "${theme.wordCount} Wörter"
            binding.root.setOnClickListener { onThemeClick(theme) }
        }
    }

    class ThemeDiffCallback : DiffUtil.ItemCallback<VocabularyTheme>() {
        override fun areItemsTheSame(oldItem: VocabularyTheme, newItem: VocabularyTheme) =
            oldItem.id == newItem.id

        override fun areContentsTheSame(oldItem: VocabularyTheme, newItem: VocabularyTheme) =
            oldItem == newItem
    }
}
