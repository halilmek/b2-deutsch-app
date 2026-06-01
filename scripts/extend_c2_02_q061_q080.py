import json

with open('app/src/main/assets/c2_02.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

existing_count = len(data['questions'])
print(f"Existing questions: {existing_count}")

new_questions = [
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welche Konjunktion leitet einen konzessiven Nebensatz ein und bedeutet 'trotz der Tatsache, dass'?",
        "options": [
            "weil",
            "obwohl",
            "damit",
            "indem"
        ],
        "correctAnswer": "obwohl",
        "explanation": "Obwohl is the most common subordinating conjunction introducing concessive clauses in German, expressing that the main clause action occurs despite the condition stated in the subordinate clause.",
        "id": "c2_02_q061"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welcher Satz verwendet die korrekte Wortstellung fuer einen konzessiven Nebensatz mit 'obgleich'?",
        "options": [
            "Obgleich er muede war, er ging weiter.",
            "Obgleich er muede war, ging er weiter.",
            "Obgleich war er muede, ging er weiter.",
            "Er ging weiter, obgleich er war muede."
        ],
        "correctAnswer": "Obgleich er muede war, ging er weiter.",
        "explanation": "In German subordinate clauses introduced by concessive conjunctions like obgleich, the finite verb moves to the end of the clause. When the subordinate clause precedes the main clause, the main clause begins with the verb (inversion).",
        "id": "c2_02_q062"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welche Praeposition verlangt den Genitiv und drueckt eine konzessive Bedeutung aus?",
        "options": [
            "wegen",
            "trotz",
            "durch",
            "fuer"
        ],
        "correctAnswer": "trotz",
        "explanation": "Trotz (+ genitive) is the standard preposition expressing concession in nominal style (e.g., 'trotz des Regens'). Ungeachtet is a more formal synonym also requiring genitive.",
        "id": "c2_02_q063"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welches Adverb verbindet zwei Hauptsaetze mit konzessiver Bedeutung und erfordert Inversion im zweiten Satz?",
        "options": [
            "deshalb",
            "trotzdem",
            "ausserdem",
            "anschliessend"
        ],
        "correctAnswer": "trotzdem",
        "explanation": "Trotzdem is a concessive adverb connecting two main clauses; when placed at position 1, it triggers verb-second word order (inversion) in the clause it introduces.",
        "id": "c2_02_q064"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Welche zweiteilige Konnektor-Struktur drueckt eine konzessive Beziehung zwischen zwei Hauptsaetzen aus?",
        "options": [
            "entweder ... oder",
            "zwar ... aber",
            "je ... desto",
            "nicht nur ... sondern auch"
        ],
        "correctAnswer": "zwar ... aber",
        "explanation": "Zwar...aber is a correlative concessive connector: zwar acknowledges a fact, while aber introduces a contrasting main clause that holds despite that fact.",
        "id": "c2_02_q065"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welcher Satz transformiert 'Obwohl es stark regnete, gingen sie spazieren' korrekt in den Nominalstil?",
        "options": [
            "Wegen des starken Regens gingen sie spazieren.",
            "Trotz des starken Regens gingen sie spazieren.",
            "Durch den starken Regen gingen sie spazieren.",
            "Beim starken Regen gingen sie spazieren."
        ],
        "correctAnswer": "Trotz des starken Regens gingen sie spazieren.",
        "explanation": "Concessive clauses with obwohl transform into prepositional phrases with trotz + genitive noun. 'Es regnete' nominalizes to 'der Regen', yielding 'trotz des starken Regens'.",
        "id": "c2_02_q066"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welche Formulierung ist die gehobenere Alternative zu 'trotz' im akademischen Kontext?",
        "options": [
            "wegen",
            "ungeachtet",
            "anstatt",
            "mithilfe"
        ],
        "correctAnswer": "ungeachtet",
        "explanation": "Ungeachtet (+ genitive) is a formal, literary synonym for trotz, frequently used in academic and legal German to express concession with elevated register.",
        "id": "c2_02_q067"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Wie lautet die korrekte erweiterte Konzessivstruktur mit 'wenn...auch' fuer: 'Auch wenn er sehr talentiert ist, uebt er taeglich'?",
        "options": [
            "Wenn er sehr talentiert auch ist, uebt er taeglich.",
            "Wenn er auch sehr talentiert ist, uebt er taeglich.",
            "Auch ist er sehr talentiert, wenn er uebt taeglich.",
            "Er ist auch sehr talentiert, wenn uebt er taeglich."
        ],
        "correctAnswer": "Wenn er auch sehr talentiert ist, uebt er taeglich.",
        "explanation": "In the wenn...auch construction, auch typically follows the subject or emphasized element within the subordinate clause, while the verb remains in final position.",
        "id": "c2_02_q068"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welcher Satz verwendet die korrekte Struktur mit 'so + Adjektiv + auch'?",
        "options": [
            "So sehr er sich auch bemuehte, der Erfolg blieb aus.",
            "Sehr so er sich auch bemuehte, der Erfolg blieb aus.",
            "Er sich so sehr auch bemuehte, der Erfolg blieb aus.",
            "So auch er sich sehr bemuehte, der Erfolg blieb aus."
        ],
        "correctAnswer": "So sehr er sich auch bemuehte, der Erfolg blieb aus.",
        "explanation": "The correlative concessive structure 'so + adverb/adjective + subject + auch + verb' emphasizes the degree of the concessive condition while maintaining subordinate clause word order.",
        "id": "c2_02_q069"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welche Formulierung mit dem Modalverb 'moegen' im Konjunktiv drueckt eine konzessive Bedeutung aus?",
        "options": [
            "Er mag kommen, ich warte trotzdem.",
            "Mag er auch kommen, ich warte trotzdem.",
            "Moechte er kommen, ich warte trotzdem.",
            "Er moechte auch kommen, ich warte trotzdem."
        ],
        "correctAnswer": "Mag er auch kommen, ich warte trotzdem.",
        "explanation": "The archaic/literary concessive construction 'Mag + subject + auch + infinitive' uses the present subjunctive of moegen to express 'even if/although', with inversion in the main clause.",
        "id": "c2_02_q070"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Wie lautet die korrekte Form mit 'moegen' im Plural fuer eine konzessive Aussage?",
        "options": [
            "Moegen die Gruende auch noch so gewichtig sein, wir bleiben bei unserer Entscheidung.",
            "Moegen auch die Gruende noch so gewichtig sein, wir bleiben bei unserer Entscheidung.",
            "Die Gruende moegen auch noch so gewichtig sein, wir bleiben bei unserer Entscheidung.",
            "Auch moegen die Gruende noch so gewichtig sein, wir bleiben bei unserer Entscheidung."
        ],
        "correctAnswer": "Moegen die Gruende auch noch so gewichtig sein, wir bleiben bei unserer Entscheidung.",
        "explanation": "In formal concessive clauses, moegen (subjunctive plural) + subject + auch + noch so + adjective expresses 'no matter how...'. The word order places auch after the subject for emphasis.",
        "id": "c2_02_q071"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welcher Satz verwendet korrekt eine freie Relativkonstruktion mit konzessiver Bedeutung?",
        "options": [
            "Was er auch sagt, ich glaube ihm nicht.",
            "Was auch er sagt, ich glaube ihm nicht.",
            "Er sagt was auch, ich glaube ihm nicht.",
            "Auch was er sagt, ich glaube ihm nicht."
        ],
        "correctAnswer": "Was er auch sagt, ich glaube ihm nicht.",
        "explanation": "Free relative concessive clauses use question words (was/wer/wie/wann) + subject + auch + verb to mean 'whatever/whoever/however...'. The auch follows the subject within the subordinate clause.",
        "id": "c2_02_q072"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welche Variante ist stilistisch am angemessensten fuer einen wissenschaftlichen Text?",
        "options": [
            "Obwohl die Daten widerspruechlich sind, wird die Hypothese beibehalten.",
            "Trotz widerspruechlicher Daten wird die Hypothese beibehalten.",
            "Die Daten sind widerspruechlich, trotzdem wird die Hypothese beibehalten.",
            "Zwar sind die Daten widerspruechlich, aber die Hypothese wird beibehalten."
        ],
        "correctAnswer": "Trotz widerspruechlicher Daten wird die Hypothese beibehalten.",
        "explanation": "Academic German prefers nominal concessive constructions (trotz + genitive) for conciseness and formality. This structure avoids personal pronouns and maintains objective tone expected at C2 level.",
        "id": "c2_02_q073"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welcher Ausdruck ist KEINE konzessive Konjunktion oder Struktur?",
        "options": [
            "wenngleich",
            "obschon",
            "wiewohl",
            "insofern"
        ],
        "correctAnswer": "insofern",
        "explanation": "Insofern is a causal/consecutive connector meaning 'insofar as' or 'to the extent that', not concessive. Wenngleich, obschon, and wiewohl are all formal synonyms of obwohl.",
        "id": "c2_02_q074"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Wie lautet die korrekte Transformation von 'Auch wenn man alle Risiken bedenkt, ist das Projekt sinnvoll' in gehobenen Stil?",
        "options": [
            "Ungeachtet aller bedachten Risiken ist das Projekt sinnvoll.",
            "Wegen aller bedachten Risiken ist das Projekt sinnvoll.",
            "Durch das Bedenken aller Risiken ist das Projekt sinnvoll.",
            "Beim Bedenken aller Risiken ist das Projekt sinnvoll."
        ],
        "correctAnswer": "Ungeachtet aller bedachten Risiken ist das Projekt sinnvoll.",
        "explanation": "Ungeachtet + genitive is the formal nominal equivalent of auch wenn clauses. The past participle 'bedachten' functions as an adjective modifying 'Risiken' in genitive plural.",
        "id": "c2_02_q075"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welche Aussage zur Verwendung von 'nichtsdestotrotz' ist korrekt?",
        "options": [
            "Es leitet einen Nebensatz ein und verlangt Verb-Endstellung.",
            "Es ist ein Adverb, das zwei Hauptsaetze verbindet und Inversion ausloest.",
            "Es ist eine Praeposition und verlangt den Dativ.",
            "Es ist eine Konjunktion und steht immer am Satzende."
        ],
        "correctAnswer": "Es ist ein Adverb, das zwei Hauptsaetze verbindet und Inversion ausloest.",
        "explanation": "Nichtsdestotrotz is a concessive adverb (like trotzdem, dennoch) that connects main clauses; at position 1, it triggers verb-second word order. It does not introduce subordinate clauses.",
        "id": "c2_02_q076"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welcher Satz demonstriert die korrekte Inversion nach einem vorangestellten konzessiven Nebensatz?",
        "options": [
            "Obwohl die Studie umfangreich war, sie lieferte keine klaren Ergebnisse.",
            "Obwohl die Studie umfangreich war, lieferte sie keine klaren Ergebnisse.",
            "Obwohl war die Studie umfangreich, lieferte sie keine klaren Ergebnisse.",
            "Die Studie war umfangreich, obwohl lieferte sie keine klaren Ergebnisse."
        ],
        "correctAnswer": "Obwohl die Studie umfangreich war, lieferte sie keine klaren Ergebnisse.",
        "explanation": "When a subordinate clause precedes the main clause, German requires inversion: the finite verb of the main clause occupies position 1 immediately after the comma.",
        "id": "c2_02_q077"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Welche Formulierung mit 'ob...oder' hat konzessive Bedeutung?",
        "options": [
            "Ob er kommt oder geht, ist mir egal.",
            "Ob das Wetter gut ist oder nicht, wir machen den Ausflug.",
            "Er fragt, ob wir kommen oder bleiben.",
            "Ich weiß nicht, ob er laechst oder weint."
        ],
        "correctAnswer": "Ob das Wetter gut ist oder nicht, wir machen den Ausflug.",
        "explanation": "The ob...oder construction expresses concession when the main clause action proceeds regardless of the alternative presented. It is paraphrasable as 'unabhaengig davon, ob...'.",
        "id": "c2_02_q078"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welcher Satz verwendet 'gleichwohl' stilistisch korrekt?",
        "options": [
            "Gleichwohl er muede war, arbeitete er weiter.",
            "Er war muede, gleichwohl arbeitete er weiter.",
            "Gleichwohl arbeitete er, er war muede.",
            "Er arbeitete weiter, gleichwohl war er muede."
        ],
        "correctAnswer": "Er war muede, gleichwohl arbeitete er weiter.",
        "explanation": "Gleichwohl is a formal concessive adverb (synonym of dennoch/trotzdem) that connects main clauses. It occupies position 1 or 3 and triggers inversion when at position 1.",
        "id": "c2_02_q079"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welche Transformation ist korrekt: 'Wenn sie auch noch so sehr protestierten, die Entscheidung fiel.'?",
        "options": [
            "So sehr sie auch protestierten, die Entscheidung fiel.",
            "Sehr so sie auch protestierten, die Entscheidung fiel.",
            "Sie protestierten so sehr auch, die Entscheidung fiel.",
            "Auch so sehr protestierten sie, die Entscheidung fiel."
        ],
        "correctAnswer": "So sehr sie auch protestierten, die Entscheidung fiel.",
        "explanation": "The wenn...auch construction with degree emphasis transforms to 'so + adverb + subject + auch + verb' while preserving concessive meaning and subordinate clause word order.",
        "id": "c2_02_q080"
    }
]

data['questions'].extend(new_questions)
data['totalQuestions'] = len(data['questions'])

with open('app/src/main/assets/c2_02.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(new_questions)} questions (q061-q080)")
print(f"Total questions now: {data['totalQuestions']}")
easy = sum(1 for q in data['questions'] if q['difficulty'] == 'easy')
medium = sum(1 for q in data['questions'] if q['difficulty'] == 'medium')
hard = sum(1 for q in data['questions'] if q['difficulty'] == 'hard')
print(f"Difficulty breakdown: easy={easy}, medium={medium}, hard={hard}")