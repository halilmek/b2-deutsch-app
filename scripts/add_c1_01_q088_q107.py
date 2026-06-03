import json

with open('app/src/main/assets/c1_01.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

questions_to_add = [
  {
    "questionText": "Was kennzeichnet den Nominalstil im Deutschen?",
    "options": [
      "Er verwendet überwiegend Verben und persönliche Pronomen.",
      "Er bevorzugt Substantive, Nominalphrasen und passive Konstruktionen.",
      "Er ist typisch für Alltagsgespräche und erzählende Texte.",
      "Er vermeidet abstrakte Begriffe und Fachterminologie."
    ],
    "correctAnswer": "Er bevorzugt Substantive, Nominalphrasen und passive Konstruktionen.",
    "explanation": "Nominalstil is characterized by a preference for nouns over verbs, complex noun phrases, passive voice, and abstract terminology, making it typical for formal, administrative, and academic texts.",
    "difficulty": "easy",
    "type": "multiple_choice"
  },
  {
    "questionText": "Welcher Stil wird häufig in der deutschen Verwaltungs- und Amtssprache verwendet?",
    "options": [
      "Verbalstil",
      "Umgangssprachlicher Stil",
      "Nominalstil",
      "Erzählender Stil"
    ],
    "correctAnswer": "Nominalstil",
    "explanation": "Nominalstil is frequently found in German administrative and official language because it conveys precision, formality, and objectivity, as seen in phrases like 'Aufgrund der Nichteinreichung der Unterlagen erfolgt die Ablehnung des Antrags'.",
    "difficulty": "easy",
    "type": "multiple_choice"
  },
  {
    "questionText": "Was ist ein Hauptvorteil des Verbalstils?",
    "options": [
      "Er wirkt besonders formell und distanziert.",
      "Er ermöglicht eine höhere Informationsdichte pro Satz.",
      "Er verbessert die Verständlichkeit und den Lesefluss.",
      "Er vermeidet persönliche Ansprache vollständig."
    ],
    "correctAnswer": "Er verbessert die Verständlichkeit und den Lesefluss.",
    "explanation": "Verbalstil uses verbs to describe actions directly, making sentences more dynamic, easier to understand, and more pleasant to read, which is ideal for everyday communication and narrative texts.",
    "difficulty": "easy",
    "type": "multiple_choice"
  },
  {
    "questionText": "Welche Transformation ist typisch für die Umwandlung von Verbalstil in Nominalstil?",
    "options": [
      "Verben werden durch Adjektive ersetzt.",
      "Verben werden in Substantive umgewandelt (z. B. 'analysieren' → 'die Analyse').",
      "Substantive werden in Verben umgewandelt.",
      "Präpositionen werden durch Konjunktionen ersetzt."
    ],
    "correctAnswer": "Verben werden in Substantive umgewandelt (z. B. 'analysieren' → 'die Analyse').",
    "explanation": "A core transformation rule for creating Nominalstil is nominalizing verbs—turning action words into nouns (e.g., 'analysieren' becomes 'die Analyse'), which increases formality and density.",
    "difficulty": "easy",
    "type": "multiple_choice"
  },
  {
    "questionText": "Welcher Stil vermeidet persönliche Pronomen wie 'wir', 'ich' oder 'man'?",
    "options": [
      "Verbalstil",
      "Nominalstil",
      "Umgangssprachlicher Stil",
      "Poetischer Stil"
    ],
    "correctAnswer": "Nominalstil",
    "explanation": "Nominalstil avoids personal pronouns to create distance and formality, preferring impersonal constructions like 'es erfolgt...' or 'die Durchführung...'.",
    "difficulty": "easy",
    "type": "multiple_choice"
  },
  {
    "questionText": "Was ist ein typisches Merkmal des Verbalstils?",
    "options": [
      "Häufige Verwendung von Partizipialattributen",
      "Komplexe Präpositionalgefüge",
      "Aktive Verbformen und persönliche Ansprache",
      "Abstrakte Nominalphrasen ohne klare Handlungsträger"
    ],
    "correctAnswer": "Aktive Verbformen und persönliche Ansprache",
    "explanation": "Verbalstil is characterized by active verb forms and personal pronouns, making othe text more direct, dynamic, and reader-friendly.",
    "difficulty": "easy",
    "type": "multiple_choice"
  },
  {
    "questionText": "Wie lautet die Nominalstil-Variante von: 'Wir haben die Daten ausgewertet.'?",
    "options": [
      "Die Daten wurden von uns ausgewertet.",
      "Die Auswertung der Daten wurde durchgeführt.",
      "Wir führten eine Datenauswertung durch.",
      "Es erfolgte eine Auswertung durch uns der Daten."
    ],
    "correctAnswer": "Die Auswertung der Daten wurde durchgeführt.",
    "explanation": "In Nominalstil, the verb 'auswerten' is nominalized to 'die Auswertung', personal pronouns are removed, and passive voice is often used to create a formal, impersonal tone.",
    "difficulty": "medium",
    "type": "multiple_choice"
  },
  {
    "questionText": "Welche Präposition wird häufig im Nominalstil verwendet, um einen kausalen Nebensatz mit 'weil' zu ersetzen?",
    "options": [
      "durch",
      "wegen",
      "für",
      "gegen"
    ],
    "correctAnswer": "wegen",
    "explanation": "In Nominalstil, causal clauses introduced by 'weil' are often replaced by prepositional phrases with 'wegen' + genitive noun (e.g., 'weil die Unterlagen fehlen' → 'wegen des Fehlens der Unterlagen').",
    "difficulty": "medium",
    "type": "multiple_choice"
  },
  {
    "questionText": "Welcher Satz steht im Verbalstil?",
    "options": [
      "Die Durchführung der Maßnahme erfolgte umgehend.",
      "Aufgrund der Nichteinhaltung der Vorschriften wurde sanktioniert.",
      "Das Team führte die Maßnahme umgehend durch.",
      "Die Einhaltung der Vorschriften ist von großer Bedeutung."
    ],
    "correctAnswer": "Das Team führte die Maßnahme umgehend durch.",
    "explanation": "This sentence uses an active verb ('führte ... durch'), a clear subject ('das Team'), and no complex nominalizations—hallmarks of Verbalstil.",
    "difficulty": "medium",
    "type": "multiple_choice"
  },
  {
    "questionText": "Wie transformiert man den konditionalen Nebensatz 'Wenn Sie den Antrag einreichen, ...' in den Nominalstil?",
    "options": [
      "Durch die Einreichung des Antrags, ...",
      "Bei Einreichung des Antrags, ...",
      "Wegen der Einreichung des Antrags, ...",
      "Trotz Einreichung des Antrags, ..."
    ],
    "correctAnswer": "Bei Einreichung des Antrags, ...",
    "explanation": "Conditional clauses with 'wenn' are often transformed in Nominalstil using the preposition 'bei' + nominalized verb (e.g., 'bei Einreichung' instead of 'wenn Sie einreichen').",
    "difficulty": "medium",
    "type": "multiple_choice"
  },
  {
    "questionText": "Welche Aussage über den Nominalstil ist NICHT korrekt?",
    "options": [
      "Er erhöht die Informationsdichte eines Textes.",
      "Er ist besonders geeignet für wissenschaftliche Texte.",
      "Er verbessert grundsätzlich die Lesbarkeit für alle Zielgruppen.",
      "Er kann Texte sperrig und schwer verständlich machen."
    ],
    "correctAnswer": "Er verbessert grundsätzlich die Lesbarkeit für alle Zielgruppen.",
    "explanation": "This statement is incorrect: while Nominalstil is precise and formal, it often reduces readability for general audiences due to complex noun phrases and abstract structures.",
    "difficulty": "medium",
    "type": "multiple_choice"
  },
  {
    "questionText": "Wie lautet die Verbalstil-Variante von: 'Die Überführung des Gefangenen erfolgte durch die Bundespolizei.'?",
    "options": [
      "Die Bundespolizei hat die Überführung des Gefangenen durchgeführt.",
      "Der Gefangene wurde von der Bundespolizei überführt.",
      "Es erfolgte eine Überführung durch die Bundespolizei des Gefangenen.",
      "Die Bundespolizei führte den Gefangenen über."
    ],
    "correctAnswer": "Der Gefangene wurde von der Bundespolizei überführt.",
    "explanation": "In Verbalstil, the nominalized noun 'Überführung' is converted back to the verb 'überführen', and the sentence structure becomes more direct and action-oriented, often using active or simple passive voice.",
    "difficulty": "medium",
    "type": "multiple_choice"
  },
  {
    "questionText": "Welche Konstruktion ist im Nominalstil typisch für die Umformung eines konzessiven Nebensatzes mit 'obwohl'?",
    "options": [
      "trotz + Genitiv",
      "wegen + Genitiv",
      "durch + Akkusativ",
      "für + Akkusativ"
    ],
    "correctAnswer": "trotz + Genitiv",
    "explanation": "Concessive clauses with 'obwohl' are commonly transformed in Nominalstil using 'trotz' + genitive noun phrase (e.g., 'obwohl es regnete' → 'trotz des Regens').",
    "difficulty": "medium",
    "type": "multiple_choice"
  },
  {
    "questionText": "Welcher Satz kombiniert Nominalstil und Verbalstil am ausgewogensten für einen formellen Bericht?",
    "options": [
      "Wir haben die Analyse durchgeführt, und die Ergebnisse sind wichtig.",
      "Die Durchführung der Analyse erfolgte, und wir präsentieren die Ergebnisse.",
      "Die Analyse wurde durchgeführt; die Ergebnisse zeigen, dass eine Optimierung notwendig ist.",
      "Es erfolgte eine Analyse, deren Ergebnisse eine Optimierung notwendig machen."
    ],
    "correctAnswer": "Die Analyse wurde durchgeführt; die Ergebnisse zeigen, dass eine Optimierung notwendig ist.",
    "explanation": "This sentence balances formality (passive nominal construction 'wurde durchgeführt') with clarity (active verbal clause 'die Ergebnisse zeigen'), making it suitable for formal reports where both precision and readability matter.",
    "difficulty": "medium",
    "type": "multiple_choice"
  },
  {
    "questionText": "Welche Nominalisierung ist grammatikalisch und stilistisch am angemessensten für C1-Niveau?",
    "options": [
      "Das schnelle Laufen des Hundes war beeindruckend.",
      "Die Schnelligkeit des Laufens vom Hund war beeindruckend.",
      "Das beeindruckende Laufen schnell vom Hund.",
      "Der Hund lief schnell und das war beeindruckend."
    ],
    "correctAnswer": "Das schnelle Laufen des Hundes war beeindruckend.",
    "explanation": "This option correctly nominalizes the verb 'laufen' while maintaining proper adjective-noun agreement ('schnelle Laufen') and genitive case ('des Hundes'), demonstrating C1-level control of nominal style.",
    "difficulty": "hard",
    "type": "multiple_choice"
  },
  {
    "questionText": "Wie transformiert man den Finalsatz 'Damit die Qualität gesichert wird, ...' in den Nominalstil?",
    "options": [
      "Zur Sicherung der Qualität, ...",
      "Wegen der Sicherung der Qualität, ...",
      "Durch die Qualität, die gesichert wird, ...",
      "Für das Sichern der Qualität, ..."
    ],
    "correctAnswer": "Zur Sicherung der Qualität, ...",
    "explanation": "Final clauses with 'damit' are typically transformed in Nominalstil using 'zur' + nominalized verb + genitive object ('zur Sicherung der Qualität'), a sophisticated C1-level construction.",
    "difficulty": "hard",
    "type": "multiple_choice"
  },
  {
    "questionText": "Welcher Satz enthält eine fehlerhafte Nominalisierung?",
    "options": [
      "Die Durchführung des Projekts erfolgte planmäßig.",
      "Das Durchführen des Projekts erfolgte planmäßig.",
      "Die Projektdurchführung erfolgte planmäßig.",
      "Die Durchführung vom Projekt erfolgte planmäßig."
    ],
    "correctAnswer": "Die Durchführung vom Projekt erfolgte planmäßig.",
    "explanation": "The phrase 'vom Projekt' uses the wrong case: after 'Durchführung', the genitive 'des Projekts' is required in formal Nominalstil. 'Vom' (von + dem) is dative and stylistically inappropriate here.",
    "difficulty": "hard",
    "type": "multiple_choice"
  },
  {
    "questionText": "Welche Aussage beschreibt den stilistischen Effekt von Partizipialattributen im Nominalstil korrekt?",
    "options": [
      "Sie machen Sätze kürzer und umgangssprachlicher.",
      "Sie erhöhen die Informationsdichte, können aber die Lesbarkeit erschweren.",
      "Sie ersetzen ausschließlich Präpositionalgefüge.",
      "Sie sind im Verbalstil häufiger als im Nominalstil."
    ],
    "correctAnswer": "Sie erhöhen die Informationsdichte, können aber die Lesbarkeit erschweren.",
    "explanation": "Participial attributes (e.g., 'die von Experten entwickelte Methode') pack complex information into noun phrases, increasing density—a hallmark of Nominalstil—but may reduce readability if overused.",
    "difficulty": "hard",
    "type": "multiple_choice"
  },
  {
    "questionText": "Wie lautet die stilistisch angemessene Nominalstil-Variante von: 'Man muss die Vorschriften beachten, sonst drohen Sanktionen.'?",
    "options": [
      "Die Beachtung der Vorschriften ist erforderlich, andernfalls drohen Sanktionen.",
      "Man beachte die Vorschriften, weil sonst Sanktionen drohen.",
      "Vorschriften beachten, sonst Sanktionen.",
      "Es ist wichtig, dass man Vorschriften beachtet, weil Sanktionen drohen."
    ],
    "correctAnswer": "Die Beachtung der Vorschriften ist erforderlich, andernfalls drohen Sanktionen.",
    "explanation": "This option correctly nominalizes 'beachten' → 'die Beachtung', removes the indefinite pronoun 'man', and maintains formal tone with 'ist erforderlich'—all key features of C1-level Nominalstil.",
    "difficulty": "hard",
    "type": "multiple_choice"
  },
  {
    "questionText": "Welche Strategie ist am effektivsten, um einen Text für ein breites Publikum verständlicher zu gestalten?",
    "options": [
      "Konsequente Anwendung des Nominalstils für maximale Präzision.",
      "Ausschließliche Verwendung des Verbalstils mit aktiven Verben und klaren Subjekten.",
      "Gezielte Mischung: Nominalstil für Fachbegriffe, Verbalstil für Erklärungen und Übergänge.",
      "Vermeidung aller Nominalisierungen und Passivkonstruktionen."
    ],
    "correctAnswer": "Gezielte Mischung: Nominalstil für Fachbegriffe, Verbalstil für Erklärungen und Übergänge.",
    "explanation": "At C1 level, stylistic competence includes knowing when to use each style: Nominalstil for precision in technical terms, Verbalstil for clarity and flow in explanations—this strategic mixing demonstrates advanced language control.",
    "difficulty": "hard",
    "type": "multiple_choice"
  }
]

# Assign IDs
next_id = 88
for q in questions_to_add:
    q['id'] = f'c1_01_q{str(next_id).zfill(3)}'
    next_id += 1

data['questions'].extend(questions_to_add)
data['totalQuestions'] = len(data['questions'])

with open('app/src/main/assets/c1_01.json', 'w', encoding='utf-8') as out:
    json.dump(data, out, ensure_ascii=False, indent=2)

print(f"Added {len(questions_to_add)} questions. New total: {data['totalQuestions']}")
print(f"Last ID: {data['questions'][-1]['id']}")
