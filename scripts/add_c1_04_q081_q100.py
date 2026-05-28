import json

questions = [
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Was kennzeichnet ein Funktionsverbgefüge (FVG)?",
        "options": [
            "Ein Vollverb wird durch ein Modalverb ersetzt.",
            "Ein semantisch schwaches Verb wird mit einem Substantiv kombiniert, um eine spezifische Bedeutung zu bilden.",
            "Zwei Synonyme werden zur Verstärkung nebeneinandergestellt.",
            "Ein Adjektiv wird als Prädikat mit 'sein' verbunden."
        ],
        "correctAnswer": "Ein semantisch schwaches Verb wird mit einem Substantiv kombiniert, um eine spezifische Bedeutung zu bilden.",
        "explanation": "A Funktionsverbgefüge combines a 'light verb' (like bringen, kommen, stellen, setzen) with a noun (often derived from a verb) to express a nuanced or formal meaning, e.g., 'zur Anwendung bringen' instead of 'anwenden'."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welches Funktionsverbgefüge bedeutet 'anwenden'?",
        "options": [
            "in Kraft treten",
            "zur Anwendung bringen",
            "zum Ausdruck kommen",
            "unter Beweis stellen"
        ],
        "correctAnswer": "zur Anwendung bringen",
        "explanation": "'Zur Anwendung bringen' is a standard FVG equivalent to the simple verb 'anwenden'. It is frequently used in formal, administrative, and academic contexts."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Ergänzen Sie das Funktionsverbgefüge: 'etwas zur ____ bringen' (= anwenden).",
        "options": [
            "Ausführung",
            "Anwendung",
            "Auswirkung",
            "Aufführung"
        ],
        "correctAnswer": "Anwendung",
        "explanation": "The correct completion is 'zur Anwendung bringen', a common FVG meaning 'to apply' or 'to put into practice'."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welches Verb vervollständigt das FVG: 'etwas in Betracht ____' (= berücksichtigen)?",
        "options": [
            "nehmen",
            "ziehen",
            "stellen",
            "bringen"
        ],
        "correctAnswer": "ziehen",
        "explanation": "'In Betracht ziehen' is a fixed FVG meaning 'to consider' or 'to take into account'. The verb 'ziegen' here has lost its literal meaning and functions as a light verb."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Was bedeutet das Funktionsverbgefüge 'zur Diskussion stellen'?",
        "options": [
            "etwas ablehnen",
            "etwas diskutieren oder zur Debatte anbieten",
            "etwas endgültig entscheiden",
            "etwas geheim halten"
        ],
        "correctAnswer": "etwas diskutieren oder zur Debatte anbieten",
        "explanation": "'Zur Diskussion stellen' means to open something for debate or consideration. FVGs like this allow for nuanced expression of procedural or communicative actions in formal discourse."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welches FVG drückt Zweifel oder Infragestellung aus?",
        "options": [
            "in Frage stellen",
            "zur Frage bringen",
            "unter Frage nehmen",
            "bei Frage bleiben"
        ],
        "correctAnswer": "in Frage stellen",
        "explanation": "'In Frage stellen' is the correct FVG meaning 'to question' or 'to cast doubt on'. It is widely used in academic and critical discourse."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Wie lautet das Funktionsverbgefüge für das einfache Verb 'beweisen'?",
        "options": [
            "unter Beweis stellen",
            "zum Beweis bringen",
            "in Beweis setzen",
            "bei Beweis bleiben"
        ],
        "correctAnswer": "unter Beweis stellen",
 "explanation": "'Unter Beweis stellen' is the standard FVG equivalent to 'beweisen'. It emphasizes the act of demonstrating validity through evidence."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welche Präposition ergänzt das FVG korrekt: '____ Kraft treten' (= gültig werden)?",
        "options": [
            "Zu",
            "In",
            "Außer",
            "Mit"
        ],
        "correctAnswer": "In",
        "explanation": "'In Kraft treten' means 'to come into effect'. The preposition 'in' is fixed; confusing it with 'außer Kraft treten' (to be repealed) is a common C1-level error."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welches FVG ist im folgenden Satz stilistisch am angemessensten? 'Die neue Regelung ____ nächste Woche ____.'",
        "options": [
            "tritt ... in Kraft",
            "kommt ... zur Kraft",
            "setzt ... in die Kraft",
            "bringt ... die Kraft"
        ],
        "correctAnswer": "tritt ... in Kraft",
        "explanation": "'In Kraft treten' is a fixed, intransitive FVG. The verb 'treten' is conjugated, and 'in Kraft' remains unchanged. This construction is standard in legal and administrative German."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Identifizieren Sie das Funktionsverbgefüge im Satz: 'Der Minister brachte seine Bedenken zur Sprache.'",
        "options": [
            "Bedenken haben",
            "zur Sprache bringen",
            "der Minister brachte",
            "seine Bedenken"
        ],
        "correctAnswer": "zur Sprache bringen",
        "explanation": "'Zur Sprache bringen' is the FVG meaning 'to mention' or 'to raise a topic'. Recognizing FVGs within complex sentences is a key C1 reading and analysis skill."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welches FVG ist typisch für juristische Texte, um auszudrücken, dass etwas verboten und strafbar gemacht wird?",
        "options": [
            "unter Strafe stellen",
            "zur Strafe bringen",
            "in Strafe setzen",
            "bei Strafe bleiben"
        ],
        "correctAnswer": "unter Strafe stellen",
        "explanation": "'Unter Strafe stellen' is a legal FVG meaning 'to make something punishable by law'."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Transformieren Sie das FVG 'in Erfüllung gehen' in ein einfaches Verb.",
        "options": [
            "erfüllen",
            "erfüllt werden",
            "sich erfüllen",
            "zur Erfüllung bringen"
        ],
        "correctAnswer": "sich erfüllen",
        "explanation": "'In Erfüllung gehen' corresponds to the reflexive verb 'sich erfüllen'. Understanding bidirectional transformation between FVGs and simple verbs demonstrates advanced grammatical control."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welcher Unterschied besteht zwischen 'zum Ausdruck bringen' und 'Ausdruck finden'?",
        "options": [
            "Keiner; beide sind synonym und austauschbar.",
            "'Zum Ausdruck bringen' ist aktiv und agentiv; 'Ausdruck finden' ist passivisch und betont das Ergebnis.",
            "'Ausdruck finden' ist umgangssprachlich; 'zum Ausdruck bringen' ist formell.",
            "'Zum Ausdruck bringen' erfordert immer ein direktes Objekt; 'Ausdruck finden' nie."
        ],
        "correctAnswer": "'Zum Ausdruck bringen' ist aktiv und agentiv; 'Ausdruck finden' ist passivisch und betont das Ergebnis.",
        "explanation": "'jemand bringt etwas zum Ausdruck' (active agency) vs. 'etwas findet Ausdruck' (impersonal, result-focused). Stylistic precision with FVGs reflects advanced proficiency."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welches FVG ist stilistisch am geeignetsten für einen wissenschaftlichen Text, um zu sagen, dass eine Theorie wirksam wird?",
        "options": [
            "Die Theorie kommt zur Geltung.",
            "Die Theorie macht geltend.",
            "Die Theorie bringt zur Geltung.",
            "Die Theorie ist in Geltung."
        ],
        "correctAnswer": "Die Theorie kommt zur Geltung.",
        "explanation": "'Zur Geltung kommen' is the appropriate intransitive FVG meaning 'to become effective/recognized'. Preferred in academic writing for its formal tone and impersonal structure."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welcher Satz enthält ein grammatikalisch oder idiomatisch fehlerhaftes Funktionsverbgefüge?",
        "options": [
            "Die Maßnahme tritt außer Kraft.",
            "Er stellte den Antrag in Antrag.",
            "Das Gesetz gelangt zur Anwendung.",
            "Seine Worte fanden großen Anklang."
        ],
        "correctAnswer": "Er stellte den Antrag in Antrag.",
        "explanation": "The proper FVG is 'einen Antrag stellen' (not 'in Antrag'). Confusing prepositions or creating hybrid forms is a frequent error."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Wie lautet das korrekte FVG mit Kasusregierung für: 'etwas (Akk) ____ Zusammenhang ____ (mit etwas)'?",
        "options": [
            "im ... stehen",
            "in ... stehen",
            "zum ... bringen",
            "unter ... stellen"
        ],
        "correctAnswer": "in ... stehen",
        "explanation": "The correct FVG is 'in Zusammenhang stehen mit' (+ dative). Case and preposition mastery is crucial at C1."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welche Formulierung ist im Register eines offiziellen Schreibens am angemessensten?",
        "options": [
            "Wir wollen das Problem schnell lösen.",
            "Wir beabsichtigen, eine Lösung des Problems zügig herbeizuführen.",
            "Man sollte das Problem bald angehen.",
            "Das Problem muss schnell gelöst werden."
        ],
        "correctAnswer": "Wir beabsichtigen, eine Lösung des Problems zügig herbeizuführen.",
        "explanation": "'Eine Lösung herbeiführen' is a formal FVG that conveys intention and procedural action. Its use in official correspondence demonstrates register awareness and stylistic sophistication."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Transformieren Sie den Satz unter Verwendung eines stilistisch angemessenen FVG: 'Man muss die Sicherheitsvorschriften genau beachten.'",
        "options": [
            "Die Sicherheitsvorschriften sind unter genaue Beachtung zu stellen.",
            "Den Sicherheitsvorschriften ist genaue Beachtung zu schenken.",
            "Man schenkt den Sicherheitsvorschriften genau Beachtung.",
            "Genaue Beachtung wird den Sicherheitsvorschriften gemacht."
        ],
        "correctAnswer": "Den Sicherheitsvorschriften ist genaue Beachtung zu schenken.",
        "explanation": "This transformation uses the FVG 'Beachtung schenken' (+ dative) combined with 'sein + zu + Infinitiv' for formal obligation. It demonstrates advanced syntactic and stylistic control."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welche Strategie zeigt fortgeschrittene Kompetenz im Umgang mit Funktionsverbgefügen auf C1-Niveau?",
        "options": [
            "FVGs ausschließlich zu vermeiden, um Klarheit zu gewährleisten.",
            "FVGs gezielt einzusetzen, um Register, Nuance und textsortenspezifische Angemessenheit zu steuern.",
            "Immer die einfachste Verbform zu wählen, um Fehler zu minimieren.",
            "FVGs nur in mündlichen Prüfungen zu verwenden."
        ],
        "correctAnswer": "FVGs gezielt einzusetzen, um Register, Nuance und textsortenspezifische Angemessenheit zu steuern.",
        "explanation": "C1 proficiency includes strategic stylistic choice: knowing when FVGs enhance formality, precision, or rhetorical effect—and when simpler verbs improve clarity."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welches FVG passt semantisch und syntaktisch in den Satz: 'Die Forschungsergebnisse ____ neue Perspektiven ____.'?",
        "options": [
            "bringen ... zur Entfaltung",
            "eröffnen ... (kein FVG)",
            "kommen ... zur Wirkung",
            "stellen ... unter Beweis"
        ],
        "correctAnswer": "bringen ... zur Entfaltung",
        "explanation": "'Zur Entfaltung bringen' is a sophisticated FVG meaning 'to enable development/unfolding'. Selecting context-appropriate FVGs is a hallmark of C1 competence."
    }
]


def add_qs(topic_json_path, questions):
    with open(topic_json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    existing_ids = {q['id'] for q in data['questions'] if 'id' in q}

    added = 0
    for q in questions:
        q_id = q.get('id')
        if q_id in existing_ids:
            continue
        data['questions'].append(q)
        added += 1

    data['totalQuestions'] = len(data['questions'])

    with open(topic_json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Added {added} questions to {topic_json_path}")
    print(f"New total: {data['totalQuestions']}")


if __name__ == '__main__':
    add_qs('app/src/main/assets/c1_04.json', questions)
