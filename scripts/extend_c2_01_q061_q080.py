import json

with open('app/src/main/assets/c2_01.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

existing_count = len(data['questions'])
print(f"Existing questions: {existing_count}")

new_questions = [
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Die Forscher diskutierten intensiv ueber die Ergebnisse. -> Im akademischen Nominalstil: Die intensive ____ der Ergebnisse erfolgte durch die Forscher.",
        "options": [
            "Diskussion",
            "diskutieren",
            "diskutierte",
            "diskutierend"
        ],
        "correctAnswer": "Diskussion",
        "explanation": "Nominalstil replaces the verb 'diskutieren' with the noun 'Diskussion'.",
        "id": "c2_01_q061"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Die Regierung analysierte die Auswirkungen der Reform. -> Die ____ der Auswirkungen der Reform wurde von der Regierung durchgefuehrt.",
        "options": [
            "Analyse",
            "Analysierung",
            "Analytik",
            "Analysieren"
        ],
        "correctAnswer": "Analyse",
        "explanation": "In formal academic German, 'Analyse' is the preferred nominalization of 'analysieren'.",
        "id": "c2_01_q062"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welche Formulierung entspricht am staerksten dem akademischen Nominalstil?",
        "options": [
            "Die Studierenden untersuchten das Phaenomen.",
            "Die Untersuchung des Phaenomens erfolgte durch die Studierenden.",
            "Die Studierenden haben das Phaenomen genau untersucht.",
            "Die Studierenden waren dabei, das Phaenomen zu untersuchen."
        ],
        "correctAnswer": "Die Untersuchung des Phaenomens erfolgte durch die Studierenden.",
        "explanation": "Academic Nominalstil favors nouns over finite verbs.",
        "id": "c2_01_q063"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Die Wissenschaftler entwickelten ein neues Modell. -> Durch die Wissenschaftler erfolgte die ____ eines neuen Modells.",
        "options": [
            "Entwicklung",
            "Entwickeln",
            "Entwickelung",
            "Entwickeltheit"
        ],
        "correctAnswer": "Entwicklung",
        "explanation": "The noun 'Entwicklung' is the standard nominalization of 'entwickeln'.",
        "id": "c2_01_q064"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Die Daten wurden ausgewertet. -> Die ____ der Daten ergab signifikante Unterschiede.",
        "options": [
            "Auswertung",
            "Auswerten",
            "Ausgewertetheit",
            "Auswerte"
        ],
        "correctAnswer": "Auswertung",
        "explanation": "Nominalstil often uses nouns such as 'Auswertung' instead of verbal constructions.",
        "id": "c2_01_q065"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welche Variante ist typischer fuer wissenschaftliche Texte?",
        "options": [
            "Man verglich die Ergebnisse miteinander.",
            "Es wurden die Ergebnisse miteinander verglichen.",
            "Der Vergleich der Ergebnisse wurde vorgenommen.",
            "Die Ergebnisse verglich man miteinander."
        ],
        "correctAnswer": "Der Vergleich der Ergebnisse wurde vorgenommen.",
        "explanation": "The nominalized form 'Vergleich' is characteristic of academic writing.",
        "id": "c2_01_q066"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Die Forscher ueberprueften die Hypothese erneut. -> Die erneute ____ der Hypothese erfolgte durch die Forscher.",
        "options": [
            "Ueberpruefung",
            "Ueberpruefen",
            "Ueberpruefbarkeit",
            "Ueberprueftheit"
        ],
        "correctAnswer": "Ueberpruefung",
        "explanation": "The noun 'Ueberpruefung' is the correct nominal form.",
        "id": "c2_01_q067"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Die Teilnehmer beantworteten die Fragen. -> Die ____ der Fragen durch die Teilnehmer erfolgte anonym.",
        "options": [
            "Beantwortung",
            "Antwort",
            "Antwortung",
            "Beantworten"
        ],
        "correctAnswer": "Beantwortung",
        "explanation": "The nominalized process noun is 'Beantwortung'.",
        "id": "c2_01_q068"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welche Formulierung weist die hoechste Nominaldichte auf?",
        "options": [
            "Die Autoren beschrieben die Methode.",
            "Die Autoren haben die Methode beschrieben.",
            "Die Beschreibung der Methode erfolgte durch die Autoren.",
            "Die Methode wurde von den Autoren beschrieben."
        ],
        "correctAnswer": "Die Beschreibung der Methode erfolgte durch die Autoren.",
        "explanation": "Nominal density increases when actions are expressed through nouns.",
        "id": "c2_01_q069"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Die Kommission entschied ueber den Antrag. -> Die ____ ueber den Antrag wurde von der Kommission getroffen.",
        "options": [
            "Entscheidung",
            "Entscheid",
            "Entscheiden",
            "Entschlossenheit"
        ],
        "correctAnswer": "Entscheidung",
        "explanation": "The noun 'Entscheidung' replaces the verb phrase.",
        "id": "c2_01_q070"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Die Wissenschaftler stellten fest, dass die Werte anstiegen. Welche Nominalisierung ist am angemessensten?",
        "options": [
            "Die Feststellung eines Anstiegs der Werte",
            "Das Feststellen, dass die Werte anstiegen",
            "Die Werteanstiegfeststellung",
            "Die festgestellten Werteanstiege"
        ],
        "correctAnswer": "Die Feststellung eines Anstiegs der Werte",
        "explanation": "This is the most idiomatic academic nominalization.",
        "id": "c2_01_q071"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Die Forscher kamen zu dem Schluss, dass weitere Studien noetig sind. -> Die ____ der Notwendigkeit weiterer Studien erfolgte auf Grundlage der Ergebnisse.",
        "options": [
            "Feststellung",
            "Festlegung",
            "Festigung",
            "Festsetzung"
        ],
        "correctAnswer": "Feststellung",
        "explanation": "Academic writing often uses 'Feststellung' to express findings or conclusions.",
        "id": "c2_01_q072"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welche Variante entspricht am ehesten dem C2-Nominalstil?",
        "options": [
            "Die Forscher fuehrten Interviews durch.",
            "Die Durchfuehrung von Interviews erfolgte durch die Forscher.",
            "Die Forscher interviewten Personen.",
            "Interviews wurden gemacht."
        ],
        "correctAnswer": "Die Durchfuehrung von Interviews erfolgte durch die Forscher.",
        "explanation": "The nominalized structure is most characteristic of academic discourse.",
        "id": "c2_01_q073"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Die Experten bewerteten die Risiken. -> Die ____ der Risiken durch die Experten bildete die Grundlage der Entscheidung.",
        "options": [
            "Bewertung",
            "Bewertbarkeit",
            "Bewerten",
            "Bewertetheit"
        ],
        "correctAnswer": "Bewertung",
        "explanation": "The noun 'Bewertung' is the correct academic nominalization.",
        "id": "c2_01_q074"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Die Forscher beobachteten Veraenderungen im Verhalten. -> Die ____ von Verhaltensveraenderungen wurde dokumentiert.",
        "options": [
            "Beobachtung",
            "Beobachten",
            "Beobachtbarkeit",
            "Beobachterschaft"
        ],
        "correctAnswer": "Beobachtung",
        "explanation": "The nominalized noun is 'Beobachtung'.",
        "id": "c2_01_q075"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welche Formulierung vermeidet Verben am staerksten?",
        "options": [
            "Die Studie zeigte deutliche Unterschiede.",
            "Die Studie hat deutliche Unterschiede gezeigt.",
            "Die Studie konnte deutliche Unterschiede zeigen.",
            "Der Nachweis deutlicher Unterschiede gelang im Rahmen der Studie."
        ],
        "correctAnswer": "Der Nachweis deutlicher Unterschiede gelang im Rahmen der Studie.",
        "explanation": "The key action is expressed through the noun 'Nachweis'.",
        "id": "c2_01_q076"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Die Forscher interpretierten die Ergebnisse unterschiedlich. -> Die unterschiedliche ____ der Ergebnisse fuehrte zu Kontroversen.",
        "options": [
            "Interpretation",
            "Interpretierung",
            "Interpretieren",
            "Interpretiertheit"
        ],
        "correctAnswer": "Interpretation",
        "explanation": "The standard noun is 'Interpretation'.",
        "id": "c2_01_q077"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Die Universitaet fuehrte eine Evaluation des Programms durch. Welche Variante ist staerker nominalisiert?",
        "options": [
            "Die Universitaet evaluierte das Programm.",
            "Die Evaluation des Programms erfolgte durch die Universitaet.",
            "Die Universitaet hat das Programm evaluiert.",
            "Das Programm wurde evaluiert."
        ],
        "correctAnswer": "Die Evaluation des Programms erfolgte durch die Universitaet.",
        "explanation": "The noun 'Evaluation' creates a more academic nominal style.",
        "id": "c2_01_q078"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Die Autoren argumentierten fuer eine Reform. -> Die ____ zugunsten einer Reform wurde ausfuehrlich begruendet.",
        "options": [
            "Argumentation",
            "Argumentierung",
            "Argument",
            "Argumentieren"
        ],
        "correctAnswer": "Argumentation",
        "explanation": "The process noun 'Argumentation' is preferred in academic writing.",
        "id": "c2_01_q079"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welche Formulierung weist die hoechste akademische Verdichtung auf?",
        "options": [
            "Man untersuchte die Ursachen und analysierte die Folgen.",
            "Die Ursachen wurden untersucht und die Folgen analysiert.",
            "Die Untersuchung der Ursachen sowie die Analyse der Folgen erfolgten.",
            "Es gab eine Untersuchung der Ursachen und man analysierte die Folgen."
        ],
        "correctAnswer": "Die Untersuchung der Ursachen sowie die Analyse der Folgen erfolgten.",
        "explanation": "This sentence contains two central nominalizations and represents a highly condensed academic style.",
        "id": "c2_01_q080"
    }
]

data['questions'].extend(new_questions)
data['totalQuestions'] = len(data['questions'])

with open('app/src/main/assets/c2_01.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(new_questions)} questions (q061-q080)")
print(f"Total questions now: {data['totalQuestions']}")
easy = sum(1 for q in data['questions'] if q['difficulty'] == 'easy')
medium = sum(1 for q in data['questions'] if q['difficulty'] == 'medium')
hard = sum(1 for q in data['questions'] if q['difficulty'] == 'hard')
print(f"Difficulty breakdown: easy={easy}, medium={medium}, hard={hard}")