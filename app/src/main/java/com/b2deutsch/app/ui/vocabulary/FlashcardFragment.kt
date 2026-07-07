package com.b2deutsch.app.ui.vocabulary

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.fragment.app.viewModels
import androidx.navigation.fragment.findNavController
import com.b2deutsch.app.data.model.VocabularyWord
import com.b2deutsch.app.databinding.FragmentFlashcardBinding
import dagger.hilt.android.AndroidEntryPoint

@AndroidEntryPoint
class FlashcardFragment : Fragment() {

    private var _binding: FragmentFlashcardBinding? = null
    private val binding get() = _binding!!

    private val viewModel: VocabularyViewModel by viewModels()

    private lateinit var level: String
    private lateinit var category: String
    private var deck: List<VocabularyWord> = emptyList()
    private var currentIndex = 0
    private var isFlipped = false

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentFlashcardBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        level = arguments?.getString("level") ?: "B2"
        category = arguments?.getString("category") ?: ""
        val categoryName = arguments?.getString("categoryName") ?: "Wortschatz"
        binding.tvProgress.text = categoryName

        binding.cardFlashcard.setOnClickListener {
            if (!isFlipped) flipCard()
        }
        binding.btnWrong.setOnClickListener { answer("wrong") }
        binding.btnHard.setOnClickListener { answer("hard") }
        binding.btnCorrect.setOnClickListener { answer("correct") }
        binding.btnBackToThemes.setOnClickListener { findNavController().popBackStack() }

        viewModel.isLoading.observe(viewLifecycleOwner) { isLoading ->
            binding.progressBar.visibility = if (isLoading) View.VISIBLE else View.GONE
        }

        viewModel.words.observe(viewLifecycleOwner) { words ->
            if (words.isNotEmpty() && deck.isEmpty() && currentIndex == 0) {
                deck = viewModel.getDueWords()
                currentIndex = 0
                if (deck.isEmpty()) {
                    showComplete("Alle Wörter in diesem Thema sind schon gelernt — schau später wieder vorbei!")
                } else {
                    showCard(currentIndex)
                }
            }
        }

        viewModel.loadWords(level, category)
    }

    private fun showCard(index: Int) {
        val word = deck[index]
        isFlipped = false
        binding.tvProgress.text = "${index + 1} / ${deck.size}"
        binding.tvPartOfSpeech.text = word.partOfSpeech
        binding.tvGerman.text = word.german
        binding.tvEnglish.text = word.english
        binding.tvTurkish.text = word.turkish
        binding.tvExample.text = word.exampleSentence
        binding.layoutBack.visibility = View.GONE
        binding.tvTapHint.visibility = View.VISIBLE
        binding.layoutActions.visibility = View.GONE
        binding.cardFlashcard.visibility = View.VISIBLE
        binding.layoutComplete.visibility = View.GONE
    }

    private fun flipCard() {
        isFlipped = true
        binding.layoutBack.visibility = View.VISIBLE
        binding.tvTapHint.visibility = View.GONE
        binding.layoutActions.visibility = View.VISIBLE
    }

    private fun answer(result: String) {
        val word = deck[currentIndex]
        viewModel.recordResult(word.id, result)
        currentIndex++
        if (currentIndex < deck.size) {
            showCard(currentIndex)
        } else {
            showComplete("Super, du hast alle ${deck.size} Wörter für heute geübt!")
        }
    }

    private fun showComplete(message: String) {
        binding.cardFlashcard.visibility = View.GONE
        binding.layoutActions.visibility = View.GONE
        binding.tvCompleteMessage.text = message
        binding.layoutComplete.visibility = View.VISIBLE
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}
