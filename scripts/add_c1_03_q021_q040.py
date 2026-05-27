import json

with open('app/src/main/assets/c1_03.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Current: {len(data['questions'])} questions")

next_id = 21

questions_raw = [
    {"difficulty": "easy", "type": "multiple_choice", "questionText": "Dieses Problem ____ leicht loesen.", "options": ["laesst sich", "wird", "ist", "hat sich"], "correctAnswer": "laesst sich", "explanation": "The structure 'sich lassen + Infinitiv' is a common passive substitute meaning 'can be done'."},
    {"difficulty": "easy", "type": "multiple_choice", "questionText": "Die Aufgabe ist bis morgen ____.", "options": ["zu erledigen", "erledigt werden", "erledigen", "zu erledigt"], "correctAnswer": "zu erledigen", "explanation": "The structure 'sein + zu + Infinitiv' functions as a passive replacement."},
    {"difficulty": "easy", "type": "multiple_choice", "questionText": "Das Auto ____ problemlos fahren.", "options": ["laesst sich", "ist zu", "wird", "hat sich"], "correctAnswer": "laesst sich", "explanation": "'Sich lassen + Infinitiv' expresses possibility in a passive-like meaning."},
    {"difficulty": "medium", "type": "multiple_choice", "questionText": "Die Formulare sind online ____.", "options": ["auszufuellen", "ausgefuellt werden", "ausfuellen", "ausgefuellt zu"], "correctAnswer": "auszufuellen", "explanation": "'Sein + zu + Infinitiv' expresses necessity or possibility."},
    {"difficulty": "easy", "type": "multiple_choice", "questionText": "Der Text ____ schwer verstehen.", "options": ["laesst sich", "ist zu", "wird", "wurde"], "correctAnswer": "laesst sich", "explanation": "This passive substitute means 'can be understood'."},
    {"difficulty": "medium", "type": "multiple_choice", "questionText": "Die Regeln sind unbedingt ____.", "options": ["zu beachten", "beachtet werden", "beachten",], "correctAnswer": "zu beachten", "explanation": "'Sein + zu + Infinitiv' expresses obligation in formal German."},
    {"difficulty": "easy", "type": "multiple_choice", "questionText": "Das Fenster ____ nicht oeffnen.", "options": ["laesst sich", "ist zu", "wird", "hat"], "correctAnswer": "laesst sich", "explanation": "The phrase means 'cannot be opened' in passive meaning."},
    {"difficulty": "medium", "type": "multiple_choice", "questionText": "Die Unterlagen sind bis Freitag ____.", "options": ["einzureichen", "eingereicht werden", "einreichen", "zu eingereicht"], "correctAnswer": "einzureichen", "explanation": "'Sein + zu + Infinitiv' expresses what must be done."},
    {"difficulty": "medium", "type": "multiple_choice", "questionText": "Der Fehler ____ kaum vermeiden.", "options": ["laesst sich", "ist zu", "wird", "sei"], "correctAnswer": "laesst sich", "explanation": "This structure substitutes passive meaning with modal nuance."},
    {"difficulty": "medium", "type": "multiple_choice", "questionText": "Die Maschine ist regelmaessig ____.", "options": ["zu warten", "gewartet werden", "warten",], "correctAnswer": "zu warten", "explanation": "'Sein + zu + Infinitiv' is used for obligations and instructions."},
    {"difficulty": "medium", "type": "multiple_choice", "questionText": "Die Situation ____ nicht einfach erklaeren.", "options": ["laesst sich", "ist zu", "wird", "hat sich"], "correctAnswer": "laesst sich", "explanation": "This passive substitute means 'cannot easily be explained'."},
    {"difficulty": "hard", "type": "multiple_choice", "questionText": "Die Medikamente sind kuehl ____.", "options": ["zu lagern", "gelagert werden", "lagern",], "correctAnswer": "zu lagern", "explanation": "The expression indicates an instruction or requirement."},
    {"difficulty": "hard", "type": "multiple_choice", "questionText": "Das Ergebnis ____ eindeutig interpretieren.", "options": ["laesst sich", "ist zu", "wird", "sei zu"], "correctAnswer": "laesst sich", "explanation": "'Sich lassen + Infinitiv' expresses passive-like possibility."},
    {"difficulty": "hard", "type": "multiple_choice", "questionText": "Die Daten sind vertraulich ____.", "options": ["zu behandeln", "behandelt werden", "behandeln",], "correctAnswer": "zu behandeln", "explanation": "This passive substitute is common in formal instructions."},
    {"difficulty": "easy", "type": "multiple_choice", "questionText": "Die Tuer ____ von innen oeffnen.", "options": ["laesst sich", "ist zu", "wird", "ist"], "correctAnswer": "laesst sich", "explanation": "The phrase means 'can be opened from inside'."},
    {"difficulty": "medium", "type": "multiple_choice", "questionText": "Die Rechnungen sind sofort ____.", "options": ["zu bezahlen", "bezahlt werden", "bezahlen",], "correctAnswer": "zu bezahlen", "explanation": "'Sein + zu + Infinitiv' expresses necessity in a passive sense."},
    {"difficulty": "medium", "type": "multiple_choice", "questionText": "Der Konflikt ____ friedlich loesen.", "options": ["laesst sich", "ist zu", "wird", "hat"], "correctAnswer": "laesst sich", "explanation": "The structure indicates possibility similar to passive voice."},
    {"difficulty": "hard", "type": "multiple_choice", "questionText": "Die Ergebnisse sind genauer ____.", "options": ["zu analysieren", "analysiert werden", "analysieren",], "correctAnswer": "zu analysieren", "explanation": "This construction expresses what should or must be done."},
    {"difficulty": "easy", "type": "multiple_choice", "questionText": "Das Geraet ____ einfach bedienen.", "options": ["laesst sich", "ist zu", "wird", "hat sich"], "correctAnswer": "laesst sich", "explanation": "The phrase means 'can easily be operated'."},
    {"difficulty": "medium", "type": "multiple_choice", "questionText": "Die Antraege sind vollstaendig ____.", "options": ["auszufuellen", "ausgefuellt werden", "ausfuellen",], "correctAnswer": "auszufuellen", "explanation": "'Sein + zu + Infinitiv' is frequently used in official and academic German."}
]

for q in questions_raw:
    q["id"] = f"c1_03_q{str(next_id).zfill(3)}"
    next_id += 1

data['questions'].extend(questions_raw)
data['totalQuestions'] = len(data['questions'])

with open('app/src/main/assets/c1_03.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(questions_raw)} questions. New total: {data['totalQuestions']}")
print(f"IDs: {questions_raw[0]['id']} — {questions_raw[-1]['id']}")
