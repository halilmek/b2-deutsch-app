import json

questions = [
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Der ____ Mann arbeitet seit Jahren in diesem Unternehmen.",
        "options": [
            "dort angestellte",
            "dort angestellt",
            "angestellt dort",
            "dort anstellen"
        ],
        "correctAnswer": "dort angestellte",
        "explanation": "Partizip I als Adjektiv muss korrekt dekliniert werden. 'Der dort angestellte Mann' — Partizip I mit Adjektivendung '-e' nach maskulinem Nominativ mit bestimmtem Artikel."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Die Studenten, ____ an dem Projekt teilnehmen, treffen sich heute Abend.",
        "options": ["die", "deren", "denen", "welcher"],
        "correctAnswer": "die",
        "explanation": "Das Relativpronomen bezieht sich auf 'Studenten' (Nominativ Plural). 'Die' ist die korrekte Form."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Die gestern ____ Dokumente müssen sofort überprüft werden.",
        "options": [
            "eingereichten",
            "eingereichte",
            "einreichenden",
            "eingereicht"
        ],
        "correctAnswer": "eingereichten",
        "explanation": "Das Partizip II als Adjektiv muss mit dem Plural 'Dokumente' dekliniert werden. Nach dem bestimmten Artikel 'die' ist die Adjektivendung '-en'."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Das Buch, ____ ich dir empfohlen habe, ist inzwischen ausverkauft.",
        "options": ["das", "dem", "dessen", "den"],
        "correctAnswer": "das",
        "explanation": "Das Relativpronomen bezieht sich auf 'das Buch' im Akkusativ. 'Das' ist die korrekte Akkusativform."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Die im Labor ____ Experimente führten zu neuen Erkenntnissen.",
        "options": [
            "durchgeführten",
            "durchgeführt",
            "durchführenden",
            "durchgeführte"
        ],
        "correctAnswer": "durchgeführten",
        "explanation": "Ein dekliniertes Partizip-Adjektiv wird vor dem Plural-Nomen benötigt. Nach 'die' im Nominativ Plural ist die Endung '-en'."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Die Frau, mit ____ ich gesprochen habe, ist Professorin.",
        "options": ["der", "die", "deren", "denen"],
        "correctAnswer": "der",
        "explanation": "Die Präposition 'mit' erfordert den Dativ. 'Der' ist die Dativ-Form des Relativpronomens für feminin Singular."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Der auf dem Tisch ____ Brief gehört meinem Bruder.",
        "options": ["liegende", "gelegen", "liegend", "gelegte"],
        "correctAnswer": "liegende",
        "explanation": "Partizip I wird als Adjektiv verwendet und muss dekliniert werden. 'Der liegende Brief' — Partizip I mit Endung '-e' nach maskulinem Nominativ."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Die Kollegen, ____ Büros renoviert werden, arbeiten heute von zu Hause.",
        "options": ["deren", "die", "denen", "welche"],
        "correctAnswer": "deren",
        "explanation": "'Deren' drückt Besitz aus: die Kollegen, deren Büros renoviert werden. 'Deren' ist der Genitiv für Plural sowohl Maskulin als auch Feminin."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Die sorgfältig ____ Daten wurden veröffentlicht.",
        "options": [
            "analysierten",
            "analysiert",
            "analysierende",
            "analysierte"
        ],
        "correctAnswer": "analysierten",
        "explanation": "Das Partizip-Adjektiv muss mit dem Plural-Nomen 'Daten' übereinstimmen. Nach 'die' im Nominativ Plural ist die Adjektivendung '-en'."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Das ist der Wissenschaftler, ____ Forschung international bekannt ist.",
        "options": ["dessen", "deren", "dem", "den"],
        "correctAnswer": "dessen",
        "explanation": "'Dessen' ist das possessive Relativpronomen für maskuline und neutrale Nomen. Es zeigt Zugehörigkeit: 'dessen Forschung' = 'whose research'."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Die neu ____ Vorschriften gelten ab sofort.",
        "options": [
            "eingeführten",
            "eingeführt",
            "einführenden",
            "eingeführte"
        ],
        "correctAnswer": "eingeführten",
        "explanation": "Das Plural-Nomen 'Vorschriften' erfordert ein dekliniertes Partizip-Adjektiv. Nach 'die' im Nominativ Plural ist die Endung '-en'."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Der Student, ____ ich das Buch gegeben habe, studiert Medizin.",
        "options": ["dem", "den", "dessen", "der"],
        "correctAnswer": "dem",
        "explanation": "Das indirekte Objekt erfordert den Dativ. 'Dem' ist die Dativ-Form für maskulin Singular."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Die während der Sitzung ____ Fragen blieben unbeantwortet.",
        "options": [
            "gestellten",
            "gestellt",
            "stellenden",
            "gestellte"
        ],
        "correctAnswer": "gestellten",
        "explanation": "Das Partizip-Adjektiv modifiziert das Plural-Nomen 'Fragen'. Nach 'die' im Nominativ Plural ist die Endung '-en'."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Die Firma, für ____ er arbeitet, expandiert international.",
        "options": ["die", "der", "deren", "denen"],
        "correctAnswer": "die",
        "explanation": "Die Präposition 'für' erfordert den Akkusativ. 'Die' ist die Akkusativ-Form für feminin Singular."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Die in Berlin ____ Konferenz war ein großer Erfolg.",
        "options": [
            "stattfindende",
            "stattgefunden",
            "stattfinden",
            "stattgefundene"
        ],
        "correctAnswer": "stattfindende",
        "explanation": "Partizip I beschreibt eine andauernde oder gleichzeitige Handlung. 'Die stattfindende Konferenz' — die Konferenz, die stattfindet."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Die Teilnehmer, ____ Namen auf der Liste stehen, erhalten Zutritt.",
        "options": ["deren", "die", "denen", "welchen"],
        "correctAnswer": "deren",
        "explanation": "'Deren' drückt Besitz im Relativsatz aus. 'Deren Namen' = 'whose names'. Korrekt für Nominativ Plural."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Der kürzlich ____ Artikel sorgte für Diskussionen.",
        "options": [
            "veröffentlichte",
            "veröffentlichten",
            "veröffentlichend",
            "veröffentlicht"
        ],
        "correctAnswer": "veröffentlichte",
        "explanation": "Das Singular-Nomen 'Artikel' (maskulin) erfordert ein korrekt dekliniertes Partizip-Adjektiv. Nach 'der' ist die Endung '-e'."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Das Museum, in ____ die Ausstellung stattfindet, ist sehr bekannt.",
        "options": ["dem", "das", "dessen", "den"],
        "correctAnswer": "dem",
        "explanation": "Die Präposition 'in' erfordert hier den Dativ. 'Dem' ist die Dativ-Form für neutral Singular."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Die vom Direktor ____ Entscheidung wurde akzeptiert.",
        "options": [
            "getroffene",
            "getroffenen",
            "treffende",
            "getroffen"
        ],
        "correctAnswer": "getroffene",
        "explanation": "Das Partizip-Adjektiv muss mit dem femininen Singular-Nomen 'Entscheidung' übereinstimmen. Nach 'die' (Nominativ Singular Femininum) ist die Endung '-e'."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Die Mitarbeiter, an ____ Vorschlägen gearbeitet wurde, erhielten eine Prämie.",
        "options": ["deren", "denen", "die", "welche"],
        "correctAnswer": "deren",
        "explanation": "'An deren Vorschlägen' ist die korrekte possessive Relativkonstruktion nach der Präposition. 'Deren' zeigt Zugehörigkeit (der Vorschläge)."
    }
]


def add_qs(topic_json_path, questions, topic_name_str):
    with open(topic_json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    added = 0
    for q in questions:
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
    add_qs('app/src/main/assets/c1_05.json', questions, 'c1_05')
