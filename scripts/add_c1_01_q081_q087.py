import json

with open('app/src/main/assets/c1_01.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

questions_to_add = [
  {
    "difficulty": "easy",
    "type": "multiple_choice",
    "questionText": "Was kennzeichnet den Nominalstil im Deutschen?",
    "options": [
      "Er verwendet überwiegend Verben und persönliche Pronomen.",
      "Er bevorzugt Substantive, Nominalphrasen und passive Konstruktionen.",
      "Er ist typisch für Alltagsgespräche und erzählende Texte.",
      "Er vermeidet abstrakte Begriffe und Fachterminologie."
    ],
    "correctAnswer": "Er bevorzugt Substantive, Nominalphrasen und passive Konstruktionen.",
    "explanation": "Nominalstil is characterized by a preference for nouns over verbs, complex noun phrases, passive voice, and abstract terminology, making it typical for formal, administrative, and academic texts.",
    "id": "c1_01_q081"
  },
  {
    "difficulty": "easy",
    "type": "multiple_choice",
    "questionText": "Welcher Stil wird häufig in der deutschen Verwaltungs- und Amtssprache verwendet?",
    "options": [
      "Verbalstil",
      "Umgangssprachlicher Stil",
      "Nominalstil",
      "Erzählender Stil"
    ],
    "correctAnswer": "Nominalstil",
    "explanation": "Nominalstil is frequently found in German administrative and official language because it conveys precision, formality, and objectivity, as seen in phrases like 'Aufgrund der Nichteinreichung der Unterlagen erfolgt die Ablehnung des Antrags'.",
    "id": "c1_01_q082"
  },
  {
    "difficulty": "easy",
    "type": "multiple_choice",
    "questionText": "Was ist ein Hauptvorteil des Verbalstils?",
    "options": [
      "Er wirkt besonders formell und distanziert.",
      "Er ermöglicht eine höhere Informationsdichte pro Satz.",
      "Er verbessert die Verständlichkeit und den Lesefluss.",
      "Er vermeidet persönliche Ansprache vollständig."
    ],
    "correctAnswer": "Er verbessert die Verständlichkeit und den Lesefluss.",
    "explanation": "Verbalstil uses verbs to describe actions directly, making sentences more dynamic, easier to understand, and more pleasant to read, which is ideal for everyday communication and narrative texts.",
    "id": "c1_01_q083"
  },
  {
    "difficulty": "easy",
    "type": "multiple_choice",
    "questionText": "Welche Transformation ist typisch für die Umwandlung von Verbalstil in Nominalstil?",
    "options": [
      "Verben werden durch Adjektive ersetzt.",
      "Verben werden in Substantive umgewandelt (z. B. 'analysieren' → 'die Analyse').",
      "Substantive werden in Verben umgewandelt.",
      "Präpositionen werden durch Konjunktionen ersetzt."
    ],
    "correctAnswer": "Verben werden in Substantive umgewandelt (z. B. 'analysieren' → 'die Analyse').",
    "explanation": "A core transformation rule for creating Nominalstil is nominalizing verbs—turning action words into nouns (e.g., 'analysieren' becomes 'die Analyse'), which increases formality and density.",
    "id": "c1_01_q084"
  },
  {
    "difficulty": "easy",
    "type": "multiple_choice",
    "questionText": "Welcher Stil vermeidet persönliche Pronomen wie 'wir', 'ich' oder 'man'?",
    "options": [
      "Verbalstil",
      "Nominalstil",
      "Umgangssprachlicher Stil",
      "Poetischer Stil"
    ],
    "correctAnswer": "Nominalstil",
    "explanation": "Nominalstil avoids personal pronouns to create distance and formality, preferring impersonal constructions like 'es erfolgt...' or 'die Durchführung...'.",
    "id": "c1_01_q085"
  },
  {
    "difficulty": "easy",
    "type": "multiple_choice",
    "questionText": "Was ist ein typisches Merkmal des Verbalstils?",
    "options": [
      "Häufige Verwendung von Partizipialattributen",
      "Komplexe Präpositionalgefüge",
      "Aktive Verbformen und persönliche Ansprache",
      "Abstrakte Nominalphrasen ohne klare Handlungsträger"
    ],
    "correctAnswer": "Aktive Verbformen und persönliche Ansprache",
    "explanation": "Verbalstil is characterized by active verb forms and personal pronouns, making the text more direct, dynamic, and reader-friendly.",
    "id": "c1_01_q086"
  },
  {
    "difficulty": "medium",
    "type": "multiple_choice",
    "questionText": "Wie lautet die Nominalstil-Variante von: 'Wir haben die Daten ausgewertet.'?",
    "options": [
      "Die Daten wurden von uns ausgewertet.",
      "Die Auswertung der Daten wurde durchgeführt.",
      "Wir führten eine Datenauswertung durch.",
      "Es erfolgte eine Auswertung durch uns der Daten."
    ],
    "correctAnswer": "Die Auswertung der Daten wurde durchgeführt.",
    "explanation": "In Nominalstil, the verb 'auswerten' is nominalized to 'die Auswertung', personal pronouns are removed, and passive voice is often used to create a formal, impersonal tone.",
    "id": "c1_01_q087"
  }
]

data['questions'].extend(questions_to_add)
data['totalQuestions'] = len(data['questions'])

with open('app/src/main/assets/c1_01.json', 'w', encoding='utf-8') as out:
    json.dump(data, out, ensure_ascii=False, indent=2)

print(f"Added {len(questions_to_add)} questions. New total: {data['totalQuestions']}")
print(f"Last ID: {data['questions'][-1]['id']}")
