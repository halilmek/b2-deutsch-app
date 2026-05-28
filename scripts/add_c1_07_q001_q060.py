#!/usr/bin/env python3
"""Create c1_07.json — Wortbildung: Komposita & Derivation — 60 questions."""

import json

QUESTIONS = [
    {"difficulty": "easy", "type": "multiple_choice",
     "questionText": "Was bedeutet das Kompositum Handschuh?",
     "options": ["Ein Schuh fuer die Hand", "Ein Kleidungsstueck fuer die Hand", "Ein Werkzeug fuer die Hand", "Ein Handtuch aus Leder"],
     "correctAnswer": "Ein Kleidungsstueck fuer die Hand",
     "explanation": "Handschuh = Hand + Schuh, but semantically it means glove. Compound meaning is not always transparent."},

    {"difficulty": "easy", "type": "multiple_choice",
     "questionText": "Welches Wort ist ein Kompositum mit dem Grundwort -arbeit?",
     "options": ["Arbeitslos", "Hausarbeit", "Arbeitgeber", "Bearbeitung"],
     "correctAnswer": "Hausarbeit",
     "explanation": "Hausarbeit = Haus + Arbeit. The Grundwort (head word) is the last element."},

    {"difficulty": "easy", "type": "multiple_choice",
     "questionText": "Welche Vorsilbe (Praefix) macht aus dem Adjektiv moeglich das Gegenteil?",
     "options": ["ver-", "ent-", "un-", "miss-"],
     "correctAnswer": "un-",
     "explanation": "un- is the standard negating prefix for adjectives: unmoeglich = impossible."},

    {"difficulty": "easy", "type": "multiple_choice",
     "questionText": "Welches Suffix wird verwendet, um aus dem Verb lehren ein Nomen fuer eine Person zu bilden? -> der ____",
     "options": ["Lehrung", "Lehrei", "Lehrer", "Lehrnis"],
     "correctAnswer": "Lehrer",
     "explanation": "-er forms agent nouns from verbs: lehren -> Lehrer (teacher)."},

    {"difficulty": "easy", "type": "multiple_choice",
     "questionText": "Welches der folgenden Woerter ist durch das Suffix -heit gebildet worden?",
     "options": ["Freiheit", "Freundschaft", "Freundlichkeit", "Befreiung"],
     "correctAnswer": "Freiheit",
     "explanation": "Freiheit = frei + -heit. -heit forms abstract nouns from adjectives; -schaft forms collective nouns."},

    {"difficulty": "medium", "type": "multiple_choice",
     "questionText": "Ergänzen Sie das passende Kompositum: Die Stadtverwaltung hat einen neuen ____ fuer Radfahrer eingerichtet.",
     "options": ["Fahrradstreifen", "Radfahrstreifen", "Streifenfahrrad", "Fahrtradstreifen"],
     "correctAnswer": "Radfahrstreifen",
     "explanation": "Radfahrstreifen = Radfahrer + Streifen. German compounds are head-final."},

    {"difficulty": "medium", "type": "multiple_choice",
     "questionText": "Welches Wort enthaelt ein Praefix mit einer trennbaren Bedeutung (trennbares Verb)?",
     "options": ["verstehen", "ankommen", "besuchen", "erkennen"],
     "correctAnswer": "ankommen",
     "explanation": "Ankommen is separable: er kommt an. ver-, be-, er- are inseparable."},

    {"difficulty": "medium", "type": "multiple_choice",
     "questionText": "Welche Bedeutung hat das Praefix ver- im Wort verreisen?",
     "options": ["Es druckt eine Verneinung aus", "Es druckt eine Bewegung weg von einem Ort aus", "Es druckt eine Wiederholung aus", "Es druckt eine Verstaerkung aus"],
     "correctAnswer": "Es druckt eine Bewegung weg von einem Ort aus",
     "explanation": "ver- in verreisen indicates movement away: to travel away."},

    {"difficulty": "medium", "type": "multiple_choice",
     "questionText": "Welches Suffix bildet ein Adjektiv mit der Bedeutung ohne etwas? -> Er ist voellig ____ (ohne Hoffnung).",
     "options": ["hoffnungsreich", "hoffnungslos", "hoffnungsvoll", "hoffnungsmäßig"],
     "correctAnswer": "hoffnungslos",
     "explanation": "-los means without: hoffnungslos = without hope (hopeless)."},

    {"difficulty": "medium", "type": "multiple_choice",
     "questionText": "Welches Fugenelement fehlt im Kompositum Arbeit____vertrag?",
     "options": ["-s-", "-en-", "-e-", "kein Fugenelement"],
     "correctAnswer": "-s-",
     "explanation": "Arbeitsvertrag uses the Fugenelement -s-. Fugenelemente connect compound parts."},

    {"difficulty": "medium", "type": "multiple_choice",
     "questionText": "Welches Wort ist eine Ableitung (Derivation) und kein Kompositum?",
     "options": ["Tischdecke", "Sonnenschein", "Freundlichkeit", "Kopfschmerzen"],
     "correctAnswer": "Freundlichkeit",
     "explanation": "Freundlichkeit = Freund -> freundlich (-lich) -> Freundlichkeit (-keit). The others are compounds."},

    {"difficulty": "medium", "type": "multiple_choice",
     "questionText": "Das Praefix ent- in enttaeuschen druckt aus, dass ____.",
     "options": ["eine Handlung verstaerkt wird", "eine Erwartung nicht erfuellt wird / etwas aufgehoben wird", "etwas wiederholt wird", "eine Bewegung beginnt"],
     "correctAnswer": "eine Erwartung nicht erfuellt wird / etwas aufgehoben wird",
     "explanation": "Ent- signals reversal/removal. Enttäuschen = to disappoint."},

    {"difficulty": "hard", "type": "multiple_choice",
     "questionText": "Welches Kompositum ist semantisch ein Bahuvrihi (Possessivkompositum)?",
     "options": ["Tischbein", "Rotkaeppchen", "Waschmaschine", "Buchregal"],
     "correctAnswer": "Rotkaeppchen",
     "explanation": "Bahuvrihi = one with red cap (possessive). Rotkaeppchen describes the girl by her characteristic."},

    {"difficulty": "hard", "type": "multiple_choice",
     "questionText": "Welche Wortbildung ist korrekt fuer das Verb analysieren -> Nomen des Vorgangs?",
     "options": ["Analysist", "Analysierung", "Analyse", "Analysat"],
     "correctAnswer": "Analyse",
     "explanation": "Verbs in -ieren drop -ieren: analysieren -> Analyse."},

    {"difficulty": "hard", "type": "multiple_choice",
     "questionText": "Welches Wort enthaelt das Suffix -bar mit passiver Bedeutung (= kann getan werden)?",
     "options": ["offenbar", "nachbar", "lesbar", "sonderbar"],
     "correctAnswer": "lesbar",
     "explanation": "-bar added to a verb stem = capable of being X-ed: lesbar = can be read."},

    {"difficulty": "hard", "type": "multiple_choice",
     "questionText": "Wie nennt man die Wortbildung, bei der ein neues Wort durch Kuerzung eines bestehenden entsteht?",
     "options": ["Derivation", "Konversion", "Kurzwortbildung (Kuerzung)", "Komposition"],
     "correctAnswer": "Kurzwortbildung (Kuerzung)",
     "explanation": "Kurzwortbildung (clipping) shortens an existing word: Universitaet -> Uni."},

    {"difficulty": "hard", "type": "multiple_choice",
     "questionText": "In welchem der folgenden Woerter liegt eine Konversion vor - also ein Wortartenwechsel ohne Affix?",
     "options": ["Freundschaft", "das Lachen", "lesbar", "Arbeitslosigkeit"],
     "correctAnswer": "das Lachen",
     "explanation": "Konversion = word class change without affix: lachen -> das Lachen."},

    {"difficulty": "hard", "type": "multiple_choice",
     "questionText": "Welches Praefix veraendert die Bedeutung des Verbs schreiben so, dass es falsch schreiben bedeutet?",
     "options": ["ver-", "ueber-", "um-", "ab-"],
     "correctAnswer": "ver-",
     "explanation": "Verschreiben = to write incorrectly. ver- indicates an erroneous action."},

    {"difficulty": "hard", "type": "multiple_choice",
     "questionText": "Welches Wort ist ein Beispiel fuer ein Determinativkompositum, bei dem das Bestimmungswort den Zweck angibt?",
     "options": ["Tischbein", "Kuechenwaage", "Rotkohl", "Grossmutter"],
     "correctAnswer": "Kuechenwaage",
     "explanation": "In Kuechenwaage (kitchen scale), Kuechen- specifies the purpose of the Grundwort Waage."},

    {"difficulty": "hard", "type": "multiple_choice",
     "questionText": "Welches der folgenden Komposita enthaelt ein Fugenelement, das historisch einem Genitiv entspricht?",
     "options": ["Tischdecke", "Hundeleine", "Tageslicht", "Blumenstrauß"],
     "correctAnswer": "Tageslicht",
     "explanation": "Tageslicht = Tag + -es- + Licht. -es- reflects the old genitive form of Tag."},

    {"difficulty": "easy", "type": "multiple_choice",
     "questionText": "Die ploetzliche ____ der Preise ueberraschte viele Kunden.",
     "options": ["Erhoehung", "Erhoeher", "Erhoehbarkeit", "Erloehnis"],
     "correctAnswer": "Erhoehung",
     "explanation": "Erhohung = noun from erhoen (to increase)."},

    {"difficulty": "medium", "type": "multiple_choice",
     "questionText": "Das Unternehmen investiert stark in die ____ neuer Technologien.",
     "options": ["Weiterentwicklung", "Weiterentwickler", "Entwickelungslos", "Entwickelbarkeit"],
     "correctAnswer": "Weiterentwicklung",
     "explanation": "Weiterentwicklung = further development."},

    {"difficulty": "easy", "type": "multiple_choice",
     "questionText": "Die ____ des Projekts dauerte laenger als erwartet.",
     "options": ["Durchfuehrung", "Durchfuehrnis", "Durchfuehrerung", "Fuehrbarkeit"],
     "correctAnswer": "Durchfuehrung",
     "explanation": "Durchfuehrung = standard nominalization of durchfuehren."},

    {"difficulty": "medium", "type": "multiple_choice",
     "questionText": "Viele Arbeitnehmer wuenschen sich mehr ____ am Arbeitsplatz.",
     "options": ["Selbststaendigkeit", "Selbststaenden", "Selbststaendigheit", "Selbstung"],
     "correctAnswer": "Selbststaendigkeit",
     "explanation": "-keit forms abstract nouns from adjectives."},

    {"difficulty": "easy", "type": "multiple_choice",
     "questionText": "Die neue ____ sorgt fuer mehr Verkehrssicherheit.",
     "options": ["Strassenbeleuchtung", "Strassenlichtung", "Strassenhellung", "Beleuchtbarkeit"],
     "correctAnswer": "Strassenbeleuchtung",
     "explanation": "Strassenbeleuchtung = street lighting."},

    {"difficulty": "medium", "type": "multiple_choice",
     "questionText": "Seine ____ gegenueber Kritik beeindruckte alle Kollegen.",
     "options": ["Gelassenheit", "Gelassigkeit", "Gelassung", "Gelassenbar"],
     "correctAnswer": "Gelassenheit",
     "explanation": "-heit forms nouns expressing qualities or states."},

    {"difficulty": "easy", "type": "multiple_choice",
     "questionText": "Die ____ der Daten muss sorgfaeltig erfolgen.",
     "options": ["Verarbeitung", "Verarbeitnis", "Bearbeitkeit", "Verarbeitbarkeit"],
     "correctAnswer": "Verarbeitung",
     "explanation": "Verarbeitung = nominalization of verarbeiten."},

    {"difficulty": "medium", "type": "multiple_choice",
     "questionText": "Das Unternehmen legt großen Wert auf ____.",
     "options": ["Kundenzufriedenheit", "Kundenzufriedung", "Zufriedenbarkeit", "Kundenglueckheit"],
     "correctAnswer": "Kundenzufriedenheit",
     "explanation": "Kundenzufriedenheit = customer satisfaction."},

    {"difficulty": "easy", "type": "multiple_choice",
     "questionText": "Die ____ des Gebaeudes wurde 2024 abgeschlossen.",
     "options": ["Renovierung", "Renovierheit", "Renovierbarkeit", "Renoviertung"],
     "correctAnswer": "Renovierung",
     "explanation": "-ung forms nouns from verbs; Renovierung = renovation."},

    {"difficulty": "hard", "type": "multiple_choice",
     "questionText": "Sein Verhalten zeugte von großer ____.",
     "options": ["Verantwortungslosigkeit", "Verantwortungheit", "Verantwortbarigkeit", "Verantwortlichkeitung"],
     "correctAnswer": "Verantwortungslosigkeit",
     "explanation": "-losigkeit = absence of a quality (irresponsibility)."},

    {"difficulty": "medium", "type": "multiple_choice",
     "questionText": "Die ____ der Umwelt hat hoechste Prioritaet.",
     "options": ["Schutzmassnahme", "Schutzigkeit", "Schuetzbarkeit", "Beschuetzungheit"],
     "correctAnswer": "Schutzmassnahme",
     "explanation": "Schutzmassnahme = protective measure."},

    {"difficulty": "easy", "type": "multiple_choice",
     "questionText": "Die ____ zwischen den Abteilungen funktionierte hervorragend.",
     "options": ["Zusammenarbeit", "Zusammenarbeitung", "Arbeitssamkeit", "Kooperierung"],
     "correctAnswer": "Zusammenarbeit",
     "explanation": "Zusammenarbeit = collaboration / teamwork."},

    {"difficulty": "easy", "type": "multiple_choice",
     "questionText": "Die ____ des Systems verursacht hohe Kosten.",
     "options": ["Wartung", "Wartigkeit", "Wartbarkeit", "Gewartung"],
     "correctAnswer": "Wartung",
     "explanation": "Wartung = maintenance, derived from warten."},

    {"difficulty": "hard", "type": "multiple_choice",
     "questionText": "Er bewies außergewoehnliche ____ in schwierigen Situationen.",
     "options": ["Belastbarkeit", "Belastungheit", "Belastsamkeit", "Belastungslosigkeit"],
     "correctAnswer": "Belastbarkeit",
     "explanation": "-barkeit = capability/resilience; Belastbarkeit = resilience."},

    {"difficulty": "medium", "type": "multiple_choice",
     "questionText": "Die ____ der Forschungsergebnisse erfolgte online.",
     "options": ["Veroeffentlichung", "Veroeffentlichtheit", "Oeffnungsbarkeit", "Publizierungkeit"],
     "correctAnswer": "Veroeffentlichung",
     "explanation": "Veroeffentlichung = publication, from veroeffentlichen."},

    {"difficulty": "medium", "type": "multiple_choice",
     "questionText": "Viele Menschen leiden unter zunehmender ____.",
     "options": ["Arbeitslosigkeit", "Arbeitsbarkeit", "Arbeitsung", "Arbeitsfreiheitigkeit"],
     "correctAnswer": "Arbeitslosigkeit",
     "explanation": "-losigkeit = lack of; Arbeitslosigkeit = unemployment."},

    {"difficulty": "easy", "type": "multiple_choice",
     "questionText": "Die ____ der Teilnehmer wurde sorgfaeltig ueberprueft.",
     "options": ["Anwesenheit", "Anwesung", "Anwesbarkeit", "Anwesigkeit"],
     "correctAnswer": "Anwesenheit",
     "explanation": "Anwesenheit = presence, formed with -heit."},

    {"difficulty": "hard", "type": "multiple_choice",
     "questionText": "Das Unternehmen foerdert die ____ seiner Mitarbeiter.",
     "options": ["Eigenverantwortung", "Eigenverantwortlichkeitung", "Verantwortungskeit", "Selbstverantwortbar"],
     "correctAnswer": "Eigenverantwortung",
     "explanation": "Eigenverantwortung = personal responsibility."},

    {"difficulty": "medium", "type": "multiple_choice",
     "questionText": "Die ____ der Informationen dauerte mehrere Stunden.",
     "options": ["Datenauswertung", "Datenauswertigkeit", "Auswertsamkeit", "Informationswertung"],
     "correctAnswer": "Datenauswertung",
     "explanation": "Datenauswertung = data analysis/evaluation."},

    {"difficulty": "easy", "type": "multiple_choice",
     "questionText": "Ihre ____ machte sie zu einer beliebten Fuehrungskraft.",
     "options": ["Freundlichkeit", "Freundsamtkeit", "Freundhaftung", "Freundung"],
     "correctAnswer": "Freundlichkeit",
     "explanation": "-keit creates abstract nouns from adjectives; Freundlichkeit = friendliness."},

    {"difficulty": "easy", "type": "multiple_choice",
     "questionText": "Die Wortbildung unterscheidet hauptsaechlich zwischen ____ und Derivation.",
     "options": ["Flexion", "Komposition", "Reduplikation", "Konversion"],
     "correctAnswer": "Komposition",
     "explanation": "Two main types: Komposition (compounds) and Derivation (affixes)."},

    {"difficulty": "easy", "type": "multiple_choice",
     "questionText": "Was ist ein Kompositum?",
     "options": ["Ein Wort mit Praefix", "Ein Wort aus zwei oder mehr eigenstaendigen Woertern", "Ein abgeleitetes Wort", "Ein Wort mit Suffix"],
     "correctAnswer": "Ein Wort aus zwei oder mehr eigenstaendigen Woertern",
     "explanation": "A Kompositum combines at least two independent words."},

    {"difficulty": "easy", "type": "multiple_choice",
     "questionText": "Welches Wort ist ein Determinativkompositum?",
     "options": ["das Singen", "der Schreibtisch", "die Schoenheit", "das Rotkaeppchen"],
     "correctAnswer": "der Schreibtisch",
     "explanation": "Schreibtisch: Schreib- (determinant) modifies Tisch (basic word)."},

    {"difficulty": "easy", "type": "multiple_choice",
     "questionText": "Vervollstaendigen Sie das Kompositum: der ____ + die Pflanze -> die ____",
     "options": ["Zimmer; Zimmerpflanze", "Zimmers; Zimmerpflanze", "Zimmern; Zimmerpflanze", "Zimmeres; Zimmerpflanze"],
     "correctAnswer": "Zimmer; Zimmerpflanze",
     "explanation": "Compounds use the base form of the first word: Zimmer + Pflanze = Zimmerpflanze."},

    {"difficulty": "easy", "type": "multiple_choice",
     "questionText": "Was ist das Grundwort im Kompositum Autobahn?",
     "options": ["Auto", "Bahn", "beide", "keins"],
     "correctAnswer": "Bahn",
     "explanation": "The Grundwort (basic word) is the last element: Bahn. Auto is the Bestimmungswort."},

    {"difficulty": "easy", "type": "multiple_choice",
     "questionText": "Welches Fugenlautelement ist hier korrekt: der Staat + der Anwalt -> der ____",
     "options": ["Staatanwalt", "Staatesanwalt", "Staatsanwalt", "Staatanwalt"],
     "correctAnswer": "Staatsanwalt",
     "explanation": "Staat + s + Anwalt = Staatsanwalt (prosecutor). Fugen-s is required."},

    {"difficulty": "medium", "type": "multiple_choice",
     "questionText": "Vervollstaendigen Sie: die Liebe + der Brief -> der ____",
     "options": ["Liebesbrief", "Liebenbrief", "Liebsbrief", "Liebeabrief"],
     "correctAnswer": "Liebesbrief",
     "explanation": "Liebe + s + Brief = Liebesbrief. Nouns in -e add -s- as Fugenelement."},

    {"difficulty": "easy", "type": "multiple_choice",
     "questionText": "Bei der Derivation wird ein ____ an ein Basiswort angehaengt.",
     "options": ["Affix", "Kompositum", "Fugenelement", "Stamm"],
     "correctAnswer": "Affix",
     "explanation": "Derivation adds affixes (prefixes or suffixes) to a base word."},

    {"difficulty": "easy", "type": "multiple_choice",
     "questionText": "Welches Wort ist eine Derivation (Ableitung)?",
     "options": ["Tischlampe", "Lehrbuch", "Fahrkarte", "Schoenheit"],
     "correctAnswer": "Schoenheit",
     "explanation": "Schoenheit = schoen + -heit. The others are compounds (two free morphemes)."},

    {"difficulty": "easy", "type": "multiple_choice",
     "questionText": "Das Suffix -ung bildet hauptsaechlich ____ aus Verben.",
     "options": ["Adjektive", "Substantive", "Verben", "Adverbien"],
     "correctAnswer": "Substantive",
     "explanation": "-ung derives nouns from verbs: pruefen -> Pruefung."},

    {"difficulty": "easy", "type": "multiple_choice",
     "questionText": "Vervollstaendigen Sie die Derivation: krank + ____ = die Krankheit",
     "options": ["-keit", "-heit", "-nis", "-tum"],
     "correctAnswer": "-heit",
     "explanation": "krank + -heit = Krankheit."},

    {"difficulty": "easy", "type": "multiple_choice",
     "questionText": "Welches Praefix druckt eine negative Bedeutung aus (Gegenteil)?",
     "options": ["ver-", "be-", "un-", "er-"],
     "correctAnswer": "un-",
     "explanation": "un- negates adjectives: unmoeglich, unbekannt."},

    {"difficulty": "medium", "type": "multiple_choice",
     "questionText": "Bilden Sie das passende Kompositum: die Tuer + der Schluessel -> ____",
     "options": ["der Tuerschluessel", "die Tuerschluessel", "das Tuerschluessel", "den Tuerschluessel"],
     "correctAnswer": "der Tuerschluessel",
     "explanation": "Gender follows the Grundwort: der Schluessel -> der Tuerschluessel."},

    {"difficulty": "medium", "type": "multiple_choice",
     "questionText": "Was bedeutet der Rauchmelder woertlich (Kompositionsanalyse)?",
     "options": ["jemand, der Rauch meldet", "ein Geraet, das Rauch meldet", "Rauch, der meldet", "ein Melder fuer Rauch"],
     "correctAnswer": "ein Geraet, das Rauch meldet",
     "explanation": "Rauchmelder = Rauch + Melder (from melden). A device that detects smoke."},

    {"difficulty": "easy", "type": "multiple_choice",
     "questionText": "Vervollstaendigen Sie das Verbderivat: Lauf + ____ = laufen",
     "options": ["-en", "-ieren", "-eln", "-ern"],
     "correctAnswer": "-en",
     "explanation": "Many verbs add -en: Lauf -> laufen."},

    {"difficulty": "medium", "type": "multiple_choice",
     "questionText": "Welches Wort enthaelt ein Praefix, das eine Trennung oder Entfernung anzeigt?",
     "options": ["bekommen", "entlassen", "verlieren", "zerbrechen"],
     "correctAnswer": "entlassen",
     "explanation": "ent- indicates removal: entlassen = to dismiss/release."},

    {"difficulty": "hard", "type": "multiple_choice",
     "questionText": "Was ist ein Kopulativkompositum?",
     "options": ["Hausaufgabe", "schwarz-weiss", "Hochhaus", "Liebesbrief"],
     "correctAnswer": "schwarz-weiss",
     "explanation": "Kopulativkomposita (dvandva) combine two equal elements: schwarz-weiss. Both parts have equal status."},

    {"difficulty": "medium", "type": "multiple_choice",
     "questionText": "Bilden Sie das Adjektiv: der Riese + -haft -> ____",
     "options": ["riesig", "riesenhaft", "rieshaft", "rieselhaft"],
     "correctAnswer": "riesenhaft",
     "explanation": "-haft derives adjectives from nouns: Riese -> riesenhaft (gigantic). Note linking -en-."},

    {"difficulty": "hard", "type": "multiple_choice",
     "questionText": "Welches der folgenden Woerter ist KEIN Kompositum?",
     "options": ["Eingang", "Arbeitszimmer", "Kindergarten", "Muttertag"],
     "correctAnswer": "Eingang",
     "explanation": "Eingang (entry) is arguably derived. Kinder garten and Muttertag are clear compounds."},

    {"difficulty": "easy", "type": "multiple_choice",
     "questionText": "Ergänzen Sie: Das Suffix -los bildet ____ mit der Bedeutung ohne.",
     "options": ["Substantive", "Adjektive", "Verben", "Adverbien"],
     "correctAnswer": "Adjektive",
     "explanation": "-los derives adjectives meaning without: hoffnungslos (hopeless), arbeitslos (unemployed)."},
]


