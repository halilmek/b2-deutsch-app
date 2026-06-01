import json

questions = [
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Was drueckt eine Konzessivstruktur grundsaetzlich aus?",
        "options": [
            "Eine Bedingung, ohne die etwas nicht eintreten kann",
            "Einen Gegensatz, bei dem ein Umstand trotz eines anderen gilt",
            "Eine zeitliche Abfolge zweier Ereignisse",
            "Eine Ursache und ihre Wirkung"
        ],
        "correctAnswer": "Einen Gegensatz, bei dem ein Umstand trotz eines anderen gilt",
        "explanation": "Concessive structures express that a result or situation holds true despite an opposing or contradicting circumstance. The core meaning is 'even though / despite the fact that X, Y is still the case.'",
        "id": "c2_02_q001"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welche der folgenden Konjunktionen leitet einen konzessiven Nebensatz ein?",
        "options": [
            "weil",
            "obwohl",
            "damit",
            "sobald"
        ],
        "correctAnswer": "obwohl",
        "explanation": "'Obwohl' (although/even though) is the most common subordinating conjunction introducing a concessive clause in German. 'Weil' is causal, 'damit' is final, and 'sobald' is temporal.",
        "id": "c2_02_q002"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welcher Satz verwendet eine konzessive Struktur?",
        "options": [
            "Er kam nicht, weil er krank war.",
            "Er kam, obwohl er krank war.",
            "Er kam, nachdem er sich erholt hatte.",
            "Er kam, damit er helfen konnte."
        ],
        "correctAnswer": "Er kam, obwohl er krank war.",
        "explanation": "Only 'obwohl er krank war' expresses a concessive relationship: coming (result) despite being sick (opposing circumstance). The other options are causal, temporal, and final respectively.",
        "id": "c2_02_q003"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welche Praeposition kann eine konzessive Bedeutung tragen?",
        "options": [
            "wegen",
            "trotz",
            "durch",
            "seit"
        ],
        "correctAnswer": "trotz",
        "explanation": "'Trotz' (despite/in spite of) is the primary concessive preposition in German, used with the genitive case: 'trotz des schlechten Wetters'. 'Wegen' is causal, 'durch' is instrumental, 'seit' is temporal.",
        "id": "c2_02_q004"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welche der folgenden Konjunktionen hat eine aehnliche konzessive Bedeutung wie 'obwohl'?",
        "options": [
            "falls",
            "wenn auch",
            "indem",
            "seitdem"
        ],
        "correctAnswer": "wenn auch",
        "explanation": "'Wenn auch' (even if/even though) introduces a concessive clause, often with a subjunctive flavour. It is close in meaning to 'obwohl' and 'obgleich', while the others are conditional, instrumental, and temporal.",
        "id": "c2_02_q005"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welche Konjunktion wird verwendet, um einen konzessiven Hauptsatz einzuleiten?",
        "options": [
            "dennoch",
            "obwohl",
            "wenngleich",
            "ungeachtet"
        ],
        "correctAnswer": "dennoch",
        "explanation": "'Dennoch' (nevertheless/yet) is a concessive adverb/conjunction that introduces a main clause and causes verb-subject inversion. 'Obwohl' and 'wenngleich' introduce subordinate clauses. 'Ungeachtet' is a preposition.",
        "id": "c2_02_q006"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Ergaenzen Sie den Satz korrekt: '____ seiner umfangreichen Erfahrung konnte er das Problem nicht loesen.'",
        "options": [
            "Wegen",
            "Trotz",
            "Aufgrund",
            "Mithilfe"
        ],
        "correctAnswer": "Trotz",
        "explanation": "'Trotz' (despite) introduces a concessive prepositional phrase with the genitive. 'Wegen' and 'Aufgrund' are causal (because of), and 'Mithilfe' is instrumental (with the help of). Only 'Trotz' creates the concessive meaning: 'despite his extensive experience.'",
        "id": "c2_02_q007"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welche der folgenden Konstruktionen ist eine konzessive Partizipialkonstruktion?",
        "options": [
            "Da er muede war, schlief er sofort ein.",
            "Obwohl er trainiert hatte, verlor er das Spiel.",
            "Trotz intensiven Trainings verlor er das Spiel.",
            "Weil er gut trainiert war, gewann er das Spiel."
        ],
        "correctAnswer": "Trotz intensiven Trainings verlor er das Spiel.",
        "explanation": "'Trotz intensiven Trainings' is a concessive prepositional phrase (not a participial construction, but the most compressed nominal concessive form). It reduces the full clause 'obwohl er intensiv trainiert hatte' to a noun phrase with a preposition - a key advanced concessive structure.",
        "id": "c2_02_q008"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welches Wort gehoert NICHT zur Gruppe der konzessiven Ausdrucksmittel?",
        "options": [
            "wenngleich",
            "ungeachtet",
            "obschon",
            "infolgedessen"
        ],
        "correctAnswer": "infolgedessen",
        "explanation": "'Infolgedessen' means 'as a result / consequently' and expresses a consecutive or causal-consecutive relationship - the opposite of concessive. 'Wenngleich', 'ungeachtet', and 'obschon' are all concessive expressions.",
        "id": "c2_02_q009"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Formen Sie den Satz um: 'Obwohl das Ergebnis negativ war, setzte das Team die Forschung fort.' Welche Variante ist stilistisch korrekt und konzessiv?",
        "options": [
            "Weil das Ergebnis negativ war, setzte das Team die Forschung fort.",
            "Das Ergebnis war negativ, und das Team setzte die Forschung fort.",
            "Ungeachtet des negativen Ergebnisses setzte das Team die Forschung fort.",
            "Nachdem das Ergebnis negativ war, setzte das Team die Forschung fort."
        ],
        "correctAnswer": "Ungeachtet des negativen Ergebnisses setzte das Team die Forschung fort.",
        "explanation": "'Ungeachtet' (regardless of / notwithstanding) is a formal concessive preposition governing the genitive. This sentence correctly transforms the 'obwohl' clause into a nominal concessive structure, preserving the concessive meaning at C2 register.",
        "id": "c2_02_q010"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welche Variante drueckt eine konzessive Bedeutung mit dem staerksten formellen Register aus?",
        "options": [
            "Aber er kam trotzdem.",
            "Er kam, obwohl er haette wegbleiben koennen.",
            "Wenngleich kein Anlass bestand, erschien er dennoch.",
            "Er kam, weil er wollte."
        ],
        "correctAnswer": "Wenngleich kein Anlass bestand, erschien er dennoch.",
        "explanation": "'Wenngleich' (even though/although) is a formal literary concessive conjunction, more elevated than 'obwohl'. Combined with 'dennoch' in the main clause, this double concessive marking is typical of academic and literary C2 German.",
        "id": "c2_02_q011"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Was ist der grammatikalische Unterschied zwischen 'obwohl' und 'obgleich'?",
        "options": [
            "'Obgleich' steht nur mit dem Konjunktiv II, 'obwohl' nur mit dem Indikativ.",
            "'Obgleich' ist veraltet und wird nicht mehr verwendet.",
            "Beide sind konzessive Subjunktoren mit gleichwertiger Bedeutung, wobei 'obgleich' etwas formeller klingt.",
            "'Obwohl' leitet Hauptsaetze ein, 'obgleich' nur Nebensaetze."
        ],
        "correctAnswer": "Beide sind konzessive Subjunktoren mit gleichwertiger Bedeutung, wobei 'obgleich' etwas formeller klingt.",
        "explanation": "'Obwohl' and 'obgleich' are both subordinating concessive conjunctions with identical grammatical behavior and near-identical meaning. 'Obgleich' (also 'obschon', 'wiewohl') carries a more formal or literary register, making it preferred in academic writing.",
        "id": "c2_02_q012"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Ergaenzen Sie die Luecke: '____ alle Warnungen ignoriert wurden, wurden keine Konsequenzen gezogen.'",
        "options": [
            "Damit",
            "Obschon",
            "Indem",
            "Sodass"
        ],
        "correctAnswer": "Obschon",
        "explanation": "'Obschon' (although/even though) is a formal concessive subordinating conjunction. It correctly introduces the concessive clause here: 'despite the fact that all warnings were ignored, no consequences were drawn.'",
        "id": "c2_02_q013"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welche Konstruktion drueckt eine konzessive Relation durch einen Partizipialsatz aus?",
        "options": [
            "Obwohl er gut vorbereitet war, scheiterte er an der Pruefung.",
            "Gut vorbereitet, scheiterte er dennoch an der Pruefung.",
            "Da er gut vorbereitet war, bestand er die Pruefung.",
            "Er war so gut vorbereitet, dass er die Pruefung bestand."
        ],
        "correctAnswer": "Gut vorbereitet, scheiterte er dennoch an der Pruefung.",
        "explanation": "The participial construction 'Gut vorbereitet, scheiterte er dennoch...' encodes a concessive meaning through the participial phrase implying 'although he was well-prepared'. The adverb 'dennoch' in the main clause signals the concessive contrast. This is a hallmark of elevated C2 academic style.",
        "id": "c2_02_q014"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welche Aussage ueber den Konjunktiv II in konzessiven Saetzen mit 'auch wenn' ist korrekt?",
        "options": [
            "'Auch wenn' verlangt immer den Konjunktiv II.",
            "'Auch wenn' kann sowohl mit dem Indikativ (reale Konzession) als auch mit dem Konjunktiv II (irreale Konzession) verwendet werden.",
            "'Auch wenn' mit Konjunktiv II ist ein Grammatikfehler.",
            "'Auch wenn' steht ausschliesslich in Hauptsaetzen."
        ],
        "correctAnswer": "'Auch wenn' kann sowohl mit dem Indikativ (reale Konzession) als auch mit dem Konjunktiv II (irreale Konzession) verwendet werden.",
        "explanation": "'Auch wenn es regnet, gehen wir spazieren' (indicative = real concession: even if it rains) vs. 'Auch wenn es regnete, wuerden wir spazieren gehen' (Konjunktiv II = hypothetical/irreale concession: even if it were raining). Both are grammatically correct with different nuances.",
        "id": "c2_02_q015"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welche der folgenden konzessiven Strukturen enthaelt eine stilistische oder grammatische Abweichung?",
        "options": [
            "Ungeachtet der Tatsache, dass die Studie kontrovers war, wurde sie veroeffentlicht.",
            "Wenngleich die Ergebnisse widerspruechlich sein sollten, bleibt die Methode valide.",
            "Obwohl dass die Daten fehlerhaft waren, wurden sie verwendet.",
            "So unvollstaendig die Datenlage auch sein mag, lassen sich Tendenzen erkennen."
        ],
        "correctAnswer": "Obwohl dass die Daten fehlerhaft waren, wurden sie verwendet.",
        "explanation": "'Obwohl dass' is a grammatical error: 'obwohl' is already a subordinating conjunction and cannot be combined with 'dass'. The correct form is either 'obwohl die Daten fehlerhaft waren' or 'trotz der Tatsache, dass...'. This double-conjunction error is a common C2 trap.",
        "id": "c2_02_q016"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welche Variante gibt die staerkste konzessive Nuancierung wieder: eine Konzession, die eine Erwartung explizit widerlegt?",
        "options": [
            "Er ist trotzdem gekommen.",
            "Er ist zwar krank, aber er ist gekommen.",
            "Obwohl er todkrank war und alle davon abrieten, erschien er dennoch persoenlich.",
            "Er kam, weil er es fuer richtig hielt."
        ],
        "correctAnswer": "Obwohl er todkrank war und alle davon abrieten, erschien er dennoch persoenlich.",
        "explanation": "This sentence maximizes concessive force through: (1) a strong opposing circumstance ('todkrank'), (2) an additional reinforcing clause ('und alle davon abrieten'), and (3) the redundant adverb 'dennoch' in the main clause - all hallmarks of emphatic concession, a C2-level rhetorical strategy.",
        "id": "c2_02_q017"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Formen Sie den folgenden Satz in eine konzessive Struktur mit 'so ... auch' um: 'Der Plan war schlecht durchdacht. Trotzdem stimmte die Mehrheit zu.'",
        "options": [
            "So schlecht durchdacht der Plan auch war, stimmte die Mehrheit dennoch zu.",
            "Der Plan war so schlecht, dass die Mehrheit zustimmte.",
            "Obwohl der Plan war schlecht, stimmte die Mehrheit trotzdem zu.",
            "So dass der Plan schlecht durchdacht war, stimmte die Mehrheit zu."
        ],
        "correctAnswer": "So schlecht durchdacht der Plan auch war, stimmte die Mehrheit dennoch zu.",
        "explanation": "The 'so ... auch' concessive structure (also called a concessive free relative or 'Exklamativsatz mit konzessiver Funktion') places the gradable adjective after 'so' with 'auch' before or after the verb: 'So schlecht ... auch war'. This is an advanced C2 concessive structure expressing resigned or emphatic concession.",
        "id": "c2_02_q018"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welche der folgenden Umformungen bewahrt die konzessive Bedeutung vollstaendig und ist stilistisch dem akademischen C2-Register angemessen?",
        "options": [
            "Obwohl die finanziellen Mittel begrenzt waren, wurde das Projekt erfolgreich abgeschlossen. -> Das Projekt wurde abgeschlossen, weil die Mittel begrenzt waren.",
            "Obwohl die finanziellen Mittel begrenzt waren, wurde das Projekt erfolgreich abgeschlossen. -> Trotz der Begrenztheit der finanziellen Mittel konnte das Projekt erfolgreich zum Abschluss gebracht werden.",
            "Obwohl die finanziellen Mittel begrenzt waren, wurde das Projekt erfolgreich abgeschlossen. -> Wenn auch die finanziellen Mittel begrenzt waren, so konnte das Projekt dennoch erfolgreich abgeschlossen werden.",
            "Sowohl B als auch C sind korrekte und stilistisch angemessene Umformungen."
        ],
        "correctAnswer": "Sowohl B als auch C sind korrekte und stilistisch angemessene Umformungen.",
        "explanation": "Option B uses 'trotz + Nominalisierung' (a compressed, formal nominal concessive structure), while option C uses 'wenn auch ... so ... dennoch' (a literary concessive correlative structure). Both are correct, semantically equivalent, and appropriate for academic C2 writing. Choosing only B or C misses the full picture.",
        "id": "c2_02_q019"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welche Funktion hat das korrelative Paar 'zwar ... aber' in einem konzessiven Kontext?",
        "options": [
            "Es verbindet zwei gleichwertige Hauptsaetze ohne konzessive Bedeutung.",
            "Es leitet einen irrealen Konditionalsatz ein.",
            "Es raeumt im ersten Glied einen Sachverhalt ein und schraenkt ihn im zweiten Glied ein oder widerlegt ihn teilweise - eine sogenannte einraeumende Adversativstruktur.",
            "Es ersetzt vollstaendig die Funktion von 'obwohl' in formellen Texten."
        ],
        "correctAnswer": "Es raeumt im ersten Glied einen Sachverhalt ein und schraenkt ihn im zweiten Glied ein oder widerlegt ihn teilweise - eine sogenannte einraeumende Adversativstruktur.",
        "explanation": "'Zwar ... aber' is a concessive-adversative correlative: 'zwar' concedes a point ('it is true that / admittedly'), while 'aber' introduces the counter-point. E.g. 'Die Methode ist zwar aufwendig, aber sie liefert zuverlaessige Ergebnisse.' It differs from 'obwohl' in that both clauses are main clauses and the concession is explicitly acknowledged before being qualified.",
        "id": "c2_02_q020"
    }
]

