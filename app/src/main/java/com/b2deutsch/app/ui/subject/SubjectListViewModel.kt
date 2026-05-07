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
            description = "Nomen-Verb-Verbindungen sind Ausdrücke, bei denen ein Nomen mit einem Verb eine feste Wendung bildet. Diese sind typisch für formelle deutsche Texte und sollten in der B2-Prüfung korrekt verwendet werden.\n\nBeispiele:\n• 'Ich werde eine Entscheidung treffen.' (Entscheidung treffen)\n• 'Er hat eine Frage gestellt.'",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 16,
            quizCount = 0,
            tips = listOf(
                "Entscheidung treffen = karar vermek",
                "Frage stellen = soru sormak",
                "Eine Entscheidung treffen, eine Frage stellen",
                "Wichtig: der Artikel bleibt beim Nomen!",
                "Im B2-Exam: Leseverstehen und Schreiben"
            )
        ),
        // 18. Folgen ausdrücken
        Subject(
            id = "b2_18",
            level = "B2",
            name = "17. Folgen ausdrücken: folglich, infolgedessen, deshalb, sodass",
            nameShort = "Folgen ausdrücken",
            description = "Um Folgen und Ergebnisse auszudrücken, werden verschiedene Konnektoren verwendet: 'deshalb', 'daher', 'deswegen', 'folglich', 'infolgedessen', 'sodass'. Diese sind wichtig für argumentative Texte.\n\nBeispiele:\n• 'Es hat viel geregnet, deshalb ist die Straße nass.'\n• 'Er hat viel gelernt, sodass er die Prüfung bestanden hat.'",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 17,
            quizCount = 0,
            tips = listOf(
                "DESHALB/DESWEGEN/DARUM = therefore / bu yüzden (Position 2)",
                "FOLGLICH = consequently / sonuç olarak (Position 1 oder 2)",
                "INFOLGEDESSEN = consequently / bunun sonucunda (nachgestellt)",
                "SODASS = so that / öyle ki (Ziel/Wirkung, Verb am Ende)",
                "Im B2-Exam: diese zeigen logische Argumentation"
            )
        ),
        // 19. Ausdrücke mit Präpositionen
        Subject(
            id = "b2_19",
            level = "B2",
            name = "18. Ausdrücke mit Präpositionen",
            nameShort = "Präposition-Ausdrücke",
            description = "Viele Ausdrücke im Deutschen werden mit festen Präpositionen verwendet. Diese zu kennen ist wichtig für das Leseverstehen und für das Schreiben.\n\nBeispiele:\n• 'Es kommt darauf an, ob du lernen willst.' (an + Akkusativ)\n• 'Ich rechne mit deiner Hilfe.' (mit + Dativ)",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 18,
            quizCount = 0,
            tips = listOf(
                "ankommen auf + Akkusativ = dependent on",
                "rechnen mit + Dativ = to count on",
                "leiden unter + Dativ = to suffer from",
                "sich erinnern an + Akkusativ = to remember",
                "Im B2-Exam: Präpositionen mit bestimmten Verben und Adjektiven"
            )
        ),
        // 20. irreale Konditionalsätze in der Vergangenheit
        Subject(
            id = "b2_20",
            level = "B2",
            name = "19. irreale Konditionalsätze in der Vergangenheit",
            nameShort = "Irreale Konditionalsätze",
            description = "Irreale Konditionalsätze in der Vergangenheit beschreiben Situationen, die nicht passiert sind. Sie bestehen aus einem wenn-Satz (Bedingung) und einem Hauptsatz (Ergebnis). Beide verwenden den Konjunktiv II.\n\nBeispiele:\n• 'Wenn ich früher aufgestanden wäre, hätte ich den Zug erreicht.'\n• 'Hätte ich mehr Zeit gehabt, hätte ich das Buch gelesen.'",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "💭",
            order = 19,
            quizCount = 0,
            tips = listOf(
                "Wenn-Satz: wäre/hätte + Partizip II + worden/gewesen",
                "Hauptsatz: hätte/wäre + Partizip II + Konjugation",
                "Hätte ich... = Wäre ich... = Inversion möglich",
                "Bedeutung: wenn + hätte/wäre = if + had + past participle",
                "Im B2-Exam: oft in Leseverstehen und Schreiben"
            )
        ),
        // 21. Relativsätze im Genitiv
        Subject(
            id = "b2_21",
            level = "B2",
            name = "20. Relativsätze im Genitiv",
            nameShort = "Relativsätze Genitiv",
            description = "Relativsätze im Genitiv werden verwendet, um Nomen zu beschreiben, die ein Genitivattribut erfordern. Sie sind typisch für formelle Texte und sollten in der B2-Prüfung beherrscht werden.\n\nBeispiele:\n• 'Das ist der Mann, dessen Auto ich gefahren habe.'\n• 'Die Studentin, deren Prüfung ich korrigiert habe, ist krank.'",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 20,
            quizCount = 0,
            tips = listOf(
                "DESSEN (maskulin/neutral) = whose (bei dem Mann)",
                "DEREN (feminin/plural) = whose (bei der Frau)",
                "Genitiv nachgestellt: der Mann, dessen Auto...",
                "Wichtig: Deklination von dessen/deren beachten!",
                "Im B2-Exam: oft in formellen Lesetexten"
            )
        ),
        // 22. Konjunktiv I in der indirekten Rede
        Subject(
            id = "b2_22",
            level = "B2",
            name = "21. Konjunktiv I in der indirekten Rede",
            nameShort = "Konjunktiv I",
            description = "Der Konjunktiv I wird hauptsächlich in der indirekten Rede verwendet, um die Aussagen einer anderen Person wiederzugeben. In der B2-Prüfung ist diese Form wichtig für das Leseverstehen von Interviews und Berichten.\n\nBeispiele:\n• 'Er sagte, er komme morgen.' (Indirekte Rede)\n• 'Sie sagte, sie habe die Prüfung bestanden.'",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "💭",
            order = 21,
            quizCount = 0,
            tips = listOf(
                "Konjunktiv I: ich komme → er komme, ich habe → er habe",
                "sein → ich sei, du seist, er sei",
                "werden → ich werde, er werde",
                "Häufigste Verwendung: sagte er, meinte sie",
                "Im B2-Exam: in Berichten und Interviews"
            )
        ),
        // 23. Konjunktiv II in irrealen Vergleichsätzen
        Subject(
            id = "b2_23",
            level = "B2",
            name = "22. Konjunktiv II in irrealen Vergleichsätzen",
            nameShort = "Irreale Vergleiche",
            description = "Irreale Vergleichssätze werden mit 'als ob' oder 'als wenn' eingeleitet und beschreiben hypothetische Situationen. Das Verb steht im Konjunktiv II am Ende des Satzes.\n\nBeispiele:\n• 'Er sieht aus, als ob er krank wäre.' (Konjunktiv II)\n• 'Sie spricht, als wenn sie Deutscher wäre.'",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "💭",
            order = 22,
            quizCount = 0,
            tips = listOf(
                "ALS OB = as if / sanki",
                "ALS WENN = als ob (gleichbedeutend)",
                "Verb am Ende: ...als ob er krank wäre",
                "Konjunktiv II von sein: wäre, wärst, wäre",
                "Im B2-Exam: beschreibende Texte und Vergleiche"
            )
        )
    )

    private fun getB1Subjects(): List<Subject> = listOf(
        Subject(
            id = "b1_01",
            level = "B1",
            name = "B1 Grammatik: Perfekt",
            nameShort = "Perfekt",
            description = "Das Perfekt wird im Alltag häufig verwendet.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 1,
            quizCount = 5
        )
    )

    private fun getA2Subjects(): List<Subject> = listOf(
        Subject(
            id = "a2_01",
            level = "A2",
            name = "A2 Grammatik: Präteritum",
            nameShort = "Präteritum",
            description = "Das Präteritum für die Vergangenheit.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 1,
            quizCount = 3
        )
    )

    private fun getA1Subjects(): List<Subject> = listOf(
        Subject(
            id = "a1_01",
            level = "A1",
            name = "A1 Grammatik: Verben konjugieren",
            nameShort = "Verben",
            description = "Die wichtigsten Verben im Präsens.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 1,
            quizCount = 2
        )
    )

    private fun getC1Subjects(): List<Subject> = listOf(
        Subject(
            id = "c1_01",
            level = "C1",
            name = "C1 Grammatik: Subjekterweiterung",
            nameShort = "Subjekterweiterung",
            description = "Komplexe Satzstrukturen.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 1,
            quizCount = 4
        )
    )
}
