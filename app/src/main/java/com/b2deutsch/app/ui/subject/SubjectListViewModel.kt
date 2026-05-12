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

    fun getDefaultSubjects(level: String): List<Subject> {
        return when (level) {
            "B2" -> getB2Subjects()
            "B1" -> getB1Subjects()
            "A2" -> getA2Subjects()
            "A1" -> getA1Subjects()
            "C1" -> getC1Subjects()
            "C2" -> getC2Subjects()
            else -> getB2Subjects()
        }
    }

    private fun getB2Subjects(): List<Subject> = listOf(
        // 1. Konnektoren: als, bevor, bis, seitdem, während, wenn, sobald, solange
        Subject(
            id = "b2_01",
            level = "B2",
            name = "1. Konnektoren",
            nameShort = "Konnektoren",
            description = "Konnektoren sind Wörter, die Sätze oder Satzteile miteinander verbinden. In der B2-Prüfung werden sie häufig verwendet, um komplexe Texte zu verstehen und zu schreiben. Die 8 temporalen Konnektoren beschreiben zeitliche Beziehungen zwischen Handlungen.\n\n" +
                "ALS — einmalige Situation in der Vergangenheit\n" +
                "• 'Als ich in Deutschland ankam, konnte ich kein Deutsch.'\n\n" +
                "BEVOR — zuerst Handlung A, dann Handlung B\n" +
                "• 'Bevor ich zur Prüfung ging, habe ich viel geübt.'\n\n" +
                "BIS — bis zu einem Zeitpunkt oder Ergebnis\n" +
                "• 'Ich warte hier, bis du fertig bist.'\n\n" +
                "SEITDEM — seit einem vergangenen Zeitpunkt bis jetzt\n" +
                "• 'Seitdem ich in Berlin wohne, fühle ich mich wohl.'\n\n" +
                "WÄHREND — zwei Handlungen geschehen gleichzeitig\n" +
                "• 'Während sie kocht, hört sie Musik.'\n\n" +
                "WENN — wiederholte Situation oder Zukunft\n" +
                "• 'Wenn es regnet, bleibe ich zu Hause.'\n\n" +
                "SOBALD — unmittelbare Abfolge\n" +
                "• 'Sobald ich ankomme, rufe ich dich an.'\n\n" +
                "SOLANGE — während der Zeitdauer einer Handlung\n" +
                "• 'Solange du lernst, darfst du hier bleiben.'",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "🔗",
            order = 1,
            quizCount = 0,
            tips = listOf(
                "ALS = einmalige Situation in der Vergangenheit (when — one time)",
                "BEVOR = zuerst Handlung A, dann Handlung B (before)",
                "BIS = bis zu einem Zeitpunkt oder Ergebnis (until)",
                "SEITDEM = seit einem vergangenen Zeitpunkt bis jetzt (since)",
                "WÄHREND = zwei Handlungen geschehen gleichzeitig (while)",
                "WENN = wiederholte Situation oder Zukunft (when/whenever)",
                "SOBALD = unmittelbare Abfolge zweier Handlungen (as soon as)",
                "SOLANGE = während der Zeitdauer einer Handlung (as long as)"
            )
        ),

        // 2. Verben und Ergänzungen
        Subject(
            id = "b2_02",
            level = "B2",
            name = "2. Verben und Ergänzungen",
            nameShort = "Verben und Ergänzungen",
            description = "In der B2-Prüfung ist es wichtig, die richtigen Verb-Ergänzungen zu kennen. Manche Verben brauchen den Akkusativ, andere den Dativ, und wieder andere beide. Einige Verben sind reflexiv oder erfordern eine Präposition.\n\nBeispiele:\n• 'Ich freue mich auf die Prüfung.' (reflexiv + Akkusativ)\n• 'Er arbeitet an einem Projekt.' (Dativ + Akkusativ)\n• 'Sie wartet auf ihren Freund.' (Akkusativ)",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 2,
            quizCount = 0,
            tips = listOf(
                "Verben mit Dativ: helfen, danken, glauben, antworten",
                "Verben mit Akkusativ: sehen, hören, finden, kennen",
                "Wechselpräpositionen: an, auf, in, über, vor, zwischen...",
                "Feste Präpositionen: denken an, warten auf, sprechen über",
                "Reflexive Verben: sich freuen, sich kümmern, sich erinnern"
            )
        ),
        // 3. Zeitformen in der Vergangenheit
        Subject(
            id = "b2_04",
            level = "B2",
            name = "3. Zeitformen in der Vergangenheit",
            nameShort = "Vergangenheit",
            description = "In der deutschen Grammatik gibt es mehrere Formen, um die Vergangenheit auszudrücken: Präteritum, Perfekt und Plusquamperfekt. Für die B2-Prüfung ist es wichtig, diese korrekt zu verwenden und den Unterschied zu verstehen.\n\nBeispiele:\n• 'Ich habe gestern Deutsch gelernt.' (Perfekt - abgeschlossene Handlung)\n• 'Ich war schon fertig, als er kam.' (Plusquamperfekt + Präteritum)",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "⏰",
            order = 3,
            quizCount = 0,
            tips = listOf(
                "PERFEKT = haben/sein (Präsens) + Partizip II",
                "PRÄTERITUM = wurde, war, hatte, konnte - häufig beiWritten verwendet",
                "PLUSQUAMPERFEKT = hatte/war + Partizip II (vor einer anderen Vergangenheit)",
                "Erzählungen: Präteritum für Hintergrund, Perfekt für Highlights",
                "Konjunktionen: als, wenn, bevor - helfen beim Strukturieren"
            )
        ),
        // 5. Zeitformen der Zukunft
        Subject(
            id = "b2_05",
            level = "B2",
            name = "4. Zeitformen der Zukunft",
            nameShort = "Zukunft",
            description = "Für die Zukunft gibt es im Deutschen zwei Hauptmethoden: 'werden' + Infinitativ für Vorhersagen und Pläne, sowie Präsens mit Zeitangabe für geplante Handlungen. Die B2-Prüfung erwartet den korrekten Gebrauch beider Formen.\n\nBeispiele:\n• 'Ich werde morgen Deutsch lernen.' (Werden + Infinitiv)\n• 'Morgen lerne ich Deutsch.' (Präsens mit Zeitangabe)",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "⏰",
            order = 4,
            quizCount = 0,  // 120 questions ÷ 10 per quiz = 12 sessions
            tips = listOf(
                "WERDEN + Infinititiv = Vorhersage, Vermutung über Zukunft",
                "Präsens + Zeitangabe = geplante, sichere Handlungen",
                "Werden auch für Höflichkeit: würde + Infinititiv",
                "Future Words: morgen, nächste Woche, bald, später",
                "Im B2-Exam: meistens wird für Zukunft verwendet"
            )
        ),
        // 5. Futur mit werden
        Subject(
            id = "b2_06",
            level = "B2",
            name = "5. Futur mit werden",
            nameShort = "Futur mit werden",
            description = "'Werden' ist das Hilfsverb für das deutsche Futur. Es wird sowohl für das Futur I als auch für das Futur II verwendet. 'Werden' kann auch für Vermutungen über die Gegenwart verwendet werden.\n\nBeispiele:\n• 'Es wird morgen regnen.' (Futur I - Vorhersage)\n• 'Du wirst die Prüfung bestanden haben.' (Futur II - Vermutung über Vergangenes)",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "⏰",
            order = 5,
            quizCount = 0,
            tips = listOf(
                "Futur I: wird + Partizip II + werden",
                "Futur II: wird + Partizip II + haben/sein + werden",
                "Vermutungen über Gegenwart: wird + Infinititiv + haben",
                "Futur II mit 'schon' = Vermutung dass etwas passiert ist",
                "Im B2-Exam: 'werden' oft für Vorhersagen und Vermutungen"
            )
        ),
        // 6. Angaben im Satz
        Subject(
            id = "b2_07",
            level = "B2",
            name = "6. Angaben im Satz",
            nameShort = "Angaben im Satz",
            description = "Angaben sind Satzglieder, die zusätzliche Informationen geben — sie antworten auf Fragen wie Wann? Wo? Warum? Wie? In German, Angaben follow the TEKAMO order when multiple ones are combined.\n\nTEKAMO — Four Main Types of Angaben:\n• TE (Temporal) — Wann? — morgen, gestern, oft\n• KA (Kausal) — Warum? — wegen des Wetters, deshalb\n• MO (Modal) — Wie? — schnell, leider, gern\n• LO (Lokal) — Wo/Wohin/Woher? — in Berlin, nach Hause\n\nSentence Position Rules (TEKAMO Order):\nWhen multiple Angaben appear together: TE → KA → MO → LO\nExample: Ich fahre morgen (TE) wegen der Arbeit (KA) mit dem Zug (MO) nach Munchen (LO).\n\nBeispiele:\n• 'Am Montag werde ich in Berlin einen Test schreiben.' (TE + LO)\n• 'Wegen der Krankheit konnte ich nicht kommen.' (KA only)\n• 'Sie hat gestern im Bro schnell gegessen.' (TE + LO + MO)",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📍",
            order = 6,
            quizCount = 0, // computed dynamically from JSON
            tips = listOf(
                "TEKAMO order: Temporal -> Kausal -> Modal -> Lokal",
                "Position 1: usually temporal information (Wann?)",
                "Position 2: Subject/Object",
                "Position 3+: other Angaben in TEKAMO order",
                "LO (Wo/Wohin/Woher) can also appear at the end of the sentence"
            )
        ),
        // 6. Verneinung mit nicht
        Subject(
            id = "b2_08",
            level = "B2",
            name = "7. Verneinung mit nicht",
            nameShort = "Nicht-Verneinung",
            description = "Die Verneinung mit 'nicht' kann sich auf verschiedene Satzglieder beziehen. Die Position von 'nicht' bestimmt, was verneint wird. Dies ist ein häufiger Fehler in der B2-Prüfung.\n\nBeispiele:\n• 'Ich spreche nicht Deutsch. (sondern Englisch)' - Verneinung des Verbs\n• 'Das ist nicht mein Buch. (sondern deins)' - Verneinung des Nominals",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "❌",
            order = 7,
            quizCount = 0,
            tips = listOf(
                "nicht + Verb = ganze Handlung verneint",
                "nicht + am Satzende = Negation des nächsten Satzglieds",
                "nicht bei Adjektiv = verneint das Adjektiv",
                "kein vs. nicht: kein = Verneinung von Nomen mit Artikel",
                "Satznegation: nicht am Ende | Wortnegation: nicht vor dem Wort"
            )
        ),
        // 7. Negationswörter
        Subject(
            id = "b2_09",
            level = "B2",
            name = "8. Negationswörter: nichts, nie/niemals, niemand, nirgends",
            nameShort = "Negationswörter",
            description = "Es gibt verschiedene Negationswörter im Deutschen, die verwendet werden, um die Verneinung zu verstärken oder zu spezifizieren. In der B2-Prüfung werden diese häufig in Lese- und Schreibaufgaben verwendet.\n\nBeispiele:\n• 'Niemand hat das verstanden.' (niemand = hiç kimse)\n• 'Ich habe ihn nirgends gefunden.' (nirgends = hiçbir yerde)\n• 'Niemals werde ich das tun!' (niemals = asla)",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "❌",
            order = 8,
            quizCount = 0,
            tips = listOf(
                "NIEMAND = no one / hiç kimse",
                "NIchts = nothing / hiçbir şey",
                "NIE/NIEMALS = never / asla",
                "NIRGENDS = nowhere / hiçbir yerde",
                "KEINER = no one / hiçbiri (Deklination wie Artikel)"
            )
        ),
        // 8. Passiv Präteritum
        Subject(
            id = "b2_10",
            level = "B2",
            name = "9. Passiv Präteritum",
            nameShort = "Passiv Präteritum",
            description = "Das Passiv Präteritum wird verwendet, um vergangene Handlungen zu beschreiben, bei denen der Handelnde unbekannt oder unwichtig ist. Es wird oft in formellen Texten und Berichten verwendet.\n\nBeispiele:\n• 'Das Problem wurde gelöst.' (Vorgangspassiv)\n• 'Die Tür war schon geöffnet.' (Zustandspassiv)",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "🔄",
            order = 9,
            quizCount = 0,
            tips = listOf(
                "Vorgangspassiv Präteritum: wurde + Partizip II",
                "Zustandspassiv: war + Partizip II",
                "Agent (von wem?): von + Dativ",
                "Wichtig: nicht alle Verben können Passiv bilden",
                "Passiv in Vergangenheit: wurde häufig in Berichten verwendet"
            )
        ),
        // 9. Konjunktiv II der Vergangenheit
        Subject(
            id = "b2_11",
            level = "B2",
            name = "10. Konjunktiv II der Vergangenheit",
            nameShort = "Konjunktiv II Vergangenheit",
            description = "🔹 1. Structure (Form)\n\nKonjunktiv II der Vergangenheit is formed as follows:\n\nhätte / wäre + Partizip II\n\nhätte → with most verbs (haben as auxiliary)\nwäre → with motion verbs and sein\n\n👉 Examples:\n• Ich hätte mehr gelernt. (If I had studied more.)\n• Er wäre früher gekommen. (If he had come earlier.)\n\n🔹 2. Areas of Use\n\n✅ a) Unrealised past situations\n• Ich hätte dich angerufen. (But I didn't call.)\n\n✅ b) Regret / criticism\n• Du hättest besser aufpassen sollen. (You should have been more careful.)\n\n✅ c) Conditional sentences (with wenn)\n• Wenn ich mehr Zeit gehabt hätte, wäre ich gekommen.\n\n🔹 3. Use with modal verbs\n\nWith modal verbs the structure is:\n\n👉 hätte + Infinitiv + Modalverb (Partizip II)\n\n• Ich hätte kommen müssen. (I should have come.)\n\n🔹 4. Important Notes\n\n• Unrealised past → not indicative!\n• Mostly used with wenn-clauses.\n• Alternative structures: ohne dass, anstatt dass.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "💭",
            order = 10,
            quizCount = 0,
            tips = listOf(
                "Irreale Bedingung: wenn + hätte/wäre + Partizip II",
                "Hätte-Form: hätte + Partizip II + gemacht",
                "Wäre-Form: wäre + Partizip II + gegangen",
                "Würde-Form: würde + Infinitiv + haben/sein (oft in gesprochener Sprache)",
                "Unterscheide: Konjunktiv II jetzt vs. damals"
            )
        ),
        // 10. Konjunktiv II mit Modalverben
        Subject(
            id = "b2_12",
            level = "B2",
            name = "11. Konjunktiv II mit Modalverben",
            nameShort = "Konjunktiv II Modalverben",
            description = "🔹 What is Konjunktiv II?\n\nKonjunktiv II is a grammatical mood in German used for assumptions, wishes, polite requests, unreal situations, and indirect speech. Its use with modal verbs (Modalverben) is particularly important at B2 level.\n\n🔹 Modalverb Forms in Konjunktiv II\n\n| Modalverb | Präteritum | Konjunktiv II |\n|-----------|-----------|---------------|| können | konnte | könnte || müssen | musste | müsste || dürfen | durfte | dürfte || sollen | sollte | sollte || wollen | wollte | wollte || mögen | mochte | möchte |\n\n⚠️ Note: sollen and wollen keep the same form as Präteritum in Konjunktiv II — context clarifies the meaning.\n\n🔹 Areas of Use\n\n✅ 1. Polite requests and suggestions:\n• Könntest du mir bitte helfen? (Could you please help me?)\n• Du solltest mehr schlafen. (You should sleep more.)\n\n✅ 2. Unreal / hypothetical situations:\n• Ich müsste eigentlich lernen. (I really should study.)\n• Er könnte die Prüfung bestehen, wenn er fleißiger wäre. (He could pass the exam if he were more diligent.)\n\n✅ 3. Probability / guess:\n• Das dürfte schwierig sein. (This is likely to be difficult.)\n• Es könnte regnen. (It could rain.)\n\n✅ 4. Indirect speech (indirekte Rede):\n• Er sagte, er müsse arbeiten. (He said he had to work.)\n\n✅ 5. Conditional sentences (Konditionalsatz):\n• Wenn ich Zeit hätte, könnte ich kommen. (If I had time, I could come.)\n\n🔹 Konjunktiv II Perfekt with Modalverben\n\nFor unreal past situations:\nStructure: hätte + Infinitiv + Modalverb\n\n• Ich hätte früher kommen können. (I could have come earlier.)\n• Du hättest das nicht tun sollen. (You shouldn't have done that.)\n• Er hätte mehr lernen müssen. (He should have studied more.)",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "💭",
            order = 11,
            quizCount = 0,
            tips = listOf(
                "Hätte + Infinitiv + Modalverb = Möglichkeit",
                "Würde + Infinitiv + Modalverb = höfliche Bitte",
                "Konjunktiv II von können: könnte",
                "Modalverben im Konjunktiv II: müssen → müsste, dürfen → dürfte",
                "In der B2-Prüfung: höfliche Bitten mit würde + Infinitiv"
            )
        ),
        // 13. Pronomen: einander
        Subject(
            id = "b2_13",
            level = "B2",
            name = "12. Pronomen: einander",
            nameShort = "einander",
            description = "🔹 What is 'Einander'?\n\n'einander' is a pronoun that expresses reciprocity (Reziprozität). It corresponds to 'birbirine' in Turkish and is used with verbs that express a mutual/reciprocal action.\n\n🔹 Basic Usage\n\n'einander' can be used alone or combined with prepositions (Präpositionen):\n\n| Form | Meaning | Example |\n|------|---------|---------|\n| einander | each other / birbirini | Sie lieben einander. |\n| miteinander | together / birlikte | Sie reden miteinander. |\n| voneinander | from each other / birbirinden | Sie lernen voneinander. |\n| füreinander | for each other / birbirleri için | Sie sorgen füreinander. |\n| aufeinander | onto each other / birbirine (üstüne) | Sie warten aufeinander. |\n| zueinander | towards each other / birbirine (doğru) | Sie sind nett zueinander. |\n| aneinander | onto each other / birbirine | Sie denken aneinander. |\n| übereinander | about each other / birbirinden (hakkında) | Sie sprechen übereinander. |\n| nebeneinander | next to each other / yan yana | Sie sitzen nebeneinander. |\n| nacheinander | one after another / birbiri ardına | Sie kommen nacheinander. |\n| gegeneinander | against each other / birbirine karşı | Sie kämpfen gegeneinander. |\n| durcheinander | mixed up / birbirine karışık | Alles ist durcheinander. |\n| hintereinander | one behind another / arka arkaya | Sie stehen hintereinander. |\n| ineinander | into each other / iç içe | Sie sind ineinander verliebt. |\n| untereinander | among themselves / kendi aralarında | Sie teilen es untereinander. |\n| beieinander | next to each other / birbirinin yanında | Sie sind beieinander. |\n\n🔹 Difference from 'sich'\n\nsich ... gegenseitig / sich\neinander\nSie helfen sich (gegenseitig).\nSie helfen einander.\nSie kennen sich.\nSie kennen einander.\n✅ Both are correct, but 'einander' is more formal and written. Both can appear in B2 exams.\n\n🔹 Important Notes\n\n• 'einander' is always written in lowercase.\n• When combined with a preposition it becomes one word: mit + einander = miteinander.\n• The subject must be at least two people or groups.\n• The verb is usually in the plural form.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "🔄",
            order = 12,
            quizCount = 0,
            tips = listOf(
                "EINANDER = sich gegenseitig / birbirine",
                "Nur für wechselseitige Handlungen!",
                "Kann mit allen Kasus verwendet werden: einander, einander, einander",
                "Synonym: sich (gegenseitig)",
                "Im B2-Exam: oft in Leseverstehen verwendet"
            )
        ),
        // 14. Weiterführende Nebensätze
        Subject(
            id = "b2_14",
            level = "B2",
            name = "13. Weiterführende Nebensätze",
            nameShort = "Weiterführende Nebensätze",
            description = "🔹 What are Weiterführende Nebensätze?\n\nWeiterführende Nebensätze (Devam Ettiren Yan Cümleler) expand, interpret, or conclude the content of the main clause. These subordinate clauses begin with 'was' or 'wo(r)-' + preposition and refer to the ENTIRE main clause — not just a single noun.\n\nEr hat die Prüfung bestanden, was uns sehr gefreut hat.\n→ 'was' = refers to the entire main clause content.\n\n🔹 Key Forms\n\n| Form | Function | Example |\n|------|---------|---------|\n| was | general reference (was mich freut, was bedeutet...) | Das ist wichtig, was ich gelernt habe. |\n| womit | mit + was (womit ich nicht einverstanden bin) | Das ist das Werkzeug, womit ich gearbeitet habe. |\n| worüber | über + was (worüber ich mich wundere) | Das Thema, worüber wir sprechen, ist interessant. |\n| woran / worauf / worin | an/auf/in + was — selected by context | Das ist das Thema, worauf wir uns konzentrieren. |\n| weswegen / weshalb | reason reference (neden/bu yüzden) | Das ist der Grund, weswegen ich gekommen bin. |\n| wodurch / wonach | durch/nach + was compound forms | Das ist die Methode, wodurch wir gelernt haben. |\n\n🔹 Important Rules\n\n• The verb goes at the END of the subordinate clause.\n• A comma is MANDATORY before the weiterführender Nebensatz.\n• 'was' does NOT refer to a noun — it refers to the entire preceding clause.\n• Contrary to regular Relativsätze (der/die/das), these have no antecedent noun.\n• They are typical in formal/written German and often appear in B2 reading texts.\n\n🔹 B2 Topic Summary — Konjunktionen und Verwendung\n\nWeiterführende Nebensätze (Devam Ettiren Yan Cümleler) describe, comment on, or draw a conclusion from the main clause situation. The key difference: these clauses refer to the ENTIRE previous sentence, not just one noun.\n\n🔹 Conjunctions and Their Uses\n\n| Conjunction | Explanation | Example |\n|------------|-------------|---------|\n| was | general reference | Er kam zu spät, was mich ärgerte. |\n| womit | mit + was | Sie hat alles erklärt, womit ich zufrieden bin. |\n| worüber | über + was | Er hat gelogen, worüber ich schockiert bin. |\n| worauf | auf + was | Sie hat gewonnen, worauf wir stolz sind. |\n| wofür | für + was | Er hat geholfen, wofür ich dankbar bin. |\n| wodurch | durch + was (reason/instrument) | Die Fabrik schloss, wodurch Jobs verloren gingen. |\n| weswegen | aus welchem Grund | Er fehlte, weswegen das Projekt scheiterte. |\n| wovor | vor + was (warning/fear) | Die Ärzte warnten, wovor er sich fürchtete. |\n\n🔹 Basic Rules\n\n• A comma is MANDATORY before the clause.\n• The verb goes to the END of the subordinate clause.\n• The choice between 'was' and 'wo(r)+Präposition' depends on the prepositional case required by the verb in the subordinate clause (sich freuen über → worüber, dankbar sein für → wofür).",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 13,
            quizCount = 0,
            tips = listOf(
                "Was + Präposition = wofür, worüber, womit...",
                "Wo + Präposition = wo, wohin, woher...",
                "Weiterführend = gibt neue, zusätzliche Information",
                "Normaler Relativsatz = eingeleitet mit der/die/das",
                "Im B2-Exam: 'was' oft in formellen Texten"
            )
        ),
        // 15. Präpositionen mit Genitiv
        Subject(
            id = "b2_15",
            level = "B2",
            name = "14. Präpositionen mit Genitiv",
            nameShort = "Genitiv-Präpositionen",
            description = "🔹 What are Präpositionen mit Genitiv?\n\nGerman genitive prepositions require nouns to be in the Genitive case. They are common in formal writing and B2 exams.\n\n🔹 Prepositions and Their Meanings\n\n| Preposition | Meaning (English) | Example |\n|------------|------------------|---------|\n| anstatt / statt | instead of | Statt des Regens kam die Sonne. |\n| aufgrund | because of / due to | Aufgrund des Lärms konnte ich nicht schlafen. |\n| außerhalb | outside (of) | Außerhalb der Stadt ist es ruhig. |\n| innerhalb | inside (of) / within | Innerhalb eines Jahres lernte er Deutsch. |\n| trotz | despite | Trotz des Verbots kamen viele Leute. |\n| während | during | Während des Unterrichts ist das Handy aus. |\n| wegen | because of / due to | Wegen des Unfalls gab es Stau. |\n| dank | thanks to | Dank seines Einsatzes gewannen wir. |\n| laut | according to | Laut des Berichts ist alles in Ordnung. |\n| mittels | by means of | Mittels eines Tricks öffnete er die Tür. |\n| mangels | for lack of | Mangels Beweisen wurde er freigesprochen. |\n| anlässlich | on the occasion of | Anlässlich seines Geburtstags gab es ein Fest. |\n| bezüglich | regarding / concerning | Bezüglich Ihrer Anfrage senden wir Unterlagen. |\n| hinsichtlich | with regard to | Hinsichtlich der Qualität gibt es keine Mängel. |\n| seitens | on the part of | Seitens der Firma gab es keine Einwände. |\n| unweit | not far from | Unweit des Bahnhofs steht ein Hotel. |\n| anhand | by means of / with the help of | Anhand der Daten wurde alles klar. |\n| infolge | as a result of | Infolge des Unfalls gab es Stau. |\n| angesichts | in view of / given | Angesichts der Lage mussten wir handeln. |\n| diesseits | on this side of | Diesseits des Flusses steht ein Bauernhof. |\n| jenseits | on the other side of | Jenseits der Grenze beginnt ein anderes Land. |\n\n🔹 Important Grammar Rules\n\n• All these prepositions GOVERN THE GENITIVE CASE.\n• Most are used in written/formal German.\n• In spoken German, some alternatives are preferred (e.g., 'wegen' can also be used with Dative in informal speech).\n• Watch the article contractions: trotz + des = trotz des, während + der = während der.\n\n🔹 B2 Exam Tips\n\n• These prepositions often appear in reading comprehension texts (formal articles, official letters).\n• In writing tasks, using genitive prepositions shows advanced grammar knowledge.\n• Remember: nouns after these prepositions ALWAYS get the genitive article (des, der, etc.).",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 14,
            quizCount = 0,
            tips = listOf(
                "Trotz, während, wegen, statt, anstatt, dank, angesichts",
                "Immer mit Artikel: trotz des/dem/die → trotz der (Nominativ/Dativ)",
                "Genitiv-Endungen: -es, -e, -s (oft bei Nomen)",
                "Bei Nomen: trotz des Wetters, während der Reise",
                "Im B2-Exam: diese Präpositionen oft in Schreibanforderungen"
            )
        ),
        // 16. je und desto/umso
        Subject(
            id = "b2_16",
            level = "B2",
            name = "15. je und desto/umso + Komparativ",
            nameShort = "Je und desto",
            description = "'Je... desto' oder 'je... umso' wird verwendet, um einen proportionalen Vergleich auszudrücken. Je mehr von A, desto mehr von B. Diese Struktur ist typisch für argumentative Texte.\n\nBeispiele:\n• 'Je mehr ich lerne, desto mehr weiß ich.'\n• 'Je länger die Wartezeit, umso unzufriedener werden die Kunden.'",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📊",
            order = 15,
            quizCount = 0,
            tips = listOf(
                "JE + Komparativ = desto/umso + Komparativ",
                "Je mehr, desto besser",
                "Je schneller, umso besser",
                "Nach JE: Verb am Ende!",
                "Im B2-Exam: oft in Statistik-Texten"
            )
        ),
        // 17. Nomen-Verb-Verbindungen
        Subject(
            id = "b2_17",
            level = "B2",
            name = "16. Nomen-Verb-Verbindungen",
            nameShort = "Nomen-Verb-Verbindungen",
            description = "📚 Nomen-Verb-Verbindungen (NVV) — B2 Topic Summary\n\nNomen-Verb-Verbindungen (noun-verb combinations) are fixed expressions in German where a specific noun is used together with a particular verb. These structures replace a single verb and are especially common in written and formal texts.\n\nBasic Concept:\nInstead of using a single verb, German often uses a noun + verb combination:\n• eine Entscheidung treffen = to decide (lit. 'to make a decision')\n• eine Frage stellen = to ask (lit. 'to place a question')\n• Kritik üben = to criticize (lit. 'to exercise criticism')\n• in Betracht ziehen = to consider (lit. 'to pull into consideration')\n• zur Verfugung stehen = to be available (lit. 'to stand at disposal')\n• Rucksicht nehmen auf = to consider / to take into account\n• einen Antrag stellen = to apply (lit. 'to place an application')\n• Einfluss nehmen auf = to influence (lit. 'to take influence on')\n• zum Ausdruck bringen = to express (lit. 'to bring to expression')\n• in Frage kommen = to be considered / to be possible (lit. 'to come into question')\n\nAdditional Common NVVs (Turkish to English):\n• einen Beitrag leisten = to contribute (lit. 'to perform a contribution')\n• eine Rolle spielen = to play a role (lit. 'to play a role')\n• in Kontakt treten = to get in contact (lit. 'to enter into contact')\n• Maßnahmen ergreifen = to take measures (lit. 'to seize measures')\n• einen Einfluss haben auf = to have an influence on\n• zur Sprache bringen = to bring up / to address (lit. 'to bring to language')\n• Fortschritte machen = to make progress\n• einen Termin vereinbaren = to make an appointment\n• unter Druck stehen = to be under pressure\n\nImportant Notes:\n• The noun usually appears without an article or with a definite article\n• The verb goes to the end of the sentence (German verb rule)\n• NVVs can be passivized: Eine Entscheidung wird getroffen\n• In the B2 exam, questions usually test correct verb selection or matching\n\nCommon Verb Patterns in NVVs:\n• treffen: eine Entscheidung treffen\n• stellen: eine Frage stellen, einen Antrag stellen\n• machen: Eindruck machen, Fortschritte machen\n• nehmen: Einfluss nehmen, Rucksicht nehmen\n• uben: Kritik uben\n• bringen: zum Ausdruck bringen, zur Sprache bringen\n• stehen: zur Verfugung stehen, unter Druck stehen\n• tragen: Sorge tragen, Verantwortung tragen\n• aufnehmen: Kontakt aufnehmen\n• ziehen: in Betracht ziehen\n• kommen: in Frage kommen, in Kontakt treten\n• halten: eine Rede halten\n• uebernnehmen: Verantwortung uebernnehmen\n• erreichen: einen Kompromiss erreichen\n• finden: einen Kompromiss finden\n• ergriffen: das Wort ergreifen\n• treten: in Kraft treten\n• leisten: einen Beitrag leisten, Gesellschaft leisten\n• spielen: eine Rolle spielen\n• ergreifen: Maßnahmen ergreifen\n• vereinbaren: einen Termin vereinbaren\n\nWhy does it matter?\nIn B2 reading and writing tasks, NVVs appear frequently in formal texts such as newspaper articles, official letters, and academic texts. Using the correct NVV instead of a simple verb shows advanced proficiency and helps you sound more natural, like a native speaker.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 16,
            quizCount = 0,
            tips = listOf(
                "eine Entscheidung treffen ≠ eine Entscheidung machen (treffen is correct!)",
                "eine Frage stellen ≠ eine Frage machen (stellen is correct!)",
                "Einfluss nehmen auf (+Akkusativ) — NOT 'Einfluss machen'!",
                "Rücksicht nehmen auf (+Akkusativ)",
                "Kritik üben an (+Dativ)",
                "in Kraft treten | in Betracht ziehen | in Frage kommen",
                "NVVs can be passivized: Eine Entscheidung wird getroffen",
                "B2 exam: usually tests correct verb selection or matching"
            )
        ),
        // 18. Folgen ausdrücken
        Subject(
            id = "b2_18",
            level = "B2",
            name = "17. Folgen ausdrücken: folglich, infolgedessen, deshalb, sodass",
            nameShort = "Folgen ausdrücken",
            description = "📚 'Folgen ausdrücken' (Expressing Consequences / Sonuç İfade Etme) is an important grammar and expression skill at B2 level. It covers various structures used to express the result of an action, situation, or event.\n\n🔑 Key Structures\n\n• deshalb / daher / darum → cause → consequence (Hauptsatz)\n  Example: 'Es regnete, deshalb blieben wir zu Hause.'\n\n• also → consequence / logical conclusion\n  Example: 'Du hast Fieber, also musst du zum Arzt.'\n\n• deswegen → therefore / bu yüzden (Hauptsatz)\n  Example: 'Sie hat nicht geschlafen, deswegen ist sie müde.'\n\n• infolgedessen → consequently / bunun sonucu olarak (formal, written)\n  Example: 'Die Fabrik schloss, infolgedessen verloren viele ihren Job.'\n\n• folglich → consequently / dolayısıyla (formal/written)\n  Example: 'Er kam zu spät, folglich verpasste er den Zug.'\n\n• sodass / so … dass → so that / öyle ki (Nebensatz — verb at the end)\n  Example: 'Er arbeitete so viel, dass er krank wurde.'\n\n• somit → thus / bu suretle (formal)\n  Example: 'Das Projekt ist beendet, somit können wir pausieren.'\n\n• demnach → accordingly / buna göre\n  Example: 'Die Studie zeigt X, demnach ist Y richtig.'\n\n🔍 Important Distinctions\n\n• deshalb / daher / darum / deswegen → very similar in meaning, used in Hauptsatz, verb in position 2\n• sodass → Nebensatz conjunction, verb goes to the end\n• so … dass → Degree + Result: 'Er sprach so leise, dass niemand ihn hörte.'\n• folglich / infolgedessen / somit / demnach → used in more formal/academic texts",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 17,
            quizCount = 0,
            tips = listOf(
                "DESHALB/DESWEGEN/DARUM = therefore / therefore (Position 2)",
                "FOLGLICH = consequently / consequently (Position 1 or 2)",
                "INFOLGEDESSEN = consequently / as a result (postpositioned)",
                "SODASS = so that / so that (Purpose/Effect, Verb at the end)",
                "In the B2 Exam: these show logical argumentation"
            )
        ),
        // 19. Ausdrücke mit Präpositionen
        Subject(
            id = "b2_19",
            level = "B2",
            name = "18. Ausdrücke mit Präpositionen",
            nameShort = "Präposition-Ausdrücke",
            description = "📚 'Ausdrücke mit Präpositionen' (Expressions with Prepositions / Edatlı Fiiller) covers fixed prepositions used with verbs, adjectives, and nouns at B2 level.\n\n🔷 1. Verbs with Prepositions (Fiil + Edat)\n\n• warten auf + Akkusativ = to wait for\n  Example: 'Ich warte auf den Bus.'\n\n• sich freuen auf / über + Akkusativ = to look forward to\n  Example: 'Ich freue mich auf die Ferien.' / 'über das Geschenk'\n\n• denken an + Akkusativ = to think of\n  Example: 'Ich denke an dich.'\n\n• sich erinnern an + Akkusativ = to remember\n  Example: 'Er erinnert sich an seine Kindheit.'\n\n• sich beschäftigen mit + Dativ = to deal with\n  Example: 'Sie beschäftigt sich mit Musik.'\n\n• sprechen über / von + Akkusativ / Dativ = to talk about\n  Example: 'Wir sprechen über das Problem.'\n\n• bitten um + Akkusativ = to ask for\n  Example: 'Er bittet um Hilfe.'\n\n• sich bewerben um / bei + Akkusativ / Dativ = to apply for\n  Example: 'Sie bewirbt sich um die Stelle bei einer Firma.'\n\n• gehören zu + Dativ = to belong to\n  Example: 'Das gehört zu meinen Aufgaben.'\n\n• leiden an / unter + Dativ = to suffer from\n  Example: 'Er leidet an einer Krankheit.' / 'unter dem Lärm'\n\n• sich interessieren für + Akkusativ = to be interested in\n  Example: 'Ich interessiere mich für Kunst.'\n\n• zweifeln an + Dativ = to doubt\n  Example: 'Sie zweifelt an seiner Ehrlichkeit.'\n\n• bestehen aus / auf + Dativ = to consist of / to insist on\n  Example: 'Das Gerät besteht aus Metall.' / 'Er besteht auf seiner Meinung.'\n\n• abhängen von + Dativ = to depend on\n  Example: 'Es hängt von dir ab.'\n\n🔷 2. Adjectives with Prepositions (Sıfat + Edat)\n\n• zufrieden mit = satisfied with\n• begeistert von / für = enthusiastic about\n• verantwortlich für = responsible for\n• neidisch auf = jealous of\n• stolz auf = proud of\n• neugierig auf = curious about\n• angewiesen auf = dependent on\n• gewöhnt an = accustomed to\n• überzeugt von = convinced of\n• enttäuscht von / über = disappointed with\n\n🔷 3. Nouns with Prepositions (İsim + Edat)\n\n• die Angst vor = fear of\n• die Lust auf = desire for\n• das Interesse an / für = interest in\n• die Hoffnung auf = hope for\n• die Freude über / an = joy over / in\n\n🔷 4. Pronominaladverbien (da(r)- / wo(r)-)\n\nWhen a preposition refers to a thing (not a person), use a pronominal adverb:\n• 'Ich warte auf den Bus.' → 'Ich warte darauf.'\n• 'Wofür interessierst du dich?' → 'Dafür interessiere ich mich sehr.'\n\nNote: Use 'worüber', 'worauf', etc. when asking about things, not people.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 18,
            quizCount = 0,
            tips = listOf(
                "warten auf + Akk = to wait for",
                "sich freuen auf/über + Akk = to look forward to",
                "sich erinnern an + Akk = to remember",
                "sich beschäftigen mit + Dat = to deal with",
                "sprechen über/von + Akk/Dat = to talk about",
                "bitten um + Akk = to ask for",
                "leiden an/unter + Dat = to suffer from",
                "zufrieden mit + Dat = satisfied with",
                "stolz auf + Akk = proud of",
                "Antwort: da(r)- / wo(r)- pronouns for things not people"
            )
        ),
        // 20. irreale Konditionalsätze in der Vergangenheit
        Subject(
            id = "b2_20",
            level = "B2",
            name = "19. irreale Konditionalsätze in der Vergangenheit",
            nameShort = "Irreale Konditionalsätze",
            description = "📚 'Irreale Konditionalsätze' (Unreal Conditional Sentences / gerçek olmayan koşul cümleleri) express conditions that did not happen or are highly unlikely to happen. They use Konjunktiv II in two time frames.\n\n1️⃣ Konjunktiv II – Gegenwart/Zukunft (Present/Future)\nUsed for hypothetical or imaginary situations.\nStructure:\nWenn + Konjunktiv II, ... Konjunktiv II\nKonjunktiv II = würde + Infinitiv OR strong verb forms (wäre, hätte, könnte, müsste)\n\nExamples:\n• 'Wenn ich Zeit hätte, würde ich kommen.' (If I had time, I would come)\n• 'Wenn er reich wäre, kaufte er ein Haus.' (If he were rich, he would buy a house)\n\n2️⃣ Konjunktiv II – Vergangenheit (Past)\nUsed for events that did not happen in the past.\nStructure:\nWenn + hätte/wäre + Partizip II, ... hätte/wäre + Partizip II\n\nExamples:\n• 'Wenn ich mehr gelernt hätte, hätte ich die Prüfung bestanden.' (If I had studied more, I would have passed)\n• 'Wenn sie früher gekommen wäre, wäre sie dabei gewesen.' (If she had come earlier, she would have been there)\n\n3️⃣ Verkürzte Konditionalsätze (Elliptical Conditionals — without wenn)\nWhen wenn is omitted, the verb moves to position 1:\n• 'Wäre ich reich, würde ich reisen.' (Were I rich, I would travel)\n• 'Hätte er gelernt, hätte er bestanden.' (Had he studied, he would have passed)\n\n⚠️ B2 Important Points\n• würde + Infinitiv can be replaced by direct Konjunktiv II forms (käme, ginge, wäre)\n• Do not mix past and present time frames\n• Recognize both wenn-clause and wenn-less structures",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "💭",
            order = 19,
            quizCount = 0,
            tips = listOf(
                "Present/Future: würde + Infinitiv OR strong verb Konjunktiv II (wäre, hätte, könnte)",
                "Past: Wenn + hätte/wäre + Partizip II → hätte/wäre + Partizip II",
                "Hätte ich... = Wäre ich... → inversion allowed (no wenn needed)",
                "if + past participle = if + had + past participle → past unreal",
                "B2 Exam: watch for Konjunktiv II in reading and writing tasks"
            )
        ),
        // 21. Relativsätze im Genitiv
        Subject(
            id = "b2_21",
            level = "B2",
            name = "20. Relativsätze im Genitiv",
            nameShort = "Relativsätze Genitiv",
            description = "📚 'Relativsätze im Genitiv' (Relative Clauses in Genitive / Belirteç Cümlelerinde Genitif) are used to express possession or belonging. They refer to a noun in the main clause (Bezugswort) and give additional information about who owns something or how something relates.\n\n📋 Relativpronomen im Genitiv — Overview\n\n• Maskulinum → dessen\n  Example: 'Der Mann, dessen Auto kaputt ist, ...' (The man whose car is broken)\n\n• Femininum → deren\n  Example: 'Die Frau, deren Buch ich lese, ...' (The woman whose book I am reading)\n\n• Neutrum → dessen\n  Example: 'Das Kind, dessen Spielzeug fehlt, ...' (The child whose toy is missing)\n\n• Plural → deren\n  Example: 'Die Leute, deren Hunde bellen, ...' (The people whose dogs are barking)\n\n🔸 When to Use Relativsätze im Genitiv\n\n• Expressing possession/belonging:\n  'Das Auto des Mannes steht vor der Tür.' → 'Der Mann, dessen Auto vor der Tür steht, ...'\n\n• Reformulating with possessive articles:\n  'Seine Eltern kommen aus der Türkei.' → 'Fatih Akin, dessen Eltern aus der Türkei kommen, ...'\n\n• After prepositions with Genitiv reference:\n  'Erika, in deren Schwester Max verliebt ist, ...' (verliebt sein in + Akkusativ, but 'deren' shows Genitive belonging)\n\n⚠️ Important for B2 Exams:\n• dessen/deren never changes — always stays in Genitiv regardless of the following noun's case\n• Relativsatz is a Nebensatz → conjugated verb goes to the end\n• After prepositions: preposition + Relativpronomen: 'von dessen', 'in deren', 'mit deren'",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 20,
            quizCount = 0,
            tips = listOf(
                "DESSEN = whose (maskulin/neutral) — for men, objects",
                "DEREN = whose (feminin/plural) — for women, groups",
                "dessen/deren stays in Genitiv regardless of following noun's case",
                "Verb goes to the end (Nebensatz)",
                "After prepositions: von dessen, in deren, mit deren"
            )
        ),
        // 22. Konjunktiv I in der indirekten Rede
        Subject(
            id = "b2_22",
            level = "B2",
            name = "21. Konjunktiv I in der indirekten Rede",
            nameShort = "Konjunktiv I",
            description = "📚 'Konjunktiv I in der indirekten Rede' (Conjunctive I in Indirect Speech / Dolaylı Anlatıda Konjunktiv I) is used to report what someone else said, especially in written language (news, official reports, interviews).\n\n🔧 How to Form Konjunktiv I\nRule: Infinitive stem + Konjunktiv I endings\n\n• ich -e → ich komme, ich habe\n• du -est → du kommest, du habest\n• er/sie/es -e → er komme, er habe\n• wir -en → wir kommen, wir haben\n• ihr -et → ihr kommet, ihr habet\n• sie/Sie -en → sie kommen, sie haben\n\n⚠️ Important: If er/sie/es looks the same as Präsens → use Konjunktiv II or würde + Infinitiv instead.\n\n🔄 Conversion Rules (Direkt → Indirekt)\n\n• 'Er sagt: Ich bin krank.' → 'Er sagt, er sei krank.'\n• 'Sie sagt: Ich habe keine Zeit.' → 'Sie sagt, sie habe keine Zeit.'\n• 'Er sagt: Wir kommen morgen.' → 'Er sagt, sie kämen morgen.' (Konj. II because Konj. I = Präsens)\n\n⏰ Tense Conversions:\n• Präsens → Konjunktiv I Präsens\n• Perfekt / Präteritum → Konjunktiv I Perfekt (habe/sei + Partizip II)\n• Futur → werde + Infinitiv\n\n🔄 Pronoun & Time Conversions:\n• ich / hier → er / dort\n• heute → an dem Tag\n• jetzt → damals / in dem Moment\n\n📰 Where It Is Used:\n• News articles: 'Der Minister erklärte, die Lage sei stabil.'\n• Official reports and academic writing\n• Interview reporting",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "💭",
            order = 21,
            quizCount = 0,
            tips = listOf(
                "Konjunktiv I: ich komme → er komme, ich habe → er habe",
                "sein → ich sei, du seist, er sei",
                "werden → ich werde, er werde",
                "haben → ich habe, du habest, er habe",
                "If er/sie/es = Präsens → use Konjunktiv II instead"
            )
        ),
        // 23. Konjunktiv II in irrealen Vergleichsätzen
        Subject(
            id = "b2_23",
            level = "B2",
            name = "22. Konjunktiv II in irrealen Vergleichsätzen",
            nameShort = "Irreale Vergleiche",
            description = "📚 'Konjunktiv II in irrealen Vergleichssaetzen' (Unreal Comparative Clauses / Gercek disi karsilastirma cumleleri) are used to compare a situation with something that is not real or hypothetical.\n\n🔗 Conjunctions\n\n• als ob + Nebensatz → as if / sanki (verb at end)\n  Example: 'Er tut so, als ob er alles wuesste.' (He acts as if he knew everything)\n\n• als wenn + Nebensatz → as if / sanki (same meaning as als ob, verb at end)\n  Example: 'Sie spricht, als wenn sie Deutscher waere.'\n\n• als + direct (no Nebensatz) → verb immediately after als\n  Example: 'Er tut so, als wuesste er alles.' (same meaning, different structure)\n\n• wie wenn + Nebensatz → as if / nasil ki (similar to als ob)\n\n📐 Structure Rules\n\n• als ob / als wenn / wie wenn → verb goes to the END (Nebensatz)\n• als (alone) → verb immediately after als (no Nebensatz)\n\n⏰ Konjunktiv II Tense Usage\n\n• Gegenwart (Present comparison):\n  'Sie sieht aus, als ob sie krank waere.' (She looks as if she were sick)\n\n• Vergangenheit (Past comparison — Konjunktiv II Perfekt):\n  'Er spricht, als ob er das selbst erlebt haette.' (He speaks as if he had experienced it himself)\n\n🔧 Konjunktiv II Formation (Summary)\n\n• sein → waere, haettest, haette, haetten\n• haben → haette, haettest, haette\n• werden → wuerde, wuerdest, wuerde\n• wissen → wuesste, wuesstest, wuesste\n• koennen → koennte, koenntest, koennte\n• muessen → muesste, muesstest, muesste\n• gehen → ginge / wuerde gehen\n• kommen → kaeme / wuerde kommen",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "💭",
            order = 22,
            quizCount = 0,
            tips = listOf(
                "als ob / als wenn = as if / sanki (Nebensatz: verb at end)",
                "als (alone) = as if / sanki (verb directly after als)",
                "Gegenwart: Konjunktiv II (waere, haette, koennte)",
                "Vergangenheit: Konjunktiv II Perfekt (haette + Partizip II)",
                "B2 Exam: descriptive texts and comparisons"
            )
        )
    )

    private fun getB1Subjects(): List<Subject> = listOf(
        Subject(
            id = "b1_01",
            level = "B1",
            name = "1. Nebensätze (dass, ob, weil, obwohl, damit, bevor, als, wenn)",
            nameShort = "Nebensätze",
            description = "Nebensätze mit: dass (dass), ob (ob), weil (weil), obwohl (obwohl), damit (damit), bevor (bevor), als (als), wenn (wenn), falls (falls), nachdem (nachdem), seitdem (seitdem), solange (solange), während (während). Das Verb steht am Ende des Nebensatzes.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 1,
            quizCount = 0
        ),
        Subject(
            id = "b1_02",
            level = "B1",
            name = "2. Konjunktiv II (wäre, hätte, würde, könnte, müsste)",
            nameShort = "Konjunktiv II",
            description = "Konjunktiv II wird für Hypothesen, Wünsche, höfliche Bitten und irreale Situationen verwendet. Wichtigste Formen: wäre, hätte, würde, könnte, müsste, dürfte, müsste, sollte.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 2,
            quizCount = 0
        ),
        Subject(
            id = "b1_03",
            level = "B1",
            name = "3. Passiv (wird gemacht, wurde gemacht, ist gemacht worden)",
            nameShort = "Passiv",
            description = "Das Passiv wird verwendet, wenn die Handlung wichtiger ist als der Handelnde. Bildung: werden + Partizip II. Zeitformen: Präsens, Präteritum, Perfekt, Plusquamperfekt.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 3,
            quizCount = 0
        ),
        Subject(
            id = "b1_04",
            level = "B1",
            name = "4. Modalverben im Konjunktiv II (könnte, müsste, würde, dürfte)",
            nameShort = "Modalverben KII",
            description = "Modalverben im Konjunktiv II: könnte (could), müsste (must), würde (would), dürfte (might), sollte (should). Verwendung für höfliche Bitten, Hypothesen und indirekte Rede.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 4,
            quizCount = 0
        ),
        Subject(
            id = "b1_05",
            level = "B1",
            name = "5. Nominalisierung (machen → die Durchführung)",
            nameShort = "Nominalisierung",
            description = "Nominalisierung: Verben und Adjektive werden zu Nomen umgewandelt. Struktur: das + Verb-Stamm + -ung oder das + Adjektiv + -heit/-keit. Wichtig für den schriftlichen Ausdruck.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 5,
            quizCount = 0
        ),
        Subject(
            id = "b1_06",
            level = "B1",
            name = "6. Relativsätze im Genitiv (deren, dessen, denen)",
            nameShort = "Relativsätze Genitiv",
            description = "Relativsätze im Genitiv: dessen (maskulin/neutral) und deren (feminin/plural) zeigen den Genitiv an. Sie werden verwendet, um Besitz oder Zugehörigkeit auszudrücken.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 6,
            quizCount = 0
        ),
        Subject(
            id = "b1_07",
            level = "B1",
            name = "7. Konnektoren (deshalb, trotzdem, allerdings, moreover, however)",
            nameShort = "Konnektoren",
            description = "Konnektoren für Argumentation und Textverknüpfung: deshalb (deshalb), trotzdem (trotzdem), allerdings (allerdings), außerdem (außerdem), furthermore (darüber hinaus), jedoch (jedoch).",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 7,
            quizCount = 0
        ),
        Subject(
            id = "b1_08",
            level = "B1",
            name = "8. Perfekt und Präteritum (对比和使用场景)",
            nameShort = "Perfekt vs Präteritum",
            description = "Unterschied zwischen Perfekt und Präteritum: Perfekt wird im Alltag und in der gesprochenen Sprache verwendet. Präteritum wird in der Schriftsprache, in Nachrichten und in formellen Texten verwendet.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 8,
            quizCount = 0
        ),
        Subject(
            id = "b1_09",
            level = "B1",
            name = "9. Verben mit festen Präpositionen (sich erinnern an, bestehen aus, abhängen von)",
            nameShort = "Feste Präpositionen",
            description = "Verben mit festen Präpositionen: sich erinnern an (+A), bestehen aus (+D), abhängen von (+D), leiden unter (+D), profitieren von (+D), sprechen über (+A), denken an (+A).",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 9,
            quizCount = 0
        ),
        Subject(
            id = "b1_10",
            level = "B1",
            name = "10. Partizip I und II als Adjektiv (lesend, gelesen, kommend, gekommen)",
            nameShort = "Partizipien",
            description = "Partizip I und II als Adjektive: Partizip I (-end) zeigt eine dauernde Handlung. Partizip II (-t/-en) zeigt eine abgeschlossene Handlung oder passiven Zustand. Verwendung als Adjektiv vor Nomen.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 10,
            quizCount = 0
        )
    )

    private fun getA2Subjects(): List<Subject> = listOf(
        Subject(
            id = "a2_01",
            level = "A2",
            name = "1. Präteritum (war, hatte, machte)",
            nameShort = "Präteritum",
            description = "Das Präteritum wird hauptsächlich in der geschriebenen Sprache und in formellen Situationen verwendet. Die wichtigsten Verben sind sein, haben und die Modalverben. Im Alltag wird es weniger häufig benutzt.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 1,
            quizCount = 0
        ),
        Subject(
            id = "a2_02",
            level = "A2",
            name = "2. Perfekt (haben/sein + Partizip II)",
            nameShort = "Perfekt",
            description = "Das Perfekt ist die wichtigste Vergangenheitsform im Alltag. Verwendung: haben oder sein als Hilfsverb + Partizip II. Die meisten Verben benutzen haben, nur Bewegungsverben und sein/werden benutzen sein.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 2,
            quizCount = 0
        ),
        Subject(
            id = "a2_03",
            level = "A2",
            name = "3. Verben mit Präpositionen (AC)",
            nameShort = "Verben + Präpositionen",
            description = "Bestimmte Verben erfordern bestimmte Präpositionen im Akkusativ oder Dativ: denken an (+A), warten auf (+A), sprechen über (+A), helfen bei (+D), sich freuen über (+A).",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 3,
            quizCount = 0
        ),
        Subject(
            id = "a2_04",
            level = "A2",
            name = "4. Wechselpräpositionen (in, auf, an, über, unter, vor, zwischen, hinter)",
            nameShort = "Wechselpräpositionen",
            description = "Wechselpräpositionen wechseln zwischen Akkusativ (Richtung) und Dativ (Ort): in, auf, an, über, unter, vor, zwischen, hinter. Akkusativ = wohin? Dativ = wo?",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 4,
            quizCount = 0
        ),
        Subject(
            id = "a2_05",
            level = "A2",
            name = "5. Nebensätze (dass, ob, weil, wenn, als)",
            nameShort = "Nebensätze",
            description = "Nebensätze sind von Sätzen eingeleitet durch: dass (dass), ob (ob), weil (weil), wenn (wenn), als (als), bevor (bevor), damit (damit), obwohl (obwohl). Das Verb steht am Satzende.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 5,
            quizCount = 0
        ),
        Subject(
            id = "a2_06",
            level = "A2",
            name = "6. Reflexive Verben (sich freuen, sich erinnern, sich befinden)",
            nameShort = "Reflexive Verben",
            description = "Reflexive Verben: sich freuen über (+A), sich erinnern an (+A), sich befinden in (+D), sich ärgern über (+A), sich interessieren für (+A). Das Reflexivpronomen richtet sich nach der Person und Kasus.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 6,
            quizCount = 0
        ),
        Subject(
            id = "a2_07",
            level = "A2",
            name = "7. Imperativ (Mach! Mach! Machen Sie!)",
            nameShort = "Imperativ",
            description = "Der Imperativ wird verwendet um Anweisungen zu geben: du-Form (Mach!), ihr-Form (Macht!), Sie-Form (Machen Sie!). Der Imperativ wird vor allem in informellen und formellen Kontexten verwendet.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 7,
            quizCount = 0
        ),
        Subject(
            id = "a2_08",
            level = "A2",
            name = "8. Plusquamperfekt (hatte gemacht, war gegangen)",
            nameShort = "Plusquamperfekt",
            description = "Das Plusquamperfekt beschreibt Handlungen, die vor einer anderen vergangenen Handlung stattfanden. Struktur: hatte/war + Partizip II. Es wird oft mit Präteritum oder Perfekt verwendet.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 8,
            quizCount = 0
        ),
        Subject(
            id = "a2_09",
            level = "A2",
            name = "9. Relativsätze (der, die, das, wo, wer, was)",
            nameShort = "Relativsätze",
            description = "Relativsätze werden mit der/die/das eingeleitet und geben zusätzliche Informationen über ein Nomen. Das Verb steht am Ende des Relativsatzes. Die Relativpronomen richten sich nach dem Kasus des Verbs.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 9,
            quizCount = 0
        ),
        Subject(
            id = "a2_10",
            level = "A2",
            name = "10. Konjunktionen (und, aber, oder, denn, sondern, deshalb, trotzdem)",
            nameShort = "Konjunktionen",
            description = "Die wichtigsten Konjunktionen: und (und), aber (aber), oder (oder), denn (denn), sondern (sondern), deshalb (deshalb), trotzdem (trotzdem), daher (daher), außerdem (außerdem).",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 10,
            quizCount = 0
        )
    )

    private fun getA1Subjects(): List<Subject> = listOf(
        // 1. Verben konjugieren (sein, haben, werden)
        Subject(
            id = "a1_01",
            level = "A1",
            name = "1. Verben konjugieren (sein, haben, werden)",
            nameShort = "Verben konjugieren",
            description = "Im A1-Level lernst du die wichtigsten Verben im Präsens zu konjugieren: sein, haben und werden. Diese Verben werden im Alltag sehr häufig verwendet.

SEIN (to be): ich bin, du bist, er/sie/es ist, wir sind, ihr seid, sie sind
HABEN (to have): ich habe, du hast, er hat, wir haben, ihr habt, sie haben
WERDEN (to become): ich werde, du wirst, er wird, wir werden, ihr werdet, sie werden

Diese drei Verben sind die Basis für fast alle deutschen Sätze.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 1,
            quizCount = 5,
            tips = listOf(
                "SEIN: ich bin, du bist, er ist, wir sind, ihr seid, sie sind",
                "HABEN: ich habe, du hast, er hat, wir haben, ihr habt, sie haben",
                "WERDEN: ich werde, du wirst, er wird, wir werden, ihr werdet, sie werden",
                "SEIN und HABEN sind unregelmäßig — auswendig lernen!",
                "In Perfekt: sein-Haben + Partizip II",
                "Frage: Was hast du gemacht? (What did you do?)"
            )
        ),
        // 2. Nomen und Artikel
        Subject(
            id = "a1_02",
            level = "A1",
            name = "2. Nomen und Artikel",
            nameShort = "Nomen und Artikel",
            description = "Lerne die Artikel (der, die, das) und die Pluralformen der Nomen im Deutschen.

DER (maskulin): der Mann, der Tisch, der Hund
DIE (feminin): die Frau, die Katze, die Schule
DAS (sächlich): das Buch, das Kind, das Auto

Pluralformen: der Mann → die Männer, das Kind → die Kinder, das Buch → die Bücher",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 2,
            quizCount = 5,
            tips = listOf(
                "DER = maskulin (der Mann), DIE = feminin (die Frau), DAS = sächlich (das Kind)",
                "Plural: -e, -er, -en, -s: das Buch → die Bücher, der Tisch → die Tische",
                "Unbestimmter Artikel: ein, eine, ein (a/an)",
                "Bestimmter Artikel: der, die, das (the)",
                "Lerne Nomen MIT Artikel: das Buch, nicht nur Buch",
                "Farben: rot, blau, grün, gelb, schwarz, weiß — immer kleingeschrieben"
            )
        ),
        // 3. Präsens (Gegenwart)
        Subject(
            id = "a1_03",
            level = "A1",
            name = "3. Präsens (Gegenwart)",
            nameShort = "Präsens",
            description = "Das Präsens beschreibt Handlungen in der Gegenwart. Regelmäßige und unregelmäßige Verben im Präsens.

REGELMÄSSIG (regular): arbeiten → ich arbeite, du arbeitest, er arbeitet
UNREGELMÄSSIG (irregular): lesen → ich lese, du liest, er liest; fahren → ich fahre, du fährst, er fährt

Wichtige unregelmäßige Verben: lesen, fahren, schlafen, nehmen, sehen, wissen",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 3,
            quizCount = 5,
            tips = listOf(
                "Regelmäßige Verben: -e, -st, -t, -en, -t, -en",
                "Unregelmäßige Verben: Vokalwechsel (a→ä, e→i, e→ie)",
                "lesen: ich lese, du liest, er liest (e→i)",
                "fahren: ich fahre, du fährst, er fährt (a→ä)",
                "sprechen: ich spreche, du sprichst, er spricht (e→i)",
                "Im A1 wichtig: Präsens für Alltag, Pläne und Gewohnheiten"
            )
        ),
        // 4. Akkusativ (Wen-Fall)
        Subject(
            id = "a1_04",
            level = "A1",
            name = "4. Akkusativ (Wen-Fall)",
            nameShort = "Akkusativ",
            description = "Der Akkusativ beschreibt die direkten Objects einer Handlung. Lerne die Akkusativformen der Artikel.

BESTIMMT (the): der → den, die → die, das → das, den → den
UNBESTIMMT (a): ein → einen, eine → eine, ein → ein

Verben mit Akkusativ: sehen, hören, kennen, lesen, machen, nehmen

Beispiele: Ich sehe den Mann. (I see the man.) Du liest das Buch. (You read the book.)",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 4,
            quizCount = 5,
            tips = listOf(
                "BESTIMMT: der → den, die → die, das → das, die (Plural) → die",
                "UNBESTIMMT: ein → einen, eine → eine, ein → ein",
                "WANN? Frage: Wen? oder Was? → Akkusativ",
                "Typische Verben: sehen, hören, kennen, lesen, machen, nehmen, brauchen",
                "Wechselpräpositionen brauchen auch Akkusativ (wohin?): in das Haus → ins Haus",
                "Maskulin und Neutrum ändern sich im Akkusativ: der → den, das → das"
            )
        ),
        // 5. Dativ (Wem-Fall)
        Subject(
            id = "a1_05",
            level = "A1",
            name = "5. Dativ (Wem-Fall)",
            nameShort = "Dativ",
            description = "Der Dativ beschreibt die indirekten Objects einer Handlung. Lerne die Dativformen der Artikel.

BESTIMMT: der → dem, die → der, das → dem, die (Plural) → den
UNBESTIMMT: ein → einem, eine → einer, ein → einem

Verben mit Dativ: helfen, danken, geben, zeigen, erklären, antworten

Beispiele: Ich helfe dem Mann. (I help the man.) Sie gibt dem Kind das Buch. (She gives the book to the child.)",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 5,
            quizCount = 5,
            tips = listOf(
                "BESTIMMT: der → dem, die → der, das → dem, die (Plural) → den",
                "UNBESTIMMT: ein → einem, eine → einer, ein → einem",
                "WANN? Frage: Wem? → Dativ",
                "Typische Verben: helfen (+D), danken (+D), geben (+D +A), zeigen (+D +A)",
                "Dativ steht oft nach Präpositionen: aus, bei, mit, nach, von, zu",
                "Plural Dativ: immer -n am Ende: den Männern, den Kindern, den Büchern"
            )
        ),
        // 6. Präpositionen
        Subject(
            id = "a1_06",
            level = "A1",
            name = "6. Präpositionen",
            nameShort = "Präpositionen",
            description = "Lerne die wichtigsten Präpositionen (in, auf, an, mit, nach, aus, von, zu, bei, für, gegen, um) und ihre Kasus.

FESTE PRÄPOSITIONEN:
• Akkusativ: für, gegen, um, durch, ohne, bis
• Dativ: aus, bei, mit, nach, seit, von, zu
• Wechsel: in, auf, an, über, vor, zwischen, hinter, unter

Beispiele: Ich gehe in die Schule. (wohin → Akkusativ) Ich bin in der Schule. (wo → Dativ)",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 6,
            quizCount = 5,
            tips = listOf(
                "AKKUSATIV fest: für, gegen, um, durch, ohne, bis",
                "DATIV fest: aus, bei, mit, nach, seit, von, zu",
                "WECHSELPRÄPOSITIONEN: in, auf, an, über, vor, zwischen, hinter, unter",
                "WECHSEL: wohin? → Akkusativ | wo? → Dativ",
                "IN: ich gehe IN die Schule (Akk) | ich bin IN der Schule (Dat)",
                "ZU: immer Dativ — Ich gehe zum (=zu dem) Arzt. Ich gehe zur (=zu der) Schule."
            )
        ),
        // 7. Verben mit Präpositionen
        Subject(
            id = "a1_07",
            level = "A1",
            name = "7. Verben mit Präpositionen",
            nameShort = "Verben + Präpositionen",
            description = "Einige Verben werden immer mit einer bestimmten Präposition verwendet. Die Präposition bestimmt den Kasus (Akkusativ oder Dativ).

WARTEN AUF (+Akk): Ich warte auf den Bus.
DENKEN AN (+Akk): Er denkt an seine Familie.
FREUEN SICH AUF/ÜBER (+Akk): Sie freut sich auf die Reise. / Sie freut sich über das Geschenk.
SPRECHEN ÜBER (+Akk): Wir sprechen über das Thema.
SICH ERINNERN AN (+Akk): Ich erinnere mich an den Tag.
HELFEN BEI (+Dat): Ich helfe bei der Arbeit.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 7,
            quizCount = 5,
            tips = listOf(
                "warten AUF (+Akk): Ich warte auf den Bus.",
                "denken AN (+Akk): Er denkt an die Familie.",
                "sprechen ÜBER (+Akk): Wir sprechen über das Problem.",
                "sich freuen AUF (+Akk): Freude auf die Zukunft",
                "sich freuen ÜBER (+Akk): Freude über etwas Geschehenes",
                "helfen BEI (+Dat): Sie hilft bei der Arbeit.",
                "sich erinnern AN (+Akk): Ich erinnere mich an dich.",
                "kümmern UM (+Akk): Wir kümmern uns um die Kinder."
            )
        ),
        // 8. Perfekt
        Subject(
            id = "a1_08",
            level = "A1",
            name = "8. Perfekt",
            nameShort = "Perfekt",
            description = "Das Perfekt beschreibt abgeschlossene Handlungen in der Vergangenheit. Bildung: haben oder sein als Hilfsverb + Partizip II.

HABEN-Verben (die meisten): ich habe gemacht, du hast gegessen, er hat gelesen
SEIN-Verben (Bewegung/Veränderung): ich bin gegangen, du bist gekommen, er ist geblieben

Partizip II: gemacht, gegessen, gelesen, gegangen, gekommen, gesehen, getrunken, geschrieben, gesprochen, gelernt",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 8,
            quizCount = 5,
            tips = listOf(
                "HABEN + Partizip II: für die meisten Verben (trinken → getrunken)",
                "SEIN + Partizip II: für Bewegung (gehen → gegangen, kommen → gekommen) und Veränderung (werden → geworden, sein → gewesen)",
                "Regelmäßige Verben: ge- + Stamm + -t: machen → gemacht, spielen → gespielt",
                "Unregelmäßige Verben: ge- + 3. Form + -en: lesen → gelesen, sehen → gesehen",
                "Trennbare Verben: am / auf / aus / ein / mit / vor / zurück → Partizip II: aufmachen → aufgemacht",
                "Frageform: Was hast du gemacht? (What did you do?)"
            )
        ),
        // 9. Modalverben (können, müssen, wollen, dürfen, sollen)
        Subject(
            id = "a1_09",
            level = "A1",
            name = "9. Modalverben (können, müssen, wollen, dürfen, sollen)",
            nameShort = "Modalverben",
            description = "Modalverben ändern die Bedeutung eines Satzes. Sie werden mit einem Infinitiv verwendet.

KÖNNEN (ability): Ich kann Deutsch sprechen. (I can speak German.)
MÜSSEN (necessity): Ich muss jetzt gehen. (I must go now.)
WOLLEN (wish): Ich will das machen. (I want to do that.)
DÜRFEN (permission): Ich darf das machen. (I am allowed to do that.)
SOLLEN (obligation): Ich soll das tun. (I should do that.)

Konjugation: ich kann, du kannst, er kann, wir können, ihr könnt, sie können",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 9,
            quizCount = 5,
            tips = listOf(
                "KÖNNEN = can/ability: Ich kann schwimmen. (I can swim.)",
                "MÜSSEN = must/necessity: Ich muss lernen. (I must study.)",
                "WOLLEN = want/wish: Ich will nach Hause. (I want to go home.)",
                "DÜRFEN = may/permission: Ich darf hier bleiben. (I may stay here.)",
                "SOLLEN = should/obligation: Du sollst zum Arzt gehen. (You should go to the doctor.)",
                "Modalverben stehen an 2. Stelle, Infinitiv am Ende: Ich muss heute Deutsch lernen.",
                "Konjugation: ich kann, du kannst, er kann, wir können, ihr könnt, sie können"
            )
        ),
        // 10. Sätze bilden (Wortstellung)
        Subject(
            id = "a1_10",
            level = "A1",
            name = "10. Sätze bilden (Wortstellung)",
            nameShort = "Satzbildung",
            description = "Grundlegende Wortstellung im deutschen Satz: Subjekt + Verb + Objekt. Das Verb steht an zweiter Stelle im Hauptsatz.

NORMAL: Ich trinke Kaffee. (Ich [Subjekt] trinke [Verb] Kaffee [Objekt])
VERB AN 2. STELLE: Heute trinke ich Kaffee. (Angabe + Verb + Subjekt + ...)
FRAGE: Trinke ich Kaffee? (Verb + Subjekt + ...)
NEBENSATZ (dass, weil, wenn): ... dass ich Kaffee trinke. (Verb am Ende!)

WICHTIG: Im Nebensatz steht das Verb am Ende!",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 10,
            quizCount = 5,
            tips = listOf(
                "HAUPTSATZ: Subjekt + Verb an 2. Stelle",
                "Frage: Verb + Subjekt an 1. Stelle? → Trinkst du Kaffee?",
                "Angabe vorne: Heute trinke ich Kaffee. (Angabe, Verb, Subjekt)",
                "NEBENSATZ: dass, weil, wenn, als, bevor → Verb am ENDE",
                "Ich trinke Kaffee. → Ich weiß, dass ich Kaffee trinke. (nicht: dass ich trinke Kaffee)",
                "Imperfekt Nebensatz: ... weil ich müde war. (Verb: war — am Ende)",
                "WORTSTELLUNG üben: Immer zuerst Subjekt und Verb finden!"
            )
        )
    )

    private fun getA2Subjects(): List<Subject> = listOf(
        Subject(
            id = "a2_01",
            level = "A2",
            name = "1. Präteritum (war, hatte, machte)",
            nameShort = "Präteritum",
            description = "Das Präteritum wird hauptsächlich in der geschriebenen Sprache und in formellen Situationen verwendet. Die wichtigsten Verben sind sein, haben und die Modalverben. Im Alltag wird es weniger häufig benutzt.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 1,
            quizCount = 0
        ),
        Subject(
            id = "a2_02",
            level = "A2",
            name = "2. Perfekt (haben/sein + Partizip II)",
            nameShort = "Perfekt",
            description = "Das Perfekt ist die wichtigste Vergangenheitsform im Alltag. Verwendung: haben oder sein als Hilfsverb + Partizip II. Die meisten Verben benutzen haben, nur Bewegungsverben und sein/werden benutzen sein.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 2,
            quizCount = 0
        ),
        Subject(
            id = "a2_03",
            level = "A2",
            name = "3. Verben mit Präpositionen (AC)",
            nameShort = "Verben + Präpositionen",
            description = "Bestimmte Verben erfordern bestimmte Präpositionen im Akkusativ oder Dativ: denken an (+A), warten auf (+A), sprechen über (+A), helfen bei (+D), sich freuen über (+A).",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 3,
            quizCount = 0
        ),
        Subject(
            id = "a2_04",
            level = "A2",
            name = "4. Wechselpräpositionen (in, auf, an, über, unter, vor, zwischen, hinter)",
            nameShort = "Wechselpräpositionen",
            description = "Wechselpräpositionen wechseln zwischen Akkusativ (Richtung) und Dativ (Ort): in, auf, an, über, unter, vor, zwischen, hinter. Akkusativ = wohin? Dativ = wo?",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 4,
            quizCount = 0
        ),
        Subject(
            id = "a2_05",
            level = "A2",
            name = "5. Nebensätze (dass, ob, weil, wenn, als)",
            nameShort = "Nebensätze",
            description = "Nebensätze sind von Sätzen eingeleitet durch: dass (dass), ob (ob), weil (weil), wenn (wenn), als (als), bevor (bevor), damit (damit), obwohl (obwohl). Das Verb steht am Satzende.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 5,
            quizCount = 0
        ),
        Subject(
            id = "a2_06",
            level = "A2",
            name = "6. Reflexive Verben (sich freuen, sich erinnern, sich befinden)",
            nameShort = "Reflexive Verben",
            description = "Reflexive Verben: sich freuen über (+A), sich erinnern an (+A), sich befinden in (+D), sich ärgern über (+A), sich interessieren für (+A). Das Reflexivpronomen richtet sich nach der Person und Kasus.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 6,
            quizCount = 0
        ),
        Subject(
            id = "a2_07",
            level = "A2",
            name = "7. Imperativ (Mach! Mach! Machen Sie!)",
            nameShort = "Imperativ",
            description = "Der Imperativ wird verwendet um Anweisungen zu geben: du-Form (Mach!), ihr-Form (Macht!), Sie-Form (Machen Sie!). Der Imperativ wird vor allem in informellen und formellen Kontexten verwendet.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 7,
            quizCount = 0
        ),
        Subject(
            id = "a2_08",
            level = "A2",
            name = "8. Plusquamperfekt (hatte gemacht, war gegangen)",
            nameShort = "Plusquamperfekt",
            description = "Das Plusquamperfekt beschreibt Handlungen, die vor einer anderen vergangenen Handlung stattfanden. Struktur: hatte/war + Partizip II. Es wird oft mit Präteritum oder Perfekt verwendet.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 8,
            quizCount = 0
        ),
        Subject(
            id = "a2_09",
            level = "A2",
            name = "9. Relativsätze (der, die, das, wo, wer, was)",
            nameShort = "Relativsätze",
            description = "Relativsätze werden mit der/die/das eingeleitet und geben zusätzliche Informationen über ein Nomen. Das Verb steht am Ende des Relativsatzes. Die Relativpronomen richten sich nach dem Kasus des Verbs.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 9,
            quizCount = 0
        ),
        Subject(
            id = "a2_10",
            level = "A2",
            name = "10. Konjunktionen (und, aber, oder, denn, sondern, deshalb, trotzdem)",
            nameShort = "Konjunktionen",
            description = "Die wichtigsten Konjunktionen: und (und), aber (aber), oder (oder), denn (denn), sondern (sondern), deshalb (deshalb), trotzdem (trotzdem), daher (daher), außerdem (außerdem).",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 10,
            quizCount = 0
        )
    )

    private fun getA1Subjects(): List<Subject> = listOf(
        Subject(
            id = "a1_01",
            level = "A1",
            name = "1. Verben konjugieren (sein, haben, werden)",
            nameShort = "Verben konjugieren",
            description = "Im A1-Level lernst du die wichtigsten Verben im Präsens zu konjugieren: sein, haben und werden. Diese Verben werden im Alltag sehr häufig verwendet.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 1,
            quizCount = 0
        ),
        Subject(
            id = "a1_02",
            level = "A1",
            name = "2. Nomen und Artikel",
            nameShort = "Nomen und Artikel",
            description = "Lerne die Artikel (der, die, das) und die Pluralformen der Nomen im Deutschen.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 2,
            quizCount = 0
        ),
        Subject(
            id = "a1_03",
            level = "A1",
            name = "3. Präsens (Gegenwart)",
            nameShort = "Präsens",
            description = "Das Präsens beschreibt Handlungen in der Gegenwart. Regelmäßige und unregelmäßige Verben im Präsens.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 3,
            quizCount = 0
        ),
        Subject(
            id = "a1_04",
            level = "A1",
            name = "4. Akkusativ (Wen-Fall)",
            nameShort = "Akkusativ",
            description = "Der Akkusativ beschreibt die direkten Objects einer Handlung. Lerne die Akkusativformen der Artikel.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 4,
            quizCount = 0
        ),
        Subject(
            id = "a1_05",
            level = "A1",
            name = "5. Dativ (Wem-Fall)",
            nameShort = "Dativ",
            description = "Der Dativ beschreibt die indirekten Objects einer Handlung. Lerne die Dativformen der Artikel.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 5,
            quizCount = 0
        ),
        Subject(
            id = "a1_06",
            level = "A1",
            name = "6. Präpositionen",
            nameShort = "Präpositionen",
            description = "Lerne die wichtigsten Präpositionen (in, auf, an, mit, nach, aus, von, zu, bei, für, gegen, um) und ihre Kasus.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 6,
            quizCount = 0
        ),
        Subject(
            id = "a1_07",
            level = "A1",
            name = "7. Verben mit Präpositionen",
            nameShort = "Verben + Präpositionen",
            description = "Einige Verben werden immer mit einer bestimmten Präposition verwendet: warten auf, denken an, sich freuen auf/über.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 7,
            quizCount = 0
        ),
        Subject(
            id = "a1_08",
            level = "A1",
            name = "8. Perfekt",
            nameShort = "Perfekt",
            description = "Das Perfekt beschreibt abgeschlossene Handlungen in der Vergangenheit. Bildung: haben/sein + Partizip II.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 8,
            quizCount = 0
        ),
        Subject(
            id = "a1_09",
            level = "A1",
            name = "9. Modalverben (können, müssen, wollen, dürfen, sollen)",
            nameShort = "Modalverben",
            description = "Modalverben ändern die Bedeutung eines Satzes: können (ability), müssen (necessity), wollen (wish), dürfen (permission), sollen (obligation).",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 9,
            quizCount = 0
        ),
        Subject(
            id = "a1_10",
            level = "A1",
            name = "10. Sätze bilden (Wortstellung)",
            nameShort = "Satzbildung",
            description = "Grundlegende Wortstellung im deutschen Satz: Subjekt + Verb + Objekt. Verb an zweiter Stelle im Hauptsatz.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 10,
            quizCount = 0
        )
    )

    private fun getC2Subjects(): List<Subject> = listOf(
        Subject(
            id = "c2_01",
            level = "C2",
            name = "1. Konjunktiv I und II in gehobener Schriftsprache",
            nameShort = "Konjunktiv I/II",
            description = "Konjunktiv I und II in gehobener Schriftsprache: Indirekte Rede mit Konjunktiv I, Hypothesen und Wünsche mit Konjunktiv II. Verwendung in akademischen und formellen Kontexten.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 1,
            quizCount = 0
        ),
        Subject(
            id = "c2_02",
            level = "C2",
            name = "2. Nominalstil und Verbalstil ( stilistische Varianten)",
            nameShort = "Nominal-/Verbalstil",
            description = "Nominalstil und Verbalstil: Vergleich beider Stile und deren Einsatzgebiete. Wann nominalisieren, wann verbalisieren. Stilistische Variation in verschiedenen Textsorten.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 2,
            quizCount = 0
        ),
        Subject(
            id = "c2_03",
            level = "C2",
            name = "3. Komplexe Satzgefüge (Mehrfach nebensätze)",
            nameShort = "Satzgefüge",
            description = "Komplexe Satzgefüge: Mehrfachnebensätze mit drei oder mehr Ebenen. Erkennung und Konstruktion von komplexen Satzstrukturen.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 3,
            quizCount = 0
        ),
        Subject(
            id = "c2_04",
            level = "C2",
            name = "4. Passiversatzformen und Funktionen des Passivs",
            nameShort = "Passivformen",
            description = "Passiversatzformen und Funktionen des Passivs: sein + zu, sich lassen + Infinitiv, man-Struktur. Vertiefte Analyse der Passivfunktionen in verschiedenen Textsorten.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 4,
            quizCount = 0
        ),
        Subject(
            id = "c2_05",
            level = "C2",
            name = "5. Konnektoren für akademische Argumentation (diesbezüglich, hinsichtlich, nonchalance)",
            nameShort = "Akademische Konnektoren",
            description = "Konnektoren für akademische Argumentation: hinsichtlich (hinsichtlich), diesbezüglich (diesbezüglich), nichtsdestoweniger (nichtsdestoweniger), obschon (obschon), ungeachtet (ungeachtet).",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 5,
            quizCount = 0
        ),
        Subject(
            id = "c2_06",
            level = "C2",
            name = "6. Partizipialattribute und ihre Umwandlung in Relativsätze",
            nameShort = "Partizipialattribute",
            description = "Partizipialattribute und ihre Umwandlung in Relativsätze: Kompression von Relativsätzen zu Partizipialgruppen. Umwandlung: Die am Fenster sitzende Frau → Die Frau, die am Fenster sitzt.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 6,
            quizCount = 0
        ),
        Subject(
            id = "c2_07",
            level = "C2",
            name = "7. Irreale Vergleichssätze (als ob, als wenn, als)",
            nameShort = "Irreale Vergleichssätze",
            description = "Irreale Vergleichssätze: als ob, als wenn, als. Ausdruck von hypothetischen Vergleichen und unrealen Situationen. Konjunktiv II in Vergleichssätzen.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 7,
            quizCount = 0
        ),
        Subject(
            id = "c2_08",
            level = "C2",
            name = "8. Modalverben: Konjunktiv I/II Formen und indirekte Rede",
            nameShort = "Modalverben indirekte Rede",
            description = "Modalverben: Konjunktiv I/II Formen und indirekte Rede: er könne, sie müsse, man habe, sie dürften. Überblick über alle Modalverbformen in der indirekten Rede.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 8,
            quizCount = 0
        ),
        Subject(
            id = "c2_09",
            level = "C2",
            name = "9. Textkohäsion: Pronomen, Konnektoren, Kettenbildung",
            nameShort = "Textkohäsion",
            description = "Textkohäsion: Pronomen, Konnektoren, Kettenbildung. Sicherstellung der internen Kohärenz und logischen Flussführung in komplexen Texten.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 9,
            quizCount = 0
        ),
        Subject(
            id = "c2_10",
            level = "C2",
            name = "10. Indirekte Rede mit Konjunktiv I (Zeitformen, Angleichung, Übereinstimmung)",
            nameShort = "Indirekte Rede KI",
            description = "Indirekte Rede mit Konjunktiv I: Zeitformen, Angleichung, Übereinstimmung. Tense conversion rules und Pronomenanpassung in der indirekten Rede.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 10,
            quizCount = 0
        )
    )

    private fun getC1Subjects(): List<Subject> = listOf(
        Subject(
            id = "c1_01",
            level = "C1",
            name = "1. Konjunktiv I (er sage, sie komme, man sei)",
            nameShort = "Konjunktiv I",
            description = "Konjunktiv I wird für die indirekte Rede verwendet. Formen: sei, habe, komme, sage, gehe, könne, müsse, dürfe, werde, habe, sei, bleibe. Besonders in Nachrichten und formellen Texten.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 1,
            quizCount = 0
        ),
        Subject(
            id = "c1_02",
            level = "C1",
            name = "2. Konjunktiv II in irrealen Bedingungssätzen (Wenn ich Zeit hätte, würde ich...)",
            nameShort = "KII Irreale Bedingung",
            description = "Konjunktiv II in irreale Bedingungssätzen: Wenn ich Zeit hätte, würde ich reisen. Strukturen: wenn + Konjunktiv II, ... Konjunktiv II. Verwendung für gegenwärtige und vergangene irreale Situationen.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 2,
            quizCount = 0
        ),
        Subject(
            id = "c1_03",
            level = "C1",
            name = "3. Passiversatzformen (sein zu, sich lassen, werden)",
            nameShort = "Passiversatz",
            description = "Passiversatzformen: sein zu + Infinitiv (müssen), sich lassen + Infinitiv (können), werden als Passiversatz. Diese Formen werden in formellen und akademischen Texten verwendet.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 3,
            quizCount = 0
        ),
        Subject(
            id = "c1_04",
            level = "C1",
            name = "4. Nominalstil (Substantivierung von Verben und Adjektiven)",
            nameShort = "Nominalstil",
            description = "Nominalstil: Verben und Adjektive werden zu Nomen nominalisiert. Verwendung von das + Verb-Stamm + -ung. Wichtig für akademische und formelle Texte.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 4,
            quizCount = 0
        ),
        Subject(
            id = "c1_05",
            level = "C1",
            name = "5. Syntax: Lange Nebensätze mit mehreren Ebenen",
            nameShort = "Lange Nebensätze",
            description = "Lange Nebensätze: Mehrere Nebensätze werden in einem Satz kombiniert. Erkennung und Konstruktion von komplexen Satzgefügen mit mehreren Ebenen.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 5,
            quizCount = 0
        ),
        Subject(
            id = "c1_06",
            level = "C1",
            name = "6. Konnektoren für wissenschaftliche Texte (daher, folglich, nicht zuletzt, zum einen...zum anderen)",
            nameShort = "Wissenschaftliche Konnektoren",
            description = "Konnektoren für wissenschaftliche Texte: daher (daher), folglich (folglich), nicht zuletzt (nicht zuletzt), zum einen...zum anderen (zum einen...zum anderen), sowohl...als auch (sowohl...als auch).",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 6,
            quizCount = 0
        ),
        Subject(
            id = "c1_07",
            level = "C1",
            name = "7. Relativsätze im Genitiv und Dativ (dessen, deren, denen, woran, worüber)",
            nameShort = "Relativsätze C1",
            description = "Relativsätze im Genitiv und Dativ: dessen, deren, denen, woran, worüber, worauf, wobei, wonach. Verwendung in formellen und akademischen Kontexten.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 7,
            quizCount = 0
        ),
        Subject(
            id = "c1_08",
            level = "C1",
            name = "8. Infinitivkonstruktionen (um zu, ohne zu, statt zu, anstatt zu)",
            nameShort = "Infinitivkonstruktionen",
            description = "Infinitivkonstruktionen: um zu (um zu), ohne zu (ohne zu), statt zu (statt zu), anstatt zu (anstatt zu). Ausdruck von Zweck und Gegensatz.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 8,
            quizCount = 0
        ),
        Subject(
            id = "c1_09",
            level = "C1",
            name = "9. Modalverben im Konjunktiv I (er könne, sie müsse, man habe)",
            nameShort = "Modalverben KI",
            description = "Modalverben im Konjunktiv I: er könne, sie müsse, man habe, sie dürften. Verwendung in der indirekten Rede mit Modalverben.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 9,
            quizCount = 0
        ),
        Subject(
            id = "c1_10",
            level = "C1",
            name = "10. Partizipialkonstruktionen (把从句压缩为分词短语)",
            nameShort = "Partizipialkonstruktionen",
            description = "Partizipialkonstruktionen: Relativsätze werden zu Partizipialgruppen komprimiert. Verwendung zur Verdichtung von Texten in formellen und akademischen Kontexten.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 10,
            quizCount = 0
        )
    )
}
