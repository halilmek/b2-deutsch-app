import json

# Load the file
with open('app/src/main/assets/b2_questions.json') as f:
    data = json.load(f)

# The 20 new Passiv Prateritum questions
new_questions = [
    {
        "id": "b2_10_q001",
        "subjectId": "b2_10",
        "type": "fill_blank",
        "questionText": "Das alte Gebäude _____ im Jahr 1998 abgerissen.",
        "options": ["wurde", "worden", "wird", "war"],
        "correctAnswer": "wurde",
        "explanation": "Grammatik-Thema: Passiv Prateritum",
        "difficulty": "easy",
        "topicName": "Passiv Prateritum"
    },
    {
        "id": "b2_10_q002",
        "subjectId": "b2_10",
        "type": "fill_blank",
        "questionText": "Die Verträge _____ gestern von beiden Seiten unterschrieben.",
        "options": ["wurden", "wurde", "werden", "worden"],
        "correctAnswer": "wurden",
        "explanation": "Grammatik-Thema: Passiv Prateritum",
        "difficulty": "easy",
        "topicName": "Passiv Prateritum"
    },
    {
        "id": "b2_10_q003",
        "subjectId": "b2_10",
        "type": "fill_blank",
        "questionText": "Der Brief _____ vom Direktor persönlich _____.",
        "options": ["wurde geschrieben", "wird geschrieben", "wurde schreiben", "war geschrieben"],
        "correctAnswer": "wurde geschrieben",
        "explanation": "Grammatik-Thema: Passiv Prateritum",
        "difficulty": "easy",
        "topicName": "Passiv Prateritum"
    },
    {
        "id": "b2_10_q004",
        "subjectId": "b2_10",
        "type": "fill_blank",
        "questionText": "Das Fenster _____ während des Sturms _____.",
        "options": ["wurde gebrochen", "wurden gebrochen", "wurde brechen", "wird gebrochen"],
        "correctAnswer": "wurde gebrochen",
        "explanation": "Grammatik-Thema: Passiv Prateritum",
        "difficulty": "easy",
        "topicName": "Passiv Prateritum"
    },
    {
        "id": "b2_10_q005",
        "subjectId": "b2_10",
        "type": "fill_blank",
        "questionText": "Die neuen Regeln _____ letztes Jahr eingeführt.",
        "options": ["werden", "wurden", "wurde", "worden"],
        "correctAnswer": "wurden",
        "explanation": "Grammatik-Thema: Passiv Prateritum",
        "difficulty": "easy",
        "topicName": "Passiv Prateritum"
    },
    {
        "id": "b2_10_q006",
        "subjectId": "b2_10",
        "type": "fill_blank",
        "questionText": "Der Zeuge _____ von der Polizei stundenlang _____.",
        "options": ["wurde befragt", "wurden befragt", "wurde befragen", "wird befragt"],
        "correctAnswer": "wurde befragt",
        "explanation": "Grammatik-Thema: Passiv Prateritum",
        "difficulty": "easy",
        "topicName": "Passiv Prateritum"
    },
    {
        "id": "b2_10_q007",
        "subjectId": "b2_10",
        "type": "fill_blank",
        "questionText": "Das Medikament _____ in den 1980er Jahren _____.",
        "options": ["wurde entwickelt", "werden entwickelt", "wurde entwickeln", "worden entwickelt"],
        "correctAnswer": "wurde entwickelt",
        "explanation": "Grammatik-Thema: Passiv Prateritum",
        "difficulty": "easy",
        "topicName": "Passiv Prateritum"
    },
    {
        "id": "b2_10_q008",
        "subjectId": "b2_10",
        "type": "fill_blank",
        "questionText": "Die Kinder _____ nach dem Unfall sofort _____.",
        "options": ["wurden versorgt", "wurde versorgt", "wurden versorgen", "werden versorgt"],
        "correctAnswer": "wurden versorgt",
        "explanation": "Grammatik-Thema: Passiv Prateritum",
        "difficulty": "easy",
        "topicName": "Passiv Prateritum"
    },
    {
        "id": "b2_10_q009",
        "subjectId": "b2_10",
        "type": "fill_blank",
        "questionText": "Der Dieb _____ von einem Nachbarn _____.",
        "options": ["wurde gesehen", "wurden gesehen", "wurde sehen", "wird gesehen"],
        "correctAnswer": "wurde gesehen",
        "explanation": "Grammatik-Thema: Passiv Prateritum",
        "difficulty": "easy",
        "topicName": "Passiv Prateritum"
    },
    {
        "id": "b2_10_q010",
        "subjectId": "b2_10",
        "type": "fill_blank",
        "questionText": "Das Konzert _____ wegen des Regens _____.",
        "options": ["wurde abgesagt", "wurden abgesagt", "wird abgesagt", "wurde absagen"],
        "correctAnswer": "wurde abgesagt",
        "explanation": "Grammatik-Thema: Passiv Prateritum",
        "difficulty": "easy",
        "topicName": "Passiv Prateritum"
    },
    {
        "id": "b2_10_q011",
        "subjectId": "b2_10",
        "type": "fill_blank",
        "questionText": "Die Brücke _____ vor zehn Jahren von einer berühmten Firma _____.",
        "options": ["wurde gebaut", "werden gebaut", "wurde bauen", "worden gebaut"],
        "correctAnswer": "wurde gebaut",
        "explanation": "Grammatik-Thema: Passiv Prateritum",
        "difficulty": "easy",
        "topicName": "Passiv Prateritum"
    },
    {
        "id": "b2_10_q012",
        "subjectId": "b2_10",
        "type": "fill_blank",
        "questionText": "Alle Dokumente _____ sorgfältig _____.",
        "options": ["wurden geprüft", "wurde geprüft", "werden geprüft", "worden geprüft"],
        "correctAnswer": "wurden geprüft",
        "explanation": "Grammatik-Thema: Passiv Prateritum",
        "difficulty": "easy",
        "topicName": "Passiv Prateritum"
    },
    {
        "id": "b2_10_q013",
        "subjectId": "b2_10",
        "type": "fill_blank",
        "questionText": "Das Problem _____ nicht rechtzeitig _____ werden.",
        "options": ["konnte gelöst", "konnte lösen", "könnte gelöst", "musste lösend"],
        "correctAnswer": "konnte gelöst",
        "explanation": "Grammatik-Thema: Passiv Prateritum",
        "difficulty": "medium",
        "topicName": "Passiv Prateritum"
    },
    {
        "id": "b2_10_q014",
        "subjectId": "b2_10",
        "type": "fill_blank",
        "questionText": "Der Vertrag _____ sofort _____ werden.",
        "options": ["musste unterzeichnet", "müsste unterzeichnet", "musste unterzeichnen", "muss unterzeichnet"],
        "correctAnswer": "musste unterzeichnet",
        "explanation": "Grammatik-Thema: Passiv Prateritum",
        "difficulty": "medium",
        "topicName": "Passiv Prateritum"
    },
    {
        "id": "b2_10_q015",
        "subjectId": "b2_10",
        "type": "fill_blank",
        "questionText": "Die Patienten _____ täglich vom Arzt _____.",
        "options": ["wurden untersucht", "wurde untersucht", "werden untersucht", "worden untersucht"],
        "correctAnswer": "wurden untersucht",
        "explanation": "Grammatik-Thema: Passiv Prateritum",
        "difficulty": "easy",
        "topicName": "Passiv Prateritum"
    },
    {
        "id": "b2_10_q016",
        "subjectId": "b2_10",
        "type": "fill_blank",
        "questionText": "Das gestohlene Auto _____ drei Tage später _____.",
        "options": ["wurde gefunden", "wurden gefunden", "wurde finden", "wird gefunden"],
        "correctAnswer": "wurde gefunden",
        "explanation": "Grammatik-Thema: Passiv Prateritum",
        "difficulty": "easy",
        "topicName": "Passiv Prateritum"
    },
    {
        "id": "b2_10_q017",
        "subjectId": "b2_10",
        "type": "fill_blank",
        "questionText": "Der Fehler _____ erst nach langer Zeit _____.",
        "options": ["wurde bemerkt", "wurden bemerkt", "wurde bemerken", "wird bemerkt"],
        "correctAnswer": "wurde bemerkt",
        "explanation": "Grammatik-Thema: Passiv Prateritum",
        "difficulty": "easy",
        "topicName": "Passiv Prateritum"
    },
    {
        "id": "b2_10_q018",
        "subjectId": "b2_10",
        "type": "fill_blank",
        "questionText": "Die Ausstellung _____ von Tausenden von Besuchern _____.",
        "options": ["wurde besucht", "wurden besucht", "wurde besuchen", "wird besucht"],
        "correctAnswer": "wurde besucht",
        "explanation": "Grammatik-Thema: Passiv Prateritum",
        "difficulty": "easy",
        "topicName": "Passiv Prateritum"
    },
    {
        "id": "b2_10_q019",
        "subjectId": "b2_10",
        "type": "fill_blank",
        "questionText": "Das Essen _____ pünktlich um 12 Uhr _____.",
        "options": ["wurde serviert", "wurden serviert", "wurde servieren", "werden serviert"],
        "correctAnswer": "wurde serviert",
        "explanation": "Grammatik-Thema: Passiv Prateritum",
        "difficulty": "easy",
        "topicName": "Passiv Prateritum"
    },
    {
        "id": "b2_10_q020",
        "subjectId": "b2_10",
        "type": "fill_blank",
        "questionText": "Die Nachrichten _____ gestern Abend im Radio _____.",
        "options": ["wurden übertragen", "wurde übertragen", "wurden übertragen werden", "worden übertragen"],
        "correctAnswer": "wurden übertragen",
        "explanation": "Grammatik-Thema: Passiv Prateritum",
        "difficulty": "medium",
        "topicName": "Passiv Prateritum"
    }
]

# Step 1: Remove all existing b2_10 questions from questionBank
original_count = len(data['questionBank'])
data['questionBank'] = [q for q in data['questionBank'] if not q['id'].startswith('b2_10')]
removed_count = original_count - len(data['questionBank'])
print(f"Removed {removed_count} old b2_10 questions from questionBank")

# Step 2: Add new questions to questionBank
data['questionBank'].extend(new_questions)
print(f"Added {len(new_questions)} new questions")

# Step 3: Update topic metadata
data['topics']['b2_10']['count'] = len(new_questions)
data['topics']['b2_10']['questionIds'] = [q['id'] for q in new_questions]
print(f"Updated b2_10 topic count to {len(new_questions)}")

# Step 4: Update totalQuestions
data['totalQuestions'] = len(data['questionBank'])
print(f"Updated totalQuestions to {data['totalQuestions']}")

# Save
with open('app/src/main/assets/b2_questions.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Done! File saved.")
