import json

questions = [
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Der Zeuge sagte aus, er ____ den Verdächtigen in der Nacht gesehen haben.",
        "options": ["will", "soll", "muss", "darf"],
        "correctAnswer": "will",
        "explanation": "'will' here is used to express a subjective claim by the subject themselves — the witness CLAIMS to have seen the suspect. This is a typical C1 usage of 'wollen' to report unverified first-person claims."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Es heisst, der Minister ____ schon seit Wochen von den Unregelmaessigkeiten gewusst haben.",
        "options": ["will", "soll", "muss", "kann"],
        "correctAnswer": "soll",
        "explanation": "'soll' is used here to convey a reported claim or rumour from a third party — i.e., 'it is said that'. This is the epistemic/reportative use of 'sollen' typical at C1."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Nach stundenlanger Suche ____ die Bergwacht die Vermissten endlich gefunden haben.",
        "options": ["duerfte", "sollte", "wollte", "musste"],
        "correctAnswer": "duerfte",
        "explanation": "'duerfte' in Konjunktiv II expresses a well-founded probability or assumption — similar to 'must have' but softer. It signals the speaker's reasoned conclusion without certainty."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "du ____ das Dokument eigentlich schon gestern abgegeben haben — warum hast du gewartet?",
        "options": ["solltest", "durftest", "wolltest", "konntest"],
        "correctAnswer": "solltest",
        "explanation": "'solltest' (Konjunktiv II of sollen) expresses an unfulfilled obligation in the past — you were supposed to (but didn't). This is a key C1 distinction from 'muessest'."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Das neue Medikament ____ angeblich innerhalb von Sekunden wirken.",
        "options": ["soll", "will", "muss", "mag"],
        "correctAnswer": "soll",
        "explanation": "'soll' combined with 'angeblich' (allegedly) reinforces the reportative function — a claim made by others that the speaker does not verify. This double marking is typical in formal/journalistic C1 German."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Sie ____ noch so jung sein — ihr Wissen ist beeindruckend.",
        "options": ["mag", "darf", "soll", "muss"],
        "correctAnswer": "mag",
        "explanation": "'mag' here expresses concession — 'however young she may be'. This concessive use of 'moegen' is a sophisticated C1 construction rarely seen at lower levels."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Waehlen Sie die grammatisch korrekte und bedeutungsgleiche Umformung: 'Es ist moeglich, dass er die Wahrheit sagt.'",
        "options": [
            "Er duerfte die Wahrheit sagen.",
            "Er soll die Wahrheit sagen.",
            "Er will die Wahrheit sagen.",
            "Er muss die Wahrheit sagen."
        ],
        "correctAnswer": "Er duerfte die Wahrheit sagen.",
        "explanation": "'duerfte' (Konjunktiv II of duerfen) is used to express epistemic possibility/probability. It is the closest paraphrase of 'Es ist moeglich, dass...' among the options."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Der Angeklagte ____ die Tat begangen haben — alle Beweise deuten darauf hin.",
        "options": ["muss", "soll", "will", "mag"],
        "correctAnswer": "muss",
        "explanation": "'muss' here expresses logical necessity or strong deduction — 'must have committed'. It reflects the speaker's certainty based on evidence, not an external obligation."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "In diesem Vertrag steht, dass Aenderungen ____ schriftlich beantragt werden.",
        "options": ["muessen", "koennen", "duerfen", "wollen"],
        "correctAnswer": "muessen",
        "explanation": "'muessen' here expresses a formal/legal obligation stated in writing — 'must be requested in writing'. 'duerfen' would only be correct in a permissive context."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Das ____ doch nicht dein Ernst sein! Du willst wirklich kuendigen?",
        "options": ["kann", "soll", "muss", "will"],
        "correctAnswer": "kann",
        "explanation": "'Das kann nicht dein Ernst sein' is a fixed idiomatic expression expressing disbelief — 'That can't be serious'. 'kann' here expresses the speaker's incredulity, not literal possibility."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Obwohl er ____ krank gewesen sein, erschien er punktlich zur Pruefung.",
        "options": ["mag", "soll", "muss", "will"],
        "correctAnswer": "mag",
        "explanation": "'mag ... sein' is used in concessive clauses — 'although he may have been ill'. This is an important C1 grammatical structure using the concessive function of 'moegen'."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Laut Presseberichten ____ der Konzern jahrelang Steuern hinterzogen haben.",
        "options": ["soll", "will", "muss", "darf"],
        "correctAnswer": "soll",
        "explanation": "'soll' paired with 'laut Presseberichten' (according to press reports) signals reported speech/unverified allegations — a hallmark of C1 journalistic and formal register."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Ich ____ mich geirrt haben — die Zahlen sehen anders aus als erwartet.",
        "options": ["koennte", "sollte", "wollte", "duerfte"],
        "correctAnswer": "koennte",
        "explanation": "'koennte' (Konjunktiv II of koennen) expresses epistemic possibility about a past event — 'I might have been wrong'. It conveys self-doubt without certainty, typical in academic or professional registers."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Die neue Regelung ____ ab dem naechsten Quartal in Kraft treten — so zumindest der Plan.",
        "options": ["soll", "muss", "will", "kann"],
        "correctAnswer": "soll",
        "explanation": "'soll' here expresses an intended plan or official schedule set by a third party (the authorities/planners), not the speaker. This 'planned intention' use is a key C1 function of 'sollen'."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Er ____ nicht gewusst haben, dass seine Aussage falsch war — das glaubt ihm aber niemand.",
        "options": ["will", "soll", "muss", "darf"],
        "correctAnswer": "will",
        "explanation": "'will' here captures a subjective self-claim — 'he claims not to have known'. Using 'wollen' to report what someone asserts about themselves (especially when doubted) is a sophisticated C1 pattern."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Du haettest das Problem frueher ansprechen ____. Jetzt ist es zu spaet.",
        "options": ["sollen", "koennen", "duerfen", "wollen"],
        "correctAnswer": "sollen",
        "explanation": "'haettest ... sollen' (Konjunktiv II Vergangenheit of sollen) expresses an unfulfilled obligation in retrospect — 'you should have'. This is a key irrealis modal construction at C1."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Das Paket ____ heute ankommen, aber laut Tracking ist es noch unterwegs.",
        "options": ["sollte", "wollte", "durfte", "mochte"],
        "correctAnswer": "sollte",
        "explanation": "'sollte' indicates an expected or planned event that didn't materialise — 'was supposed to arrive'. This temporal/expectational use of 'sollte' (Prateritum) is important at C1."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Es ist nicht klar, ob die Ausgaben ____ genehmigt worden sein.",
        "options": ["koennen", "sollen", "wollen", "muessen"],
        "correctAnswer": "koennen",
        "explanation": "'koennen' in this embedded clause expresses uncertainty about whether something is even possible/permitted — 'whether the expenditures could have been approved'. This is the epistemic use of 'koennen' in subordinate clauses."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Waehlen Sie die Aussage mit der staerksten Gewissheit des Sprechers: 'Der Taeter ____ die Stadt verlassen haben.'",
        "options": ["muss", "koennte", "duerfte", "mag"],
        "correctAnswer": "muss",
        "explanation": "Among epistemic modals, 'muss' expresses the highest degree of certainty — logical necessity. 'duerfte' and 'koennte' express probability and possibility respectively, while 'mag' signals mere acknowledgment."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Was auch immer andere ____ — ich bin von meiner Entscheidung ueberzeugt.",
        "options": ["sagen moegen", "sagen sollen", "sagen wollen", "sagen muessen"],
        "correctAnswer": "sagen moegen",
        "explanation": "'Was auch immer ... sagen moegen' is a formal concessive construction — 'whatever others may say'. This use of 'moegen' in concessive clauses with 'auch immer' is a hallmark C1 grammatical structure."
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
