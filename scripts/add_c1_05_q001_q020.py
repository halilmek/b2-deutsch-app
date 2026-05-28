import json

questions = [
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Was ist ein Partizipialattribut?",
        "options": [
            "Ein Nebensatz, der mit 'der', 'die' oder 'das' eingeleitet wird",
            "Ein erweitertes Partizip, das wie ein Adjektiv vor einem Nomen steht",
            "Ein Verb im Infinitiv, das nach einem Nomen steht",
            "Ein Adverb, das ein Verb näher beschreibt"
        ],
        "correctAnswer": "Ein erweitertes Partizip, das wie ein Adjektiv vor einem Nomen steht",
        "explanation": "A Partizipialattribut (participial attribute) is a participle (Partizip I or II) that is expanded with additional elements and placed before a noun, functioning like an adjective. E.g. 'das gestern eingereichte Formular' = 'the form submitted yesterday'."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welche Form ist das Partizip I von 'laufen'?",
        "options": [
            "gelaufen",
            "laufend",
            "gelaufend",
            "laeufend"
        ],
        "correctAnswer": "laufend",
        "explanation": "Partizip I (present participle) is formed by adding '-d' to the infinitive: laufen -> laufend. 'Gelaufen' is Partizip II (past participle). 'Gelaufend' and 'laeufend' do not exist in standard German."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Wandeln Sie den Relativsatz in ein Partizipialattribut um: 'die Frau, die singt'",
        "options": [
            "die gesungene Frau",
            "die singende Frau",
            "die zu singende Frau",
            "die gesungen habende Frau"
        ],
        "correctAnswer": "die singende Frau",
        "explanation": "An active, ongoing action in a relative clause ('die singt') is replaced by Partizip I + adjective ending: 'singend' -> 'die singende Frau'. Partizip I expresses simultaneity with the main clause action."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Wandeln Sie das Partizipialattribut in einen Relativsatz um: 'das reparierte Auto'",
        "options": [
            "das Auto, das repariert",
            "das Auto, das repariert wurde",
            "das Auto, das repariert worden ist",
            "das Auto, das repariert hat"
        ],
        "correctAnswer": "das Auto, das repariert wurde",
        "explanation": "Partizip II of transitive verbs ('repariert') expresses a completed passive action. The relative clause equivalent uses passive voice: 'das repariert wurde'. Both 'wurde' (Priteritum Passiv) and 'worden ist' (Perfekt Passiv) are correct, but 'wurde' is the most natural choice here."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Was drueckt das Partizip I als Attribut aus?",
        "options": [
            "Eine abgeschlossene Handlung in der Vergangenheit",
            "Eine gleichzeitig stattfindende, aktive Handlung",
            "Eine zukuenftige Handlung",
            "Eine Notwendigkeit oder Pflicht"
        ],
        "correctAnswer": "Eine gleichzeitig stattfindende, aktive Handlung",
        "explanation": "Partizip I as an attribute expresses an action happening at the same time as the main clause action (simultaneity) and is active in meaning. E.g. 'der schlafende Hund' = 'the dog that is sleeping' (right now, simultaneously)."
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Ergaenzen Sie das richtige Partizipialattribut: 'die ____ Pakete' (= die Pakete, die ankommen)",
        "options": [
            "angekommenen",
            "ankommenden",
            "anzukommenden",
            "gekommenen"
        ],
        "correctAnswer": "ankommenden",
        "explanation": "Since the packages are in the process of arriving (active, simultaneous action), Partizip I is used: 'ankommen' -> 'ankommend' -> 'die ankommenden Pakete'. 'Angekommenen' (Partizip II) would mean 'the packages that have already arrived'."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Wandeln Sie um: 'der Brief, der gestern geschrieben wurde' -> Partizipialattribut",
        "options": [
            "der gestern schreibende Brief",
            "der gestern geschriebene Brief",
            "der gestern zu schreibende Brief",
            "der gestern geschrieben habende Brief"
        ],
        "correctAnswer": "der gestern geschriebene Brief",
        "explanation": "A passive relative clause ('der geschrieben wurde') is replaced by Partizip II with adjective ending and the adverbial 'gestern' is included in the participial phrase before the noun: 'der gestern geschriebene Brief'. The adverbial always comes before the participle."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Was drueckt 'zu + Partizip I' als Attribut aus?",
        "options": [
            "Eine abgeschlossene Handlung",
            "Eine aktive, gleichzeitige Handlung",
            "Eine Notwendigkeit oder Moeglichkeit (Passiversatzform)",
            "Eine hypothetische Handlung in der Vergangenheit"
        ],
        "correctAnswer": "Eine Notwendigkeit oder Moeglichkeit (Passiversatzform)",
        "explanation": "'Zu + Partizip I' as an attribute is equivalent to 'sein + zu + Infinitiv' or 'koennen/muessen + Passiv'. E.g. 'die zu loesende Aufgabe' = 'die Aufgabe, die geloest werden muss/kann'. It always has a passive meaning."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Wandeln Sie um: 'die Probleme, die noch geloest werden muessen' -> erweitertes Partizipialattribut",
        "options": [
            "die noch geloesten Probleme",
            "die noch loesenden Probleme",
            "die noch zu loesenden Probleme",
            "die noch loesbaren Probleme"
        ],
        "correctAnswer": "die noch zu loesenden Probleme",
        "explanation": "'Zu + Partizip I' ('zu loesend') replaces 'muessen + Passiv' in a relative clause. The adverbial 'noch' is placed before the participial construction: 'die noch zu loesenden Probleme'. This is the standard way to express obligation/possibility in a compressed attributive form."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welche Aussage ueber erweiterte Partizipialattribute ist RICHTIG?",
        "options": [
            "Das Partizip steht immer nach dem Nomen.",
            "Alle Erweiterungen (Adverbien, Objekte, Praepositionalphrasen) stehen zwischen Artikel und Partizip.",
            "Erweiterte Partizipialattribute kommen nur in der gesprochenen Sprache vor.",
            "Das Partizip II kann nicht als erweitertes Attribut verwendet werden."
        ],
        "correctAnswer": "Alle Erweiterungen (Adverbien, Objekte, Praepositionalphrasen) stehen zwischen Artikel und Partizip.",
        "explanation": "In an extended participial attribute, all modifiers (adverbs, objects, prepositional phrases) are placed between the article and the participle, directly before the noun. E.g. 'das [von der Kommission gestern einstimmig verabschiedete] Gesetz'. This creates the typical 'bracket' structure of German nominal phrases."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Wandeln Sie das erweiterte Partizipialattribut in einen Relativsatz um: 'das von allen erwartete Ergebnis'",
        "options": [
            "das Ergebnis, das von allen erwartet",
            "das Ergebnis, das alle erwartend",
            "das Ergebnis, das von allen erwartet wird",
            "das Ergebnis, das alle erwartet haben"
        ],
        "correctAnswer": "das Ergebnis, das von allen erwartet wird",
        "explanation": "Partizip II of transitive verbs ('erwartet') signals a passive meaning. The relative clause equivalent uses 'werden' passiv: 'das von allen erwartet wird'. The agent phrase 'von allen' is retained."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welches Relativpronomen fehlt? 'Das ist die Kollegin, ____ Vorschlag angenommen wurde.'",
        "options": [
            "die",
            "deren",
            "derer",
            "der"
        ],
        "correctAnswer": "deren",
        "explanation": "'Deren' is the genitive form of the relative pronoun for feminine nouns (die Kollegin -> deren). It shows possession: 'whose proposal'. 'Derer' is used in different contexts (demonstrative pronoun). 'Die' and 'der' are nominative/dative forms and do not fit here."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Wandeln Sie um in ein erweitertes Partizipialattribut: 'die Studentin, die seit drei Semestern in Berlin studiert'",
        "options": [
            "die seit drei Semestern in Berlin studierende Studentin",
            "die seit drei Semestern in Berlin studierte Studentin",
            "die in Berlin zu studierende Studentin",
            "die drei Semester studierende Studentin"
        ],
        "correctAnswer": "die seit drei Semestern in Berlin studierende Studentin",
        "explanation": "The relative clause uses an active present verb ('studiert'), so Partizip I ('studierend') is used. The full adverbial phrase 'seit drei Semestern in Berlin' is placed between the article and the participle: 'die [seit drei Semestern in Berlin] studierende Studentin'."
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welches Relativpronomen ist korrekt? 'Das ist das Projekt, ____ wir uns seit Monaten beschäftigen.'",
        "options": [
            "das",
            "mit dem",
            "womit",
            "fuer das"
        ],
        "correctAnswer": "mit dem",
        "explanation": "'Sich beschaeftigen mit' requires the preposition 'mit'. In a relative clause, the preposition must precede the relative pronoun: 'mit dem'. 'Womit' is used in less formal contexts but 'mit dem' is the standard relative clause form here."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Wandeln Sie vollstaendig um: 'das Gesetz, das vom Parlament nach langer Debatte verabschiedet wurde' -> erweitertes Partizipialattribut",
        "options": [
            "das vom Parlament nach langer Debatte verabschiedete Gesetz",
            "das nach langer Debatte verabschiedende Gesetz",
            "das vom Parlament verabschiedete und nach langer Debatte Gesetz",
            "das zu verabschiedende Gesetz vom Parlament"
        ],
        "correctAnswer": "das vom Parlament nach langer Debatte verabschiedete Gesetz",
        "explanation": "The passive relative clause becomes a Partizip II attribute ('verabschiedet' -> 'verabschiedete'). All modifiers ('vom Parlament', 'nach langer Debatte') are inserted between the article and the participle in their original order. The result is a dense but grammatically correct nominal phrase."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welche Umformung ist korrekt? 'die Massnahmen, die ergriffen werden sollen' -> Partizipialattribut",
        "options": [
            "die ergriffenen Massnahmen",
            "die ergreifenden Massnahmen",
            "die zu ergreifenden Massnahmen",
            "die ergreifend zu nehmenden Massnahmen"
        ],
        "correctAnswer": "die zu ergreifenden Massnahmen",
        "explanation": "'Sollen + Passiv' (obligation/intention) in a relative clause is replaced by 'zu + Partizip I' as an attribute: 'zu ergreifend' -> 'die zu ergreifenden Massnahmen'. This construction always signals passive meaning (measures that are to be taken)."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Bestimmen Sie die Bedeutung: 'die noch auszuwertenden Daten'",
        "options": [
            "Die Daten, die bereits ausgewertet wurden",
            "Die Daten, die gerade ausgewertet werden",
            "Die Daten, die noch ausgewertet werden muessen",
            "Die Daten, die ausgewertet werden koennten"
        ],
        "correctAnswer": "Die Daten, die noch ausgewertet werden muessen",
        "explanation": "'Zu + Partizip I' ('auszuwertenden') expresses necessity — the data still needs to be evaluated. The adverb 'noch' reinforces that this has not happened yet. The construction is equivalent to 'Daten, die noch ausgewertet werden muessen' — a passive obligation."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Wandeln Sie um: 'der Wissenschaftler, dessen Theorie die Fachwelt revolutioniert hat' -> korrekte Relativpronomenform und warum?",
        "options": [
            "dessen – Genitiv Maskulinum, zeigt Zugehoerigkeit",
            "deren – Genitiv Femininum, zeigt Zugehoerigkeit",
            "dem – Dativ Maskulinum, nach Praeposition",
            "den – Akkusativ Maskulinum, direktes Objekt"
        ],
        "correctAnswer": "dessen – Genitiv Maskulinum, zeigt Zugehoerigkeit",
        "explanation": "'Dessen' is the genitive masculine relative pronoun, used when the relative clause modifies a noun that belongs to the antecedent (here: 'seine Theorie' -> 'dessen Theorie'). It corresponds to 'whose' in English and signals possession or attribution."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welcher Satz enthaelt ein fehlerhaftes Partizipialattribut?",
        "options": [
            "das von der Jury ausgezeichnete Werk",
            "die seit Jahren diskutierte Frage",
            "der morgen anreisend Delegierte",
            "die zu beruecksichtigenden Faktoren"
        ],
        "correctAnswer": "der morgen anreisend Delegierte",
        "explanation": "The Partizip I used as an attribute must take adjective endings agreeing with the noun in gender, number, and case. 'Anreisend' is missing its ending: it must be 'der morgen anreisende Delegierte'. Without the adjective ending, the construction is ungrammatical."
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Wandeln Sie vollstaendig um in einen Relativsatz: 'die von der Kommission als unzuresichend bewerteten Massnahmen'",
        "options": [
            "die Massnahmen, die die Kommission als unzuresichend bewertet",
            "die Massnahmen, die von der Kommission als unzuresichend bewertet wurden",
            "die Massnahmen, die als unzuresichend von der Kommission bewertet werden",
            "die Massnahmen, welche die Kommission unzuresichend bewertet hatte"
        ],
        "correctAnswer": "die Massnahmen, die von der Kommission als unzuresichend bewertet wurden",
        "explanation": "The Partizip II ('bewerteten') signals a completed passive action. The relative clause equivalent uses Passiv Prateritum: 'die ... bewertet wurden'. The agent phrase 'von der Kommission' and the predicative complement 'als unzuresichend' are both retained in the relative clause."
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
