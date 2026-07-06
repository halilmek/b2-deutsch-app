import json

NEW_QUESTIONS = [
    {
        "id": "c2_12_q021",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Lass das ______ bleiben, das könnte gefährlich werden!",
        "options": ["bloß", "eben", "wohl", "denn"],
        "correctAnswer": "bloß",
        "explanation": "'Bloß' verstärkt in Imperativsätzen eine Warnung oder einen dringenden Rat: 'Lass das bloß bleiben!' signalisiert eine ernste Ermahnung.",
        "difficulty": "medium",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q022",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Komm ______ her, wenn du dich traust!",
        "options": ["nur", "eben", "wohl", "ruhig"],
        "correctAnswer": "nur",
        "explanation": "'Nur' verstärkt in Aufforderungen einen herausfordernden oder ermutigenden Ton: 'Komm nur her!' klingt wie eine Provokation oder Einladung.",
        "difficulty": "medium",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q023",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Ich habe ______ keine Ahnung, wovon du sprichst.",
        "options": ["überhaupt", "ruhig", "eben", "denn"],
        "correctAnswer": "überhaupt",
        "explanation": "'Überhaupt' verstärkt in Verbindung mit einer Verneinung die Aussage zu einer absoluten Verneinung: 'überhaupt keine Ahnung' = absolut keine Ahnung.",
        "difficulty": "easy",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q024",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Ich wäre ______ zu spät gekommen, auch ohne den Stau.",
        "options": ["sowieso", "ruhig", "denn", "bloß"],
        "correctAnswer": "sowieso",
        "explanation": "'Sowieso' drückt aus, dass etwas unabhängig von den genannten Umständen ohnehin der Fall gewesen wäre — hier: die Verspätung wäre auch ohne Stau eingetreten.",
        "difficulty": "medium",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q025",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Du brauchst nicht zu kommen, ich schaffe das ______ allein.",
        "options": ["ohnehin", "bloß", "denn", "mal"],
        "correctAnswer": "ohnehin",
        "explanation": "'Ohnehin' (Synonym zu 'sowieso') signalisiert, dass eine Handlung auch ohne die erwähnte Bedingung eintreten würde — hier: die Aufgabe wird unabhängig von Hilfe allein bewältigt.",
        "difficulty": "medium",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q026",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Das Ergebnis ist ______ nicht optimal, aber immerhin ein Anfang.",
        "options": ["zwar", "eben", "denn", "ruhig"],
        "correctAnswer": "zwar",
        "explanation": "'Zwar' leitet eine konzessive Einschränkung ein, die meist mit 'aber' fortgesetzt wird: 'zwar nicht optimal, aber immerhin ein Anfang' — eine Konzession vor einem Gegenargument.",
        "difficulty": "hard",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q027",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Wir haben das Ziel nicht ganz erreicht, aber ______ haben wir viel gelernt.",
        "options": ["immerhin", "bloß", "denn", "wohl"],
        "correctAnswer": "immerhin",
        "explanation": "'Immerhin' drückt eine positive Relativierung aus — trotz eines negativen Gesamtergebnisses wird ein positiver Teilaspekt hervorgehoben (hier: der Lerneffekt).",
        "difficulty": "medium",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q028",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Das ist ______ eine ungewöhnliche Frage, aber ich beantworte sie gerne.",
        "options": ["allerdings", "bloß", "ruhig", "denn"],
        "correctAnswer": "allerdings",
        "explanation": "'Allerdings' signalisiert hier eine milde Einschränkung/Zugeständnis vor einer Fortsetzung — vergleichbar mit 'zwar', oft gefolgt von einem Kontrastsatz.",
        "difficulty": "hard",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q029",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Das ist ______ eine gute Idee, aber leider zu teuer.",
        "options": ["freilich", "bloß", "ruhig", "mal"],
        "correctAnswer": "freilich",
        "explanation": "'Freilich' (gehoben, süddeutsch/österreichisch geprägt, = 'natürlich/gewiss') bestätigt einen Sachverhalt, bevor eine einschränkende Fortsetzung folgt.",
        "difficulty": "hard",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q030",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Was hast du dir ______ dabei gedacht?",
        "options": ["bloß", "ruhig", "wohl", "ja"],
        "correctAnswer": "bloß",
        "explanation": "In Fragen drückt 'bloß' (ähnlich wie 'nur') Verwunderung, Vorwurf oder Ratlosigkeit aus: 'Was hast du dir bloß dabei gedacht?' klingt nach echtem Unverständnis/Vorwurf.",
        "difficulty": "medium",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q031",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Welche Funktion hat 'überhaupt' in der Frage: 'Willst du das überhaupt?'",
        "options": [
            "Es hinterfragt grundsätzlich, ob der genannte Wunsch überhaupt besteht.",
            "Es bestätigt, dass der Wunsch mit Sicherheit besteht.",
            "Es mildert die Frage höflich ab.",
            "Es signalisiert, dass die Frage bereits beantwortet wurde."
        ],
        "correctAnswer": "Es hinterfragt grundsätzlich, ob der genannte Wunsch überhaupt besteht.",
        "explanation": "'Überhaupt' in Fragen stellt die grundsätzliche Voraussetzung infrage — hier wird nicht nach Details gefragt, sondern ob der Wunsch an sich überhaupt vorhanden ist.",
        "difficulty": "hard",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q032",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Welches Wortpaar ist bedeutungsgleich und in den meisten Kontexten austauschbar?",
        "options": ["sowieso / ohnehin", "bloß / denn", "ruhig / eben", "ja / wohl"],
        "correctAnswer": "sowieso / ohnehin",
        "explanation": "'Sowieso' und 'ohnehin' sind nahezu bedeutungsgleiche Modalpartikeln, die beide ausdrücken, dass etwas unabhängig von den genannten Umständen der Fall ist/wäre.",
        "difficulty": "medium",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q033",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Er hat die Prüfung nicht bestanden. ______ hat er es überhaupt versucht — das zählt auch etwas.",
        "options": ["Immerhin", "Bloß", "Denn", "Ruhig"],
        "correctAnswer": "Immerhin",
        "explanation": "'Immerhin' leitet hier eine relativierende, positive Gegenperspektive zu einer negativen Aussage ein — der Versuch selbst wird als Teilerfolg gewürdigt.",
        "difficulty": "medium",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q034",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Warum lässt sich 'sowieso' NICHT durch eine Modalpartikel wie 'ja' ersetzen, obwohl beide unbetont sein können?",
        "options": [
            "Weil 'sowieso' eine eigenständige, festere Bedeutung (ohnehin/in jedem Fall) trägt, während 'ja' nur geteiltes Wissen signalisiert.",
            "Weil 'sowieso' nur in Fragen stehen darf.",
            "Weil 'sowieso' immer betont werden muss.",
            "Weil 'ja' ausschließlich in der Vergangenheit verwendet wird."
        ],
        "correctAnswer": "Weil 'sowieso' eine eigenständige, festere Bedeutung (ohnehin/in jedem Fall) trägt, während 'ja' nur geteiltes Wissen signalisiert.",
        "explanation": "Modalpartikeln unterscheiden sich in ihrer spezifischen pragmatischen Funktion; 'sowieso' hat eine klar umrissene Bedeutung (Unabhängigkeit von Umständen), die nicht mit der reinen Bekanntheits-Markierung von 'ja' austauschbar ist.",
        "difficulty": "hard",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q035",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Welche Umschreibung passt am besten zu 'Er kommt sowieso zu spät.' im formellen Schreiben?",
        "options": [
            "Er wird ohnehin verspätet eintreffen.",
            "Er wird ja verspätet eintreffen.",
            "Er wird ruhig verspätet eintreffen.",
            "Er wird bloß verspätet eintreffen."
        ],
        "correctAnswer": "Er wird ohnehin verspätet eintreffen.",
        "explanation": "'Ohnehin' ist im formellen Register gebräuchlicher als 'sowieso' und behält dieselbe Bedeutung (unabhängig von den Umständen).",
        "difficulty": "medium",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q036",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Was unterscheidet 'allerdings' als Modalpartikel von 'allerdings' als Antwortpartikel ('Kommst du mit? – Allerdings!')?",
        "options": [
            "Als Antwortpartikel bedeutet es 'ja, unbedingt' (bekräftigend), als Modalpartikel leitet es eine Einschränkung ein.",
            "Es gibt keinen Unterschied — beide Verwendungen sind identisch.",
            "Als Antwortpartikel ist es unbetont, als Modalpartikel wird es immer betont.",
            "Als Modalpartikel darf es nur am Satzende stehen."
        ],
        "correctAnswer": "Als Antwortpartikel bedeutet es 'ja, unbedingt' (bekräftigend), als Modalpartikel leitet es eine Einschränkung ein.",
        "explanation": "'Allerdings' als alleinstehende Antwort bekräftigt zustimmend ('Ja, unbedingt!'), während es im Satz als Modalpartikel eine Einschränkung/Konzession einleitet ('Das ist allerdings teuer.').",
        "difficulty": "hard",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q037",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Frag ihn ______, ob er mitkommen möchte — schaden kann es nicht.",
        "options": ["ruhig", "bloß", "sowieso", "immerhin"],
        "correctAnswer": "ruhig",
        "explanation": "'Ruhig' signalisiert hier erneut Erlaubnis/Ermutigung ohne Bedenken — die Handlung ist risikofrei, wie der Nachsatz 'schaden kann es nicht' bestätigt.",
        "difficulty": "easy",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q038",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Er hat ______ nichts falsch gemacht — warum wird er dann kritisiert?",
        "options": ["doch", "bloß", "sowieso", "immerhin"],
        "correctAnswer": "doch",
        "explanation": "'Doch' widerspricht hier einer impliziten gegenteiligen Annahme (dass er etwas falsch gemacht habe) und verleiht der Aussage einen insistierenden Ton.",
        "difficulty": "medium",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q039",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Welcher Satz zeigt die korrekte Kombination 'ja sowieso', die Bekanntheit UND Unabhängigkeit von Umständen ausdrückt?",
        "options": [
            "Das wusste ich ja sowieso schon.",
            "Das wusste ich sowieso ja schon.",
            "Das ja wusste ich sowieso schon.",
            "Sowieso das wusste ich ja schon."
        ],
        "correctAnswer": "Das wusste ich ja sowieso schon.",
        "explanation": "Bei Kombinationen aus Modalpartikel + Gradpartikel/Adverb wie 'sowieso' steht die reine Modalpartikel ('ja') meist vor dem spezifischeren Zusatz ('sowieso'): 'ja sowieso' ist die natürliche Reihenfolge.",
        "difficulty": "hard",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q040",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Welche der folgenden Modalpartikeln eignet sich am wenigsten für einen formellen Bericht?",
        "options": ["halt", "vermutlich (Adverb)", "offensichtlich (Adverb)", "daher (Konnektor)"],
        "correctAnswer": "halt",
        "explanation": "'Halt' ist eine regional geprägte, umgangssprachliche Modalpartikel und sollte in formellen Berichten durch Adverbien wie 'offensichtlich' oder 'nun einmal' ersetzt werden. Die anderen Optionen sind bereits formelle Adverbien/Konnektoren.",
        "difficulty": "medium",
        "type": "multiple_choice",
        "reviewed": False
    }
]

path = 'app/src/main/assets/c2_12.json'
data = json.load(open(path, encoding='utf-8'))
existing_ids = {q['id'] for q in data['questions']}
added = [q for q in NEW_QUESTIONS if q['id'] not in existing_ids]
data['questions'].extend(added)
data['totalQuestions'] = len(data['questions'])

for out_path in [path, 'content/grammar/c2_12.json']:
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f'Updated {out_path}: {len(data["questions"])} questions total')
