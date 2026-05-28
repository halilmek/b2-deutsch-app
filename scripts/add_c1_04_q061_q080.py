import json

questions = [
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Was ist ein Funktionsverbgefüge?",
        "options": [
            "Ein Verb, das nur im Passiv verwendet wird",
            "Eine Verbindung aus einem bedeutungsschwachen Verb und einem Nomen, die gemeinsam eine Handlung ausdrücken",
            "Ein zusammengesetztes Substantiv aus zwei Verben",
            "Ein Modalverb mit Infinitiv"
        ],
        "correctAnswer": "Eine Verbindung aus einem bedeutungsschwachen Verb und einem Nomen, die gemeinsam eine Handlung ausdrücken",
        "explanation": "A Funktionsverbgefüge (support verb construction) is a combination of a semantically weak verb (e.g. 'bringen', 'kommen', 'stehen') and a noun (often with a preposition) that together express an action. The verb alone carries little meaning; the noun provides the core content."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welches der folgenden Beispiele ist ein Funktionsverbgefüge?",
        "options": [
            "Er schreibt einen Brief.",
            "Sie bringt das Kind zur Schule.",
            "Der Vorschlag kommt zur Abstimmung.",
            "Wir haben das Problem gelöst."
        ],
        "correctAnswer": "Der Vorschlag kommt zur Abstimmung.",
        "explanation": "'Zur Abstimmung kommen' is a Funktionsverbgefüge: the verb 'kommen' is semantically weak and the noun 'Abstimmung' carries the core meaning. It means 'to be voted on'. The other sentences use full-meaning verbs (schreiben, bringen, lösen)."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Ersetzen Sie das Vollverb durch ein Funktionsverbgefüge: Die Behörde entscheidet über den Antrag.",
        "options": [
            "Die Behörde macht eine Entscheidung über den Antrag.",
            "Die Behörde trifft eine Entscheidung über den Antrag.",
            "Die Behörde hat eine Entscheidung über den Antrag.",
            "Die Behörde gibt eine Entscheidung über den Antrag."
        ],
        "correctAnswer": "Die Behörde trifft eine Entscheidung über den Antrag.",
        "explanation": "'Eine Entscheidung treffen' is the standard Funktionsverbgefüge equivalent of 'entscheiden'. The verb 'treffen' is the support verb here."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welches Verb gehört zu dem Funktionsverbgefüge ____ Kritik?",
        "options": ["machen", "üben", "treffen", "nehmen"],
        "correctAnswer": "üben",
        "explanation": "'Kritik üben' (to criticize) is the established Funktionsverbgefüge. The verb 'üben' is the correct support verb here. 'Kritik machen' or 'Kritik treffen' are not standard collocations in formal German."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Was bedeutet das Funktionsverbgefüge 'in Frage stellen'?",
        "options": [
            "Eine Frage stellen",
            "Etwas anzweifeln oder infrage stellen",
            "Eine Antwort geben",
            "Etwas fragen wollen"
        ],
        "correctAnswer": "Etwas anzweifeln oder infrage stellen",
        "explanation": "'In Frage stellen' means to question or cast doubt on something. It is a fixed Funktionsverbgefüge where 'stellen' is the support verb and 'Frage' provides the meaning."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Ergänzen Sie das passende Funktionsverbgefüge: Das neue Gesetz tritt am 1. Januar ____.",
        "options": ["in Kraft", "in Frage", "in Betrieb", "in Anspruch"],
        "correctAnswer": "in Kraft",
        "explanation": "'In Kraft treten' means 'to come into force/effect' and is a standard Funktionsverbgefüge used for laws, regulations, and contracts."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welches Funktionsverbgefüge ersetzt das Verb 'berücksichtigen'?",
        "options": ["in Betracht ziehen", "in Angriff nehmen", "in Frage kommen", "unter Druck setzen"],
        "correctAnswer": "in Betracht ziehen",
        "explanation": "'In Betracht ziehen' is the Funktionsverbgefüge equivalent of 'berücksichtigen' (to consider/take into account). 'In Angriff nehmen' means to tackle something, 'in Frage kommen' means to be a possibility, and 'unter Druck setzen' means to put pressure on someone."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Die Firma nimmt die Produktion ____. - Ergänzen Sie das richtige Nomen.",
        "options": ["in Angriff", "in Kauf", "zur Kenntnis", "in Anspruch"],
        "correctAnswer": "in Angriff",
        "explanation": "'In Angriff nehmen' means 'to tackle / start working on something'. 'In Kauf nehmen' means to accept (a disadvantage), 'zur Kenntnis nehmen' means to take note of, 'in Anspruch nehmen' means to make use of."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Ersetzen Sie das Funktionsverbgefüge durch ein Vollverb: Der Zeuge steht unter Verdacht.",
        "options": [
            "Der Zeuge verdächtigt.",
            "Der Zeuge wird verdächtigt.",
            "Der Zeuge hat Verdacht.",
            "Der Zeuge ist verdächtig geworden."
        ],
        "correctAnswer": "Der Zeuge wird verdächtigt.",
        "explanation": "'Unter Verdacht stehen' is a Funktionsverbgefüge meaning 'to be suspected'. Its verb equivalent is the passive 'wird verdächtigt'."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welches der folgenden ist KEIN Funktionsverbgefüge?",
        "options": ["zur Verfügung stellen", "Hilfe leisten", "einen Spaziergang machen", "das Haus renovieren"],
        "correctAnswer": "das Haus renovieren",
        "explanation": "'Das Haus renovieren' uses a full-meaning verb ('renovieren') with a direct object. The others are all FVG: the noun carries the core meaning and the verb is semantically weak."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Was ist der bedeutungsähnliche Vollverb-Ausdruck für 'Einfluss nehmen auf'?",
        "options": ["einflüstern", "beeinflussen", "einwirken lassen", "Einfluss haben"],
        "correctAnswer": "beeinflussen",
        "explanation": "'Einfluss nehmen auf' is a Funktionsverbgefüge meaning 'to influence'. Its direct verb equivalent is 'beeinflussen'."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Die Mitarbeiter nehmen an der Schulung ____. - Welches Wort fehlt?",
        "options": ["teil", "Platz", "Abstand", "Rücksicht"],
        "correctAnswer": "teil",
        "explanation": "'Teilnehmen an' (to participate in) is a separable verb that functions similarly to a Funktionsverbgefüge. 'Platz nehmen' means to take a seat, 'Abstand nehmen' means to refrain from, 'Rücksicht nehmen' means to show consideration."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welches Funktionsverbgefüge passt in den Satz? Der Konflikt kam ____.",
        "options": ["zur Sprache", "in Kraft", "zum Einsatz", "unter Kontrolle"],
        "correctAnswer": "zur Sprache",
        "explanation": "'Zur Sprache kommen' means 'to be brought up / mentioned'. 'In Kraft kommen' is non-standard (correct is 'in Kraft treten'), 'zum Einsatz kommen' means to be deployed, 'unter Kontrolle kommen' = to come under control."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Ersetzen Sie durch ein Funktionsverbgefüge: Die Polizei kontrolliert den Bereich.",
        "options": [
            "Die Polizei nimmt den Bereich unter Kontrolle.",
            "Die Polizei bringt den Bereich unter Kontrolle.",
            "Die Polizei setzt den Bereich unter Kontrolle.",
            "Die Polizei stellt den Bereich unter Kontrolle."
        ],
        "correctAnswer": "Die Polizei bringt den Bereich unter Kontrolle.",
        "explanation": "'Unter Kontrolle bringen' is the standard Funktionsverbgefüge for actively gaining control over something. 'Nehmen', 'setzen', and 'stellen' do not form standard collocations with 'unter Kontrolle' in this active sense."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welche Aussage über Funktionsverbgefüge ist RICHTIG?",
        "options": [
            "Sie können immer durch ein einfaches Vollverb ohne Bedeutungsverlust ersetzt werden.",
            "Sie sind hauptsächlich in der gesprochenen Umgangssprache üblich.",
            "Sie ermöglichen oft feinere Bedeutungsnuancen, z. B. Aspekt oder Kausalität, die das Vollverb nicht ausdrückt.",
            "Das Funktionsverb trägt die Hauptbedeutung des Ausdrucks."
        ],
        "correctAnswer": "Sie ermöglichen oft feinere Bedeutungsnuancen, z. B. Aspekt oder Kausalität, die das Vollverb nicht ausdrückt.",
        "explanation": "FVG often convey nuances that a single verb cannot — for example, they can signal the beginning of an action (inchoative aspect: 'in Brand geraten' vs. 'brennen'), a causative meaning, or a more formal register."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Was ist der Unterschied zwischen 'zum Einsatz kommen' und 'zum Einsatz bringen'?",
        "options": [
            "Kein Unterschied; beide sind bedeutungsgleich.",
            "'kommen' drückt einen Zustand aus; 'bringen' drückt eine Bewegung aus.",
            "'kommen' ist intransitiv (kein Verursacher); 'bringen' ist transitiv (jemand verursacht den Einsatz).",
            "'bringen' wird nur im Passiv verwendet."
        ],
        "correctAnswer": "'kommen' ist intransitiv (kein Verursacher); 'bringen' ist transitiv (jemand verursacht den Einsatz).",
        "explanation": "Key distinction in FVG pairs: 'zum Einsatz kommen' = to be deployed (intransitive, no agent), while 'zum Einsatz bringen' = to deploy something (transitive, agent causes the action)."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welches Funktionsverbgefüge entspricht dem Vollverb 'beginnen' (inchoativer Aspekt)?",
        "options": ["in Brand stehen", "in Brand geraten", "in Brand setzen", "in Brand bleiben"],
        "correctAnswer": "in Brand geraten",
        "explanation": "'In Brand geraten' expresses the beginning of a state (inchoative aspect). 'In Brand stehen' = to be on fire (ongoing state), 'in Brand setzen' = to set on fire (causative), 'in Brand bleiben' is not a standard FVG."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Die Verhandlungsführer ____ das Abkommen ____ Abschluss. - Welche Kombination bildet ein korrektes Funktionsverbgefüge?",
        "options": ["brachten / zum", "kamen / zum", "setzten / in", "stellten / unter"],
        "correctAnswer": "brachten / zum",
        "explanation": "'Zum Abschluss bringen' means 'to conclude / bring to completion'. It is a transitive FVG where an agent brings something to its conclusion. 'Zum Abschluss kommen' would mean the conclusion happens on its own."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Bestimmen Sie die Funktion des Funktionsverbgefüges in diesem Satz: Das Projekt wurde in Angriff genommen. Welche grammatische Besonderheit liegt vor?",
        "options": [
            "Das Funktionsverbgefüge steht im Aktiv mit einem Modalverb.",
            "Das Funktionsverbgefüge ist ins Passiv gesetzt worden; das Nomen bleibt unverändert.",
            "Das Nomen 'Angriff' wird zum Verb 'angreifen' zurückgebildet.",
            "Das Funktionsverbgefüge kann nicht passiviert werden."
        ],
        "correctAnswer": "Das Funktionsverbgefüge ist ins Passiv gesetzt worden; das Nomen bleibt unverändert.",
        "explanation": "FVG can be passivized: 'in Angriff nehmen' (active) → 'in Angriff genommen werden' (passive). The noun ('Angriff') within the FVG remains unchanged — only the support verb is conjugated in the passive."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welcher Satz enthält ein Funktionsverbgefüge, das einen kausativen Aspekt ausdrückt?",
        "options": [
            "Die Reform steht zur Debatte.",
            "Die Moderatorin brachte das Thema zur Sprache.",
            "Der Angeklagte geriet unter Verdacht.",
            "Das Urteil kam zur Bekanntmachung."
        ],
        "correctAnswer": "Die Moderatorin brachte das Thema zur Sprache.",
        "explanation": "'Zur Sprache bringen' is a causative FVG: the moderator (an agent) actively causes the topic to be mentioned. Compare with 'zur Sprache kommen' (non-causative: the topic comes up on its own). The other options all use non-causative FVG."
    }
]


def add_qs(topic_json_path, questions):
    with open(topic_json_path, 'r', encoding='utf-8') as f:
        fdata = json.load(f)

    existing_ids = {q['id'] for q in fdata['questions'] if 'id' in q}

    added = 0
    for q in questions:
        q_id = q.get('id')
        if q_id in existing_ids:
            continue
        fdata['questions'].append(q)
        added += 1

    fdata['totalQuestions'] = len(fdata['questions'])

    with open(topic_json_path, 'w', encoding='utf-8') as f:
        json.dump(fdata, f, ensure_ascii=False, indent=2)

    print(f"Added {added} questions to {topic_json_path}")
    print(f"New total: {fdata['totalQuestions']}")


if __name__ == '__main__':
    add_qs('app/src/main/assets/c1_04.json', questions)
