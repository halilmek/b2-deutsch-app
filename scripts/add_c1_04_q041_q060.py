import json

questions = [
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Der Vertrag tritt morgen in ____.",
        "options": ["Kraft", "Macht", "Wirkung", "Bedeutung"],
        "correctAnswer": "Kraft",
        "explanation": "'In Kraft treten' is a fixed functional verb phrase meaning 'to come into effect'."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Die Entscheidung wurde zur ____ gebracht.",
        "options": ["Ausführung", "Handlung", "Tat", "Leistung"],
        "correctAnswer": "Ausführung",
        "explanation": "'Zur Ausführung bringen' means 'to carry out or execute'."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Er brachte seine Meinung deutlich zum ____.",
        "options": ["Ausdruck", "Druck", "Begriff", "Hinweis"],
        "correctAnswer": "Ausdruck",
        "explanation": "'Zum Ausdruck bringen' means 'to express something'."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Die neue Regelung findet ab sofort ____.",
        "options": ["Anwendung", "Benutzung", "Einsatz", "Verwendung"],
        "correctAnswer": "Anwendung",
        "explanation": "'Anwendung finden' is a common functional verb phrase meaning 'to be applied'."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Der Vorschlag stieß auf große ____.",
        "options": ["Kritik", "Meinung", "Sprache", "Erklärung"],
        "correctAnswer": "Kritik",
        "explanation": "'Auf Kritik stoßen' means 'to encounter criticism'."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Die Firma nahm an der Messe teil und kam mit vielen Kunden in ____.",
        "options": ["Kontakt", "Verbindung", "Beziehung", "Diskussion"],
        "correctAnswer": "Kontakt",
        "explanation": "'In Kontakt kommen' means 'to get in touch'."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Die Ergebnisse stehen im engen ____ mit der Studie.",
        "options": ["Zusammenhang", "Kontakt", "Verhältnis", "Vergleich"],
        "correctAnswer": "Zusammenhang",
        "explanation": "'Im Zusammenhang stehen' means 'to be connected with'."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Der Politiker zog seine Aussage in ____.",
        "options": ["Zweifel", "Frage", "Unsicherheit", "Probleme"],
        "correctAnswer": "Zweifel",
        "explanation": "'In Zweifel ziehen' means 'to question something'."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Nach langen Diskussionen kam man zu einer ____.",
        "options": ["Entscheidung", "Bestimmung", "Überlegung", "Aussage"],
        "correctAnswer": "Entscheidung",
        "explanation": "'Zu einer Entscheidung kommen' means 'to reach a decision'."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Der Vorfall wurde zur ____ gebracht.",
        "options": ["Anzeige", "Meldung", "Information", "Erklärung"],
        "correctAnswer": "Anzeige",
        "explanation": "'Zur Anzeige bringen' means 'to report officially'."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Die neuen Maßnahmen kommen erst nächstes Jahr zur ____.",
        "options": ["Anwendung", "Verwendung", "Nutzung", "Leistung"],
        "correctAnswer": "Anwendung",
        "explanation": "'Zur Anwendung kommen' means 'to be applied'."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Er stellte dem Publikum eine interessante Theorie zur ____.",
        "options": ["Diskussion", "Frage", "Aussage", "Überlegung"],
        "correctAnswer": "Diskussion",
        "explanation": "'Zur Diskussion stellen' means 'to present for discussion'."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Die Organisation leistete wichtige ____ zur Verbesserung der Situation.",
        "options": ["Beiträge", "Arbeiten", "Hilfen", "Dienste"],
        "correctAnswer": "Beiträge",
        "explanation": "'Einen Beitrag leisten' means 'to contribute'."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Die Verhandlungen wurden zum ____ gebracht.",
        "options": ["Abschluss", "Ende", "Ziel", "Resultat"],
        "correctAnswer": "Abschluss",
        "explanation": "'Zum Abschluss bringen' means 'to complete something'."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Der Wissenschaftler kam zu der ____ , dass weitere Forschung nötig sei.",
        "options": ["Erkenntnis", "Kenntnis", "Meinung", "Information"],
        "correctAnswer": "Erkenntnis",
        "explanation": "'Zu der Erkenntnis kommen' means 'to realize or conclude'."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Das Thema fand große ____ in den Medien.",
        "options": ["Beachtung", "Aufmerksamkeit", "Bedeutung", "Wirkung"],
        "correctAnswer": "Beachtung",
        "explanation": "'Beachtung finden' means 'to receive attention'."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Die Teilnehmer führten intensive Gespräche und kamen zu keinem ____.",
        "options": ["Ergebnis", "Ziel", "Beschluss", "Abschluss"],
        "correctAnswer": "Ergebnis",
        "explanation": "'Zu einem Ergebnis kommen' means 'to reach a result'."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Die neuen Vorschriften treten nächsten Monat in ____.",
        "options": ["Kraft", "Wirkung", "Einfluss", "Anwendung"],
        "correctAnswer": "Kraft",
        "explanation": "'In Kraft treten' is a fixed legal expression."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Der Verdächtige stand unter starkem ____.",
        "options": ["Druck", "Stress", "Einfluss", "Problem"],
        "correctAnswer": "Druck",
        "explanation": "'Unter Druck stehen' is a common functional verb phrase."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Die Kritik brachte ihn in große ____.",
        "options": ["Verlegenheit", "Probleme", "Unsicherheit", "Schwierigkeiten"],
        "correctAnswer": "Verlegenheit",
        "explanation": "'In Verlegenheit bringen' means 'to embarrass someone'."
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
