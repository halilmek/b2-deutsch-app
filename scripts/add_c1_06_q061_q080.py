import json

questions = [
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welche Bedeutung hat 'koennen' in folgendem Satz: 'Er kann sehr gut Klavier spielen.'?",
        "options": ["Erlaubnis", "Moeglichkeit", "Faehigkeit", "Vermutung"],
        "correctAnswer": "Faehigkeit",
        "explanation": "Here 'koennen' expresses an ability or skill (Faeahigkeit) — he is able to play the piano well."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Ergaenzen Sie das passende Modalverb: 'Es ____ morgen regnen, aber ich bin nicht sicher.'",
        "options": ["muss", "kann", "soll", "mag"],
        "correctAnswer": "kann",
        "explanation": "'Kann' expresses possibility (it might rain tomorrow). 'Muss' would be too certain, 'soll' means hearsay, 'mag' is old-fashioned for possibility."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welches Modalverb druckt in der Vergangenheit eine fast sichere Vermutung aus?",
        "options": ["konnte", "musste", "durfte", "wollte"],
        "correctAnswer": "musste",
        "explanation": "Past tense 'musste' + infinitive can express a strong assumption: 'Er musste schon zu Hause sein' = 'He must already be at home' (logical deduction)."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "'Sie soll eine neue Stelle bekommen haben.' – Was druckt dieser Satz aus?",
        "options": [
            "Eine sichere Tatsache",
            "Eine Faeahigkeit",
            "Eine Aussage von anderer Person (Gerruecht)",
            "Eine Erlaubnis"
        ],
        "correctAnswer": "Eine Aussage von anderer Person (Gerruecht)",
        "explanation": "'Sollen' in indirect speech or hearsay context reports what others say: 'She is said to have gotten a new job.'"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Vervollstaendigen Sie: 'du ____ punktlich kommen, das ist wichtig!'",
        "options": ["kannst", "magst", "sollst", "darfst"],
        "correctAnswer": "sollst",
        "explanation": "'Sollen' expresses a strong request or obligation from someone else: 'You are supposed to / should come on time.'"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welches Modalverb kann eine hoefliche Frage einleiten?",
        "options": ["muessen", "duerfen", "moegen (Konjunktiv: moechte)", "wollen"],
        "correctAnswer": "moegen (Konjunktiv: moechte)",
        "explanation": "Konjunktiv II 'moechte' (would like to) is used for polite requests: 'Ich moechte bitte zahlen.' 'DuERfen' (Konj. II) is also possible but less common."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Ergaenzen Sie: 'Nach dem Unfall ____ er drei Wochen im Krankenhaus bleiben.'",
        "options": ["durfte", "musste", "wollte", "sollte"],
        "correctAnswer": "musste",
        "explanation": "'Musste' expresses necessity/obligation due to circumstances: he had to stay in hospital (no choice)."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welche Bedeutung hat 'duerfen' im Satz 'Das darf nicht wahr sein!'?",
        "options": ["Erlaubnis", "Moeglichkeit (Ausruf der Unglaeubigkeit)", "Vermutung", "Faeahigkeit"],
        "correctAnswer": "Moeglichkeit (Ausruf der Unglaeubigkeit)",
        "explanation": "In exclamations like 'Das darf nicht wahr sein!' (That can't be true!), 'duerfen' expresses impossibility or disbelief, not permission."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Formen Sie um: 'Es ist moeglich, dass er den Zug verpasst hat.' -> 'Er ____ den Zug verpasst haben.'",
        "options": ["kann", "mag", "duerfte", "Alle drei sind moeglich, aber mit leichten Nuancen."],
        "correctAnswer": "Alle drei sind moeglich, aber mit leichten Nuancen.",
        "explanation": "'Er kann/mag/duerfte den Zug verpasst haben' all express possibility. 'Kann' neutral, 'mag' weaker/old-fashioned, 'duerfte' stronger probability."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Modalverben koennen auch ____ Bedeutungen haben, die nicht direkt mit Erlaubnis, Faeahigkeit oder Notwendigkeit zu tun haben.",
        "options": ["subjektive", "objektive", "tempus", "reflexive"],
        "correctAnswer": "subjektive",
        "explanation": "Subjective use of modal verbs expresses the speaker's opinion, assumption, or evaluation (e.g., 'Er muss krank sein' = assumption, not obligation)."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welcher Satz zeigt den subjektiven Gebrauch von 'muessen'?",
        "options": [
            "Ich muss nach Hause gehen.",
            "Er muss Zahnarzt sein, bei seinen Zahnschmerzen.",
            "du musst die Hausaufgaben machen.",
            "Wir müssen frueh aufstehen."
        ],
        "correctAnswer": "Er muss Zahnarzt sein, bei seinen Zahnschmerzen.",
        "explanation": "Subjective 'müssen' = strong assumption (He must be a dentist given his toothache). The others are objective necessity."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Vervollstaendigen Sie: 'Die Nachbarn ____ gestern Abend laut Musik gehoert haben; ich bin mir fast sicher.'",
        "options": ["koennen", "muessen", "duerfen", "wollen"],
        "correctAnswer": "muessen",
        "explanation": "Subjective 'müssen' in past: 'müssen + past infinitive' = strong assumption: 'The neighbors must have played loud music yesterday.'"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Was druckt 'wollen' im subjektiven Gebrauch aus (z.B. 'Das will nichts heissen')?",
        "options": ["Wunsch", "Faeahigkeit", "Behauptung mit Zweifel des Sprechers", "Erlaubnis"],
        "correctAnswer": "Behauptung mit Zweifel des Sprechers",
        "explanation": "Subjective 'wollen' can express that someone claims something, often with the speaker doubting it: 'Er will das gesehen haben' = He claims to have seen it (but maybe not true)."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Ergaenzen Sie: '____ ich Ihnen helfen?'",
        "options": ["Muss", "Will", "Darf", "Soll"],
        "correctAnswer": "Darf",
        "explanation": "'Darf ich helfen?' is a polite offer (May I help?). 'Darf' expresses permission-seeking, common in service contexts."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welche Ersatzform fuer Modalverben im Passiv ist korrekt? 'Das Problem kann geloest werden.' ->",
        "options": [
            "Das Problem laesst sich loesen.",
            "Das Problem ist zu loesen.",
            "Das Problem hat sich geloest.",
            "Das Problem geht zu loesen."
        ],
        "correctAnswer": "Das Problem laesst sich loesen.",
        "explanation": "'sich lassen + Infinitiv' replaces 'koennen + Passiv' to express possibility: 'The problem can be solved.'"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Druckt 'Er muss nicht kommen' oder 'Er braucht nicht zu kommen' aus, dass ____?",
        "options": [
            "er nicht kommen darf",
            "er nicht kommen soll",
            "keine Notwendigkeit besteht",
            "er nicht kommen moechte"
        ],
        "correctAnswer": "keine Notwendigkeit besteht",
        "explanation": "'nicht muessen' means 'not necessary / don't have to' (absence of obligation), NOT 'must not' (which is 'nicht duerfen')."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Vervollstaendigen Sie: 'Das ____ doch nicht wahr sein!' (Ausdruck der Unglaeubigkeit)",
        "options": [
            "kann",
            "darf",
            "mag",
            "Alle drei sind in bestimmten Kontexten moeglich."
        ],
        "correctAnswer": "Alle drei sind in bestimmten Kontexten moeglich.",
        "explanation": "'Das kann/darf/mag nicht wahr sein!' All are possible in exclamations of disbelief, with regional or stylistic differences. 'Darf' and 'kann' are most common."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welches Modalverb passt: 'Ich ____ nach Hause, aber ich bin noch mue_de.' (fehlende Notwendigkeit)",
        "options": ["muss nicht", "brauche nicht", "soll nicht", "kann nicht"],
        "correctAnswer": "brauche nicht",
        "explanation": "In standard German, 'nicht brauchen' + zu + infinitive replaces 'nicht muessen': 'Ich brauche nicht nach Hause zu gehen.' 'Muss nicht' is also possible but less idiomatic in this position."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Erkennen Sie die subjektive Bedeutung: 'Sie will ihn gesehen haben, aber ich glaube ihr nicht.'",
        "options": [
            "Sie hat ihn wirklich gesehen.",
            "Sie behauptet es, der Sprecher zweifelt.",
            "Sie hatte die Faeahigkeit zu sehen.",
            "Sie hatte die Erlaubnis zu sehen."
        ],
        "correctAnswer": "Sie behauptet es, der Sprecher zweifelt.",
        "explanation": "Subjective 'wollen' here reports her claim, and the speaker explicitly doubts it ('ich glaube ihr nicht')."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welcher Satz mit 'moegen' ist heute noch ueblich in der geschriebenen Standardsprache?",
        "options": [
            "Magst du Kaffee?",
            "Er mag krank sein.",
            "Ich mag nach Hause gehen.",
            "Das mag sein, aber es ist teuer."
        ],
        "correctAnswer": "Das mag sein, aber es ist teuer.",
        "explanation": "'Das mag sein' (That may be) is a common concessive phrase. 'Magst du Kaffee?' is colloquial for 'Do you like coffee?', originally modal use is fading."
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
