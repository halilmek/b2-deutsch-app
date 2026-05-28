#!/usr/bin/env python3
"""Create c1_08.json — Konnektoren & Satzverknüpfung (C1) — 40 questions."""

import json

QUESTIONS = [
    # === Batch 1 (19:19 — 20 questions) ===
    {"difficulty": "easy", "type": "multiple_choice",
     "questionText": "Welcher Konnektor druckt einen Gegensatz aus? Er ist muede, ____ er arbeitet weiter.",
     "options": ["denn", "trotzdem", "deshalb", "ausserdem"],
     "correctAnswer": "trotzdem",
     "explanation": "Trotzdem (nevertheless/yet) expresses a concessive contrast. Denn = reason, deshalb = result, ausserdem = addition."},

    {"difficulty": "easy", "type": "multiple_choice",
     "questionText": "Waehlen Sie den richtigen Kausalkonnektor: ____ das Wetter schlecht war, blieben wir zu Hause.",
     "options": ["Obwohl", "Da", "Damit", "Sobald"],
     "correctAnswer": "Da",
     "explanation": "Da is a causal subordinating conjunction meaning since/because. Obwohl = although, Damit = so that, Sobald = as soon as."},

    {"difficulty": "easy", "type": "multiple_choice",
     "questionText": "Welcher Konnektor leitet einen Finalsatz (Zweck/Absicht) ein?",
     "options": ["weil", "obwohl", "damit", "nachdem"],
     "correctAnswer": "damit",
     "explanation": "Damit introduces a final clause (so that). Weil = cause, obwohl = concession, nachdem = temporal."},

    {"difficulty": "easy", "type": "multiple_choice",
     "questionText": "Ergaenzen Sie den passenden Konnektor: Ich lerne Deutsch, ____ ich in Deutschland studieren moechte.",
     "options": ["weil", "wenn", "obwohl", "sodass"],
     "correctAnswer": "weil",
     "explanation": "Weil (because) introduces a causal subordinate clause. Wenn = when/if, obwohl = although, sodass = so that."},

    {"difficulty": "easy", "type": "multiple_choice",
     "questionText": "Welcher Konnektor hat dieselbe Bedeutung wie aber und steht in der gleichen Satzposition?",
     "options": ["jedoch", "deshalb", "naemlich", "zudem"],
     "correctAnswer": "jedoch",
     "explanation": "Jedoch (however) is a synonym for aber. Unlike aber, jedoch can appear after the verb in second position."},

    {"difficulty": "medium", "type": "multiple_choice",
     "questionText": "Welcher Satz ist grammatikalisch korrekt?",
     "options": ["Er hat den Job bekommen, obwohl er keine Erfahrung hat.", "Er hat den Job bekommen, obwohl er keine Erfahrung haben.", "Obwohl er keine Erfahrung hat, er hat den Job bekommen.", "Obwohl keine Erfahrung er hat, hat er den Job bekommen."],
     "correctAnswer": "Er hat den Job bekommen, obwohl er keine Erfahrung hat.",
     "explanation": "Obwohl is a subordinating conjunction sending the verb to the end. After fronted obwohl clause, main clause follows V2 rule."},

    {"difficulty": "medium", "type": "multiple_choice",
     "questionText": "Welcher Konnektor passt? Das Projekt war teuer. ____ hat es sich langfristig gelohnt.",
     "options": ["Dennoch", "Deshalb", "Naemlich", "Sobald"],
     "correctAnswer": "Dennoch",
     "explanation": "Dennoch (nevertheless) is a concessive adverbial connector between two main clauses. Stronger and more formal than trotzdem."},

    {"difficulty": "medium", "type": "multiple_choice",
     "questionText": "Waehlen Sie den Konnektor, der unter der Bedingung, dass ausdrueckt: ____ du frueh aufstehst, koennen wir den Zug erreichen.",
     "options": ["Als", "Nachdem", "Sofern", "Seit"],
     "correctAnswer": "Sofern",
     "explanation": "Sofern means provided that/as long as and expresses a formal conditional. Als = when (single past), Nachdem = after, Seit = since."},

    {"difficulty": "medium", "type": "multiple_choice",
     "questionText": "Welche Verbindung ist ein Konsekutivkonnektor (Folge/Ergebnis)?",
     "options": ["Er lernte hart, obwohl er muede war.", "Er lernte hart, sodass er die Pruefung bestand.", "Er lernte hart, damit er schlafen konnte.", "Er lernte hart, waehrend er Musik hoerte."],
     "correctAnswer": "Er lernte hart, sodass er die Pruefung bestand.",
     "explanation": "Sodass (so that) is a consecutive connector expressing result. Obwohl = concessive, damit = final, waehrend = temporal."},

    {"difficulty": "medium", "type": "multiple_choice",
     "questionText": "Was ist der Unterschied zwischen weil und denn?",
     "options": ["Es gibt keinen Unterschied.", "Weil = Subjunktion mit Verbendstellung; denn = Konjunktion mit Hauptsatzwortfolge.", "Denn sendet das Verb ans Ende; weil nicht.", "Weil steht immer am Satzanfang; denn nicht."],
     "correctAnswer": "Weil = Subjunktion mit Verbendstellung; denn = Konjunktion mit Hauptsatzwortfolge.",
     "explanation": "Weil pushes the verb to the end (subordinating); denn keeps V2 word order (coordinating). Critical C1 distinction."},

    {"difficulty": "medium", "type": "multiple_choice",
     "questionText": "Welcher Konnektor druckt eine zeitliche Gleichzeitigkeit aus? Sie kochte das Abendessen, ____ ihr Mann die Kinder badete.",
     "options": ["nachdem", "bevor", "waehrend", "seit"],
     "correctAnswer": "waehrend",
     "explanation": "Waehrend (while) expresses simultaneity. Nachdem = after, Bevor = before, Seit = since (duration)."},

    {"difficulty": "medium", "type": "multiple_choice",
     "questionText": "Ergaenzen Sie: Er sprach so leise, ____ ihn kaum jemand verstehen konnte.",
     "options": ["damit", "dass", "ob", "als"],
     "correctAnswer": "dass",
     "explanation": "The structure so ... dass is a consecutive construction meaning so ... that. Damit = purpose, ob = indirect question, als = comparison."},

    {"difficulty": "hard", "type": "multiple_choice",
     "questionText": "Welcher Satz verwendet wobei korrekt?",
     "options": ["Wobei er krank war, arbeitete er weiter.", "Er erklaerte die Loesung, wobei er ein Beispiel nannte.", "Wobei sie die Aufgabe loeste, fragte sie um Hilfe.", "Sie schlief, wobei ihr Bruder lernte."],
     "correctAnswer": "Er erklaerte die Loesung, wobei er ein Beispiel nannte.",
     "explanation": "Wobei adds a supplementary detail about how something was done. It only follows a main clause and refers back to the entire preceding statement."},

    {"difficulty": "hard", "type": "multiple_choice",
     "questionText": "Was ist der stilistische Unterschied zwischen obwohl und wenngleich?",
     "options": ["Wenngleich ist umgangssprachlich; obwohl ist formell.", "Wenngleich ist gehoben/formell-schriftsprachlich; obwohl ist neutral.", "Beide gehoeren zur Umgangssprache.", "Wenngleich leitet einen Konditionalsatz ein; obwohl einen Konzessivsatz."],
     "correctAnswer": "Wenngleich ist gehoben/formell-schriftsprachlich; obwohl ist neutral.",
     "explanation": "Wenngleich and obwohl both introduce concessive clauses but register differs: wenngleich is formal/literary, obwohl is neutral."},

    {"difficulty": "hard", "type": "multiple_choice",
     "questionText": "Welcher Satz ist korrekt umformuliert? Original: Er ist krank. Trotzdem geht er zur Arbeit.",
     "options": ["Er geht zur Arbeit, weil er krank ist.", "Obwohl er krank ist, geht er zur Arbeit.", "Da er krank ist, geht er zur Arbeit.", "Er geht zur Arbeit, sodass er krank ist."],
     "correctAnswer": "Obwohl er krank ist, geht er zur Arbeit.",
     "explanation": "Trotzdem (adverb) = concessive. Its subordinating equivalent is obwohl. Classic C1 reformulation task."},

    {"difficulty": "hard", "type": "multiple_choice",
     "questionText": "Welcher Konnektor druckt eine Einschraenkung oder partielle Verneinung aus?",
     "options": ["zumal", "insofern", "allerdings", "demzufolge"],
     "correctAnswer": "allerdings",
     "explanation": "Allerdings (however/admittedly) concedes or qualifies a statement without fully negating it. Zumal = especially since, insofern = in so far as, demzufolge = consequently."},

    {"difficulty": "hard", "type": "multiple_choice",
     "questionText": "Ergaenzen Sie den passenden Konnektor: ____ sie kein Geld hat, kauft sie sich jeden Tag Kaffee.",
     "options": ["Da", "Obgleich", "Sofern", "Indem"],
     "correctAnswer": "Obgleich",
     "explanation": "Obgleich (even though/although) is a formal concessive conjunction. Da = since (causal), Sofern = provided that, Indem = by doing (modal)."},

    {"difficulty": "hard", "type": "multiple_choice",
     "questionText": "Welcher Satz verwendet indem korrekt?",
     "options": ["Er bestand die Pruefung, indem er fleissig lernte.", "Indem er muede war, schlief er ein.", "Er lernte Deutsch, indem er nach Deutschland reiste.", "Sie half mir, indem ich dankbar war."],
     "correctAnswer": "Er bestand die Pruefung, indem er fleissig lernte.",
     "explanation": "Indem introduces a modal subordinate clause describing the means. Both clauses must share the same subject."},

    {"difficulty": "hard", "type": "multiple_choice",
     "questionText": "Welcher Konnektor druckt aus, dass zwei negative Alternativen gleichzeitig ausgeschlossen werden? ____ kam er punktlich, ____ rief er an.",
     "options": ["entweder ... oder", "weder ... noch", "sowohl ... als auch", "nicht nur ... sondern auch"],
     "correctAnswer": "weder ... noch",
     "explanation": "Weder ... noch (neither ... nor) negates both elements. Negative counterpart of sowohl ... als auch."},

    {"difficulty": "hard", "type": "multiple_choice",
     "questionText": "Welche Aussage ueber den Konnektor zumal ist korrekt?",
     "options": ["Er leitet einen Konzessivsatz ein und bedeutet obwohl.", "Er verstaerkt eine Begruendung und bedeutet besonders weil.", "Er druckt eine zeitliche Folge aus.", "Er verbindet zwei gleichwertige Saetze."],
     "correctAnswer": "Er verstaerkt eine Begruendung und bedeutet besonders weil.",
     "explanation": "Zumal (especially since) is a causal connector reinforcing a reason. Formal/academic German. C1/C2 register."},

    # === Batch 2 (19:21 — 19 questions) ===
    {"difficulty": "easy", "type": "multiple_choice",
     "questionText": "Ergaenzen Sie den passenden zweiteiligen Konnektor: Das Projekt war ____ extrem zeitaufwendig, ____ schlussendlich sehr erfolgreich.",
     "options": ["zwar ... aber", "sowohl ... als auch", "weder ... noch", "nicht nur ... sondern auch"],
     "correctAnswer": "zwar ... aber",
     "explanation": "Zwar ... aber (it is true ... but) connects opposing logical qualities in a concessive structure."},

    {"difficulty": "easy", "type": "multiple_choice",
     "questionText": "Welcher Konnektor fordert Nebensatz-Wortstellung (Verb am Ende)? Wir muessen die Massnahmen verschaerfen, ____ die Infektionszahlen weiter steigen.",
     "options": ["sofern", "andernfalls", "jedoch", "es sei denn"],
     "correctAnswer": "sofern",
     "explanation": "Sofern introduces a conditional subordinate clause, pushing the verb to the end. Andernfalls and jedoch trigger inversion in main clauses."},

    {"difficulty": "medium", "type": "multiple_choice",
     "questionText": "Ergaenzen Sie das passende Bindeglied: Der Oekonom rechnet mit einer baldigen Erholung der Maerkte, ____ viele Haendler skeptisch bleiben.",
     "options": ["wohingegen", "darum", "demnach", "infolgedessen"],
     "correctAnswer": "wohingegen",
     "explanation": "Wohingegen is an adversative subordinating conjunction used to contrast two opposing facts directly."},

    {"difficulty": "easy", "type": "multiple_choice",
     "questionText": "Waehlen Sie die korrekte Wortstellung nach demnach: Die Testergebnisse waren negativ, ____ hat sich der Verdacht nicht bestaetigt.",
     "options": ["demnach", "demnach er", "und demnach", "er demnach"],
     "correctAnswer": "demnach",
     "explanation": "Demnach (accordingly/consequently) is a connector adverb in position 1, requiring the verb immediately in position 2."},

    {"difficulty": "hard", "type": "multiple_choice",
     "questionText": "Vervollstaendigen Sie den Satz sinnvoll: Wir haben alle Vorbereitungen getroffen, ____ es morgen zu keinen Verzoegerungen kommt.",
     "options": ["auf dass", "um zu", "weshalb", "insofern"],
     "correctAnswer": "auf dass",
     "explanation": "Auf dass is an archaic/formal C1-level final conjunction meaning so that. Requires subordinate clause word order."},

    {"difficulty": "medium", "type": "multiple_choice",
     "questionText": "Welche Wortstellung verlangt es sei denn? Ich gehe morgen wandern, ____ das Wetter schlaegt komplett um.",
     "options": ["es sei denn,", "es sei denn, dass", "es sei denn, schlaegt", "es sei denn, umschlaegt"],
     "correctAnswer": "es sei denn,",
     "explanation": "Without dass, es sei denn introduces a main clause with regular V2 word order (Subject + Verb: das Wetter schlaegt...)."},

    {"difficulty": "medium", "type": "multiple_choice",
     "questionText": "Ergaenzen Sie den modalen Konnektor: Er tat so, ____ er von den Plaenen der Chefetage ueberhaupt nichts gewusst ____.",
     "options": ["als ob ... haette", "als ... habe", "wie wenn ... hat", "als ob ... habe"],
     "correctAnswer": "als ob ... haette",
     "explanation": "Er tat so ... als ob requires als ob + Konjunktiv II: als ob er ... haette. Flags non-factual nature of the claim."},

    {"difficulty": "easy", "type": "multiple_choice",
     "questionText": "Finden Sie die korrekte Satzverknuepfung fuer eine proportionale Beziehung: ____ komplexer die Aufgaben werden, ____ strukturierter muessen wir vorgehen.",
     "options": ["Je ... desto", "Umso ... je", "Je ... umso mehr", "Desto ... je"],
     "correctAnswer": "Je ... desto",
     "explanation": "Proportional structures: Je (dependent clause, verb at end) + desto/umso (main clause, immediate inversion after)."},

    {"difficulty": "easy", "type": "multiple_choice",
     "questionText": "Welche Option verbindet diese Saetze konzessiv? Es gab heftige Proteste. ____ es heftige Proteste gab, setzte die Regierung die Reform durch.",
     "options": ["Obgleich", "Demzufolge", "Inwiefern", "Ungeachtet"],
     "correctAnswer": "Obgleich",
     "explanation": "Obgleich is a highly formal C1 subordinating conjunction meaning although/even though."},

    {"difficulty": "medium", "type": "multiple_choice",
     "questionText": "Ergaenzen Sie den restriktiven Konnektor: Ich helfe Ihnen gerne, ____ meine eigenen Aufgaben darunter nicht leiden.",
     "options": ["insofern", "insoweit als", "als dass", "geschweige denn"],
     "correctAnswer": "insofern",
     "explanation": "Insofern introduces a limiting condition (provided that / in as far as) with subordinate word order."},

    {"difficulty": "easy", "type": "multiple_choice",
     "questionText": "Welches Element passt in die Luecke dieser negativen Konjunktion? Der Student konnte sich ____ an den Namen des Professors ____ an den Raum erinnern.",
     "options": ["weder ... noch", "nicht nur ... sondern auch", "entweder ... oder", "sowohl ... als auch"],
     "correctAnswer": "weder ... noch",
     "explanation": "Weder ... noch (neither ... nor) uniquely serves double negation with correlative structure."},

    {"difficulty": "medium", "type": "multiple_choice",
     "questionText": "Achten Sie auf die Wortstellung: Es war extrem glatt; ____ ereigneten sich zahlreiche Unfaelle.",
     "options": ["infolgedessen", "weshalb", "daher haben sich", "sodass"],
     "correctAnswer": "infolgedessen",
     "explanation": "Infolgedessen (consequently) occupies position 1, forcing the verb into position 2: ereigneten sich."},

    {"difficulty": "easy", "type": "multiple_choice",
     "questionText": "Welcher Konnektor druckt eine Steigerung/Addition aus? Das Gebaeude ist ____ architektonisch wertvoll, ____ von historischer Bedeutung.",
     "options": ["nicht nur ... sondern auch", "weder ... noch", "zwar ... aber", "entweder ... oder"],
     "correctAnswer": "nicht nur ... sondern auch",
     "explanation": "Nicht nur ... sondern auch (not only ... but also) adds a second positive point to amplify the first."},

    {"difficulty": "medium", "type": "multiple_choice",
     "questionText": "Ergaenzen Sie: Der neue Mitarbeiter packt kraeftig mit an, ____ seine Kollegin eher passiv bleibt.",
     "options": ["waehrend", "obgleich", "wogegen", "insofern"],
     "correctAnswer": "waehrend",
     "explanation": "Waehrend as an adversative conjunction represents a direct behavioral contrast between two parties."},

    {"difficulty": "easy", "type": "multiple_choice",
     "questionText": "Welche Konstruktion zeigt die Abwesenheit einer erwarteten Handlung? Er hat den Bericht abgegeben, ____ ihn vorher noch einmal Korrektur zu lesen.",
     "options": ["ohne", "anstatt", "um nicht", "dadurch dass"],
     "correctAnswer": "ohne",
     "explanation": "Die Konstruktion ohne ... zu + Infinitiv expresses that an expected action did NOT take place (without proofreading)."},

    {"difficulty": "medium", "type": "multiple_choice",
     "questionText": "Waehlen Sie den passenden Konnektor fuer eine alternative Bedingung: Sie muessen die Gebuehr bis morgen bezahlen, ____ wird Ihre Anmeldung geloescht.",
     "options": ["andernfalls", "sofern", "es sei denn", "vielmehr"],
     "correctAnswer": "andernfalls",
     "explanation": "Andernfalls (otherwise) acts as a conditional adverb in position 1, pointing to a negative consequence if the condition is not met."},

    {"difficulty": "easy", "type": "multiple_choice",
     "questionText": "Ergaenzen Sie: Das Unternehmen investiert stark in KI, ____ die Effizienz der Produktion langfristig ____ steigern.",
     "options": ["um ... zu", "damit ... zu", "auf dass ... zu", "anstatt ... zu"],
     "correctAnswer": "um ... zu",
     "explanation": "Since the subject of both clauses is identical (Das Unternehmen), the infinitive construction um ... zu is required."},

    {"difficulty": "hard", "type": "multiple_choice",
     "questionText": "Welcher Satz zeigt eine grammatikalisch FALSCHE Wortstellung nach jedoch?",
     "options": ["Das Auto ist teuer, jedoch es ist sehr zuverlaessig.", "Das Auto ist teuer, jedoch ist es sehr zuverlaessig.", "Das Auto ist teuer, es ist jedoch sehr zuverlaessig.", "Das Auto ist teuer; es ist jedoch sehr zuverlaessig."],
     "correctAnswer": "Das Auto ist teuer, jedoch es ist sehr zuverlaessig.",
     "explanation": "Jedoch as a connector adverb in position 1 must be followed immediately by the verb: jedoch ist es. The form jedoch es ist is ungrammatical."},

    {"difficulty": "easy", "type": "multiple_choice",
     "questionText": "Ergaenzen Sie den anspruchsvollen modalen Konnektor: Man kann ein System am besten optimieren, ____ man alle Prozesse digitalisiert.",
     "options": ["indem", "dadurch", "wobei", "unterdessen"],
     "correctAnswer": "indem",
     "explanation": "Indem is the standard modal subordinating conjunction explaining how/by what method a goal is accomplished."},

    {"difficulty": "hard", "type": "multiple_choice",
     "questionText": "Welche Konjunktion leitet einen irrealen Vergleichssatz ein und verlangt das Verb direkt in Position 2? ____ er mir kuendigen.",
     "options": ["als wolle", "als ob wolle", "wie wenn wolle", "als wenn gewollt"],
     "correctAnswer": "als wolle",
     "explanation": "If als is used alone for unreal comparisons (without ob or wenn), the inflected Konjunktiv II (wolle) immediately follows als in position 2."},
]


