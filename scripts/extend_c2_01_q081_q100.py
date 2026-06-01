import json

with open('app/src/main/assets/c2_01.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

existing_count = len(data['questions'])
print(f"Existing questions: {existing_count}")

new_questions = [
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Der Nominalstil ist vor allem gekennzeichnet durch die Hauefung von ____.",
        "options": [
            "Nomen und Adjektiven",
            "Verben und Konjunktionen",
            "Pronomen und Partikeln",
            "Adverbien und Interjektionen"
        ],
        "correctAnswer": "Nomen und Adjektiven",
        "explanation": "Nominal style uses many nouns and adjectives, while verbal style relies on verbs.",
        "id": "c2_01_q081"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welches Beispiel steht fuer Nominalstil?",
        "options": [
            "Weil er sich beeilte, kam er punktlich.",
            "Durch seine Eile kam er punktlich.",
            "Er beeilte sich und kam punktlich.",
            "Er kam punktlich, denn er beeilte sich."
        ],
        "correctAnswer": "Durch seine Eile kam er punktlich.",
        "explanation": "The phrase uses a noun ('Eile') instead of a verb ('beeilte sich').",
        "id": "c2_01_q082"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "In welchem Textdomaene ist der Nominalstil im Deutschen am haeufigsten anzutreffen?",
        "options": [
            "Alltagsgespraech",
            "Privater Brief",
            "Akademischer Diskurs",
            "Maerchen"
        ],
        "correctAnswer": "Akademischer Diskurs",
        "explanation": "Nominal style is typical in academic writing for precision and density.",
        "id": "c2_01_q083"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Was ist ein typisches Merkmal des Nominalstils?",
        "options": [
            "Viele Nebensaetze mit 'weil'",
            "Haeufige Verwendung von Modalpartikeln",
            "Lange Nominalphrasen mit Genitivattributen",
            "Viele direkte Reden"
        ],
        "correctAnswer": "Lange Nominalphrasen mit Genitivattributen",
        "explanation": "Long noun phrases with genitive attributes are a hallmark of nominal style.",
        "id": "c2_01_q084"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Der Satz 'Die Durchfuehrung der Studie erwies sich als problematisch' ist ein Beispiel fuer ____.",
        "options": [
            "Verbalstil",
            "Nominalstil",
            "Praeteritalstil",
            "Konjunktivstil"
        ],
        "correctAnswer": "Nominalstil",
        "explanation": "The noun 'Durchfuehrung' replaces a verb phrase like 'Die Studie durchzufuehren'.",
        "id": "c2_01_q085"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welche Umformung wandelt den Verbalstil in Nominalstil um?",
        "options": [
            "weil sie forscht -> wegen ihrer Forschung",
            "sie forscht -> sie ist forschend",
            "sie forscht -> das Forschen von ihr",
            "sie forscht -> forschend"
        ],
        "correctAnswer": "weil sie forscht -> wegen ihrer Forschung",
        "explanation": "The causal clause becomes a prepositional phrase with a noun ('Forschung').",
        "id": "c2_01_q086"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welcher Satz ist im Nominalstil verfasst?",
        "options": [
            "Nachdem die Daten erhoben wurden, begann die Auswertung.",
            "Nach der Datenerhebung begann die Auswertung.",
            "Man erhob die Daten und dann wertete man aus.",
            "Als die Daten erhoben waren, wertete man sie aus."
        ],
        "correctAnswer": "Nach der Datenerhebung begann die Auswertung.",
        "explanation": "'Datenerhebung' and 'Auswertung' are nouns, avoiding finite verbs.",
        "id": "c2_01_q087"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Was versteht man unter 'Nominalisierung' im Kontext des Nominalstils?",
        "options": [
            "Die Umwandlung eines Nomens in ein Verb",
            "Die Umwandlung eines Verbs oder Adjektivs in ein Nomen",
            "Die Wiederholung desselben Nomens",
            "Die Ersetzung eines Nomens durch ein Pronomen"
        ],
        "correctAnswer": "Die Umwandlung eines Verbs oder Adjektivs in ein Nomen",
        "explanation": "Nominalization turns verbs or adjectives into nouns (e.g., 'laufen' -> 'das Laufen').",
        "id": "c2_01_q088"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welche Wirkung hat der Nominalstil im akademischen Diskurs?",
        "options": [
            "Er wirkt umgangssprachlich und emotional.",
            "Er wirkt objektivierend und informationsverdichtend.",
            "Er wirkt dialogisch und interaktiv.",
            "Er wirkt ironisch und distanzierend."
        ],
        "correctAnswer": "Er wirkt objektivierend und informationsverdichtend.",
        "explanation": "Nominal style creates objectivity and condenses information, valued in academic texts.",
        "id": "c2_01_q089"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Kritik am uebermaessigen Nominalstil lautet oft, dass er ____.",
        "options": [
            "zu subjektiv und emotional sei",
            "zu ungenau und vage sei",
            "schwer verstaendlich und abstrakt wirke",
            "zu viele Verben enthalte"
        ],
        "correctAnswer": "schwer verstaendlich und abstrakt wirke",
        "explanation": "Excessive nominal style can make texts abstract and hard to follow.",
        "id": "c2_01_q090"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welcher Fachbereich verwendet traditionell am staerksten den Nominalstil?",
        "options": [
            "Literaturwissenschaft",
            "Rechtswissenschaft",
            "Sportwissenschaft",
            "Musikpaedagogik"
        ],
        "correctAnswer": "Rechtswissenschaft",
        "explanation": "Legal German is famous for extreme nominal style (e.g., 'In Erfuellung der ...').",
        "id": "c2_01_q091"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Der Satz 'Die Tatsache, dass er kam, ueberraschte niemanden' enthaelt eine ____.",
        "options": [
            "Nominalisierung ohne Funktionsverb",
            "Nominalisierung mit 'dass'-Satz",
            "verdeckte Nominalisierung",
            "echte Nominalphrase"
        ],
        "correctAnswer": "verdeckte Nominalisierung",
        "explanation": "'Die Tatsache, dass ...' is a nominalization hiding a clause, often criticized as inflated.",
        "id": "c2_01_q092"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welches Signalwort leitet oft eine Nominalphrase im Nominalstil ein?",
        "options": [
            "weil",
            "obwohl",
            "aufgrund",
            "indem"
        ],
        "correctAnswer": "aufgrund",
        "explanation": "'Aufgrund' is a preposition that requires a noun phrase, promoting nominal style.",
        "id": "c2_01_q093"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welcher Satz ist im reinen Nominalstil (ohne finites Verb im Hauptgeschehen) geschrieben?",
        "options": [
            "Der Autor analysiert die Daten gruendlich.",
            "Der Autor ist ein gruendlicher Analytiker der Daten.",
            "Der Autor, der die Daten gruendlich analysiert, ist erfahren.",
            "Gruendliche Datenanalyse durch den Autor."
        ],
        "correctAnswer": "Gruendliche Datenanalyse durch den Autor.",
        "explanation": "This phrase has no finite verb; all information is packed into nouns.",
        "id": "c2_01_q094"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Was ist ein Funktionsverbgefuege (FVG) im Nominalstil?",
        "options": [
            "Ein Verb, das zwei Nominale verbindet",
            "Eine Verbindung wie 'zur Anwendung bringen' statt 'anwenden'",
            "Ein Verb, das nur im Nominalstil vorkommt",
            "Eine Konjunktion, die Nomen verbindet"
        ],
        "correctAnswer": "Eine Verbindung wie 'zur Anwendung bringen' statt 'anwenden'",
        "explanation": "FVG (e.g., 'in Betracht ziehen') is typical for nominal style, replacing simple verbs.",
        "id": "c2_01_q095"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welcher der folgenden Saetze ist ein Beispiel fuer uebertriebenen Nominalstil (sogenannter 'Nominalstil-Exzess')?",
        "options": [
            "Die Sonne schien hell.",
            "Das Zur-Verfuegung-Stellen von Loesungsansaetzen obliegt der Zustaendigkeit des Teams.",
            "Wir trafen uns, um zu diskutieren.",
            "Der Vortrag war kurz und klar."
        ],
        "correctAnswer": "Das Zur-Verfuegung-Stellen von Loesungsansaetzen obliegt der Zustaendigkeit des Teams.",
        "explanation": "This string of nouns and nested phrases is an example of excessive, heavy nominal style.",
        "id": "c2_01_q096"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Im akademischen Diskurs dient der Nominalstil oft der ____.",
        "options": [
            "Emotionalisierung",
            "Verschleierung von Verantwortlichkeit",
            "Steigerung der Lesbarkeit fuer Laien",
            "Verkuerzung der Satzlaengen"
        ],
        "correctAnswer": "Verschleierung von Verantwortlichkeit",
        "explanation": "Nominal style can hide agency (e.g., 'Die Analyse ergab' instead of 'Wir analysierten').",
        "id": "c2_01_q097"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welche sprachliche Handlung ist typisch fuer den Nominalstil?",
        "options": [
            "Handlungen werden als Prozesse (Verben) dargestellt.",
            "Handlungen werden als Zustände oder Gegenstaende (Nomen) dargestellt.",
            "Handlungen werden durch Imperative ausgedrueckt.",
            "Handlungen werden durch Modalverben relativiert."
        ],
        "correctAnswer": "Handlungen werden als Zustände oder Gegenstaende (Nomen) dargestellt.",
        "explanation": "Nominal style reifies actions into nouns, e.g., 'die Entscheidung' statt 'entscheiden'.",
        "id": "c2_01_q098"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Um einen Text vom Nominalstil in den Verbalstil zu ueberfuehren, muss man vor allem ____.",
        "options": [
            "Nomen in Verben umwandeln und Nebensaetze bilden",
            "Adjektive streichen",
            "Praepositionen entfernen",
            "Aktiv ins Passiv setzen"
        ],
        "correctAnswer": "Nomen in Verben umwandeln und Nebensaetze bilden",
        "explanation": "Verbal style uses finite verbs and clauses instead of noun phrases.",
        "id": "c2_01_q099"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welche Aussage ueber den Nominalstil im Deutschen trifft zu?",
        "options": [
            "Er ist ein Zeichen fuer mangelnde Sprachkompetenz.",
            "Er ist in der muendlichen Kommunikation genauso haeufig wie in der schriftlichen.",
            "Er kann die Objektivitaet und Praezision eines Textes erhoehen.",
            "Er kommt nur in der deutschen Sprache vor."
        ],
        "correctAnswer": "Er kann die Objektivitaet und Praezision eines Textes erhoehen.",
        "explanation": "Used appropriately, nominal style increases precision and objectivity, especially in academic writing.",
        "id": "c2_01_q100"
    }
]

data['questions'].extend(new_questions)
data['totalQuestions'] = len(data['questions'])

with open('app/src/main/assets/c2_01.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(new_questions)} questions (q081-q100)")
print(f"Total questions now: {data['totalQuestions']}")
easy = sum(1 for q in data['questions'] if q['difficulty'] == 'easy')
medium = sum(1 for q in data['questions'] if q['difficulty'] == 'medium')
hard = sum(1 for q in data['questions'] if q['difficulty'] == 'hard')
print(f"Difficulty breakdown: easy={easy}, medium={medium}, hard={hard}")