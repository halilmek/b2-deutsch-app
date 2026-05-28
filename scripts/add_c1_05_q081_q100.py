import json

questions = [
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Ein Partizipialattribut ist eine ____ Form, die ein Nomen näher beschreibt.",
        "options": [
            "finite Verb",
            "infinitivische Verb",
            "konjugierte Verb",
            "Präpositional-"
        ],
        "correctAnswer": "infinitivische Verb",
        "explanation": "A participial attribute uses a non-finite verb form (Partizip I or Partizip II) to modify a noun, like 'der lesende Mann' or 'das gekochte Ei'."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welcher Satz enthält ein Partizipialattribut?",
        "options": [
            "Der Mann, der lacht, ist mein Bruder.",
            "Der lachende Mann ist mein Bruder.",
            "Der Mann lacht laut.",
            "Der Mann, welcher lacht, ist mein Bruder."
        ],
        "correctAnswer": "Der lachende Mann ist mein Bruder.",
        "explanation": "'Der lachende Mann' contains the present participle (Partizip I) 'lachende' as an attribute before the noun, replacing a relative clause."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Ersetzen Sie den Relativsatz durch ein Partizipialattribut: 'Der Antrag, der abgelehnt wurde, lag auf dem Tisch.'",
        "options": [
            "Der abgelehnte Antrag lag auf dem Tisch.",
            "Der ablehnende Antrag lag auf dem Tisch.",
            "Der Antrag abgelehnt lag auf dem Tisch.",
            "Der Antrag, abgelehnt, lag auf dem Tisch."
        ],
        "correctAnswer": "Der abgelehnte Antrag lag auf dem Tisch.",
        "explanation": "The passive relative clause 'der abgelehnt wurde' becomes the past participle (Partizip II) 'abgelehnte' as an attribute before the noun."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Partizip I (Präsenspartizip) wird gebildet aus ____ + ____.",
        "options": [
            "Infinitiv + -t",
            "Infinitiv + -nd",
            "Präteritumstamm + -end",
            "Partizip II + -er"
        ],
        "correctAnswer": "Infinitiv + -nd",
        "explanation": "Partizip I = Infinitive + -d (e.g., 'lachen' -> 'lachend', 'arbeiten' -> 'arbeitend'). It describes an ongoing action."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welches Partizipialattribut ist korrekt?",
        "options": [
            "der zu lesende Buch",
            "der lesende Buch",
            "das gelesene Buch",
            "das lesende Buch"
        ],
        "correctAnswer": "das gelesene Buch",
        "explanation": "'Das gelesene Buch' (the read book) uses Partizip II of 'lesen' with correct neuter article. 'Das lesende Buch' would mean 'the book that is reading' (active, unusual)."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Vervollständigen Sie: 'Die ____ Tür wurde repariert.'",
        "options": [
            "offenstehende",
            "offen gestandene",
            "offen tretende",
            "offen werdende"
        ],
        "correctAnswer": "offenstehende",
        "explanation": "'Offenstehende' = standing open. Partizip I of 'offenstehen' as an attribute: 'die offenstehende Tür' (the door that is standing open)."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Ein Partizipialattribut mit ____ kann eine aktive, gleichzeitige Handlung ausdrücken.",
        "options": [
            "Partizip I",
            "Partizip II",
            "Partizip Perfekt",
            "Präteritum"
        ],
        "correctAnswer": "Partizip I",
        "explanation": "Partizip I (e.g., 'der weinende Junge') describes an active action happening at the same time as the main clause."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Ersetzen Sie: 'Die Studentin, die die Prüfung bestanden hat, ist glücklich.' -> 'Die ____ Studentin ist glücklich.'",
        "options": [
            "die Prüfung bestehende",
            "die Prüfung bestandene",
            "die Prüfung bestehnde",
            "die Prüfung bestand habende"
        ],
        "correctAnswer": "die Prüfung bestehende",
        "explanation": "Active present participle 'bestehend' replaces the active relative clause with present perfect. In participle attributes, present participle is used for active actions regardless of tense."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welcher Relativsatz kann nicht direkt in ein Partizipialattribut umgewandelt werden (ohne Bedeutungsänderung)?",
        "options": [
            "Der Mann, der schläft.",
            "Das Buch, das mir gehört.",
            "Der Brief, der geschrieben wurde.",
            "Die Frau, die lacht."
        ],
        "correctAnswer": "Das Buch, das mir gehört.",
        "explanation": "Relative clauses with a dative object ('mir gehört') are hard to convert because participles can't easily incorporate dative objects. 'Das mir gehörende Buch' is possible but very formal/rare."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Partizipialattribute können auch ____ Attribute sein, die nach dem Nomen stehen.",
        "options": [
            "erweiterte",
            "verkürzte",
            "finite",
            "prädikative"
        ],
        "correctAnswer": "erweiterte",
        "explanation": "Erweiterte Partizipialattribute (extended participial attributes) come after the noun with additional phrases, e.g., 'der von seinem Freund begleitete Mann'."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Vervollständigen Sie das erweiterte Partizipialattribut: 'Die ____ Lösung wurde akzeptiert.'",
        "options": [
            "von allen Beteiligten vorgeschlagene",
            "vorgeschlagene von allen Beteiligten",
            "alle Beteiligten vorgeschlagene",
            "die von allen Beteiligten vorgeschlagene"
        ],
        "correctAnswer": "von allen Beteiligten vorgeschlagene",
        "explanation": "In an extended participial attribute, the additional elements (here 'von allen Beteiligten') come before the past participle, all positioned before the noun."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welche Form ist ein Partizip II als Attribut?",
        "options": [
            "der tanzende Mann",
            "der getanzte Walzer",
            "der zu tanzende Walzer",
            "der Walzer tanzend"
        ],
        "correctAnswer": "der getanzte Walzer",
        "explanation": "'Getanzte' is Partizip II of 'tanzen' used as an attribute (passive meaning: the waltz that was danced)."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Ein Partizipialattribut mit Partizip I hat meist eine ____ Bedeutung.",
        "options": [
            "passive",
            "aktive",
            "futurische",
            "modale"
        ],
        "correctAnswer": "aktive",
        "explanation": "Partizip I attributes (e.g., 'der schreibende Student') have active meaning: the student is writing (actively doing the action)."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Ersetzen Sie das Partizipialattribut durch einen Relativsatz: 'Das von mir gelesene Buch war spannend.'",
        "options": [
            "Das Buch, das von mir gelesen ist, war spannend.",
            "Das Buch, das ich gelesen habe, war spannend.",
            "Das Buch, das mir gelesen wurde, war spannend.",
            "Das Buch, gelesen von mir, war spannend."
        ],
        "correctAnswer": "Das Buch, das ich gelesen habe, war spannend.",
        "explanation": "The participial attribute 'von mir gelesene' corresponds to the active relative clause 'das ich gelesen habe' (not passive)."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welches Partizipialattribut ist falsch?",
        "options": [
            "der bei der Arbeit schlafende Mann",
            "der seit Tagen nicht geschlafene Mann",
            "der auf dem Sofa schlafende Mann",
            "der tief schlafende Mann"
        ],
        "correctAnswer": "der seit Tagen nicht geschlafene Mann",
        "explanation": "Partizip II 'geschlafene' would mean 'the man who has been slept on' (passive nonsense). Correct form must use active construction or Partizip I: 'der seit Tagen nicht geschlafen habende Mann' (rare) or simply restructure."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Ein erweitertes Partizipialattribut steht normalerweise ____.",
        "options": [
            "vor dem Nomen",
            "nach dem Nomen",
            "hinter dem Verb",
            "am Satzende"
        ],
        "correctAnswer": "vor dem Nomen",
        "explanation": "Extended participial attributes (with additional words like adverbs or prepositional phrases) are placed before the noun in German: 'Der auf dem Tisch liegende Schlüssel'."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Vervollständigen Sie: 'Das ____ Problem wurde gelöst.'",
        "options": [
            "seit Monaten diskutierende",
            "seit Monaten diskutierte",
            "diskutierende seit Monaten",
            "seit Monaten zu diskutierende"
        ],
        "correctAnswer": "seit Monaten diskutierte",
        "explanation": "Passive meaning = 'the problem discussed for months'. Partizip II 'diskutierte' + extended element 'seit Monaten' before the noun."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Was drückt das Attribut 'der zu lösende' aus?",
        "options": [
            "aktiv und abgeschlossen",
            "passiv und zukünftig / Notwendigkeit",
            "aktiv und gleichzeitig",
            "vergangen und passiv"
        ],
        "correctAnswer": "passiv und zukünftig / Notwendigkeit",
        "explanation": "'Der zu lösende Konflikt' = the conflict that needs to be solved / is to be solved. It expresses passive future or necessity (Gerundivum)."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welcher Satz ist stilistisch am formalsten und nominalsten?",
        "options": [
            "Der Brief, der vom Chef unterschrieben wurde, ist wichtig.",
            "Der vom Chef unterschriebene Brief ist wichtig.",
            "Der Brief wurde vom Chef unterschrieben und ist wichtig.",
            "Der Chef unterschrieb den Brief, der wichtig ist."
        ],
        "correctAnswer": "Der vom Chef unterschriebene Brief ist wichtig.",
        "explanation": "The extended participial attribute 'Der vom Chef unterschriebene Brief' is the most nominal and formal style, typical of written German."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Vom Relativsatz zum Partizipialattribut: 'Die Touristen, die am Strand entlangspazieren, genießen das Wetter.' -> 'Die ____ Touristen genießen das Wetter.'",
        "options": [
            "am Strand entlangspazierenden",
            "am Strand entlangspazierte",
            "am Strand entlangspazierte",
            "am Strand entlangzuspazierenden"
        ],
        "correctAnswer": "am Strand entlangspazierenden",
        "explanation": "Active present tense relative clause -> Partizip I 'entlangspazierenden' with extended element 'am Strand' before the noun. Correct strong declension plural."
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
    add_qs('app/src/main/assets/c1_05.json', questions, 'c1_05')
