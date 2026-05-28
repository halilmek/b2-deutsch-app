import json

questions = [
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Ein Funktionsverbgefüge (FVG) besteht aus einem ____ und einem nominalen Ausdruck.",
        "options": [
            "funktionsschwachen Verb",
            "Vollverb",
            "Modalverb",
            "Hilfsverb 'haben'"
        ],
        "correctAnswer": "funktionsschwachen Verb",
        "explanation": "A Funktionsverbgefüge combines a semantically weak verb (like 'bringen', 'kommen', 'setzen') with a noun phrase, often a nominalized verb."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welches der folgenden ist ein typisches Funktionsverbgefüge?",
        "options": [
            "einen Brief schreiben",
            "zur Aufführung bringen",
            "schnell laufen",
            "das Haus bauen"
        ],
        "correctAnswer": "zur Aufführung bringen",
        "explanation": "'zur Aufführung bringen' = to perform (literally 'to bring to performance'). The verb 'bringen' loses its full meaning and functions with the noun."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Ergänzen Sie: 'Er hat den Plan ____.'",
        "options": [
            "durchgeführt",
            "zur Durchführung gebracht",
            "in Durchführung genommen",
            "auf die Durchführung gesetzt"
        ],
        "correctAnswer": "zur Durchführung gebracht",
        "explanation": "'zur Durchführung bringen' is a common FVG meaning 'to carry out/implement'. The other options are not standard FVG collocations."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welche Funktion haben Funktionsverbgefüge im Deutschen?",
        "options": [
            "Sie machen den Text emotionaler.",
            "Sie machen den Satz nominaler und oft formeller.",
            "Sie ersetzen immer das Passiv.",
            "Sie werden nur in der Umgangssprache verwendet."
        ],
        "correctAnswer": "Sie machen den Satz nominaler und oft formeller.",
        "explanation": "FVGs shift the meaning toward nominal style, often sounding more abstract, formal, or official than the corresponding full verb (e.g., 'zur Anwendung bringen' vs. 'anwenden')."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welches Verb ist KEIN typisches Funktionsverb?",
        "options": [
            "bringen",
            "kommen",
            "schlagen",
            "setzen"
        ],
        "correctAnswer": "schlagen",
        "explanation": "Common function verbs in German are 'bringen', 'kommen', 'setzen', 'stellen', 'treten', 'geraten', 'ziehen'. 'schlagen' rarely appears in FVGs."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Vervollständigen Sie: 'Das Projekt ____ zum Abschluss.'",
        "options": [
            "wird gebracht",
            "kommt",
            "ist",
            "stellt sich"
        ],
        "correctAnswer": "kommt",
        "explanation": "'zum Abschluss kommen' = to be completed/finished. This FVG uses 'kommen' as the function verb."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Was bedeutet 'etwas in Frage stellen'?",
        "options": [
            "eine Frage stellen",
            "etwas anzweifeln / bezweifeln",
            "etwas fragen",
            "etwas beantworten"
        ],
        "correctAnswer": "etwas anzweifeln / bezweifeln",
        "explanation": "'etwas in Frage stellen' is an FVG meaning 'to question something / to doubt something'. It's not literal (placing something into a question)."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Ersetzen Sie das Vollverb durch ein Funktionsverbgefüge: 'Sie beabsichtigt zu reisen.'",
        "options": [
            "Sie hat die Absicht zu reisen.",
            "Sie ist in der Absicht zu reisen.",
            "Sie setzt die Absicht zu reisen.",
            "Sie bringt die Absicht zu reisen."
        ],
        "correctAnswer": "Sie hat die Absicht zu reisen.",
        "explanation": "'die Absicht haben' + zu + Infinitive is the FVG for 'beabsichtigen'. This is a very common pattern with 'haben'."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welches Funktionsverbgefüge bedeutet 'to come to a decision'?",
        "options": [
            "eine Entscheidung bringen",
            "eine Entscheidung setzen",
            "eine Entscheidung fällen",
            "eine Entscheidung treffen"
        ],
        "correctAnswer": "eine Entscheidung treffen",
        "explanation": "'eine Entscheidung treffen' is the correct FVG for 'to make a decision'. 'treffen' is the function verb here."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Vervollständigen Sie: 'Die Firma wurde ____ gesetzt.'",
        "options": [
            "in Kenntnis",
            "außer Betrieb",
            "unter Druck",
            "auf Probe"
        ],
        "correctAnswer": "außer Betrieb",
        "explanation": "'außer Betrieb setzen' = to decommission/take out of service. This is a fixed FVG with 'setzen'."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welche Präposition kommt typischerweise in FVGs mit dem Verb 'bringen' vor?",
        "options": [
            "auf",
            "in",
            "unter",
            "Alle drei sind möglich."
        ],
        "correctAnswer": "Alle drei sind möglich.",
        "explanation": "'bringen' appears in many FVGs: 'auf den Punkt bringen', 'in Gefahr bringen', 'unter Kontrolle bringen' – all prepositions are possible."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "'in Anspruch nehmen' bedeutet:",
        "options": [
            "jemanden einladen",
            "etwas nutzen/beanspruchen",
            "etwas ablehnen",
            "etwas bezahlen"
        ],
        "correctAnswer": "etwas nutzen/beanspruchen",
        "explanation": "'in Anspruch nehmen' means 'to use/utilize' or 'to claim/take up' (e.g., time, resources, services)."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Ergänzen Sie: 'Die Verhandlungen ____ zu einem positiven Ergebnis.'",
        "options": [
            "brachten",
            "führten",
            "kamen",
            "stellten"
        ],
        "correctAnswer": "führten",
        "explanation": "'zu einem Ergebnis führen' = to lead to a result. 'führen' is the function verb in this FVG."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welches Funktionsverbgefüge ist synonym zu 'sich entscheiden'?",
        "options": [
            "eine Entscheidung haben",
            "zur Entscheidung kommen",
            "eine Entscheidung stellen",
            "in Entscheidung treten"
        ],
        "correctAnswer": "zur Entscheidung kommen",
        "explanation": "'zur Entscheidung kommen' means 'to come to a decision', synonymous with 'sich entscheiden'."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Was ist der Unterschied zwischen 'jemanden in Kenntnis setzen' und 'jemanden informieren'?",
        "options": [
            "Kein Unterschied.",
            "Ersteres ist formeller/behördlicher.",
            "Ersteres ist umgangssprachlich.",
            "Ersteres bedeutet 'falsch informieren'."
        ],
        "correctAnswer": "Ersteres ist formeller/behördlicher.",
        "explanation": "'jemanden in Kenntnis setzen' is an FVG used in formal or official contexts, while 'informieren' is neutral."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Vervollständigen Sie: 'Er ____ die Sache ins Lächerliche.'",
        "options": [
            "zieht",
            "bringt",
            "nimmt",
            "tritt"
        ],
        "correctAnswer": "zieht",
        "explanation": "'ins Lächerliche ziehen' = to ridicule/make fun of. This FVG uses 'ziehen' as the function verb."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welches FVG bedeutet 'to apply/use' im Sinne von 'etwas anwenden'?",
        "options": [
            "zum Einsatz bringen",
            "in Gebrauch setzen",
            "zur Anwendung bringen",
            "Alle drei sind möglich."
        ],
        "correctAnswer": "Alle drei sind möglich.",
        "explanation": "'zum Einsatz bringen', 'in Gebrauch setzen', and 'zur Anwendung bringen' all mean 'to apply/use' and are valid FVGs."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Erkennen Sie das Funktionsverbgefüge: 'Die Behörde hat das Gesetz in Kraft gesetzt.'",
        "options": [
            "Das Gesetz",
            "Die Behörde",
            "in Kraft gesetzt",
            "hat das Gesetz"
        ],
        "correctAnswer": "in Kraft gesetzt",
        "explanation": "'in Kraft setzen' is the FVG meaning 'to put into force/effect'. 'setzen' is the function verb."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welcher Satz enthält ein Funktionsverbgefüge?",
        "options": [
            "Der Hund läuft schnell.",
            "Sie steht unter Verdacht.",
            "Das Haus wird gebaut.",
            "Ich lese ein Buch."
        ],
        "correctAnswer": "Sie steht unter Verdacht.",
        "explanation": "'unter Verdacht stehen' = to be suspected. 'stehen' is the function verb, and the meaning is not literal (standing)."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Formen Sie um in ein Funktionsverbgefüge: 'Der Arzt untersuchte den Patienten.'",
        "options": [
            "Der Arzt brachte den Patienten zur Untersuchung.",
            "Der Arzt stellte den Patienten unter Untersuchung.",
            "Der Arzt zog den Patienten in Untersuchung.",
            "Der Arzt nahm den Patienten in Untersuchung."
        ],
        "correctAnswer": "Der Arzt brachte den Patienten zur Untersuchung.",
        "explanation": "'zur Untersuchung bringen' is an FVG meaning 'to examine'. It's more formal/official than 'untersuchen'."
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
