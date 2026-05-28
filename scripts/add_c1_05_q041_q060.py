import json

questions = [
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Verwandeln Sie den Relativsatz in ein Partizipialattribut: 'Die Firma stellt Mitarbeiter ein, die fliessend Deutsch sprechen.' -> 'Die Firma stellt ____ Mitarbeiter ein.'",
        "options": [
            "fliessend Deutsch sprechenden",
            "fliessend Deutsch gesprochene",
            "fliessend Deutsch sprechende",
            "Deutsch fliessend gesprochenen"
        ],
        "correctAnswer": "fliessend Deutsch sprechende",
        "explanation": "The action is active and simultaneous, requiring Partizip I ('sprechend'). Since 'Mitarbeiter' is plural accusative with no article following the verb 'einstellen', the adjective/participle ending must be '-e'."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Ergaenzen Sie das Partizipialattribut (Passiv/Vorzeitigkeit): 'Das Gesetz, das im vergangenen Jahr ____ wurde, trat heute in Kraft.' -> 'Das im vergangenen Jahr ____ Gesetz trat heute in Kraft.'",
        "options": [
            "beschlossene",
            "beschliesend",
            "beschlossener",
            "zu beschliessende"
        ],
        "correctAnswer": "beschlossene",
        "explanation": "The relative clause is passive and completed in the past (vorzeitig). This requires Partizip II ('beschlossen'). It modifies 'Gesetz' (neuter singular nominative with the definite article 'das'), so the weak adjective ending is '-e'."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Waehlen Sie die richtige Form des erweiterten Partizipialattributs: Die ____ Massnahmen fuehrten schliesslich zum Erfolg.",
        "options": [
            "von der Regierung getroffenen",
            "von der Regierung treffenden",
            "durch die Regierung getroffen",
            "von die Regierung getroffene"
        ],
        "correctAnswer": "von der Regierung getroffenen",
        "explanation": "The relative clause equivalent would be 'Die Massnahmen, die von der Regierung getroffen wurden...'. Passive completion requires Partizip II ('getroffen'). Preposition 'von' requires dative ('der Regierung'). Plural nominative with definite article 'die' requires the adjective ending '-en'."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Ersetzen Sie den Relativsatz durch ein Gerundiv (passive Noetwendigkeit): 'Projekte, die noch finanziert werden muessen, erhalten Vorrang.' -> '____ Projekte erhalten Vorrang.'",
        "options": [
            "Noch zu finanzierende",
            "Noch finanzierte",
            "Noch zu finanzierenden",
            "Noch finanzierende"
        ],
        "correctAnswer": "Noch zu finanzierende",
        "explanation": "Passive necessity ('muessen ... werden') is expressed via the Gerundiv ('zu' + Partizip I). 'Projekte' is plural nominative with no article, which triggers the strong adjective ending '-e'."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welche Form ist korrekt? 'Der Professor lobte den Studenten, der seine Masterarbeit fehlerfrei verfasst hatte.' -> 'Der Professor lobte den seine Masterarbeit fehlerfrei ____ Studenten.'",
        "options": [
            "verfasst habenden",
            "verfassenden",
            "verfassten",
            "zu verfassenden"
        ],
        "correctAnswer": "verfasst habenden",
        "explanation": "The relative clause is active but completed in the past (vorzeitig / Plusquamperfekt). To express active past completion in a participial attribute, use past participle of main verb + Partizip I of auxiliary 'haben': 'verfasst habenden'. Modifies 'Studenten' (masculine accusative singular)."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Ergaenzen Sie die Endung des Partizips: Trotz des stundenlang anhaltend____ Regens blieb die Stimmung gut.",
        "options": ["en", "er", "es", "em"],
        "correctAnswer": "en",
        "explanation": "The active simultaneous Partizip I 'anhaltend' modifies 'Regens' (masculine genitive singular). Following the genitive preposition 'trotz' and the definite article element 'des', the weak adjective ending is '-en'."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Verwandeln Sie das Partizipialattribut in einen Relativsatz: 'Die im Labor gezeugt____ Pflanzen sind resistent gegen Schaedlinge.'",
        "options": [
            "Die Pflanzen, die im Labor gezeugt wurden, sind resistent...",
            "Die Pflanzen, die das Labor zeugt, sind resistent...",
            "Die Pflanzen, die im Labor zeugen muessen, sind resistent...",
            "Die Pflanzen, die man im Labor zeugend sieht, sind resistent..."
        ],
        "correctAnswer": "Die Pflanzen, die im Labor gezeugt wurden, sind resistent...",
        "explanation": "Partizip II ('gezeugt') used with a non-reflexive, transitive verb indicates a passive, completed action. Therefore it translates to a passive relative clause in the past."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welches Partizip passt? 'Ein seit Jahren un geloest____ Problem beschaeftigt die Wissenschaftler.'",
        "options": ["es", "en", "er", "e"],
        "correctAnswer": "es",
        "explanation": "'Problem' is neuter singular nominative. Prefaced by the indefinite article 'ein', it requires the strong adjective ending '-es' on the Partizip II 'ungeloest'."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Ergaenzen Sie das passende Gerundiv: Die vom Vorstand morgen ____ Richtlinien muessen von allen Mitarbeitern beachtet werden.",
        "options": [
            "zu beschliessenden",
            "beschlossenen",
            "zu beschliessende",
            "beschliesend"
        ],
        "correctAnswer": "zu beschliessenden",
        "explanation": "The time marker 'morgen' signals a future action that must happen, showing passive obligation. This requires the Gerundiv ('zu' + Partizip I). Modifying 'Richtlinien' (plural nominative with definite article 'die'), it takes the weak ending '-en'."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Transformieren Sie praezise: 'Der Zug, der um 14 Uhr auf Gleis 4 einfaehrt, hat 10 Minuten Verspaetung.' -> 'Der um 14 Uhr auf Gleis 4 ____ Zug hat 10 Minuten Verspaetung.'",
        "options": [
            "einfahrende",
            "eingefahrene",
            "einzufahrende",
            "einfahrenden"
        ],
        "correctAnswer": "einfahrende",
        "explanation": "Active, simultaneous, and current action requires Partizip I of 'einfahren' -> 'einfahrend'. Masculine singular nominative with definite article 'der' results in the ending '-e'."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welcher Satz enthaelt ein grammatikalisch FEHLERFREIES erweitertes Attribut?",
        "options": [
            "Die auf dem Kongress heftig diskutierte These erwies sich als falsch.",
            "Die auf dem Kongress heftig diskutiert These erwies sich als falsch.",
            "Die heftig diskutierte auf dem Kongress These erwies sich als falsch.",
            "Die These heftig auf dem Kongress diskutierte erwies sich als falsch."
        ],
        "correctAnswer": "Die auf dem Kongress heftig diskutierte These erwies sich als falsch.",
        "explanation": "In an extended attribute block, all prepositional details and adverbs must stand between the article ('Die') and the participle ('diskutierte'), which immediately precedes the noun ('These')."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Wie lautet die verbale Entsprechung von: 'Das am Boden liegende Buch gehoert mir.'?",
        "options": [
            "Das Buch, das auf dem Boden liegt, gehoert mir.",
            "Das Buch, das auf den Boden gelegt wurde, gehoert mir.",
            "Das Buch, das man auf den Boden legen muss, gehoert mir.",
            "Das Buch, das auf dem Boden gelegen hat, gehoert mir."
        ],
        "correctAnswer": "Das Buch, das auf dem Boden liegt, gehoert mir.",
        "explanation": "Partizip I ('liegend') denotes an active, progressive, or present state (simultaneous), which translates directly to the present tense indicative active relative clause."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Ergaenzen Sie die komplexe Struktur (Aktiv + Vergangenheit): Die gestern Abend spaet ____ Gaeste schliefen bis zum Mittag.",
        "options": [
            "angekommenen",
            "ankommenden",
            "angekommen",
            "ankommen habenden"
        ],
        "correctAnswer": "angekommenen",
        "explanation": "The verb 'ankommen' is intransitive and forms its past tense with 'sein'. For intransitive verbs that indicate a change of state and pair with 'sein', the simple Partizip II ('angekommen') can be used as an attribute to express an active completed past action. Plural nominative weak ending is '-en'."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Formulieren Sie im Partizipialattribut um: 'Die Aufgaben, die von uns geloest werden koennen, sind ueberschaubar.' -> 'Die von uns ____ Aufgaben sind ueberschaubar.'",
        "options": [
            "zu loesenden",
            "geloesten",
            "loesbaren",
            "loesenden"
        ],
        "correctAnswer": "zu loesenden",
        "explanation": "A participle attribute construction representing passive possibility/necessity explicitly utilizes the Gerundiv structure ('zu' + Partizip I) -> 'zu loesenden'. Although 'loesbar' is an adjective with passive possibility, the Gerundiv is the correct participial form here."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Finden Sie das fehlerhafte Partizipialattribut:",
        "options": [
            "Das gestern gekaufte Auto ist schon kaputt.",
            "Die im Sterben liegende Tradition stirbt aus.",
            "Der gestern den Dieb gefasst habende Polizist wurde geehrt.",
            "Der den Dieb gefangene Polizist wurde geehrt."
        ],
        "correctAnswer": "Der den Dieb gefangene Polizist wurde geehrt.",
        "explanation": "'Fangen' is a transitive active verb. Using Partizip II ('gefangene') as an attribute makes the phrase passive ('the policeman who was caught by the thief'). To keep it active past tense, write 'der den Dieb gefasst habende Polizist'."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Ergaenzen Sie die Endung fuer den Genitiv: Die Aufklaerung des vor zwei Wochen geschehen____ Unfalls dauert an.",
        "options": ["en", "em", "er", "es"],
        "correctAnswer": "en",
        "explanation": "'Geschehen' is an intransitive state-change verb using 'sein', so its Partizip II acts as a past active attribute for 'Unfalls' (masculine genitive singular). Following 'des', the weak ending is '-en'."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Was drueckt das Gerundiv in folgendem Satz aus? 'Die einzureichenden Unterlagen sind vollstaendig.'",
        "options": [
            "Die Unterlagen muessen eingereicht werden.",
            "Die Unterlagen koennen eingereicht werden.",
            "Die Unterlagen wurden bereits eingereicht.",
            "Die Unterlagen duerfen nicht eingereicht werden."
        ],
        "correctAnswer": "Die Unterlagen muessen eingereicht werden.",
        "explanation": "The Gerundiv ('zu' + Partizip I) primarily conveys an absolute duty or obligation (passive necessity) equivalent to 'muessen' or 'sollen'."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Ergaenzen Sie die Luecke: Alle an der Konferenz ____ Experten stimmten dem Vorschlag zu.",
        "options": [
            "teilnehmenden",
            "teilgenommenen",
            "teilzunehmen",
            "teilgenommen habenden"
        ],
        "correctAnswer": "teilnehmenden",
        "explanation": "The relative clause is active and simultaneous ('Experten, die teilnehmen'). This calls for Partizip I ('teilnehmend') plus weak plural ending '-en'."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Waehlen Sie die korrekte Umwandlung in einen Relativsatz: 'Die von Forschern oft zitierte Studie enthaelt Fehler.'",
        "options": [
            "Die Studie, die von Forschern oft zitiert wird, enthaelt Fehler.",
            "Die Studie, die Forscher oft zitierten, hatte Fehler.",
            "Die Studie, die Forscher oft zitieren muessen, enthaelt Fehler.",
            "Die Studie, die Forscher oft zitiert haben werden, enthaelt Fehler."
        ],
        "correctAnswer": "Die Studie, die von Forschern oft zitiert wird, enthaelt Fehler.",
        "explanation": "Partizip II ('zitierte') paired with an ongoing adverbial ('oft') and an agent indicator ('von Forschern') represents a regular present or simple past passive relative clause ('zitiert wird' / 'zitiert wurde')."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welche Konstruktion ist grammatikalisch unzulaessig?",
        "options": [
            "Das zu essende Kind schlaeft.",
            "Das schlafende Kind im Bett ist suess.",
            "Die zu lesenden Buecher liegen auf dem Tisch.",
            "Die reparierte Uhr laeuft wieder einwandfrei."
        ],
        "correctAnswer": "Das zu essende Kind schlaeft.",
        "explanation": "The Gerundiv has passive meaning. 'Das zu essende Kind' would mean 'the child that needs to be eaten', which is semantically nonsensical. It should be 'Das essende Kind' (active: the child that is currently eating)."
    }
]


def add_qs(topic_json_path, questions, topic_name_str):
    with open(topic_json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    existing_ids = {q['id'] for q in data['questions'] if 'id' in q}

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
