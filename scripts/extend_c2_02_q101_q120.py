import json

with open('app/src/main/assets/c2_02.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

existing_count = len(data['questions'])
print(f"Existing questions: {existing_count}")

new_questions = [
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Erweiterte Konzessivstrukturen druecken aus, dass etwas ____.",
        "options": [
            "eine Ursache hat",
            "eine Folge ist",
            "trotz eines Gegengrundes gilt",
            "unter einer Bedingung steht"
        ],
        "correctAnswer": "trotz eines Gegengrundes gilt",
        "explanation": "Concessive structures express that something holds true despite an opposing reason.",
        "id": "c2_02_q101"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welche Konjunktion leitet einen klassischen Konzessivsatz ein?",
        "options": [
            "weil",
            "obwohl",
            "damit",
            "falls"
        ],
        "correctAnswer": "obwohl",
        "explanation": "'Obwohl' is the standard concessive conjunction meaning 'although'.",
        "id": "c2_02_q102"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "____ er sich sehr anstrengte, gelang ihm der Durchbruch nicht.",
        "options": [
            "Trotz",
            "Obwohl",
            "Trotzdem",
            "Wegen"
        ],
        "correctAnswer": "Obwohl",
        "explanation": "'Obwohl' introduces a concessive clause; 'trotz' is a preposition.",
        "id": "c2_02_q103"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welche der folgenden Praepositionen leitet eine konzessive Nominalphrase ein?",
        "options": [
            "aufgrund",
            "mangels",
            "trotz",
            "laut"
        ],
        "correctAnswer": "trotz",
        "explanation": "'Trotz' is a preposition used for concessive noun phrases (e.g., 'trotz des Regens').",
        "id": "c2_02_q104"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "____ des schlechten Wetters fand das Konzert statt.",
        "options": [
            "Trotz",
            "Obwohl",
            "Ungeachtet",
            "Trotzdem"
        ],
        "correctAnswer": "Ungeachtet",
        "explanation": "'Ungeachtet' (formal for 'despite') is correct here; 'trotz' would also fit but 'ungeachtet' is a valid elevated variant.",
        "id": "c2_02_q105"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welches ist eine erweiterte konzessive Struktur mit 'auch'?",
        "options": [
            "weil er auch muede war",
            "wenn er auch muede war",
            "ob er auch muede war",
            "auch wenn er muede war"
        ],
        "correctAnswer": "auch wenn er muede war",
        "explanation": "'Auch wenn' is an extended concessive structure meaning 'even if'.",
        "id": "c2_02_q106"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "____ du dir noch so grosse Muehe gibst, du wirst ihn nicht ueberzeugen.",
        "options": [
            "Wenn",
            "Obwohl",
            "So sehr",
            "Mag"
        ],
        "correctAnswer": "Mag",
        "explanation": "'Mag' (as in 'Mag ... auch') is an archaic/literary concessive structure (e.g., 'Mag er sich auch bemuehen').",
        "id": "c2_02_q107"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welche Konstruktion ist typisch fuer eine erweiterte konzessive Struktur im geschriebenen Deutsch?",
        "options": [
            "Noch so + Adjektiv + Hauptsatz",
            "Weil + Nebensatz",
            "Damit + Nebensatz",
            "Als ob + Nebensatz"
        ],
        "correctAnswer": "Noch so + Adjektiv + Hauptsatz",
        "explanation": "'Noch so sehr', 'noch so gut' etc. appear in concessive patterns (e.g., 'Noch so klug, er irrt sich').",
        "id": "c2_02_q108"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Erweiterte Konzessivstrukturen werden haeufig in ____ verwendet.",
        "options": [
            "Alltagsdialogen",
            "wissenschaftlichen Texten und formaler Rede",
            "Kindergeschichten",
            "Werbeanzeigen"
        ],
        "correctAnswer": "wissenschaftlichen Texten und formaler Rede",
        "explanation": "Extended concessive forms like 'wenngleich', 'so...auch' are typical of academic/formal German.",
        "id": "c2_02_q109"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "____ die Hypothese plausibel erscheint, weist sie dennoch Schwaechen auf.",
        "options": [
            "Trotz",
            "Obgleich",
            "Trotzdem",
            "Wohingegen"
        ],
        "correctAnswer": "Obgleich",
        "explanation": "'Obgleich' is a formal concessive conjunction similar to 'obwohl'.",
        "id": "c2_02_q110"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welche der folgenden Formen ist eine konzessive Praeposition mit Genitiv?",
        "options": [
            "dank",
            "laut",
            "unbeschadet",
            "lauter"
        ],
        "correctAnswer": "unbeschadet",
        "explanation": "'Unbeschadet' (meaning 'without prejudice to') is a concessive preposition requiring the genitive.",
        "id": "c2_02_q111"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Im Satz '____ seiner BemuEhungen blieb der Erfolg aus' fehlt eine konzessive Praeposition.",
        "options": [
            "Dank",
            "Wegen",
            "Trotz",
            "Mittels"
        ],
        "correctAnswer": "Trotz",
        "explanation": "'Trotz' (despite) is the standard concessive preposition here.",
        "id": "c2_02_q112"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "____ es ihm an Erfahrung mangelte, ging er das Projekt souveraen an.",
        "options": [
            "Trotz",
            "Wenngleich",
            "Anstatt",
            "Waehrend"
        ],
        "correctAnswer": "Wenngleich",
        "explanation": "'Wenngleich' is a formal, extended concessive conjunction meaning 'although'.",
        "id": "c2_02_q113"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welches Beispiel zeigt eine konzessive Struktur mit 'so' im Vorfeld?",
        "options": [
            "So sehr er sich bemuehte, er schaffte es nicht.",
            "So er sich bemuehte, schaffte er es.",
            "Er bemuehte sich so sehr, dass er es schaffte.",
            "So er sich auch bemuehte, er schaffte es."
        ],
        "correctAnswer": "So sehr er sich bemuehte, er schaffte es nicht.",
        "explanation": "'So sehr ... auch' is an extended concessive pattern; here 'So sehr er sich bemuehte' (without 'auch') still works in elevated style.",
        "id": "c2_02_q114"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welche der folgenden Konstruktionen ist NICHT konzessiv?",
        "options": [
            "bei aller Kritik",
            "was auch immer",
            "je ... desto",
            "ungeachtet der Tatsache"
        ],
        "correctAnswer": "je ... desto",
        "explanation": "'Je ... desto' is comparative, not concessive.",
        "id": "c2_02_q115"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Im akademischen Deutsch wird 'obzwar' verwendet als ____.",
        "options": [
            "kausale Konjunktion",
            "konzessive Konjunktion",
            "finale Konjunktion",
            "modale Konjunktion"
        ],
        "correctAnswer": "konzessive Konjunktion",
        "explanation": "'Obzwar' is a rare, formal concessive conjunction meaning 'although'.",
        "id": "c2_02_q116"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "____ man die Methode verbesserte, blieben die Ergebnisse widerspruechlich.",
        "options": [
            "Unbeschadet",
            "Bei allem, wie",
            "Sooft",
            "Wiewohl"
        ],
        "correctAnswer": "Wiewohl",
        "explanation": "'Wiewohl' is an archaic/formal concessive conjunction (although).",
        "id": "c2_02_q117"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Erweiterte Konzessivstrukturen wie 'wenn ... auch' unterscheiden sich von 'obwohl' primaer durch ____.",
        "options": [
            "ihre rein kausale Bedeutung",
            "ihre staerkere hypothetische oder einraeumende Nuance",
            "ihre Unfaehigkeit, im Nebensatz zu stehen",
            "ihre Beschraenkung auf die Umgangssprache"
        ],
        "correctAnswer": "ihre staerkere hypothetische oder einraeumende Nuance",
        "explanation": "'Wenn ... auch' often concedes a stronger hypothetical or extreme case than 'obwohl'.",
        "id": "c2_02_q118"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welcher Satz enthaelt eine konzessive Struktur mit einer Partizipialgruppe?",
        "options": [
            "Geregnet hat es, aber das Fest fand statt.",
            "Trotz des Regens fand das Fest statt.",
            "Bei Regen fand das Fest statt.",
            "Obwohl es regnete, fand das Fest statt."
        ],
        "correctAnswer": "Bei Regen fand das Fest statt.",
        "explanation": "'Bei Regen' (literally 'with rain') can have a concessive meaning in context, functioning as a participle-like noun phrase.",
        "id": "c2_02_q119"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Die konzessive Konjunktion 'obschon' ist ____.",
        "options": [
            "veraltet und wird nicht mehr verwendet",
            "ein Synonym fuer 'obwohl' im formalen Deutsch",
            "eine kausale Konjunktion",
            "nur in der Schweiz gebraeuchlich"
        ],
        "correctAnswer": "ein Synonym fuer 'obwohl' im formalen Deutsch",
        "explanation": "'Obschon' is a formal, slightly dated synonym for 'obwohl', still used in academic writing.",
        "id": "c2_02_q120"
    }
]

data['questions'].extend(new_questions)
data['totalQuestions'] = len(data['questions'])

with open('app/src/main/assets/c2_02.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(new_questions)} questions (q101-q120)")
print(f"Total questions now: {data['totalQuestions']}")
easy = sum(1 for q in data['questions'] if q['difficulty'] == 'easy')
medium = sum(1 for q in data['questions'] if q['difficulty'] == 'medium')
hard = sum(1 for q in data['questions'] if q['difficulty'] == 'hard')
print(f"Difficulty breakdown: easy={easy}, medium={medium}, hard={hard}")