import json

with open('app/src/main/assets/a2_02.json') as f:
    data = json.load(f)

print(f"Current: {len(data['questions'])}")

new_qs = [
    {
        "id": "a2_02_q081",
        "subjectId": "a2_02",
        "topicId": "a2_02",
        "topicName": "Perfekt",
        "sourceId": "manual",
        "originalId": "manual_081",
        "level": "B2",
        "type": "multiple_choice",
        "questionText": "Nachdem sie den ganzen Tag durch die Stadt ________ ________, ________ sie völlig erschöpft nach Hause ________ ________.",
        "options": [
            {"text": "gelaufen ist / ist / gekommen", "isCorrect": False},
            {"text": "gelaufen war / ist / gekommen", "isCorrect": True},
            {"text": "gelaufen ist / hat / gekommen", "isCorrect": False},
            {"text": "laufen ist / ist / gekommen", "isCorrect": False}
        ],
        "correctAnswer": "gelaufen war / ist / gekommen",
        "explanation": "After 'Nachdem,' the subordinate clause uses Plusquamperfekt (war gelaufen) because it describes an action completed before the main clause. The main clause uses Perfekt (ist gekommen) with sein because 'kommen' is a movement verb indicating a change of location.",
        "questionNumber": 81
    },
    {
        "id": "a2_02_q082",
        "subjectId": "a2_02",
        "topicId": "a2_02",
        "topicName": "Perfekt",
        "sourceId": "manual",
        "originalId": "manual_082",
        "level": "B2",
        "type": "multiple_choice",
        "questionText": "Er hat mir erzählt, dass er letztes Jahr nach Japan ________ ________.",
        "options": [
            {"text": "geflogen ist", "isCorrect": True},
            {"text": "geflogen hat", "isCorrect": False},
            {"text": "fliegen ist", "isCorrect": False},
            {"text": "geflogen gewesen ist", "isCorrect": False}
        ],
        "correctAnswer": "geflogen ist",
        "explanation": "'Fliegen' takes sein in Perfekt when indicating a change of location/direction (nach Japan). With manner of movement verbs, sein is used when the focus is on the movement itself rather than the action.",
        "questionNumber": 82
    },
    {
        "id": "a2_02_q083",
        "subjectId": "a2_02",
        "topicId": "a2_02",
        "topicName": "Perfekt",
        "sourceId": "manual",
        "originalId": "manual_083",
        "level": "B2",
        "type": "multiple_choice",
        "questionText": "________ du schon einmal davon ________ ________, dass man in der Schweiz auch Deutsch spricht?",
        "options": [
            {"text": "Hast / gehört", "isCorrect": True},
            {"text": "Bist / gehört", "isCorrect": False},
            {"text": "Hast / gehört worden", "isCorrect": False},
            {"text": "Warst / gehört", "isCorrect": False}
        ],
        "correctAnswer": "Hast / gehört",
        "explanation": "'Hören' takes haben in Perfekt (like all perception and communication verbs: hören, sehen, fühlen, verstehen, erzählen). 'Hast du gehört' is the correct Perfekt question form.",
        "questionNumber": 83
    },
    {
        "id": "a2_02_q084",
        "subjectId": "a2_02",
        "topicId": "a2_02",
        "topicName": "Perfekt",
        "sourceId": "manual",
        "originalId": "manual_084",
        "level": "B2",
        "type": "multiple_choice",
        "questionText": "Die Kinder ________ so laut ________ ________, dass die Nachbarn sich beschwert ________ ________.",
        "options": [
            {"text": "haben / gespielt / haben", "isCorrect": True},
            {"text": "sind / gespielt / haben", "isCorrect": False},
            {"text": "haben / gespielt / hatten", "isCorrect": False},
            {"text": "sind / gespielt / hatten", "isCorrect": False}
        ],
        "correctAnswer": "haben / gespielt / haben",
        "explanation": "'Spielen' takes haben in Perfekt (no change of location or state). The past perfect ('hatten beschwert') in the result clause would be possible but the simple Perfekt 'haben beschwert' is the standard correct answer here.",
        "questionNumber": 84
    },
    {
        "id": "a2_02_q085",
        "subjectId": "a2_02",
        "topicId": "a2_02",
        "topicName": "Perfekt",
        "sourceId": "manual",
        "originalId": "manual_085",
        "level": "B2",
        "type": "multiple_choice",
        "questionText": "Seitdem er diesen Kurs ________ ________, ________ er viel besser Deutsch ________ ________.",
        "options": [
            {"text": "besucht hat / hat / gesprochen", "isCorrect": False},
            {"text": "besucht hat / spricht", "isCorrect": True},
            {"text": "besucht hatte / hat / sprechen", "isCorrect": False},
            {"text": "besuchen hat / hat / gesprochen", "isCorrect": False}
        ],
        "correctAnswer": "besucht hat / spricht",
        "explanation": "Seitdem (since) can be followed by Perfekt for a completed action with ongoing result. The main clause uses Präsens (spricht) because the ongoing improved ability is described in the present. 'Sprechen' is a state verb that uses Präsens for current abilities.",
        "questionNumber": 85
    },
    {
        "id": "a2_02_q086",
        "subjectId": "a2_02",
        "topicId": "a2_02",
        "topicName": "Perfekt",
        "sourceId": "manual",
        "originalId": "manual_086",
        "level": "B2",
        "type": "multiple_choice",
        "questionText": "Ich glaube, ich ________ meinen Schlüssel zu Hause ________ ________.",
        "options": [
            {"text": "habe / liegen lassen", "isCorrect": False},
            {"text": "bin / liegen gelassen", "isCorrect": False},
            {"text": "habe / liegen lassen", "isCorrect": True},
            {"text": "habe / gelassen liegen", "isCorrect": False}
        ],
        "correctAnswer": "habe / liegen lassen",
        "explanation": "With 'lassen' meaning 'to leave (something somewhere),' the main verb 'lassen' takes haben and the second verb stays in infinitive. This is the Doppelinfinitiv construction: habe liegen lassen (not 'gelassen liegen'). The meaning is 'I left my key lying at home.'",
        "questionNumber": 86
    },
    {
        "id": "a2_02_q087",
        "subjectId": "a2_02",
        "topicId": "a2_02",
        "topicName": "Perfekt",
        "sourceId": "manual",
        "originalId": "manual_087",
        "level": "B2",
        "type": "multiple_choice",
        "questionText": "Warum ________ ihr eigentlich nicht zur Party ________ ________?",
        "options": [
            {"text": "seid / gekommen", "isCorrect": True},
            {"text": "habt / gekommen", "isCorrect": False},
            {"text": "seid / gekommen worden", "isCorrect": False},
            {"text": "habt / kommen", "isCorrect": False}
        ],
        "correctAnswer": "seid / gekommen",
        "explanation": "'Kommen' is a movement verb that takes sein in Perfekt. The correct Perfekt form is 'seid gekommen.' The auxiliary matches the subject: 'ihr' → 'seid.'",
        "questionNumber": 87
    },
    {
        "id": "a2_02_q088",
        "subjectId": "a2_02",
        "topicId": "a2_02",
        "topicName": "Perfekt",
        "sourceId": "manual",
        "originalId": "manual_088",
        "level": "B2",
        "type": "multiple_choice",
        "questionText": "Der Arzt sagte, dass das Fieber seit gestern ________ ________ ________.",
        "options": [
            {"text": "gestiegen ist", "isCorrect": True},
            {"text": "gestiegen hat", "isCorrect": False},
            {"text": "steigen ist", "isCorrect": False},
            {"text": "gestiegen gewesen ist", "isCorrect": False}
        ],
        "correctAnswer": "gestiegen ist",
        "explanation": "'Steigen' (to rise/climb) indicates a change of state and takes sein in Perfekt: 'ist gestiegen.' It expresses a Zustandsänderung (change of condition). The perfect participle of steigen is 'gestiegen.'",
        "questionNumber": 88
    },
    {
        "id": "a2_02_q089",
        "subjectId": "a2_02",
        "topicId": "a2_02",
        "topicName": "Perfekt",
        "sourceId": "manual",
        "originalId": "manual_089",
        "level": "B2",
        "type": "multiple_choice",
        "questionText": "________ Sie schon einmal Sushi ________ ________?",
        "options": [
            {"text": "Haben / gegessen", "isCorrect": True},
            {"text": "Sind / gegessen", "isCorrect": False},
            {"text": "Haben / gegessen worden", "isCorrect": False},
            {"text": "Sind / gegessen worden", "isCorrect": False}
        ],
        "correctAnswer": "Haben / gegessen",
        "explanation": "'Essen' is a verb of consumption that takes haben in Perfekt, not sein. The past participle is 'gegessen.' The formal 'Sie' form uses 'haben' as auxiliary: 'Haben Sie gegessen?'",
        "questionNumber": 89
    },
    {
        "id": "a2_02_q090",
        "subjectId": "a2_02",
        "topicId": "a2_02",
        "topicName": "Perfekt",
        "sourceId": "manual",
        "originalId": "manual_090",
        "level": "B2",
        "type": "multiple_choice",
        "questionText": "Nachdem der Zug Verspätung ________ ________, ________ wir den Anschlusszug nicht mehr ________ ________.",
        "options": [
            {"text": "gehabt hat / haben / erreicht", "isCorrect": False},
            {"text": "gehabt hatte / haben / erreicht", "isCorrect": False},
            {"text": "gehabt hat / hatten / erreichen", "isCorrect": False},
            {"text": "gehabt hatte / hatten / erreicht", "isCorrect": True}
        ],
        "correctAnswer": "gehabt hatte / hatten / erreicht",
        "explanation": "After 'Nachdem,' the subordinate clause uses Plusquamperfekt (hatte gehabt) because it refers to an action completed before another past event. The main clause also uses Plusquamperfekt (hatten erreicht) showing the missed connection was also in the past relative to the narrative time.",
        "questionNumber": 90
    },
    {
        "id": "a2_02_q091",
        "subjectId": "a2_02",
        "topicId": "a2_02",
        "topicName": "Perfekt",
        "sourceId": "manual",
        "originalId": "manual_091",
        "level": "B2",
        "type": "multiple_choice",
        "questionText": "Sie hat behauptet, dass sie den Brief schon vor einer Woche ________ ________ ________.",
        "options": [
            {"text": "abgeschickt hat", "isCorrect": True},
            {"text": "abgeschickt hätte", "isCorrect": False},
            {"text": "abschicken hat", "isCorrect": False},
            {"text": "abgeschickt worden ist", "isCorrect": False}
        ],
        "correctAnswer": "abgeschickt hat",
        "explanation": "In indirect speech (indirekte Rede), Konjunktiv II would normally be expected (hätte abgeschickt). However, when reporting a claim about a completed action without主观判断, Perfekt with haben can be used. The answer key indicates the non-subjunctive form for A2-B2 level teaching purposes.",
        "questionNumber": 91
    },
    {
        "id": "a2_02_q092",
        "subjectId": "a2_02",
        "topicId": "a2_02",
        "topicName": "Perfekt",
        "sourceId": "manual",
        "originalId": "manual_092",
        "level": "B2",
        "type": "multiple_choice",
        "questionText": "________ du das Buch, das ich dir empfohlen ________ ________, schon ________ ________?",
        "options": [
            {"text": "Hast / habe / gelesen", "isCorrect": True},
            {"text": "Hast / habe / gelesen gehabt", "isCorrect": False},
            {"text": "Bist / habe / gelesen", "isCorrect": False},
            {"text": "Hast / habe / zu lesen", "isCorrect": False}
        ],
        "correctAnswer": "Hast / habe / gelesen",
        "explanation": "Lesen takes haben in Perfekt. The relative clause 'das ich dir empfohlen habe' uses Perfekt to describe a completed recommendation. The main question 'Hast du gelesen?' is Perfekt with haben. The double perfect 'gelesen gehabt' is grammatically possible but not used in standard answers.",
        "questionNumber": 92
    },
    {
        "id": "a2_02_q093",
        "subjectId": "a2_02",
        "topicId": "a2_02",
        "topicName": "Perfekt",
        "sourceId": "manual",
        "originalId": "manual_093",
        "level": "B2",
        "type": "multiple_choice",
        "questionText": "Er ist sehr schnell ________ ________, weil er den Bus noch ________ ________ ________.",
        "options": [
            {"text": "gelaufen / hat / erwischen wollen", "isCorrect": True},
            {"text": "gelaufen / hat / erwischen gewollt", "isCorrect": False},
            {"text": "gelaufen / hat / wollen erwischen", "isCorrect": False},
            {"text": "gelaufen / hat / zu erwischen gewollt", "isCorrect": False}
        ],
        "correctAnswer": "gelaufen / hat / erwischen wollen",
        "explanation": "This is the Doppelinfinitiv construction with a modal verb. When a modal verb (wollen) appears with another verb in Perfekt, both infinitives go to the end: 'hat erwischen wollen' (not 'gewollt'). The verb 'erwischen' takes haben.",
        "questionNumber": 93
    },
    {
        "id": "a2_02_q094",
        "subjectId": "a2_02",
        "topicId": "a2_02",
        "topicName": "Perfekt",
        "sourceId": "manual",
        "originalId": "manual_094",
        "level": "B2",
        "type": "multiple_choice",
        "questionText": "Seit dem Unfall ________ sie nicht mehr Auto ________ ________.",
        "options": [
            {"text": "hat / gefahren", "isCorrect": True},
            {"text": "ist / gefahren", "isCorrect": False},
            {"text": "hat / fahren", "isCorrect": False},
            {"text": "ist / fahren", "isCorrect": False}
        ],
        "correctAnswer": "hat / gefahren",
        "explanation": "Fahren takes haben in Perfekt when no specific destination or direction is emphasized (Zustandsänderung without movement direction). When the focus is on the activity rather than the journey/destination, haben is used. Here, the emphasis is on the ability/skill, not movement.",
        "questionNumber": 94
    },
    {
        "id": "a2_02_q095",
        "subjectId": "a2_02",
        "topicId": "a2_02",
        "topicName": "Perfekt",
        "sourceId": "manual",
        "originalId": "manual_095",
        "level": "B2",
        "type": "multiple_choice",
        "questionText": "________ ihr schon ________ ________, dass die Prüfung auf nächste Woche ________ ________ ________?",
        "options": [
            {"text": "Habt / mitbekommen / verschoben worden ist", "isCorrect": True},
            {"text": "Seid / mitbekommen / verschoben hat", "isCorrect": False},
            {"text": "Habt / mitbekommen / verschoben worden hat", "isCorrect": False},
            {"text": "Habt / mitbekommen / verschoben worden ist", "isCorrect": False}
        ],
        "correctAnswer": "Habt / mitbekommen / verschoben worden ist",
        "explanation": "'Mitbekommen' takes haben in Perfekt. The passive construction 'verschoben worden ist' uses worden (not geworden) as the passive auxiliary in Perfekt. The subject 'die Prüfung' receives the action, so the passive is correct: 'wurde verschoben → ist verschoben worden.'",
        "questionNumber": 95
    },
    {
        "id": "a2_02_q096",
        "subjectId": "a2_02",
        "topicId": "a2_02",
        "topicName": "Perfekt",
        "sourceId": "manual",
        "originalId": "manual_096",
        "level": "B2",
        "type": "multiple_choice",
        "questionText": "Ich ________ noch nie in meinem Leben so etwas ________ ________!",
        "options": [
            {"text": "habe / erlebt", "isCorrect": True},
            {"text": "bin / erlebt", "isCorrect": False},
            {"text": "habe / erleben", "isCorrect": False},
            {"text": "habe / erlebt worden", "isCorrect": False}
        ],
        "correctAnswer": "habe / erlebt",
        "explanation": "'Erleben' (to experience/witness) is an action verb that takes haben in Perfekt. It does not indicate a change of location or state, so sein is not used. The past participle is 'erlebt.'",
        "questionNumber": 96
    },
    {
        "id": "a2_02_q097",
        "subjectId": "a2_02",
        "topicId": "a2_02",
        "topicName": "Perfekt",
        "sourceId": "manual",
        "originalId": "manual_097",
        "level": "B2",
        "type": "multiple_choice",
        "questionText": "Nachdem sie die Nachricht ________ ________ ________, ________ sie vor Freude ________ ________ ________.",
        "options": [
            {"text": "bekommen hat / hat / tanzen wollen", "isCorrect": False},
            {"text": "bekommen hatte / hat / tanzen gewollt", "isCorrect": False},
            {"text": "bekommen hat / hat / tanzen gewollt", "isCorrect": False},
            {"text": "bekommen hatte / hat / tanzen wollen", "isCorrect": True}
        ],
        "correctAnswer": "bekommen hatte / hat / tanzen wollen",
        "explanation": "After 'Nachdem,' Plusquamperfekt (hatte bekommen) shows the message was received before the main clause action. The main clause uses Perfekt with a modal verb: 'hat tanzen wollen.' With Doppelinfinitiv, the modal verb stays in infinitive form at the end.",
        "questionNumber": 97
    },
    {
        "id": "a2_02_q098",
        "subjectId": "a2_02",
        "topicId": "a2_02",
        "topicName": "Perfekt",
        "sourceId": "manual",
        "originalId": "manual_098",
        "level": "B2",
        "type": "multiple_choice",
        "questionText": "________ Sie schon einmal daran ________ ________, im Ausland zu arbeiten?",
        "options": [
            {"text": "Haben / gedacht", "isCorrect": True},
            {"text": "Sind / gedacht", "isCorrect": False},
            {"text": "Haben / denken", "isCorrect": False},
            {"text": "Sind / gedacht worden", "isCorrect": False}
        ],
        "correctAnswer": "Haben / gedacht",
        "explanation": "'Denken an + Akkusativ' (to think about) takes haben in Perfekt, not sein. The past participle is 'gedacht.' The construction 'an etwas denken' means to consider or think about something.",
        "questionNumber": 98
    },
    {
        "id": "a2_02_q099",
        "subjectId": "a2_02",
        "topicId": "a2_02",
        "topicName": "Perfekt",
        "sourceId": "manual",
        "originalId": "manual_099",
        "level": "B2",
        "type": "multiple_choice",
        "questionText": "Der Film, den wir gestern ________ ________ ________, ________ mir sehr gut ________ ________.",
        "options": [
            {"text": "gesehen haben / hat / gefallen", "isCorrect": False},
            {"text": "gesehen haben / ist / gefallen", "isCorrect": True},
            {"text": "gesehen haben / hat / gefallen haben", "isCorrect": False},
            {"text": "gesehen haben / hat / gefallen gewesen", "isCorrect": False}
        ],
        "correctAnswer": "gesehen haben / ist / gefallen",
        "explanation": "'Gefallen' (to like/be pleasing) is a Zustandsverb that takes sein in Perfekt because it describes a state/condition. The film caused a positive feeling ( Gefallen = pleasure received). The subject 'der Film' is what caused the Gefallen, and the person experiencing it is in the dative case.",
        "questionNumber": 99
    },
    {
        "id": "a2_02_q100",
        "subjectId": "a2_02",
        "topicId": "a2_02",
        "topicName": "Perfekt",
        "sourceId": "manual",
        "originalId": "manual_100",
        "level": "B2",
        "type": "multiple_choice",
        "questionText": "Nachdem er jahrelang im Ausland ________ ________ ________, ________ er fließend Deutsch ________ ________ ________.",
        "options": [
            {"text": "gearbeitet hat / hat / sprechen lernen", "isCorrect": False},
            {"text": "gearbeitet hatte / hat / sprechen gelernt", "isCorrect": False},
            {"text": "gearbeitet hat / hat / sprechen gelernt", "isCorrect": True},
            {"text": "gearbeitet hatte / hat / sprechen lernen", "isCorrect": False}
        ],
        "correctAnswer": "gearbeitet hat / hat / sprechen gelernt",
        "explanation": "'Nachdem' can be followed by Perfekt (not just Plusquamperfekt) when the events are recent or the temporal relationship is clear from context. 'Hat sprechen gelernt' is Perfekt with lernen as a modal-like verb (Zahlwort/lernen verbindet sich mit Modalverbregel). 'Sprechen gelernt' means 'learned to speak.'",
        "questionNumber": 100
    }
]

data['questions'].extend(new_qs)
print(f"Updated: {len(data['questions'])}")

with open('app/src/main/assets/a2_02.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Done!")