data = {
    "version": "1.0",
    "subjectId": "c2_02",
    "topicName": "Erweiterte Konzessivstrukturen",
    "level": "C2",
    "totalQuestions": len(questions),
    "description": "Erweiterte Konzessivstrukturen im akademischen Diskurs - C2 level concession structures in German. Master advanced concessive conjunctions (obwohl, obgleich, obschon, wenngleich, wenn auch), prepositions (trotz, ungeachtet, mithilfe), correlative pairs (zwar...aber, wenn auch...so...dennoch), participial concessive constructions, 'so...auch' structures, and the Konjunktiv II in hypothetical concessions.",
    "tips": [
        "Konzessiv connectors: obwohl, obgleich, obschon, wenngleich, wenn auch, ungeachtet, trotz, obwohl, trotzdem.",
        "Preposition twins: weil -> aufgrund/wegen; obwohl -> trotz/ungeachtet; wenn -> bei/im Falle.",
        "Correlative pairs: zwar...aber (concessive-adversative); wenn auch...so...dennoch (literary); so...auch (emphatic concession).",
        "Konjunktiv II in concessions: 'Auch wenn es regnete, wuerden wir gehen' (irreale Konzession) vs 'Auch wenn es regnet, gehen wir' (reale).",
        "Avoid: 'obwohl dass' (grammatical error), overloading with dennoch when obwohl already present.",
        "Partizipialkonstruktion: 'Gut vorbereitet, scheiterte er dennoch...' - implies 'obwohl er gut vorbereitet war'.",
        "Nominalstil concession: 'Trotz der Begrenztheit der Mittel...' replaces 'obwohl die Mittel begrenzt waren'."
    ],
    "questions": questions
}

with open('app/src/main/assets/c2_02.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Created c2_02.json with {len(questions)} questions")
easy = sum(1 for q in questions if q['difficulty'] == 'easy')
medium = sum(1 for q in questions if q['difficulty'] == 'medium')
hard = sum(1 for q in questions if q['difficulty'] == 'hard')
print(f"Difficulty breakdown: easy={easy}, medium={medium}, hard={hard}")