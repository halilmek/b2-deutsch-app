import json

# Load existing c2_01.json
with open('app/src/main/assets/c2_01.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

existing_count = len(data['questions'])
print(f"Existing questions: {existing_count}")

# New questions to add (q041-q060)
new_questions = [
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Was ist das Hauptmerkmal des Nominalstils im akademischen Diskurs?",
        "options": [
            "Die Verwendung vieler aktiver Verben und kurzer Saetze",
            "Die Verdichtung von Handlungen in Substantive mit Praepositionen und Genitivattributen",
            "Der ausschliessliche Gebrauch von Passivkonstruktionen ohne Substantivierungen",
            "Die Praeferenz fuer umgangssprachliche Ausdruecke und direkte Anrede"
        ],
        "correctAnswer": "Die Verdichtung von Handlungen in Substantive mit Praepositionen und Genitivattributen",
        "explanation": "Nominalstil compresses actions into nouns (often with -ung, -heit, -keit suffixes) linked by prepositions and genitive attributes, creating dense, formal phrasing typical of academic and bureaucratic German.",
        "id": "c2_01_q041"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welche Endung ist am produktivsten fuer die Bildung von Nominalisierungen aus Verben im Nominalstil?",
        "options": [
            "-ling",
            "-ung",
            "-schaft",
            "-nis"
        ],
        "correctAnswer": "-ung",
        "explanation": "The suffix -ung is the most productive pattern for creating feminine action nouns from verbs in formal German (e.g., durchfuehren -> die Durchfuehrung, untersuchen -> die Untersuchung).",
        "id": "c2_01_q042"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Wie lautet die korrekte Nominalisierung des Satzes: 'Weil sich die Lage verbessert hat, ...'?",
        "options": [
            "Wegen der Verbesserung der Lage, ...",
            "Wegen die Verbesserung von der Lage, ...",
            "Durch das Verbessern der Lage, ...",
            "Nachdem die Lage verbessert wurde, ..."
        ],
        "correctAnswer": "Wegen der Verbesserung der Lage, ...",
        "explanation": "In Nominalstil, the causal clause 'weil sich die Lage verbessert hat' transforms into a prepositional phrase with a nominalized verb: 'wegen der Verbesserung der Lage'. The verb 'verbessern' becomes 'Verbesserung' (capitalized noun) and the case shifts to genitive.",
        "id": "c2_01_q043"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welcher Ausdruck ist ein typisches Funktionsverbgefuege im Nominalstil?",
        "options": [
            "schnell entscheiden",
            "eine Entscheidung treffen",
            "die Entscheidung ist schnell",
            "entscheidend sein"
        ],
        "correctAnswer": "eine Entscheidung treffen",
        "explanation": "Funktionsverbgefuege combine a 'light' verb (like treffen, geben, leisten) with a nominalized action where the noun carries the core meaning. 'Eine Entscheidung treffen' is the formal equivalent of the simple verb 'entscheiden'.",
        "id": "c2_01_q044"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Was ist grammatikalisch korrekt: 'die Senkung ____ Emissionen'?",
        "options": [
            "die",
            "der",
            "den",
            "des"
        ],
        "correctAnswer": "der",
        "explanation": "When a verb is nominalized, its original accusative object becomes a genitive attribute. 'Man senkt die Emissionen' (accusative) -> 'die Senkung der Emissionen' (genitive).",
        "id": "c2_01_q045"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welche Transformation von Verbalstil zu Nominalstil ist korrekt?",
        "options": [
            "Nachdem er das Studium beendet hatte -> Nach dem Beenden das Studium",
            "Nachdem er das Studium beendet hatte -> Nach Beendigung des Studiums",
            "Nachdem er das Studium beendet hatte -> Wegen dem Beendigung vom Studium",
            "Nachdem er das Studium beendet hatte -> Fuer die Beendigung von das Studium"
        ],
        "correctAnswer": "Nachdem er das Studium beendet hatte -> Nach Beendigung des Studiums",
        "explanation": "The subordinate clause 'nachdem er ... beendet hatte' collapses into 'nach + nominalized verb (Beendigung) + genitive attribute (des Studiums)'. This is the mechanical core of Nominalstil.",
        "id": "c2_01_q046"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welcher Satz verwendet den Nominalstil angemessen fuer einen wissenschaftlichen Abstract?",
        "options": [
            "Wir haben die Daten analysiert und festgestellt, dass...",
            "Die Analyse der Daten ergab, dass...",
            "Ich denke, die Daten zeigen klar, dass...",
            "Man kann sehen, dass die Daten beweisen, dass..."
        ],
        "correctAnswer": "Die Analyse der Daten ergab, dass...",
        "explanation": "Academic German prefers nominalized subjects ('Die Analyse der Daten') over personal pronouns and active verbs for objectivity and formality. This balances density with readability.",
        "id": "c2_01_q047"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Was ist ein häufiger Fehler bei der Anwendung des Nominalstils?",
        "options": [
            "Die Verwendung von zu vielen Adjektiven",
            "Die Anhaeufung von mehr als drei Nominalisierungen pro Satz, was die Lesbarkeit beeintraechtigt",
            "Der Gebrauch von direkten Zitaten",
            "Die Verwendung von Aktiv statt Passiv"
        ],
        "correctAnswer": "Die Anhaeufung von mehr als drei Nominalisierungen pro Satz, was die Lesbarkeit beeintraechtigt",
        "explanation": "While Nominalstil is appropriate for formal contexts, over-nominalization (3+ abstract nouns in a row) creates unreadable 'Beamtendeutsch'. C2 competence requires calibration between density and clarity.",
        "id": "c2_01_q048"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Wie lautet die korrekte Nominalisierung von 'man beruecksichtigt alle Variablen'?",
        "options": [
            "Die Beruecksichtigung von alle Variablen",
            "Die Beruecksichtigung aller Variablen",
            "Das Beruecksichtigen alle Variablen",
            "Die Beruecksichtigung die Variablen"
        ],
        "correctAnswer": "Die Beruecksichtigung aller Variablen",
        "explanation": "The verb 'beruecksichtigen' nominalizes to 'die Beruecksichtigung'. The accusative object 'alle Variablen' becomes a genitive attribute: 'aller Variablen' (plural genitive).",
        "id": "c2_01_q049"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welche Praeposition ersetzt im Nominalstil typischerweise die Konjunktion 'nachdem'?",
        "options": [
            "waehrend",
            "nach",
            "seit",
            "bis"
        ],
        "correctAnswer": "nach",
        "explanation": "Temporal clauses with 'nachdem' transform into prepositional phrases with 'nach' + nominalized verb + genitive: 'Nachdem er beendet hatte' -> 'Nach Beendigung'.",
        "id": "c2_01_q050"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Was bedeutet der Begriff 'Funktionsverbgefuege' im Kontext des Nominalstils?",
        "options": [
            "Eine Kombination aus Adjektiv und Substantiv zur Stilverbesserung",
            "Eine feste Verbindung aus einem semantisch leichten Verb und einem nominalisierten Handlungsbegriff",
            "Die Verwendung von Modalverben zur Abschwaechung von Aussagen",
            "Ein Satzgefege mit mehreren Nebensaetzen"
        ],
        "correctAnswer": "Eine feste Verbindung aus einem semantisch leichten Verb und einem nominalisierten Handlungsbegriff",
        "explanation": "Funktionsverbgefuege like 'eine Entscheidung treffen' or 'Kritik ueben' use a light verb (treffen, ueben) with a noun carrying the core meaning. They are hallmark structures of formal German.",
        "id": "c2_01_q051"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welcher Satz enthaelt eine inkorrekte Nominalisierung?",
        "options": [
            "Wegen der Verbesserung der Lage wurden Massnahmen ergriffen.",
            "Nach dem Ueberpruefen der Unterlagen erfolgte die Bewilligung.",
            "Die Durchfuehrung der Untersuchung war erfolgreich.",
            "Zur Beantragung des Antrags ist die Vorlage noetig."
        ],
        "correctAnswer": "Nach dem Ueberpruefen der Unterlagen erfolgte die Bewilligung.",
        "explanation": "The infinitive nominalization 'das Ueberpruefen' is grammatically possible but stylistically inferior to the -ung form 'die Ueberpruefung' in formal academic writing. C2 style prefers 'Nach Ueberpruefung der Unterlagen'.",
        "id": "c2_01_q052"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Wie transformiert man 'Die Forscher analysierten die Daten gruendlich' in den Nominalstil?",
        "options": [
            "Die Daten wurden von den Forschern gruendlich analysiert.",
            "Die gruendliche Analyse der Daten erfolgte durch die Forscher.",
            "Die Forscher fuehrten eine gruendliche Analyse der Daten durch.",
            "Es wurde eine gruendliche Datenanalyse von den Forschern gemacht."
        ],
        "correctAnswer": "Die gruendliche Analyse der Daten erfolgte durch die Forscher.",
        "explanation": "The active verb 'analysierten' becomes the nominal subject 'die Analyse', modified by the adjective 'gruendliche'. The agent ('durch die Forscher') is retained in a prepositional phrase for clarity.",
        "id": "c2_01_q053"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welche Aussage zum Verhaeltnis von Nominalstil und Verbalstil ist korrekt?",
        "options": [
            "Nominalstil ist immer besser als Verbalstil, da er professioneller wirkt.",
            "Verbalstil sollte in wissenschaftlichen Texten vollstaendig vermieden werden.",
            "Ein gelungener akademischer Text balanciert beide Stile je nach Funktion der Passage.",
            "Nominalstil ist nur fuer juristische Texte geeignet, nicht fuer Naturwissenschaften."
        ],
        "correctAnswer": "Ein gelungener akademischer Text balanciert beide Stile je nach Funktion der Passage.",
        "explanation": "C2 writing requires stylistic calibration: use Nominalstil for definitions, methods, and dense information; use Verbalstil for narrative flow, emphasis, and clarity. Overuse of either reduces effectiveness.",
        "id": "c2_01_q054"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Was ist die korrekte Form: 'die Implementierung ____ Software'?",
        "options": [
            "die",
            "der",
            "den",
            "dem"
        ],
        "correctAnswer": "der",
        "explanation": "The nominalized verb 'Implementierung' requires a genitive attribute for its object. 'Die Software' (accusative/feminine) becomes 'der Software' in genitive case.",
        "id": "c2_01_q055"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welcher Ausdruck ist KEIN typisches Funktionsverbgefuege?",
        "options": [
            "eine Antwort geben",
            "Hilfe leisten",
            "schnell reagieren",
            "Kritik ueben"
        ],
        "correctAnswer": "schnell reagieren",
        "explanation": "'Schnell reagieren' uses a full lexical verb with an adverb, not a light verb + action noun. The other options are classic Funktionsverbgefuege where the noun carries the semantic weight.",
        "id": "c2_01_q056"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Wie lautet die stilistisch angemessene Nominalisierung fuer einen Methodenabschnitt: 'Wir ueberprueften die Hypothese mit statistischen Tests'?",
        "options": [
            "Die Hypothese wurde von uns mit statistischen Tests ueberprueft.",
            "Die Ueberpruefung der Hypothese erfolgte mittels statistischer Tests.",
            "Wir fuehrten eine Ueberpruefung von der Hypothese durch mit statistischen Tests.",
            "Das Ueberpruefen der Hypothese war mit statistischen Tests."
        ],
        "correctAnswer": "Die Ueberpruefung der Hypothese erfolgte mittels statistischer Tests.",
        "explanation": "This version uses the nominalized subject 'Die Ueberpruefung', the formal verb 'erfolgte', and the genitive/technical preposition 'mittels statistischer Tests' — all hallmarks of academic Nominalstil.",
        "id": "c2_01_q057"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welche Substantivierung ist lexikalisch korrekt?",
        "options": [
            "die Beweisung",
            "der Beweis",
            "das Beweisen",
            "die Beweishung"
        ],
        "correctAnswer": "der Beweis",
        "explanation": "Some verbs have irregular or suppletive nominalizations: 'beweisen' -> 'der Beweis', not '*die Beweisung'. C2 competence includes knowledge of these lexicalized forms.",
        "id": "c2_01_q058"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Was ist der Hauptunterschied zwischen 'von + Dativ' und Genitiv bei Nominalisierungen?",
        "options": [
            "Es gibt keinen Unterschied; beide sind immer austauschbar.",
            "Genitiv ist im formalen Nominalstil praeferiert; 'von + Dativ' wirkt umgangssprachlicher.",
            "'Von + Dativ' ist ausschliesslich fuer Personen reserviert.",
            "Genitiv darf nur bei maskulinen Nomen verwendet werden."
        ],
        "correctAnswer": "Genitiv ist im formalen Nominalstil praeferiert; 'von + Dativ' wirkt umgangssprachlicher.",
        "explanation": "In high-register Nominalstil, genitive attributes ('die Analyse der Daten') are preferred over 'von + dative' ('die Analyse von den Daten'), which is perceived as less formal or colloquial.",
        "id": "c2_01_q059"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welcher Satz demonstriert uebermaessigen Nominalstil ('Beamtendeutsch')?",
        "options": [
            "Die Studie untersucht den Einfluss von Temperatur auf Reaktionsgeschwindigkeit.",
            "Die Inangriffnahme der Umsetzung der Reform erfolgt nach Genehmigung durch das Ministerium.",
            "Nach Abschluss der Datenerhebung wurden die Ergebnisse analysiert.",
            "Zur Validierung der Methode wurden Kontrolltests durchgefuehrt."
        ],
        "correctAnswer": "Die Inangriffnahme der Umsetzung der Reform erfolgt nach Genehmigung durch das Ministerium.",
        "explanation": "This sentence stacks three abstract nominalizations ('Inangriffnahme', 'Umsetzung', 'Genehmigung') with genitive chains, creating heavy, hard-to-parse bureaucratese. C2 writers learn to recognize and avoid such over-nominalization.",
        "id": "c2_01_q060"
    }
]

# Add new questions
data['questions'].extend(new_questions)
data['totalQuestions'] = len(data['questions'])

# Save
with open('app/src/main/assets/c2_01.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(new_questions)} questions (q041-q060)")
print(f"Total questions now: {data['totalQuestions']}")
easy = sum(1 for q in data['questions'] if q['difficulty'] == 'easy')
medium = sum(1 for q in data['questions'] if q['difficulty'] == 'medium')
hard = sum(1 for q in data['questions'] if q['difficulty'] == 'hard')
print(f"Difficulty breakdown: easy={easy}, medium={medium}, hard={hard}")