def create_c1_07():
    topic = {
        "topicName": "Wortbildung: Komposita & Derivation",
        "subjectId": "c1_07",
        "level": "C1",
        "totalQuestions": 0,
        "description": (
            "In this topic you will practice advanced German word formation.\n\n"
            "KOMPOSITA (compounds): Determinative, possessive (Bahuvrihi), copulative.\n"
            "Fugenelemente: -s-, -es-, -en- (historical genitive links).\n"
            "DERIVATION: prefixes (ver-, ent-, er-, be-, un-), suffixes (-heit, -keit, -schaft, -ung, -er, -los, -bar, -haft, -lich).\n"
            "KONVERSION: zero-derivation without affix (lachen -> das Lachen).\n"
            "KURZWORTBILDUNG: clipping (Universitaet -> Uni)."
        ),
        "tips": [
            "In compounds the last word (Grundwort) determines gender and meaning",
            "un- negates adjectives; ver-/ent-/er-/be- are verbal prefixes",
            "-heit and -keit are variants: -heit for consonants, -keit for -el/-ler endings",
            "-los = without, -reich = rich in, -voll = full of",
            "-bar added to verb stems = capable of being X-ed (lesbar)",
            "Fugenelemente (-s-, -es-) often reflect historical genitive forms",
            "Konversion = word class change without affix: lachen -> das Lachen",
            "Bahuvrihi (possessive compounds) describe by characteristic: Rotkappchen = one with red cap"
        ],
        "questions": []
    }

    for i, q in enumerate(QUESTIONS):
        q_copy = dict(q)
        q_copy["id"] = f"c1_07_q{i+1:03d}"
        topic["questions"].append(q_copy)

    topic["totalQuestions"] = len(topic["questions"])

    path = "app/src/main/assets/c1_07.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(topic, f, ensure_ascii=False, indent=2)

    print(f"Created {path} with {topic['totalQuestions']} questions")
    print(f"Topic: {topic['topicName']}")
    easy_ct = sum(1 for q in topic["questions"] if q["difficulty"] == "easy")
    med_ct = sum(1 for q in topic["questions"] if q["difficulty"] == "medium")
    hard_ct = sum(1 for q in topic["questions"] if q["difficulty"] == "hard")
    print(f"Split: easy={easy_ct}, medium={med_ct}, hard={hard_ct}")


if __name__ == "__main__":
    create_c1_07()
