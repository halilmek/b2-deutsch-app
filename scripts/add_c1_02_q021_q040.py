import json
import sys

with open('app/src/main/assets/c1_02.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

existing_ids = {q['id'] for q in data['questions']}
print(f"Existing questions: {len(data['questions'])}, IDs: {min(existing_ids)}-{max(existing_ids)}")

next_id = 21

questions_raw = [
    {"difficulty": "easy", "type": "multiple_choice", "questionText": "Der Sprecher sagte, er ____ morgen an der Konferenz teil.", "options": ["nehme", "nimmt", "nähme", "genommen habe"], "correctAnswer": "nehme", "explanation": "Konjunktiv I is used in indirect speech to report statements neutrally."},
    {"difficulty": "medium", "type": "multiple_choice", "questionText": "Die Journalistin berichtete, der Minister ____ keine weiteren Kommentare abgeben.", "options": ["werde", "wird", "würde", "worden sei"], "correctAnswer": "werde", "explanation": "Future statements in indirect speech often use 'werde' in Konjunktiv I."},
    {"difficulty": "easy", "type": "multiple_choice", "questionText": "Er behauptete, er ____ die Unterlagen bereits abgeschickt.", "options": ["habe", "hat", "hätte", "sei"], "correctAnswer": "habe", "explanation": "Perfect tense in indirect speech uses Konjunktiv I auxiliary forms like 'habe'."},
    {"difficulty": "medium", "type": "multiple_choice", "questionText": "Die Experten erklärten, die Situation ____ sich bald verbessern.", "options": ["werde", "würde", "wird", "verbessere"], "correctAnswer": "werde", "explanation": "Indirect future statements require Konjunktiv I with 'werde'."},
    {"difficulty": "easy", "type": "multiple_choice", "questionText": "Sie sagte, sie ____ mit dem Ergebnis nicht zufrieden.", "options": ["sei", "ist", "wäre", "gewesen sei"], "correctAnswer": "sei", "explanation": "The verb 'sein' changes to 'sei' in Konjunktiv I."},
    {"difficulty": "medium", "type": "multiple_choice", "questionText": "Der Zeuge erklärte, er ____ den Täter nicht erkennen können.", "options": ["habe", "hatte", "hätte", "sei"], "correctAnswer": "habe", "explanation": "Indirect speech in the perfect tense uses Konjunktiv I forms."},
    {"difficulty": "hard", "type": "multiple_choice", "questionText": "Die Mitarbeiter teilten mit, sie ____ nächste Woche im Homeoffice arbeiten.", "options": ["würden", "werden", "arbeiteten", "arbeiteten würden"], "correctAnswer": "würden", "explanation": "Konjunktiv II with 'würden' is often used when Konjunktiv I sounds identical to indicative."},
    {"difficulty": "hard", "type": "multiple_choice", "questionText": "Er meinte, die Entscheidung ____ bereits getroffen worden.", "options": ["sei", "ist", "wäre", "worde"], "correctAnswer": "sei", "explanation": "Passive perfect constructions in indirect speech use 'sei ... worden'."},
    {"difficulty": "hard", "type": "multiple_choice", "questionText": "Die Professorin sagte, die Studenten ____ die Aufgabe bis Freitag abgeben.", "options": ["müssten", "müssen", "mussten", "müssten haben"], "correctAnswer": "müssten", "explanation": "Konjunktiv II is used here because the Konjunktiv I form would be identical to indicative."},
    {"difficulty": "easy", "type": "multiple_choice", "questionText": "Er erklärte, er ____ keine Zeit für ein weiteres Gespräch.", "options": ["habe", "hat", "hätte", "sei"], "correctAnswer": "habe", "explanation": "Indirect speech requires Konjunktiv I where possible."},
    {"difficulty": "medium", "type": "multiple_choice", "questionText": "Die Politikerin betonte, man ____ dringend neue Maßnahmen ergreifen.", "options": ["müsse", "muss", "musste", "müsste"], "correctAnswer": "müsse", "explanation": "The modal verb appears in Konjunktiv I as 'müsse'."},
    {"difficulty": "medium", "type": "multiple_choice", "questionText": "Der Sprecher behauptete, das Unternehmen ____ niemals gegen das Gesetz verstoßen.", "options": ["habe", "hat", "hätte", "sei"], "correctAnswer": "habe", "explanation": "Perfect tense in indirect speech uses Konjunktiv I auxiliary verbs."},
    {"difficulty": "hard", "type": "multiple_choice", "questionText": "Sie erklärte, die Ergebnisse ____ noch überprüft werden.", "options": ["müssten", "müssen", "mussten", "müssten worden"], "correctAnswer": "müssten", "explanation": "Konjunktiv II is used because Konjunktiv I would sound identical to indicative."},
    {"difficulty": "medium", "type": "multiple_choice", "questionText": "Der Arzt sagte, der Patient ____ sich ausreichend erholen.", "options": ["solle", "soll", "sollte", "hätte sollen"], "correctAnswer": "solle", "explanation": "The modal verb 'sollen' becomes 'solle' in Konjunktiv I."},
    {"difficulty": "medium", "type": "multiple_choice", "questionText": "Die Zeitung schrieb, die Regierung ____ eine Reform geplant.", "options": ["habe", "hat", "hätte", "sei"], "correctAnswer": "habe", "explanation": "Indirect speech in reported writing typically uses Konjunktiv I."},
    {"difficulty": "easy", "type": "multiple_choice", "questionText": "Er behauptete, er ____ von den Problemen nichts gewusst.", "options": ["habe", "hatte", "hätte", "sei"], "correctAnswer": "habe", "explanation": "Konjunktiv I perfect tense is formed with 'habe' + participle."},
    {"difficulty": "hard", "type": "multiple_choice", "questionText": "Die Forscher erklärten, die Daten ____ eindeutig interpretiert werden.", "options": ["könnten", "können", "konnten", "könnten haben"], "correctAnswer": "könnten", "explanation": "Konjunktiv II is used to avoid ambiguity with indicative forms."},
    {"difficulty": "easy", "type": "multiple_choice", "questionText": "Sie sagte, ihr Bruder ____ derzeit im Ausland.", "options": ["arbeite", "arbeitet", "arbeitete", "habe gearbeitet"], "correctAnswer": "arbeite", "explanation": "The verb 'arbeiten' changes to 'arbeite' in Konjunktiv I."},
    {"difficulty": "hard", "type": "multiple_choice", "questionText": "Der Reporter berichtete, der Unfall ____ durch einen technischen Defekt verursacht worden.", "options": ["sei", "ist", "wäre", "worden sei"], "correctAnswer": "sei", "explanation": "Passive perfect indirect speech uses 'sei ... worden'."},
    {"difficulty": "medium", "type": "multiple_choice", "questionText": "Die Studentin meinte, sie ____ die Prüfung ohne Probleme bestehen.", "options": ["werde", "würde", "wird", "bestünde"], "correctAnswer": "werde", "explanation": "Future meaning in indirect speech is expressed with 'werde'."}
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
