import json

questions = [
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welches Partizip wird verwendet, um eine aktive, gleichzeitige Handlung als Attribut auszudrücken?",
        "options": [
            "Partizip I (z. B. 'laufend')",
            "Partizip II (z. B. 'gelaufen')",
            "Infinitiv mit 'zu'",
            "Gerundium"
        ],
        "correctAnswer": "Partizip I (z. B. 'laufend')",
        "explanation": "Partizip I (present participle) expresses active, ongoing, or simultaneous actions when used attributively, e.g., 'der laufende Motor' (= the engine that is running)."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Transformieren Sie den Relativsatz in ein Partizipialattribut: 'Der Mann, der am Fenster steht, winkt.'",
        "options": [
            "Der am Fenster stehende Mann winkt.",
            "Der am Fenster gestandene Mann winkt.",
            "Der am Fenster zu stehende Mann winkt.",
            "Der Mann am Fenster stehend winkt."
        ],
        "correctAnswer": "Der am Fenster stehende Mann winkt.",
        "explanation": "Active relative clauses with present tense verbs are reduced to Partizip I attributes. The participle 'stehend' takes the appropriate adjective ending '-e' to agree with the masculine nominative noun 'Mann'."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welches Partizipialattribut entspricht dem Relativsatz: 'Das Buch, das gestern veroeffentlicht wurde, ist ein Bestseller.'?",
        "options": [
            "Das gestern veroeffentlichte Buch ist ein Bestseller.",
            "Das gestern veroeffentlichende Buch ist ein Bestseller.",
            "Das gestern zu veroeffentlichende Buch ist ein Bestseller.",
            "Das Buch, gestern veroeffentlicht, ist ein Bestseller."
        ],
        "correctAnswer": "Das gestern veroeffentlichte Buch ist ein Bestseller.",
        "explanation": "Passive relative clauses with 'wurde' + Partizip II are reduced to Partizip II attributes. 'Veroeffentlicht' (past participle of 'veroeffentlichen') takes the ending '-e' for neuter nominative singular."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Ergaenzen Sie das Partizipialattribut korrekt: 'Die ____ (ankommen) Gaeste wurden begruesst.'",
        "options": [
            "angekommenen",
            "ankommenden",
            "anzukommenden",
            "angekommene"
        ],
        "correctAnswer": "angekommenen",
        "explanation": "The completed action of arrival requires Partizip II 'angekommen'. The plural accusative noun 'Gaeste' requires the adjective ending '-en' after the definite article 'die'."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welcher Satz enthaelt ein korrektes Partizipialattribut mit erweitertem Attribut?",
        "options": [
            "Der das Buch lesende Student sitzt in der Bibliothek.",
            "Der lesende das Buch Student sitzt in der Bibliothek.",
            "Der Student, das Buch lesend, sitzt in der Bibliothek.",
            "Der Student lesend das Buch sitzt in der Bibliothek."
        ],
        "correctAnswer": "Der das Buch lesende Student sitzt in der Bibliothek.",
        "explanation": "Extended participial attributes place objects/adverbials before the participle. The accusative object 'das Buch' precedes 'lesende', which takes the correct ending for masculine nominative singular."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Wann wird Partizip II als Attribut verwendet?",
        "options": [
            "Bei aktiven, andauernden Handlungen",
            "Bei passiven oder abgeschlossenen Handlungen",
            "Bei zukuenftigen Handlungen mit Modalverben",
            "Bei reflexiven Verben ausschliesslich"
        ],
        "correctAnswer": "Bei passiven oder abgeschlossenen Handlungen",
        "explanation": "Partizip II attributes express completed actions or passive meaning, e.g., 'die geschriebene Arbeit' (= the work that has been written / that was written)."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Transformieren Sie in einen Relativsatz: 'Die von Experten entwickelte Methode ist effektiv.'",
        "options": [
            "Die Methode, die von Experten entwickelt wurde, ist effektiv.",
            "Die Methode, die von Experten entwickelt wird, ist effektiv.",
            "Die Methode, die von Experten entwickelt worden ist, ist effektiv.",
            "Die Methode, die von Experten zu entwickeln ist, ist effektiv."
        ],
        "correctAnswer": "Die Methode, die von Experten entwickelt wurde, ist effektiv.",
        "explanation": "Partizip II attributes with 'von' + agent expand to passive relative clauses in Prateritum ('wurde entwickelt') when describing a completed past action."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welche Adjektivendung ist korrekt? 'Ein ____ (lachen) Kind spielt im Garten.'",
        "options": [
            "lachendes",
            "lachender",
            "lachende",
            "gelachtes"
        ],
        "correctAnswer": "lachendes",
        "explanation": "Partizip I 'lachend' functions as an adjective and requires the ending '-es' for neuter nominative singular after the indefinite article 'ein'."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Identifizieren Sie den stilistisch angemessensten Satz fuer einen wissenschaftlichen Text.",
        "options": [
            "Die Daten, die von uns analysiert wurden, zeigen einen Trend.",
            "Die von uns analysierten Daten zeigen einen Trend.",
            "Wir haben die Daten analysiert, und sie zeigen einen Trend.",
            "Die Daten zeigen einen Trend, nachdem wir sie analysiert haben."
        ],
        "correctAnswer": "Die von uns analysierten Daten zeigen einen Trend.",
        "explanation": "Participial attributes create concise, information-dense noun phrases preferred in academic German. This structure avoids relative clauses while maintaining clarity and formality."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welcher Satz enthaelt einen Fehler im Partizipialattribut?",
        "options": [
            "Die im Labor durchgefuehrten Experimente waren erfolgreich.",
            "Der den Vortrag haltende Professor ist renommiert.",
            "Das zu bearbeitende Problem ist komplex.",
            "Die bearbeitend Problem sind komplex."
        ],
        "correctAnswer": "Die bearbeitend Problem sind komplex.",
        "explanation": "This sentence has two errors: (1) 'bearbeitend' (Partizip I) implies active ongoing action, but 'Problem' cannot actively 'bearbeiten'; (2) missing adjective ending '-e' for plural nominative. Correct: 'Die zu bearbeitenden Probleme' or 'Die bearbeiteten Probleme'."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Wie lautet das Partizipialattribut fuer den Relativsatz mit Modalverb: 'Aufgaben, die erledigt werden muessen.'?",
        "options": [
            "die zu erledigenden Aufgaben",
            "die erledigenden Aufgaben",
            "die erledigten Aufgaben",
            "die zu erledigende Aufgaben"
        ],
        "correctAnswer": "die zu erledigenden Aufgaben",
        "explanation": "Relative clauses with modal verbs expressing necessity ('muessen') transform to 'zu + Partizip I' attributes with passive meaning. The ending '-en' agrees with plural accusative/dative 'Aufgaben'."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welche Transformation ist korrekt? Relativsatz -> Partizipialattribut mit Praepositionalergaenzung: 'Personen, die an dem Projekt beteiligt sind.'",
        "options": [
            "die an dem Projekt beteiligten Personen",
            "die an dem Projekt beteiligenden Personen",
            "die am Projekt zu beteiligenden Personen",
            "die beteiligten Personen an dem Projekt"
        ],
        "correctAnswer": "die an dem Projekt beteiligten Personen",
        "explanation": "Prepositional phrases ('an dem Projekt') remain before the participle in extended attributes. 'Beteiligt' (Partizip II of 'beteiligen') takes the ending '-en' for plural nominative after 'die'."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welcher Unterschied besteht zwischen 'der laufende Prozess' und 'der gelaufene Prozess'?",
        "options": [
            "Keiner; beide sind synonym.",
            "'Laufende' beschreibt einen aktiven, gegenwaertigen Prozess; 'gelaufene' einen abgeschlossenen.",
            "'Gelaufene' ist standardsprachlich korrekt; 'laufende' umgangssprachlich.",
            "'Laufende' ist passiv; 'gelaufene' aktiv."
        ],
        "correctAnswer": "'Laufende' beschreibt einen aktiven, gegenwaertigen Prozess; 'gelaufene' einen abgeschlossenen.",
        "explanation": "Partizip I ('laufend') expresses ongoing action; Partizip II ('gelaufen') expresses completion. This aspectual distinction is crucial for precise meaning in formal German."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Wie lautet die stilistisch elegantere Variante mit Partizipialattribut? 'Ein Vorschlag, der kontrovers diskutiert wird und der neue Impulse geben kann.'",
        "options": [
            "Ein kontrovers diskutierter, neue Impulse gebender Vorschlag",
            "Ein kontrovers diskutierender, neue Impulse zu gebender Vorschlag",
            "Ein zu diskutierender Vorschlag, der neue Impulse geben kann",
            "Ein Vorschlag, kontrovers diskutiert und neue Impulse gebend"
        ],
        "correctAnswer": "Ein kontrovers diskutierter, neue Impulse gebender Vorschlag",
        "explanation": "Multiple participial attributes can be coordinated before a noun. 'Diskutierter' (Partizip II, passive) and 'gebender' (Partizip I, active) correctly reflect the original clause meanings while creating a concise, formal noun phrase."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welche Kasus- und Endungskontrolle ist im Satz korrekt? 'Ich kenne den ____ (von der Kommission empfohlene) Kandidaten.'",
        "options": [
            "von der Kommission empfohlenen",
            "von der Kommission empfohlener",
            "von der Kommission empfehlende",
            "von der Kommission zu empfehlenden"
        ],
        "correctAnswer": "von der Kommission empfohlenen",
        "explanation": "'Kandidaten' is masculine accusative singular. After the definite article 'den', the attributive adjective/participle takes the ending '-en'. 'Empfohlenen' is Partizip II of 'empfehlen', correctly expressing passive recommendation."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Transformieren Sie den komplexen Relativsatz in ein Partizipialattribut: 'Ein System, das automatisch Daten sammelt und sie in Echtzeit analysiert.'",
        "options": [
            "Ein automatisch Daten sammelndes und sie in Echtzeit analysierendes System",
            "Ein Daten automatisch sammelndes und in Echtzeit analysierendes System",
            "Ein System, Daten automatisch sammelnd und in Echtzeit analysierend",
            "Ein zu sammelndes und zu analysierendes Datensystem"
        ],
        "correctAnswer": "Ein automatisch Daten sammelndes und sie in Echtzeit analysierendes System",
        "explanation": "Coordinated active relative clauses transform to coordinated Partizip I attributes. Objects/adverbials precede their respective participles. The ending '-es' agrees with neuter nominative 'System'."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welche Aussage ueber die Wortstellung in erweiterten Partizipialattributen ist korrekt?",
        "options": [
            "Alle Ergaenzungen stehen nach dem Partizip.",
            "Praepositional- und Objektergaenzungen stehen vor dem Partizip; das Partizip steht unmittelbar vor dem Nomen.",
            "Adverbiale stehen immer am Satzanfang, nie im Attribut.",
            "Partizipialattribute duerfen keine Artikel oder Pronomen enthalten."
        ],
        "correctAnswer": "Praepositional- und Objektergaenzungen stehen vor dem Partizip; das Partizip steht unmittelbar vor dem Nomen.",
        "explanation": "In German, extended participial attributes follow a strict order: all modifiers (objects, prepositional phrases, adverbials) precede the participle, which directly precedes the head noun."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Identifizieren Sie den Satz mit korrekter Trennung von Partizip und Praefix im Attribut: 'ein ____ (durchzufuehrender) Test'",
        "options": [
            "ein durchzufuehrender Test",
            "ein durch zu fuehrender Test",
            "ein durchzufuehrender Test",
            "ein durchzufuehrender Test"
        ],
        "correctAnswer": "ein durchzufuehrender Test",
        "explanation": "With separable verbs in 'zu + Partizip I' attributes, 'zu' is inserted between prefix and stem: 'durchfuehren' -> 'durchzufuehrender'. The ending '-er' agrees with masculine nominative singular after 'ein'."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welche Strategie zeigt fortgeschrittene Kompetenz im Umgang mit Partizipialattributen auf C1-Niveau?",
        "options": [
            "Ausschliessliche Verwendung von Relativsaetzen fuer maximale Verstaendlichkeit.",
            "Gezielte Wahl zwischen Relativsatz und Partizipialattribut je nach Fokus, Register und Informationsdichte.",
            "Vermeidung aller erweiterten Attribute zugunsten kurzer Hauptsaetze.",
            "Nutzung von Partizipialattributen nur in muendlichen Pruefungen."
        ],
        "correctAnswer": "Gezielte Wahl zwischen Relativsatz und Partizipialattribut je nach Fokus, Register und Informationsdichte.",
        "explanation": "C1 proficiency includes stylistic flexibility: using participial attributes for conciseness in formal/academic texts, and relative clauses for clarity or emphasis. Strategic selection demonstrates advanced syntactic and rhetorical control."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welches Partizipialattribut ist semantisch und syntaktisch korrekt im Kontext: 'Die ____ (noch zu beruecksichtigenden) Faktoren wurden vergessen.'?",
        "options": [
            "noch zu beruecksichtigenden",
            "noch beruecksichtigenden",
            "noch beruecksichtigten",
            "noch zu beruecksichtigte"
        ],
        "correctAnswer": "noch zu beruecksichtigenden",
        "explanation": "The phrase expresses future necessity ('factors that still need to be considered'), requiring 'zu + Partizip I' with passive meaning. 'Beruecksichtigenden' takes the ending '-en' for plural nominative after 'die'. The adverb 'noch' correctly precedes the infinitive construction."
    }
]


def add_qs(topic_json_path, questions, topic_name_str):
    with open(topic_json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    existing_ids = {q['id'] for q in data['questions'] if 'id' in q}

    added = 0
    for q in questions:
        q_id = q.get('id')
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
