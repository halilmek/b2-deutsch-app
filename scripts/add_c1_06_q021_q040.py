import json

questions = [
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welche Bedeutung hat 'müssen' im Satz: 'Das muss stimmen.'?",
        "options": [
            "Eine objektive Notwendigkeit",
            "Eine subjektive Annahme oder Vermutung",
            "Eine Erlaubnis",
            "Eine Aufforderung"
        ],
        "correctAnswer": "Eine subjektive Annahme oder Vermutung",
        "explanation": "At C1 level, 'müssen' can express epistemic modality — a logical conclusion or assumption based on evidence ('That must be true'), distinct from its deontic meaning of obligation."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welches Modalverb drückt im Konjunktiv II eine höfliche Bitte oder Vorschlag aus?",
        "options": ["müsste", "dürfte", "könnte", "sollte"],
        "correctAnswer": "könnte",
        "explanation": "'Könnte' (Konjunktiv II of 'können') is commonly used for polite requests or suggestions ('Könntest du mir helfen?'), softening the utterance compared to the indicative 'kann'."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Ergaenzen Sie korrekt: 'Er ____ gestern kommen, aber er hatte keine Zeit.'",
        "options": ["wollte", "wollte haben", "hat wollen", "wollte gekommen sein"],
        "correctAnswer": "wollte",
        "explanation": "In past tense contexts with modal verbs, the Prateritum form ('wollte') is standard when the main verb is omitted or implied. The double infinitive construction is only required in perfect tenses with a complementary infinitive."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Was bedeutet 'duerfte' im Satz: 'Das duerfte schwierig werden.'?",
        "options": [
            "Es ist erlaubt, schwierig zu werden.",
            "Es wird wahrscheinlich schwierig.",
            "Es muss schwierig werden.",
            "Es soll schwierig werden."
        ],
        "correctAnswer": "Es wird wahrscheinlich schwierig.",
        "explanation": "'Dürfte' (Konjunktiv II of 'dürfen') expresses epistemic probability or likelihood at C1 level, not permission. It functions as a hedging device to soften assertions."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welcher Satz verwendet 'sollen' korrekt, um eine fremde Aufforderung wiederzugeben?",
        "options": [
            "du sollst sofort kommen!",
            "Er soll reich sein.",
            "Sie sollen das Formular ausfuellen, hat der Chef gesagt.",
            "Ich soll morgen arbeiten."
        ],
        "correctAnswer": "Sie sollen das Formular ausfuellen, hat der Chef gesagt.",
        "explanation": "'Sollen' is used to report commands or requests from a third party ('He said you should fill out the form'). This indirect imperative function is a key C1 usage distinct from personal obligation."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Transformieren Sie in die Perfektform: 'Er kann das Problem loesen.'",
        "options": [
            "Er hat das Problem loesen koennen.",
            "Er hat das Problem geloest koennen.",
            "Er hat das Problem koennen loesen.",
            "Er ist das Problem loesen gekonnt."
        ],
        "correctAnswer": "Er hat das Problem loesen koennen.",
        "explanation": "In perfect tenses, modal verbs use the double infinitive construction: auxiliary 'haben' + main verb infinitive + modal infinitive ('loesen koennen'). The modal verb does not take a past participle form here."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welche Nuance unterscheidet 'müssen' von 'sollen' im Satz: 'du ____ das nicht tun.'?",
        "options": [
            "'Müssen' druckt eine externe Regel aus; 'sollen' eine moralische Empfehlung.",
            "'Müssen' druckt eine zwingende Notwendigkeit aus; 'sollen' eine Erwartung oder Aufforderung von aussen.",
            "'Sollen' ist staerker als 'müssen'.",
            "Es gibt keinen Unterschied; beide sind austauschbar."
        ],
        "correctAnswer": "'Müssen' druckt eine zwingende Notwendigkeit aus; 'sollen' eine Erwartung oder Aufforderung von aussen.",
        "explanation": "At C1, learners distinguish deontic nuances: 'müssen' expresses objective compulsion ('must'), while 'sollen' conveys external expectation or reported instruction ('ought to / is supposed to')."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Wie lautet die korrekte Passivkonstruktion mit Modalverb: 'Man muss die Unterlagen einreichen.'?",
        "options": [
            "Die Unterlagen müssen eingereicht werden.",
            "Die Unterlagen müssen eingereicht worden sein.",
            "Die Unterlagen müssen einreichen werden.",
            "Die Unterlagen werden eingereicht müssen."
        ],
        "correctAnswer": "Die Unterlagen müssen eingereicht werden.",
        "explanation": "In passive constructions with modal verbs, the structure is: modal verb + past participle + 'werden'. The modal remains in its finite position, and 'werden' carries the passive meaning in infinitive form."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welcher Satz druckt eine unrealistische Vergangenheit mit Modalverb aus?",
        "options": [
            "Er hätte kommen sollen.",
            "Er sollte kommen.",
            "Er muss gekommen sein.",
            "Er konnte kommen."
        ],
        "correctAnswer": "Er hätte kommen sollen.",
        "explanation": "The construction 'hätte + infinitive + sollen' expresses a past obligation that was not fulfilled ('He should have come'). This counterfactual modal perfect is a sophisticated C1 structure for expressing regret or criticism."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Was bedeutet 'moegen' im Konjunktiv II ('moechte') im Vergleich zum Indikativ?",
        "options": [
            "'Möchte' druckt einen starken Wunsch aus; 'mag' eine Tatsache.",
            "'Möchte' ist eine hoefliche Form des Wollens; 'mag' beschreibt eine Vorliebe oder Möglichkeit.",
            "'Möchte' ist veraltet; 'mag' ist standardsprachlich.",
            "Beide Formen sind synonym und austauschbar."
        ],
        "correctAnswer": "'Möchte' ist eine hoefliche Form des Wollens; 'mag' beschreibt eine Vorliebe oder Möglichkeit.",
        "explanation": "'Möchte' (Konjunktiv II of 'mögen') functions as a polite substitute for 'wollen' ('I would like'), while 'mag' expresses preference ('I like') or epistemic possibility ('It may be'). This distinction is crucial for pragmatic competence at C1."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Ergaenzen Sie korrekt: 'Sie ____ das Buch gelesen haben, denn sie zitiert daraus.'",
        "options": ["muss", "muesste", "haette", "soll"],
        "correctAnswer": "muss",
        "explanation": "'Muss' + perfect infinitive ('gelesen haben') expresses a logical conclusion about a past event ('She must have read the book'). This epistemic use of 'müssen' with modal perfect is a hallmark of C1 proficiency."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welcher Satz verwendet 'koennen' korrekt, um eine theoretische Möglichkeit auszudruecken?",
        "options": [
            "Er kann sehr nett sein, wenn er will.",
            "Er kann schwimmen.",
            "Er kann heute nicht kommen.",
            "Kannst du mir helfen?"
        ],
        "correctAnswer": "Er kann sehr nett sein, wenn er will.",
        "explanation": "Here, 'kann' expresses epistemic possibility ('He can be nice' = 'It is possible for him to be nice'), distinct from ability ('Er kann schwimmen') or permission. Recognizing these semantic layers is essential at C1."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Wie lautet die indirekte Rede mit Modalverb: 'Ich muss gehen.' -> 'Er sagte, er ____'.",
        "options": ["er muesse gehen", "er muesse gegangen sein", "er haette gehen muessen", "er sollte gehen"],
        "correctAnswer": "er muesse gehen",
        "explanation": "In indirect speech, modal verbs take Konjunktiv I form ('müsse') to mark reported speech while preserving the original modal meaning. This maintains distance and neutrality, a key journalistic convention at C1."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welche Konstruktion ist korrekt für die Verneinung von 'brauchen' als Modalverb?",
        "options": [
            "du brauchst nicht zu kommen.",
            "du brauchst nicht kommen.",
            "du brauchst zu nicht kommen.",
            "du brauchst kommen nicht."
        ],
        "correctAnswer": "du brauchst nicht zu kommen.",
        "explanation": "When 'brauchen' functions as a modal-like verb (only in negative contexts), it requires 'zu + infinitive'. This semi-modal behavior is a frequent C1 exam point, distinguishing it from true modals that omit 'zu'."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welcher Satz demonstriert die korrekte Verwendung von 'wollen' im Konjunktiv II für eine hypothetische Aussage?",
        "options": [
            "Wenn ich mehr Zeit haette, wollte ich reisen.",
            "Wenn ich mehr Zeit haette, wuerde ich reisen wollen.",
            "Wenn ich mehr Zeit haette, wollte ich gereist sein.",
            "Wenn ich mehr Zeit haette, will ich reisen."
        ],
        "correctAnswer": "Wenn ich mehr Zeit haette, wuerde ich reisen wollen.",
        "explanation": "In hypothetical conditional clauses, 'wollen' typically appears in the 'wuerde + infinitive + wollen' construction rather than the archaic Konjunktiv II 'wollte'. This reflects modern C1 usage preferences for clarity and naturalness."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Wie unterscheidet sich die Bedeutung von 'sollen' in diesen Saetzen? (1) 'Du sollst nicht toeten.' (2) 'Er soll reich sein.'",
        "options": [
            "(1) moralisches Gebot; (2) Geruecht oder fremde Behauptung",
            "(1) persoenliche Meinung; (2) faktische Aussage",
            "(1) Erlaubnis; (2) Verbot",
            "Beide Saetze haben dieselbe Bedeutung."
        ],
        "correctAnswer": "(1) moralisches Gebot; (2) Geruecht oder fremde Behauptung",
        "explanation": "'Sollen' has multiple C1-level functions: (1) deontic obligation (moral/legal command), (2) epistemic hearsay ('is said to be'). Context determines interpretation, and mastering this polysemy is essential for advanced comprehension."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welche Modalverbkonstruktion ist im folgenden Kontext am angemessensten? 'Angesichts der Beweislage ____ der Angeklagte schuldig ____.'",
        "options": [
            "muss ... sein",
            "duerfte ... gewesen sein",
            "kann ... gewesen sein",
            "soll ... sein"
        ],
        "correctAnswer": "muss ... sein",
        "explanation": "'Muss ... sein' expresses a strong logical conclusion based on evidence ('must be guilty'), appropriate for legal or argumentative contexts. The epistemic use of 'müssen' with present infinitive conveys high certainty about a present state."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Identifizieren Sie den Satz mit fehlerhafter Modalverb-Perfekt-Konstruktion.",
        "options": [
            "Sie hat nicht kommen koennen.",
            "Er hat es machen muessen.",
            "Wir haben gehen wollen.",
            "Ich habe das Buch lesen gemocht."
        ],
        "correctAnswer": "Ich habe das Buch lesen gemocht.",
        "explanation": "While 'mögen' can form the perfect with double infinitive ('hat mögen'), in practice 'hat ... gemocht' is used for preference ('liked'), and the double infinitive is rare/awkward. More natural: 'Ich habe das Buch gern gelesen'. This tests awareness of modal verb irregularities in perfect tenses."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welche Strategie zeigt fortgeschrittene Kompetenz im Einsatz von Modalverben auf C1-Niveau?",
        "options": [
            "Ausschliessliche Verwendung des Indikativs fuer maximale Klarheit.",
            "Gezielte Wahl zwischen epistemischer und deontischer Bedeutung je nach Kontext, Register und Aussageabsicht.",
            "Vermeidung von Konjunktiv-II-Formen, um Fehler zu minimieren.",
            "Nutzung nur der Grundbedeutungen von Modalverben."
        ],
        "correctAnswer": "Gezielte Wahl zwischen epistemischer und deontischer Bedeutung je nach Kontext, Register und Aussageabsicht.",
        "explanation": "C1 proficiency includes pragmatic awareness: selecting modal verbs not just for grammatical correctness but for nuanced meaning — hedging ('dürfte'), asserting ('muss'), reporting ('soll'), or politeness ('könnte'). This strategic flexibility is assessed in advanced exams."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welcher Satz verwendet 'moegen' korrekt im Sinne von 'vielleicht' (epistemische Möglichkeit)?",
        "options": [
            "Ich mag Schokolade.",
            "Das mag sein, aber ich bin anderer Meinung.",
            "Er mag kommen, wenn er will.",
            "Sie moechte bitte leise sein."
        ],
        "correctAnswer": "Das mag sein, aber ich bin anderer Meinung.",
        "explanation": "'Das mag sein' is a fixed C1 expression where 'mögen' concedes epistemic possibility ('That may be true'), often used to acknowledge an opposing view before presenting a counterargument. This pragmatic function is distinct from expressing preference or desire."
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
