import json

# Load existing c2_01.json
with open('app/src/main/assets/c2_01.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Count existing questions
existing_count = len(data['questions'])
print(f"Existing questions: {existing_count}")

# New questions to add (q021-q040)
new_questions = [
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Die Regierung entschied, die Steuern zu senken. Wie lautet die Transformation in den Nominalstil?\nDie Regierung traf die ____ zur Steuersenkung.",
        "options": [
            "Entscheidung",
            "Entscheidungsfindung",
            "Entschlossenheit",
            "Entscheiden"
        ],
        "correctAnswer": "Entscheidung",
        "explanation": "The verb 'entscheiden' is transformed into its corresponding noun 'die Entscheidung' (decision). It forms a typical functional verb construction (Funktionsverbgefüge): 'eine Entscheidung treffen'.",
        "id": "c2_01_q021"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Weil die Fallzahlen rasant ansteigen, müssen die Maßnahmen verschärft werden.\nNominalstil: Aufgrund des rasanten ____ der Fallzahlen ist eine Verschärfung der Maßnahmen erforderlich.",
        "options": [
            "Anstiegs",
            "Ansteigen",
            "Anwachsens",
            "Anstiegen"
        ],
        "correctAnswer": "Anstiegs",
        "explanation": "The subclause introduced by 'Weil' is replaced by the preposition 'Aufgrund' (which requires the genitive case). The verb 'anstiegen' becomes the masculine noun 'der Anstieg', which takes the genitive ending '-es' ('des rasanten Anstiegs').",
        "id": "c2_01_q022"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Obwohl das Budget knapp war, wurde das Forschungsprojekt erfolgreich abgeschlossen.\nNominalstil: ____ des knappen Budgets konnte das Forschungsprojekt erfolgreich abgeschlossen werden.",
        "options": [
            "Trotz",
            "Wegen",
            "Ungeachtet",
            "Infolge"
        ],
        "correctAnswer": "Trotz",
        "explanation": "The concessive subclause connector 'Obwohl' (although) translates to the concessive preposition 'Trotz' (despite) in nominal style, which is followed here by the genitive case.",
        "id": "c2_01_q023"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Der Professor fordert, dass die Studierenden pünktlich abgeben.\nNominalstil: Der Professor fordert die pünktliche ____ der Studierenden.",
        "options": [
            "Abgabe",
            "Abgebung",
            "Abgeben",
            "Aufgabe"
        ],
        "correctAnswer": "Abgabe",
        "explanation": "The object clause (dass-Satz) is compressed into a noun phrase. The verb 'abgeben' turns into the feminine noun 'die Abgabe'.",
        "id": "c2_01_q024"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Wenn man die Daten präzise analysiert, lassen sich Fehler vermeiden.\nNominalstil: Bei ____ Analyse der Daten lassen sich Fehler vermeiden.",
        "options": [
            "präziser",
            "präzise",
            "präzisen",
            "präzises"
        ],
        "correctAnswer": "präziser",
        "explanation": "The conditional clause with 'Wenn' is replaced by the preposition 'Bei' + dative. 'Analyse' is feminine, so 'präzise' takes the dative feminine ending '-er' (Bei präziser Analyse).",
        "id": "c2_01_q025"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Nachdem das Experiment beendet worden war, wertete das Team die Ergebnisse aus.\nNominalstil: Nach ____ des Experiments erfolgte die Auswertung der Ergebnisse durch das Team.",
        "options": [
            "Beendigung",
            "Beenden",
            "Beendens",
            "Abschließen"
        ],
        "correctAnswer": "Beendigung",
        "explanation": "'Nachdem' is a temporal conjunction translated into the preposition 'Nach' (+ dative). The noun 'Beendigung' (termination/completion) is preferred in high-level academic German over the nominalized infinitive 'Beenden'.",
        "id": "c2_01_q026"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Die Forscher untersuchten, wie das Virus übertragen wird.\nNominalstil: Die Forscher widmeten sich der Untersuchung des ____ des Virus.",
        "options": [
            "Übertragungsweges",
            "Übertragens",
            "Übertragungsweg",
            "Übertragungsart"
        ],
        "correctAnswer": "Übertragungsweges",
        "explanation": "In academic German, dependent interrogative clauses (wie...) are often transformed using compound nouns to increase precision. 'Wie das Virus übertragen wird' becomes 'des Übertragungsweges des Virus' (the transmission route of the virus) in the genitive case.",
        "id": "c2_01_q027"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Er betonte noch einmal, dass diese Entdeckung von großer Bedeutung ist.\nNominalstil: Er hob die große ____ dieser Entdeckung erneut hervor.",
        "options": [
            "Bedeutsamkeit",
            "Bedeutung",
            "Bedeuten",
            "Wichtigkeit"
        ],
        "correctAnswer": "Bedeutung",
        "explanation": "The phrase 'von großer Bedeutung sein' is nominalized into 'die große Bedeutung'. While 'Bedeutsamkeit' exists, 'Bedeutung' is the standard, precise choice in academic discourse for this specific context.",
        "id": "c2_01_q028"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Man muss berücksichtigen, dass die Probanden unterschiedlich alt sind.\nNominalstil: Die Berücksichtigung des ____ der Probanden ist zwingend erforderlich.",
        "options": [
            "unterschiedlichen Alters",
            "unterschiedliche Alter",
            "unterschiedlichem Alter",
            "Altersunterschieds"
        ],
        "correctAnswer": "unterschiedlichen Alters",
        "explanation": "The noun 'Alter' is neuter (das Alter). In the genitive attribute structure following 'Berücksichtigung des...', the adjective takes the weak ending '-en' and the noun takes '-s': 'des unterschiedlichen Alters'.",
        "id": "c2_01_q029"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Das Phänomen lässt sich dadurch erklären, dass die Temperaturen kontinuierlich steigen.\nNominalstil: Die Erklärung des Phänomens liegt im ____ Temperaturanstieg.",
        "options": [
            "kontinuierlichen",
            "kontinuierlicher",
            "kontinuierliche",
            "kontinuierlich"
        ],
        "correctAnswer": "kontinuierlichen",
        "explanation": "The causal clause is nominalized using a compound noun ('Temperaturanstieg', masculine). It is preceded by the prepositional contraction 'im' (in dem = dative). Therefore, the adjective 'kontinuierlich' needs the weak dative masculine ending '-en'.",
        "id": "c2_01_q030"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Indem man die Parameter modifiziert, kann das Ergebnis optimiert werden.\nNominalstil: ____ eine Modifikation der Parameter lässt sich das Ergebnis optimieren.",
        "options": [
            "Durch",
            "Mittels",
            "Mithilfe",
            "Dank"
        ],
        "correctAnswer": "Durch",
        "explanation": "The modal subclause introduced by 'Indem' indicates a method or instrument. In academic nominal style, this is standardly replaced by 'Durch' (+ accusative). While 'Mittels' or 'Mithilfe' can express means, they require the genitive case, which doesn't match 'eine Modifikation' (accusative/feminine).",
        "id": "c2_01_q031"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Der Bericht kritisiert, wie die Behörden mit der Krise umgegangen sind.\nNominalstil: Der Bericht übt Kritik am ____ der Behörden mit der Krise.",
        "options": [
            "Umgang",
            "Umgangen",
            "Umgehen",
            "Umgangsweise"
        ],
        "correctAnswer": "Umgang",
        "explanation": "The idiom 'Kritik üben an' combines with the masculine noun 'der Umgang' (derived from umgehen). Fixed contraction: 'am' (an dem) + dative singular 'Umgang'.",
        "id": "c2_01_q032"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Die Volkswirtschaft bricht zusammen, falls die Notenbank die Zinsen drastisch anhebt.\nNominalstil: Im Falle einer drastischen ____ durch die Notenbank droht der Zusammenbruch der Volkswirtschaft.",
        "options": [
            "Zinsanhebung",
            "Zinserhöhung",
            "Zinssteigerung",
            "Zinsanhebens"
        ],
        "correctAnswer": "Zinsanhebung",
        "explanation": "To match 'drastischen' (feminine genitive ending '-en' following 'einer'), we need a feminine noun. Academic German prefers exact technical terms like 'Zinsanhebung' over nominalized infinitives like 'Zinsanhebens'.",
        "id": "c2_01_q033"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Die Absicht der Studie ist es, herauszufinden, welche Faktoren das Konsumverhalten beeinflussen.\nNominalstil: Die Studie zielt auf die ____ der Einflussfaktoren auf das Konsumverhalten ab.",
        "options": [
            "Ermittlung",
            "Herausfindung",
            "Feststellbarkeit",
            "Ermitteln"
        ],
        "correctAnswer": "Ermittlung",
        "explanation": "In high-level academic German (C2), colloquial or literal translations of verbs like 'herausfinden' are replaced by formal terminology such as 'die Ermittlung' (investigation/determination) or 'die Identifikation'. 'Herausfindung' is not standard German.",
        "id": "c2_01_q034"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Bevor die neue Software implementiert wird, muss die IT-Infrastruktur gründlich überprüft werden.\nNominalstil: Der Implementierung der neuen Software muss eine ____ Überprüfung der IT-Infrastruktur vorausgehen.",
        "options": [
            "eingehende",
            "gründlich",
            "vollzogene",
            "vorausgegangene"
        ],
        "correctAnswer": "eingehende",
        "explanation": "To elevate the text to a C2 academic level, synonyms like 'eingehend' or 'tiefgreifend' are preferred over the basic word 'gründlich'. The adjective must match the feminine accusative/nominative slot here ('eine eingehende Überprüfung').",
        "id": "c2_01_q035"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Weil die Ressourcen knapp sind, verteilen sich die Investitionen ungleichmäßig auf die Regionen.\nNominalstil: Die Ressourcenknappheit ____ zu einer ungleichmäßigen Verteilung der Investitionen auf die Regionen.",
        "options": [
            "führt",
            "bedingt",
            "verursacht",
            "resultiert"
        ],
        "correctAnswer": "führt",
        "explanation": "When shifting into nominal style, verbs are downsized to functional connectors. 'Die Ressourcenknappheit führt zu...' perfectly integrates the prepositional object 'zu einer...'. 'Bedingt' and 'verursacht' would require a direct accusative object.",
        "id": "c2_01_q036"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Man vermutet, dass die Zielgruppe das Produkt ablehnt, weil der Preis zu hoch angesetzt wurde.\nNominalstil: Die vermutete Produktablehnung seitens der Zielgruppe ____ auf der zu hohen Preissetzung.",
        "options": [
            "basiert",
            "beruht",
            "folgt",
            "stammt"
        ],
        "correctAnswer": "beruht",
        "explanation": "The causal relationship ('weil') is expressed via the verbal structure 'beruht auf' (+ dative). 'Basiert' usually takes 'auf' but is less idiomatic for direct causal roots here; 'beruhen auf' means 'to be caused by / due to'.",
        "id": "c2_01_q037"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Dadurch, dass der Autor historische Dokumente akribisch auswertete, konnte er die These untermauern.\nNominalstil: Die akribische ____ historischer Dokumente ermöglichte dem Autor die Untermauerung der These.",
        "options": [
            "Auswertung",
            "Evaluierung",
            "Analyse",
            "Rezeption"
        ],
        "correctAnswer": "Auswertung",
        "explanation": "The exact nominal counterpart to the verb 'auswerten' is 'die Auswertung'. While 'Analyse' and 'Evaluierung' are academic, 'Auswertung' preserves the precise meaning of extracting data from existing documents.",
        "id": "c2_01_q038"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Es ist notwendig, dass alle Beteiligten eng zusammenarbeiten, damit das Projekt gelingt.\nNominalstil: Die enge Zusammenarbeit aller Beteiligten ist eine zwingende ____ für das Gelingen des Projekts.",
        "options": [
            "Voraussetzung",
            "Notwendigkeit",
            "Bedingung",
            "Folge"
        ],
        "correctAnswer": "Voraussetzung",
        "explanation": "The final clause ('damit das Projekt gelingt') implies a prerequisite. In academic German, 'eine zwingende Voraussetzung' (a mandatory prerequisite) is a fixed collocated phrase used to compress conditional/final dependencies.",
        "id": "c2_01_q039"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Das Gesetz gilt erst dann, wenn es im Bundesgesetzblatt veröffentlicht wird.\nNominalstil: Die Rechtsgültigkeit des Gesetzes ____ erst mit dessen Veröffentlichung im Bundesgesetzblatt ein.",
        "options": [
            "tritt",
            "setzt",
            "folgt",
            "beginnt"
        ],
        "correctAnswer": "tritt",
        "explanation": "This targets nominalized legal jargon at C2 level. The expression 'in Kraft treten' or 'Rechtsgültigkeit tritt ein' uses the separable verb 'eintreten'. Therefore, 'tritt... ein' is the correct functional verb.",
        "id": "c2_01_q040"
    }
]

# Add new questions
data['questions'].extend(new_questions)
data['totalQuestions'] = len(data['questions'])

# Save
with open('app/src/main/assets/c2_01.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(new_questions)} questions (q021-q040)")
print(f"Total questions now: {data['totalQuestions']}")
easy = sum(1 for q in data['questions'] if q['difficulty'] == 'easy')
medium = sum(1 for q in data['questions'] if q['difficulty'] == 'medium')
hard = sum(1 for q in data['questions'] if q['difficulty'] == 'hard')
print(f"Difficulty breakdown: easy={easy}, medium={medium}, hard={hard}")