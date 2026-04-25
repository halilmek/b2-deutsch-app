package com.b2deutsch.app.ui.subject

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
import javax.inject.Inject

@HiltViewModel
class SubjectListViewModel @Inject constructor(
    private val contentRepository: ContentRepository,
    private val userRepository: UserRepository
) : ViewModel() {

    private val _subjects = MutableLiveData<List<Subject>>()
    val subjects: LiveData<List<Subject>> = _subjects

    private val _progressMap = MutableLiveData<Map<String, SubjectProgress>>()
    val progressMap: LiveData<Map<String, SubjectProgress>> = _progressMap

    private val _isLoading = MutableLiveData<Boolean>()
    val isLoading: LiveData<Boolean> = _isLoading

    private val _selectedSubject = MutableLiveData<Subject?>()
    val selectedSubject: LiveData<Subject?> = _selectedSubject

    fun loadSubjectsForLevel(level: String) {
        viewModelScope.launch {
            _isLoading.value = true

            // Get all subjects for this level
            contentRepository.getSubjectsByLevel(level)
                .onSuccess { subjectList ->
                    _subjects.value = subjectList
                }
                .onFailure {
                    // Fall back to default subjects
                    _subjects.value = getDefaultSubjects(level)
                }

            // Load progress for each subject
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

    fun getDefaultSubjects(level: String): List<Subject> {
        return when (level) {
            "B2" -> getB2Subjects()
            "B1" -> getB1Subjects()
            "A2" -> getA2Subjects()
            "A1" -> getA1Subjects()
            "C1" -> getC1Subjects()
            else -> getB2Subjects()
        }
    }

    private fun getB2Subjects(): List<Subject> = listOf(
        // GRAMMAR
        Subject(
            id = "b2_grammatik_01",
            level = "B2",
            name = "Grammatik: Konjunktiv II",
            nameShort = "Konjunktiv II",
            description = "Der Konjunktiv II wird verwendet, um hypothetische Situationen, Wünsche und Höflichkeitsformen auszudrücken. Er beschreibt unrealistische Bedingungen und träumende Wünsche.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 1,
            quizCount = 3,
            tips = listOf(
                "Konjunktiv II = würde + Infinitiv (einfachste Form)",
                "z.B.: Ich würde gerne reisen (hypothetisch)",
                "Im Perfekt: würde + Partizip II von 'haben/sein'",
                "Häufig mit 'wenn' verwendet: Wenn ich Zeit hätte..."
            )
        ),
        Subject(
            id = "b2_grammatik_02",
            level = "B2",
            name = "Grammatik: Passiv",
            nameShort = "Passiv",
            description = "Das Passiv wird verwendet, wenn die Handlung wichtiger ist als der Handelnde. In der B2-Prüfung kommt oft das Zustandspassiv und das werden-Passiv vor.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 2,
            quizCount = 3,
            tips = listOf(
                "Vorgangspassiv: wird + Partizip II",
                "Zustandspassiv: ist + Partizip II",
                "'Man' + Aktiv = wird + Partizip II (Passiv)",
                "Von-Wendung: von + Dativ (wer macht etwas)"
            )
        ),
        Subject(
            id = "b2_grammatik_03",
            level = "B2",
            name = "Grammatik: Nebensätze",
            nameShort = "Nebensätze",
            description = "Nebensätze sind abhängige Sätze, die mit Konjunktionen (dass, weil, obwohl, wenn) eingeleitet werden. Das Verb steht am Ende des Nebensatzes.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 3,
            quizCount = 2,
            tips = listOf(
                "Weil/Sodass/Obwohl + Verb am Ende",
                "dass + Subjekt + Verb",
                "wenn + Verb am Ende (Bedingung)",
                "Bevor/Nachdem + Partizip II oder hatte/war"
            )
        ),
        Subject(
            id = "b2_grammatik_04",
            level = "B2",
            name = "Grammatik: Nominalisierung",
            nameShort = "Nominalisierung",
            description = "Nominalisierung bedeutet, Verben oder Adjektive in Nomen umzuwandeln. Das ist typisch für den gehobenen Schreibstil in B2-Prüfungen.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 4,
            quizCount = 2,
            tips = listOf(
                "Verben → Nomen: entscheiden → die Entscheidung",
                "Adj → Nomen: wichtig → die Wichtigkeit",
                "Nominalisierung macht Texte formeller",
                "Oft mit 'von' oder 'für': die Lösung des Problems"
            )
        ),

        // READING - LESEVERSTEHEN
        Subject(
            id = "b2_reading_01",
            level = "B2",
            name = "Lesen: Beruf und Arbeitswelt",
            nameShort = "Beruf",
            description = "Texte über Bewerbungen, Arbeitsbedingungen, Karriereplanung und den deutschen Arbeitsmarkt. Diese Themen sind Teil des Goethe B2 Exams.",
            category = Constants.Categories.READING,
            iconEmoji = "💼",
            order = 10,
            quizCount = 10,
            tips = listOf(
                "Achte auf Zahlen und Daten im Text",
                "Unterscheide Fakten von Meinungen",
                "Typische Wörter: Stellenanzeige, Bewerbung, Gehalt",
                "Übe das scrapbook-Methode: Thema → Gliederung → Details"
            )
        ),
        Subject(
            id = "b2_reading_02",
            level = "B2",
            name = "Lesen: Gesundheit und Medizin",
            nameShort = "Gesundheit",
            description = " Texte über Krankheiten, Prävention, das deutsche Gesundheitssystem und psychische Gesundheit. Wichtiges Thema für Alltag und Prüfung.",
            category = Constants.Categories.READING,
            iconEmoji = "🏥",
            order = 11,
            quizCount = 10,
            tips = listOf(
                "Gesundheitssystem-Artikel enthalten oft Zahlen",
                "Achte auf Symptom-Beschreibungen",
                "Typische Wörter: Symptome, Behandlung, Prävention",
                "Lese nach Fakten, nicht nach Meinungen"
            )
        ),
        Subject(
            id = "b2_reading_03",
            level = "B2",
            name = "Lesen: Umwelt und Natur",
            nameShort = "Umwelt",
            description = "Texte über Klimawandel, Nachhaltigkeit, erneuerbare Energien und Umweltschutz. Ein aktuelles Thema in allen deutschsprachigen Ländern.",
            category = Constants.Categories.READING,
            iconEmoji = "🌍",
            order = 12,
            quizCount = 10,
            tips = listOf(
                "Umweltthemen enthalten oft Prozent- und Zahlenangaben",
                "Erkene Argumentationsstruktur: Problem → Lösung",
                "Typische Wörter: Klimawandel, CO2, Nachhaltigkeit",
                "Wichtig: Meinung des Autors verstehen"
            )
        ),
        Subject(
            id = "b2_reading_04",
            level = "B2",
            name = "Lesen: Gesellschaft und Soziales",
            nameShort = "Gesellschaft",
            description = "Texte über Demografie, Integration, soziale Gerechtigkeit und den demografischen Wandel in Deutschland.",
            category = Constants.Categories.READING,
            iconEmoji = "👥",
            order = 13,
            quizCount = 10,
            tips = listOf(
                "Gesellschaftsthemen sind oft argumentativ",
                "Achte auf Kontrastwörter: jedoch, aber, andererseits",
                "Zahlen und Statistiken sind wichtige Detailfragen",
                "Verstehe die Kernaussage des Autors"
            )
        ),
        Subject(
            id = "b2_reading_05",
            level = "B2",
            name = "Lesen: Medien und Kommunikation",
            nameShort = "Medien",
            description = "Texte über soziale Medien, Datenschutz, Fake News und die Digitalisierung. Hochaktuell und relevant für die B2-Prüfung.",
            category = Constants.Categories.READING,
            iconEmoji = "📱",
            order = 14,
            quizCount = 5,
            tips = listOf(
                "Typische Wörter: Algorithmus, Datenschutz, Cybermobbing",
                "Verstehe den Unterschied zwischen Fakten und Meinungen",
                "Achte auf den Ton des Artikels (kritisch, neutral, positiv)",
                "DSGVO ist ein wichtiges Stichwort"
            )
        ),
        Subject(
            id = "b2_reading_06",
            level = "B2",
            name = "Lesen: Bildung und Erziehung",
            nameShort = "Bildung",
            description = "Texte über das deutsche Schulsystem, Hochschulbildung, lebenslanges Lernen und Bildungsungerechtigkeit.",
            category = Constants.Categories.READING,
            iconEmoji = "🎓",
            order = 15,
            quizCount = 5,
            tips = listOf(
                "Deutsches Schulsystem: Grundschule → Sekundarstufe",
                "Wichtig: Unterschied Ausbildung vs. Studium",
                "Typische Wörter: Gymnasium, Realschule, Hauptschule",
                "Bildungsthemen oft mit Statistiken"
            )
        ),

        // VOCABULARY - WORTSCHATZ
        Subject(
            id = "b2_vokabel_01",
            level = "B2",
            name = "Wortschatz: Beruf und Karriere",
            nameShort = "Beruf-Vokabeln",
            description = "Wichtige Vokabeln und Redewendungen für das Thema Beruf und Karriere. Unverzichtbar für die B2-Prüfung.",
            category = Constants.Categories.VOCABULARY,
            iconEmoji = "💼",
            order = 20,
            quizCount = 2,
            tips = listOf(
                "Lerne Vokabeln immer mit Artikel (der/die/das)",
                "Notiere auch die Verbalformen: sich bewerben → die Bewerbung",
                "Bildung von Nomen: arbeiten → die Arbeit, der Arbeitnehmer",
                "Übe mit Beispielsätzen, nicht nur einzelne Wörter"
            )
        ),
        Subject(
            id = "b2_vokabel_02",
            level = "B2",
            name = "Wortschatz: Umwelt und Nachhaltigkeit",
            nameShort = "Umwelt-Vokabeln",
            description = "Vokabeln rund um Umweltschutz, Klimawandel und nachhaltiges Leben. Ein häufiges Prüfungsthema.",
            category = Constants.Categories.VOCABULARY,
            iconEmoji = "🌍",
            order = 21,
            quizCount = 2,
            tips = listOf(
                "Grüne Vokabeln: nachhaltig, erneuerbar, recyceln",
                "Wortfamilien lernen: der Klimawandel → klimatisch → Klima",
                " opposites: erneuerbar ↔ endlich (Ressourcen)",
                "Lerne phraseologische Wendungen: CO2 ausstoßen"
            )
        )
    )

    private fun getB1Subjects(): List<Subject> = listOf(
        Subject(
            id = "b1_grammatik_01",
            level = "B1",
            name = "Grammatik: Perfekt",
            nameShort = "Perfekt",
            description = "Das Perfekt wird im Alltag häufig verwendet. Lerne die Verwendung von 'haben' und 'sein' als Hilfsverben.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 1,
            quizCount = 3
        ),
        Subject(
            id = "b1_reading_01",
            level = "B1",
            name = "Lesen: Alltag und Freizeit",
            nameShort = "Alltag",
            description = "Texte über Hobbys, Freizeitaktivitäten und den Alltag in Deutschland.",
            category = Constants.Categories.READING,
            iconEmoji = "⚽",
            order = 10,
            quizCount = 5
        )
    )

    private fun getA2Subjects(): List<Subject> = listOf(
        Subject(
            id = "a2_grammatik_01",
            level = "A2",
            name = "Grammatik: Präteritum",
            nameShort = "Präteritum",
            description = "Das Präteritum für die Vergangenheit. Besonders wichtig für 'sein', 'haben' und die Modalverben.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 1,
            quizCount = 3
        )
    )

    private fun getA1Subjects(): List<Subject> = listOf(
        Subject(
            id = "a1_grammatik_01",
            level = "A1",
            name = "Grammatik: Verben konjugieren",
            nameShort = "Verben",
            description = "Die wichtigsten Verben im Präsens: sein, haben, gehen, machen.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 1,
            quizCount = 2
        )
    )

    private fun getC1Subjects(): List<Subject> = listOf(
        Subject(
            id = "c1_grammatik_01",
            level = "C1",
            name = "Grammatik: Subjekterweiterung",
            nameShort = "Subjekterweiterung",
            description = "Komplexe Satzstrukturen mit Nominalisierung und erweiterten Attributen.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 1,
            quizCount = 4
        )
    )
}
