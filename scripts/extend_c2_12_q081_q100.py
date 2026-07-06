import json

NEW_QUESTIONS = [
    {
        "id": "c2_12_q081",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Das wird ______ nichts mehr, so kurz vor Ladenschluss.",
        "options": ["wohl", "ruhig", "immerhin", "ja"],
        "correctAnswer": "wohl",
        "explanation": "'Wohl' drückt hier eine begründete Vermutung/Wahrscheinlichkeit aus: Der Sprecher vermutet, dass das Vorhaben angesichts der Zeit scheitern wird.",
        "difficulty": "easy",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q082",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Ob das ______ stimmt, was er da erzählt hat?",
        "options": ["wohl", "ruhig", "sowieso", "immerhin"],
        "correctAnswer": "wohl",
        "explanation": "In indirekten Fragen mit 'ob' erzeugt 'wohl' einen nachdenklichen, unsicheren Ton: Der Sprecher zweifelt und überlegt laut.",
        "difficulty": "medium",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q083",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Welche der folgenden Formulierungen zeigt eine C2-typische, präzise Register-Anpassung eines wohl-Satzes für einen Businessbericht?",
        "options": [
            "Der Umsatzrückgang ist vermutlich auf saisonale Effekte zurückzuführen.",
            "Der Umsatzrückgang ist wohl auf saisonale Effekte zurückzuführen.",
            "Der Umsatzrückgang ist ruhig auf saisonale Effekte zurückzuführen.",
            "Der Umsatzrückgang ist eigentlich auf saisonale Effekte zurückzuführen."
        ],
        "correctAnswer": "Der Umsatzrückgang ist vermutlich auf saisonale Effekte zurückzuführen.",
        "explanation": "In einem formellen Businessbericht wird die Modalpartikel 'wohl' durch das stilistisch angemessenere Adverb 'vermutlich' ersetzt.",
        "difficulty": "medium",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q084",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Was unterscheidet die Verwendung von 'denn' in Fragen von der Verwendung von 'denn' als Konjunktion (z.B. 'Ich bleibe zu Hause, denn es regnet.')?",
        "options": [
            "Als Modalpartikel in Fragen zeigt 'denn' Neugier/Interesse; als Konjunktion begründet es eine Aussage (= 'weil').",
            "Es gibt keinen funktionalen Unterschied.",
            "Als Konjunktion muss 'denn' immer am Satzanfang stehen.",
            "Als Modalpartikel kann 'denn' negiert werden."
        ],
        "correctAnswer": "Als Modalpartikel in Fragen zeigt 'denn' Neugier/Interesse; als Konjunktion begründet es eine Aussage (= 'weil').",
        "explanation": "Dies ist eine zentrale Homonym-Unterscheidung: 'denn' als nebenordnende Konjunktion (Begründung) vs. 'denn' als Modalpartikel (nur in Fragen, Neugier/Ungeduld).",
        "difficulty": "medium",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q085",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Wie heißt du ______ mit Nachnamen?",
        "options": ["denn", "ruhig", "sowieso", "immerhin"],
        "correctAnswer": "denn",
        "explanation": "'Denn' in dieser Frage signalisiert echtes, freundliches Interesse — typisch für ein erstes Kennenlerngespräch.",
        "difficulty": "easy",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q086",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Warum ist der folgende Satz ungrammatisch: '*Er kommt denn morgen.'?",
        "options": [
            "Weil 'denn' als Modalpartikel ausschließlich in Fragesätzen erscheinen darf, nicht in Aussagesätzen.",
            "Weil 'morgen' nicht mit 'kommen' kombiniert werden kann.",
            "Weil 'denn' hier negiert werden müsste.",
            "Weil das Verb an der falschen Position steht."
        ],
        "correctAnswer": "Weil 'denn' als Modalpartikel ausschließlich in Fragesätzen erscheinen darf, nicht in Aussagesätzen.",
        "explanation": "Dies ist eine der wenigen Modalpartikeln mit einer harten syntaktischen Beschränkung: 'denn' als Abtönungspartikel kommt nur in Interrogativsätzen vor.",
        "difficulty": "hard",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q087",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Das Museum ist ______ einen Besuch wert, auch wenn der Eintritt teuer ist.",
        "options": ["durchaus", "ruhig", "bloß", "denn"],
        "correctAnswer": "durchaus",
        "explanation": "'Durchaus' (= 'in der Tat, wirklich') ist ein formelles Gradadverb, das eine Aussage bekräftigt — eine gute, registeradäquate Alternative zu umgangssprachlichen Verstärkern in gehobenen Texten.",
        "difficulty": "medium",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q088",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Welche der folgenden Aussagen über die diachrone Entwicklung von Modalpartikeln ist korrekt?",
        "options": [
            "Viele Modalpartikeln sind aus vollwertigen Adverbien oder Konjunktionen entstanden, die im Lauf der Zeit eine zusätzliche pragmatische Funktion entwickelt haben.",
            "Modalpartikeln sind eine moderne Erfindung des 21. Jahrhunderts.",
            "Modalpartikeln existieren ausschließlich im geschriebenen Deutsch seit dem Mittelalter unverändert.",
            "Modalpartikeln wurden aus dem Englischen ins Deutsche entlehnt."
        ],
        "correctAnswer": "Viele Modalpartikeln sind aus vollwertigen Adverbien oder Konjunktionen entstanden, die im Lauf der Zeit eine zusätzliche pragmatische Funktion entwickelt haben.",
        "explanation": "Sprachhistorisch sind Modalpartikeln oft aus Wörtern mit ursprünglich anderer/breiterer Funktion (Adverbien, Konjunktionen) entstanden — dies erklärt auch die vielen Homonymien (schon, aber, doch).",
        "difficulty": "hard",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q089",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "In einer Debatte sagt jemand: 'Das ist ja wohl nicht dein Ernst!' Welche kombinierte Wirkung erzeugen 'ja' und 'wohl' hier?",
        "options": [
            "Empörte Überraschung/Unglauben gegenüber einer als unangemessen empfundenen Aussage.",
            "Höfliche, neutrale Zustimmung.",
            "Eine sachliche, emotionslose Feststellung.",
            "Eine formelle Entschuldigung."
        ],
        "correctAnswer": "Empörte Überraschung/Unglauben gegenüber einer als unangemessen empfundenen Aussage.",
        "explanation": "Die Kombination 'ja wohl' in Ausrufen wie diesem verstärkt Empörung/Unglauben — ein Ausdruck starker emotionaler Reaktion in der gesprochenen Sprache.",
        "difficulty": "hard",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q090",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Was ist beim Sprachenlernen die wichtigste praktische Konsequenz aus der Tatsache, dass Modalpartikeln keine feste Übersetzung in andere Sprachen haben?",
        "options": [
            "Man muss ihre Funktion im Kontext lernen (Pragmatik), statt eine Eins-zu-eins-Übersetzung zu suchen.",
            "Man sollte sie in der Fremdsprache komplett ignorieren.",
            "Man sollte sie wortwörtlich übersetzen, auch wenn das unnatürlich klingt.",
            "Man sollte sie durch das englische Wort 'well' ersetzen."
        ],
        "correctAnswer": "Man muss ihre Funktion im Kontext lernen (Pragmatik), statt eine Eins-zu-eins-Übersetzung zu suchen.",
        "explanation": "Modalpartikeln sind ein klassisches Beispiel für sprachspezifische Pragmatik ohne direkte Entsprechung — Lernende müssen die kommunikative Funktion im jeweiligen Kontext verstehen, nicht wörtlich übersetzen.",
        "difficulty": "medium",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q091",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Sie ist ______ nicht dumm, aber manchmal etwas unaufmerksam.",
        "options": ["zwar", "ruhig", "denn", "bloß"],
        "correctAnswer": "zwar",
        "explanation": "'Zwar... aber' leitet eine konzessive Struktur ein: ein Zugeständnis ('nicht dumm'), gefolgt von einer einschränkenden Ergänzung ('aber unaufmerksam').",
        "difficulty": "medium",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q092",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Wähle die Formulierung, die am ehesten in einem literarischen Dialog (nicht in einem Sachtext) vorkäme:",
        "options": [
            "'Na, dann komm doch mal rein, du wirst ja ganz nass!'",
            "Die Umsatzzahlen sind im dritten Quartal vermutlich gesunken.",
            "Gemäß Paragraph 5 ist der Antrag fristgerecht einzureichen.",
            "Die Studie zeigt einen signifikanten Zusammenhang zwischen X und Y."
        ],
        "correctAnswer": "'Na, dann komm doch mal rein, du wirst ja ganz nass!'",
        "explanation": "Die Häufung von 'doch', 'mal' und 'ja' in einer lebendigen, direkten Anrede ist typisch für gesprochene/literarische Dialoge, nicht für Sachtexte.",
        "difficulty": "easy",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q093",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Ich weiß auch nicht, was ich ______ machen soll.",
        "options": ["bloß", "ruhig", "sowieso", "immerhin"],
        "correctAnswer": "bloß",
        "explanation": "'Bloß' verstärkt hier Ratlosigkeit/Verzweiflung in einer indirekten Frage — ein häufiges Muster bei Unsicherheit oder Überforderung.",
        "difficulty": "medium",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q094",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Fasse zusammen: Warum gelten Modalpartikeln als 'Abtönungspartikeln'?",
        "options": [
            "Weil sie die emotionale/kommunikative 'Tönung' (Färbung) einer Aussage verändern, ohne deren sachlichen Inhalt zu beeinflussen.",
            "Weil sie ausschließlich Tonhöhen in der Musik beschreiben.",
            "Weil sie immer laut ausgesprochen werden müssen.",
              "Weil sie den Kasus des folgenden Nomens verändern."
        ],
        "correctAnswer": "Weil sie die emotionale/kommunikative 'Tönung' (Färbung) einer Aussage verändern, ohne deren sachlichen Inhalt zu beeinflussen.",
        "explanation": "Der Fachbegriff 'Abtönungspartikel' beschreibt genau diese Funktion: eine feine emotionale/pragmatische Färbung, ohne die Wahrheitsbedingungen (den sachlichen Inhalt) des Satzes zu ändern.",
        "difficulty": "medium",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q095",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Welche Strategie empfiehlt sich für C2-Lernende, um Modalpartikeln aktiv und natürlich zu üben?",
        "options": [
            "Authentische Dialoge (Filme, Serien, Alltagsgespräche) analysieren und die Funktion jeder Partikel im Kontext bestimmen, statt Listen auswendig zu lernen.",
            "Nur geschriebene, formelle Zeitungsartikel lesen, da diese die meisten Modalpartikeln enthalten.",
            "Modalpartikeln in willkürlicher Reihenfolge in jeden Satz einfügen.",
            "Ausschließlich Grammatikregeln ohne Beispielsätze auswendig lernen."
        ],
        "correctAnswer": "Authentische Dialoge (Filme, Serien, Alltagsgespräche) analysieren und die Funktion jeder Partikel im Kontext bestimmen, statt Listen auswendig zu lernen.",
        "explanation": "Da Modalpartikeln primär im gesprochenen Register vorkommen und stark kontextabhängig sind, ist authentischer Input (Dialoge) der wirksamste Lernweg — reines Auswendiglernen von Listen greift zu kurz.",
        "difficulty": "medium",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q096",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Komm, sei ______ nicht so streng mit dir selbst!",
        "options": ["doch", "ruhig", "sowieso", "immerhin"],
        "correctAnswer": "doch",
        "explanation": "'Doch' verleiht der Aufforderung/Bitte hier einen einfühlsamen, ermutigenden Nachdruck — typisch für tröstende oder beruhigende Ansprache.",
        "difficulty": "easy",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q097",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Warum ist die Aussage 'Modalpartikeln haben keine Bedeutung' fachlich ungenau?",
        "options": [
            "Sie haben keine propositionale/lexikalische Bedeutung wie Inhaltswörter, aber eine klare pragmatische Funktion (Einstellung, Erwartungshaltung des Sprechers).",
            "Modalpartikeln haben exakt dieselbe Bedeutung wie Substantive.",
            "Modalpartikeln haben nur eine Bedeutung in der Mathematik.",
            "Die Aussage ist vollkommen korrekt und unproblematisch."
        ],
        "correctAnswer": "Sie haben keine propositionale/lexikalische Bedeutung wie Inhaltswörter, aber eine klare pragmatische Funktion (Einstellung, Erwartungshaltung des Sprechers).",
        "explanation": "Modalpartikeln verändern nicht den propositionalen Gehalt (die 'Fakten') eines Satzes, aber sie transportieren wichtige pragmatische Information über die Einstellung des Sprechers — das ist eine Bedeutungsebene, nur eine andere als bei Inhaltswörtern.",
        "difficulty": "hard",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q098",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Ordne der Situation die passende Modalpartikel zu: Ein Freund erzählt etwas offensichtlich Übertriebenes, und du reagierst zweifelnd-amüsiert: 'Das ist ______ nicht dein Ernst!'",
        "options": ["ja wohl", "ruhig", "sowieso", "immerhin"],
        "correctAnswer": "ja wohl",
        "explanation": "Die Kombination 'ja wohl' erzeugt hier einen zweifelnd-überraschten, leicht amüsierten Ton — eine typische informelle Reaktion auf eine unglaubwürdige Aussage.",
        "difficulty": "medium",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q099",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Welche der folgenden C2-Prüfungsaufgaben würde Modalpartikeln-Kompetenz am direktesten testen?",
        "options": [
            "Ein Hördialog, in dem die Testperson die Einstellung/Emotion eines Sprechers anhand von Tonfall und Partikelgebrauch identifizieren muss.",
            "Eine Aufgabe zum Auswendiglernen der deutschen Zahlen.",
            "Eine Aufgabe zur Konjugation regelmäßiger Verben im Präsens.",
            "Eine Aufgabe zum Erkennen von Farben auf einem Bild."
        ],
        "correctAnswer": "Ein Hördialog, in dem die Testperson die Einstellung/Emotion eines Sprechers anhand von Tonfall und Partikelgebrauch identifizieren muss.",
        "explanation": "Modalpartikeln sind primär eine Kompetenz des Hör-/Leseverstehens (Erkennen von Nuancen) und der mündlichen Produktion — passend zu Hördialog-Aufgaben, die Einstellung/Emotion erfragen.",
        "difficulty": "medium",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q100",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Fasse die wichtigste Grundregel für Modalpartikeln im formellen Schreiben in einem Satz zusammen:",
        "options": [
            "Modalpartikeln gehören primär zur gesprochenen Sprache und sollten in formellen Texten durch passende Adverbien oder ganz weggelassen werden.",
            "Modalpartikeln müssen in jedem formellen Satz mindestens einmal vorkommen.",
            "Modalpartikeln sind in formellen Texten grammatisch verboten und führen zu Fehlermeldungen.",
            "Modalpartikeln haben im formellen Schreiben dieselbe Funktion wie in der gesprochenen Sprache."
        ],
        "correctAnswer": "Modalpartikeln gehören primär zur gesprochenen Sprache und sollten in formellen Texten durch passende Adverbien oder ganz weggelassen werden.",
        "explanation": "Dies ist die zentrale Register-Regel dieser Lektion: Modalpartikeln sind grammatisch korrekt, aber stilistisch an das gesprochene/informelle Register gebunden — in formellen Texten wirken sie deplatziert.",
        "difficulty": "easy",
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