def create_c1_08():
    topic = {
        "topicName": "Konnektoren & Satzverknuepfung (C1)",
        "subjectId": "c1_08",
        "level": "C1",
        "totalQuestions": 0,
        "description": (
            "C1 Konnektoren & Satzverknuepfung.\n\n"
            "KANNEKTOR-TYPEN:\n"
            "- Kausal: weil, da, denn, deshalb, deswegen, darum, infolgedessen, demnach\n"
            "- Konzessiv: obwohl, obgleich, obgleich, obzwar, wenngleich, obgleich, obwhr, trotzdem, dennoch, allerdings, zumal\n"
            "- Final: damit, um ... zu, auf dass, damit\n"
            "- Temporal: als, wenn, waehrend, bevor, nachdem, sobald, solange, seit\n"
            "- Konditional: wenn, falls, sofern, es sei denn, andernfalls\n"
            "- Konsekutiv: sodass, so ... dass, demnach, infolgedessen\n"
            "- Modal: indem, dadurch dass, ohne ... zu, anstatt ... zu\n"
            "- Adversativ: aber, jedoch, waehrend, wohingegen, dagegen\n"
            "- Proportional: je ... desto, je ... umso\n"
            "- Additv: ausserdem, zudem, ueberdies, sowohl ... als auch, nicht nur ... sondern auch\n"
            "\nWORTSTELLUNG (C1 CRITICAL):\n"
            "- Subordinating conjunctions (weil, obwohl, damit, etc.) -> Verb at END\n"
            "- Coordinating conjunctions (denn, aber, oder) -> V2 normal order\n"
            "- Connector adverbs (deshalb, jedoch, leider) -> Verb in Position 2\n"
            "- Nebensatz after fronted subordinate clause -> V2 in main clause"
        ),
        "tips": [
            "Weil = Verb am ENDE; denn = V2 Wortfolge (normal order)",
            "Obwohl und wenngleich = concessive; wenngleich is more formal",
            "Zwar ... aber = contrast concession; nicht nur ... sondern auch = additive contrast",
            "Sodass = consecutive (Folge/Ergebnis); damit = final (Zweck)",
            "Indem = modal clause (HOW to achieve something); um ... zu = same subject infinitive",
            "Ohne ... zu + Infinitiv = expected action did NOT happen",
            "Weder ... noch = double negation (neither ... nor)",
            "Je ... desto = proportional correlation (the more ... the more)"
        ],
        "questions": []
    }

    for i, q in enumerate(QUESTIONS):
        q_copy = dict(q)
        q_copy["id"] = f"c1_08_q{i+1:03d}"
        topic["questions"].append(q_copy)

    topic["totalQuestions"] = len(topic["questions"])

    path = "app/src/main/assets/c1_08.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(topic, f, ensure_ascii=False, indent=2)

    easy = sum(1 for q in topic["questions"] if q["difficulty"] == "easy")
    med = sum(1 for q in topic["questions"] if q["difficulty"] == "medium")
    hard = sum(1 for q in topic["questions"] if q["difficulty"] == "hard")
    print(f"Created {path} with {topic['totalQuestions']} questions")
    print(f"Split: easy={easy}, medium={med}, hard={hard}")


if __name__ == "__main__":
    create_c1_08()
