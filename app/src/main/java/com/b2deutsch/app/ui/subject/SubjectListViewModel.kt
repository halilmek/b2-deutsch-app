package com.b2deutsch.app.ui.subject

import android.app.Application
import android.util.Log
import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.b2deutsch.app.data.model.Subject
import com.b2deutsch.app.data.model.SubjectProgress
import com.b2deutsch.app.data.repository.ContentRepository
import com.b2deutsch.app.data.repository.UserRepository
import com.b2deutsch.app.util.Constants
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.launch
import org.json.JSONObject
import java.io.InputStreamReader
import javax.inject.Inject

@HiltViewModel
class SubjectListViewModel @Inject constructor(
    private val contentRepository: ContentRepository,
    private val userRepository: UserRepository,
    private val application: Application
) : ViewModel() {

    private val _subjects = MutableLiveData<List<Subject>>()
    val subjects: LiveData<List<Subject>> = _subjects

    private val _progressMap = MutableLiveData<Map<String, SubjectProgress>>()
    val progressMap: LiveData<Map<String, SubjectProgress>> = _progressMap

    private val _isLoading = MutableLiveData<Boolean>()
    val isLoading: LiveData<Boolean> = _isLoading

    private val _selectedSubject = MutableLiveData<Subject?>()
    val selectedSubject: LiveData<Subject?> = _selectedSubject

    /**
     * Level-agnostic subject loading — no hardcoded per-level lists.
     * Primary source: Firestore `topics` collection, filtered by level (dynamic —
     * a topic added there appears with no code change). On success, each result is
     * enriched with description/tips from the matching bundled asset JSON file, if
     * one exists (assets ship with the APK, so this is instant and doesn't need
     * network — no reason to skip it just because Firestore succeeded).
     * On Firestore failure (offline), falls back to discovering topics directly
     * from bundled assets by listing files matching "{level}_NN.json".
     */
    fun loadSubjectsForLevel(level: String) {
        viewModelScope.launch {
            _isLoading.value = true

            contentRepository.getSubjectsByLevel(level)
                .onSuccess { subjectList ->
                    _subjects.value = subjectList.map { enrichFromAssetJson(it) }
                }
                .onFailure {
                    Log.d("SubjectListVM", "Firestore topics unavailable for $level, falling back to bundled assets", it)
                    _subjects.value = discoverSubjectsFromAssets(level)
                }

            loadProgressForSubjects(level)
            _isLoading.value = false
        }
    }

    private suspend fun loadProgressForSubjects(level: String) {
        val userId = userRepository.currentUserId ?: return
        val subjectList = _subjects.value ?: return

        val progressMap = mutableMapOf<String, SubjectProgress>()
        subjectList.forEach { subject ->
            userRepository.getSubjectProgress(userId, subject.id)
                .onSuccess { progress ->
                    progressMap[subject.id] = progress
                }
        }
        _progressMap.value = progressMap
    }

    fun selectSubject(subject: Subject) {
        _selectedSubject.value = subject
    }

    fun loadQuizzesForCategory(level: String, category: String) {
        viewModelScope.launch {
            _isLoading.value = true

            // For quiz categories, return subjects that represent quiz topics
            val quizSubjects = when (category) {
                "reading" -> getReadingQuizSubjects(level)
                "listening" -> getListeningQuizSubjects(level)
                "writing" -> getWritingQuizSubjects(level)
                "speaking" -> getSpeakingQuizSubjects(level)
                else -> emptyList()
            }

            _subjects.value = quizSubjects
            _isLoading.value = false
        }
    }

    private fun getReadingQuizSubjects(level: String): List<Subject> = listOf(
        Subject(id = "${level.lowercase()}_reading_1", level = level, name = "📖 Beruf & Arbeit", nameShort = "Reading 1", description = "Reading comprehension about job and work topics.", category = Constants.Categories.READING, iconEmoji = "📖", order = 1, quizCount = 10),
        Subject(id = "${level.lowercase()}_reading_2", level = level, name = "📖 Gesundheit & Medizin", nameShort = "Reading 2", description = "Reading comprehension about health and medicine.", category = Constants.Categories.READING, iconEmoji = "📖", order = 2, quizCount = 10),
        Subject(id = "${level.lowercase()}_reading_3", level = level, name = "📖 Umwelt & Natur", nameShort = "Reading 3", description = "Reading comprehension about environment and nature.", category = Constants.Categories.READING, iconEmoji = "📖", order = 3, quizCount = 10),
        Subject(id = "${level.lowercase()}_reading_4", level = level, name = "📖 Gesellschaft & Soziales", nameShort = "Reading 4", description = "Reading comprehension about society and social issues.", category = Constants.Categories.READING, iconEmoji = "📖", order = 4, quizCount = 10),
        Subject(id = "${level.lowercase()}_reading_5", level = level, name = "📖 Medien & Kommunikation", nameShort = "Reading 5", description = "Reading comprehension about media and communication.", category = Constants.Categories.READING, iconEmoji = "📖", order = 5, quizCount = 10)
    )

    private fun getListeningQuizSubjects(level: String): List<Subject> = listOf(
        Subject(id = "${level.lowercase()}_listening_1", level = level, name = "🎧 Alltagsgespräche", nameShort = "Listening 1", description = "Listen to everyday conversations.", category = Constants.Categories.LISTENING, iconEmoji = "🎧", order = 1, quizCount = 8),
        Subject(id = "${level.lowercase()}_listening_2", level = level, name = "🎧 Nachrichten & Berichte", nameShort = "Listening 2", description = "Listen to news and reports.", category = Constants.Categories.LISTENING, iconEmoji = "🎧", order = 2, quizCount = 8),
        Subject(id = "${level.lowercase()}_listening_3", level = level, name = "🎧 Interviews & Diskussionen", nameShort = "Listening 3", description = "Listen to interviews and discussions.", category = Constants.Categories.LISTENING, iconEmoji = "🎧", order = 3, quizCount = 8)
    )

    private fun getWritingQuizSubjects(level: String): List<Subject> = listOf(
        Subject(id = "${level.lowercase()}_writing_1", level = level, name = "✍️ E-Mail schreiben", nameShort = "Writing 1", description = "Practice writing formal and informal emails.", category = Constants.Categories.WRITING, iconEmoji = "✍️", order = 1, quizCount = 5),
        Subject(id = "${level.lowercase()}_writing_2", level = level, name = "✍️ Foruminbeitrag", nameShort = "Writing 2", description = "Practice writing forum posts and comments.", category = Constants.Categories.WRITING, iconEmoji = "✍️", order = 2, quizCount = 5),
        Subject(id = "${level.lowercase()}_writing_3", level = level, name = "✍️ Aufsatz", nameShort = "Writing 3", description = "Practice essay writing with different topics.", category = Constants.Categories.WRITING, iconEmoji = "✍️", order = 3, quizCount = 5)
    )

    private fun getSpeakingQuizSubjects(level: String): List<Subject> = listOf(
        Subject(id = "${level.lowercase()}_speaking_1", level = level, name = "🎤 Alltagsgespräch", nameShort = "Speaking 1", description = "Practice everyday conversation.", category = Constants.Categories.SPEAKING, iconEmoji = "🎤", order = 1, quizCount = 5),
        Subject(id = "${level.lowercase()}_speaking_2", level = level, name = "🎤 Meinung äußern", nameShort = "Speaking 2", description = "Practice expressing opinions.", category = Constants.Categories.SPEAKING, iconEmoji = "🎤", order = 2, quizCount = 5),
        Subject(id = "${level.lowercase()}_speaking_3", level = level, name = "🎤 Diskussion", nameShort = "Speaking 3", description = "Practice discussion skills.", category = Constants.Categories.SPEAKING, iconEmoji = "🎤", order = 3, quizCount = 5)
    )

    // ============ DYNAMIC GRAMMAR SUBJECT DISCOVERY (no hardcoded per-level lists) ============

    /**
     * Overlay description/tips (and topicName, if the JSON has one) from the
     * bundled asset file onto a Subject that came from Firestore. Firestore's
     * `topics` collection only carries lightweight metadata (name, questionCount);
     * the richer authored content lives in the asset JSON that ships with the APK.
     */
    private fun enrichFromAssetJson(subject: Subject): Subject {
        val json = readAssetJson(subject.id) ?: return subject
        return subject.copy(
            name = json.optString("topicName", subject.name),
            nameShort = json.optString("topicName", subject.nameShort),
            description = json.optString("description", subject.description),
            tips = jsonTips(json) ?: subject.tips
        )
    }

    /**
     * Fully offline fallback: discover topics by listing bundled asset files
     * matching "{level}_NN.json" — adding a new asset file makes it appear here
     * with no code change, same as the Firestore path.
     */
    private fun discoverSubjectsFromAssets(level: String): List<Subject> {
        val prefix = "${level.lowercase()}_"
        val pattern = Regex("^${Regex.escape(prefix)}(\\d+)\\.json$")

        val fileNames = try {
            application.assets.list("")?.toList() ?: emptyList()
        } catch (e: Exception) {
            emptyList()
        }

        return fileNames
            .mapNotNull { fileName -> pattern.find(fileName)?.let { fileName to it.groupValues[1].toInt() } }
            .sortedBy { (_, order) -> order }
            .mapNotNull { (fileName, order) ->
                val subjectId = fileName.removeSuffix(".json")
                val json = readAssetJson(subjectId) ?: return@mapNotNull null
                val topicName = json.optString("topicName", subjectId)
                Subject(
                    id = subjectId,
                    level = level,
                    name = topicName,
                    nameShort = topicName,
                    description = json.optString("description", ""),
                    category = Constants.Categories.GRAMMAR,
                    iconEmoji = "📝",
                    order = order,
                    questionCount = json.optInt("totalQuestions", 0),
                    tips = jsonTips(json) ?: emptyList()
                )
            }
    }

    private fun readAssetJson(subjectId: String): JSONObject? {
        return try {
            application.assets.open("$subjectId.json").use { inputStream ->
                JSONObject(InputStreamReader(inputStream).readText())
            }
        } catch (e: Exception) {
            null
        }
    }

    private fun jsonTips(json: JSONObject): List<String>? {
        val tipsArray = json.optJSONArray("tips") ?: return null
        return (0 until tipsArray.length()).map { tipsArray.getString(it) }
    }
}
