import json

with open('app/src/main/assets/c2_02.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

existing_count = len(data['questions'])
print(f"Existing questions: {existing_count}")

# New questions q021-q060
new_questions = [
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "____ das Testergebnis auch ausfallen mag, wir muessen das Projekt in jedem Fall fortfuehren.",
        "options": [
            "Wie",
            "Wie auch immer",
            "Wie immer",
            "Inwiefern"
        ],
        "correctAnswer": "Wie auch immer",
        "explanation": "The formula 'Wie [adjective] auch [verb] mag' or 'Wie auch immer... mag' expresses an unconditional concession ('no matter how...'). 'Wie auch immer' fits perfectly with the inflected verb 'ausfallen mag' at the end of the clause.",
        "id": "c2_02_q021"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Er ging das Risiko ein, ____ er sich der drohenden Konsequenzen vollkommen bewusst war.",
        "options": [
            "wiewohl",
            "obgleich",
            "wennschon",
            "ungeachtet"
        ],
        "correctAnswer": "wiewohl",
        "explanation": "'Wiewohl' is an elevated, literary synonym for 'obwohl' (although) frequently tested at C2 level to introduce subordinate concessive clauses with verb-final placement.",
        "id": "c2_02_q022"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Es wurden keine signifikanten Fortschritte erzielt, ____ die Forscher Tag und Nacht arbeiteten.",
        "options": [
            "sosehr",
            "wie sehr",
            "wenngleich",
            "trotzdem"
        ],
        "correctAnswer": "sosehr",
        "explanation": "'Sosehr' means 'no matter how much' or 'even though... very much'. It quantifies the intensity of the action in the concessive clause and functions as a subordinating conjunction.",
        "id": "c2_02_q023"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "____ anstrengend die Forschungsarbeit auch sein mag, das Team gibt nicht auf.",
        "options": [
            "So",
            "Wie",
            "Obgleich",
            "Trotzdem"
        ],
        "correctAnswer": "So",
        "explanation": "The concessive structure 'So + Adjective + auch + Verb' functions as an advanced concession meaning 'no matter how adjective'. Here, it patterns perfectly as 'So anstrengend die Forschungsarbeit auch sein mag'.",
        "id": "c2_02_q024"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Die Reform wird durchgefuehrt, ____ es heftigen Widerstand aus der Bevoelkerung gibt.",
        "options": [
            "wennschon",
            "ungeachtet",
            "trotz",
            "wiewohl"
        ],
        "correctAnswer": "wennschon",
        "explanation": "'Wennschon' is an advanced, formal alternative to 'obwohl'. It introduces a verbal subordinate clause, whereas 'ungeachtet' and 'trotz' are prepositions that would require a nominal structure.",
        "id": "c2_02_q025"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "____ alle Beteiligten ihr Bestes gaben, konnte das gesteckte Saisonziel nicht mehr realisiert werden.",
        "options": [
            "Wenngleich",
            "Ungeachtet",
            "Trifft",
            "Sosehr"
        ],
        "correctAnswer": "Wenngleich",
        "explanation": "'Wenngleich' acts as a high-register subordinating conjunction introducing a complete concessive subclause with the verb ('gaben') at the very end.",
        "id": "c2_02_q026"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Wir halten an unserem Investitionsplan fest – ____ die Zinsen in den kommenden Monaten noch weiter steigen.",
        "options": [
            "sollten",
            "wenn auch",
            "wenngleich",
            "obschon"
        ],
        "correctAnswer": "sollten",
        "explanation": "This is a condition-based concession using a verb-first subclause without a conjunction ('sollten die Zinsen...'). It functions like 'selbst wenn die Zinsen... steigen sollten'.",
        "id": "c2_02_q027"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "____ der massiven Kritik seitens der Opposition hielt die Regierung an ihrem Kurs fest.",
        "options": [
            "Ungeachtet",
            "Obschon",
            "Wiewohl",
            "Trotzdem"
        ],
        "correctAnswer": "Ungeachtet",
        "explanation": "'Ungeachtet' is an advanced preposition requiring the genitive case ('der massiven Kritik'). The other options are either conjunctions for verbal clauses or connectors requiring inversion.",
        "id": "c2_02_q028"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Mag die oekonomische Lage auch noch ____ prekaer sein, das Unternehmen entlässt keine Mitarbeiter.",
        "options": [
            "so",
            "wie",
            "mehr",
            "sehr"
        ],
        "correctAnswer": "so",
        "explanation": "The fixed double-bracket structure 'Mag... auch noch so + Adjective + sein' is an advanced alternative to express 'no matter how critical the economic situation might be'.",
        "id": "c2_02_q029"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "____ Gefahren auch auf uns lauern moegen, wir werden die Expedition keinesfalls abbrechen.",
        "options": [
            "Welche",
            "Was fuer",
            "Wie viele",
            "Einige"
        ],
        "correctAnswer": "Welche",
        "explanation": "When dealing with abstract or plural nouns in an extended concessive structure ('...auch lauern moegen'), 'Welche + Noun + auch immer/moegen' is used to define an all-inclusive, unconditional concession.",
        "id": "c2_02_q030"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Er weigerte sich, den Vertrag zu unterzeichnen, ____ ihm die Chefetage weitreichende Zugestaendnisse gemacht hatte.",
        "options": [
            "obschon",
            "waehrend",
            "trotz",
            "demnach"
        ],
        "correctAnswer": "obschon",
        "explanation": "'Obschon' is a classic C2-level concessive conjunction meaning 'although', integrating smoothly with the subordinate clause structure and final verb placement.",
        "id": "c2_02_q031"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "____ man das Problem auch dreht und wendet, es laesst sich im Moment keine optimale Loesung finden.",
        "options": [
            "Wie",
            "So",
            "Sosehr",
            "Obgleich"
        ],
        "correctAnswer": "Wie",
        "explanation": "The common modal-concessive idiomatic phrase is 'Wie man es auch dreht und wendet' ('no matter which way you look at it / turn it'). It requires 'Wie' at the front of the clause.",
        "id": "c2_02_q032"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Das Gesetz tritt am ersten Januar in Kraft, ____ noch offene Detailfragen im Ausschuss geklaert sind oder nicht.",
        "options": [
            "ob",
            "sofern",
            "wiewohl",
            "falls"
        ],
        "correctAnswer": "ob",
        "explanation": "An alternative double-sided concession ('whether... or not') uses 'ob... oder nicht' to indicate that the outcome is completely decoupled from the condition.",
        "id": "c2_02_q033"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "____ schmerzvoll diese Einsicht fuer das gesamte Management auch sein mag: Die Neuausrichtung ist alternativlos.",
        "options": [
            "Wie sehr",
            "So",
            "Obschon",
            "Gleichwohl"
        ],
        "correctAnswer": "So",
        "explanation": "This structure relies on 'So + Adjective... auch... mag'. It provides a highly stylistic, academic way to grant a point while enforcing the main clause statement.",
        "id": "c2_02_q034"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "____ reich er sein mag, echtes Glueck kann er sich mit all seinem Vermoegen nicht kaufen.",
        "options": [
            "So",
            "Wie",
            "Obgleich",
            "Wenngleich"
        ],
        "correctAnswer": "Wie",
        "explanation": "'Wie + Adjective + Subject + auch + verb + mag' is a formal, syntax-strict variant of the concessive format. Note that 'auch' is omitted in the prompt's placeholder structure, which is structurally permitted when 'Wie' initiates the clause directly.",
        "id": "c2_02_q035"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Die Verhandlungen wurden abgebrochen. ____ betonte der Sprecher, dass man im Dialog bleiben wolle.",
        "options": [
            "Gleichwohl",
            "Demzufolge",
            "Wiewohl",
            "Nichtsdestotrotz"
        ],
        "correctAnswer": "Gleichwohl",
        "explanation": "'Gleichwohl' functions here as a concessive adverb (conjunct) positioned in position 1 of the main sentence, triggering inversion ('betonte der Sprecher'). 'Wiewohl' would require subclause verb-final ordering.",
        "id": "c2_02_q036"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Und ____ die Sanierung des Altbaus Unmengen an Kapital verschlingen sollte, wir ziehen das jetzt durch.",
        "options": [
            "wenn",
            "obschon",
            "wenngleich",
            "falls"
        ],
        "correctAnswer": "wenn",
        "explanation": "'Und wenn...' combined with a subjunctive or intensive helper ('sollte') creates a highly emphatic hypothetical concessive clause ('Even if it should devour...').",
        "id": "c2_02_q037"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Es wurden keine nennenswerten Maengel dokumentiert, ____ man die Anlage einer peinlich genauen Inspektion unterzog.",
        "options": [
            "obzwar",
            "ungeachtet",
            "trotzdem",
            "sonst"
        ],
        "correctAnswer": "obzwar",
        "explanation": "'Obzwar' is a highly advanced, slightly archaic but entirely correct concessive subordinating conjunction seen in high-tier academic texts or C2 structures testing ultimate vocabulary depth.",
        "id": "c2_02_q038"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Man warf ihm Urkundenfaelschung vor, ____ er sich vehement zur Wehr setzte.",
        "options": [
            "wogegen",
            "obgleich",
            "wohingegen",
            "trotz dessen"
        ],
        "correctAnswer": "wogegen",
        "explanation": "This displays a relative concessive / adversative hybrid. 'Wogegen' fields the action of defending oneself directly against the prior accusation phrase ('sich wehren gegen etwas').",
        "id": "c2_02_q039"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Die Expedition scheiterte schlussendlich, ____ alle erdenklichen Sicherheitsvorkehrungen im Vorfeld getroffen worden waren.",
        "options": [
            "obgleich doch",
            "obgleich",
            "ungeachtet",
            "trotzdem"
        ],
        "correctAnswer": "obgleich doch",
        "explanation": "Adding particles like 'doch' or 'auch' directly to 'obgleich' creates an intensified, emphatic concessive balance ('obgleich doch...'), highlighting the deep paradox between safety steps and total failure.",
        "id": "c2_02_q040"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "____ erheblicher finanzieller Schwierigkeiten konnte das Forschungsprojekt erfolgreich abgeschlossen werden.",
        "options": [
            "Trotz",
            "Wegen",
            "Dank",
            "Aufgrund"
        ],
        "correctAnswer": "Trotz",
        "explanation": "'Trotz' introduces a concessive relationship, meaning 'despite'.",
        "id": "c2_02_q041"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "____ die Ergebnisse zunaechst vielversprechend erschienen, wurde die Studie nicht veroeffentlicht.",
        "options": [
            "Obwohl",
            "Weil",
            "Sodass",
            "Nachdem"
        ],
        "correctAnswer": "Obwohl",
        "explanation": "'Obwohl' is the standard concessive conjunction meaning 'although'.",
        "id": "c2_02_q042"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "Die Massnahme wurde umgesetzt, ____ erheblicher Kritik aus Fachkreisen.",
        "options": [
            "ungeachtet",
            "aufgrund",
            "mittels",
            "infolge"
        ],
        "correctAnswer": "ungeachtet",
        "explanation": "'Ungeachtet' is a formal concessive preposition commonly used in academic and official texts.",
        "id": "c2_02_q043"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "____ die Beweislage eindeutig war, bestanden weiterhin Zweifel an der Interpretation.",
        "options": [
            "Obgleich",
            "Weil",
            "Sobald",
            "Waehrend"
        ],
        "correctAnswer": "Obgleich",
        "explanation": "'Obgleich' is a formal alternative to 'obwohl'.",
        "id": "c2_02_q044"
    },
    {
        "difficulty": "easy",
        "type": "multiple_choice",
        "questionText": "____ aller BemuEhungen konnte keine Einigung erzielt werden.",
        "options": [
            "Trotz",
            "Wegen",
            "Dank",
            "Auf"
        ],
        "correctAnswer": "Trotz",
        "explanation": "'Trotz aller Bemuehungen' is a common concessive expression.",
        "id": "c2_02_q045"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "____ der Autor ueberzeugende Argumente vorbrachte, blieb die Kritik bestehen.",
        "options": [
            "Wenngleich",
            "Da",
            "Sodass",
            "Indem"
        ],
        "correctAnswer": "Wenngleich",
        "explanation": "'Wenngleich' is a sophisticated concessive conjunction often used at C2 level.",
        "id": "c2_02_q046"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Die Theorie wird weiterhin diskutiert, ____ sie bereits mehrfach widerlegt wurde.",
        "options": [
            "obschon",
            "weil",
            "nachdem",
            "damit"
        ],
        "correctAnswer": "obschon",
        "explanation": "'Obschon' is a formal concessive connector equivalent to 'although'.",
        "id": "c2_02_q047"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "____ die Datenlage begrenzt ist, lassen sich gewisse Schlussfolgerungen ziehen.",
        "options": [
            "Auch wenn",
            "Weil",
            "Sobald",
            "Seitdem"
        ],
        "correctAnswer": "Auch wenn",
        "explanation": "'Auch wenn' expresses concession and possibility.",
        "id": "c2_02_q048"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "____ intensiver Verhandlungen scheiterte das Vorhaben letztlich.",
        "options": [
            "Ungeachtet",
            "Wegen",
            "Mangels",
            "Aufgrund"
        ],
        "correctAnswer": "Ungeachtet",
        "explanation": "'Ungeachtet' means 'regardless of' and expresses concession.",
        "id": "c2_02_q049"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "Die Studie gilt als relevant, ____ methodische Schwächen nicht zu uebersehen sind.",
        "options": [
            "selbst wenn",
            "weil",
            "da",
            "sobald"
        ],
        "correctAnswer": "selbst wenn",
        "explanation": "'Selbst wenn' introduces a strong concessive condition.",
        "id": "c2_02_q050"
    },
    {
        "difficulty": "medium",
        "type": "multiple_choice",
        "questionText": "____ man die Gegenargumente beruecksichtigt, bleibt die Grundannahme plausibel.",
        "options": [
            "Selbst wenn",
            "Falls",
            "Weil",
            "Nachdem"
        ],
        "correctAnswer": "Selbst wenn",
        "explanation": "'Selbst wenn' emphasizes that the result remains unchanged despite a hypothetical circumstance.",
        "id": "c2_02_q051"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "____ der erheblichen Komplexitaet des Sachverhalts gelang eine nachvollziehbare Darstellung.",
        "options": [
            "Ungeachtet",
            "Infolge",
            "Mangels",
            "Aufgrund"
        ],
        "correctAnswer": "Ungeachtet",
        "explanation": "'Ungeachtet der Komplexitaet' is a highly formal concessive construction.",
        "id": "c2_02_q052"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welche Variante drueckt die staerkste Konzession aus?",
        "options": [
            "obwohl",
            "auch wenn",
            "selbst wenn",
            "da"
        ],
        "correctAnswer": "selbst wenn",
        "explanation": "'Selbst wenn' often expresses the strongest concessive meaning because the outcome remains valid even under extreme conditions.",
        "id": "c2_02_q053"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "____ die Evidenzlage eindeutig gegen diese These spricht, findet sie weiterhin Anhänger.",
        "options": [
            "Obgleich",
            "Nachdem",
            "Waehrend",
            "Sobald"
        ],
        "correctAnswer": "Obgleich",
        "explanation": "'Obgleich' introduces a formal concessive relationship.",
        "id": "c2_02_q054"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Die Entscheidung wurde getroffen, ____ zahlreiche Experten davor gewarnt hatten.",
        "options": [
            "obwohl",
            "sodass",
            "weil",
            "indem"
        ],
        "correctAnswer": "obwohl",
        "explanation": "The warning contrasts with the decision, creating a concessive relation.",
        "id": "c2_02_q055"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welche Formulierung ist typisch fuer den akademischen C2-Stil?",
        "options": [
            "Obwohl viele Probleme bestanden.",
            "Auch wenn es Probleme gab.",
            "Ungeachtet zahlreicher bestehender Probleme.",
            "Weil Probleme bestanden."
        ],
        "correctAnswer": "Ungeachtet zahlreicher bestehender Probleme.",
        "explanation": "'Ungeachtet' is highly formal and frequently appears in academic or administrative texts.",
        "id": "c2_02_q056"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "____ die Kritikpunkte berechtigt erscheinen moegen, rechtfertigen sie keinen vollstaendigen Verzicht auf die Methode.",
        "options": [
            "So berechtigt",
            "Da",
            "Weil",
            "Nachdem"
        ],
        "correctAnswer": "So berechtigt",
        "explanation": "'So + Adjektiv + ... moegen' is an advanced concessive structure often tested at C2 level.",
        "id": "c2_02_q057"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "____ ueberzeugend die Argumentation auch sein mag, einige Fragen bleiben offen.",
        "options": [
            "So",
            "Weil",
            "Da",
            "Nachdem"
        ],
        "correctAnswer": "So",
        "explanation": "'So ueberzeugend ... auch sein mag' is a classic advanced concessive structure.",
        "id": "c2_02_q058"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "____ gross die BemuEhungen auch gewesen sein moegen, das Ergebnis blieb hinter den Erwartungen zurueck.",
        "options": [
            "So",
            "Da",
            "Weil",
            "Waehrend"
        ],
        "correctAnswer": "So",
        "explanation": "'So + Adjektiv + auch' is a sophisticated concessive pattern typical of advanced German.",
        "id": "c2_02_q059"
    },
    {
        "difficulty": "hard",
        "type": "multiple_choice",
        "questionText": "Welche Satzvariante enthaelt die komplexeste Konzessivstruktur?",
        "options": [
            "Obwohl die Studie fehlerhaft war, wurde sie zitiert.",
            "Auch wenn die Studie fehlerhaft war, wurde sie zitiert.",
            "So fehlerhaft die Studie auch gewesen sein mag, wurde sie dennoch vielfach zitiert.",
            "Die Studie war fehlerhaft, wurde aber zitiert."
        ],
        "correctAnswer": "So fehlerhaft die Studie auch gewesen sein mag, wurde sie dennoch vielfach zitiert.",
        "explanation": "The pattern 'So + Adjektiv + auch gewesen sein mag' represents a highly advanced concessive construction expected at C2 level.",
        "id": "c2_02_q060"
    }
]

data['questions'].extend(new_questions)
data['totalQuestions'] = len(data['questions'])

with open('app/src/main/assets/c2_02.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(new_questions)} questions (q021-q060)")
print(f"Total questions now: {data['totalQuestions']}")
easy = sum(1 for q in data['questions'] if q['difficulty'] == 'easy')
medium = sum(1 for q in data['questions'] if q['difficulty'] == 'medium')
hard = sum(1 for q in data['questions'] if q['difficulty'] == 'hard')
print(f"Difficulty breakdown: easy={easy}, medium={medium}, hard={hard}")