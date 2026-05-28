import json

questions = [
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Du ____ die Tür abschliessen, bevor du gehst.",
        "options": ["musst", "darfst", "magst", "kannst"],
        "correctAnswer": "musst",
        "explanation": "'Muessen' expresses obligation or necessity."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Er ____ schon zu Hause sein, denn das Licht brennt.",
        "options": ["muss", "darf", "soll", "mag"],
        "correctAnswer": "muss",
        "explanation": "Here 'muss' expresses a logical assumption or strong probability based on evidence."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Man ____ während der Pruefung keine Handys benutzen.",
        "options": ["darf", "muss", "kann", "mag"],
        "correctAnswer": "darf",
        "explanation": "'Nicht duerfen' expresses prohibition."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Sie ____ gestern sehr beschaeftigt gewesen sein.",
        "options": ["muss", "kann", "mag", "will"],
        "correctAnswer": "muss",
        "explanation": "'Muss gewesen sein' expresses a strong assumption about the past — subjective epistemic use of 'muessen'."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Du ____ heute frueher gehen, wenn du moechtest.",
        "options": ["darfst", "musst", "sollst", "magst"],
        "correctAnswer": "darfst",
        "explanation": "'DuERfen' is used to give permission in the du-form."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Er ____ angeblich drei Sprachen fliessend sprechen.",
        "options": ["soll", "muss", "mag", "darf"],
        "correctAnswer": "soll",
        "explanation": "'Sollen' can express reported information or hearsay — subjective use to report third-party claims."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Das ____ durchaus moeglich sein.",
        "options": ["kann", "muss", "will", "darf"],
        "correctAnswer": "kann",
        "explanation": "'Kann' expresses possibility or epistemic openness."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Du ____ mehr Wasser trinken; das waere gesuender.",
        "options": ["solltest", "musst", "willst", "magst"],
        "correctAnswer": "solltest",
        "explanation": "'Sollten' is the standard advisory form for recommendations and polite advice."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Er ____ die Wahrheit gesagt haben, aber sicher bin ich nicht.",
        "options": ["mag", "muss", "soll", "will"],
        "correctAnswer": "mag",
        "explanation": "'Mag' expresses a weak assumption or possibility — concessive epistemic use in C1."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Die Teilnehmer ____ ihre Ergebnisse bis Freitag einreichen.",
        "options": ["muessen", "duerfen", "moegen", "wollen"],
        "correctAnswer": "muessen",
        "explanation": "'Muessen' expresses obligation or necessity in formal/regulatory contexts."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Er ____ sich weigern, daran teilzunehmen.",
        "options": ["will", "muss", "darf", "mag"],
        "correctAnswer": "will",
        "explanation": "'Wollen' in this context expresses intention or determination."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Das Wetter ____ morgen besser werden.",
        "options": ["soll", "muss", "mag", "will"],
        "correctAnswer": "soll",
        "explanation": "'Sollen' is used for reported forecasts, expectations, or predictions from third-party sources."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Sie ____ die Nachricht uebersehen haben, anders kann ich es mir nicht erklaeren.",
        "options": ["muss", "darf", "will", "soll"],
        "correctAnswer": "muss",
        "explanation": "'Muss ... haben' (epistemic Perfekt) expresses a logical conclusion about a past event."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Du ____ ruhig ehrlich sein; niemand wird dich verurteilen.",
        "options": ["kannst", "musst", "willst", "magst"],
        "correctAnswer": "kannst",
        "explanation": "'Kannst' expresses possibility, permission, or gentle encouragement here."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Er ____ frueher sehr reich gewesen sein.",
        "options": ["soll", "darf", "will", "muss"],
        "correctAnswer": "soll",
        "explanation": "'Soll ... gewesen sein' expresses reported information or hearsay — a third-party claim."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Niemand ____ den Raum ohne Erlaubnis betreten.",
        "options": ["darf", "muss", "mag", "kann"],
        "correctAnswer": "darf",
        "explanation": "'Nicht duerfen' indicates strict prohibition in formal/regulatory contexts."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Die Ergebnisse ____ sich noch aendern.",
        "options": ["koennen", "muessen", "wollen", "sollen"],
        "correctAnswer": "koennen",
        "explanation": "'Koennen' expresses possibility or potential for change."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Du ____ dich nicht so aufregen; alles wird gut.",
        "options": ["musst", "darfst", "willst", "magst"],
        "correctAnswer": "musst",
        "explanation": "'Du musst dich nicht aufregen' means 'you don't need to get upset' — negation of necessity, not obligation."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Er ____ die ganze Nacht gearbeitet haben, so muede wie er aussieht.",
        "options": ["muss", "mag", "soll", "darf"],
        "correctAnswer": "muss",
        "explanation": "'Muss gearbeitet haben' expresses a strong logical conclusion about the past based on visible evidence (epistemic Perfekt)."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Sie ____ ihre Meinung jederzeit aendern, wenn sie moechte.",
        "options": ["kann", "muss", "soll", "mag"],
        "correctAnswer": "kann",
        "explanation": "'Kann' expresses ability or personal possibility in polite contexts."
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
    add_qs('app/src/main/assets/c1_06.json', questions, 'c1_06')
