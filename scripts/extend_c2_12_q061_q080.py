import json

NEW_QUESTIONS = [
    {
        "id": "c2_12_q061",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Welche Modalpartikel passt in eine rhetorische Frage, die eigentlich eine Verneinung ausdrückt: 'Wer soll das ______ bezahlen?'",
        "options": ["schon", "ruhig", "sowieso", "immerhin"],
        "correctAnswer": "schon",
        "explanation": "'Wer soll das schon bezahlen?' bedeutet implizit 'Niemand kann/wird das bezahlen' — 'schon' verstärkt hier die rhetorische Verneinung.",
        "difficulty": "medium",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q062",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Das war ______ klar, dass das nicht funktionieren würde!",
        "options": ["ja", "ruhig", "bloß", "sowieso"],
        "correctAnswer": "ja",
        "explanation": "'Ja' markiert hier eine im Nachhinein als offensichtlich dargestellte Tatsache — der Sprecher betont, dass das Scheitern vorhersehbar war.",
        "difficulty": "easy",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q063",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Warum eignet sich der Satz 'Man müsste das eigentlich anders regeln.' gut, um C2-Kompetenz in einer Diskussion zu zeigen?",
        "options": [
            "Er kombiniert Konjunktiv II (Höflichkeit/Vorsicht) mit der Modalpartikel 'eigentlich' (leichte Korrektur/Kritik), ein typisches Muster gehobener Diskursivität.",
            "Er enthält keine Modalpartikel.",
            "Er ist im Präsens formuliert und daher direkt.",
            "Er verwendet ausschließlich Fachvokabular ohne Partikeln."
        ],
        "correctAnswer": "Er kombiniert Konjunktiv II (Höflichkeit/Vorsicht) mit der Modalpartikel 'eigentlich' (leichte Korrektur/Kritik), ein typisches Muster gehobener Diskursivität.",
        "explanation": "Die Kombination aus Konjunktiv II und 'eigentlich' erlaubt es, Kritik oder Verbesserungsvorschläge höflich-indirekt zu formulieren — eine Zielkompetenz für C2-Diskursivität.",
        "difficulty": "hard",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q064",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Welches Verb + Modalpartikel-Kombination drückt am ehesten milde Ungeduld aus: 'Nun ______ zu, was ich sage!'",
        "options": ["hör", "höre ruhig", "höre sowieso", "höre immerhin"],
        "correctAnswer": "hör",
        "explanation": "'Nun hör zu!' mit vorangestelltem 'nun' (temporale Modalpartikel-ähnliche Funktion) drückt Ungeduld/Nachdruck aus, ähnlich wie 'doch' in Aufforderungen.",
        "difficulty": "medium",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q065",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Welche Aussage zu 'nun' als Modalpartikel/Diskursmarker ist korrekt?",
        "options": [
            "'Nun' kann einen Übergang oder eine leichte Ungeduld/Betonung markieren, z.B. 'Nun mach schon!'",
            "'Nun' bedeutet ausschließlich 'niemals'.",
            "'Nun' ist ausschließlich ein Fachbegriff der Mathematik.",
            "'Nun' kann nicht am Satzanfang stehen."
        ],
        "correctAnswer": "'Nun' kann einen Übergang oder eine leichte Ungeduld/Betonung markieren, z.B. 'Nun mach schon!'",
        "explanation": "'Nun' fungiert oft als Diskursmarker/Modalpartikel-ähnliches Element, das einen Übergang, eine Schlussfolgerung oder eine leichte Ungeduld signalisiert.",
        "difficulty": "medium",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q066",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Ich hab's dir ______ gesagt!",
        "options": ["doch", "ruhig", "immerhin", "sowieso"],
        "correctAnswer": "doch",
        "explanation": "'Ich hab's dir doch gesagt!' ist eine feste Vorwurfsformel — 'doch' erinnert an eine bereits gegebene Warnung, die ignoriert wurde.",
        "difficulty": "easy",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q067",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Welche zwei Modalpartikeln lassen sich in der Vorwurfsformel 'Du hättest ______ ______ fragen können!' idiomatisch kombinieren?",
        "options": ["doch ruhig", "ruhig doch", "sowieso bloß", "bloß sowieso"],
        "correctAnswer": "doch ruhig",
        "explanation": "'Du hättest doch ruhig fragen können!' kombiniert den Vorwurfston von 'doch' mit der Erlaubnis-Nuance von 'ruhig' (= es wäre problemlos möglich gewesen) — eine idiomatische, natürliche Reihenfolge.",
        "difficulty": "hard",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q068",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Welche der folgenden Sätze verwendet 'schon' eindeutig als Temporaladverb (nicht als Modalpartikel)?",
        "options": [
            "Bist du schon fertig?",
            "Das schaffst du schon.",
            "Na, wird schon werden.",
            "Wer weiß das schon genau?"
        ],
        "correctAnswer": "Bist du schon fertig?",
        "explanation": "'Bist du schon fertig?' fragt nach dem Zeitpunkt (= bereits) — ein klarer temporaler Gebrauch, im Gegensatz zu den anderen Beispielen, in denen 'schon' Beruhigung oder rhetorische Verneinung signalisiert.",
        "difficulty": "medium",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q069",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "In einem literarischen Text: 'Ach, was weiß ich schon davon!' — welche Haltung drückt der Sprecher aus?",
        "options": [
            "Resignierte Bescheidenheit oder Selbstironie bezüglich der eigenen Kenntnis.",
            "Vollständige Expertise und Stolz.",
            "Eine neutrale, sachliche Aussage ohne emotionale Färbung.",
            "Eine formelle Ablehnung eines Antrags."
        ],
        "correctAnswer": "Resignierte Bescheidenheit oder Selbstironie bezüglich der eigenen Kenntnis.",
        "explanation": "Die Kombination aus 'ach', rhetorischer Frage-Struktur und 'schon' erzeugt einen Ton von Selbstironie/Bescheidenheit — 'ich weiß eigentlich kaum etwas darüber'.",
        "difficulty": "hard",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q070",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Welches Adverb ersetzt 'wohl' (Vermutung) am treffendsten in einer formellen Analyse: 'Die Ursache liegt wohl in der mangelnden Kommunikation.'?",
        "options": [
            "vermutlich / wahrscheinlich",
            "ruhig",
            "immerhin",
            "sowieso"
        ],
        "correctAnswer": "vermutlich / wahrscheinlich",
        "explanation": "'Vermutlich/wahrscheinlich' sind die formellen Adverb-Äquivalente zur Modalpartikel 'wohl' und eignen sich für akademische/analytische Texte.",
        "difficulty": "easy",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q071",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Was passiert grammatisch, wenn man versucht, 'ja' in 'Du weißt ja, dass ich das nicht mag.' zu negieren ('*Du weißt nicht ja...')?",
        "options": [
            "Der Satz wird ungrammatisch — Modalpartikeln können nicht negiert werden.",
            "Der Satz bleibt grammatisch korrekt und bedeutungsgleich.",
            "Die Bedeutung kehrt sich einfach ins Gegenteil um.",
            "'Ja' wird dadurch zu einem Fragewort."
        ],
        "correctAnswer": "Der Satz wird ungrammatisch — Modalpartikeln können nicht negiert werden.",
        "explanation": "Dies bestätigt eines der Kern-Diagnosekriterien für Modalpartikeln: Sie sind nicht negierbar, im Gegensatz zu vielen Adverbien.",
        "difficulty": "medium",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q072",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Kannst du mir ______ helfen, den Tisch zu tragen?",
        "options": ["mal", "ruhig", "immerhin", "sowieso"],
        "correctAnswer": "mal",
        "explanation": "'Mal' downtoned hier eine Bitte um Hilfe und macht sie beiläufiger/informeller: 'Kannst du mir mal helfen?' klingt weniger fordernd als ohne Partikel.",
        "difficulty": "easy",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q073",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Welche Aussage zur Verwendung von Modalpartikeln in Prüfungsaufsätzen (Stellungnahme, Bericht) ist am zutreffendsten?",
        "options": [
            "Sie sollten vermieden und durch entsprechende Adverbien/Konnektoren ersetzt werden, da sie zum gesprochenen Register gehören.",
            "Sie sollten in jedem Satz verwendet werden, um Authentizität zu zeigen.",
            "Sie sind in Prüfungsaufsätzen verboten und führen automatisch zu Punktabzug bei jeder Verwendung, unabhängig vom Kontext.",
            "Sie haben in formellen Texten dieselbe Funktion wie in der gesprochenen Sprache."
        ],
        "correctAnswer": "Sie sollten vermieden und durch entsprechende Adverbien/Konnektoren ersetzt werden, da sie zum gesprochenen Register gehören.",
        "explanation": "Modalpartikeln sind kein automatischer 'Fehler', aber ihr gehäufter Einsatz in einem formellen Prüfungsaufsatz senkt den Stilwert — die professionellere Strategie ist die Umschreibung durch Adverbien.",
        "difficulty": "medium",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q074",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Er ist ______ ein bisschen spät dran, aber das ist normal für ihn.",
        "options": ["eben", "denn", "ruhig", "bloß"],
        "correctAnswer": "eben",
        "explanation": "'Eben' präsentiert die Verspätung als typisches, unveränderliches Merkmal der Person — Resignation gegenüber einer bekannten Gewohnheit.",
        "difficulty": "easy",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q075",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Welche Modalpartikel-Kombination aus dieser Lektion würde man am ehesten in einer Fernsehnachrichtensendung NICHT erwarten?",
        "options": ["halt eben mal", "vermutlich (Adverb)", "offensichtlich (Adverb)", "daher (Konnektor)"],
        "correctAnswer": "halt eben mal",
        "explanation": "Gehäufte umgangssprachliche Modalpartikeln wie 'halt eben mal' passen nicht zum formellen Register von Nachrichtensendungen — dort dominieren Adverbien und Konnektoren.",
        "difficulty": "medium",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q076",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Was zeigt der Kontrast zwischen 'Er kommt schon.' (ohne Kontext) und 'Er kommt schon!' (als Antwort auf 'Kommt er überhaupt?')?",
        "options": [
            "Im zweiten Fall bestätigt/beruhigt 'schon' explizit einen geäußerten Zweifel, im ersten ist die Bedeutung ohne Kontext mehrdeutig (temporal oder Modalpartikel möglich).",
            "Es gibt keinen Bedeutungsunterschied.",
            "'Schon' ist im zweiten Satz ein Rechtschreibfehler.",
            "Beide Sätze sind grammatisch unterschiedlich aufgebaut."
        ],
        "correctAnswer": "Im zweiten Fall bestätigt/beruhigt 'schon' explizit einen geäußerten Zweifel, im ersten ist die Bedeutung ohne Kontext mehrdeutig (temporal oder Modalpartikel möglich).",
        "explanation": "Kontext und Betonung entscheiden oft, ob 'schon' als Temporaladverb oder Modalpartikel gelesen wird — ein wichtiger Punkt für das Hörverstehen auf C2-Niveau.",
        "difficulty": "hard",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q077",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Welche Präferenz gilt tendenziell für süddeutsche/österreichische Sprecher bei der Wahl zwischen 'eben' und 'halt'?",
        "options": [
            "Eine Präferenz für 'halt', während norddeutsche Sprecher eher 'eben' bevorzugen.",
            "Eine strikte Ablehnung von 'eben' als falsch.",
            "Keine der beiden Formen wird in Süddeutschland verwendet.",
            "'Halt' wird nur schriftlich verwendet."
        ],
        "correctAnswer": "Eine Präferenz für 'halt', während norddeutsche Sprecher eher 'eben' bevorzugen.",
        "explanation": "Dies ist ein bekanntes dialektal bedingtes Präferenzmuster, relevant für das soziolinguistische Verständnis der Modalpartikeln auf C2-Niveau.",
        "difficulty": "medium",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q078",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Konjunktiv II + 'eigentlich' in 'Ich müsste eigentlich noch einkaufen gehen.' drückt aus:",
        "options": [
            "Eine nicht ausgeführte Verpflichtung/Absicht, oft mit dem Unterton, dass etwas anderes Vorrang hatte.",
            "Eine bereits abgeschlossene Handlung.",
            "Eine strikte, unumstößliche Verpflichtung ohne jede Ausnahme.",
            "Eine Frage nach der Meinung des Gesprächspartners."
        ],
        "correctAnswer": "Eine nicht ausgeführte Verpflichtung/Absicht, oft mit dem Unterton, dass etwas anderes Vorrang hatte.",
        "explanation": "Konjunktiv II mildert die Verpflichtung zu einer moralischen statt zwingenden Notwendigkeit, während 'eigentlich' andeutet, dass die Handlung (noch) nicht ausgeführt wurde.",
        "difficulty": "hard",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q079",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Was für eine Prüfungsfähigkeit trainiert die Unterscheidung von Modalpartikeln-Homonymen (schon/aber/ja) am meisten?",
        "options": [
            "Hörverstehen und Leseverstehen — das Erkennen von Tonfall, Betonung und pragmatischer Absicht des Sprechers.",
            "Ausschließlich die Rechtschreibung.",
            "Die Fähigkeit, lange Wörter auswendig zu lernen.",
            "Die Kenntnis mathematischer Formeln."
        ],
        "correctAnswer": "Hörverstehen und Leseverstehen — das Erkennen von Tonfall, Betonung und pragmatischer Absicht des Sprechers.",
        "explanation": "Modalpartikeln sind vor allem für das Verstehen von Nuancen, Tonfall und impliziten Botschaften relevant — Kernkompetenzen des Hör- und Leseverstehens auf C2-Niveau.",
        "difficulty": "medium",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q080",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Welche Zusammenfassung der Funktion von 'doch' ist am vollständigsten?",
        "options": [
            "Es kann Widerspruch, Nachdruck bei Aufforderungen und Erinnerung mit Vorwurfston ausdrücken, je nach Kontext.",
            "Es bedeutet immer 'jedoch' und ist eine reine Konjunktion.",
            "Es wird nur in Fragen verwendet.",
            "Es hat in jedem Kontext exakt dieselbe Bedeutung."
        ],
        "correctAnswer": "Es kann Widerspruch, Nachdruck bei Aufforderungen und Erinnerung mit Vorwurfston ausdrücken, je nach Kontext.",
        "explanation": "'Doch' ist eine der vielseitigsten Modalpartikeln mit mehreren kontextabhängigen Funktionen — dieses Verständnis ist zentral für C2-Kompetenz.",
        "difficulty": "medium",
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
