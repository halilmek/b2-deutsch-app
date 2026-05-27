import json

with open('app/src/main/assets/c1_02.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

existing_ids = {q['id'] for q in data['questions']}
print(f"Current: {len(data['questions'])} questions, IDs: {min(existing_ids)}-{max(existing_ids)}")

next_id = 41

questions_raw = [
    {"difficulty": "easy", "type": "multiple_choice", "questionText": "Der Zeuge sagte, er ____ den Vorfall klar gesehen.", "options": ["habe", "hat", "hätte", "sei"], "correctAnswer": "habe", "explanation": "Perfect tense with Konjunktiv I auxiliary 'habe' is used in indirect speech for witnessed events."},
    {"difficulty": "medium", "type": "multiple_choice", "questionText": "Die Behörde teilte mit, die Genehmigung ____ bis Ende des Jahres verlängert.", "options": ["werde", "wird", "würde", "worden sei"], "correctAnswer": "werde", "explanation": "Future passive in indirect speech uses Konjunktiv I of 'werden' + past participle."},
    {"difficulty": "easy", "type": "multiple_choice", "questionText": "Er erwähnte, dass er ____ nach Berlin reisen müsse.", "options": ["solle", "soll", "sollte", "hätte sollen"], "correctAnswer": "solle", "explanation": "Modal verb 'sollen' becomes 'solle' in Konjunktiv I for reported obligation."},
    {"difficulty": "medium", "type": "multiple_choice", "questionText": "Die Stadtverwaltung gab bekannt, das Projekt ____ im nächsten Monat starten.", "options": ["werde", "würde", "fange", "habe angefangen"], "correctAnswer": "werde", "explanation": "Future statements in indirect speech use Konjunktiv I of 'werden'."},
    {"difficulty": "easy", "type": "multiple_choice", "questionText": "Sie behauptete, sie ____ den Vertrag bereits unterschrieben.", "options": ["habe", "hat", "hätte", "sei"], "correctAnswer": "habe", "explanation": "'Habe' is the Konjunktiv I form of 'haben' used in indirect speech perfect tense."},
    {"difficulty": "medium", "type": "multiple_choice", "questionText": "Der Experte meinte, die Studie ____ keine eindeutigen Ergebnisse liefern.", "options": ["könne", "kann", "könnte", "habe gekonnt"], "correctAnswer": "könne", "explanation": "Modal verb 'können' becomes 'könne' in Konjunktiv I 3rd person singular."},
    {"difficulty": "hard", "type": "multiple_choice", "questionText": "Man berichtete, der Chef ____ sich über die Verzögerung beschwert.", "options": ["habe", "hätte", "würde", "habe gehabt"], "correctAnswer": "habe", "explanation": "Reflexive verbs in perfect tense indirect speech use 'habe' + participle + 'sich', preserving Konjunktiv I."},
    {"difficulty": "medium", "type": "multiple_choice", "questionText": "Der Richter erklärte, der Angeklagte ____ unschuldig gewesen.", "options": ["sei", "ist", "wäre", "gewesen sei"], "correctAnswer": "sei", "explanation": "'Sei' is the Konjunktiv I form of 'sein' for past statements in indirect speech."},
    {"difficulty": "easy", "type": "multiple_choice", "questionText": "Die Zeitung meldete, der Preis ____ um zehn Prozent gestiegen.", "options": ["sei", "ist", "wäre", "worden sei"], "correctAnswer": "sei", "explanation": "For movement verbs in perfect tense, 'sein' becomes 'sei' in indirect speech."},
    {"difficulty": "medium", "type": "multiple_choice", "questionText": "Er teilte mit, er ____ am Wochenende nicht erreichbar.", "options": ["sei", "ist", "wäre", "habe sein"], "correctAnswer": "sei", "explanation": "State-of-being verbs use 'sei' (Konjunktiv I of 'sein') in reported speech."},
    {"difficulty": "hard", "type": "multiple_choice", "questionText": "Der Analyst sagte, der Markt ____ sich in den nächsten Monaten erholen.", "options": ["werde", "wolle", "würde", "wollte"], "correctAnswer": "werde", "explanation": "'Werden' + infinitive (Konjunktiv II form sometimes preferred stylistically) is common in professional news reporting when Konjunktiv I would be ambiguous."},
    {"difficulty": "hard", "type": "multiple_choice", "questionText": "Der Generalsekretär betonte, alle Mitgliedsstaaten ____ die Vereinbarung einhalten.", "options": ["müssten", "müssen", "mussten", "werden müssen"], "correctAnswer": "müssten", "explanation": "Konjunktiv II 'müssten' used to avoid confusion with indicative 'müssen' in formal reported speech."},
    {"difficulty": "medium", "type": "multiple_choice", "questionText": "Sie schrieb, ihr Anwalt ____ sich um den Fall kümmern.", "options": ["werde", "wolle", "würde", "wollte"], "correctAnswer": "werde", "explanation": "Future-in-the-past in indirect speech where 'werden' + infinitive preserves future meaning in reported speech."},
    {"difficulty": "easy", "type": "multiple_choice", "questionText": "Er meinte, das Auto ____ in der Werkstatt.", "options": ["sei", "ist", "wäre", "gewesen sei"], "correctAnswer": "sei", "explanation": "Location statements use 'sei' (Konjunktiv I of 'sein') in indirect speech."},
    {"difficulty": "medium", "type": "multiple_choice", "questionText": "Der Fahrer gab an, er ____ nur Schrittgeschwindigkeit gefahren.", "options": ["habe", "hat", "hätte", "sei"], "correctAnswer": "habe", "explanation": "When 'haben' is the main verb, 'habe' in Konjunktiv I reports the statement exactly."},
    {"difficulty": "hard", "type": "multiple_choice", "questionText": "Die Kommission sei der Meinung, die Vorschriften ____ dringend überarbeitet werden.", "options": ["müssten", "müssen", "mussten", "werden müssten"], "correctAnswer": "müssten", "explanation": "Konjunktiv II is required when the Konjunktiv I form of a modal verb ('müssen') is identical to the indicative."},
    {"difficulty": "medium", "type": "multiple_choice", "questionText": "Das Ministerium teilte mit, die Öffnungszeiten ____ geändert.", "options": ["seien", "sind", "wären", "worden seien"], "correctAnswer": "seien", "explanation": "Plural passive in indirect speech uses 'seien' + past participle, the Konjunktiv I form of 'sein'."},
    {"difficulty": "easy", "type": "multiple_choice", "questionText": "Sie erwähnte, ihr Mann ____ Arzt von Beruf.", "options": ["sei", "ist", "wäre", "gewesen sei"], "correctAnswer": "sei", "explanation": "Stative sentences use 'sei' in Konjunktiv I for profession or permanent state reports."},
    {"difficulty": "hard", "type": "multiple_choice", "questionText": "Er erklärte, seine Kollegin ____ die Aufgabe bereits erledigt.", "options": ["habe", "hat", "hätte", "hätte gehabt"], "correctAnswer": "habe", "explanation": "Perfect tense passive in indirect speech uses 'habe' + past participle (with 'worden' omitted in shorthand constructions)."},
    {"difficulty": "medium", "type": "multiple_choice", "questionText": "Die Vertreterin sagte, sie ____ sich für die Lösung einsetzen.", "options": ["werde", "würde", "setze ein", "setze sich ein"], "correctAnswer": "werde", "explanation": "Future reflexive statements in indirect speech use 'werde' + reflexive infinitive to preserve the intended action."}
]

for q in questions_raw:
    q["id"] = f"c1_02_q{str(next_id).zfill(3)}"
    next_id += 1

data['questions'].extend(questions_raw)
data['totalQuestions'] = len(data['questions'])

with open('app/src/main/assets/c1_02.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(questions_raw)} questions. New total: {data['totalQuestions']}")
print(f"IDs: {questions_raw[0]['id']} — {questions_raw[-1]['id']}")
