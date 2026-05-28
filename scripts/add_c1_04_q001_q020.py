import json

questions = [
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Ergänzen Sie das richtige Funktionsverb: Der Abgeordnete ____ scharfe Kritik an den neuen Regierungsplänen.",
        "options": [
            "übte",
            "machte",
            "äußerte",
            "brachte"
        ],
        "correctAnswer": "übte",
        "explanation": "The fixed collocation (Funktionsverbgefüge) for criticizing someone or something is 'Kritik üben an' (+ dative)."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welches Verb vervollständigt das Gefüge mit der Bedeutung 'entscheiden'? Wir müssen endlich eine Entscheidung ____.",
        "options": [
            "treffen",
            "machen",
            "fällen",
            "nehmen"
        ],
        "correctAnswer": "treffen",
        "explanation": "'Eine Entscheidung treffen' is the standard, high-frequency Funktionsverbgefüge meaning 'to make a decision'. 'Eine Entscheidung fällen' is also used (usually by judges or high authorities), but 'treffen' is the most universally applicable correct option among the choices."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Wählen Sie das passende Verb: Nach langen Verhandlungen ____ die beiden Parteien ein Abkommen.",
        "options": [
            "schlossen",
            "machten",
            "trafen",
            "gingen"
        ],
        "correctAnswer": "schlossen",
        "explanation": "The fixed legal and economic expression for signing/concluding a contract or agreement is 'ein Abkommen / einen Vertrag schließen'."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Ergänzen Sie das Gefüge im Passiv-Sinne: Die neue Technologie ____ bereits nächste Woche zur Anwendung.",
        "options": [
            "kommt",
            "bringt",
            "stellt",
            "führt"
        ],
        "correctAnswer": "kommt",
        "explanation": "'Zur Anwendung kommen' has a passive meaning and means 'to be applied/used'. In contrast, 'zur Anwendung bringen' would be the active/causative counterpart."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welches Funktionsverb passt zur Kausalität (etwas bewirken)? Der Vorfall ____ die Ermittler ins Grübeln.",
        "options": [
            "brachte",
            "setzte",
            "führte",
            "gab"
        ],
        "correctAnswer": "brachte",
        "explanation": "The idiom 'jemanden ins Grübeln bringen' means to make someone start pondering or worrying about something."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Ersetzen Sie das Verb durch ein FVG: 'Wir müssen das Thema morgen ansprechen.' -> 'Wir müssen das Thema morgen ____ bringen.'",
        "options": [
            "zur Sprache",
            "ins Gespräch",
            "zum Ausdruck",
            "vor Augen"
        ],
        "correctAnswer": "zur Sprache",
        "explanation": "'Etwas zur Sprache bringen' is the precise Funktionsverbgefüge for mentioning a topic or bringing it up for discussion."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Ergänzen Sie die Lücke: Der Professor ____ den Studierenden Unterstützung bei der Jobsuche in Aussicht.",
        "options": [
            "stellte",
            "gab",
            "brachte",
            "zeigte"
        ],
        "correctAnswer": "stellte",
        "explanation": "'Jemandem etwas in Aussicht stellen' means to promise someone a high probability of a future benefit or outcome (to hold out prospects of something)."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welches Funktionsverb verlangt diese präpositionale Wendung? Der Neubau befindet sich momentan ____.",
        "options": [
            "in der Bauphase",
            "im Bau",
            "zur Errichtung",
            "unter Konstruktion"
        ],
        "correctAnswer": "im Bau",
        "explanation": "The fixed phrase 'im Bau sein / sich im Bau befinden' means 'to be under construction' (wird gebaut)."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Wählen Sie das korrekte Verb für dieses FVG: Bitte ____ Sie Rücksicht auf die anderen Hotelgäste.",
        "options": [
            "nehmen",
            "geben",
            "haben",
            "machen"
        ],
        "correctAnswer": "nehmen",
        "explanation": "'Rücksicht nehmen auf' (+ accusative) is the fixed construction meaning to be considerate of or show consideration for someone."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welches Verb passt in diesen C1-Geschäftskontext? Die Firma möchte mit dem Konkurrenten in Verbindung ____.",
        "options": [
            "treten",
            "kommen",
            "gehen",
            "stehen"
        ],
        "correctAnswer": "treten",
        "explanation": "'In Verbindung treten mit' implies the dynamic action of initiating contact. 'In Verbindung stehen' would mean they are already in contact."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Ergänzen Sie die Lücke im akademischen Kontext: Die Ergebnisse dieser Studie ____ die Behauptungen der Kritiker Lügen.",
        "options": [
            "strafen",
            "machen",
            "stellen",
            "weisen"
        ],
        "correctAnswer": "strafen",
        "explanation": "The sophisticated C1 idiomatic structure 'jemanden/etwas Lügen strafen' means to prove someone or something completely wrong (to belie/give the lie to)."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welches Funktionsverb drückt den Beginn eines Zustands (Inchoativ) aus? Das Gesetz ____ am 1. Januar in Kraft.",
        "options": [
            "tritt",
            "kommt",
            "ist",
            "wird"
        ],
        "correctAnswer": "tritt",
        "explanation": "'In Kraft treten' means to become effective / come into force (start of a state). 'In Kraft sein' represents the durative state itself."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Ergänzen Sie das passende Funktionsverb: Seine mutige Tat ____ bei allen Bürgern große Anerkennung.",
        "options": [
            "fand",
            "erhielt",
            "bekam",
            "erntete"
        ],
        "correctAnswer": "fand",
        "explanation": "'Anerkennung finden' is the proper abstract structural pairing for 'to find / receive recognition'. While 'Anerkennung ernten' is used colloquially, 'fand' is the ideal formal FVG."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welches FVG bedeutet 'etwas fälschlicherweise annehmen'? Ich ____ den Irrtum auf, dass der Termin heute sei.",
        "options": [
            "saß ... dem",
            "lief ... in den",
            "machte ... den",
            "befand ... im"
        ],
        "correctAnswer": "saß ... dem",
        "explanation": "The highly idiomatic expression 'einem Irrtum aufsitzen' (past tense: 'ich saß dem Irrtum auf') means to labor under a misconception / be mistaken."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Vervollständigen Sie den Satz: Der Zeuge wurde vom Gericht unter Eid ____.",
        "options": [
            "genommen",
            "gestellt",
            "gebracht",
            "gesetzt"
        ],
        "correctAnswer": "genommen",
        "explanation": "The official legal phrase meaning to put someone under oath is 'jemanden unter Eid nehmen'."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welches Verb passt hier? Das neue Bauprojekt ____ auf heftigen Widerstand in der Bevölkerung.",
        "options": [
            "stieß",
            "traf",
            "machte",
            "kam"
        ],
        "correctAnswer": "stieß",
        "explanation": "The fixed collocation for encountering resistance or opposition is 'auf Widerstand stoßen'."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Ergänzen Sie das kausative Funktionsverb: Die Regierung hat die Armee in Bereitschaft ____.",
        "options": [
            "versetzt",
            "gestellt",
            "gebracht",
            "gerufen"
        ],
        "correctAnswer": "versetzt",
        "explanation": "To alter a state of a person or institution drastically (like panic, alert, or readiness) requires the functional verb 'versetzen' ('in Bereitschaft versetzen')."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Finden Sie das falsche Funktionsverbgefüge:",
        "options": [
            "Einen Fehler machen",
            "Eine Frage stellen",
            "Einen Antrag bringen",
            "Einen Entschluss fassen"
        ],
        "correctAnswer": "Einen Antrag bringen",
        "explanation": "'Einen Antrag bringen' is incorrect. The grammatically and idiomatically correct functional verb pairing for filing an application is 'einen Antrag stellen'."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Vervollständigen Sie das Gefüge mit der passenden Präposition: Das Projekt steht kurz ____ Abschluss.",
        "options": [
            "vor dem",
            "zum",
            "beim",
            "hinter dem"
        ],
        "correctAnswer": "vor dem",
        "explanation": "The expression 'vor dem Abschluss stehen' means to be near completion / close to being finished."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welche Bedeutung hat das FVG im folgenden Satz? 'Der Direktor stellte klar, dass diese Maßnahme nicht zur Debatte steht.'",
        "options": [
            "Die Maßnahme wird nicht diskutiert.",
            "Die Maßnahme muss sofort umgesetzt werden.",
            "Die Maßnahme ist illegal.",
            "Die Maßnahme wird positiv bewertet."
        ],
        "correctAnswer": "Die Maßnahme wird nicht diskutiert.",
        "explanation": "'Zur Debatte stehen' means 'to be open for discussion/debate'. Combined with a negation ('nicht zur Debatte stehen'), it implies that the option is completely off the table and will not be discussed."
    }
]


def add_qs(topic_json_path, questions, topic_name_str):
    with open(topic_json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    existing_ids = {q['id'] for q in data['questions'] if 'id' in q}

    added = 0
    for q in questions:
        q_id = q.get('id')
        if q_id and q_id in existing_ids:
            continue
        new_id = f"{topic_name_str}_q{len(data['questions']) + 1:03d}"
        q['id'] = new_id
        data['questions'].append(q)
        added += 1

    data['totalQuestions'] = len(data['questions'])

    with open(topic_json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Added {added} questions to {topic_json_path}")
    print(f"New total: {data['totalQuestions']}")


if __name__ == '__main__':
    add_qs('app/src/main/assets/c1_04.json', questions, 'c1_04')
