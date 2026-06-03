import json

with open('app/src/main/assets/c1_01.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

questions_to_add = [
  {
    "questionText": "Der ____ des Berichts ist sehr sachlich und nominal geprägt.",
    "options": ["Verbalstil", "Nominalstil", "Satzbau", "Konjunktiv"],
    "correctAnswer": "Nominalstil",
    "explanation": "Nominalstil refers to a style heavy on nouns and noun phrases, often used in official or technical reports. Verbalstil is more verb-based and dynamic.",
    "difficulty": "easy",
    "type": "multiple_choice"
  },
  {
    "questionText": "Welcher Satz steht im Verbalstil?",
    "options": ["Die Durchführung der Maßnahme erfolgt morgen.", "Zur Durchführung der Maßnahme kommt es morgen.", "Die Maßnahme wird morgen durchgeführt.", "Die Maßnahme findet morgen ihre Durchführung."],
    "correctAnswer": "Die Maßnahme wird morgen durchgeführt.",
    "explanation": "The sentence uses a finite verb ('wird durchgeführt') and active/passive verbal construction, typical for Verbalstil. The others nominalize 'Durchführung'.",
    "difficulty": "easy",
    "type": "multiple_choice"
  },
  {
    "questionText": "Die ____ der Anmeldefrist führt zum Ausschluss vom Wettbewerb.",
    "options": ["verspätete Anmeldung", "sich verspäten", "wenn man sich verspätet", "dass die Anmeldung verspätet ist"],
    "correctAnswer": "verspätete Anmeldung",
    "explanation": "A nominal phrase with an adjective attribute ('verspätete Anmeldung') is characteristic of Nominalstil. The others contain verbs or clauses.",
    "difficulty": "easy",
    "type": "multiple_choice"
  },
  {
    "questionText": "Welcher Satz ist ein typisches Beispiel für Nominalstil?",
    "options": ["Nachdem er angekommen war, begann er sofort mit der Arbeit.", "Nach seiner Ankunft begann er sofort mit der Arbeit.", "Er kam an und begann sofort zu arbeiten.", "Sobald er ankam, begann er die Arbeit."],
    "correctAnswer": "Nach seiner Ankunft begann er sofort mit der Arbeit.",
    "explanation": "'Nach seiner Ankunft' is a nominal prepositional phrase replacing a temporal clause ('Nachdem er angekommen war'). This reduces verbs and increases nouns.",
    "difficulty": "medium",
    "type": "multiple_choice"
  },
  {
    "questionText": "____ wird häufig in Gesetzen, Verträgen und Behördenbriefen verwendet.",
    "options": ["Der Verbalstil", "Der Nominalstil", "Der Imperativ", "Die indirekte Rede"],
    "correctAnswer": "Der Nominalstil",
    "explanation": "Nominalstil is common in legal and administrative texts because it sounds precise, objective, and timeless.",
    "difficulty": "easy",
    "type": "multiple_choice"
  },
  {
    "questionText": "Formen Sie ins Verbale um: 'Bei Nichtbeachtung der Hinweise erfolgt der Ausschluss.'",
    "options": ["Wenn Sie die Hinweise nicht beachten, werden Sie ausgeschlossen.", "Nichtbeachtung führt zum Ausschluss.", "Bei Missachtung Ausschluss.", "Ohne Beachtung Ausschluss."],
    "correctAnswer": "Wenn Sie die Hinweise nicht beachten, werden Sie ausgeschlossen.",
    "explanation": "The correct option replaces the noun 'Nichtbeachtung' and 'Ausschluss' with the verb 'nicht beachten' and passive 'werden ausgeschlossen' – clear Verbalstil.",
    "difficulty": "medium",
    "type": "multiple_choice"
  },
  {
    "questionText": "Welche Wortgruppe ist ein Signal für Nominalstil?",
    "options": ["weil, dass, obwohl", "unter Berücksichtigung von, in Bezug auf", "laufen, springen, denken", "sehr, ziemlich, extrem"],
    "correctAnswer": "unter Berücksichtigung von, in Bezug auf",
    "explanation": "Prepositional phrases with nominalizations (e.g., 'unter Berücksichtigung von') are typical for Nominalstil. Conjunctions and verbs signal Verbalstil.",
    "difficulty": "medium",
    "type": "multiple_choice"
  },
  {
    "questionText": "Der ____ wirkt oft dichter, abstrakter und informationsverdichteter.",
    "options": ["Verbalstil", "Nominalstil", "Konjunktiv", "Präteritum"],
    "correctAnswer": "Nominalstil",
    "explanation": "Nominalstil packs information into noun phrases, making sentences denser and often more abstract than Verbalstil.",
    "difficulty": "easy",
    "type": "multiple_choice"
  },
  {
    "questionText": "Ersetzen Sie den Verbalstil durch Nominalstil: 'Weil er sich gut vorbereitet hat, bestand er die Prüfung.'",
    "options": ["Durch gute Vorbereitung bestand er die Prüfung.", "Er bestand die Prüfung aufgrund seiner guten Vorbereitung.", "Seine gute Vorbereitung führte zum Bestehen der Prüfung.", "Alle drei Antworten sind nominale Umformungen."],
    "correctAnswer": "Alle drei Antworten sind nominale Umformungen.",
    "explanation": "All three replace the causal clause 'Weil er sich gut vorbereitet hat' with noun-based structures ('Durch gute Vorbereitung', 'aufgrund seiner guten Vorbereitung', 'Seine gute Vorbereitung').",
    "difficulty": "hard",
    "type": "multiple_choice"
  },
  {
    "questionText": "Welcher Satz enthält einen nominalisierten Infinitiv?",
    "options": ["Das Laufen fällt ihm leicht.", "Er läuft jeden Tag.", "Er ist am Laufen.", "Beim Laufen denkt er nach."],
    "correctAnswer": "Das Laufen fällt ihm leicht.",
    "explanation": "'Das Laufen' is a nominalized infinitive (neutral article + verb infinitive capitalized), a form often used in Nominalstil.",
    "difficulty": "medium",
    "type": "multiple_choice"
  },
  {
    "questionText": "Vom Verbalstil zum Nominalstil: 'Die Firma stellt die Produktion ein, weil die Kosten gestiegen sind.'",
    "options": ["Die Firma stellt wegen gestiegener Kosten die Produktion ein.", "Die Firma beendet die Produktion bei steigenden Kosten.", "Die Einstellung der Produktion erfolgt aufgrund des Kostenanstiegs.", "Kostensteigerung bedingt Produktionseinstellung."],
    "correctAnswer": "Die Einstellung der Produktion erfolgt aufgrund des Kostenanstiegs.",
    "explanation": "This option is fully nominalized: 'Einstellung' instead of 'stellt ein', 'Kostenanstiegs' instead of 'Kosten gestiegen sind', and no finite verb in the causal clause.",
    "difficulty": "hard",
    "type": "multiple_choice"
  },
  {
    "questionText": "Welche Aussage über Nominalstil ist falsch?",
    "options": ["Er verwendet viele Hauptwörter.", "Er ist typisch für persönliche Briefe.", "Er reduziert Nebensätze.", "Er kommt oft in wissenschaftlichen Texten vor."],
    "correctAnswer": "Er ist typisch für persönliche Briefe.",
    "explanation": "Personal letters usually use Verbalstil (more verb-based, personal, dynamic). Nominalstil is common in academic, official, and technical texts.",
    "difficulty": "easy",
    "type": "multiple_choice"
  },
  {
    "questionText": "Formulieren Sie nominal: 'Bevor man eine Entscheidung trifft, sollte man alle Fakten prüfen.'",
    "options": ["Vor einer Entscheidungsfindung ist eine Faktenprüfung ratsam.", "Man sollte vor Entscheidungen alle Fakten prüfen.", "Prüfe Fakten vor Entscheidungen.", "Vor dem Entscheiden sollte geprüft werden."],
    "correctAnswer": "Vor einer Entscheidungsfindung ist eine Faktenprüfung ratsam.",
    "explanation": "The original temporal clause 'Bevor man eine Entscheidung trifft' becomes the prepositional phrase 'Vor einer Entscheidungsfindung'; 'alle Fakten prüfen' becomes 'eine Faktenprüfung'.",
    "difficulty": "hard",
    "type": "multiple_choice"
  },
  {
    "questionText": "Welcher Satz steht im reinen Nominalstil?",
    "options": ["Der Antrag auf Verlängerung der Frist wurde abgelehnt.", "Man lehnte den Antrag ab, die Frist zu verlängern.", "Die Fristverlängerung wurde nicht genehmigt.", "Sie haben den Verlängerungsantrag abgelehnt."],
    "correctAnswer": "Die Fristverlängerung wurde nicht genehmigt.",
    "explanation": "'Fristverlängerung' is a compound noun replacing 'die Frist verlängern'; no verb except passive 'wurde genehmigt' – very nominalized.",
    "difficulty": "medium",
    "type": "multiple_choice"
  },
  {
    "questionText": "____ ist lebendiger, handlungsorientierter und persönlicher.",
    "options": ["Nominalstil", "Verbalstil", "Nominalisierung", "Nominalphrase"],
    "correctAnswer": "Verbalstil",
    "explanation": "Verbalstil uses active verbs and personal forms, making texts more dynamic, vivid, and personal compared to Nominalstil.",
    "difficulty": "easy",
    "type": "multiple_choice"
  },
  {
    "questionText": "Welche Umformung ist falsch (vom Verbal- zum Nominalstil)? Original: 'Weil das Wetter schlecht war, fiel das Spiel aus.'",
    "options": ["Wegen des schlechten Wetters fiel das Spiel aus.", "Das Spiel fiel aufgrund der schlechten Wetterlage aus.", "Das Ausfallen des Spiels geschah wegen dem schlechten Wetter.", "Schlechtes Wetter verursachte Spielausfallspielen."],
    "correctAnswer": "Das Ausfallen des Spiels geschah wegen dem schlechten Wetter.",
    "explanation": "The error is 'wegen dem' (colloquial; standard is 'wegen des') and 'geschah' is odd with 'Ausfallen' – style is unnatural and grammatically borderline.",
    "difficulty": "medium",
    "type": "multiple_choice"
  },
  {
    "questionText": "Erkennen Sie den Stil: 'Nach Erhalt Ihrer Zahlung senden wir Ihnen die Ware zu.'",
    "options": ["Verbalstil", "Nominalstil", "Gemischter Stil", "Imperativstil"],
    "correctAnswer": "Nominalstil",
    "explanation": "'Nach Erhalt Ihrer Zahlung' is a nominal phrase (Erhalt + Zahlung) instead of a temporal clause like 'Nachdem wir Ihre Zahlung erhalten haben'.",
    "difficulty": "easy",
    "type": "multiple_choice"
  },
  {
    "questionText": "Vom Nominal- zum Verbalstil: 'Die sofortige Räumung des Gebäudes wurde angeordnet.'",
    "options": ["Man ordnete an, dass das Gebäude sofort geräumt werden soll.", "Das Gebäude wurde sofort geräumt.", "Die Anordnung der sofortigen Räumung erfolgte.", "Es gab eine Räumungsanordnung."],
    "correctAnswer": "Man ordnete an, dass das Gebäude sofort geräumt werden soll.",
    "explanation": "This replaces the noun 'Räumung' with the verb 'geräumt werden' and 'Anordnung' with 'ordnete an' – clear Verbalstil with a subordinate clause.",
    "difficulty": "hard",
    "type": "multiple_choice"
  },
  {
    "questionText": "Welches Signalwort leitet oft einen Nominalstil ein?",
    "options": ["dass", "weil", "aufgrund", "bevor"],
    "correctAnswer": "aufgrund",
    "explanation": "'Aufgrund' is a preposition that requires a noun phrase, typical for Nominalstil (e.g., 'aufgrund des Regens'). 'dass', 'weil', 'bevor' introduce clauses with verbs.",
    "difficulty": "medium",
    "type": "multiple_choice"
  },
  {
    "questionText": "Warum wird Nominalstil in wissenschaftlichen Arbeiten geschätzt?",
    "options": ["Er ist emotionaler.", "Er ist subjektiver.", "Er wirkt objektiver und abstrakter.", "Er ist kürzer und einfacher."],
    "correctAnswer": "Er wirkt objektiver und abstrakter.",
    "explanation": "Nominalstil removes personal and temporal references, creating an objective, timeless tone – ideal for academic writing. Verbalstil can feel too personal or narrative.",
    "difficulty": "easy",
    "type": "multiple_choice"
  }
]

next_id = 108
for q in questions_to_add:
    q['id'] = f'c1_01_q{str(next_id).zfill(3)}'
    next_id += 1

data['questions'].extend(questions_to_add)
data['totalQuestions'] = len(data['questions'])

with open('app/src/main/assets/c1_01.json', 'w', encoding='utf-8') as out:
    json.dump(data, out, ensure_ascii=False, indent=2)

print(f"Added {len(questions_to_add)} questions. New total: {data['totalQuestions']}")
print(f"Last ID: {data['questions'][-1]['id']}")
