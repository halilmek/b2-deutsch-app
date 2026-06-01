import json

with open('app/src/main/assets/c2_02.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

existing_count = len(data['questions'])
print(f"Existing questions: {existing_count}")

new_questions = [
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Was bedeutet die konzessive Struktur 'wie auch immer'?",
        "options": [
            "Auch wenn etwas nicht eintritt",
            "Unabhaengig davon, was geschieht",
            "Wegen einer bestimmten Situation",
            "Nachdem etwas geschehen ist"
        ],
        "correctAnswer": "Unabhaengig davon, was geschieht",
        "explanation": "'Wie auch immer' drueckt eine vollstaendige Konzession aus und bedeutet 'unabhaengig davon, was geschieht /无论如何'.",
        "id": "c2_02_q081"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welche konzessive Konjunktion ist am formellsten fuer akademische Texte?",
        "options": [
            "obwohl",
            "wenn auch",
            "obgleich",
            "wofern"
        ],
        "correctAnswer": "obgleich",
        "explanation": "'Obgleich' ist die formellste Variante und wird vor allem in wissenschaftlichen und juristischen Texten verwendet.",
        "id": "c2_02_q082"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Was ist der Unterschied zwischen 'obwohl' und 'wenn auch'?",
        "options": [
            "'Obwohl' ist eine Nebensatzkonjunktion, 'wenn auch' eine Adverbialphrase.",
            "'Wenn auch' erfordert den Konjunktiv, 'obwohl' den Indikativ.",
            "Es gibt keinen semantischen Unterschied, nur stilistische Nuancen.",
            "'Obwohl' leitet Konzessionen ein, 'wenn auch' Conditionalis."
        ],
        "correctAnswer": "Es gibt keinen semantischen Unterschied, nur stilistische Nuancen.",
        "explanation": "Beide fuehren konzessive Nebensaetze ein. 'Obwohl' ist neutral, 'wenn auch' klingt leicht gehobener.",
        "id": "c2_02_q083"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welche Partikelverstärkung macht 'obwohl' noch emphatischer?",
        "options": [
            "obwohl schon",
            "obwohl doch",
            "obwohl auch",
            "obwohl gar"
        ],
        "correctAnswer": "obwohl auch",
        "explanation": "'Obwohl auch' verstaerkt die konzessive Bedeutung und betont die Unvermeidlichkeit des Widerspruchs.",
        "id": "c2_02_q084"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Was ist die korrekte Stellung von 'auch' in der Struktur 'wenn...auch'?",
        "options": [
            "Immer vor dem Subjekt",
            "Nach dem Subjekt, vor dem Verb",
            "Am Satzende",
            "Vor der Konjunktion 'wenn'"
        ],
        "correctAnswer": "Nach dem Subjekt, vor dem Verb",
        "explanation": "In 'wenn...auch' folgt 'auch' direkt nach dem Subjekt: 'wenn er auch kommt'.",
        "id": "c2_02_q085"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welche Präposition erfordert 'trotz' im Unterschied zu den meisten anderen Präpositionen?",
        "options": [
            "Akkusativ",
            "Dativ",
            "Genitiv",
            "Wechselpräposition"
        ],
        "correctAnswer": "Genitiv",
        "explanation": "'Trotz' ist eine der wenigen praepositionen, die den Genitiv erfordern (neben wegen, während, statt, trotz, ungeachtet, mangels, anstatt, ausschließlich, etc.).",
        "id": "c2_02_q086"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welche Konstruktion wird als 'freie Relative' im konzessiven Kontext bezeichnet?",
        "options": [
            "Was auch immer geschieht",
            "Wenn etwas geschieht",
            "Damit etwas geschieht",
            "Weil etwas geschieht"
        ],
        "correctAnswer": "Was auch immer geschieht",
        "explanation": "Freie Relative mit 'was/wer/wie/wann + auch + Verb' drueckt eine generelle Konzession aus: 'was auch immer geschieht' = 'egal was geschieht'.",
        "id": "c2_02_q087"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Wie transformiert man 'Obwohl die Kritik berechtigt war, nahm er die Stelle an' in den gehobenen Nominalstil?",
        "options": [
            "Wegen der berechtigten Kritik nahm er die Stelle an.",
            "Trotz der berechtigten Kritik nahm er die Stelle an.",
            "Ungeachtet der Kritikberechtigung nahm er die Stelle an.",
            "Die Kritik war berechtigt, trotzdem nahm er die Stelle an."
        ],
        "correctAnswer": "Ungeachtet der berechtigten Kritik nahm er die Stelle an.",
        "explanation": "'Ungeachtet + Genitiv' ist die gehobene nominale Form von 'obwohl'. Die Adjektivkonstruktion 'berechtigt' wird Teil des Genitivattributs.",
        "id": "c2_02_q088"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welche Verbindung ist ein korrektes Funktionsverbgefüge mit konzessiver Bedeutung?",
        "options": [
            "etwas in Frage stellen",
            "von etwas absehen",
            "etwas in Betracht ziehen",
            "etwas zur Kenntnis nehmen"
        ],
        "correctAnswer": "von etwas absehen",
        "explanation": "'Von etwas absehen' bedeutet 'etwas nicht berücksichtigen / ignore', was konzessiv interpretiert werden kann: 'ungeachtet einer Sache handeln'.",
        "id": "c2_02_q089"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Was ist bei 'mag' in konzessiven Strukturen zu beachten?",
        "options": [
            "Es steht immer im Indikativ.",
            "Es ist eine veraltete Konjunktion.",
            "Es kann subjunctive/moegen Form annehmen.",
            "Es erfordert immer den Dativ."
        ],
        "correctAnswer": "Es kann subjunctive/moegen Form annehmen.",
        "explanation": "'Mag' ist die Konjunktivform von 'moegen' und wird in gehobenen konzessiven Strukturen verwendet: 'mag er auch kommen'.",
        "id": "c2_02_q090"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welches Adverb ist ein Synonym fuer 'trotzdem' mit gehobener Konnotation?",
        "options": [
            "dennoch",
            "jedoch",
            "allerdings",
            "zwar"
        ],
        "correctAnswer": "dennoch",
        "explanation": "'Dennoch' ist ein gehobenes Synonym fuer 'trotzdem' und wird häufig in wissenschaftlichen und journalistischen Texten verwendet.",
        "id": "c2_02_q091"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Was bedeutet 'sosehr' in einer konzessiven Struktur?",
        "options": [
            "Sehr wichtig",
            "Wie sehr auch immer",
            "Deshalb",
            "Deswegen"
        ],
        "correctAnswer": "Wie sehr auch immer",
        "explanation": "'Sosehr' fungiert als Konjunktion und bedeutet 'no matter how much': 'sosehr er sich auch bemuehte'.",
        "id": "c2_02_q092"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welches der folgenden Woerter ist KEINE konzessive Konjunktion?",
        "options": [
            "obschon",
            "wiewohl",
            "soweit",
            "wenngleich"
        ],
        "correctAnswer": "soweit",
        "explanation": "'Soweit' ist ein Conditionalausdruck ('insofern'), keine Konzession. 'Obschon', 'wiewohl' und 'wenngleich' sind konzessiv.",
        "id": "c2_02_q093"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welche Struktur verwendet man für eine 'irreale Konzession'?",
        "options": [
            "obwohl + Indikativ",
            "selbst wenn + Konjunktiv II",
            "weil + Genitiv",
            "trotz + Dativ"
        ],
        "correctAnswer": "selbst wenn + Konjunktiv II",
        "explanation": "'Selbst wenn' mit Konjunktiv II drueckt eine irreale oder hypothetische Konzession aus: 'selbst wenn er käme' (aber er kommt nicht).",
        "id": "c2_02_q094"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Was ist bei der Verwendung von 'wogegen' zu beachten?",
        "options": [
            "Es leitet einen Temporalsatz ein.",
            "Es ist ein Relativpronomen mit konzessiver Bedeutung.",
            "Es erfordert den Akkusativ.",
            "Es steht immer am Satzende."
        ],
        "correctAnswer": "Es ist ein Relativpronomen mit konzessiver Bedeutung.",
        "explanation": "'Wogegen' ist ein_RELATIVPRONOMEN_ in Verbindung mit einem vorangehenden Demonstrativum und drueckt einen konzessiven Gegensatz aus.",
        "id": "c2_02_q095"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welche nominale Form entspricht 'obwohl er krank war'?",
        "options": [
            "Wegen seiner Krankheit",
            "Trotz seiner Krankheit",
            "Mit seiner Krankheit",
            "Seine Krankheit betreffend"
        ],
        "correctAnswer": "Trotz seiner Krankheit",
        "explanation": "'Trotz + Genitiv' ist die nominale Aequivalentstruktur zu 'obwohl + Nebensatz'.",
        "id": "c2_02_q096"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Was ist die korrekte Reihenfolge bei 'so + Adjektiv + auch'?",
        "options": [
            "So + auch + Adjektiv + Subjekt + Verb",
            "So + Adjektiv + Subjekt + auch + Verb",
            "Adjektiv + So + Subjekt + auch + Verb",
            "So + Subjekt + Adjektiv + Verb + auch"
        ],
        "correctAnswer": "So + Adjektiv + Subjekt + auch + Verb",
        "explanation": "Die korrekte Wortstellung ist: 'So + Adjektiv + Subjekt + auch + Verb' z.B. 'So muede er auch war'.",
        "id": "c2_02_q097"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welche konzessive Struktur ist als 'korreliativ' bekannt?",
        "options": [
            "obwohl ... deshalb",
            "zwar ... aber",
            "weil ... also",
            "wenn ... dann"
        ],
        "correctAnswer": "zwar ... aber",
        "explanation": "'Zwar ... aber' ist eine korrelative Struktur, bei der 'zwar' den Sachverhalt einraeumt und 'aber' den Gegensatz einfuehrt.",
        "id": "c2_02_q098"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welche Funktion hat 'daran' in der Struktur 'ungeachtet daran'?",
        "options": [
            "Es verstärkt die konzessive Bedeutung.",
            "Es bezieht sich auf einen vorherigen Satz.",
            "Es ist ein Demonstrativpronomen.",
            "Es ist überflüssig."
        ],
        "correctAnswer": "Es bezieht sich auf einen vorherigen Satz.",
        "explanation": "'Daran' ist ein Demonstrativpronomen, das sich auf den zuvor genannten Sachverhalt bezieht: 'ungeachtet daran' = 'trotz dieser Tatsache'.",
        "id": "c2_02_q099"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Was ist ein typischer Fehler bei der Verwendung von 'obwohl dass'?",
        "options": [
            "'Obwohl' kann nicht mit 'dass' kombiniert werden.",
            "'Dass' muss immer groß geschrieben werden.",
            "'Obwohl' und 'dass' sind synonym.",
            "'Dass' ist überflüssig, aber grammatisch korrekt."
        ],
        "correctAnswer": "'Obwohl' kann nicht mit 'dass' kombiniert werden.",
        "explanation": "'Obwohl dass' ist ein Grammatikfehler. 'Obwohl' ist bereits eine Subjunktor und leitet einen Nebensatz ein; 'dass' ist redundand.",
        "id": "c2_02_q100"
    }
]

data['questions'].extend(new_questions)
data['totalQuestions'] = len(data['questions'])

with open('app/src/main/assets/c2_02.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(new_questions)} questions (q081-q100)")
print(f"Total questions now: {data['totalQuestions']}")
easy = sum(1 for q in data['questions'] if q['difficulty'] == 'easy')
medium = sum(1 for q in data['questions'] if q['difficulty'] == 'medium')
hard = sum(1 for q in data['questions'] if q['difficulty'] == 'hard')
print(f"Difficulty breakdown: easy={easy}, medium={medium}, hard={hard}")