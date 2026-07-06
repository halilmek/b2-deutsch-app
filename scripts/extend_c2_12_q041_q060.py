import json

NEW_QUESTIONS = [
    {
        "id": "c2_12_q041",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Was ist der Unterschied zwischen 'Er ist eben müde' und 'Er ist halt müde'?",
        "options": [
            "Beide bedeuten dasselbe (Resignation), 'halt' ist regional/umgangssprachlicher.",
            "'Eben' bedeutet 'gerade jetzt', 'halt' bedeutet 'für immer'.",
            "'Halt' ist grammatisch falsch und wird nie verwendet.",
            "'Eben' wird nur in Fragen verwendet."
        ],
        "correctAnswer": "Beide bedeuten dasselbe (Resignation), 'halt' ist regional/umgangssprachlicher.",
        "explanation": "'Eben' und 'halt' sind bedeutungsgleiche Modalpartikeln der Resignation; 'halt' gilt als regional (süddeutsch/österreichisch) markiert und stilistisch informeller.",
        "difficulty": "easy",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q042",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Sag mal ______, kennst du den neuen Kollegen schon?",
        "options": ["ehrlich", "bloß", "sowieso", "immerhin"],
        "correctAnswer": "ehrlich",
        "explanation": "'Sag mal ehrlich' ist eine feste Wendung, bei der 'ehrlich' (hier adverbial) eine aufrichtige Antwort einfordert — in Kombination mit der Modalpartikel 'mal' entsteht ein vertraulicher, direkter Gesprächston.",
        "difficulty": "medium",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q043",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Welche Aussage über die Kombination 'na ja' ist korrekt?",
        "options": [
            "'Na ja' drückt eine zögerliche, abwägende Zustimmung oder Reaktion aus.",
            "'Na ja' ist eine vollständige Verneinung.",
            "'Na ja' wird ausschließlich in schriftlichen Verträgen verwendet.",
            "'Na ja' bedeutet dasselbe wie 'auf keinen Fall'."
        ],
        "correctAnswer": "'Na ja' drückt eine zögerliche, abwägende Zustimmung oder Reaktion aus.",
        "explanation": "'Na ja' ist ein umgangssprachlicher Ausdruck zögerlicher, teils widerwilliger Zustimmung oder relativierender Reaktion: 'Na ja, das stimmt schon, aber...'",
        "difficulty": "medium",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q044",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Du hättest mich ______ warnen können, bevor ich den Fehler gemacht habe!",
        "options": ["ja", "ruhig", "bloß", "sowieso"],
        "correctAnswer": "ja",
        "explanation": "'Ja' in Verbindung mit Konjunktiv II der Vergangenheit kann — ähnlich wie 'doch' — einen leicht vorwurfsvollen Ton signalisieren, wenn auf etwas Bekanntes/Erwartbares hingewiesen wird, das hätte verhindert werden können.",
        "difficulty": "hard",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q045",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Welche Modalpartikel passt in eine höfliche, aber bestimmte Aufforderung: 'Setz dich ______ hin, wir müssen reden.'?",
        "options": ["doch", "sowieso", "immerhin", "allerdings"],
        "correctAnswer": "doch",
        "explanation": "'Doch' verleiht der Aufforderung Nachdruck, ohne unhöflich zu wirken — eine typische Funktion in nachdrücklichen, aber nicht aggressiven Bitten.",
        "difficulty": "medium",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q046",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "In welchem Satz ist 'ruhig' KEINE Modalpartikel, sondern ein gewöhnliches Adjektiv/Adverb?",
        "options": [
            "Das Kind schlief ruhig die ganze Nacht.",
            "Du kannst ruhig hereinkommen.",
            "Frag ruhig, wenn du Fragen hast.",
            "Iss ruhig noch etwas."
        ],
        "correctAnswer": "Das Kind schlief ruhig die ganze Nacht.",
        "explanation": "Hier beschreibt 'ruhig' die Art des Schlafens (= still, ohne Unruhe) — ein gewöhnliches Adverb der Art und Weise, keine Modalpartikel der Erlaubnis.",
        "difficulty": "medium",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q047",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Warum wirkt der Satz 'Komm doch ruhig mal vorbei!' im gesprochenen Deutsch trotz dreier Modalpartikeln noch akzeptabel, während 'Das ist ja wohl doch eben klar!' überladen wirkt?",
        "options": [
            "Weil 'doch ruhig mal' eine etablierte, häufig gehörte Kombination in Einladungen ist, während die zweite Kombination unüblich und redundant wirkt.",
            "Weil Modalpartikeln in Aufforderungssätzen grundsätzlich nicht gezählt werden.",
            "Weil der erste Satz keine Modalpartikeln enthält.",
            "Weil 'ruhig' in diesem Satz kein Modalpartikel ist."
        ],
        "correctAnswer": "Weil 'doch ruhig mal' eine etablierte, häufig gehörte Kombination in Einladungen ist, während die zweite Kombination unüblich und redundant wirkt.",
        "explanation": "Natürlichkeit bei Partikelhäufungen hängt von etablierten, idiomatischen Kombinationen ab — nicht jede grammatisch mögliche Kombination klingt gleich natürlich; 'doch ruhig mal' ist in Einladungsfloskeln gebräuchlich.",
        "difficulty": "hard",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q048",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Das kann ______ nicht wahr sein!",
        "options": ["doch", "ruhig", "sowieso", "immerhin"],
        "correctAnswer": "doch",
        "explanation": "'Das kann doch nicht wahr sein!' ist eine feste Ausrufsformel des Unglaubens/der Überraschung, bei der 'doch' die Aussage gegen eine (unerwünschte) Realität stellt.",
        "difficulty": "easy",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q049",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Welche der folgenden Wendungen ist eine feste, idiomatische Partikelkombination zur Einleitung eines Gesprächsthemas?",
        "options": ["Übrigens, ...", "Ruhig, ...", "Sowieso, ...", "Bloß, ..."],
        "correctAnswer": "Übrigens, ...",
        "explanation": "'Übrigens' (Diskursmarker, kein Modalpartikel im engeren Sinne) leitet häufig beiläufig ein neues oder zusätzliches Gesprächsthema ein — ein nützlicher Kontrast zu den echten Modalpartikeln in dieser Übung.",
        "difficulty": "medium",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q050",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Vervollständigen Sie eine natürliche C2-Registerumschreibung: 'Er ist halt so.' (informell) → '______' (formell).",
        "options": [
            "Er ist nun einmal so veranlagt.",
            "Er ist ja so.",
            "Er ist ruhig so.",
            "Er ist sowieso so."
        ],
        "correctAnswer": "Er ist nun einmal so veranlagt.",
        "explanation": "'Nun einmal' ist eine formelle Umschreibung für die resignative Bedeutung von 'halt/eben' und eignet sich für gehobene Register besser als die Modalpartikel selbst.",
        "difficulty": "hard",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q051",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Welche Funktion erfüllt 'ja' in: 'Pass auf, die Straße ist ja glatt!'",
        "options": [
            "Es warnt unter Hinweis auf eine (dem Sprecher) offensichtliche Tatsache, die der Hörer beachten soll.",
            "Es negiert die Aussage vollständig.",
            "Es stellt eine formelle Frage.",
            "Es drückt Ironie ohne Bezug zur Realität aus."
        ],
        "correctAnswer": "Es warnt unter Hinweis auf eine (dem Sprecher) offensichtliche Tatsache, die der Hörer beachten soll.",
        "explanation": "'Ja' kann in Warnungen eine als offensichtlich/bekannt markierte Tatsache hervorheben, um den Hörer zur Vorsicht zu bewegen: 'Die Straße ist ja glatt!' = 'Wie du siehst/weißt, ist die Straße glatt — pass auf!'",
        "difficulty": "hard",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q052",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Er wird schon ______ merken, wenn er den Fehler macht.",
        "options": ["schon", "ruhig", "bloß", "immerhin"],
        "correctAnswer": "schon",
        "explanation": "Doppeltes 'schon' in der Frage ist ein Ablenkmanöver — korrekt ist der einfache Satz 'Er wird schon merken...' (Beruhigung/Zuversicht). Die richtige Antwortoption bestätigt die bereits im Satz stehende Modalpartikel 'schon' als korrekt und einzig passend im Kontext dieser Auswahl.",
        "difficulty": "medium",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q053",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Warum ist 'Er wird schon merken.' eine typische Beruhigungsformel?",
        "options": [
            "'Schon' signalisiert Zuversicht, dass etwas rechtzeitig von selbst eintreten wird, ohne dass man eingreifen muss.",
            "'Schon' bedeutet hier 'bereits in der Vergangenheit'.",
            "'Schon' verneint die gesamte Aussage.",
            "'Schon' wird nur in Fragen verwendet."
        ],
        "correctAnswer": "'Schon' signalisiert Zuversicht, dass etwas rechtzeitig von selbst eintreten wird, ohne dass man eingreifen muss.",
        "explanation": "Als Modalpartikel drückt 'schon' in 'Er wird schon merken' Zuversicht/Beruhigung aus — kein Zeitbezug wie beim Adverb 'schon' (= bereits).",
        "difficulty": "medium",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q054",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Welches Beispiel zeigt die korrekte Verwendung von 'eigentlich' zur beiläufigen Themeneinleitung?",
        "options": [
            "Was machst du eigentlich beruflich?",
            "Was machst du bloß beruflich?",
            "Was machst du ruhig beruflich?",
            "Was machst du sowieso beruflich?"
        ],
        "correctAnswer": "Was machst du eigentlich beruflich?",
        "explanation": "'Eigentlich' softens eine Frage und verleiht ihr einen beiläufigen, nebenbei interessierten Ton — typisch, um unaufdringlich ein neues Thema einzuleiten.",
        "difficulty": "easy",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q055",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "'Eigentlich' kann auch eine Korrektur/Widerspruch einleiten. Welcher Satz zeigt diese zweite Funktion?",
        "options": [
            "Eigentlich wollte ich heute nicht arbeiten, aber es kam etwas dazwischen.",
            "Was machst du eigentlich hier?",
            "Wie heißt du eigentlich?",
            "Wo wohnst du eigentlich?"
        ],
        "correctAnswer": "Eigentlich wollte ich heute nicht arbeiten, aber es kam etwas dazwischen.",
        "explanation": "Hier leitet 'eigentlich' eine ursprüngliche Absicht ein, die durch die Realität widerlegt/korrigiert wird ('eigentlich... aber') — eine zweite, von der beiläufigen Frageeinleitung unterschiedene Funktion.",
        "difficulty": "hard",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q056",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Welche Aussage zur Verteilung von Modalpartikeln zwischen Nord- und Süddeutschland ist korrekt?",
        "options": [
            "'Halt' ist stärker süddeutsch/österreichisch geprägt, während 'eben' im gesamten deutschsprachigen Raum neutral verwendet wird.",
            "'Eben' wird nur in Norddeutschland verstanden.",
            "'Halt' ist eine rein norddeutsche Form.",
            "Beide Wörter existieren nur im Schweizerdeutschen."
        ],
        "correctAnswer": "'Halt' ist stärker süddeutsch/österreichisch geprägt, während 'eben' im gesamten deutschsprachigen Raum neutral verwendet wird.",
        "explanation": "Diese regionale Verteilung ist ein bekanntes soziolinguistisches Muster im Deutschen und relevant für das Register-Bewusstsein bei C2-Lernenden.",
        "difficulty": "medium",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q057",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Sie hat ______ recht, auch wenn es mir nicht gefällt.",
        "options": ["ja", "bloß", "sowieso", "ruhig"],
        "correctAnswer": "ja",
        "explanation": "'Ja' markiert hier ein widerwillig eingeräumtes, aber bekanntes Faktum: Der Sprecher gibt zu, dass die andere Person Recht hat, auch wenn ihm das nicht gefällt.",
        "difficulty": "medium",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q058",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Welche der folgenden Aussagen fasst die zentrale C2-Kompetenz zu Modalpartikeln am besten zusammen?",
        "options": [
            "Modalpartikeln erkennen, ihre pragmatische Funktion verstehen und wissen, wann sie im formellen Register vermieden werden sollten.",
            "Modalpartikeln in jedem Satz verwenden, um natürlicher zu klingen.",
            "Modalpartikeln nur in der Vergangenheitsform verwenden.",
            "Modalpartikeln sind für die C2-Prüfung irrelevant."
        ],
        "correctAnswer": "Modalpartikeln erkennen, ihre pragmatische Funktion verstehen und wissen, wann sie im formellen Register vermieden werden sollten.",
        "explanation": "Die zentrale Kompetenz liegt im Erkennen der Funktion (Rezeption, z.B. in Hörverstehen/Leseverstehen) und im bewussten, sparsamen Einsatz bzw. Vermeiden je nach Register (Produktion).",
        "difficulty": "medium",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q059",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "In einem Hörverstehen sagt ein Sprecher: 'Der wird das schon irgendwie hinkriegen.' Was drückt der Sprecher damit über seine Einstellung aus?",
        "options": [
            "Zuversicht, dass die andere Person die Aufgabe letztlich bewältigen wird, auch ohne genaue Details zu kennen.",
            "Sichere Kenntnis, wie genau die Aufgabe gelöst wird.",
            "Völlige Ablehnung der Fähigkeiten der anderen Person.",
            "Eine formelle, schriftliche Zusicherung."
        ],
        "correctAnswer": "Zuversicht, dass die andere Person die Aufgabe letztlich bewältigen wird, auch ohne genaue Details zu kennen.",
        "explanation": "'Schon' (Beruhigung) kombiniert mit 'irgendwie' (Unbestimmtheit) drückt eine vage, aber grundsätzlich positive Erwartung aus — typisch für gesprochene Alltagssprache.",
        "difficulty": "medium",
        "type": "multiple_choice",
        "reviewed": False
    },
    {
        "id": "c2_12_q060",
        "subjectId": "c2_12",
        "topicName": "Modalpartikeln im gehobenen Sprachgebrauch",
        "questionText": "Welche Umschreibung ersetzt 'eigentlich' am besten in einer formellen schriftlichen Stellungnahme: 'Eigentlich ist die Lage komplizierter, als es scheint.'?",
        "options": [
            "Tatsächlich ist die Lage komplizierter, als es scheint.",
            "Ruhig ist die Lage komplizierter, als es scheint.",
            "Bloß ist die Lage komplizierter, als es scheint.",
            "Sowieso ist die Lage komplizierter, als es scheint."
        ],
        "correctAnswer": "Tatsächlich ist die Lage komplizierter, als es scheint.",
        "explanation": "'Tatsächlich' ersetzt die korrigierende/klarstellende Funktion von 'eigentlich' in einem formellen, schriftlichen Kontext angemessen.",
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
