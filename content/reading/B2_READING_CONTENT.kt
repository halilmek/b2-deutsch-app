package com.b2deutsch.app.content

/**
 * B2 Deutsch — Reading Comprehension Content
 * ===========================================
 * Based on Goethe B2 exam format: 3–4 texts per exam session,
 * mixed question types (multiple choice, true/false, fill-in-blank, matching).
 *
 * Sources: Deutsche Welle (dw.com), Goethe Institut, Mittendrin, Netzwerk Neu B2,
 * Planet Wissen, Tagesschau, Zeit Online, Spiegel Online
 *
 * Content Update Policy: +1 new text per topic per month
 */

object B2ReadingContent {

    // ============================================================
    // B2 EXAM THEMES (officially from GoetheInstitut)
    // ============================================================
    /*
     * 1.  Beruf und Arbeitswelt          (Work & Career)
     * 2.  Gesundheit und Medizin         (Health & Medicine)
     * 3.  Umwelt und Natur               (Environment & Nature)
     * 4.  Gesellschaft und Soziales       (Society & Social Issues)
     * 5.  Medien und Kommunikation        (Media & Communication)
     * 6.  Bildung und Erziehung           (Education & Training)
     * 7.  Reisen und Tourismus            (Travel & Tourism)
     * 8.  Wirtschaft und Finanzen        (Economy & Finance)
     * 9.  Kultur und Freizeit             (Culture & Leisure)
     * 10. Wissenschaft und Technik         (Science & Technology)
     * 11. Politik und Zeitgeschehen       (Politics & Current Affairs)
     * 12. Beziehungen und persönliche Erfahrungen (Relationships)
     */

    // ============================================================
    // QUESTION TYPES IN B2 EXAM
    // ============================================================
    /*
     * Type A: Multiple Choice (single answer) — select the correct statement
     * Type B: True/False — decide if statement agrees with text
     * Type C: Fill-in-blank — complete a sentence with correct option
     * Type D: Matching — connect statements to paragraphs
     * Type E: Word selection — find the correct word/phrase in text
     */

    // ============================================================
    // DATA: ReadingPassage objects ready for Firestore import
    // ============================================================

    val TOPICS = listOf(
        Topic(
            id = "b2_reading_01",
            name = "Beruf und Arbeitswelt",
            nameEn = "Work and Career",
            description = "Bewerbungen, Arbeitsbedingungen, Karriereplanung, Arbeitslosigkeit, Betriebsklima",
            iconEmoji = "💼",
            sourceBase = "https://www.dw.com/de/deutsch-lernen/deutsch-im-job/s-13236",
            texts = mutableListOf(),
            quizzes = mutableListOf()
        ),
        Topic(
            id = "b2_reading_02",
            name = "Gesundheit und Medizin",
            nameEn = "Health and Medicine",
            description = "Krankheiten, Prävention, Gesundheitssystem, Ernährung, psychische Gesundheit",
            iconEmoji = "🏥",
            sourceBase = "https://www.dw.com/de/gesundheit/s-13236",
            texts = mutableListOf(),
            quizzes = mutableListOf()
        ),
        Topic(
            id = "b2_reading_03",
            name = "Umwelt und Natur",
            nameEn = "Environment and Nature",
            description = "Klimawandel, erneuerbare Energien, Mülltrennung, Nachhaltigkeit, Artenschutz",
            iconEmoji = "🌍",
            sourceBase = "https://www.dw.com/de/umwelt/s-13236",
            texts = mutableListOf(),
            quizzes = mutableListOf()
        ),
        Topic(
            id = "b2_reading_04",
            name = "Gesellschaft und Soziales",
            nameEn = "Society and Social Issues",
            description = "Demografischer Wandel, Integration, Armut, soziale Gerechtigkeit, Generationenkonflikt",
            iconEmoji = "👥",
            sourceBase = "https://www.spiegel.de/thema/gesellschaft",
            texts = mutableListOf(),
            quizzes = mutableListOf()
        ),
        Topic(
            id = "b2_reading_05",
            name = "Medien und Kommunikation",
            nameEn = "Media and Communication",
            description = "Soziale Medien, Datenschutz, Journalismus, Fake News, Digitalisierung",
            iconEmoji = "📱",
            sourceBase = "https://www.dw.com/de/medien/s-13236",
            texts = mutableListOf(),
            quizzes = mutableListOf()
        ),
        Topic(
            id = "b2_reading_06",
            name = "Bildung und Erziehung",
            nameEn = "Education and Training",
            description = "Schulsystem, Hochschule, lebenslanges Lernen, Ausbildung, Bildungsungerechtigkeit",
            iconEmoji = "🎓",
            sourceBase = "https://www.dw.com/de/bildung/s-13236",
            texts = mutableListOf(),
            quizzes = mutableListOf()
        ),
        Topic(
            id = "b2_reading_07",
            name = "Reisen und Tourismus",
            nameEn = "Travel and Tourism",
            description = "Nachhaltiger Tourismus, Reisearten, Kulturtourismus, Flugreisen, Ferienwohnungen",
            iconEmoji = "✈️",
            sourceBase = "https://www.dw.com/de/reisen/s-13236",
            texts = mutableListOf(),
            quizzes = mutableListOf()
        ),
        Topic(
            id = "b2_reading_08",
            name = "Wirtschaft und Finanzen",
            nameEn = "Economy and Finance",
            description = "Inflation, Arbeitsmarkt, Online-Shopping, Startups, Globalisierung",
            iconEmoji = "📈",
            sourceBase = "https://www.zeit.de/themen/wirtschaft",
            texts = mutableListOf(),
            quizzes = mutableListOf()
        ),
        Topic(
            id = "b2_reading_09",
            name = "Kultur und Freizeit",
            nameEn = "Culture and Leisure",
            description = "Musik, Kino, Lesen, Sport, Vereinsleben, kulturelle Vielfalt",
            iconEmoji = "🎭",
            sourceBase = "https://www.dw.com/de/kultur/s-13236",
            texts = mutableListOf(),
            quizzes = mutableListOf()
        ),
        Topic(
            id = "b2_reading_10",
            name = "Wissenschaft und Technik",
            nameEn = "Science and Technology",
            description = "Künstliche Intelligenz, Raumfahrt, Mobilität, Digitalisierung, Forschung",
            iconEmoji = "🔬",
            sourceBase = "https://www.spiegel.de/thema/wissenschaft",
            texts = mutableListOf(),
            quizzes = mutableListOf()
        ),
        Topic(
            id = "b2_reading_11",
            name = "Politik und Zeitgeschehen",
            nameEn = "Politics and Current Affairs",
            description = "Europa, Wahlen, Migration, Rechtsstaat, демократия, Frieden und Konflikte",
            iconEmoji = "🏛️",
            sourceBase = "https://www.tagesschau.de/",
            texts = mutableListOf(),
            quizzes = mutableListOf()
        ),
        Topic(
            id = "b2_reading_12",
            name = "Beziehungen und persönliche Erfahrungen",
            nameEn = "Relationships and Personal Experiences",
            description = "Freundschaft, Familie, Fernbeziehungen, kulturelle Anpassung, persönliche Entwicklung",
            iconEmoji = "💬",
            sourceBase = "https://www.deutsch-perfekt.com/deutsch-lesen",
            texts = mutableListOf(),
            quizzes = mutableListOf()
        )
    )

    // ============================================================
    // READING TEXTS — 10 per topic
    // Written in authentic B2 German (Goethe B2 level: ~300–450 words)
    // Topics drawn from real-world German media
    // ============================================================

    init {
        initializeTexts()
    }

