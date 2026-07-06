import json

data = {
    "subjectId": "c2_12",
    "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
    "level": "C2",
    "description": "Modalpartikeln (Abtönungspartikeln) im gehobenen und gesprochenen Deutsch — C2-Kompetenz im Erkennen und korrekten Einsatz unbetonter Wörter, die die Einstellung des Sprechers zur Aussage signalisieren, ohne die propositionale Bedeutung des Satzes zu verändern.\n\n1. Definition und Grundeigenschaften\nModalpartikeln (auch Abtönungspartikeln genannt) sind eine geschlossene Wortklasse unbetonter, nicht flektierbarer Wörter im Mittelfeld des Satzes. Sie: (a) tragen nie den Satzakzent, (b) koennen nicht negiert werden (*nicht ja, *nicht doch), (c) koennen nicht allein als Antwort auf eine Frage stehen, (d) koennen nicht im Vorfeld (Position 1) stehen, (e) veraendern nicht die Wahrheitsbedingungen des Satzes, sondern nur dessen illokutionaere Faerbung.\n\n2. ja — geteiltes Wissen\n'Ja' signalisiert, dass die Information dem Hoerer bereits bekannt ist oder offensichtlich sein sollte. Beispiel: 'Du weisst ja, dass ich das nicht mag.' (Reminder-Funktion, keine Ueberraschung erwartet.)\n\n3. doch — Widerspruch, Nachdruck, Erinnerung\n'Doch' hat drei Hauptfunktionen: (a) Widerspruch zu einer impliziten Annahme: 'Das ist doch nicht so schwer!'; (b) Nachdrueckliche Aufforderung: 'Komm doch mit!'; (c) Erinnerung an Bekanntes mit Vorwurfston: 'Du haettest doch fragen koennen!'\n\n4. eben / halt — Resignation, Unabaenderlichkeit\nBeide Partikeln praesentieren einen Sachverhalt als gegeben und nicht mehr diskutierbar. 'eben' ist standardsprachlich neutral, 'halt' ist regional (süddeutsch/österreichisch) gepraegt und im formellen Schriftdeutsch zu vermeiden. Beispiel: 'Das ist eben so.' / 'Das ist halt so.'\n\n5. wohl — Vermutung, Wahrscheinlichkeit\n'Wohl' druckt eine Annahme mit einem gewissen Grad an Unsicherheit aus: 'Sie wird wohl wissen, was sie tut.' In Fragen erzeugt es einen nachdenklichen, unsicheren Ton: 'Ob das wohl stimmt?'\n\n6. schon — Beruhigung, rhetorische Bekraeftigung\nAls Modalpartikel (nicht zu verwechseln mit dem Temporaladverb 'schon' = bereits) druckt es Zuversicht/Beruhigung aus: 'Das wird schon klappen.' In rhetorischen Fragen verstaerkt es eine implizite Verneinung: 'Wer soll das schon wissen?' (= Niemand weiss das wirklich.)\n\n7. ruhig — Erlaubnis, Ermutigung\n'Ruhig' signalisiert, dass eine Handlung ohne Bedenken ausgefuehrt werden darf: 'Du kannst ruhig fragen.' (= Es ist kein Problem, wenn du fragst.)\n\n8. mal — Verharmlosung, Beilaeufigkeit\n'Mal' downtoned eine Aufforderung oder macht sie beilaeufiger: 'Komm mal her.' / 'Sag mal, kennst du ihn schon?' Kombinationen mit anderen Partikeln folgen einer festen Reihenfolge: 'Komm doch mal her!' (nicht: *'Komm mal doch her!').\n\n9. denn — neugierige/ungeduldige Frage\n'Denn' erscheint ausschliesslich in Fragesaetzen und signalisiert echtes Interesse oder Ungeduld: 'Was machst du denn hier?' Ohne 'denn' wirkt die gleiche Frage neutraler oder sogar konfrontativ.\n\n10. aber (exklamatorisch) — Ueberraschung, Bewunderung\nIn Ausrufesaetzen fungiert das unbetonte 'aber' als Modalpartikel der Ueberraschung: 'Das ist aber schoen!' (= Wie schoen das ist!) Dies ist von der adversativen Konjunktion 'aber' (= 'jedoch') klar zu unterscheiden.\n\n11. Register: Modalpartikeln im formellen Schreiben\nModalpartikeln sind primaer ein Merkmal der gesprochenen Sprache und informeller Texte. In formellen/akademischen Aufsaetzen (Stellungnahme, Bericht) werden sie in der Regel vermieden oder durch explizite Adverbien ersetzt (z.B. 'wohl' → 'vermutlich', 'eben' → 'offensichtlich'). Ihre Verwendung in Pruefungsaufsaetzen gilt als Stilfehler.",
    "tips": [
        "Rule A — Die vier Diagnosetests fuer Modalpartikeln: (1) Kann das Wort betont werden? Wenn ja, ist es keine Modalpartikel. (2) Kann es negiert werden (*nicht doch)? Nein → Modalpartikel. (3) Kann es allein auf eine Frage antworten? Nein → Modalpartikel. (4) Steht es im Vorfeld? Nein, nur im Mittelfeld → Modalpartikel. Wenden Sie diese Tests an, um Modalpartikeln von homonymen Adverbien/Konjunktionen zu unterscheiden.",
        "Rule B — Homonyme richtig trennen: 'schon' als Modalpartikel (Beruhigung: 'Das wird schon') vs. 'schon' als Temporaladverb (bereits: 'Er ist schon da'). 'aber' als Modalpartikel (Ueberraschung: 'Das ist aber schoen!') vs. 'aber' als Konjunktion (Gegensatz: 'Ich wollte kommen, aber es ging nicht'). Der Betonungstest hilft: Modalpartikeln sind IMMER unbetont.",
        "Rule C — Partikelkombinationen haben eine feste Reihenfolge: 'doch mal', 'ja auch', 'doch wohl' — die Reihenfolge ist nicht frei vertauschbar. Merken Sie sich haeufige Kombinationen als feste Einheiten, statt sie grammatisch herzuleiten.",
        "Rule D — Register-Bewusstsein fuer die Pruefung: Verwenden Sie in formellen Schreibaufgaben (Bericht, Stellungnahme, Kommentar) KEINE Modalpartikeln. Ersetzen Sie sie durch Adverbien: 'wohl' → 'vermutlich/wahrscheinlich', 'eben/halt' → 'offensichtlich/nun einmal', 'ja' → '(bekanntlich)'. Modalpartikeln in einem C2-Aufsatz senken den Stilwert erheblich.",
        "Tip 1 — 'denn' nur in Fragen: Anders als die meisten Modalpartikeln ist 'denn' auf Interrogativsaetze beschraenkt. 'Was machst du denn?' ist korrekt, ein Aussagesatz mit 'denn' als Modalpartikel ('*Ich mache denn das') ist ungrammatisch.",
        "Tip 2 — 'halt' vs. 'eben' im Schriftdeutsch: Beide sind bedeutungsgleich (Resignation/Unabaenderlichkeit), aber 'halt' gilt als regional markiert und sollte im formellen Hochdeutsch durch 'eben' oder eine Umschreibung ersetzt werden.",
        "Tip 3 — 'doch' als Vorwurfssignal erkennen: Wenn 'doch' mit dem Konjunktiv II der Vergangenheit kombiniert wird ('Du haettest doch fragen koennen'), signalisiert es fast immer einen impliziten Vorwurf oder Bedauern — wichtig fuer das Textverstaendnis in Dialogen und literarischen Texten.",
        "Tip 4 — Ruhig vs. gerne: 'Ruhig' erteilt eine Erlaubnis ohne Bedenken ('Du kannst ruhig fragen' = es ist kein Problem), waehrend 'gerne' eine Bereitschaft ausdrueckt. Diese beiden werden von Lernenden haeufig verwechselt.",
        "Tip 5 — Haeufungen vermeiden: Auch im gesprochenen Deutsch wirken mehr als zwei Modalpartikeln in einem Satz ueberladen ('Das ist ja wohl doch eben klar' ist stilistisch schlecht). Fuer die Pruefung: maximal eine, selten zwei Modalpartikeln pro Aeusserung als natuerliches Vorbild verwenden."
    ],
    "questions": [
        {
            "id": "c2_12_q001",
            "subjectId": "c2_12",
            "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
            "questionText": "Du weißt ______, dass ich das nicht mag.",
            "options": ["ja", "vielmehr", "bloß", "erst"],
            "correctAnswer": "ja",
            "explanation": "Die Modalpartikel 'ja' signalisiert, dass die genannte Information dem Hörer bereits bekannt ist — hier mit leicht erinnerndem/vorwurfsvollem Unterton.",
            "difficulty": "easy",
            "type": "multiple_choice"
        },
        {
            "id": "c2_12_q002",
            "subjectId": "c2_12",
            "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
            "questionText": "Frag ______, wenn du etwas nicht verstehst – das ist kein Problem.",
            "options": ["ruhig", "eben", "wohl", "doch"],
            "correctAnswer": "ruhig",
            "explanation": "'Ruhig' als Modalpartikel erteilt eine Erlaubnis oder Ermutigung ohne Bedenken: Es signalisiert, dass die Handlung problemlos ausgeführt werden darf.",
            "difficulty": "easy",
            "type": "multiple_choice"
        },
        {
            "id": "c2_12_q003",
            "subjectId": "c2_12",
            "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
            "questionText": "Das ist ______ klar, dass er zu spät kommt – er kommt schließlich immer zu spät.",
            "options": ["eben", "denn", "bloß", "vielmehr"],
            "correctAnswer": "eben",
            "explanation": "'Eben' präsentiert einen Sachverhalt als gegeben und nicht mehr diskutierbar — hier als Ausdruck von Resignation gegenüber einer bekannten Gewohnheit.",
            "difficulty": "easy",
            "type": "multiple_choice"
        },
        {
            "id": "c2_12_q004",
            "subjectId": "c2_12",
            "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
            "questionText": "Was machst du ______ hier so spät? Ich hätte dich gar nicht erwartet.",
            "options": ["denn", "doch", "schon", "ruhig"],
            "correctAnswer": "denn",
            "explanation": "'Denn' erscheint ausschließlich in Fragesätzen und signalisiert echtes Interesse oder Neugier des Sprechers.",
            "difficulty": "easy",
            "type": "multiple_choice"
        },
        {
            "id": "c2_12_q005",
            "subjectId": "c2_12",
            "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
            "questionText": "Sie wird ______ wissen, was sie tut – sie ist schließlich Expertin.",
            "options": ["wohl", "bloß", "mal", "vielmehr"],
            "correctAnswer": "wohl",
            "explanation": "'Wohl' drückt eine Vermutung mit einem gewissen Grad an Wahrscheinlichkeit aus, hier im Sinne von 'vermutlich'.",
            "difficulty": "easy",
            "type": "multiple_choice"
        },
        {
            "id": "c2_12_q006",
            "subjectId": "c2_12",
            "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
            "questionText": "Welche Aussage über Modalpartikeln (Abtönungspartikeln) ist korrekt?",
            "options": [
                "Sie können nicht negiert werden und tragen nie den Satzakzent.",
                "Sie stehen immer im Vorfeld (Position 1) des Satzes.",
                "Sie können allein als vollständige Antwort auf eine Frage stehen.",
                "Sie verändern stets die Wahrheitsbedingungen des Satzes."
            ],
            "correctAnswer": "Sie können nicht negiert werden und tragen nie den Satzakzent.",
            "explanation": "Modalpartikeln sind unbetont, nicht negierbar, nicht vorfeldfähig und nicht alleinstehend als Antwort verwendbar — sie verändern nur die illokutionäre Färbung, nicht die propositionale Bedeutung.",
            "difficulty": "medium",
            "type": "multiple_choice"
        },
        {
            "id": "c2_12_q007",
            "subjectId": "c2_12",
            "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
            "questionText": "Komm ______ mit, es wird bestimmt lustig!",
            "options": ["doch mal", "mal doch", "schon mal", "halt doch"],
            "correctAnswer": "doch mal",
            "explanation": "Partikelkombinationen folgen einer festen Reihenfolge. 'Doch mal' ist die idiomatische Abfolge (Nachdruck + Verharmlosung); die umgekehrte Reihenfolge 'mal doch' ist ungrammatisch.",
            "difficulty": "medium",
            "type": "multiple_choice"
        },
        {
            "id": "c2_12_q008",
            "subjectId": "c2_12",
            "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
            "questionText": "In welchem Satz ist 'schon' ein Temporaladverb (NICHT eine Modalpartikel)?",
            "options": [
                "Er ist schon angekommen.",
                "Das wird schon klappen.",
                "Wer soll das schon wissen?",
                "Sie kommt schon zurecht."
            ],
            "correctAnswer": "Er ist schon angekommen.",
            "explanation": "Hier bedeutet 'schon' 'bereits' und bezieht sich auf den Zeitpunkt der Handlung — ein Temporaladverb. In den anderen Sätzen drückt 'schon' als Modalpartikel Beruhigung oder rhetorische Bekräftigung aus.",
            "difficulty": "medium",
            "type": "multiple_choice"
        },
        {
            "id": "c2_12_q009",
            "subjectId": "c2_12",
            "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
            "questionText": "Der Ausblick von hier oben ist ______ atemberaubend!",
            "options": ["aber", "denn", "wohl", "eben"],
            "correctAnswer": "aber",
            "explanation": "In Ausrufesätzen fungiert das unbetonte 'aber' als Modalpartikel der Überraschung/Bewunderung (= 'Wie atemberaubend das ist!') — klar zu unterscheiden von der adversativen Konjunktion 'aber' (= 'jedoch').",
            "difficulty": "medium",
            "type": "multiple_choice"
        },
        {
            "id": "c2_12_q010",
            "subjectId": "c2_12",
            "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
            "questionText": "Du hättest mich ______ früher anrufen können, dann hätte ich noch reagieren können!",
            "options": ["doch", "ruhig", "mal", "wohl"],
            "correctAnswer": "doch",
            "explanation": "'Doch' in Kombination mit dem Konjunktiv II der Vergangenheit signalisiert einen impliziten Vorwurf oder Bedauern über eine verpasste Gelegenheit.",
            "difficulty": "medium",
            "type": "multiple_choice"
        },
        {
            "id": "c2_12_q011",
            "subjectId": "c2_12",
            "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
            "questionText": "Sag ______, kennst du den neuen Kollegen eigentlich schon?",
            "options": ["mal", "eben", "wohl", "bloß"],
            "correctAnswer": "mal",
            "explanation": "'Sag mal' ist eine feste, beiläufige Gesprächseröffnung; 'mal' downtoned hier die Aufforderung und macht sie informeller.",
            "difficulty": "medium",
            "type": "multiple_choice"
        },
        {
            "id": "c2_12_q012",
            "subjectId": "c2_12",
            "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
            "questionText": "Welche Partikel gilt als regional (süddeutsch/österreichisch) markiert und sollte im formellen Hochdeutsch eher durch 'eben' ersetzt werden?",
            "options": ["halt", "denn", "ja", "aber"],
            "correctAnswer": "halt",
            "explanation": "'Halt' ist bedeutungsgleich mit 'eben' (Resignation/Unabänderlichkeit), gilt aber als regional geprägt und wird im formellen Schriftdeutsch vermieden.",
            "difficulty": "medium",
            "type": "multiple_choice"
        },
        {
            "id": "c2_12_q013",
            "subjectId": "c2_12",
            "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
            "questionText": "Warum sollten Modalpartikeln in einem formellen C2-Prüfungsaufsatz (z.B. einer Stellungnahme) vermieden werden?",
            "options": [
                "Weil sie ein Merkmal der gesprochenen/informellen Sprache sind und den Stilwert eines formellen Textes senken.",
                "Weil sie grammatisch grundsätzlich falsch sind.",
                "Weil sie nur in der Umgangssprache existieren und keine Bedeutung tragen.",
                "Weil sie ausschließlich in Fragesätzen erlaubt sind."
            ],
            "correctAnswer": "Weil sie ein Merkmal der gesprochenen/informellen Sprache sind und den Stilwert eines formellen Textes senken.",
            "explanation": "Modalpartikeln sind grammatisch korrekt, gehören aber primär zum gesprochenen/informellen Register. In akademischen oder formellen Texten wirken sie stilistisch unpassend und sollten durch Adverbien ersetzt werden.",
            "difficulty": "medium",
            "type": "multiple_choice"
        },
        {
            "id": "c2_12_q014",
            "subjectId": "c2_12",
            "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
            "questionText": "Welcher Satz ist eine geeignete formelle Umschreibung für 'Das stimmt wohl.' in einem akademischen Text?",
            "options": [
                "Das trifft vermutlich zu.",
                "Das stimmt ja.",
                "Das stimmt halt.",
                "Das stimmt eben."
            ],
            "correctAnswer": "Das trifft vermutlich zu.",
            "explanation": "Im formellen Register wird die Modalpartikel 'wohl' (Vermutung) durch das Adverb 'vermutlich' ersetzt, um denselben Grad an Unsicherheit auszudrücken.",
            "difficulty": "hard",
            "type": "multiple_choice"
        },
        {
            "id": "c2_12_q015",
            "subjectId": "c2_12",
            "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
            "questionText": "Wer soll das ______ wissen? Es steht doch nirgendwo geschrieben.",
            "options": ["schon", "denn", "ruhig", "halt"],
            "correctAnswer": "schon",
            "explanation": "In rhetorischen Fragen verstärkt 'schon' eine implizite Verneinung: 'Wer soll das schon wissen?' bedeutet 'Niemand weiß das wirklich.'",
            "difficulty": "hard",
            "type": "multiple_choice"
        },
        {
            "id": "c2_12_q016",
            "subjectId": "c2_12",
            "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
            "questionText": "Welcher der folgenden Sätze ist grammatisch UNGRAMMATISCH, weil eine Modalpartikel gegen ihre syntaktische Beschränkung verstößt?",
            "options": [
                "Doch machen wir das morgen.",
                "Wir machen das doch morgen.",
                "Machen wir das doch morgen?",
                "Wir sollten das doch morgen machen."
            ],
            "correctAnswer": "Doch machen wir das morgen.",
            "explanation": "Modalpartikeln können nicht im Vorfeld (Position 1) stehen. 'Doch' am Satzanfang wäre nur als betontes Adverb ('jedoch/jedenfalls') möglich, nicht als unbetonte Modalpartikel mit der hier intendierten Abtönungsfunktion.",
            "difficulty": "hard",
            "type": "multiple_choice"
        },
        {
            "id": "c2_12_q017",
            "subjectId": "c2_12",
            "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
            "questionText": "Worin unterscheidet sich 'ruhig' von 'gerne' in Sätzen wie 'Du kannst ruhig fragen' vs. 'Ich helfe dir gerne'?",
            "options": [
                "'Ruhig' erteilt eine Erlaubnis ohne Bedenken, 'gerne' drückt eine positive Bereitschaft aus.",
                "Beide Wörter sind vollständig synonym und austauschbar.",
                "'Ruhig' ist ein Adjektiv, 'gerne' eine Modalpartikel.",
                "'Ruhig' drückt Ungeduld aus, 'gerne' drückt Ablehnung aus."
            ],
            "correctAnswer": "'Ruhig' erteilt eine Erlaubnis ohne Bedenken, 'gerne' drückt eine positive Bereitschaft aus.",
            "explanation": "'Ruhig' als Modalpartikel signalisiert, dass eine Handlung bedenkenlos ausgeführt werden darf, während 'gerne' die Bereitschaft des Sprechers ausdrückt, etwas zu tun.",
            "difficulty": "hard",
            "type": "multiple_choice"
        },
        {
            "id": "c2_12_q018",
            "subjectId": "c2_12",
            "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
            "questionText": "Welcher Test hilft am zuverlässigsten, eine Modalpartikel von einem homonymen Adverb zu unterscheiden?",
            "options": [
                "Der Betonungstest: Modalpartikeln sind immer unbetont.",
                "Der Kasustest: Modalpartikeln stehen immer im Akkusativ.",
                "Der Pluraltest: Modalpartikeln haben eine eigene Pluralform.",
                "Der Komparationstest: Modalpartikeln können gesteigert werden."
            ],
            "correctAnswer": "Der Betonungstest: Modalpartikeln sind immer unbetont.",
            "explanation": "Modalpartikeln tragen nie den Satzakzent. Wird das homonyme Wort betont (z.B. 'schon' im Sinne von 'bereits'), handelt es sich nicht um die Modalpartikel-Lesart.",
            "difficulty": "hard",
            "type": "multiple_choice"
        },
        {
            "id": "c2_12_q019",
            "subjectId": "c2_12",
            "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
            "questionText": "Warum ist der Satz 'Das ist ja wohl doch eben klar!' stilistisch problematisch, obwohl er grammatisch korrekt ist?",
            "options": [
                "Weil die Häufung von vier Modalpartikeln in einem Satz überladen und unnatürlich wirkt.",
                "Weil Modalpartikeln grundsätzlich nicht kombiniert werden dürfen.",
                "Weil der Satz keine der genannten Partikeln enthalten darf.",
                "Weil 'klar' in diesem Kontext kein zulässiges Adjektiv ist."
            ],
            "correctAnswer": "Weil die Häufung von vier Modalpartikeln in einem Satz überladen und unnatürlich wirkt.",
            "explanation": "Auch im gesprochenen Deutsch gilt: Mehr als zwei Modalpartikeln in einer Äußerung wirken stilistisch überladen. Für die Prüfung empfiehlt sich ein sparsamer, natürlicher Einsatz.",
            "difficulty": "hard",
            "type": "multiple_choice"
        },
        {
            "id": "c2_12_q020",
            "subjectId": "c2_12",
            "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
            "questionText": "Welche Funktion hat 'eigentlich' in der Frage: 'Was machst du eigentlich beruflich?'",
            "options": [
                "Es mildert die Direktheit der Frage und wirkt beiläufig-interessiert.",
                "Es verneint die gesamte Aussage.",
                "Es fordert eine sofortige, knappe Antwort ohne Umschweife.",
                "Es signalisiert, dass die Frage bereits einmal gestellt wurde."
            ],
            "correctAnswer": "Es mildert die Direktheit der Frage und wirkt beiläufig-interessiert.",
            "explanation": "'Eigentlich' als Modalpartikel softens eine Frage und verleiht ihr einen beiläufigen, nebenbei interessierten Ton, oft eingesetzt, um ein neues Gesprächsthema unaufdringlich einzuleiten.",
            "difficulty": "medium",
            "type": "multiple_choice"
        }
    ],
    "totalQuestions": 20
}

output_path = 'app/src/main/assets/c2_12.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Created {output_path} with {len(data['questions'])} questions")
print(f"Description length: {len(data['description'])} chars")
print(f"Tips: {len(data['tips'])} tips")
