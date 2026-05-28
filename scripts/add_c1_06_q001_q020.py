import json

questions = [
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welches Modalverb drueckt eine fast sichere Vermutung (ca. 90%) aus? 'Das Licht brennt noch. Er ____ noch im Buero arbeiten.'",
        "options": ["muss", "duerfte", "kann", "soll"],
        "correctAnswer": "muss",
        "explanation": "Subjective use of 'müssen' indicates an absolute high-probability conviction or near certainty based on visible evidence."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Ergaenzen Sie das passende Modalverb fuer ein unbestaetigtes Geruecht: 'Laut Zeitungsberichten ____ der Vorstand heimlich Gelder veruntreut haben.'",
        "options": ["soll", "muss", "will", "darf"],
        "correctAnswer": "soll",
        "explanation": "The subjective modal verb 'sollen' is used when reporting public rumors, hearsay, or third-party claims without claiming personal verification."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welche subjektive Bedeutung vermittelt das Modalverb 'wollen' hier? 'Der Angeklagte will zur Tatzeit geschlafen haben.'",
        "options": [
            "Der Angeklagte behauptet das ueber sich selbst, aber man zweifelt daran.",
            "Der Angeklagte hatte die feste Absicht, zu schlafen.",
            "Ein Zeuge sagt, dass der Angeklagte geschlafen hat.",
            "Es ist absolut sicher, dass der Angeklagte geschlafen hat."
        ],
        "correctAnswer": "Der Angeklagte behauptet das ueber sich selbst, aber man zweifelt daran.",
        "explanation": "The subjective use of 'wollen' expresses a self-assertion or claim made by the subject which is often met with skepticism by the narrator."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Ergaenzen Sie die Luecke fuer eine vorsichtige, hoefliche Vermutung (ca. 50-70%): 'Die Reparatur des Laptops ____ schaetzungsweise 200 Euro kosten.'",
        "options": ["duerfte", "will", "muss", "sollte"],
        "correctAnswer": "duerfte",
        "explanation": "'Duerfen' in Konjunktiv II ('duerfte') represents a calculated, cautious estimation or a highly probable assumption."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Wie drueckt man aus, dass eine vergangene Aktion eine verpasste Pflicht war? 'du ____ dich frueher um das Visum kuemmern muessen!'",
        "options": ["haettest", "hast", "waerst", "musst"],
        "correctAnswer": "haettest",
        "explanation": "To express an unfulfilled past obligation or missed opportunity, use Konjunktiv II of 'haben' ('haettest') combined with the double infinitive structure."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welches Modalverb passt, um eine bloe Moeglichkeit oder Ungewissheit auszudruecken? 'Es ____ sein, dass der Streik morgen abgesagt wird, aber niemand weiss es genau.'",
        "options": ["kann", "muss", "soll", "will"],
        "correctAnswer": "kann",
        "explanation": "The subjective use of 'koennen' signals a simple possibility or hypothesis (around 50% probability)."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Analysieren Sie die Vergangenheit: 'Er konnte die Pruefung nicht mitschreiben.' Was bedeutet dieser objektive Satz?",
        "options": [
            "Es war ihm aus aeusseren Gruenden unmoeglich, die Pruefung mitzuschreiben.",
            "Es ist moeglich, dass er die Pruefung nicht mitgeschrieben hat.",
            "Er wollte die Pruefung eigentlich gar nicht mitschreiben.",
            "Er haette die Pruefung mitschreiben muessen, hat es aber vergessen."
        ],
        "correctAnswer": "Es war ihm aus aeusseren Gruenden unmoeglich, die Pruefung mitzuschreiben.",
        "explanation": "Objective use of 'koennen' in Prateritum indicates factual ability or possibility in the past. Here, it denotes an objective impossibility."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Was bedeutet der Satz mit subjektivem Modalverb? 'Sie mag damals 20 Jahre alt gewesen sein.'",
        "options": [
            "Der Sprecher vermutet vage, dass sie damals etwa 20 Jahre alt war.",
            "Sie hatte eine Vorliebe dafuer, 20 Jahre alt zu sein.",
            "Sie durfte das Labor erst betreten, als sie 20 Jahre alt war.",
            "Es ist voellig unmoeglich, dass sie damals 20 Jahre alt war."
        ],
        "correctAnswer": "Der Sprecher vermutet vage, dass sie damals etwa 20 Jahre alt war.",
        "explanation": "The subjective use of 'moegen' + Infinitiv Perfekt expresses a concessive or vague present assumption about a past event."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Ergaenzen Sie die Luecke: 'Der neue Mitarbeiter spricht hervorragend Japanisch. Er ____ jahrelang in Tokio gelebt haben.'",
        "options": ["muss", "soll", "darf", "mag"],
        "correctAnswer": "muss",
        "explanation": "Because of the strong evidence ('spricht hervorragend Japanisch'), the speaker draws a logical conclusion about the past with near-absolute certainty, which requires subjective 'muessen' + Infinitiv Perfekt."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Waehlen Sie die korrekte Struktur fuer das Passiv mit Modalverb: 'Dieses Problem ____ geloest werden.'",
        "options": ["muss umgehend", "umgehend muss", "wird umgehend", "hat umgehend"],
        "correctAnswer": "muss umgehend",
        "explanation": "Standard syntax for passive voice with modal verbs places the inflected modal verb in position 2, followed by modifiers, and ends with Partizip II + 'werden'."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welcher Satz drueckt eine scharfe Distanzierung des Sprechers von einer Behauptung aus?",
        "options": [
            "Der Politiker will von den Schmiergeldern nichts gewusst haben.",
            "Der Politiker muss von den Schmiergeldern nichts gewusst haben.",
            "Der Politiker duerfte von den Schmiergeldern nichts gewusst haben.",
            "Der Politiker konnte von den Schmiergeldern nichts wissen."
        ],
        "correctAnswer": "Der Politiker will von den Schmiergeldern nichts gewusst haben.",
        "explanation": "Subjective 'wollen' explicitly communicates that the subject is making a self-serving claim, heavily implying that the speaker does not believe them."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Ergaenzen Sie das Modalverb im Konjunktiv II fuer eine Empfehlung: 'Es ist schon sehr spät. Sie ____ langsam den Heimweg antreten.'",
        "options": ["sollten", "muessten", "duerften", "wollten"],
        "correctAnswer": "sollten",
        "explanation": "'Sollten' (Konjunktiv II of sollen) is the standard, polite way to formulate an advisory recommendation or soft duty."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Verwandeln Sie den Satz in die subjektive Vergangenheit: 'Ich vermute, dass sie den Zug verpasst hat.' -> 'Sie ____ den Zug verpasst ____.'",
        "options": ["kann ... haben", "konnte ... haben", "kann ... sein", "muss ... verpassen"],
        "correctAnswer": "kann ... haben",
        "explanation": "A present assumption about a past action uses the present form of the subjective modal verb ('kann') + the Infinitiv Perfekt of the main verb ('verpasst haben')."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Was bedeutet 'nicht duerfen' in folgendem rechtlichen Kontext? 'Dokumente duerfen nicht ohne Unterschrift vernichtet werden.'",
        "options": [
            "Es ist strengstens verboten, diese Dokumente ohne Unterschrift zu vernichten.",
            "Es ist nicht notwendig, die Dokumente zu unterschreiben.",
            "Man kann die Dokumente vernichten, wenn man moechte.",
            "Es wird vermutet, dass die Dokumente keine Unterschrift haben."
        ],
        "correctAnswer": "Es ist strengstens verboten, diese Dokumente ohne Unterschrift zu vernichten.",
        "explanation": "Negated 'duerfen' ('nicht duerfen') means strict prohibition or ban, especially in regulatory or legal frameworks."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welches Modalverb ersetzt den Ausdruck 'Ich bin nicht in der Lage': Ich ____ die Deadline unmöglich einhalten.",
        "options": ["kann", "darf", "muss", "soll"],
        "correctAnswer": "kann",
        "explanation": "Objective 'koennen' expresses ability/capability. Combined with 'unmoeglich', it denotes an absolute inability to execute an action."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Ergaenzen Sie die Luecke in diesem Nebensatz: 'Da der Zeuge den Taeter nicht genau gesehen ____ haben will, wurde das Verfahren eingestellt.'",
        "options": ["haben", "hat", "haette", "wollte"],
        "correctAnswer": "haben",
        "explanation": "In a subordinate clause with subjective 'wollen' + past infinitive, the conjugated auxiliary ('haben') goes before the double infinitive: '...dass er das gesagt haben muss'."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welche Nuance transportiert das Modalverb 'sollen' in einer Frage wie: 'Soll ich Ihnen bei den Koffern helfen?'",
        "options": [
            "Ein Angebot oder ein Vorschlag.",
            "Ein strenger Befehl an sich selbst.",
            "Eine Weiterleitung eines Geruechts.",
            "Ein unbedingtes Verbot."
        ],
        "correctAnswer": "Ein Angebot oder ein Vorschlag.",
        "explanation": "Using 'sollen' in the first person singular interrogative form ('Soll ich...?') translates directly to offering assistance or proposing an action."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Finden Sie die fehlerhafte subjektive Satzstruktur:",
        "options": [
            "Er mag das wohl vergessen haben.",
            "Sie muss gestern krank gewesen sein.",
            "Er will das Geld gestern gestohlen haben gemusst.",
            "Sie duerften die Nachricht bereits erhalten haben."
        ],
        "correctAnswer": "Er will das Geld gestern gestohlen haben gemusst.",
        "explanation": "You cannot chain subjective assertions using past participles of modal verbs ('gemusst') in this manner. The construction is completely ungrammatical."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Ergaenzen Sie das passende Verb: 'Wer promovieren moechte, ____ eine enorme wissenschaftliche Ausdauer mitbringen.' (Bedeutung: Es ist eine zwingende Voraussetzung)",
        "options": ["muss", "sollte", "darf", "mag"],
        "correctAnswer": "muss",
        "explanation": "An objective absolute requirement, inescapable precondition, or natural necessity is expressed via 'muessen'."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welches Modalverb passt hier am besten? 'Nach der langen Reise ____ die Urlauber voellig erschoepft sein.' (Vermutung liegt sehr nahe)",
        "options": ["duerften", "wollen", "moegen", "koennen"],
        "correctAnswer": "duerften",
        "explanation": "'Duerften' (Konjunktiv II) signals a highly logical probability based on standard human experience (long travel leads to exhaustion)."
    }
]


def add_qs(topic_json_path, questions, topic_name_str):
    with open(topic_json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    added = 0
    for q in questions:
        new_id = f"{topic_name_str}_q{len(data['questions']) + 1:03d}"
        q['id'] = new_id
        data['questions'].append(q)
        added += 1

    data['totalQuestions'] = len(data['questions'])

    with open(topic_json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Added {added} questions to {topic_json_path}")
    print(f"New total: {data['totalQuestions']}")


if __name__ == '__main__':
    add_qs('app/src/main/assets/c1_06.json', questions, 'c1_06')