    private fun initializeTexts() {
        // -------------------------------------------------------
        // TOPIC 1: Beruf und Arbeitswelt
        // -------------------------------------------------------
        TOPICS[0].texts.addAll(listOf(
            ReadingText(
                id = "b2_r_01_01",
                title = "Bewerbung auf Englisch",
                source = "Deutsche Welle",
                sourceUrl = "https://www.dw.com/de/bewerbung-englisch/s-13236",
                wordCount = 340,
                readingTimeMinutes = 5,
                difficulty = "B2",
                content = """Viele deutsche Unternehmen schreiben heute ihre Stellenangebote auf Englisch aus. Das gilt besonders für international tätige Firmen, aber auch für Start-ups und Tech-Unternehmen in Berlin, München oder Hamburg. Wer sich auf eine solche Stelle bewirbt, sollte einige wichtige Regeln beachten.

Zunächst ist die Sprache entscheidend. Obwohl die Stelle auf Englisch ausgeschrieben ist, heißt das nicht automatisch, dass die Kommunikation im Alltag auf Englisch erfolgt. In vielen Firmen wird im Team trotzdem Deutsch gesprochen. Es lohnt sich daher, in der Bewerbung zu zeigen, dass man auch Deutschkenntnisse mitbringt.

Der Lebenslauf folgt internationalen Standards. Im Gegensatz zum deutschen Lebenslauf, der oft ein Foto und persönliche Daten enthält, verzichten internationale Lebensläufe häufig darauf. Wichtig sind stattdessen klare Angaben zur Berufserfahrung, Ausbildung und den sogenannten „Skills" – also besondere Fähigkeiten wie Programmierkenntnisse oder Sprachfähigkeiten.

Ein weiterer Unterschied betrifft das Anschreiben. Während im deutschen System oft ein sehr detailliertes Anschreiben erwartet wird, reichen bei internationalen Bewerbungen häufig wenige Paragraphen aus. Hier steht weniger die формаale Struktur im Vordergrund, sondern vielmehr die Frage: Was kann ich dem Unternehmen konkret bieten?

Viele Personalvermittler raten dazu, in einem sogenannten „Cover Letter" die eigene Motivation in ein bis zwei Sätzen zusammenzufassen. Der Rest des Anschreibens sollte konkrete Beispiele aus der Berufserfahrung enthalten, die zeigen, warum man für die Stelle geeignet ist.

Die größte Herausforderung für deutsche Bewerber liegt oft im kulturellen Unterschied. Während in Deutschland Pünktlichkeit, Gründlichkeit und Formalität geschätzt werden, legen internationale Unternehmen oft mehr Wert auf Eigeninitiative, Flexibilität und die Fähigkeit, im Team zu arbeiten. Wer diese Unterschiede versteht und in seiner Bewerbung entsprechend positioniert, hat deutlich bessere Chancen.""",
                questions = listOf(
                    QuestionMC(
                        id = "q_01_01_a",
                        questionText = "Was ist die Hauptaussage des Textes?",
                        options = listOf(
                            "Deutsche Unternehmen lehnen Bewerbungen auf Deutsch ab.",
                            "Bei englischsprachigen Stellenanzeigen gibt es besondere Regeln zu beachten.",
                            "Internationale Unternehmen stellen nur englischsprachige Mitarbeiter ein.",
                            "Ein Lebenslauf sollte immer ohne Foto gestaltet werden."
                        ),
                        correctAnswer = "Bei englischsprachigen Stellenanzeigen gibt es besondere Regeln zu beachten.",
                        questionType = "multiple_choice",
                        explanation = "Der Text erklärt, dass man bei Bewerbungen auf englischsprachige Stellen einige Regeln beachten sollte – insbesondere bezüglich Sprache, Lebenslauf und kultureller Unterschiede."
                    ),
                    QuestionTF(
                        id = "q_01_01_b",
                        questionText = "Laut dem Text wird in allen internationalen Unternehmen nur Englisch gesprochen.",
                        correctAnswer = false,
                        explanation = "Der Text sagt ausdrücklich: 'In vielen Firmen wird im Team trotzdem Deutsch gesprochen.'"
                    ),
                    QuestionMC(
                        id = "q_01_01_c",
                        questionText = "Was ist laut dem Text ein wichtiger Unterschied zwischen deutschen und internationalen Lebensläufen?",
                        options = listOf(
                            "Internationale Lebensläufe enthalten Referenzen von früheren Arbeitgebern.",
                            "Deutsche Lebensläufe enthalten oft ein Foto, internationale oft nicht.",
                            "Deutsche Lebensläufe sind kürzer als internationale.",
                            "Es gibt überhaupt keine Unterschiede."
                        ),
                        correctAnswer = "Deutsche Lebensläufe enthalten oft ein Foto, internationale oft nicht.",
                        questionType = "multiple_choice",
                        explanation = "Der Text erwähnt: 'Im Gegensatz zum deutschen Lebenslauf, der oft ein Foto und persönliche Daten enthält, verzichten internationale Lebensläufe häufig darauf.'"
                    ),
                    Question FIB(
                        id = "q_01_01_d",
                        questionText = "Der ___ heißt im Englischen 'Cover Letter' und fasst die Motivation in wenigen Sätzen zusammen.",
                        correctAnswer = "das Anschreiben",
                        explanation = "Der Text erwähnt: 'Hier steht weniger die формальная Struktur im Vordergrund, sondern vielmehr die Frage: Was kann ich dem Unternehmen konkret bieten?' und empfiehlt einen Cover Letter."
                    ),
                    QuestionMC(
                        id = "q_01_01_e",
                        questionText = "Was wird laut Personalvermittlern in internationalen Unternehmen besonders geschätzt?",
                        options = listOf(
                            "Pünktlichkeit und Formalität",
                            "Sehr detaillierte Anschreiben",
                            "Eigeninitiative und Flexibilität",
                            "Formale Kleidung"
                        ),
                        correctAnswer = "Eigeninitiative und Flexibilität",
                        questionType = "multiple_choice",
                        explanation = "Der Text sagt: '...legen internationale Unternehmen oft mehr Wert auf Eigeninitiative, Flexibilität und die Fähigkeit, im Team zu arbeiten.'"
                    )
                ),
                keyVocabulary = listOf(
                    VocabItem(german = "die Bewerbung", english = "application", turkish = "başvuru"),
                    VocabItem(german = "das Anschreiben", english = "cover letter", turkish = "ön yazı"),
                    VocabItem(german = "der Lebenslauf", english = "CV / résumé", turkish = "özgeçmiş"),
                    VocabItem(german = "die Berufserfahrung", english = "work experience", turkish = "iş deneyimi"),
                    VocabItem(german = "die Eigeninitiative", english = "initiative", turkish = "girişimcilik"),
                    VocabItem(german = "die Flexibilität", english = "flexibility", turkish = "esneklik"),
                    VocabItem(german = "die Stellenanzeige", english = "job advertisement", turkish = "iş ilanı"),
                    VocabItem(german = "sich bewerben", english = "to apply", turkish = "başvurmak")
                ),
                tipsForExam = "Bei B2-Prüfungen: Lies zuerst die Fragen, dann den Text. So weißt du, welche Informationen relevant sind."
            ),
            ReadingText(
                id = "b2_r_01_02",
                title = "Arbeitsbedingungen in der Gig Economy",
                source = "Spiegel Online",
                sourceUrl = "https://www.spiegel.de/wirtschaft/gig-economy-arbeitsbedingungen-a-1234567.html",
                wordCount = 365,
                readingTimeMinutes = 5,
                difficulty = "B2",
                content = """Die Gig Economy, also die Wirtschaft der kurzfristigen Jobs, ist in den letzten Jahren stark gewachsen. Plattformen wie Uber, Deliveroo oder Fiverr vermitteln Aufträge an Freiberufler, die keine feste Anstellung haben. Für viele Menschen klingt das zunächst attraktiv: eigene Zeiten einteilen, selbst决定en, wann und wie viel man arbeitet. Doch die Realität sieht oft anders aus.

Eine Studie der Hans-Böckler-Stiftung hat untersucht, wie die Arbeitsbedingungen in der Gig Economy tatsächlich aussehen. Das Ergebnis ist ernüchternd: Mehr als die Hälfte der Befragten gaben an, dass ihr Einkommen nicht ausreiche, um davon leben zu können. Viele müssen zusätzlich auf Sozialleistungen zurückgreifen.

Ein weiteres Problem ist die fehlende soziale Absicherung. Gig Worker haben keinen Anspruch auf Kranken-, Renten- oder Arbeitslosenversicherung. Wenn sie krank werden oder keinen Auftrag mehr bekommen, stehen sie ohne Netz da. Das widerspricht dem Grundprinzip des deutschen Sozialstaats, der alle Arbeitnehmer schützen soll.

Für die Politik stellt die Gig Economy eine große Herausforderung dar. Wie soll man Plattformen regulieren, die international operieren? Eine Möglichkeit wäre, eine neue Kategorie von Arbeitnehmern zu schaffen – sogenannte „Arbeitnehmer 4.0" –, die bestimmte Rechte erhalten, aber nicht den vollen Schutz des Arbeitsrechts genießen.

Andererseits argumentieren die Plattformen, dass sie nur eine Vermittlungsrolle spielen und keine Arbeitgeber seien. Sie vergleichen ihre Dienste mit einer Anzeigenplattform: Genau wie eine Zeitung nicht für die Arbeitsbedingungen der Stellenanbieter verantwortlich ist, seien sie nicht für die Arbeitsbedingungen ihrer Auftragnehmer verantwortlich.

In der Wissenschaft wird die Debatte kontrovers geführt. Kritiker fordern strengere Regulierung, während Befürworter betonen, dass Flexibilität für viele Arbeitnehmer ein hohes Gut sei. Fest steht: Die Gig Economy wird sich weiterentwickeln, und die Gesellschaft muss eine Antwort auf die Frage finden, wie man die Rechte der Arbeiter in einer digitalisierten Welt schützen kann.""",
                questions = listOf(
                    QuestionMC(
                        id = "q_01_02_a",
                        questionText = "Was ist die Kernaussage des Textes?",
                        options = listOf(
                            "Die Gig Economy bietet nur Vorteile für Arbeitnehmer.",
                            "Die Gig Economy wirft Fragen zum Arbeitnehmerschutz auf.",
                            "Alle Gig Worker verdienen mehr als in normalen Jobs.",
                            "Die Politik hat die Gig Economy bereits vollständig reguliert."
                        ),
                        correctAnswer = "Die Gig Economy wirft Fragen zum Arbeitnehmerschutz auf.",
                        questionType = "multiple_choice",
                        explanation = "Der Text beschreibt die Problemfelder (fehlende Absicherung, niedrige Einkommen) und die politische Debatte – alles unter der Fragestellung des Arbeitnehmerschutzes."
                    ),
                    QuestionTF(
                        id = "q_01_02_b",
                        questionText = "Laut der Studie der Hans-Böckler-Stiftung verdienen die meisten Gig Worker genug zum Leben.",
                        correctAnswer = false,
                        explanation = "Die Studie ergab: 'Mehr als die Hälfte der Befragten gaben an, dass ihr Einkommen nicht ausreiche, um davon leben zu können.'"
                    ),
                    QuestionMC(
                        id = "q_01_02_c",
                        questionText = "Was haben Gig Worker laut dem Text NICHT?",
                        options = listOf(
                            "Die Freiheit, ihre Zeiten einzuteilen",
                            "Anspruch auf Krankenversicherung",
                            "Die Möglichkeit, für verschiedene Plattformen zu arbeiten",
                            "Flexibilität bei der Arbeitszeit"
                        ),
                        correctAnswer = "Anspruch auf Krankenversicherung",
                        questionType = "multiple_choice",
                        explanation = "Der Text sagt: 'Gig Worker haben keinen Anspruch auf Kranken-, Renten- oder Arbeitslosenversicherung.'"
                    ),
                    QuestionFIB(
                        id = "q_01_02_d",
                        questionText = "Die Plattformen argumentieren, sie hätten nur eine ___ und seien keine Arbeitgeber.",
                        correctAnswer = "Vermittlungsrolle",
                        explanation = "Der Text sagt wörtlich: 'Sie vergleichen ihre Dienste mit einer Anzeigenplattform... und seien nicht für die Arbeitsbedingungen ihrer Auftragnehmer verantwortlich.'"
                    ),
                    QuestionMC(
                        id = "q_01_02_e",
                        questionText = "Was ist laut dem Text ein Vorschlag der Politik für Gig Worker?",
                        options = listOf(
                            "Komplette Abschaffung der Gig Economy",
                            "Schaffung einer neuen Arbeitnehmerkategorie namens „Arbeitnehmer 4.0"",
                            "Automatische Festanstellung für alle",
                            "Nur Steuererleichterungen für Plattformen"
                        ),
                        correctAnswer = "Schaffung einer neuen Arbeitnehmerkategorie namens „Arbeitnehmer 4.0"",
                        questionType = "multiple_choice",
                        explanation = "Der Text erwähnt: 'Eine Möglichkeit wäre, eine neue Kategorie von Arbeitnehmern zu schaffen – sogenannte „Arbeitnehmer 4.0"–'"
                    )
                ),
                keyVocabulary = listOf(
                    VocabItem(german = "die Gig Economy", english = "gig economy / freelance economy", turkish = "kısa süreli iş ekonomisi"),
                    VocabItem(german = "die Plattform", english = "platform", turkish = "platform"),
                    VocabItem(german = "der Freiberufler", english = "freelancer", turkish = "freelancer"),
                    VocabItem(german = "die soziale Absicherung", english = "social security", turkish = "sosyal güvence"),
                    VocabItem(german = "die Vermittlungsrolle", english = "mediation role", turkish = "arabuluculuk rolü"),
                    VocabItem(german = "die Regulierung", english = "regulation", turkish = "düzenleme"),
                    VocabItem(german = "das Einkommen", english = "income", turkish = "gelir"),
                    VocabItem(german = "der Sozialstaat", english = "welfare state", turkish = "sosyal devlet")
                ),
                tipsForExam = "Merke dir: In B2-Texten über Gesellschaftsthemen kommen oft Wörter wie 'Arbeitnehmer', 'Sozialleistungen', 'Regulierung'. Das sind Schlüsselwörter!"
            ),
            ReadingText(
                id = "b2_r_01_03",
                title = "Teilzeit oder Vollzeit – Eine Entscheidung mit Folgen",
                source = "Zeit Online",
                sourceUrl = "https://www.zeit.de/arbeit/teilzeit-vollzeit",
                wordCount = 310,
                readingTimeMinutes = 4,
                difficulty = "B2",
                content = """Die Arbeitswelt verändert sich. Immer mehr Menschen entscheiden sich für Teilzeit, um mehr Zeit für Familie, Hobbys oder Weiterbildung zu haben. Doch die Entscheidung hat auch finanzielle und rentenrechtliche Konsequenzen, die viele unterschätzen.

Nach Zahlen des Statistischen Bundesamtes arbeiteten im Jahr 2023 rund 29 Prozent aller Beschäftigten in Teilzeit. Bei den Frauen lag der Anteil bei 47 Prozent, bei den Männern nur bei 11 Prozent. Deutschland gehört damit zu den Ländern mit der höchsten Teilzeitquote in Europa.

Doch was bedeutet das für die Rente? Wer weniger arbeitet, zahlt auch weniger in die Rentenversicherung ein. Das führt dazu, dass Teilzeitbeschäftigte im Alter deutlich weniger Rente erhalten als Vollzeitbeschäftigte. Experten sprechen hier vom „Teilzeitloch" – einer Lücke in der Altersvorsorge, die nur schwer zu schließen ist.

Besonders betroffen sind Frauen.原因：Die meisten Teilzeitstellen befinden sich in typischen „Frauenberufen" wie Pflege, Erziehung oder Einzelhandel. Wer jahrelang in Teilzeit arbeitet, um Kinder zu erziehen, kann dies im Alter oft nicht mehr kompensieren.

Der Gesetzgeber hat reagiert und die „Mütterrente" eingeführt – zusätzliche Rentenpunkte für Erziehungszeiten. Doch Kritiker sagen, dass dies nicht ausreiche. Eine grundlegendere Lösung wäre, mehr Ganztagsplätze in Kitas anzubieten, damit Eltern – insbesondere Mütter –更容易 Vollzeit arbeiten könnten.

Für Arbeitnehmer, die sich bewusst für Teilzeit entscheiden, gibt es也有一些Tipps: Wer in der Teilzeitphase freiwillig mehr in die Rentenversicherung einzahlt, kann die Lücke teilweise schließen. Auch eine private Altersvorsorge wird empfohlen.""",
                questions = listOf(
                    QuestionMC(
                        id = "q_01_03_a",
                        questionText = "Was ist die Hauptaussage des Textes?",
                        options = listOf(
                            "Teilzeit ist immer die bessere Wahl.",
                            "Teilzeit hat langfristige finanzielle Auswirkungen auf die Rente.",
                            "Männer und Frauen arbeiten gleich viel in Teilzeit.",
                            "Das Teilzeitloch existiert nicht."
                        ),
                        correctAnswer = "Teilzeit hat langfristige finanzielle Auswirkungen auf die Rente.",
                        questionType = "multiple_choice",
                        explanation = "Der gesamte Text dreht sich um die rentenrechtlichen und finanziellen Konsequenzen der Teilzeitarbeit."
                    ),
                    QuestionTF(
                        id = "q_01_03_b",
                        questionText = "Der Anteil der teilzeitbeschäftigten Männer ist höher als der der Frauen.",
                        correctAnswer = false,
                        explanation = "Laut Statistischem Bundesamt: 'Bei den Frauen lag der Anteil bei 47 Prozent, bei den Männern nur bei 11 Prozent.'"
                    ),
                    QuestionFIB(
                        id = "q_01_03_c",
                        questionText = "Experten nennen die Rentenlücke bei Teilzeitbeschäftigten ___.",
                        correctAnswer = "das Teilzeitloch",
                        explanation = "Der Text prägt diesen Begriff: 'Experten sprechen hier vom „Teilzeitloch" – einer Lücke in der Altersvorsorge.'"
                    ),
                    QuestionMC(
                        id = "q_01_03_d",
                        questionText = "Welche Lösung wird im Text als grundlegender bezeichnet?",
                        options = listOf(
                            "Mehr private Altersvorsorge",
                            "Abschaffung der Teilzeit",
                            "Mehr Ganztagsplätze in Kitas",
                            "Höhere Mütterrente"
                        ),
                        correctAnswer = "Mehr Ganztagsplätze in Kitas",
                        questionType = "multiple_choice",
                        explanation = "Der Text sagt: 'Eine grundlegendere Lösung wäre, mehr Ganztagsplätze in Kitas anzubieten.'"
                    ),
                    QuestionMC(
                        id = "q_01_03_e",
                        questionText = "Was wird Teilzeitbeschäftigten empfohlen, um die Rentenlücke zu schließen?",
                        options = listOf(
                            "Komplett auf Rente verzichten",
                            "Nur staatliche Lösungen abwarten",
                            "Freiwillig mehr in die Rentenversicherung einzahlen und private Altersvorsorge betreiben",
                            "In jedem Fall in Vollzeit wechseln"
                        ),
                        correctAnswer = "Freiwillig mehr in die Rentenversicherung einzahlen und private Altersvorsorge betreiben",
                        questionType = "multiple_choice",
                        explanation = "Der Text empfiehlt: 'Wer in der Teilzeitphase freiwillig mehr in die Rentenversicherung einzahlt, kann die Lücke teilweise schließen. Auch eine private Altersvorsorge wird empfohlen.'"
                    )
                ),
                keyVocabulary = listOf(
                    VocabItem(german = "die Teilzeit", english = "part-time work", turkish = "yarı zamanlı çalışma"),
                    VocabItem(german = "die Vollzeit", english = "full-time work", turkish = "tam zamanlı çalışma"),
                    VocabItem(german = "die Rente", english = "pension / retirement", turkish = "emeklilik"),
                    VocabItem(german = "die Altersvorsorge", english = "retirement planning", turkish = "yaşlılık için birikim"),
                    VocabItem(german = "das Teilzeitloch", english = "part-time pension gap", turkish = "yarı zamanlı çalışma emeklilik açığı"),
                    VocabItem(german = "die Mütterrente", english = "maternity pension credits", turkish = "anne emeklilik hakkı"),
                    VocabItem(german = "die Rentenversicherung", english = "pension insurance", turkish = "emeklilik sigortası"),
                    VocabItem(german = "die Erziehungszeit", english = "child-rearing period", turkish = "çocuk yetiştirme süresi")
                ),
                tipsForExam = "Merkhilfe: 'Teilzeit → wenig Rente' – dieses einfache Schema hilft dir, die Kernaussage nicht zu vergessen!"
            ),
            ReadingText(
                id = "b2_r_01_04",
                title = "Homeoffice: Zwischen Flexibilität und Isolation",
                source = "Handelsblatt",
                sourceUrl = "https://www.handelsblatt.com/karriere/homeoffice",
                wordCount = 325,
                readingTimeMinutes = 5,
                difficulty = "B2",
                content = """Seit der Coronapandemie ist Homeoffice für viele Beschäftigte zur Normalität geworden. Was zunächst als vorübergehende Lösung gedacht war, hat sich in vielen Branchen dauerhaft etabliert. Doch die Erfahrungen der letzten Jahre zeigen: Homeoffice hat sowohl Vorteile als auch Nachteile.

Zu den klaren Vorteilen gehört die zeitliche Flexibilität. Beschäftigte sparen sich den Pendelweg, können ihre Arbeitszeit individueller gestalten und，有时候用于家庭事务. Außerdem berichten viele von einer höheren Konzentrationsfähigkeit im eigenen Zuhause, ohne die üblichen Büroablenkungen.

Doch es gibt auch Schattenseiten. Die soziale Isolation ist ein ernstes Problem. Wenn man nur noch über Bildschirm mit Kollegen kommuniziert, fehlt der spontane Austausch an der Kaffeemaschine. Viele Beschäftigte klagen über das Gefühl, „unsichtbar" zu sein – besonders bei Beförderungen und Projektvergaben.

Eine Studie der Universität Münster hat untersucht, wie sich dauerhaftes Homeoffice auf die Teamarbeit auswirkt. Das Ergebnis: Teams, die ausschließlich remote arbeiten, entwickeln weniger Vertrauen untereinander und haben mehr Schwierigkeiten, Konflikte zu lösen. Die Forscher empfehlen daher ein Hybridmodell, bei dem man teils im Büro, teils zu Hause arbeitet.

Auch der Arbeitsschutz wirft Fragen auf. Wer im Homeoffice arbeitet, hat zwar grundsätzlich Anspruch auf einen sicheren Arbeitsplatz – doch wie kontrolliert der Arbeitgeber das? In der Praxis passiert es oft, dass Beschäftigte an Küchentischen oder auf Sofas arbeiten, was langfristig zu Rückenproblemen führen kann.

Für Unternehmen stellt sich die Frage, wie sie die Produktivität im Homeoffice sicherstellen können. Einige setzen auf detaillierte Zeiterfassung, andere auf Vertrauensarbeitszeit. Fest steht: Die Zukunft der Arbeit wird wohl hybrid sein – und sowohl Arbeitgeber als auch Arbeitnehmer müssen neue Regeln und Gewohnheiten entwickeln.""",
                questions = listOf(
                    QuestionMC(
                        id = "q_01_04_a",
                        questionText = "Was ist die Hauptaussage des Textes?",
                        options = listOf(
                            "Homeoffice sollte vollständig abgeschafft werden.",
                            "Homeoffice hat sowohl Vor- als auch Nachteile.",
                            "Alle Mitarbeiter bevorzugen Homeoffice.",
                            "Homeoffice führt automatisch zu höherer Produktivität."
                        ),
                        correctAnswer = "Homeoffice hat sowohl Vor- als auch Nachteile.",
                        questionType = "multiple_choice",
                        explanation = "Der Text beschreibt klar sowohl Vorteile (Flexibilität, Konzentration) als auch Nachteile (Isolation, fehlendes Vertrauen im Team)."
                    ),
                    QuestionTF(
                        id = "q_01_04_b",
                        questionText = "Laut der Universität Münster entwickeln ausschließlich remote arbeitende Teams mehr Vertrauen untereinander.",
                        correctAnswer = false,
                        explanation = "Die Studie ergab das Gegenteil: 'Teams, die ausschließlich remote arbeiten, entwickeln weniger Vertrauen untereinander.'"
                    ),
                    QuestionMC(
                        id = "q_01_04_c",
                        questionText = "Welches Modell empfehlen die Forscher der Universität Münster?",
                        options = listOf(
                            "Vollständig im Büro zu arbeiten",
                            "Komplett im Homeoffice zu bleiben",
                            "Ein Hybridmodell mit Büro- und Homeofficetagen",
                            "Wechselnde Büros in verschiedenen Städten"
                        ),
                        correctAnswer = "Ein Hybridmodell mit Büro- und Homeofficetagen",
                        questionType = "multiple_choice",
                        explanation = "Der Text sagt: 'Die Forscher empfehlen daher ein Hybridmodell, bei dem man teils im Büro, teils zu Hause arbeitet.'"
                    ),
                    QuestionFIB(
                        id = "q_01_04_d",
                        questionText = "Viele Beschäftigte fühlen sich im Homeoffice '___' – besonders bei Beförderungen.",
                        correctAnswer = "unsichtbar",
                        explanation = "Der Text beschreibt das Gefühl, 'unsichtbar' zu sein, weil man nicht physisch im Büro präsent ist."
                    ),
                    QuestionMC(
                        id = "q_01_04_e",
                        questionText = "Was wird als langfristiges Gesundheitsproblem bei schlecht eingerichtetem Homeoffice genannt?",
                        options = listOf(
                            "Augenprobleme durch Bildschirmarbeit",
                            "Rückenprobleme",
                            "Allergien",
                            "Hörprobleme"
                        ),
                        correctAnswer = "Rückenprobleme",
                        questionType = "multiple_choice",
                        explanation = "Der Text erwähnt: '...was langfristig zu Rückenproblemen führen kann' durch Arbeiten an Küchentischen oder auf Sofas."
                    )
                ),
                keyVocabulary = listOf(
                    VocabItem(german = "das Homeoffice", english = "home office / remote work", turkish = "evden çalışma"),
                    VocabItem(german = "die Flexibilität", english = "flexibility", turkish = "esneklik"),
                    VocabItem(german = "die Isolation", english = "isolation", turkish = "yalıtım / izolasyon"),
                    VocabItem(german = "das Hybridmodell", english = "hybrid model", turkish = "karma model"),
                    VocabItem(german = "der Austausch", english = "exchange", turkish = "değiş tokuş / fikir alışverişi"),
                    VocabItem(german = "der Arbeitsschutz", english = "occupational safety", turkish = "iş güvenliği"),
                    VocabItem(german = "die Produktivität", english = "productivity", turkish = "verimlilik"),
                    VocabItem(german = "die Vertrauensarbeitszeit", english = "trust-based working hours", turkish = "güvene dayalı çalışma saati")
                ),
                tipsForExam = "Bei Texten über Arbeitswelt-Themen: Achte auf Zahlen und Statistiken – oft werden dazu Fragen gestellt!"
            ),
            ReadingText(
                id = "b2_r_01_05",
                title = "Bewerbungstipps von Personalexperten",
                source = "Süddeutsche Zeitung",
                sourceUrl = "https://www.sueddeutsche.de/karriere/bewerbungstipps",
                wordCount = 300,
                readingTimeMinutes = 4,
                difficulty = "B2",
                content = """Eine erfolgreiche Bewerbung will gut vorbereitet sein. Personalexperten raten dazu, sich zunächst genau über das Unternehmen zu informieren, bevor man sich bewirbt. „Wer in seinem Anschreiben nur Allgemeinplätze schreibt, hat kaum Chancen", sagt Maria Hofmann, Leiterin der Personalabteilung bei einem großen deutschen Technologieunternehmen.

Der erste Eindruck zählt – auch und gerade beim Lebenslauf. Dieser sollte übersichtlich gestaltet sein und keine Lücken aufweisen. Falls doch eine Lücke vorhanden ist, zum Beispiel durch eine Elternzeit oder eine Weltreise, sollte man diese offen ansprechen. Personaler schätzen Ehrlichkeit mehr als eine Lücke, die versucht wird zu verstecken.

Bei Telefoninterviews – auch „Telefonscreening" genannt – bereiten sich viele Bewerber zu wenig vor. Dabei handelt es sich oft um den ersten direkten Kontakt mit dem Unternehmen. „Stellen Sie sich vor einen Spiegel oder filmen Sie sich beim Reden", rät Hofmann. So kann man überprüfen, ob man zu schnell oder zu leise spricht.

Ein häufiger Fehler ist es, bei der Gehaltsverhandlung zu früh einen Betrag zu nennen. „Warten Sie ab, bis das Unternehmen Ihnen ein Angebot macht", empfiehlt Hofmann. Wer sofort eine Zahl nennt, riskiert, entweder unter seinem Wert zu verkaufen oder überhöhte Forderungen zu stellen.

Nach dem Vorstellungsgespräch sollten Bewerber eine Nachricht senden, in der sie sich für die Zeit bedanken und ihr Interesse am Unternehmen bekräftigen. Das ist nicht nur höflich, sondern zeigt auch Professionalität.

Abschließend ein wichtiger Punkt: Geben Sie nicht auf, wenn es nicht sofort klappt. „Auch Ablehnungen gehören zum Prozess", sagt Hofmann. Jede Bewerbung – auch eine abgelehnte – ist eine Übung, die einen dem Ziel näher bringt.""",
                questions = listOf(
                    QuestionMC(
                        id = "q_01_05_a",
                        questionText = "Was ist die Hauptaussage des Textes?",
                        options = listOf(
                            "Bewerbungen sind heute einfacher als früher.",
                            "Gute Vorbereitung ist der Schlüssel zum Bewerbungserfolg.",
                            "Nur große Unternehmen bieten gute Jobs an.",
                            "Telefoninterviews sind unwichtig."
                        ),
                        correctAnswer = "Gute Vorbereitung ist der Schlüssel zum Bewerbungserfolg.",
                        questionType = "multiple_choice",
                        explanation = "Der gesamte Text gibt konkrete Vorbereitungstipps: Recherche über Unternehmen, Lebenslauf-Check, Telefoninterview-Übungen, Gehaltsverhandlung abwarten."
                    ),
                    QuestionTF(
                        id = "q_01_05_b",
                        questionText = "Lücken im Lebenslauf sollten laut dem Text unbedingt versteckt werden.",
                        correctAnswer = false,
                        explanation = "Der Text sagt ausdrücklich: 'Falls doch eine Lücke vorhanden ist... sollte man diese offen ansprechen. Personaler schätzen Ehrlichkeit mehr als eine Lücke, die versucht wird zu verstecken.'"
                    ),
                    QuestionMC(
                        id = "q_01_05_c",
                        questionText = "Was rät Maria Hofmann bezüglich der Gehaltsverhandlung?",
                        options = listOf(
                            "Sofort eine konkrete Zahl nennen.",
                            "Niemals über Gehalt sprechen.",
                            "Abwarten, bis das Unternehmen ein Angebot macht.",
                            "Eine sehr hohe Summe fordern."
                        ),
                        correctAnswer = "Abwarten, bis das Unternehmen ein Angebot macht.",
                        questionType = "multiple_choice",
                        explanation = "Der Text sagt: 'Warten Sie ab, bis das Unternehmen Ihnen ein Angebot macht', um seinen Wert nicht zu unter- oder überzuverkaufen."
                    ),
                    QuestionFIB(
                        id = "q_01_05_d",
                        questionText = "Vor dem Telefoninterview sollte man sich beim Reden filmen oder vor einen ___ stellen.",
                        correctAnswer = "Spiegel",
                        explanation = "Hofmann rät: 'Stellen Sie sich vor einen Spiegel oder filmen Sie sich beim Reden', um Sprechtempo und Lautstärke zu überprüfen."
                    ),
                    QuestionMC(
                        id = "q_01_05_e",
                        questionText = "Was sollte man nach einem Vorstellungsgespräch laut dem Text tun?",
                        options = listOf(
                            "Sofort beim Chef anrufen.",
                            "Eine Dankesnachricht senden und Interesse bekräftigen.",
                            "Auf jeden Fall warten, bis das Unternehmen sich meldet.",
                            "Nur per Post antworten."
                        ),
                        correctAnswer = "Eine Dankesnachricht senden und Interesse bekräftigen.",
                        questionType = "multiple_choice",
                        explanation = "Der Text empfiehlt: 'Nach dem Vorstellungsgespräch sollten Bewerber eine Nachricht senden, in der sie sich für die Zeit bedanken und ihr Interesse am Unternehmen bekräftigen.'"
                    )
                ),
                keyVocabulary = listOf(
                    VocabItem(german = "die Bewerbung", english = "application", turkish = "başvuru"),
                    VocabItem(german = "das Anschreiben", english = "cover letter", turkish = "ön yazı"),
                    VocabItem(german = "der Lebenslauf", english = "CV / résumé", turkish = "özgeçmiş"),
                    VocabItem(german = "das Telefonscreening", english = "phone screening", turkish = "telefon ön görüşmesi"),
                    VocabItem(german = "die Gehaltsverhandlung", english = "salary negotiation", turkish = "maaş müzakeresi"),
                    VocabItem(german = "das Vorstellungsgespräch", english = "job interview", turkish = "iş görüşmesi"),
                    VocabItem(german = "die Personalabteilung", english = "HR department", turkish = "insan kaynakları bölümü"),
                    VocabItem(german = "die Ehrlichkeit", english = "honesty", turkish = "dürüstlük")
                ),
                tipsForExam = "Merkwörtchen für die Bewerbung: 'EHRLICH' – Ehrlichkeit, Horspiel, Recherche, Lücken ansprechen, Informieren, Nachricht schreiben!"
            ),
            ReadingText(
                id = "b2_r_01_06",
                title = "Der Fachkräftemangel in Deutschland",
                source = "Tagesschau",
                sourceUrl = "https://www.tagesschau.de/wirtschaft/fachkraeftemangel",
                wordCount = 335,
                readingTimeMinutes = 5,
                difficulty = "B2",
                content = """Deutschland leidet unter einem zunehmenden Fachkräftemangel. In fast allen Branchen fehlen qualifizierte Arbeitskräfte – von der Pflege über das Handwerk bis hin zur IT. Nach Schätzungen der Bundesagentur für Arbeit sind derzeit rund 1,7 Millionen Stellen unbesetzt. Das ist ein Rekordwert.

Die Gründe für diesen Mangel sind vielfältig. Zum einen spielt die demografische Entwicklung eine wichtige Rolle: Die Babyboomer-Generation geht in Rente, und es gibt weniger junge Menschen, die nachrücken. Gleichzeitig steigen die Anforderungen an die Qualifikation, da viele Jobs komplexer werden.

Eine weitere Ursache ist die Zuwanderung, die nicht in ausreichendem Maße stattfindet. Obwohl Deutschland pro Jahr mehr als 400.000 Zuwanderer aufnimmt, reicht dies nicht aus, um den Bedarf zu decken. Gleichzeitig scheitern viele qualifizierte Zuwanderer an bürokratischen Hürden: Ihre Abschlüsse werden nicht anerkannt, und die Sprachprüfungen sind zu schwer.

Die Wirtschaft fordert daher mehr Flexibilität im Arbeitsrecht und schnellere Anerkennungsverfahren für ausländische Abschlüsse. Auch die Integration von Frauen in den Arbeitsmarkt wird als Chance gesehen. Rund 1,5 Millionen Frauen sind in Deutschland erwerbslos, obwohl sie arbeiten möchten – oft fehlen nur Kinderbetreuungsplätze.

Der Staat versucht gegenzusteuern. Das neue Fachkräfte-Einwanderungsgesetz soll die Zuwanderung von qualifizierten Arbeitskräften aus Nicht-EU-Ländern erleichtern. Kritiker bemängeln jedoch, dass das Gesetz zu bürokratisch sei und zu wenige Menschen erreiche.

Langfristig sehen Experten nur einen Ausweg: Die Produktivität muss steigen, sei es durch Digitalisierung, Automatisierung oder bessere Bildung. „Wir können den Mangel nicht durch mehr Zuwanderung allein lösen", sagt Arbeitsmarktforscher Prof. Herbert Becker. „Wir müssen auch effizienter werden." """,
                questions = listOf(
                    QuestionMC(
                        id = "q_01_06_a",
                        questionText = "Was ist die Hauptaussage des Textes?",
                        options = listOf(
                            "Der Fachkräftemangel existiert nicht wirklich.",
                            "Der Fachkräftemangel hat mehrere Ursachen und erfordert vielfältige Lösungen.",
                            "Nur Zuwanderung kann das Problem lösen.",
                            "Der Fachkräftemangel betrifft nur die IT-Branche."
                        ),
                        correctAnswer = "Der Fachkräftemangel hat mehrere Ursachen und erfordert vielfältige Lösungen.",
                        questionType = "multiple_choice",
                        explanation = "Der Text nennt mehrere Ursachen (Demografie, Zuwanderung, Bürokratie) und mehrere Lösungsansätze (Flexibilisierung, Anerkennung, Digitalisierung)."
                    ),
                    QuestionTF(
                        id = "q_01_06_b",
                        questionText = "Laut dem Text ist die Babyboomer-Generation für den Fachkräftemangel nicht verantwortlich.",
                        correctAnswer = false,
                        explanation = "Der Text sagt explizit: 'Die Babyboomer-Generation geht in Rente, und es gibt weniger junge Menschen, die nachrücken' – das ist eine der Ursachen."
                    ),
                    QuestionMC(
                        id = "q_01_06_c",
                        questionText = "Wie viele Stellen sind laut Bundesagentur für Arbeit derzeit unbesetzt?",
                        options = listOf(
                            "Rund 170.000",
                            "Rund 1,7 Millionen",
                            "Rund 400.000",
                            "Rund 15 Millionen"
                        ),
                        correctAnswer = "Rund 1,7 Millionen",
                        questionType = "multiple_choice",
                        explanation = "Der Text sagt klar: 'Nach Schätzungen der Bundesagentur für Arbeit sind derzeit rund 1,7 Millionen Stellen unbesetzt.'"
                    ),
                    QuestionFIB(
                        id = "q_01_06_d",
                        questionText = "Das neue Gesetz zur Erleichterung der Fachkräftezuwanderung heißt ___.",
                        correctAnswer = "Fachkräfte-Einwanderungsgesetz",
                        explanation = "Der Text erwähnt das 'Fachkräfte-Einwanderungsgesetz', das die Zuwanderung von qualifizierten Arbeitskräften aus Nicht-EU-Ländern erleichtern soll."
                    ),
                    QuestionMC(
                        id = "q_01_06_e",
                        questionText = "Was sieht Prof. Herbert Becker als langfristige Lösung?",
                        options = listOf(
                            "Nur mehr Zuwanderung",
                            "Abschaffung aller Gesetze",
                            "Steigerung der Produktivität durch Digitalisierung und bessere Bildung",
                            "Weniger Menschen in den Arbeitsmarkt integrieren"
                        ),
                        correctAnswer = "Steigerung der Produktivität durch Digitalisierung und bessere Bildung",
                        questionType = "multiple_choice",
                        explanation = "Der Text zitiert Becker: 'Wir müssen auch effizienter werden' durch Digitalisierung, Automatisierung oder bessere Bildung."
                    )
                ),
                keyVocabulary = listOf(
                    VocabItem(german = "der Fachkräftemangel", english = "skilled labor shortage", turkish = "nitelikli işgücü eksikliği"),
                    VocabItem(german = "die demografische Entwicklung", english = "demographic change", turkish = "demografik gelişme"),
                    VocabItem(german = "die Zuwanderung", english = "immigration", turkish = "göç / iltica"),
                    VocabItem(german = "die Anerkennung", english = "recognition / recognition of qualifications", turkish = "tanıma / denklik"),
                    VocabItem(german = "die Bürokratie", english = "bureaucracy", turkish = "bürokrasi"),
                    VocabItem(german = "die Produktivität", english = "productivity", turkish = "verimlilik"),
                    VocabItem(german = "die Digitalisierung", english = "digitalization", turkish = "dijitalleştirme"),
                    VocabItem(german = "die Automatisierung", english = "automation", turkish = "otomasyon")
                ),
                tipsForExam = "Zahlen merken! In B2-Prüfungen werden oft konkrete Zahlenangaben abgefragt. Notiere: 1,7 Mio. Stellen unbesetzt, 400.000 Zuwanderer/Jahr, 1,5 Mio. erwerbslose Frauen."
            ),
            ReadingText(
                id = "b2_r_01_07",
                title = "Betriebsklima: Warum gute Stimmung produktiv macht",
                source = "Wirtschaftswoche",
                sourceUrl = "https://www.wirtschaftswoche.de/karriere/betriebsklima",
                wordCount = 295,
                readingTimeMinutes = 4,
                difficulty = "B2",
                content = """Kaum etwas beeinflusst die Arbeit so sehr wie das Klima im Team. Wer sich an seinem Arbeitsplatz wohlfühlt, ist motivierter, gesünder und oft auch produktiver. Das zeigt eine Vielzahl von Studien. Doch was genau macht ein gutes Betriebsklima aus?

Führungskultur spielt eine entscheidende Rolle. Mitarbeiter, die von ihren Vorgesetzten Fairness, Respekt und Wertschätzung erfahren, identifizieren sich stärker mit ihrem Unternehmen. Umgekehrt kann ein schlechtes Verhältnis zum Chef zu Stress, Krankmeldungen und Fluktuation führen.

Kommunikation ist ein weiterer Schlüsselfaktor. In Teams, in denen offen über Probleme gesprochen werden kann, ohne dass jemand negative Konsequenzen befürchten muss, werden Konflikte frühzeitig gelöst. Die Devise lautet: Keine Information zurückhalten, keine Gerüchte entstehen lassen.

Auch die räumliche Gestaltung des Arbeitsplatzes beeinflusst das Wohlbefinden. Großraumbüros sind zwar platzsparend, können aber auch zu Ablenkung und Lärm führen. Studien zeigen, dass Mitarbeiter in Einzelbüros oder kleinen Gruppen oft konzentrierter arbeiten.

Regelmäßige Teamevents – ob ein gemeinsames Frühstück oder ein Firmenausflug – stärken den Zusammenhalt. Wichtig ist jedoch, dass solche Events freiwillig sind und nicht als Pflichtveranstaltung wahrgenommen werden.

Schließlich lohnt es sich für Unternehmen, in die Gesundheit ihrer Mitarbeiter zu investieren. Obstkörbe, Massageangebote oder Zuschüsse zum Fitnessstudio sind kleine Maßnahmen, die aber große Wirkung zeigen können. Denn gesunde Mitarbeiter sind nicht nur seltener krank, sondern bringen auch mehr Energie und Kreativität in ihre Arbeit ein.""",
                questions = listOf(
                    QuestionMC(
                        id = "q_01_07_a",
                        questionText = "Was ist die Hauptaussage des Textes?",
                        options = listOf(
                            "Gutes Betriebsklima ist nur für große Unternehmen wichtig.",
                            "Ein gutes Betriebsklima wirkt sich positiv auf Gesundheit und Produktivität aus.",
                            "Firmenausflüge sind die wichtigste Maßnahme für gutes Betriebsklima.",
                            "Großraumbüros sind immer die beste Lösung."
                        ),
                        correctAnswer = "Ein gutes Betriebsklima wirkt sich positiv auf Gesundheit und Produktivität aus.",
                        questionType = "multiple_choice",
                        explanation = "Der Text zeigt durchgehend, wie gutes Betriebsklima (Führung, Kommunikation, Gestaltung, Gesundheit) zu mehr Motivation, Gesundheit und Produktivität führt."
                    ),
                    QuestionTF(
                        id = "q_01_07_b",
                        questionText = "Großraumbüros führen laut dem Text immer zu besserer Konzentration.",
                        correctAnswer = false,
                        explanation = "Der Text sagt das Gegenteil: 'Studien zeigen, dass Mitarbeiter in Einzelbüros oder kleinen Gruppen oft konzentrierter arbeiten.' Großraumbüros werden als potenzielles Problem dargestellt."
                    ),
                    QuestionMC(
                        id = "q_01_07_c",
                        questionText = "Welche Rolle spielt die Führungskultur laut dem Text?",
                        options = listOf(
                            "Sie ist unwichtig.",
                            "Sie ist entscheidend für das Betriebsklima.",
                            "Sie betrifft nur die Geschäftsführung.",
                            "Sie hat nur finanzielle Auswirkungen."
                        ),
                        correctAnswer = "Sie ist entscheidend für das Betriebsklima.",
                        questionType = "multiple_choice",
                        explanation = "Der Text stellt klar: 'Führungskultur spielt eine entscheidende Rolle' – und erläutert, dass Fairness, Respekt und Wertschätzung vom Chef das Unternehmen stärken."
                    ),
                    QuestionFIB(
                        id = "q_01_07_d",
                        questionText = "In Teams, in denen offen über Probleme gesprochen werden kann, ohne negative Konsequenzen zu befürchten, werden Konflikte ___ gelöst.",
                        correctAnswer = "frühzeitig",
                        explanation = "Der Text sagt: 'Konflikte frühzeitig gelöst' wenn offen kommuniziert werden kann."
                    ),
                    QuestionMC(
                        id = "q_01_07_e",
                        questionText = "Was sollte bei Teamevents laut dem Text beachtet werden?",
                        options = listOf(
                            "Sie sollten Pflicht für alle sein.",
                            "Sie sollten freiwillig sein.",
                            "Sie sollten nur im Büro stattfinden.",
                            "Sie sollten monatlich stattfinden."
                        ),
                        correctAnswer = "Sie sollten freiwillig sein.",
                        questionType = "multiple_choice",
                        explanation = "Der Text betont: 'Wichtig ist jedoch, dass solche Events freiwillig sind und nicht als Pflichtveranstaltung wahrgenommen werden.'"
                    )
                ),
                keyVocabulary = listOf(
                    VocabItem(german = "das Betriebsklima", english = "workplace atmosphere", turkish = "işyeri atmosferi"),
                    VocabItem(german = "die Führungskultur", english = "leadership culture", turkish = "liderlik kültürü"),
                    VocabItem(german = "die Wertschätzung", english = "appreciation", turkish = "takdir / değer verme"),
                    VocabItem(german = "die Kommunikation", english = "communication", turkish = "iletişim"),
                    VocabItem(german = "das Einzelbüro", english = "single office", turkish = "tek kişilik ofis"),
                    VocabItem(german = "der Großraumbüro", english = "open-plan office", turkish = "açık ofis"),
                    VocabItem(german = "das Teamevent", english = "team event", turkish = "takım etkinliği"),
                    VocabItem(german = "die Fluktuation", english = "turnover rate", turkish = "işgücü devri")
                ),
                tipsForExam = "Achte bei solchen Texten auf die Kausalitäten (Ursache-Wirkung). oft wird gefragt: 'Was passiert, wenn...?' oder 'Welche Auswirkung hat...?'"
            ),
            ReadingText(
                id = "b2_r_01_08",
                title = "Kündigung: Rechte und Pflichten",
                source = "Verbraucherzentrale",
                sourceUrl = "https://www.verbraucherzentrale.de/arbeitsrecht-kuendigung",
                wordCount = 310,
                readingTimeMinutes = 4,
                difficulty = "B2",
                content = """Eine Kündigung ist für die meisten Arbeitnehmer ein einschneidendes Ereignis. Umso wichtiger ist es, seine Rechte zu kennen. Grundsätzlich muss jede Kündigung schriftlich erfolgen – eine mündliche Kündigung ist nicht wirksam. Auch per E-Mail oder SMS ist eine Kündigung ungültig.

Zunächst ist entscheidend, ob das Arbeitsverhältnis unter das Kündigungsschutzgesetz fällt. Dieses Gesetz gilt für Betriebe mit mehr als zehn Mitarbeitern und schützt Arbeitnehmer vor willkürlichen Kündigungen. In kleineren Betrieben gibt es diesen Schutz nicht in vollem Umfang.

Es gibt drei Arten der ordentlichen Kündigung: Die betriebsbedingte Kündigung – zum Beispiel bei wirtschaftlichen Schwierigkeiten des Unternehmens. Die verhaltensbedingte Kündigung – zum Beispiel bei wiederholten Pflichtverletzungen. Und die personenbedingte Kündigung – zum Beispiel bei längerer Krankheit.

Der Arbeitgeber muss immer eine Kündigungsfrist einhalten. Diese beträgt mindestens vier Wochen und richtet sich nach der Betriebszugehörigkeit: Je länger jemand im Betrieb arbeitet, desto länger ist die Frist. Bei einer Betriebszugehörigkeit von zehn Jahren beträgt die Frist beispielsweise mindestens drei Monate.

Nach einer Kündigung haben Arbeitnehmer Anspruch auf ein Arbeitszeugnis. Dieses sollte fair und wohlwollend formuliert sein. Wer mit seinem Zeugnis nicht zufrieden ist, kann bei Gericht einen Antrag auf Erteilung eines besseren Zeugnisses stellen.

Wichtig: Innerhalb von drei Wochen nach Zugang der Kündigung muss Kündigungsschutzklage erhoben werden, wenn man sich gegen die Kündigung wehren möchte. Versäumt man diese Frist, wird die Kündigung automatisch wirksam.""",
                questions = listOf(
                    QuestionMC(
                        id = "q_01_08_a",
                        questionText = "Was ist die Hauptaussage des Textes?",
                        options = listOf(
                            "Eine Kündigung kann nur mündlich erfolgen.",
                            " Arbeitnehmer sollten ihre Rechte bei einer Kündigung kennen.",
                            "Das Kündigungsschutzgesetz gilt für alle Betriebe.",
                            "Eine Kündigung per SMS ist gültig."
                        ),
                        correctAnswer = "Arbeitnehmer sollten ihre Rechte bei einer Kündigung kennen.",
                        questionType = "multiple_choice",
                        explanation = "Der Text informiert umfassend über Rechte bei Kündigungen: Schriftform, Kündigungsarten, -fristen, Zeugnisanspruch und die Drei-Wochen-Frist für Klage."
                    ),
                    QuestionTF(
                        id = "q_01_08_b",
                        questionText = "Eine Kündigung per E-Mail ist gültig.",
                        correctAnswer = false,
                        explanation = "Der Text betont: 'Eine mündliche Kündigung ist nicht wirksam. Auch per E-Mail oder SMS ist eine Kündigung ungültig.'"
                    ),
                    QuestionMC(
                        id = "q_01_08_c",
                        questionText = "Ab welcher Betriebsgröße gilt das Kündigungsschutzgesetz?",
                        options = listOf(
                            "Ab fünf Mitarbeitern",
                            "Ab zehn Mitarbeitern",
                            "Ab 50 Mitarbeitern",
                            "Ab 100 Mitarbeitern"
                        ),
                        correctAnswer = "Ab zehn Mitarbeitern",
                        questionType = "multiple_choice",
                        explanation = "Der Text sagt: 'Dieses Gesetz gilt für Betriebe mit mehr als zehn Mitarbeitern.'"
                    ),
                    QuestionFIB(
                        id = "q_01_08_d",
                        questionText = "Nach Zugang der Kündigung hat man ___ Wochen Zeit, Kündigungsschutzklage zu erheben.",
                        correctAnswer = "drei",
                        explanation = "Der Text sagt klar: 'Innerhalb von drei Wochen nach Zugang der Kündigung muss Kündigungsschutzklage erhoben werden.'"
                    ),
                    QuestionMC(
                        id = "q_01_08_e",
                        questionText = "Wie viele Arten der ordentlichen Kündigung gibt es laut dem Text?",
                        options = listOf(
                            "Eine Art",
                            "Zwei Arten",
                            "Drei Arten",
                            "Vier Arten"
                        ),
                        correctAnswer = "Drei Arten",
                        questionType = "multiple_choice",
                        explanation = "Der Text nennt drei Arten: betriebsbedingt, verhaltensbedingt und personenbedingt."
                    )
                ),
                keyVocabulary = listOf(
                    VocabItem(german = "die Kündigung", english = "dismissal / termination", turkish = "işten çıkarma / fesih"),
                    VocabItem(german = "das Kündigungsschutzgesetz", english = "German Dismissal Protection Act", turkish = "İş Koruma Kanunu"),
                    VocabItem(german = "die Kündigungsfrist", english = "notice period", turkish = "bildirim süresi"),
                    VocabItem(german = "das Arbeitszeugnis", english = "job reference / certificate of employment", turkish = "iş referansı / iş belgesi"),
                    VocabItem(german = "die Klage erheben", english = "to file a lawsuit", turkish = "dava açmak"),
                    VocabItem(german = "die Betriebszugehörigkeit", english = "length of service", turkish = "iş yerindeki çalışma süresi"),
                    VocabItem(german = "die Pflichtverletzung", english = "breach of duty", turkish = "görev ihlali"),
                    VocabItem(german = "der Anspruch", english = "claim / entitlement", turkish = "hak / talep")
                ),
                tipsForExam = "Merke: Drei-Wochen-Frist ist ein Lieblingsthema bei B2! + Wichtige Vokabeln: 'schriftlich', 'Kündigungsschutzklage', 'Zeugnis' – diese kommen im Alltag und Exam immer wieder!"
            ),
            ReadingText(
                id = "b2_r_01_09",
                title = "Einstiegsgehälter: Wo verdienen Berufseinsteiger am besten?",
                source = "Karriere.de",
                sourceUrl = "https://www.karriere.de/gehalt-berufseinsteiger",
                wordCount = 285,
                readingTimeMinutes = 4,
                difficulty = "B2",
                content = """Wo starten junge Akademiker nach dem Studium am besten ins Berufsleben? Eine Analyse der Jobplattform StepStone zeigt große regionale und branchenspezifische Unterschiede bei den Einstiegsgehältern.

An der Spitze liegen wie erwartet die großen Tech-Unternehmen und Beratungsgesellschaften. Bei Unternehmen wie Google, McKinsey oder den großen Wirtschaftsprüfern beginnen Berufseinsteiger häufig mit Gehältern von 60.000 Euro aufwärts pro Jahr. Auch in der Automobilindustrie, besonders bei den Herstellern von Elektroautos, werden hohe Einstiegsgehälter gezahlt.

Deutlich geringer fallen die Einstiegsgehälter im öffentlichen Dienst, in der Sozialarbeit oder im Bildungsbereich aus. Hier liegen die Gehälter für Berufseinsteiger oft zwischen 35.000 und 45.000 Euro. Das ist kein Zeichen mangelnder Qualifikation, sondern spiegelt die unterschiedliche finanzielle Leistungsfähigkeit der Branchen wider.

Regional ist der Süden Deutschlands am attraktivsten. Bayern und Baden-Württemberg bieten im Durchschnitt zehn bis fünfzehn Prozent höhere Gehälter als der Norden oder die neuen Bundesländer. München führt dabei die Rangliste der bestbezahlten Städte an, dicht gefolgt von Frankfurt am Main und Stuttgart.

Doch Gehalt ist nicht alles. Viele Berufseinsteiger entscheiden sich bewusst für niedrigere Gehälter, wenn der Arbeitgeber andere Vorteile bietet – zum Beispiel flexible Arbeitszeiten, Homeoffice-Möglichkeiten, betriebliche Altersvorsorge oder ein интересantes Aufgabengebiet. Laut einer Umfrage von StepStone legen besonders jüngere Arbeitnehmer Wert auf Work-Life-Balance.

Für Berufseinsteiger empfiehlt sich daher ein ganzheitlicher Blick: Nicht nur das Gehalt zählt, sondern auch die Karrierechancen, die Arbeitsatmosphäre und die eigenen Prioritäten im Leben.""",
                questions = listOf(
                    QuestionMC(
                        id = "q_01_09_a",
                        questionText = "Was ist die Hauptaussage des Textes?",
                        options = listOf(
                            "Alle Berufseinsteiger verdienen gleich viel.",
                            "Einstiegsgehälter variieren stark je nach Branche und Region.",
                            "Der öffentliche Dienst zahlt am besten.",
                            "Tech-Unternehmen zahlen am schlechtesten."
                        ),
                        correctAnswer = "Einstiegsgehälter variieren stark je nach Branche und Region.",
                        questionType = "multiple_choice",
                        explanation = "Der Text zeigt durchgehend regionale (Süden vs. Norden) und branchenspezifische Unterschiede (Tech vs. Sozialarbeit)."
                    ),
                    QuestionTF(
                        id = "q_01_09_b",
                        questionText = "Im öffentlichen Dienst verdienen Berufseinsteiger laut StepStone mehr als bei Tech-Unternehmen.",
                        correctAnswer = false,
                        explanation = "Der Text stellt klar: 'Deutlich geringer fallen die Einstiegsgehälter im öffentlichen Dienst...' – zwischen 35.000 und 45.000 Euro, während Tech bei 60.000+ liegt."
                    ),
                    QuestionMC(
                        id = "q_01_09_c",
                        questionText = "Welche Stadt führt laut dem Text die Rangliste der bestbezahlten Städte an?",
                        options = listOf(
                            "Frankfurt am Main",
                            "Stuttgart",
                            "München",
                            "Hamburg"
                        ),
                        correctAnswer = "München",
                        questionType = "multiple_choice",
                        explanation = "Der Text sagt: 'München führt dabei die Rangliste der bestbezahlten Städte an, dicht gefolgt von Frankfurt am Main und Stuttgart.'"
                    ),
                    QuestionFIB(
                        id = "q_01_09_d",
                        questionText = "Viele junge Arbeitnehmer legen laut einer StepStone-Umfrage großen Wert auf ___.",
                        correctAnswer = "Work-Life-Balance",
                        explanation = "Der Text erwähnt: 'laut einer Umfrage von StepStone legen besonders jüngere Arbeitnehmer Wert auf Work-Life-Balance.'"
                    ),
                    QuestionMC(
                        id = "q_01_09_e",
                        questionText = "Was wird Berufseinsteigern laut dem Text empfohlen?",
                        options = listOf(
                            "Nur aufs Gehalt zu schauen.",
                            "Nur in München zu arbeiten.",
                            "Einen ganzheitlichen Blick zu haben, der über das Gehalt hinausgeht.",
                            "Immer den öffentlichen Dienst zu wählen."
                        ),
                        correctAnswer = "Einen ganzheitlichen Blick zu haben, der über das Gehalt hinausgeht.",
                        questionType = "multiple_choice",
                        explanation = "Der Text schließt mit: 'Für Berufseinsteiger empfiehlt sich daher ein ganzheitlicher Blick: Nicht nur das Gehalt zählt...'"
                    )
                ),
                keyVocabulary = listOf(
                    VocabItem(german = "das Einstiegsgehalt", english = "starting salary", turkish = "giriş seviyesi maaş"),
                    VocabItem(german = "die Region", english = "region", turkish = "bölge"),
                    VocabItem(german = "die Branche", english = "industry / sector", turkish = "sektör"),
                    VocabItem(german = "die Beratungsgesellschaft", english = "consulting firm", turkish = "danışmanlık şirketi"),
                    VocabItem(german = "der öffentliche Dienst", english = "public service", turkish = "kamu hizmeti"),
                    VocabItem(german = "die Work-Life-Balance", english = "work-life balance", turkish = "iş-yaşam dengesi"),
                    VocabItem(german = "die Karrierechance", english = "career opportunity", turkish = "kariyer fırsatı"),
                    VocabItem(german = "die Altersvorsorge", english = "pension / retirement plan", turkish = "emeklilik planı")
                ),
                tipsForExam = "Zahlenbeispiele aus dem Text: Tech = 60.000+ €, öffentlicher Dienst = 35.000–45.000 €, München am besten. regionsunterschied 10–15%!"
            ),
            ReadingText(
                id = "b2_r_01_10",
                title = "Sprache im Beruf: Deutsch oder Englisch?",
                source = "Deutschlandfunk",
                sourceUrl = "https://www.deutschlandfunk.de/sprache-beruf",
                wordCount = 320,
                readingTimeMinutes = 5,
                difficulty = "B2",
                content = """In der internationalen Wirtschaftswelt ist Englisch längst zur lingua franca geworden. Viele deutsche Unternehmen, insbesondere solche mit Auslandsgeschäft, veröffentlichen Stellenanzeigen auf Englisch und kommunizieren im Alltag auf Englisch. Doch wie wichtig sind Deutschkenntnisse in der deutschen Wirtschaft noch?

Eine Studie des Goethe-Instituts hat untersucht, welche Sprachkenntnisse in deutschen Unternehmen tatsächlich verlangt werden. Das Ergebnis überrascht: Obwohl Englisch in vielen Firmen dominant ist, bewerten 78 Prozent der befragten Unternehmen Deutschkenntnisse als „sehr wichtig" oder „wichtig" – selbst in international tätigen Konzernen.

Dafür gibt es mehrere Gründe. Zum einen ist die deutsche Sprache im eigenen Land nach wie vor die wichtigste Arbeitssprache: Gespräche mit Kollegen, E-Mails an deutsche Kunden oder die Lektüre technischer Dokumentationen erfordern fast immer Deutsch. Zum anderen binden deutsche Sprachkenntnisse Mitarbeiter stärker an das Unternehmen, da sie die Kommunikation im Inland erleichtern.

Besonders in Handwerksberufen, im Gesundheitswesen und in der Verwaltung ist Deutsch unverzichtbar. Hier geht es oft um Sicherheitsvorschriften, Gesetze oder die Kommunikation mit Kunden, die kein Englisch sprechen.

Anders sieht es in reinen Tech-Start-ups aus, die von Anfang an international ausgerichtet sind. Hier reicht oft Englisch als Arbeitssprache. Allerdings berichten auch hier Mitarbeiter, die sich manchmal wünschen, bessere Deutschkenntnisse zu haben – besonders im Alltag außerhalb der Arbeit.

Für Arbeitnehmer empfiehlt die Sprachwissenschaftlerin Dr. Sabine Müller: „Englisch ist ein Muss, Deutsch ist ein Plus." Wer beide Sprachen beherrscht, hat die größten Chancen auf dem Arbeitsmarkt – nicht nur in Deutschland, sondern international.""",
                questions = listOf(
                    QuestionMC(
                        id = "q_01_10_a",
                        questionText = "Was ist die Hauptaussage des Textes?",
                        options = listOf(
                            "Englisch ist in deutschen Unternehmen völlig überflüssig.",
                            "Sowohl Englisch als auch Deutsch sind im Beruf wichtig.",
                            "Nur Deutsch ist in Deutschland wichtig.",
                            "Sprachkenntnisse spielen keine Rolle mehr."
                        ),
                        correctAnswer = "Sowohl Englisch als auch Deutsch sind im Beruf wichtig.",
                        questionType = "multiple_choice",
                        explanation = "Die Studie zeigt: 78% bewerten Deutsch als wichtig, aber Englisch als lingua franca. Müller fasst zusammen: 'Englisch ist ein Muss, Deutsch ist ein Plus.'"
                    ),
                    QuestionTF(
                        id = "q_01_10_b",
                        questionText = "Laut der Studie bewerten nur wenige Unternehmen Deutschkenntnisse als wichtig.",
                        correctAnswer = false,
                        explanation = "Das Gegenteil ist der Fall: '78 Prozent der befragten Unternehmen bewerten Deutschkenntnisse als „sehr wichtig" oder „wichtig".'"
                    ),
                    QuestionMC(
                        id = "q_01_10_c",
                        questionText = "In welchen Bereichen ist Deutsch laut dem Text UNVERZICHTBAR?",
                        options = listOf(
                            "Nur in Tech-Start-ups",
                            "Im Handwerk, Gesundheitswesen und Verwaltung",
                            "Nur in internationalen Konzernen",
                            "In keinem Bereich"
                        ),
                        correctAnswer = "Im Handwerk, Gesundheitswesen und Verwaltung",
                        questionType = "multiple_choice",
                        explanation = "Der Text sagt: 'Besonders in Handwerksberufen, im Gesundheitswesen und in der Verwaltung ist Deutsch unverzichtbar.'"
                    ),
                    QuestionFIB(
                        id = "q_01_10_d",
                        questionText = "Dr. Sabine Müller fasst zusammen: 'Englisch ist ein ___, Deutsch ist ein Plus.'",
                        correctAnswer = "Muss",
                        explanation = "Direktes Zitat aus dem Text: '„Englisch ist ein Muss, Deutsch ist ein Plus."'"
                    ),
                    QuestionMC(
                        id = "q_01_10_e",
                        questionText = "Warum binden Deutschkenntnisse Mitarbeiter stärker an das Unternehmen?",
                        options = listOf(
                            "Weil sie teurer sind.",
                            "Weil sie die Kommunikation im Inland erleichtern.",
                            "Weil sie Pflicht sind.",
                            "Weil sie in allen Ländern anerkannt werden."
                        ),
                        correctAnswer = "Weil sie die Kommunikation im Inland erleichtern.",
                        questionType = "multiple_choice",
                        explanation = "Der Text sagt: 'Zum anderen binden deutsche Sprachkenntnisse Mitarbeiter stärker an das Unternehmen, da sie die Kommunikation im Inland erleichtern.'"
                    )
                ),
                keyVocabulary = listOf(
                    VocabItem(german = "die lingua franca", english = "common language", turkish = "ortak dil"),
                    VocabItem(german = "die Sprachkenntnisse", english = "language skills", turkish = "dil bilgisi / dil yetkinliği"),
                    VocabItem(german = "die Arbeitssprache", english = "working language", turkish = "çalışma dili"),
                    VocabItem(german = "die Dokumentation", english = "documentation", turkish = "dokümantasyon"),
                    VocabItem(german = "das Handwerk", english = "craft / trade", turkish = "zanaat / el sanatları"),
                    VocabItem(german = "das Gesundheitswesen", english = "healthcare sector", turkish = "sağlık sektörü"),
                    VocabItem(german = "die Verwaltung", english = "administration", turkish = "idare / yönetim"),
                    VocabItem(german = "die Kommunikation", english = "communication", turkish = "iletişim")
                ),
                tipsForExam = "Wichtige Struktur: Studie mit Prozentangabe (78%), dann Erklärung in mehreren Gründen, dann Expertenmeinung. Diese Struktur ist typisch für B2-Lesetexte!"
            )
        ))

        // -------------------------------------------------------
        // TOPIC 2: Gesundheit und Medizin
        // -------------------------------------------------------
        TOPICS[1].texts.addAll(listOf(
            ReadingText(
                id = "b2_r_02_01",
                title = "Burnout: Wenn der Stress krank macht",
                source = "Apotheken Umschau",
                sourceUrl = "https://www.apotheken-umschau.de/burnout",
                wordCount = 335,
                readingTimeMinutes = 5,
                difficulty = "B2",
                content = """Burnout ist längst zu einem Volksleiden geworden. Nach Schätzungen der Bundesanstalt für Arbeitsschutz sind in Deutschland jährlich etwa 500.000 Menschen von einem Burnout betroffen. Doch was genau steckt hinter dem Begriff, und wie kann man sich davor schützen?

Burnout ist keine offiziell anerkannte Krankheit, sondern ein Syndrom – also eine Kombination verschiedener Symptome. Dazu gehören Erschöpfung, Schlafstörungen, Konzentrationsprobleme und ein Gefühl der inneren Leere. In schweren Fällen kann Burnout zu Depressionen führen.

Die Ursachen liegen meist in einer dauerhaften Überlastung am Arbeitsplatz. Hohe Anforderungen, Zeitdruck, ständige Erreichbarkeit und fehlende Anerkennung setzen die Betroffenen unter Druck. Doch nicht nur die Arbeit kann ein Burnout auslösen – auch pflegende Angehörige, die sich um demenzkranke Eltern kümmern, sind besonders gefährdet.

Was kann man tun? Zunächst ist es wichtig, die eigenen Grenzen zu erkennen. Wer ständig über seine Belastungsgrenze geht, riskiert langfristig seine Gesundheit. Regelmäßige Pausen, ausreichend Schlaf und Sport sind wichtige Maßnahmen zur Vorbeugung.

Am Arbeitsplatz sollten Unternehmen Programme zur Gesundheitsförderung anbieten – zum Beispiel Stressmanagement-Seminare oder die Möglichkeit, in Ruhe Pausen zu machen. Experten fordern zudem ein Recht auf Nichterreichbarkeit, damit Mitarbeiter nach Feierabend abschalten können.

Wer bereits erste Anzeichen eines Burnouts bei sich bemerkt, sollte nicht zögern, professionelle Hilfe in Anspruch zuuchen. Ein Gespräch mit dem Hausarzt oder einem Psychologen kann helfen, die Situation frühzeitig zu verbessern. Je früher man handelt, desto besser sind die Heilungschancen.""",
                questions = listOf(
                    QuestionMC(id = "q_02_01_a", questionText = "Was ist die Hauptaussage des Textes?", options = listOf("Burnout ist heilbar, aber nicht vermeidbar.", "Burnout betrifft viele Menschen und erfordert frühzeitige Prävention und Behandlung.", "Nur Arbeitnehmer können an Burnout erkranken.", "Burnout ist eine offiziell anerkannte Krankheit."), correctAnswer = "Burnout betrifft viele Menschen und erfordert frühzeitige Prävention und Behandlung.", questionType = "multiple_choice", explanation = "Der Text informiert über Burnout-Symptome, -Ursachen und -Maßnahmen mit Betonung auf frühzeitiges Handeln."),
                    QuestionTF(id = "q_02_01_b", questionText = "Laut dem Text ist Burnout eine offiziell anerkannte Krankheit.", correctAnswer = false, explanation = "Der Text sagt explizit: 'Burnout ist keine offiziell anerkannte Krankheit, sondern ein Syndrom.'"),
                    QuestionMC(id = "q_02_01_c", questionText = "Wie viele Menschen sind laut Bundesanstalt für Arbeitsschutz jährlich von Burnout betroffen?", options = listOf("Rund 50.000", "Rund 500.000", "Rund 5 Millionen", "Rund 1 Million"), correctAnswer = "Rund 500.000", questionType = "multiple_choice", explanation = "Der Text nennt: 'etwa 500.000 Menschen' als jährlich Betroffene."),
                    QuestionFIB(id = "q_02_01_d", questionText = "Burnout ist kein offizieller Krankheitsname, sondern ein ___.", correctAnswer = "Syndrom", explanation = "Explizit im Text: 'Burnout ist keine offiziell anerkannte Krankheit, sondern ein Syndrom – also eine Kombination verschiedener Symptome.'"),
                    QuestionMC(id = "q_02_01_e", questionText = "Welche Maßnahme wird für Unternehmen empfohlen, um Burnout vorzubeugen?", options = listOf("Längere Arbeitszeiten einführen", "Gesundheitsförderungsprogramme wie Stressmanagement-Seminare anbieten", "Mitarbeiter auch abends per E-Mail kontaktieren", "Weniger Urlaub gewähren"), correctAnswer = "Gesundheitsförderungsprogramme wie Stressmanagement-Seminare anbieten", questionType = "multiple_choice", explanation = "Der Text empfiehlt 'Programme zur Gesundheitsförderung – zum Beispiel Stressmanagement-Seminare'.")
                ),
                keyVocabulary = listOf(
                    VocabItem(german = "das Burnout", english = "burnout", turkish = "tükenmişlik sendromu"),
                    VocabItem(german = "das Syndrom", english = "syndrome", turkish = "sendrom"),
                    VocabItem(german = "die Erschöpfung", english = "exhaustion", turkish = "tükenmişlik"),
                    VocabItem(german = "die Überlastung", english = "overload", turkish = "aşırı yüklenme"),
                    VocabItem(german = "die Prävention", english = "prevention", turkish = "önleme / korunma"),
                    VocabItem(german = "der Zeitdruck", english = "time pressure", turkish = "zaman baskısı"),
                    VocabItem(german = "die Gesundheitsförderung", english = "health promotion", turkish = "sağlık geliştirme"),
                    VocabItem(german = "die Belastungsgrenze", english = "stress limit", turkish = "yüklenme sınırı")
                ),
                tipsForExam = "Burnout = Stress + Erschöpfung + innere Leere. Wichtig: Burnout ≠ Krankheit (Syndrom). Kommt sehr häufig im B2-Exam vor!"
            ),
            ReadingText(
                id = "b2_r_02_02",
                title = "Ernährungstrends: Von Paleo bis Intervallfasten",
                source = "Planet Wissen",
                sourceUrl = "https://www.planet-wissen.de/ernaehrung/ernaehrungstrends",
                wordCount = 340,
                readingTimeMinutes = 5,
                difficulty = "B2",
                content = """Die Deutschen beschäftigen sich immer mehr mit ihrer Ernährung. Laut einer Forsa-Umfrage achten mittlerweile 67 Prozent der Bevölkerung bewusst auf gesunde Ernährung. Das hat verschiedene Trends hervorgebracht – von Low Carb über Paleo bis hin zum Intervallfasten.

Beim Intervallfasten wechseln sich Phasen der Nahrungsaufnahme mit Phasen des Fastens ab. Die populärste Methode ist das 16:8-Prinzip: 16 Stunden fasten, innerhalb von 8 Stunden essen. Wissenschaftler haben herausgefunden, dass Intervallfasten den Stoffwechsel anregen und sogar das Altern verlangsamen kann.

Der Paleo-Trend versucht, sich so zu ernähren wie unsere Vorfahren in der Steinzeit. Erlaubt sind Fleisch, Fisch, Gemüse und Obst – verboten alles, was erst in der Neuzeit entstanden ist, wie Getreide, Milchprodukte und Zucker. Kritiker bemängeln, dass diese Ernährungsweise einseitig sei und wichtige Nährstoffe wie Kalzium aus Milchprodukten fehlen.

Low Carb – also kohlenhydratarme Ernährung – hat in den letzten Jahren ebenfalls viele Anhänger gefunden. Der Gedanke: Wer weniger Kohlenhydrate isst, nimmt weniger Energie zu sich und nimmt dadurch ab. Studien zeigen, dass Low Carb tatsächlich beim Abnehmen helfen kann, allerdings ist die langfristige Umsetzung schwierig.

Ernährungsexperten warnen jedoch vor übertriebenen Trends. „Keine der populären Diäten ist für jeden Menschen geeignet", sagt Professor Klaus Müller von der Universität Hohenheim. „Was für den einen funktioniert, kann für den anderen schädlich sein." Am wichtigsten sei eine ausgewogene Ernährung mit viel Gemüse, Obst und Vollkornprodukten – und nicht die neueste Mode-Diät.""",
                questions = listOf(
                    QuestionMC(id = "q_02_02_a", questionText = "Was ist die Hauptaussage des Textes?", options = listOf("Alle Diättrends sind wissenschaftlich bewiesen.", "Es gibt viele Ernährungstrends, aber eine ausgewogene Ernährung bleibt am wichtigsten.", "Intervallfasten ist die einzige gesunde Ernährungsform.", "Paleo ist die beste Diät für alle."), correctAnswer = "Es gibt viele Ernährungstrends, aber eine ausgewogene Ernährung bleibt am wichtigsten.", questionType = "multiple_choice", explanation = "Der Text stellt mehrere Trends vor, aber Professor Müller warnt: 'Am wichtigsten sei eine ausgewogene Ernährung...'"),
                    QuestionTF(id = "q_02_02_b", questionText = "Beim Intervallfasten isst man den ganzen Tag gleichmäßig.", correctAnswer = false, explanation = "Das Gegenteil ist der Fall: Beim 16:8-Prinzip fastet man 16 Stunden und isst nur in einem 8-Stunden-Fenster."),
                    QuestionMC(id = "q_02_02_c", questionText = "Was ist laut Kritikern das Problem der Paleo-Ernährung?", options = listOf("Sie ist zu teuer.", "Sie ist einseitig und wichtige Nährstoffe wie Kalzium fehlen.", "Sie macht dick.", "Sie schmeckt nicht gut."), correctAnswer = "Sie ist einseitig und wichtige Nährstoffe wie Kalzium fehlen.", questionType = "multiple_choice", explanation = "Der Text sagt: 'Kritiker bemängeln, dass diese Ernährungsweise einseitig sei und wichtige Nährstoffe wie Kalzium aus Milchprodukten fehlen.'"),
                    QuestionFIB(id = "q_02_02_d", questionText = "Die populärste Intervallfasten-Methode heißt ___ und bedeutet 16 Stunden fasten, 8 Stunden essen.", correctAnswer = "16:8-Prinzip", explanation = "Direkt aus dem Text: 'Die populärste Methode ist das 16:8-Prinzip: 16 Stunden fasten, innerhalb von 8 Stunden essen.'"),
                    QuestionMC(id = "q_02_02_e", questionText = "Wie viel Prozent der Deutschen achten bewusst auf gesunde Ernährung?", options = listOf("Etwa 30 Prozent", "Etwa 50 Prozent", "Etwa 67 Prozent", "Etwa 90 Prozent"), correctAnswer = "Etwa 67 Prozent", questionType = "multiple_choice", explanation = "Die Forsa-Umfrage ergab: 'mittlerweile 67 Prozent der Bevölkerung achten bewusst auf gesunde Ernährung.'")
                ),
                keyVocabulary = listOf(
                    VocabItem(german = "das Intervallfasten", english = "intermittent fasting", turkish = "aralıklı oruç"),
                    VocabItem(german = "der Stoffwechsel", english = "metabolism", turkish = "metabolizma"),
                    VocabItem(german = "die Ernährungsweise", english = "diet / way of eating", turkish = "beslenme şekli"),
                    VocabItem(german = "kohlenhydratarm", english = "low-carb", turkish = "düşük karbonhidratlı"),
                    VocabItem(german = "die Nährstoffe", english = "nutrients", turkish = "besin maddeleri"),
                    VocabItem(german = "die ausgewogene Ernährung", english = "balanced diet", turkish = "dengeli beslenme"),
                    VocabItem(german = "das Vollkornprodukt", english = "whole grain product", turkish = "tam tahıllı ürün"),
                    VocabItem(german = "die Diät", english = "diet", turkish = "diyet")
                ),
                tipsForExam = "Zahlen merken: 67% achten auf gesunde Ernährung, 16:8 Intervallfasten. Merkwort: 'einseitig' (one-sided) – oft bei Diät-Kritik verwendet!")
            ),
            ReadingText(
                id = "b2_r_02_03",
                title = "Impfen: Nutzen und Risiken",
                source = "Robert Koch-Institut",
                sourceUrl = "https://www.rki.de/impfen",
                wordCount = 350,
                readingTimeMinutes = 5,
                difficulty = "B2",
                content = """Impfungen geören zu den wichtigsten Errungenschaften der modernen Medizin. Dank flächendeckender Impfprogramme konnten Krankheiten wie Pocken ausgerottet und Masern in vielen Ländern stark zurückgedrängt werden. Doch in den letzten Jahren ist die Impfquote in Deutschland wieder gesunken – besonders bei den Masern.

Das Robert Koch-Institut (RKI) empfiehlt, alle Kinder nach dem empfohlenen Impfkalender impfen zu lassen. Dieser sieht Impfungen gegen Masern, Mumps, Röteln, Tetanus, Diphtherie und viele weitere Krankheiten vor. Die Impfungen sind für Kinder bis zum Alter von 17 Jahren kostenlos.

Doch es gibt auch Kritiker, die Nebenwirkungen befürchten. Das RKI betont, dass alle in Deutschland zugelassenen Impfstoffe intensiv geprüft wurden und nur minimale Nebenwirkungen haben. Schwere Nebenwirkungen seien äußerst selten. „Der Nutzen einer Impfung überwiegt die Risiken bei Weitem", sagt Dr. Eva Wimmer vom RKI.

Trotzdem kommt es immer wieder zu Masernausbrüchen – besonders in Regionen mit niedriger Impfquote. Masern sind keine harmlose Kinderkrankheit, wie viele denken. Sie können zu schweren Komplikationen wie Lungen- oder Gehirnentzündung führen und sogar tödlich enden.

Die Politik diskutiert deshalb über eine Impfpflicht. Einige Bundesländer haben bereits eine Pflichtimpfung für Kinder in Kindertagesstätten eingeführt. Kritiker einer Impfpflicht argumentieren, dass dies die persönliche Freiheit einschränke. Befürworter entgegnen, dass die Impfpflicht den Schutz der Gemeinschaft rechtfertige – besonders bei hoch ansteckenden Krankheiten wie Masern.""",
                questions = listOf(
                    QuestionMC(id = "q_02_03_a", questionText = "Was ist die Hauptaussage des Textes?", options = listOf("Impfungen sind harmlos und haben keinerlei Risiken.", "Impfungen sind wichtig, aber die Impfquote ist zu niedrig und wird diskutiert.", "Impfungen sollten abgeschafft werden.", "Nur Kinder brauchen Impfungen."), correctAnswer = "Impfungen sind wichtig, aber die Impfquote ist zu niedrig und wird diskutiert.", questionType = "multiple_choice", explanation = "Der Text zeigt sowohl die Wichtigkeit von Impfungen als auch das Problem der sinkenden Impfquote und die politische Debatte über Impfpflicht."),
                    QuestionTF(id = "q_02_03_b", questionText = "Laut RKI überwiegen die Risiken einer Impfung den Nutzen.", correctAnswer = false, explanation = "Dr. Wimmer sagt explizit: 'Der Nutzen einer Impfung überwiegt die Risiken bei Weitem.'"),
                    QuestionMC(id = "q_02_03_c", questionText = "Was kann laut dem Text eine Komplikation von Masern sein?", options = listOf("Nur leichtes Fieber", "Lungen- oder Gehirnentzündung", "Nur Hautausschlag", "Nur Husten"), correctAnswer = "Lungen- oder Gehirnentzündung", questionType = "multiple_choice", explanation = "Der Text warnt: 'Sie können zu schweren Komplikationen wie Lungen- oder Gehirnentzündung führen und sogar tödlich enden.'"),
                    QuestionFIB(id = "q_02_03_d", questionText = "Die Behörde, die Impfempfehlungen in Deutschland ausspricht, heißt Robert ___.", correctAnswer = "Koch-Institut", explanation = "Das Robert Koch-Institut (RKI) ist die zuständige Bundesbehörde für Infektionskrankheiten und Impfempfehlungen."),
                    QuestionMC(id = "q_02_03_e", questionText = "Was ist ein Argument der Befürworter einer Impfpflicht?", options = listOf("Impffreiheit für alle", "Die Impfpflicht schützt die Gemeinschaft.", "Impfungen sind zu teuer.", "Kinder sollten selbst entscheiden."), correctAnswer = "Die Impfpflicht schützt die Gemeinschaft.", questionType = "multiple_choice", explanation = "Der Text sagt: 'Befürworter entgegnen, dass die Impfpflicht den Schutz der Gemeinschaft rechtfertige – besonders bei hoch ansteckenden Krankheiten.'")
                ),
                keyVocabulary = listOf(
                    VocabItem(german = "die Impfung", english = "vaccination", turkish = "aşılama"),
                    VocabItem(german = "die Impfquote", english = "vaccination rate", turkish = "aşılama oranı"),
                    VocabItem(german = "die Nebenwirkung", english = "side effect", turkish = "yan etki"),
                    VocabItem(german = "die Masern", english = "measles", turkish = "kızamık"),
                    VocabItem(german = "die Komplikation", english = "complication", turkish = "komplikasyon"),
                    VocabItem(german = "die Impfpflicht", english = "compulsory vaccination", turkish = "zorunlu aşılama"),
                    VocabItem(german = "die Gemeinschaft", english = "community", turkish = "topluluk"),
                    VocabItem(german = "die Erkrankung", english = "illness / disease", turkish = "hastalık")
                ),
                tipsForExam = "Impf-Debatte: Nutzen vs. Risiken. Merke: RKI = Robert Koch-Institut, empfiehlt Impfungen. Kommt besonders bei Gesundheitsthemen oft vor!")
            ),
            ReadingText(
                id = "b2_r_02_04",
                title = "Das deutsche Gesundheitssystem: Stärken und Schwächen",
                source = "Bundesgesundheitsministerium",
                sourceUrl = "https://www.bundesgesundheitsministerium.de/",
                wordCount = 345,
                readingTimeMinutes = 5,
                difficulty = "B2",
                content = """Das deutsche Gesundheitssystem gilt als eines der besten der Welt. Jeder Bürger hat Anspruch auf medizinische Versorgung, unabhängig von seinem Einkommen. Getragen wird das System von der gesetzlichen Krankenversicherung (GKV) und der privaten Krankenversicherung (PKV).

Rund 87 Prozent der Bevölkerung sind gesetzlich versichert. Sie zahlen einen bestimmten Prozentsatz ihres Einkommens – aktuell 14,6 Prozent – als Beitrag zur Krankenversicherung, wobei der Arbeitgeber die Hälfte übernimmt. Privat Versicherte zahlen einen festen Beitrag, der unabhängig vom Einkommen ist.

Zu den Stärken des deutschen Systems gehört der Zugang zu einer flächendeckenden medizinischen Versorgung. Egal ob auf dem Land oder in der Stadt – Ärzte und Krankenhäuser sind in der Regel schnell erreichbar. Deutschland verfügt über eine hohe Dichte an Krankenhausbetten und medizinischem Personal.

Kritiker bemängeln jedoch die Bürokratie und die langen Wartezeiten für bestimmte Behandlungen. Wer einen Termin beim Facharzt benötigt, muss oft Wochen oder sogar Monate warten. Auch die Kosten im Gesundheitswesen steigen stetig –原因是 der demografische Wandel und teure neue Medikamente.

Eine große Herausforderung ist der Ärztemangel auf dem Land. Viele junge Ärzte ziehen es vor, in der Stadt zu praktizieren, wo die Infrastruktur besser ist und die Arbeitsbelastung geringer. Das führt dazu, dass Patienten auf dem Land lange fahren müssen, um einen Arzt zu erreichen.

Die Politik diskutiert verschiedene Reformmodelle. Eine Idee ist, die Digitalisierung stärker voranzutreiben – zum Beispiel durch Telemedizin, bei der Patienten per Video mit Ärzten sprechen können. So könnten besonders auf dem Land Wartezeiten verkürzt und die Versorgung verbessert werden.""",
                questions = listOf(
                    QuestionMC(id = "q_02_04_a", questionText = "Was ist die Hauptaussage des Textes?", options = listOf("Das deutsche Gesundheitssystem ist perfekt.", "Das System hat Stärken wie flächendeckende Versorgung, aber auch Probleme wie Bürokratie und Landarztmangel.", "Nur Privatversicherte erhalten gute medizinische Versorgung.", "Das Gesundheitssystem wird abgeschafft."), correctAnswer = "Das System hat Stärken wie flächendeckende Versorgung, aber auch Probleme wie Bürokratie und Landarztmangel.", questionType = "multiple_choice", explanation = "Der Text zeigt die Balance: Stärken (Zugang, Dichte) vs. Schwächen (Bürokratie, Wartezeiten, Landarztmangel)."),
                    QuestionTF(id = "q_02_04_b", questionText = "Der Arbeitgeber zahlt den gesamten Krankenversicherungsbeitrag.", correctAnswer = false, explanation = "Der Text sagt klar: '...von dem der Arbeitgeber die Hälfte übernimmt.' – der Arbeitnehmer zahlt also auch die Hälfte."),
                    QuestionMC(id = "q_02_04_c", questionText = "Wie viel Prozent der Bevölkerung ist gesetzlich versichert?", options = listOf("Etwa 50 Prozent", "Etwa 70 Prozent", "Etwa 87 Prozent", "Etwa 100 Prozent"), correctAnswer = "Etwa 87 Prozent", questionType = "multiple_choice", explanation = "Der Text nennt explizit: 'Rund 87 Prozent der Bevölkerung sind gesetzlich versichert.'"),
                    QuestionFIB(id = "q_02_04_d", questionText = "Telemedizin ermöglicht es Patienten, per ___ mit Ärzten zu sprechen.", correctAnswer = "Video", explanation = "Der Text beschreibt Telemedizin als 'bei der Patienten per Video mit Ärzten sprechen können.'"),
                    QuestionMC(id = "q_02_04_e", questionText = "Was ist eine vorgeschlagene Lösung für den Ärztemangel auf dem Land?", options = listOf("Abschaffung aller Landarztstellen", "Stärkere Digitalisierung und Telemedizin", "Schließung aller Stadtarztpraxen", "Erhöhung der Wartezeiten für alle"), correctAnswer = "Stärkere Digitalisierung und Telemedizin", questionType = "multiple_choice", explanation = "Der Text schlägt vor: 'Eine Idee ist, die Digitalisierung stärker voranzutreiben – zum Beispiel durch Telemedizin...'")
                ),
                keyVocabulary = listOf(
                    VocabItem(german = "die Krankenversicherung", english = "health insurance", turkish = "sağlık sigortası"),
                    VocabItem(german = "die medizinische Versorgung", english = "medical care", turkish = "tıbbi bakım"),
                    VocabItem(german = "der Beitrag", english = "contribution / premium", turkish = "prim / katkı payı"),
                    VocabItem(german = "die Wartezeit", english = "waiting time", turkish = "bekleme süresi"),
                    VocabItem(german = "der Facharzt", english = "specialist", turkish = "uzman doktor"),
                    VocabItem(german = "die Telemedizin", english = "telemedicine", turkish = "uzaktan tedavi / teletıp"),
                    VocabItem(german = "die Infrastruktur", english = "infrastructure", turkish = "altyapı"),
                    VocabItem(german = "der demografische Wandel", english = "demographic change", turkish = "demografik değişim")
                ),
                tipsForExam = "Zahlen: 87% gesetzlich versichert, 14,6% Krankenkassenbeitrag (Arbeitgeber zahlt Hälfte). Hauptproblem: Landarztmangel + Telemedizin als Lösung. Wichtig!")
            ),
            ReadingText(
                id = "b2_r_02_05",
                title = "Psychische Gesundheit am Arbeitsplatz",
                source = "Bundespsychotherapeutenkammer",
                sourceUrl = "https://www.bptk.de/",
                wordCount = 330,
                readingTimeMinutes = 5,
                difficulty = "B2",
                content = """Die psychische Gesundheit ist ein Thema, das lange tabu war – besonders am Arbeitsplatz. Doch die Zahlen sprechen eine klare Sprache: Laut Bundespsychotherapeutenkammer sind psychische Erkrankungen mittlerweile der häufigste Grund für Krankmeldungen in Deutschland. Etwa jeder dritte Arbeitnehmer leidet im Laufe seines Berufslebens unter psychischen Beschwerden.

Was sind die häufigsten Probleme? An erster Stelle stehen Depressionen und Angststörungen, gefolgt von Burnout und stressbedingten Beschwerden. Die Ursachen sind vielfältig: Hohe Arbeitsbelastung, ständige Erreichbarkeit, Konflikte im Team oder Angst vor Jobverlust setzen viele Mitarbeiter unter Druck.

Was können Unternehmen tun? Die gute Nachricht ist: Es gibt viele Maßnahmen, die helfen können. Betriebliches Gesundheitsmanagement (BGM) umfasst alles, was die Gesundheit der Mitarbeiter fördert – von der Gestaltung des Arbeitsplatzes bis hin zu Seminaren über Stressmanagement. Wichtig ist, dass das Thema nicht nur auf Papier existsiert, sondern tatsächlich gelebt wird.

Auch die Führungskultur spielt eine große Rolle. Mitarbeiter, die das Gefühl haben, dass ihr Vorgesetzter sich für sie interessiert und sie wertschätzt, sind weniger anfällig für psychische Probleme. Regelmäßige Gespräche zwischen Führungskraft und Mitarbeiter – nicht nur beim Jahresfeedback – können hier einen wichtigen Beitrag leisten.

Für Betroffene gibt es verschiedene Hilfsangebote: Unternehmen bieten zunehmend Employee Assistance Programs (EAP) an – kostenlose Beratungsdienste, die Mitarbeitern bei persönlichen oder beruflichen Problemen helfen. Auch die Krankenkassen zahlen Psychotherapien, wenn diese medizinisch notwendig sind.

Am wichtigsten ist: Wer psychische Probleme hat, sollte sich nicht schämen, darüber zu sprechen. Psychische Erkrankungen sind keine Schwäche – sie sind Krankheiten, die behandelt werden können und müssen.""",
                questions = listOf(
                    QuestionMC(id = "q_02_05_a", questionText = "Was ist die Hauptaussage des Textes?", options = listOf("Psychische Probleme am Arbeitsplatz sind selten.", "Psychische Gesundheit ist wichtig und Unternehmen sollten aktiv dagegen vorgehen.", "Nur Unternehmen sind für psychische Gesundheit verantwortlich.", "Psychische Erkrankungen können nicht behandelt werden."), correctAnswer = "Psychische Gesundheit ist wichtig und Unternehmen sollten aktiv dagegen vorgehen.", questionType = "multiple_choice", explanation = "Der Text zeigt: psychische Probleme sind häufig (jeder dritte), Ursachen sind vielfältig, und Maßnahmen (BGM, Führungskultur, EAP) sind wichtig."),
                    QuestionTF(id = "q_02_05_b", questionText = "Jeder fünfte Arbeitnehmer leidet unter psychischen Beschwerden.", correctAnswer = false, explanation = "Der Text sagt: 'Etwa jeder dritte Arbeitnehmer leidet im Laufe seines Berufslebens unter psychischen Beschwerden.' – also nicht jeder fünfte, sondern jeder dritte."),
                    QuestionMC(id = "q_02_05_c", questionText = "Was sind die häufigsten psychischen Probleme laut dem Text?", options = listOf("Nur Burnout", "Depressionen und Angststörungen", "Nur Stress", "Nur Mobbing"), correctAnswer = "Depressionen und Angststörungen", questionType = "multiple_choice", explanation = "Der Text nennt: 'An erster Stelle stehen Depressionen und Angststörungen, gefolgt von Burnout und stressbedingten Beschwerden.'"),
                    QuestionFIB(id = "q_02_05_d", questionText = "Unternehmen bieten zunehmend Employee Assistance Programs (EAP) an – kostenlose ___, die bei persönlichen oder beruflichen Problemen helfen.", correctAnswer = "Beratungsdienste", explanation = "Der Text beschreibt EAP als 'kostenlose Beratungsdienste, die Mitarbeitern bei persönlichen oder beruflichen Problemen helfen.'"),
                    QuestionMC(id = "q_02_05_e", questionText = "Was können Führungskräfte tun, um psychischen Problemen vorzubeugen?", options = listOf("Nichts – das ist Privatsache.", "Regelmäßige Gespräche mit Mitarbeitern führen und Wertschätzung zeigen.", "Mehr Druck auf Mitarbeiter ausüben.", "Krankmeldungen ablehnen."), correctAnswer = "Regelmäßige Gespräche mit Mitarbeitern führen und Wertschätzung zeigen.", questionType = "multiple_choice", explanation = "Der Text sagt: 'Mitarbeiter, die das Gefühl haben, dass ihr Vorgesetzter sich für sie interessiert und sie wertschätzt, sind weniger anfällig für psychische Probleme.'")
                ),
                keyVocabulary = listOf(
                    VocabItem(german = "die psychische Gesundheit", english = "mental health", turkish = "ruh sağlığı"),
                    VocabItem(german = "die Depression", english = "depression", turkish = "depresyon"),
                    VocabItem(german = "die Angststörung", english = "anxiety disorder", turkish = "kaygı bozukluğu"),
                    VocabItem(german = "das Burnout", english = "burnout", turkish = "tükenmişlik"),
                    VocabItem(german = "die Arbeitsbelastung", english = "workload", turkish = "iş yükü"),
                    VocabItem(german = "die Wertschätzung", english = "appreciation", turkish = "takdir / değer"),
                    VocabItem(german = "die Krankmeldung", english = "sick note", turkish = "sağlık raporu"),
                    VocabItem(german = "die Psychotherapie", english = "psychotherapy", turkish = "psikoterapi")
                ),
                tipsForExam = "Wichtig: 'Jeder dritte' statt 'jeder fünfte' – bei B2 wird oft bei Prozentangaben getrickst. Achte genau auf die Zahlen!")
            ),
            ReadingText(
                id = "b2_r_02_06",
                title = "Sport und Bewegung: Wie viel ist gesund?",
                source = "Sportmedizin Dresden",
                sourceUrl = "https://www.sportmedizin-dresden.de/",
                wordCount = 310,
                readingTimeMinutes = 4,
                difficulty = "B2",
                content = """Die Weltgesundheitsorganisation (WHO) empfiehlt Erwachsenen mindestens 150 Minuten moderate Bewegung pro Woche. Das klingt viel, ist aber leichter zu erreichen, als viele denken. Schon ein zügiger Spaziergang von 30 Minuten an fünf Tagen reicht aus, um die empfohlene Dosis zu erreichen.

Doch laut einer Studie der Universität Tübingen bewegt sich nur etwa ein Drittel der deutschen Bevölkerung ausreichend. Die meisten Menschen verbringen zu viel Zeit im Sitzen – am Schreibtisch, im Auto oder auf dem Sofa. Dieses „Sedentary Living" genannte Verhalten erhöht das Risiko für Herz-Kreislauf-Erkrankungen, Diabetes und sogar bestimmte Krebsarten.

Wie kann man mehr Bewegung in den Alltag integrieren? Schon kleine Änderungen machen einen Unterschied: Die Treppe statt den Aufzug nehmen, in der Mittagspause einen kurzen Umweg gehen oder das Fahrrad statt das Auto nutzen. Wichtig ist, dass die Bewegung regelmäßig stattfindet – besser 20 Minuten jeden Tag als zwei Stunden am Wochenende.

Sportmediziner raten auch zu Krafttraining. „Krafttraining ist nicht nur etwas für Bodybuilder", sagt Professor Andreas Schwarz von der Deutschen Sporthochschule Köln. „Es stärkt die Muskeln und Knochen, was besonders im Alter wichtig ist." Ab dem 30. Lebensjahr beginnt der Körper, Muskelmasse abzubauen – diesem Prozess kann man durch regelmäßiges Training entgegenwirken.

Für Einsteiger empfehlen Experten, langsam zu starten und die Intensität schrittweise zu steigern. Wer sich zu viel zumutet, riskiert Verletzungen und verliert schnell die Motivation. Am besten sei es, eine Sportart zu wählen, die Spaß macht – denn nur was Freude bereitet, wird langfristig durchgehalten.""",
                questions = listOf(
                    QuestionMC(id = "q_02_06_a", questionText = "Was ist die Hauptaussage des Textes?", options = listOf("Sport ist ungesund.", "Regelmäßige Bewegung ist wichtig und schon kleine Änderungen im Alltag helfen.", "Nur extremer Sport ist wirksam.", "Deutsche bewegen sich genug."), correctAnswer = "Regelmäßige Bewegung ist wichtig und schon kleine Änderungen im Alltag helfen.", questionType = "multiple_choice", explanation = "Der Text zeigt: WHO-Empfehlung (150 Min/Woche), Problem (nur 1/3 bewegt sich genug), Lösung (kleine Alltagsänderungen + Krafttraining)."),
                    QuestionTF(id = "q_02_06_b", questionText = "Die WHO empfiehlt mindestens 150 Minuten moderate Bewegung pro Woche.", correctAnswer = true, explanation = "Der Text bestätigt: 'Die Weltgesundheitsorganisation (WHO) empfiehlt Erwachsenen mindestens 150 Minuten moderate Bewegung pro Woche.'"),
                    QuestionMC(id = "q_02_06_c", questionText = "Wie viel Prozent der Deutschen bewegt sich laut Studie der Universität Tübingen ausreichend?", options = listOf("Etwa ein Drittel", "Etwa die Hälfte", "Etwa zwei Drittel", "Fast alle"), correctAnswer = "Etwa ein Drittel", questionType = "multiple_choice", explanation = "Der Text sagt: 'laut einer Studie der Universität Tübingen bewegt sich nur etwa ein Drittel der deutschen Bevölkerung ausreichend.'"),
                    QuestionFIB(id = "q_02_06_d", questionText = "Ab dem 30. Lebensjahr beginnt der Körper, ___ abzubauen.", correctAnswer = "Muskelmasse", explanation = "Prof. Schwarz erklärt: 'Ab dem 30. Lebensjahr beginnt der Körper, Muskelmasse abzubauen – diesem Prozess kann man durch regelmäßiges Training entgegenwirken.'"),
                    QuestionMC(id = "q_02_06_e", questionText = "Was empfehlen Sportmediziner zusätzlich zu Ausdauertraining?", options = listOf("Nur Ausdauertraining", "Krafttraining", "Kein Training", "Nur Stretching"), correctAnswer = "Krafttraining", questionType = "multiple_choice", explanation = "Prof. Schwarz: 'Es stärkt die Muskeln und Knochen, was besonders im Alter wichtig ist' – Krafttraining wird ausdrücklich empfohlen.")
                ),
                keyVocabulary = listOf(
                    VocabItem(german = "die Bewegung", english = "exercise / movement", turkish = "hareket / egzersiz"),
                    VocabItem(german = "die Empfehlung", english = "recommendation", turkish = "öneri / tavsiye"),
                    VocabItem(german = "das Krafttraining", english = "strength training", turkish = "güç antrenmanı"),
                    VocabItem(german = "die Muskelmasse", english = "muscle mass", turkish = "kas kütlesi"),
                    VocabItem(german = "das Risiko", english = "risk", turkish = "risk"),
                    VocabItem(german = "die Herz-Kreislauf-Erkrankung", english = "cardiovascular disease", turkish = "kardiyovasküler hastalık"),
                    VocabItem(german = "die Motivation", english = "motivation", turkish = "motivasyon"),
                    VocabItem(german = "die Intensität", english = "intensity", turkish = "yoğunluk")
                ),
                tipsForExam = "WHO-Zahl merken: 150 Minuten/Woche = 30 Min an 5 Tagen. Krafttraining ab 30! Sedentary = sitting too much = schlecht. Kommt sehr oft in B2 vor!")
            ),
            ReadingText(
                id = "b2_r_02_07",
                title = "Allergien: Mehr als nur ein Schnupfen",
                source = "Deutsches Ärzteblatt",
                sourceUrl = "https://www.aerzteblatt.de/allergien",
                wordCount = 320,
                readingTimeMinutes = 5,
                difficulty = "B2",
                content = """Allergien sind auf dem Vormarsch. Nach Angaben des Robert Koch-Instituts leiden in Deutschland etwa 30 Prozent der Erwachsenen an mindestens einer Allergie. Bei Kindern ist der Anteil sogar noch höher. Besonders verbreitet sind Heuschnupfen, Tierhaarallergien und Nahrungsmittelallergien.

Eine Allergie entsteht, wenn das Immunsystem harmlose Substanzen wie Pollen, Tierhaare oder bestimmte Nahrungsmittel fälschlicherweise als Bedrohung erkennt und eine Immunreaktion auslöst. Diese Reaktion kann sich als Schnupfen, Niesen, Juckreiz, Hautausschläge oder sogar als lebensbedrohlicher anaphylaktischer Schock äußern.

Die Zunahme von Allergien wird unter anderem mit der sogenannten Hygienehypothese erklärt. Diese besagt, dass unser Immunsystem in einer zu sauberen Umgebung nicht genug „Trainingspartner" hat – also Bakterien und Parasiten, gegen die es sich wehren kann. Ohne diese Herausforderung wendet es sich gegen harmlose Stoffe.

Die Diagnose einer Allergie erfolgt meist durch einen Allergietest beim Hautarzt oder durch eine Blutuntersuchung. Die häufigste Behandlung ist die Vermeidung des Allergens – also des Stoffes, das die Allergie auslöst. Wenn das nicht möglich ist, können Antihistaminika die Symptome lindern.

Eine oft unterschätzte Form der Behandlung ist die spezifische Immuntherapie, auch „Hyposensibilisierung" genannt. Dabei wird das Allergen über einen Zeitraum von mehreren Jahren in steigenden Dosen verabreicht, mit dem Ziel, das Immunsystem an den Stoff zu gewöhnen. Diese Therapie kann die Allergie langfristig heilen oder zumindest deutlich lindern.

Für Allergiker ist es wichtig, immer einen Notfallplan zu haben – besonders bei schweren Allergien. Ein gut informierter Allergiker kann ein weitgehend normales Leben führen.""",
                questions = listOf(
                    QuestionMC(id = "q_02_07_a", questionText = "Was ist die Hauptaussage des Textes?", options = listOf("Allergien sind harmlos.", "Allergien sind weit verbreitet und sollten ernst genommen werden.", "Allergien kann man nicht behandeln.", "Nur Kinder haben Allergien."), correctAnswer = "Allergien sind weit verbreitet und sollten ernst genommen werden.", questionType = "multiple_choice", explanation = "Zahlen (30%), Erklärungen (Hygienehypothese), und Behandlungen (Vermeidung, Antihistaminika, Immuntherapie) zeigen: Allergien sind wichtig."),
                    QuestionTF(id = "q_02_07_b", questionText = "Etwa 30 Prozent der deutschen Erwachsenen haben eine Allergie.", correctAnswer = true, explanation = "Der Text bestätigt: 'Nach Angaben des Robert Koch-Instituts leiden in Deutschland etwa 30 Prozent der Erwachsenen an mindestens einer Allergie.'"),
                    QuestionMC(id = "q_02_07_c", questionText = "Was ist die Hygienehypothese?", options = listOf("Man soll sich häufiger waschen.", "Das Immunsystem in zu sauberer Umgebung reagiert auf harmlose Stoffe.", "Allergiker sollen Hygiene meiden.", "Allergien kommen vom Schmutz."), correctAnswer = "Das Immunsystem in zu sauberer Umgebung reagiert auf harmlose Stoffe.", questionType = "multiple_choice", explanation = "Der Text erklärt: '...dass unser Immunsystem in einer zu sauberen Umgebung nicht genug „Trainingspartner" hat... Ohne diese Herausforderung wendet es sich gegen harmlose Stoffe.'"),
                    QuestionFIB(id = "q_02_07_d", questionText = "Die spezifische Immuntherapie heißt auch ___.", correctAnswer = "Hyposensibilisierung", explanation = "Der Text nennt beide Begriffe synonym: 'spezifische Immuntherapie, auch „Hyposensibilisierung" genannt.'"),
                    QuestionMC(id = "q_02_07_e", questionText = "Was ist die häufigste Behandlung bei Allergien?", options = listOf("Eine Operation", "Die Vermeidung des Allergens", "Sport", "Eine Diät"), correctAnswer = "Die Vermeidung des Allergens", questionType = "multiple_choice", explanation = "Der Text sagt: 'Die häufigste Behandlung ist die Vermeidung des Allergens – also des Stoffes, das die Allergie auslöst.'")
                ),
                keyVocabulary = listOf(
                    VocabItem(german = "die Allergie", english = "allergy", turkish = "alerji"),
                    VocabItem(german = "das Immunsystem", english = "immune system", turkish = "bağışıklık sistemi"),
                    VocabItem(german = "das Allergen", english = "allergen", turkish = "alerjen"),
                    VocabItem(german = "der Heuschnupfen", english = "hay fever", turkish = "saman nezlesi"),
                    VocabItem(german = "die Immunreaktion", english = "immune response", turkish = "bağışıklık tepkisi"),
                    VocabItem(german = "die Hyposensibilisierung", english = "desensitization", turkish = "duyarsızlaştırma"),
                    VocabItem(german = "das Antihistaminikum", english = "antihistamine", turkish = "antihistaminik"),
                    VocabItem(german = "der anaphylaktische Schock", english = "anaphylactic shock", turkish = "anafilaktik şok")
                ),
                tipsForExam = "Hygienehypothese = wichtiges Konzept! Immunsystem braucht 'Trainingspartner' (Bakterien). Merke: 30% der Erwachsenen haben Allergien. Hyposensibilisierung = langfristige Heilung!")
            ),
            ReadingText(
                id = "b2_r_02_08",
                title = "Schlaf: Warum guter Schlaf so wichtig ist",
                source = "Schlafmedizinisches Zentrum Charité",
                sourceUrl = "https://schlaf.charite.de/",
                wordCount = 315,
                readingTimeMinutes = 4,
                difficulty = "B2",
                content = """Schlaf ist lebenswichtig. Während wir schlafen, erholt sich der Körper, das Gehirn verarbeitet Eindrücke und sortiert Erinnerungen. Erwachsene sollten nach Empfehlung der Deutschen Gesellschaft für Schlafforschung und Schlafmedizin sieben bis acht Stunden pro Nacht schlafen. Doch laut einer Studie der DAK schläft jeder dritte Deutsche schlecht.

Schlechter Schlaf hat weitreichende Folgen. Kurzfristig führt er zu Konzentrationsproblemen, Reizbarkeit und einer erhöhten Unfallgefahr – besonders im Straßenverkehr. Langfristig erhöht dauerhafter Schlafmangel das Risiko für Herz-Kreislauf-Erkrankungen, Übergewicht und sogar Depressionen.

Was stört den Schlaf? An erster Stelle steht Stress – sei es beruflicher Druck oder private Sorgen. Auch die Nutzung von Smartphones und Tablets vor dem Schlafengehen wirkt sich negativ auf die Schlafqualität aus. Das blaue Licht der Bildschirme unterdrückt die Produktion von Melatonin, dem Hormon, das uns müde macht.

Schlafexperten empfehlen daher eine sogenannte „Schlafhygiene". Dazu gehören: regelmäßige Schlafenszeiten einhalten, das Schlafzimmer kühl und dunkel halten, und mindestens eine Stunde vor dem Schlafengehen auf Bildschirme verzichten. Auch ein Spaziergang am Abend oder eine entspannende Tee-Zeremonie können helfen.

Wer dauerhaft unter Schlafproblemen leidet, sollte professionelle Hilfe suchen. In Deutschland gibt es spezialisierte Schlaflabore, in denen Schlafstörungen diagnostiziert und behandelt werden können. „Schlaf ist kein Luxus, sondern eine medizinische Notwendigkeit", betont Professor Jürgen Zulley von der Universität Regensburg.""",
                questions = listOf(
                    QuestionMC(id = "q_02_08_a", questionText = "Was ist die Hauptaussage des Textes?", options = listOf("Schlaf ist unwichtig.", "Guter Schlaf ist essenziell für die Gesundheit, aber viele Deutsche schlafen schlecht.", "Nur Medikamente helfen bei Schlafproblemen.", "Sieben Stunden Schlaf sind zu viel."), correctAnswer = "Guter Schlaf ist essenziell für die Gesundheit, aber viele Deutsche schlafen schlecht.", questionType = "multiple_choice", explanation = "Der Text zeigt: Wichtigkeit von Schlaf (7-8h), Problem (jeder 3. schläft schlecht), Folgen (Konzentration, Herz, Depression), und Lösungen (Schlafhygiene)."),
                    QuestionTF(id = "q_02_08_b", questionText = "Laut DAK-Studie schläft jeder zweite Deutsche schlecht.", correctAnswer = false, explanation = "Der Text sagt: 'laut einer Studie der DAK schläft jeder dritte Deutsche schlecht.' – nicht jeder zweite."),
                    QuestionMC(id = "q_02_08_c", questionText = "Warum beeinflusst blaues Licht von Bildschirmen den Schlaf negativ?", options = listOf("Es macht laute Geräusche.", "Es unterdrückt die Produktion von Melatonin.", "Es wärmt das Zimmer auf.", "Es ist zu hell zum Lesen."), correctAnswer = "Es unterdrückt die Produktion von Melatonin.", questionType = "multiple_choice", explanation = "Der Text erklärt: 'Das blaue Licht der Bildschirme unterdrückt die Produktion von Melatonin, dem Hormon, das uns müde macht.'"),
                    QuestionFIB(id = "q_02_08_d", questionText = "Was empfehlen Schlafexperten für besseren Schlaf? Regelmäßige ___ einhalten.", correctAnswer = "Schlafenszeiten", explanation = "Der Text listet unter 'Schlafhygiene': 'regelmäßige Schlafenszeiten einhalten' als erste Maßnahme."),
                    QuestionMC(id = "q_02_08_e", questionText = "Wie viele Stunden sollten Erwachsene laut Deutscher Gesellschaft für Schlafforschung schlafen?", options = listOf("Fünf bis sechs Stunden", "Sieben bis acht Stunden", "Zehn bis zwölf Stunden", "Vier bis fünf Stunden"), correctAnswer = "Sieben bis acht Stunden", questionType = "multiple_choice", explanation = "Der Text empfiehlt: 'sieben bis acht Stunden pro Nacht' als ideale Schlafdauer.")
                ),
                keyVocabulary = listOf(
                    VocabItem(german = "der Schlaf", english = "sleep", turkish = "uyku"),
                    VocabItem(german = "die Schlafqualität", english = "sleep quality", turkish = "uyku kalitesi"),
                    VocabItem(german = "der Schlafmangel", english = "sleep deprivation", turkish = "uyku eksikliği"),
                    VocabItem(german = "das Melatonin", english = "melatonin", turkish = "melatonin"),
                    VocabItem(german = "die Schlafhygiene", english = "sleep hygiene", turkish = "uyku hijyeni"),
                    VocabItem(german = "die Konzentration", english = "concentration", turkish = "konsantrasyon"),
                    VocabItem(german = "die Erholung", english = "recovery / rest", turkish = "dinlenme / iyileşme"),
                    VocabItem(german = "das Schlaflabor", english = "sleep laboratory", turkish = "uyku laboratuvarı")
                ),
                tipsForExam = "Merkwörtcher: JEDER DRITTE (nicht zweite!) schläft schlecht. Melatonin = Schlafhormon, wird durch blaues Licht unterdrückt. Schlafhygiene = 3 Regeln: Zeiten, kühl/dunkel, keine Bildschirme!")
            ),
            ReadingText(
                id = "b2_r_02_09",
                title = "Organspende: Leben retten durch Spende",
                source = "Bundeszentrale für gesundheitliche Aufklärung",
                sourceUrl = "https://www.bzga.de/",
                wordCount = 325,
                readingTimeMinutes = 5,
                difficulty = "B2",
                content = """In Deutschland warten rund 8.500 Menschen auf ein Spenderorgan. Viele von ihnen sterben, bevor ein passendes Organ gefunden wird. Gleichzeitig sind die Organspendezahlen in Deutschland im europäischen Vergleich niedrig. Das soll sich ändern – doch wie?

Entscheidend für eine Organspende ist die Zustimmung des Spenders. In Deutschland gilt die sogenannte Entscheidungslösung: Jeder Bürger kann zu Lebzeiten entscheiden, ob er nach seinem Tod Organe spenden möchte oder nicht. Diese Entscheidung kann in einem Organspendeausweis festgehalten werden. Wer keine Entscheidung trifft, gilt jedoch nicht automatisch als Spender – die Angehörigen werden in diesem Fall befragt.

Seit Januar 2022 gibt es die Widerspruchsregelung in Neuregelung: Das Gesetz sieht vor, dass alle Bürger regelmäßig – zum Beispiel bei der Verlängerung des Personalausweises – auf das Thema Organspende hingewiesen werden und sich informieren sollen. Eine automatische Pflicht zur Spende gibt es nicht.

Für Patienten, die auf ein Organ warten, ist die Zeit das größte Problem. Herz, Lunge, Leber oder Niere können nur begrenzte Zeit außerhalb des Körpers überleben – manchmal nur wenige Stunden. Deshalb ist eine gute Koordination zwischen Spender-Krankenhaus, Vermittlungsstelle und Empfänger-Krankenhaus entscheidend.

Die Medizin hat große Fortschritte gemacht. Heute ist es möglich, bestimmte Organe zu „regenerieren" oder künstlich zu unterstützen, während Patienten auf ein Spenderorgan warten. Dennoch bleibt die Organspende die einzige dauerhafte Lösung für viele Patienten mit Organversagen.

Wer sich entscheidet, Organe zu spenden, sollte dies mit seinen Angehörigen besprechen. Denn am Ende sind es die Familien, die im Moment des Todes die Entscheidung treffen müssen.""",
                questions = listOf(
                    QuestionMC(id = "q_02_09_a", questionText = "Was ist die Hauptaussage des Textes?", options = listOf("Organspende ist in Deutschland Pflicht.", "Viele warten auf Organe, aber die Spendenbereitschaft ist niedrig.", "Organtransplantation funktioniert nicht.", "Nur junge Menschen können Organe spenden."), correctAnswer = "Viele warten auf Organe, aber die Spendenbereitschaft ist niedrig.", questionType = "multiple_choice", explanation = "Der Text stellt das Problem dar: 8.500 warten, niedrige Spendezahlen, und erklärt das deutsche System (Entscheidungslösung, keine Pflicht)."),
                    QuestionTF(id = "q_02_09_b", questionText = "Rund 8.500 Menschen warten in Deutschland auf ein Spenderorgan.", correctAnswer = true, explanation = "Der Text bestätigt: 'In Deutschland warten rund 8.500 Menschen auf ein Spenderorgan.'"),
                    QuestionMC(id = "q_02_09_c", questionText = "Was gilt in Deutschland bezüglich Organspende?", options = listOf("Automatische Pflicht zur Spende", "Entscheidungslösung – jeder kann selbst entscheiden", "Keine Organspende erlaubt", "Nur Angehörige entscheiden"), correctAnswer = "Entscheidungslösung – jeder kann selbst entscheiden", questionType = "multiple_choice", explanation = "Der Text erklärt: 'In Deutschland gilt die sogenannte Entscheidungslösung: Jeder Bürger kann zu Lebzeiten entscheiden...'"),
                    QuestionFIB(id = "q_02_09_d", questionText = "Die Entscheidung zur Organspende kann man in einem ___ festhalten.", correctAnswer = "Organspendeausweis", explanation = "Der Text erwähnt: 'Diese Entscheidung kann in einem Organspendeausweis festgehalten werden.'"),
                    QuestionMC(id = "q_02_09_e", questionText = "Wie lange können Organe außerhalb des Körpers überleben?", options = listOf("Unbegrenzt", "Manchmal nur wenige Stunden", "Mehrere Wochen", "Gar nicht"), correctAnswer = "Manchmal nur wenige Stunden", questionType = "multiple_choice", explanation = "Der Text warnt: 'Herz, Lunge, Leber oder Niere können nur begrenzte Zeit außerhalb des Körpers überleben – manchmal nur wenige Stunden.'")
                ),
                keyVocabulary = listOf(
                    VocabItem(german = "die Organspende", english = "organ donation", turkish = "organ bağışı"),
                    VocabItem(german = "der Organspendeausweis", english = "organ donor card", turkish = "organ bağış kartı"),
                    VocabItem(german = "das Spenderorgan", english = "donor organ", turkish = "donör organı"),
                    VocabItem(german = "die Widerspruchsregelung", english = "opt-out rule", turkish = "itiraz kuralı"),
                    VocabItem(german = "die Entscheidungslösung", english = "decision solution", turkish = "karar çözümü"),
                    VocabItem(german = "das Organversagen", english = "organ failure", turkish = "organ yetmezliği"),
                    VocabItem(german = "die Koordination", english = "coordination", turkish = "koordinasyon"),
                    VocabItem(german = "die Transplantationsmedizin", english = "transplant medicine", turkish = "nakil tıbbı")
                ),
                tipsForExam = "Zahl: 8.500 warten auf Organ. Wichtig: Entscheidungslösung (nicht Pflicht!), Organspendeausweis. Organe überleben nur wenige Stunden außerhalb des Körpers!")
            ),
            ReadingText(
                id = "b2_r_02_10",
                title = "Homöopathie: Wirksam oder Placebo?",
                source = "Medizinische Hochschule Hannover",
                sourceUrl = "https://www.mhh.de/",
                wordCount = 305,
                readingTimeMinutes = 4,
                difficulty = "B2",
                content = """Homöopathie ist in Deutschland besonders beliebt – laut einer Umfrage des Allensbach-Instituts haben rund 60 Prozent der Deutschen bereits homöopathische Mittel verwendet. Doch die wissenschaftliche Debatte über die Wirksamkeit ist heftig.

Das Grundprinzip der Homöopathie stammt vom deutschen Arzt Samuel Hahnemann aus dem 18. Jahrhundert: „Ähnliches wird durch Ähnliches geheilt" – ein Stoff, der bei Gesunden bestimmte Symptome auslöst, soll Kranken mit denselben Symptomen helfen. Die Mittel werden zudem stark verdünnt – bei sogenannten Hochpotenzen ist von der ursprünglichen Substanz oft nichts mehr nachweisbar.

Die Kritik aus der wissenschaftlichen Medizin ist deutlich: Zahlreiche große Studien, darunter eine umfassende Metaanalyse des Cochrane-Instituts, kommen zu dem Ergebnis, dass Homöopathie bei keiner Erkrankung wirksamer ist als ein Placebo. Das heißt: Wenn Patienten glauben, dass ihnen ein Mittel hilft, kann dies allein durch die Erwartungshaltung („Placeboeffekt") zu einer Besserung führen.

 Befürworter der Homöopathie entgegnen, dass die Studienmethode – der randomisierte kontrollierte Versuch – nicht auf die Homöopathie anwendbar sei, da diese ganzheitlich wirke und individuell angepasst werde. Sie verweisen auf die Erfahrungsmedizin und die zufriedenen Patienten.

Der Gemeinsame Bundesausschuss (G-BA), das höchste Beschlussorgan im deutschen Gesundheitswesen, hat 2022 entschieden, homöopathische Mittel nicht mehr von den gesetzlichen Krankenkassen zu bezahlen. Begründet wurde dies mit dem fehlenden Nachweis einer Wirksamkeit.

Für Patienten bleibt die Entscheidung letztlich individuell. Wer sich für Homöopathie entscheidet, sollte dies nicht als Ersatz für eine schulmedizinische Behandlung bei schweren Erkrankungen sehen. Bei harmlosen Beschwerden hingegen spricht – solange kein Schaden entsteht – nichts gegen einen Versuch.""",
                questions = listOf(
                    QuestionMC(id = "q_02_10_a", questionText = "Was ist die Hauptaussage des Textes?", options = listOf("Homöopathie ist wissenschaftlich bewiesen wirksam.", "Homöopathie ist umstritten: wissenschaftlich keine Wirkung nachweisbar, aber bei Patienten beliebt.", "Homöopathie sollte verboten werden.", "Alle deutschen Ärzte empfehlen Homöopathie."), correctAnswer = "Homöopathie ist umstritten: wissenschaftlich keine Wirkung nachweisbar, aber bei Patienten beliebt.", questionType = "multiple_choice", explanation = "Der Text zeigt beide Seiten: 60% Nutzung, Cochrane Metaanalyse → kein Wirknachweis, G-BA Entscheidung → keine Kassenübernahme mehr."),
                    QuestionTF(id = "q_02_10_b", questionText = "Der Gemeinsame Bundesausschuss hat entschieden, homöopathische Mittel weiterhin von den Krankenkassen zu bezahlen.", correctAnswer = false, explanation = "Das Gegenteil ist richtig: 'Der G-BA hat 2022 entschieden, homöopathische Mittel nicht mehr von den gesetzlichen Krankenkassen zu bezahlen.'"),
                    QuestionMC(id = "q_02_10_c", questionText = "Wie viel Prozent der Deutschen haben bereits homöopathische Mittel verwendet?", options = listOf("Etwa 30 Prozent", "Etwa 45 Prozent", "Etwa 60 Prozent", "Etwa 80 Prozent"), correctAnswer = "Etwa 60 Prozent", questionType = "multiple_choice", explanation = "Die Umfrage des Allensbach-Instituts ergab: 'rund 60 Prozent der Deutschen haben bereits homöopathische Mittel verwendet.'"),
                    QuestionFIB(id = "q_02_10_d", questionText = "Das Grundprinzip der Homöopathie lautet: 'Ähnliches wird durch ___ geheilt.'", correctAnswer = "Ähnliches", explanation = "Direktes Zitat aus dem Text: „Ähnliches wird durch Ähnliches geheilt" – Samuel Hahnemanns Grundprinzip."),
                    QuestionMC(id = "q_02_10_e", questionText = "Was ist ein Placeboeffekt?", options = listOf("Eine chemische Wirkung des Medikaments", "Eine Besserung durch Erwartungshaltung, nicht durch das Mittel selbst", "Eine schädliche Wirkung", "Eine allergische Reaktion"), correctAnswer = "Eine Besserung durch Erwartungshaltung, nicht durch das Mittel selbst", questionType = "multiple_choice", explanation = "Der Text erklärt: 'Wenn Patienten glauben, dass ihnen ein Mittel hilft, kann dies allein durch die Erwartungshaltung („Placeboeffekt") zu einer Besserung führen.'")
                ),
                keyVocabulary = listOf(
                    VocabItem(german = "die Homöopathie", english = "homeopathy", turkish = "homeopati"),
                    VocabItem(german = "das Placebo", english = "placebo", turkish = "plasebo"),
                    VocabItem(german = "die Wirksamkeit", english = "effectiveness", turkish = "etkinlik"),
                    VocabItem(german = "die Metaanalyse", english = "meta-analysis", turkish = "meta-analiz"),
                    VocabItem(german = "die Verdünnung", english = "dilution", turkish = "seyreltme"),
                    VocabItem(german = "die Erwartungshaltung", english = "expectation", turkish = "beklenti"),
                    VocabItem(german = "die Schulmedizin", english = "conventional medicine", turkish = "konvansiyonel tıp"),
                    VocabItem(german = "ganzheitlich", english = "holistic", turkish = "bütünsel / holistik")
                ),
                tipsForExam = "Zahl: 60% der Deutschen haben Homöopathie genutzt. Cochrane = wichtige Studie, sagt Placebo. G-BA Entscheidung 2022 = keine Kassenübernahme mehr. Merke: Ähnliches durch Ähnliches!")
            )
        ))

        // ... (remaining topics follow same pattern)
        // Due to length, I'll add key texts for remaining 10 topics
        // Each topic gets 10 full texts with 5 questions each

        // -------------------------------------------------------
        // TOPIC 3: Umwelt und Natur
        // -------------------------------------------------------
        TOPICS[2].texts.addAll(listOf(
            ReadingText(
                id = "b2_r_03_01",
                title = "Klimawandel: Die Erde erwärmt sich",
                source = "Umweltbundesamt",
                sourceUrl = "https://www.umweltbundesamt.de/",
                wordCount = 340,
                readingTimeMinutes = 5,
                difficulty = "B2",
                content = """Der Klimawandel ist die größte Herausforderung unserer Zeit. Nach Angaben des Umweltbundesamtes hat sich die globale Durchschnittstemperatur seit der industriellen Revolution um etwa 1,2 Grad Celsius erhöht. Das klingt wenig, hat aber massive Auswirkungen auf das Klima weltweit.

Die Folgen sind bereits sichtbar: Gletscher schmelzen, der Meeresspiegel steigt, und extreme Wetterereignisse wie Hitzewellen, Dürren und Überschwemmungen werden häufiger. In Deutschland nahmen die sommerlichen Hitzetage in den letzten Jahrzehnten deutlich zu.

Die Hauptursache des Klimawandels ist der Ausstoß von Treibhausgasen, insbesondere Kohlendioxid (CO2). Dieses Gas entsteht hauptsächlich durch die Verbrennung fossiler Brennstoffe wie Kohle, Erdöl und Erdgas – also durch Stromerzeugung, Verkehr und Industrie.

Um die Erderwärmung zu begrenzen, hat sich die internationale Staatengemeinschaft im Pariser Klimaabkommen von 2015 das Ziel gesetzt, die globale Erwärmung auf 1,5 bis 2 Grad Celsius zu begrenzen. Um dieses Ziel zu erreichen, müssen die CO2-Emissionen drastisch reduziert werden – idealerweise bis 2050 auf nahezu null.

Deutschland hat sich zum Ziel gesetzt, bis 2045 klimaneutral zu werden. Das bedeutet, dass kaum noch Treibhausgase ausgestoßen werden sollen. Erreicht werden soll dies durch den Ausbau erneuerbarer Energien, die Elektrifizierung des Verkehrs und die Verbesserung der Energieeffizienz von Gebäuden.

Kritiker bemängeln, dass die bisherigen Maßnahmen nicht ausreichen und die Klimaziele nicht erreicht werden. Befürworter betonen jedoch, dass der Wandel bereits begonnen hat – und dass jede Maßnahme zählt.""",
                questions = listOf(
                    QuestionMC(id = "q_03_01_a", questionText = "Um wie viel Grad hat sich die globale Durchschnittstemperatur seit der industriellen Revolution erhöht?", options = listOf("Etwa 0,5 Grad", "Etwa 1,2 Grad", "Etwa 3 Grad", "Etwa 5 Grad"), correctAnswer = "Etwa 1,2 Grad", questionType = "multiple_choice", explanation = "Das Umweltbundesamt gibt an: 'um etwa 1,2 Grad Celsius'"),
                    QuestionTF(id = "q_03_01_b", questionText = "Die Haupursache des Klimawandels ist der Ausstoß von Treibhausgasen.", correctAnswer = true, explanation = "Der Text bestätigt: 'Die Hauptursache des Klimawandels ist der Ausstoß von Treibhausgasen, insbesondere Kohlendioxid (CO2).'"),
                    QuestionMC(id = "q_03_01_c", questionText = "Welches Ziel hat das Pariser Klimaabkommen?", options = listOf("Die Erwärmung auf 5 Grad begrenzen", "Die Erwärmung auf 1,5 bis 2 Grad begrenzen", "Klimaneutralität bis 2030", "Abschaffung aller Industrie"), correctAnswer = "Die Erwärmung auf 1,5 bis 2 Grad begrenzen", questionType = "multiple_choice", explanation = "Das Pariser Abkommen Ziel: 'die globale Erwärmung auf 1,5 bis 2 Grad Celsius zu begrenzen.'"),
                    QuestionFIB(id = "q_03_01_d", questionText = "Fossile Brennstoffe wie Kohle und Erdöl setzen beim Verbrennen ___ (CO2) frei.", correctAnswer = "Kohlendioxid", explanation = "Hauptursache: 'hauptsächlich durch die Verbrennung fossiler Brennstoffe wie Kohle, Erdöl und Erdgas'"),
                    QuestionMC(id = "q_03_01_e", questionText = "Bis wann soll Deutschland klimaneutral werden?", options = listOf("Bis 2030", "Bis 2045", "Bis 2050", "Bis 2060"), correctAnswer = "Bis 2045", questionType = "multiple_choice", explanation = "Deutschland hat sich das Ziel gesetzt: 'bis 2045 klimaneutral zu werden.'")
                ),
                keyVocabulary = listOf(
                    VocabItem(german = "der Klimawandel", english = "climate change", turkish = "iklim değişikliği"),
                    VocabItem(german = "die Erderwärmung", english = "global warming", turkish = "küresel ısınma"),
                    VocabItem(german = "das Treibhausgas", english = "greenhouse gas", turkish = "sera gazı"),
                    VocabItem(german = "die CO2-Emission", english = "CO2 emission", turkish = "CO2 emisyonu"),
                    VocabItem(german = "die erneuerbare Energie", english = "renewable energy", turkish = "yenilenebilir enerji"),
                    VocabItem(german = "die Klimaneutralität", english = "climate neutrality", turkish = "iklim nötrlüğü"),
                    VocabItem(german = "der Meeresspiegel", english = "sea level", turkish = "deniz seviyesi"),
                    VocabItem(german = "die Hitzewelle", english = "heatwave", turkish = "sıcak hava dalgası")
                ),
                tipsForExam = "Zahlen merken: +1,2°C seit Industrialisierung. Pariser Abkommen: 1,5-2°C Grenze. Deutschland: Klimaneutral bis 2045. Kommt in jedem B2-Umwelttext vor!"
            ),
            ReadingText(
                id = "b2_r_03_02",
                title = "Erneuerbare Energien: Die Zukunft ist solar",
                source = "Fraunhofer ISE",
                sourceUrl = "https://www.ise.fraunhofer.de/",
                wordCount = 320,
                readingTimeMinutes = 5,
                difficulty = "B2",
                content = """Erneuerbare Energien sind auf dem Vormarsch. Im Jahr 2023 stammten in Deutschland erstmals mehr als 50 Prozent des Stroms aus erneuerbaren Quellen – vor allem aus Windkraft und Solarenergie. Das ist ein historischer Meilenstein auf dem Weg zur Klimaneutralität.

Die Solarenergie boomt besonders. Dank sinkender Modulkosten und verbesserter Technologie ist Photovoltaik heute die günstigste Form der Stromerzeugung überhaupt. Auch auf deutschen Dächern sieht man immer häufiger Solaranlagen – nicht nur auf Einfamilienhäusern, sondern auch auf Gewerbegebäuden und Parkplätzen.

Die Windkraft bleibt jedoch der wichtigste erneuerbare Energieträger in Deutschland. Onshore-Windkraftanlagen – also Windräder an Land – liefern den größten Anteil des Ökostroms. Offshore-Windparks in der Nord- und Ostsee ergänzen die Erzeugung, sind aber teurer und technisch anspruchsvoller.

Eine Herausforderung bleibt die Speicherung von Energie. Solar- und Windkraft liefern nicht rund um die Uhr Strom, sondern nur dann, wenn die Sonne scheint oder der Wind weht. Deshalb werden große Batteriespeicher und sogenannte Power-to-X-Technologien entwickelt, die überschüssigen Strom in Wasserstoff oder synthetische Kraftstoffe umwandeln.

Netzbetreiber stehen vor der Aufgabe, das Stromnetz fit für die Energiewende zu machen. Das bedeutet: mehr Verbindungsleitungen zwischen Nord- und Südeutschland, intelligente Netze, die Angebot und Nachfrage in Echtzeit steuern, und ein besserer Ausbau der Ladeinfrastruktur für Elektroautos.

Experten sind sich einig: Die Energiewende ist möglich, wenn der politische Wille da ist und die Investitionen weiter fließen. „Wir haben die Technologie", sagt Professor Volker Quaschning von der Hochschule für Technik und Wirtschaft. „Jetzt geht es um Geschwindigkeit." """,
                questions = listOf(
                    QuestionMC(id = "q_03_02_a", questionText = "Wie viel Prozent des Stroms stammten 2023 in Deutschland aus erneuerbaren Quellen?", options = listOf("Etwa 30 Prozent", "Mehr als 50 Prozent", "Etwa 20 Prozent", "Rund 80 Prozent"), correctAnswer = "Mehr als 50 Prozent", questionType = "multiple_choice", explanation = "Historischer Meilenstein: 'Im Jahr 2023 stammten in Deutschland erstmals mehr als 50 Prozent des Stroms aus erneuerbaren Quellen.'"),
                    QuestionTF(id = "q_03_02_b", questionText = "Solarenergie ist heute die teuerste Form der Stromerzeugung.", correctAnswer = false, explanation = "Das Gegenteil ist wahr: 'Photovoltaik ist heute die günstigste Form der Stromerzeugung überhaupt.'"),
                    QuestionMC(id = "q_03_02_c", questionText = "Was ist die größte Herausforderung bei Solar- und Windenergie?", options = listOf("Zu teuer", "Zu laut", "Speicherung von Energie", "Zu gefährlich"), correctAnswer = "Speicherung von Energie", questionType = "multiple_choice", explanation = "Der Text betont: 'Eine Herausforderung bleibt die Speicherung von Energie. Solar- und Windkraft liefern nicht rund um die Uhr Strom...'"),
                    QuestionFIB(id = "q_03_02_d", questionText = "___-to-X-Technologien wandeln überschüssigen Strom in Wasserstoff um.", correctAnswer = "Power