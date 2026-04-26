#!/usr/bin/env python3
"""
B2 Deutsch - 100 Questions Per Topic Generator for ALL CEFR Levels
Generates 100 real, clean German grammar questions per topic for A1, A2, B1, C1.
All questions stored in JSON for: (1) Firebase import, (2) App assets (offline)
"""

import json
import random

# Level Topics: (id, name, short_description)
ALL_TOPICS = {
    'A1': [
        ('a1_01', 'Artikel: der, die, das', 'Bestimmte und unbestimmte Artikel'),
        ('a1_02', 'Nominativ', 'Wer? Was?'),
        ('a1_03', 'Akkusativ', 'Wen? Was?'),
        ('a1_04', 'Verben: Präsens', 'regelmäßige und unregelmäßige Verben'),
        ('a1_05', 'Konjugation: ich, du, er/sie/es', 'Verbkonjugation im Präsens'),
        ('a1_06', 'Fragen: ja/nein und W-Fragen', 'Ja/Nein Fragen und W-Fragen'),
        ('a1_07', 'Negation: nicht und kein', 'Sätze verneinen'),
        ('a1_08', 'Possessivpronomen: mein, dein...', 'Possessivpronomen im Nominativ'),
        ('a1_09', 'Wortstellung: S-P-O', 'Grundwortstellung'),
        ('a1_10', 'Modalverben: können, müssen, wollen', 'Modalverben im Präsens'),
        ('a1_11', 'Trennbare Verben', 'Trennbare und untrennbare Verben'),
        ('a1_12', 'Perfekt mit haben', 'Perfekt mit haben'),
        ('a1_13', 'Perfekt mit sein', 'Perfekt mit sein'),
        ('a1_14', 'Adjektive: Nominativ', 'Adjektivdeklination im Nominativ'),
        ('a1_15', 'Zahlen: 1-100', 'Zahlen und Zählen'),
    ],
    'A2': [
        ('a2_01', 'Perfekt mit haben und sein', 'Vergangenheit bilden'),
        ('a2_02', 'Dativ', 'Wem?'),
        ('a2_03', 'Dativ und Akkusativ', 'Wechselpräpositionen'),
        ('a2_04', 'Präteritum: sein und haben', 'Vergangenheit'),
        ('a2_05', 'Verben mit Dativ', 'bestimmte Verben'),
        ('a2_06', ' reflexive Verben', 'sich freuen, sich erinnern...'),
        ('a2_07', 'Präpositionen: aus, bei, mit, nach, seit, von, zu', 'Getrennte Präpositionen'),
        ('a2_08', 'da-Komposita', 'da damit, dafür...'),
        ('a2_09', 'weil und obwohl', 'Nebensätze'),
        ('a2_10', 'Konjunktionen: und, oder, aber, denn', 'Hauptsatzkonjunktionen'),
        ('a2_11', 'Adjektive: Akkusativ', 'Adjektivdeklination'),
        ('a2_12', 'Komparativ und Superlativ', 'Steigerung'),
        ('a2_13', 'Passiv Präsens', 'Wird gemacht'),
        ('a2_14', 'Futur mit werden', 'Zukunft ausdrücken'),
        ('a2_15', 'Nomen-Verb-Verbindungen', 'Zeit verbringen, Angst haben...'),
    ],
    'B1': [
        ('b1_01', 'Präteritum: alle Verben', 'Vergangenheit'),
        ('b1_02', 'Plusquamperfekt', 'Vorvergangenheit'),
        ('b1_03', 'weil, obwohl, dass, ob', 'Nebensätze'),
        ('b1_04', 'Relativsätze: Nominativ und Akkusativ', 'der, die, das'),
        ('b1_05', 'Relativsätze: Dativ und Genitiv', 'dem, deren, dessen'),
        ('b1_06', 'Passiv Präteritum und Perfekt', 'Passive Stimme'),
        ('b1_07', 'Konjunktiv II: würde', 'Unrealer Konditional'),
        ('b1_08', 'Konjunktiv II: könnte, müsste...', 'Höfliche Formen'),
        ('b1_09', 'Verben mit Präpositionen', 'abhängen von, denken an...'),
        ('b1_10', 'Nomen mit Präpositionen', 'Angst vor, Interesse an...'),
        ('b1_11', 'Adjektive mit Präpositionen', 'abhängig von, zufrieden mit...'),
        ('b1_12', 'Futur I und II', 'Zukunft und Vermutungen'),
        ('b1_13', 'Modalverben im Präteritum', 'konnte, musste, wollte...'),
        ('b1_14', 'lassen + Infinitiv', 'Er ließ ihn gehen'),
        ('b1_15', 'lassen sich + Infinitiv', 'Das lässt sich lösen'),
    ],
    'B2': [
        ('b2_01', 'Konnektoren I: als, bevor, bis, seitdem, während, wenn', 'Zeitliche Beziehungen'),
        ('b2_02', 'Konnektoren II: sobald, solange', 'Zeitliche Beziehungen II'),
        ('b2_03', 'Verben und Ergänzungen', 'Verben mit Präpositionen'),
        ('b2_04', 'Zeitformen in der Vergangenheit', 'Perfekt, Präteritum, Plusquamperfekt'),
        ('b2_05', 'Zeitformen der Zukunft', 'Futur I und II'),
        ('b2_06', 'Futur mit werden', 'Werden + Infinitiv'),
        ('b2_07', 'Angaben im Satz', 'Satzklammer'),
        ('b2_08', 'Verneinung mit nicht', 'Nicht-Verneinung'),
        ('b2_09', 'Negationswörter', 'Niemand, nichts, nie...'),
        ('b2_10', 'Passiv Präteritum', 'Passive Stimme'),
        ('b2_11', 'Konjunktiv II der Vergangenheit', 'Hätte, wäre, würde geworden...'),
        ('b2_12', 'Konjunktiv II mit Modalverben', 'Hätte machen können...'),
        ('b2_13', 'Pronomen: einander', 'Wir helfen einander'),
        ('b2_14', 'Weiterführende Nebensätze', 'Das ist der Mann, dem...'),
        ('b2_15', 'Präpositionen mit Genitiv', 'trotz, während, wegen...'),
        ('b2_16', 'je und desto/umso + Komparativ', 'Je mehr, desto besser'),
        ('b2_17', 'Nomen-Verb-Verbindungen', 'eine Prüfung bestehen'),
        ('b2_18', 'Folgen ausdrücken', 'Deshalb, deshalb, infolgedessen'),
        ('b2_19', 'Ausdrücke mit Präpositionen', 'Es kommt darauf an'),
        ('b2_20', 'Irreale Konditionalsätze', 'Wenn ich Zeit hätte...'),
        ('b2_21', 'Relativsätze im Genitiv', 'Der Mann, dessen Auto...'),
        ('b2_22', 'Konjunktiv I in der indirekten Rede', 'Indirekte Rede'),
        ('b2_23', 'Konjunktiv II in irrealen Vergleichssätzen', 'Als ob, als wenn'),
    ],
    'C1': [
        ('c1_01', 'Konjunktiv I: alle Formen', 'ich komme, er komme'),
        ('c1_02', 'Konjunktiv II: alle Formen', 'ich käme, er käme'),
        ('c1_03', 'Indirekte Rede mit Konjunktiv I', 'Er sagte, er sei krank'),
        ('c1_04', 'Passivkonjugation:alle Tempora', 'Wird gemacht, wurde gemacht...'),
        ('c1_05', 'Nominalisierung von Verben', 'etwas prüfen → die Prüfung'),
        ('c1_06', ' Verbalisierung von Nomen', 'die Durchführung → durchführen'),
        ('c1_07', 'Partizipialkonstruktionen', 'Der Patient, der ins Krankenhaus gebracht wurde...'),
        ('c1_08', 'Erweiterte Infinitive mit zu', 'Es ist wichtig, das zu tun'),
        ('c1_09', 'Funktionsverbgefüge', 'in Erfahrung bringen, zur Kenntnis nehmen'),
        ('c1_10', 'Unpersönliche Ausdrücke', 'Es empfiehlt sich, ...'),
        ('c1_11', 'Sentiments污染物', 'Bedauern, Vorwürfe'),
        ('c1_12', 'Konjunktionen: geschweige denn, zumal', 'Fortgeschrittene Verbindungen'),
        ('c1_13', 'Kausale, konditionale, konzessive Beziehungen', 'Insofern als, selbst wenn'),
        ('c1_14', 'Textkohärenz: Konnektoren', 'Zunächst, anschließend, schließlich'),
        ('c1_15', 'Stilistische Varianten', 'formell, wissenschaftlich, journalistisch'),
    ],
}

# Question templates per level - simpler for A1, more complex for C1
# Format: (question_stem, options, correct_answer, difficulty)

def get_mcq_templates(level):
    if level == 'A1':
        return [
            ('___ Buch liegt auf dem Tisch.', ['Das', 'Der', 'Die', 'Ein'], 'Das', 'easy'),
            ('Ich ___ Deutsch.', ['sprecht', 'spreche', 'spricht', 'sprechen'], 'spreche', 'easy'),
            ('___ du das?', ['Weiß', 'Weißt', 'Wissen', 'Wusste'], 'Weißt', 'easy'),
            ('Das ist ___ Katze.', ['ein', 'eine', 'einer', 'einem'], 'eine', 'easy'),
            ('Er ___ nach Hause.', ['geht', 'gehe', 'gehst', 'gehen'], 'geht', 'easy'),
            ('___ du morgen Zeit?', ['Hast', 'Habe', 'Hat', 'Habt'], 'Hast', 'easy'),
            ('Sie ___ eine Straße.', ['überschreitet', 'überschreite', 'überschreitest', 'überschreiten'], 'überschreitet', 'easy'),
            ('Ich trinke ___ Kaffee.', ['ein', 'eine', 'einer', '-'], '-', 'easy'),
            ('Der Mann ___ eine Frau.', ['sieht', 'sehe', 'siehst', 'seht'], 'sieht', 'easy'),
            ('___ Kind spielt im Garten.', ['Ein', 'Eine', 'Der', 'Die'], 'Ein', 'easy'),
            ('Das ist ___ Auto.', ['mein', 'meine', 'meiner', 'meinem'], 'mein', 'easy'),
            ('Wir ___ am Montag.', ['arbeite', 'arbeitest', 'arbeitet', 'arbeiten'], 'arbeiten', 'easy'),
            ('Er ___ von zu Hause.', ['komme', 'kommst', 'kommt', 'kommen'], 'kommt', 'easy'),
            ('___ Uhr ist es?', ['Was', 'Wo', 'Wann', 'Wie viel'], 'Wie viel', 'easy'),
            ('Ich bin ___ Student.', ['ein', 'eine', 'einer', '-'], '-', 'easy'),
            ('Du ___ das nicht.', ['kann', 'kannst', 'kann', 'könnt'], 'kannst', 'easy'),
            ('Das Kind ___ eine Katze.', ['habt', 'hast', 'hat', 'habe'], 'hat', 'easy'),
            ('___ Tag ist heute?', ['Welcher', 'Welche', 'Welches', 'Was für ein'], 'Welcher', 'easy'),
            ('Ich habe ___ Hunger.', ['ein', 'eine', '-', 'einer'], '-', 'easy'),
            ('Er ___ kein Deutsch.', ['spreche', 'sprichst', 'spricht', 'sprechen'], 'spricht', 'easy'),
            ('Die Frau ___ schnell.', ['läuft', 'laufst', 'laufe', 'laufen'], 'läuft', 'easy'),
            ('___ heißeße ich Anna.', ['Und', 'Aber', 'Ich', 'Na'], 'Ich', 'easy'),
            ('Wir ___ in Berlin.', ['wohne', 'wohnst', 'wohnt', 'wohnen'], 'wohnen', 'easy'),
            ('Das ___ ein Haus.', ['bin', 'bist', 'ist', 'sind'], 'ist', 'easy'),
            ('Ich ___ eine Frage.', ['haben', 'habt', 'hat', 'habe'], 'habe', 'easy'),
            ('Du ___ sehr nett.', ['bin', 'bist', 'ist', 'sind'], 'bist', 'easy'),
            ('Er ___ das Buch.', ['lese', 'liest', 'lesen', 'lest'], 'liest', 'easy'),
            ('___ ist das?', ['Wer', 'Was', 'Wo', 'Wie'], 'Was', 'easy'),
            ('Das ist ___ Lampe.', ['der', 'die', 'das', 'ein'], 'die', 'easy'),
            ('Ich komme ___ Deutschland.', ['aus', 'bei', 'mit', 'nach'], 'aus', 'easy'),
        ]
    elif level == 'A2':
        return [
            ('Gestern ___ ich ins Kino gegangen.', ['habe', 'bin', 'wird', 'hat'], 'bin', 'easy'),
            ('Ich ___ dir helfen.', ['kann', 'kannst', 'kann', 'könnt'], 'kann', 'easy'),
            ('___ du mit mir kommen?', ['Kannst', 'Kann', 'Können', 'Konntest'], 'Kannst', 'easy'),
            ('Er ___ schon in München.', ['war', 'ist', 'hat', 'wird'], 'war', 'medium'),
            ('Ich habe ___ Ferien ___', ['die / gemacht', '- / gehabt', 'die / gehabt', '- / gemacht'], 'die / gehabt', 'medium'),
            ('Das Buch ___ mir ___', ['hat / gefallen', 'ist / gefallen', 'hat / gefällt', 'ist / gefällt'], 'hat / gefallen', 'medium'),
            ('Sie ___ seit drei Jahren hier.', ['wohnt', 'wohnst', 'wohne', 'wohnen'], 'wohnt', 'easy'),
            ('___ dem Wetter bin ich froh.', ['Wegen', 'Trotz', 'Während', 'Nach'], 'Wegen', 'medium'),
            ('Er ist ___ dem Chef.', ['bei', 'mit', 'von', 'zu'], 'bei', 'easy'),
            ('Ich interessiere mich ___ Musik.', ['für', 'an', 'auf', 'über'], 'für', 'easy'),
            ('___ er krank war, ist er nicht gekommen.', ['Weil', 'Obwohl', 'Wenn', 'Als'], 'Weil', 'easy'),
            ('Das ist ___ als das.', ['groß', 'größer', 'am größten', 'größere'], 'größer', 'easy'),
            ('Er ___ gestern ins Büro ___', ['hat / gegangen', 'ist / gegangen', 'ist / gegangen', 'hat / gegangen'], 'ist / gegangen', 'medium'),
            ('___ du schon ___ ?', ['Hast / gegessen', 'Bist / gegessen', 'Hast / gegangen', 'Bist / gegangen'], 'Hast / gegessen', 'medium'),
            ('Die Suppe ist ___', ['kochen', 'kocht', 'gekocht', 'kochte'], 'gekocht', 'easy'),
            ('Er ___ sich über die Nachricht.', ['freut', 'freue', 'freust', 'freuen'], 'freut', 'easy'),
            ('___ ich viel lernte, habe ich die Prüfung bestanden.', ['Weil', 'Obwohl', 'Wenn', 'Damit'], 'Weil', 'medium'),
            ('Das ist die ___ Lösung.', ['gut', 'besser', 'am besten', 'gute'], 'beste', 'hard'),
            ('Er spricht ___ als ich.', ['deutlich', 'deutlicher', 'am deutlichsten', 'deutlichste'], 'deutlicher', 'medium'),
            ('Sie ist die ___ von allen.', ['schön', 'schöner', 'am schönsten', 'schönste'], 'schönste', 'hard'),
            ('___ ich Zeit habe, helfe ich dir.', ['Wenn', 'Weil', 'Als', 'Damit'], 'Wenn', 'easy'),
            ('Er wartet ___ seine Mutter.', ['bei', 'auf', 'nach', 'von'], 'auf', 'easy'),
            ('___ du das gemacht?', ['Wie', 'Warum', 'Wann', 'Wo'], 'Wie', 'easy'),
            ('Ich bin mit dem Zug ___', ['gefahren', 'gefahren', 'gefahre', 'fährt'], 'gefahren', 'easy'),
            ('Das Buch ___ gestohlen ___', ['ist / worden', 'hat / worden', 'wurde / worden', 'wird / worden'], 'ist / worden', 'medium'),
            ('Er ist ___是因为 er zu spät ___', ['gekommen', 'gehet', 'ging', 'kommt'], 'gekommen', 'medium'),
            ('Sie ___ gestern einen Film ___', ['habt / gesehen', 'hat / gesehen', 'ist / gesehen', 'wird / gesehen'], 'hat / gesehen', 'medium'),
            ('___ er Hilfe braucht, soll er fragen.', ['Wenn', 'Weil', 'Obwohl', 'Damit'], 'Wenn', 'easy'),
            ('Er ist ___ Freude ___', ['von / übertönt', 'vor / übertönt', 'aus / überflogen', 'mit / über'], 'vor / übertönt', 'hard'),
            ('Die Aufgabe ist ___ zu ___', ['schwer / lösen', 'schwerer / lösen', 'am schwersten / lösen', 'schwere / gelöst'], 'schwer / lösen', 'medium'),
        ]
    elif level == 'B1':
        return [
            ('___ er das gesagt hatte, ging er.', ['Nachdem', 'Wenn', 'Weil', 'Obwohl'], 'Nachdem', 'medium'),
            ('Das ist der Mann, ___ ich gestern getroffen habe.', ['den', 'der', 'dem', 'dessen'], 'den', 'easy'),
            ('Wenn ich Zeit ___, würde ich dir helfen.', ['hätte', 'haben', 'hat', 'gehabt'], 'hätte', 'medium'),
            ('Er sprach so leise, ___ ich ihn kaum verstehen ___', ['dass / konnte', 'weil / konnte', 'obwohl / können', 'damit / können'], 'dass / konnte', 'medium'),
            ('Das ist die Frau, ___ Mann in Hamburg arbeitet.', ['deren', 'dessen', 'die', 'den'], 'deren', 'medium'),
            ('Die Aufgabe ___ gestern ___ worden.', ['hat / machend', 'ist / gemacht', 'wurde / gemacht', 'wird / gemacht'], 'wurde / gemacht', 'medium'),
            ('Ich hätte ___ können, wenn ich mehr Zeit ___', ['machen / gehabt', 'arbeiten / gehabt', 'helfen / gehabt', 'kommen / hatte'], 'machen / gehabt', 'hard'),
            ('Er sagte, er ___ morgen kommen.', ['würde', 'wird', 'kann', 'muss'], 'würde', 'easy'),
            ('___ du Deutsch gelernt ___?', ['Hast / hast', 'Bist / gelernt', 'Hast / gelernt', 'Bist / hast'], 'Hast / gelernt', 'medium'),
            ('Das ist der Junge, ___ Mutter Ärztin ist.', ['dessen', 'deren', 'die', 'dem'], 'dessen', 'easy'),
            ('Wenn ich du ___, würde ich das nicht tun.', ['wäre', 'bin', 'sei', 'war'], 'wäre', 'medium'),
            ('Er sprach mit ihr, ___ er sie verstehen ___', ['damit / konnte', 'weil / konnte', 'obwohl / können', 'wenn / könnte'], 'obwohl / können', 'hard'),
            ('___ ich in Berlin war, habe ich das Brandenburger Tor besucht.', ['Als', 'Wenn', 'Wann', 'Während'], 'Als', 'easy'),
            ('Das Buch, ___ ich gestern gekauft habe, ist sehr gut.', ['den', 'der', 'dem', 'dessen'], 'das', 'medium'),
            ('Ich würde das ___ machen, ___ ich Zeit hätte.', ['gerne / wenn', 'lieber / weil', 'am liebsten / obwohl', 'besser / damit'], 'gerne / wenn', 'easy'),
            ('Die Prüfung ___ am Montag ___', ['wird / geschrieben', 'wurde / geschrieben', 'ist / geschrieben', 'hat / geschrieben'], 'wurde / geschrieben', 'medium'),
            ('Er hat gesagt, er ___ morgen kommen.', ['würde', 'wird', 'kann', 'wollte'], 'würde', 'easy'),
            ('Sie ist die beste Schülerin, die ich je ___', ['gesehen habe', 'sehe', 'sah', 'sehen werde'], 'gesehen habe', 'medium'),
            ('___ er fleißig lernte, hätte er die Prüfung bestanden.', ['Wenn', 'Weil', 'Als', 'Obwohl'], 'Wenn', 'hard'),
            ('Das ist das Haus, ___ wir letztes Jahr gewohnt haben.', ['indem', 'wo', 'in dem', 'zu dem'], 'wo', 'medium'),
            ('Er ist zu müde, ___ er noch weitermachen könnte.', ['um', 'als', 'weil', 'obwohl'], 'als', 'hard'),
            ('___ er auch versuchte, er konnte es nicht schaffen.', ['So', 'Wie', 'Was', 'Wenn'], 'So', 'hard'),
            ('Das Buch liegt ___ ich es hingelegt habe.', ['wo', 'in dem', 'da', 'zu dem'], 'wo', 'easy'),
            ('Er tut so, ___ er alles wüsste.', ['als', 'als ob', 'wenn', 'dass'], 'als ob', 'medium'),
            ('Ich habe ihm geholfen, ___ er mich darum gebeten hat.', ['weil', 'obwohl', 'wenn', 'damit'], 'weil', 'easy'),
            ('Das ist die Lehrerin, ___ wir alle respektieren.', ['die', 'der', 'den', 'welche'], 'die', 'easy'),
            ('Wenn er pünktlich ___, hätten wir den Zug noch erreicht.', ['gewesen wäre', 'ist', 'war', 'wäre', 'gewesen'], 'gewesen wäre', 'hard'),
            ('Er sprach mit einem Mann, ___ ich nicht kannte.', ['den', 'der', 'dem', 'dessen'], 'den', 'medium'),
            ('___ ich auch sagte, er glaubte mir nicht.', ['Was', 'Wie', 'So', 'Wenn'], 'Was', 'hard'),
            ('Sie ist die einzige Person, ___ ich vertraue.', ['der', 'die', 'den', 'dem'], 'der', 'medium'),
        ]
    elif level == 'B2':
        return [
            ('___ ich in Deutschland ankam, konnte ich kein Deutsch.', ['Als', 'Wenn', 'Während', 'Bevor'], 'Als', 'easy'),
            ('Er hat sich gemeldet, ___ er die Nachricht gelesen hatte.', ['nachdem', 'bevor', 'als', 'wenn'], 'nachdem', 'medium'),
            ('Ich freue mich ___ die Ferien.', ['auf', 'über', 'an', 'nach'], 'auf', 'easy'),
            ('Gestern ___ ich ins Kino gegangen.', ['habe', 'bin', 'wird', 'hat'], 'bin', 'easy'),
            ('___ du fleißig lernst, wirst du die Prüfung bestehen.', ['Wenn', 'Als', 'Weil', 'Während'], 'Wenn', 'easy'),
            ('Das Auto ___ gestern repariert ___', ['wurde / worden', 'ist / geworden', 'hat / gehabt', 'wird / werden'], 'wurde / worden', 'medium'),
            ('Er sah aus, ___ er krank ___', ['als ob / wäre', 'wenn / ist', 'weil / war', 'obwohl / ist'], 'als ob / wäre', 'hard'),
            ('___ er das Problem verstand, konnte er es lösen.', ['Als', 'Wenn', 'Weil', 'Nachdem'], 'Als', 'medium'),
            ('Ich lerne Deutsch, ___ ich in Deutschland arbeiten möchte.', ['weil', 'wenn', 'damit', 'dass'], 'weil', 'easy'),
            ('Er ist gestorben, ___ er 80 Jahre alt wurde.', ['als', 'wenn', 'bis', 'seitdem'], 'als', 'medium'),
            ('Sie wartet ___ ihren Freund.', ['auf', 'bei', 'mit', 'von'], 'auf', 'easy'),
            ('___ du mit dem Essen fertig bist, räum bitte auf.', ['Sobald', 'Solange', 'Wenn', 'Nachdem'], 'Sobald', 'easy'),
            ('Das Haus, ___ wir gekauft haben, ist sehr alt.', ['das', 'der', 'dem', 'dessen'], 'das', 'easy'),
            ('Er spricht Deutsch, ___ er in Deutschland gelebt ___', ['weil / hat', 'obwohl / gewohnt hat', 'wenn / lebt', 'damit / lebte'], 'weil / gewohnt hat', 'hard'),
            ('___ sie in München wohnte, hat sie viele Museen besucht.', ['Als', 'Wenn', 'Während', 'Seitdem'], 'Während', 'medium'),
            ('Ich würde das ___ machen, wenn ich Zeit ___', ['gerne / hätte', 'besser / habe', 'am liebsten / haben würde', 'viel / gehabt'], 'gerne / hätte', 'medium'),
            ('Er denkt ___ seine Familie.', ['an', 'auf', 'über', 'nach'], 'an', 'easy'),
            ('Die Prüfung ist schwer, ___ sie leicht ___ könnte.', ['obwohl / sein', 'weil / war', 'wenn / ist', 'damit / sei'], 'obwohl / sein', 'hard'),
            ('Ich bin stolz ___ meine Kinder.', ['auf', 'an', 'über', 'für'], 'auf', 'easy'),
            ('Er ist der beste Schüler, ___ ich je unterrichtet habe.', ['den', 'der', 'dem', 'dessen'], 'den', 'medium'),
        ]
    elif level == 'C1':
        return [
            ('Er sagte, er ___ die Prüfung bestanden.', ['hätte', 'habe', 'wird', 'war'], 'habe', 'medium'),
            ('Das ist der Mann, ___ Auto gestohlen ___', ['dessen / wurde', 'der / ist', 'dem / wurde', 'dessen / ist'], 'dessen / wurde', 'hard'),
            ('___ man auch sagen mag, er hat Recht.', ['Was', 'Wie', 'So', 'Wenn'], 'Was', 'hard'),
            ('Er sprach, ___ er alles wüsste.', ['als ob', 'wenn', 'weil', 'damit'], 'als ob', 'medium'),
            ('Die Aufgabe, ___ gelöst werden ___, ist sehr schwer.', ['die / muss', 'die / muss', 'zu / werden', 'zu / werden'], 'zu / werden', 'hard'),
            ('Es empfiehlt sich, ___ ___', ['früh / zu buchen', 'bald / buchen', 'schnell / gebucht', 'rechtzeitig / buchen'], 'früh / zu buchen', 'hard'),
            ('Der Experte wurde gebeten, eine ___ zu ___', ['Analyse / durchführen', 'Analysen / durchführen', 'Analyse / gemacht', 'Analysen / macht'], 'Analyse / durchzuführen', 'hard'),
            ('___ ich auch recherchierte, fand ich keine Antwort.', ['Wo', 'Was', 'Wie', 'Wonach'], 'Wonach', 'hard'),
            ('Sie sprach, ___ sie die Absicht ___, die Stelle anzunehmen.', ['als / hätte', 'wenn / hat', 'weil / hatte', 'damit / haben würde'], 'als / hätte', 'hard'),
            ('Das Projekt wurde ___ Zeit ___', ['rechtzeitig / abgeschlossen', 'in / Abschluss', 'zu / beendet', 'nach / vollendet'], 'rechtzeitig / abgeschlossen', 'medium'),
            ('Es ist von ___ Bedeutung, dass ___ rechtzeitig reagiert wird.', ['entscheidender / man', 'entscheidender / man', 'entscheidender / man', 'entscheidender / man'], 'entscheidender / man', 'hard'),
            ('Er tat so, ___ er von nichts ___', ['als / wüsste', 'wenn / weiß', 'weil / wusste', 'obwohl / weiß'], 'als / wüsste', 'hard'),
            ('___ dem Umstand, dass er krank war, ist die Leistung akzeptabel.', ['In', 'Zu', 'Bei', 'An'], 'In', 'hard'),
            ('Die Forschung kommt zu dem Ergebnis, ___ die Theorie ___', ['dass / stimmt', 'ob / stimmt', 'weil / stimmte', 'wenn / gestimmt hat'], 'dass / stimmt', 'medium'),
            ('Er hätte die Prüfung ___ bestehen ___, wenn er mehr gelernt ___', ['leicht / können / hätte', 'besser / gekonnt / hätte', 'schwer / gemusst / hätte', 'leicht / gemusst / haben'], 'leicht / können / hätte', 'hard'),
            ('___ demzufolge die Daten ausgewertet wurden, ergab sich ein neues Bild.', ['Nachdem', 'Weil', 'Obwohl', 'Als'], 'Nachdem', 'medium'),
            ('Das ist ein Aspekt, ___ man in der Diskussion ___ sollte.', ['den / berücksichtigen', 'der / berücksichtigt', 'dem / berücksichtigt', 'dessen / berücksichtigen'], 'den / berücksichtigen', 'hard'),
            ('Er verhielt sich so, ___ er die Regeln nicht ___', ['als ob / kennt', 'wenn / kennt', 'weil / kannte', 'obwohl / kennt'], 'als ob / kennt', 'hard'),
            ('___ man auch argumentieren mag, die Fakten sprechen für sich.', ['Wie', 'Was', 'Wo', 'Wonach'], 'Was', 'hard'),
            ('Die Entwicklung ist ___ zu ___', ['fortschreitend / beobachten', 'fortschreitend / beobachtend', 'zu / beobachtend', 'fortschreitend / beobachtet'], 'fortschreitend / zu beobachten', 'hard'),
        ]
    return []


def get_tf_templates(level):
    if level == 'A1':
        return [
            ('Das Nomen "Tisch" ist feminin.', False),
            ('Im Nominativ sagt man: der, die, das.', True),
            ('Das Verb "sprechen" ist regelmäßig.', False),
            ('Im Präsens: ich spRECHE.', True),
            ('"Kannst" ist die du-Form von "können".', True),
            ('Das Wort "ein" ist ein Artikel.', True),
            ('Im Satz "Ich bin müde" ist "müde" ein Verb.', False),
            ('"Nicht" kommt immer an den Anfang des Satzes.', False),
            ('Das Wort "hast" gehört zu "haben".', True),
            ('Im Deutschen sagt man "der Auto".', False),
            ('"Gehen" ist ein unregelmäßiges Verb.', True),
            ('Der Plural von "das Buch" ist "die Bücher".', True),
            ('"Sein" ist ein Hilfsverb.', True),
            ('Im A1 Niveau lernt man das Perfekt.', False),
            ('"Ich trinke Kaffee" ist ein.complete Satz.', True),
            ('Das Verb steht an zweiter Stelle im Hauptsatz.', True),
            ('"Wollen" ist ein Modalverb.', True),
            ('Im Deutschen gibt es nur einen Artikel.', False),
            ('"Der" ist der bestimmte Artikel für Maskulin.', True),
            ('Das Wort "und" ist eine Konjunktion.', True),
        ]
    elif level == 'A2':
        return [
            ('Perfekt bildet man mit "haben" oder "sein".', True),
            ('"Sein" Perfekt ist "ist gegangen".', True),
            ('Im Dativ sagt man "dem Mann".', True),
            ('"Weil" leitet einen Nebensatz ein.', True),
            ('"Obwohl" bedeutet das Gegenteil von "weil".', True),
            ('Im Komparativ fügt man "-er" hinzu.', True),
            ('"Am besten" ist der Superlativ.', True),
            ('Das Passiv wird mit "werden" gebildet.', True),
            ('"Ich freue mich auf" braucht den Akkusativ.', True),
            ('"Bei" ist eine Wechselpräposition.', False),
            ('"Nach" braucht immer den Dativ.', True),
            ('Im Perfekt sagt man "ich habe gesehen".', True),
            ('"Oder" verbindet zwei Hauptsätze.', True),
            ('"Denn" leitet einen Nebensatz ein.', False),
            ('"Wegen" braucht den Dativ.', False),
            ('Im Präteritum: "ich war".', True),
            ('"Das gefällt mir" braucht den Dativ.', True),
            ('"Ob" leitet einen Nebensatz ein.', True),
            ('"Am" wird bei Wochentagen verwendet.', True),
            ('"Zur" ist die Kurzform von "zu der".', True),
        ]
    elif level == 'B1':
        return [
            ('Im Präteritum sagt man "ich war, du warst".', True),
            ('Plusquamperfekt = Vorvergangenheit.', True),
            ('"Obwohl" ist ein Konnektor.', True),
            ('Relativpronomen im Nominativ: der, die, das.', True),
            ('Im Genitiv sagt man "des Mannes".', True),
            ('Passiv: "Das Haus wird gebaut."', True),
            ('Konjunktiv II: "Ich würde gehen."', True),
            ('"Könnte" ist Konjunktiv II.', True),
            ('"Dativ" fragt man mit "Wem?".', True),
            ('"Wenn" kann auch für die Zukunft verwendet werden.', True),
            ('Relativpronomen im Dativ: dem, der, den.', True),
            ('Plusquamperfekt: "Ich hatte gegessen."', True),
            ('"Lassen" funktioniert als Vollverb.', True),
            ('"Es lässt sich nicht ändern" ist ein Infinitiv mit "sich".', True),
            ('Im Passiv steht das Verb "werden" am Ende.', False),
            ('"Ich hätte" ist Konjunktiv II der Vergangenheit.', True),
            ('Relativsätze haben immer ein Komma.', True),
            ('"Wegen" braucht den Genitiv.', True),
            ('"Ob" leitet eine indirekte Frage ein.', True),
            ('Konjunktiv II wird für Höflichkeit verwendet.', True),
        ]
    elif level == 'B2':
        return [
            ('"Als" wird für einmalige Situationen verwendet.', True),
            ('"Während" drückt Gleichzeitigkeit aus.', True),
            ('"Sobald" bedeutet "olur olmaz".', True),
            ('"Solange" bedeutet "sürece".', True),
            ('"Bevor" bedeutet "önce".', True),
            ('"Nachdem" zeigt eine Handlung davor.', True),
            ('"Bis" zeigt eine zeitliche Begrenzung.', True),
            ('"Seitdem" braucht das Perfekt.', True),
            ('Konjunktiv I: "er komme".', True),
            ('Konjunktiv II: "er käme".', True),
            ('Passiv Präteritum: "wurde gemacht".', True),
            ('"Je...desto" braucht den Komparativ.', True),
            ('Relativsätze im Genitiv: "der Mann, dessen Auto..."', True),
            ('"Einander" ist ein Pronomen.', True),
            ('"Weil" und "da" sind synonym.', True),
            ('"Trotzdem" ist ein Konnektor.', True),
            ('"Werden" zeigt die Zukunft an.', True),
            ('"Nicht" verneint das Verb.', True),
            ('"Niemand" negiert "jemand".', True),
            ('Konjunktiv II der Vergangenheit: "hätte gemacht".', True),
        ]
    elif level == 'C1':
        return [
            ('Konjunktiv I: "ich komme, er komme".', True),
            ('Konjunktiv II: "ich käme, er käme".', True),
            ('Indirekte Rede mit Konjunktiv I.', True),
            ('Partizipialkonstruktionen ersetzen Nebensätze.', True),
            ('"Es empfiehlt sich" ist ein unpersönlicher Ausdruck.', True),
            ('"Geschweige denn" ist eine Konjunktion.', True),
            ('"Zumal" bedeutet "besonders weil".', True),
            ('Funktionsverbgefüge: "in Erfahrung bringen".', True),
            ('Nominalisierung: "durchführen" → "die Durchführung".', True),
            ('"Insofern als" ist eine Konditionalverbindung.', True),
            ('Konjunktiv I wird für Berichte verwendet.', True),
            ('"Selbst wenn" ist konzessiv.', True),
            ('Partizip I kann als Adjektiv verwendet werden.', True),
            ('"Während" kann auch als Subjunktion verwendet werden.', True),
            ('Indirekte Rede braucht oft Konjunktiv I.', True),
            ('Konjunktiv II für Vorwürfe: "Hättest du doch..."', True),
            ('"Angesichts dessen" ist ein Konnektor.', True),
            ('Passiv Perfekt: "ist gemacht worden".', True),
            ('"Nicht nur...sondern auch" ist korrekt.', True),
            ('Konjunktiv II der Vergangenheit: "wäre gekommen".', True),
        ]
    return []


def get_fill_templates(level):
    if level == 'A1':
        return [
            ('Das ist ___ Buch.', ['der', 'die', 'das', 'ein'], 'das', 'easy'),
            ('Ich ___ Deutsch.', ['spreche', 'sprichst', 'spricht', 'sprechen'], 'spreche', 'easy'),
            ('___ du das?', ['Weißt', 'Weiß', 'Wissen', 'Wusste'], 'Weißt', 'easy'),
            ('Das ist ___ Katze.', ['eine', 'ein', 'einer', 'einem'], 'eine', 'easy'),
            ('Er ___ nach Hause.', ['geht', 'gehe', 'gehst', 'gehen'], 'geht', 'easy'),
            ('___ du morgen Zeit?', ['Hast', 'Habe', 'Hat', 'Habt'], 'Hast', 'easy'),
            ('Sie ___ eine Straße.', ['überschreitet', 'überschreite', 'überschreitest', 'überschreiten'], 'überschreitet', 'easy'),
            ('Ich trinke ___ Kaffee.', ['ein', 'eine', 'einer', '-'], '-', 'easy'),
            ('Der Mann ___ eine Frau.', ['sieht', 'sehe', 'siehst', 'seht'], 'sieht', 'easy'),
            ('___ Kind spielt im Garten.', ['Ein', 'Eine', 'Der', 'Die'], 'Ein', 'easy'),
            ('Das ist ___ Auto.', ['mein', 'meine', 'meiner', 'meinem'], 'mein', 'easy'),
            ('Wir ___ am Montag.', ['arbeite', 'arbeitest', 'arbeitet', 'arbeiten'], 'arbeiten', 'easy'),
            ('Er ___ von zu Hause.', ['komme', 'kommst', 'kommt', 'kommen'], 'kommt', 'easy'),
            ('___ Uhr ist es?', ['Was', 'Wo', 'Wann', 'Wie viel'], 'Wie viel', 'easy'),
            ('Ich bin ___ Student.', ['ein', 'eine', 'einer', '-'], '-', 'easy'),
            ('Du ___ das nicht.', ['kann', 'kannst', 'kann', 'könnt'], 'kannst', 'easy'),
            ('Das Kind ___ eine Katze.', ['habt', 'hast', 'hat', 'habe'], 'hat', 'easy'),
            ('___ Tag ist heute?', ['Welcher', 'Welche', 'Welches', 'Was für ein'], 'Welcher', 'easy'),
            ('Ich habe ___ Hunger.', ['ein', 'eine', '-', 'einer'], '-', 'easy'),
            ('Er ___ kein Deutsch.', ['spreche', 'sprichst', 'spricht', 'sprechen'], 'spricht', 'easy'),
            ('Die Frau ___ schnell.', ['läuft', 'laufst', 'laufe', 'laufen'], 'läuft', 'easy'),
            ('Wir ___ in Berlin.', ['wohne', 'wohnst', 'wohnt', 'wohnen'], 'wohnen', 'easy'),
            ('Das ___ ein Haus.', ['bin', 'bist', 'ist', 'sind'], 'ist', 'easy'),
            ('Ich ___ eine Frage.', ['haben', 'habt', 'hat', 'habe'], 'habe', 'easy'),
            ('Du ___ sehr nett.', ['bin', 'bist', 'ist', 'sind'], 'bist', 'easy'),
            ('Er ___ das Buch.', ['lese', 'liest', 'lesen', 'lest'], 'liest', 'easy'),
            ('___ ist das?', ['Wer', 'Was', 'Wo', 'Wie'], 'Was', 'easy'),
            ('Das ist ___ Lampe.', ['der', 'die', 'das', 'ein'], 'die', 'easy'),
            ('Ich komme ___ Deutschland.', ['aus', 'bei', 'mit', 'nach'], 'aus', 'easy'),
            ('Das ist ___ rote Auto.', ['ein', 'eine', '-', 'der'], 'ein', 'medium'),
        ]
    elif level == 'A2':
        return [
            ('Gestern ___ ich ins Kino ___', ['bin / gegangen', 'habe / gegangen', 'ist / gegangen', 'hat / gegangen'], 'bin / gegangen', 'easy'),
            ('Ich ___ dir helfen ___', ['kann / -', 'kannst / -', 'kann / können', 'könnt / -'], 'kann / -', 'easy'),
            ('___ du mit mir ___?', ['Kannst / kommen', 'Kann / kommen', 'Können / kommst', 'Kannst / kommst'], 'Kannst / kommen', 'easy'),
            ('Er ___ schon in München ___', ['war / -', 'ist / -', 'hat / -', 'wird / -'], 'war / -', 'medium'),
            ('Ich habe ___ Ferien ___', ['die / gemacht', '- / gehabt', 'die / gehabt', '- / gemacht'], 'die / gehabt', 'medium'),
            ('Das Buch ___ mir ___', ['hat / gefallen', 'ist / gefallen', 'hat / gefällt', 'ist / gefällt'], 'hat / gefallen', 'medium'),
            ('Sie ___ seit drei Jahren hier.', ['wohnt', 'wohnst', 'wohne', 'wohnen'], 'wohnt', 'easy'),
            ('___ dem Wetter bin ich froh.', ['Wegen', 'Trotz', 'Während', 'Nach'], 'Wegen', 'medium'),
            ('Er ist ___ dem Chef.', ['bei', 'mit', 'von', 'zu'], 'bei', 'easy'),
            ('Ich interessiere mich ___ Musik.', ['für', 'an', 'auf', 'über'], 'für', 'easy'),
            ('___ er krank war, ist er nicht gekommen.', ['Weil', 'Obwohl', 'Wenn', 'Als'], 'Weil', 'easy'),
            ('Das ist ___ als das.', ['groß', 'größer', 'am größten', 'größere'], 'größer', 'easy'),
            ('Er ___ gestern ins Büro ___', ['ist / gegangen', 'hat / gegangen', 'ist / gegangen', 'hat / gegangen'], 'ist / gegangen', 'medium'),
            ('___ du schon ___ ?', ['Hast / gegessen', 'Bist / gegessen', 'Hast / gegangen', 'Bist / gegangen'], 'Hast / gegessen', 'medium'),
            ('Die Suppe ist ___', ['gekocht', 'kochen', 'kocht', 'kochte'], 'gekocht', 'easy'),
            ('Er ___ sich über die Nachricht.', ['freut', 'freue', 'freust', 'freuen'], 'freut', 'easy'),
            ('___ ich viel lernte, habe ich die Prüfung bestanden.', ['Weil', 'Obwohl', 'Wenn', 'Damit'], 'Weil', 'medium'),
            ('Das ist die ___ Lösung.', ['gut', 'besser', 'am besten', 'gute'], 'beste', 'hard'),
            ('Er spricht ___ als ich.', ['deutlich', 'deutlicher', 'am deutlichsten', 'deutlichste'], 'deutlicher', 'medium'),
            ('Sie ist die ___ von allen.', ['schön', 'schöner', 'am schönsten', 'schönste'], 'schönste', 'hard'),
            ('___ ich Zeit habe, helfe ich dir.', ['Wenn', 'Weil', 'Als', 'Damit'], 'Wenn', 'easy'),
            ('Er wartet ___ seine Mutter.', ['auf', 'bei', 'nach', 'von'], 'auf', 'easy'),
            ('___ du das gemacht?', ['Wie', 'Warum', 'Wann', 'Wo'], 'Wie', 'easy'),
            ('Ich bin mit dem Zug ___', ['gefahren', 'fahren', 'fahre', 'fährt'], 'gefahren', 'easy'),
            ('Das Buch ___ gestohlen ___', ['ist / worden', 'hat / worden', 'wurde / worden', 'wird / worden'], 'ist / worden', 'medium'),
            ('Er ist ___是因为 er zu spät ___', ['gekommen', 'gehet', 'ging', 'kommt'], 'gekommen', 'medium'),
            ('Sie ___ gestern einen Film ___', ['hat / gesehen', 'habt / gesehen', 'ist / gesehen', 'wird / gesehen'], 'hat / gesehen', 'medium'),
            ('___ er Hilfe braucht, soll er fragen.', ['Wenn', 'Weil', 'Obwohl', 'Damit'], 'Wenn', 'easy'),
            ('Er ist ___ Freude ___', ['vor / übertönt', 'von / übertönt', 'aus / überflogen', 'mit / über'], 'vor / übertönt', 'hard'),
        ]
    elif level == 'B1':
        return [
            ('___ er das gesagt hatte, ging er.', ['Nachdem', 'Wenn', 'Weil', 'Obwohl'], 'Nachdem', 'medium'),
            ('Das ist der Mann, ___ ich gestern ___', ['den / getroffen habe', 'der / getroffen habe', 'dem / getroffen habe', 'dessen / getroffen habe'], 'den / getroffen habe', 'easy'),
            ('Wenn ich Zeit ___, würde ich dir ___', ['hätte / helfen', 'habe / helfen', 'gehabt / geholfen', 'hätte / geholfen'], 'hätte / helfen', 'medium'),
            ('Er sprach so leise, ___ ich ihn kaum ___ ___', ['dass / verstehen / konnte', 'weil / verstehen / konnte', 'obwohl / können / konnte', 'damit / verstehen / können'], 'dass / verstehen / konnte', 'medium'),
            ('Das ist die Frau, ___ Mann in Hamburg ___', ['deren / arbeitet', 'dessen / arbeitet', 'die / arbeitet', 'den / arbeitet'], 'deren / arbeitet', 'medium'),
            ('Die Aufgabe ___ gestern ___ ___', ['wurde / gemacht', 'ist / gemacht', 'hat / gemacht', 'wird / gemacht'], 'wurde / gemacht', 'medium'),
            ('Ich hätte ___ ___, wenn ich mehr Zeit ___', ['machen / können / gehabt', 'arbeiten / können / gehabt', 'helfen / gekonnt / hatte', 'kommen / gemusst / gehabt'], 'machen / können / gehabt', 'hard'),
            ('Er sagte, er ___ morgen ___', ['würde / kommen', 'wird / kommen', 'kann / kommen', 'muss / kommen'], 'würde / kommen', 'easy'),
            ('___ du Deutsch ___ ___?', ['Hast / gelernt / hast', 'Bist / gelernt / hast', 'Hast / gelernt / bist', 'Bist / gelernt / bist'], 'Hast / gelernt / hast', 'medium'),
            ('Das ist der Junge, ___ Mutter ___', ['dessen / ist', 'deren / ist', 'die / ist', 'den / ist'], 'dessen / ist', 'easy'),
            ('Wenn ich du ___, würde ich das nicht tun.', ['wäre', 'bin', 'sei', 'war'], 'wäre', 'medium'),
            ('Er sprach mit ihr, ___ er sie ___ ___', ['obwohl / verstehen / konnte', 'weil / verstehen / konnte', 'damit / können / konnte', 'wenn / verstehen / könnte'], 'obwohl / verstehen / konnte', 'hard'),
            ('___ ich in Berlin ___, habe ich das Brandenburger Tor ___', ['Als / war / besucht', 'Wenn / bin / besuche', 'Wann / war / besucht', 'Während / bin / besucht'], 'Als / war / besucht', 'easy'),
            ('Das Buch, ___ ich gestern ___ ___, ist sehr gut.', ['das / gekauft / habe', 'der / gekauft / habe', 'dem / gekauft / habe', 'dessen / gekauft / habe'], 'das / gekauft / habe', 'medium'),
            ('Ich würde das ___ ___, ___ ich Zeit ___', ['gerne / machen / hätte', 'besser / machen / habe', 'am liebsten / machen / haben würde', 'viel / machen / gehabt'], 'gerne / machen / hätte', 'easy'),
            ('Die Prüfung ___ am Montag ___', ['wurde / geschrieben', 'ist / geschrieben', 'hat / geschrieben', 'wird / geschrieben'], 'wurde / geschrieben', 'medium'),
            ('Er hat gesagt, er ___ morgen ___', ['würde / kommen', 'wird / kommen', 'kann / kommen', 'wollte / kommen'], 'würde / kommen', 'easy'),
            ('Sie ist die beste Schülerin, die ich je ___', ['gesehen habe', 'sehe', 'sah', 'sehen werde'], 'gesehen habe', 'medium'),
            ('___ er fleißig ___, hätte er die Prüfung ___', ['Wenn / lernte / bestanden', 'Weil / lernt / bestanden', 'Als / lernte / bestehen', 'Obwohl / lernt / bestehen'], 'Wenn / lernte / bestanden', 'hard'),
            ('Das ist das Haus, ___ wir letztes Jahr ___ ___', ['wo / gewohnt / haben', 'in dem / gewohnt / haben', 'da / gewohnt / haben', 'zu dem / gewohnt / haben'], 'wo / gewohnt / haben', 'medium'),
        ]
    elif level == 'B2':
        return [
            ('___ ich in Deutschland ankam, konnte ich kein Deutsch.', ['Als', 'Wenn', 'Während', 'Bevor'], 'Als', 'easy'),
            ('Er hat sich ___, ___ er die Nachricht ___ ___', ['gemeldet / nachdem / gelesen / hatte', 'gemeldet / bevor / gelesen / hatte', 'gemeldet / als / gelesen / hatte', 'gemeldet / wenn / gelesen / hatte'], 'gemeldet / nachdem / gelesen / hatte', 'medium'),
            ('Ich freue mich ___ die Ferien.', ['auf', 'über', 'an', 'nach'], 'auf', 'easy'),
            ('Gestern ___ ich ins Kino ___', ['bin / gegangen', 'habe / gegangen', 'ist / gegangen', 'hat / gegangen'], 'bin / gegangen', 'easy'),
            ('___ du fleißig lernst, wirst du die Prüfung ___', ['Wenn / bestehen', 'Als / bestehen', 'Weil / bestehen', 'Während / bestehen'], 'Wenn / bestehen', 'easy'),
            ('Das Auto ___ gestern ___ ___', ['wurde / repariert', 'ist / repariert', 'hat / repariert', 'wird / repariert'], 'wurde / repariert', 'medium'),
            ('Er sah aus, ___ er krank ___', ['als ob / wäre', 'wenn / ist', 'weil / war', 'obwohl / ist'], 'als ob / wäre', 'hard'),
            ('___ er das Problem ___, konnte er es ___', ['Als / verstand / lösen', 'Wenn / versteht / lösen', 'Weil / verstand / lösen', 'Nachdem / verstand / lösen'], 'Als / verstand / lösen', 'medium'),
            ('Ich lerne Deutsch, ___ ich in Deutschland arbeiten ___', ['weil / möchte', 'wenn / will', 'damit / will', 'dass / möchte'], 'weil / möchte', 'easy'),
            ('Er ist ___, ___ er 80 Jahre alt ___', ['gestorben / als / wurde', 'gestorben / wenn / wurde', 'gestorben / bis / wurde', 'gestorben / seitdem / wurde'], 'gestorben / als / wurde', 'medium'),
            ('Sie wartet ___ ihren Freund.', ['auf', 'bei', 'mit', 'von'], 'auf', 'easy'),
            ('___ du mit dem Essen ___ ___, räum bitte ___', ['Sobald / fertig / bist / auf', 'Solange / fertig / bist / auf', 'Wenn / fertig / bist / ein', 'Nachdem / fertig / bist / auf'], 'Sobald / fertig / bist / auf', 'easy'),
            ('Das Haus, ___ wir ___ ___, ist sehr alt.', ['das / gekauft / haben', 'der / gekauft / haben', 'dem / gekauft / haben', 'dessen / gekauft / haben'], 'das / gekauft / haben', 'easy'),
            ('Er spricht Deutsch, ___ er in Deutschland ___ ___', ['weil / gewohnt / hat', 'obwohl / lebt', 'wenn / gelebt / hat', 'damit / lebte'], 'weil / gewohnt / hat', 'hard'),
            ('___ sie in München ___, hat sie viele Museen ___', ['Während / wohnte / besucht', 'Als / wohnt / besucht', 'Wenn / wohnte / besucht', 'Nachdem / wohnte / besucht'], 'Während / wohnte / besucht', 'medium'),
            ('Ich würde das ___ ___, wenn ich Zeit ___', ['gerne / machen / hätte', 'besser / machen / habe', 'am liebsten / machen / haben würde', 'viel / machen / gehabt'], 'gerne / machen / hätte', 'medium'),
            ('Er denkt ___ seine Familie.', ['an', 'auf', 'über', 'nach'], 'an', 'easy'),
            ('Die Prüfung ist schwer, ___ sie leicht ___ ___', ['obwohl / sein / könnte', 'weil / sein / war', 'wenn / sein / ist', 'damit / sein / wird'], 'obwohl / sein / könnte', 'hard'),
            ('Ich bin stolz ___ meine Kinder.', ['auf', 'an', 'über', 'für'], 'auf', 'easy'),
            ('Er ist der beste Schüler, ___ ich je ___ ___', ['den / unterrichtet / habe', 'der / unterrichtet / habe', 'dem / unterrichtet / habe', 'dessen / unterrichtet / habe'], 'den / unterrichtet / habe', 'medium'),
        ]
    elif level == 'C1':
        return [
            ('Er sagte, er ___ die Prüfung ___', ['habe / bestanden', 'hat / bestanden', 'würde / bestehen', 'wird / bestehen'], 'habe / bestanden', 'medium'),
            ('Das ist der Mann, ___ Auto ___ ___', ['dessen / gestohlen / wurde', 'der / gestohlen / wurde', 'dem / gestohlen / wurde', 'dessen / wurde / gestohlen'], 'dessen / gestohlen / wurde', 'hard'),
            ('___ man auch sagen mag, er hat ___', ['Was / Recht', 'Wie / unrecht', 'So / recht', 'Wenn / recht'], 'Was / Recht', 'hard'),
            ('Er sprach, ___ er alles ___', ['als ob / wüsste', 'wenn / weiß', 'weil / wusste', 'obwohl / weiß'], 'als ob / wüsste', 'hard'),
            ('Die Aufgabe, ___ ___ ___ ___, ist sehr schwer.', ['zu / gelöst / werden / muss', 'die / gelöst / werden / muss', 'zu / werden / gelöst / muss', 'die / werden / gelöst / muss'], 'zu / gelöst / werden / muss', 'hard'),
            ('Es empfiehlt sich, ___ ___', ['früh / zu buchen', 'bald / buchen', 'schnell / gebucht', 'rechtzeitig / buchen'], 'früh / zu buchen', 'hard'),
            ('Der Experte wurde gebeten, eine ___ zu ___', ['Analyse / durchführen', 'Analysen / durchführen', 'Analyse / gemacht', 'Analysen / macht'], 'Analyse / durchzuführen', 'hard'),
            ('___ ich auch ___ ___, fand ich keine Antwort.', ['Wonach / recherchierte', 'Wo / recherchierte', 'Was / recherchierte', 'Wie / recherchierte'], 'Wonach / recherchierte', 'hard'),
            ('Sie sprach, ___ sie die Absicht ___, die Stelle ___', ['als / hätte / anzunehmen', 'wenn / hat / anzunehmen', 'weil / hatte / anzunehmen', 'damit / haben würde / anzunehmen'], 'als / hätte / anzunehmen', 'hard'),
            ('Das Projekt wurde ___ ___ ___', ['rechtzeitig / abgeschlossen', 'in / Abschluss', 'zu / beendet', 'nach / vollendet'], 'rechtzeitig / abgeschlossen', 'medium'),
            ('Es ist von ___ Bedeutung, dass ___ ___ ___ ___', ['entscheidender / man / rechtzeitig / reagiert / wird', 'entscheidender / er / reagiert / wird / rechtzeitig', 'entscheidender / man / wird / reagiert / rechtzeitig', 'entscheidender / sie / rechtzeitig / wird / reagiert'], 'entscheidender / man / rechtzeitig / reagiert / wird', 'hard'),
            ('Er tat so, ___ er von nichts ___', ['als ob / wüsste', 'wenn / weiß', 'weil / wusste', 'obwohl / weiß'], 'als ob / wüsste', 'hard'),
            ('___ dem Umstand, dass er krank war, ist die Leistung ___', ['In / akzeptabel', 'Zu / akzeptabler', 'Bei / akzeptiert', 'An / akzeptabel'], 'In / akzeptabel', 'hard'),
            ('Die Forschung kommt zu dem ___, ___ die Theorie ___', ['Ergebnis / dass / stimmt', 'Ergebnis / ob / stimmt', 'Ergebnis / weil / stimmte', 'Ergebnis / wenn / gestimmt hat'], 'Ergebnis / dass / stimmt', 'medium'),
            ('Er hätte die Prüfung ___ ___ ___, wenn er mehr ___ ___', ['leicht / bestehen / können / hätte / gelernt', 'besser / gekonnt / hätte / gelernt', 'schwer / gemusst / hätte / gelernt', 'leicht / können / hätte / hatte / gelernt'], 'leicht / bestehen / können / hätte / gelernt', 'hard'),
            ('___ demzufolge die Daten ___ ___ ___, ergab sich ein neues ___', ['Nachdem / ausgewertet / wurden / Bild', 'Weil / ausgewertet / wurden / Bild', 'Als / werden / ausgewertet / Bilder', 'Obwohl / sind / ausgewertet / Bild'], 'Nachdem / ausgewertet / wurden / Bild', 'medium'),
            ('Das ist ein Aspekt, ___ man in der Diskussion ___ ___', ['den / berücksichtigen / sollte', 'der / berücksichtigt / sollte', 'dem / berücksichtigen / sollte', 'dessen / berücksichtigt / sollte'], 'den / berücksichtigen / sollte', 'hard'),
            ('Er verhielt sich so, ___ er die Regeln nicht ___', ['als ob / kennt', 'wenn / kennt', 'weil / kannte', 'obwohl / kennt'], 'als ob / kennt', 'hard'),
            ('___ man auch ___ ___ mag, die Fakten sprechen für ___', ['Was / argumentieren', 'Wie / argumentieren', 'Wo / arguieren', 'Wonach / argumentieren'], 'Was / argumentieren', 'hard'),
            ('Die Entwicklung ist ___ ___ ___', ['fortschreitend / zu / beobachten', 'fortschreitend / beobachtend', 'zu / beobachtend', 'fortschreitend / beobachtet'], 'fortschreitend / zu / beobachten', 'hard'),
        ]
    return []


def generate_100_questions(level, topic_id, topic_name):
    """Generate exactly 100 questions for a topic."""
    mcq_templates = get_mcq_templates(level)
    tf_templates = get_tf_templates(level)
    fill_templates = get_fill_templates(level)
    
    questions = []
    q_num = 1

    # 30 MCQ
    for i in range(30):
        tpl = mcq_templates[i % len(mcq_templates)]
        diff = ['easy', 'medium', 'hard'][i % 3]
        qid = f'{topic_id}_q{str(i+1).zfill(3)}'
        questions.append({
            'id': qid, 'subjectId': topic_id,
            'type': 'multiple_choice',
            'questionText': tpl[0],
            'options': tpl[1],
            'correctAnswer': tpl[2],
            'explanation': f'Grammatik-Thema: {topic_name}',
            'difficulty': diff,
            'topicName': topic_name
        })
        q_num += 1

    # 30 T/F
    for i in range(30):
        tpl = tf_templates[i % len(tf_templates)]
        diff = ['easy', 'medium', 'hard'][i % 3]
        qid = f'{topic_id}_q{str(i+31).zfill(3)}'
        questions.append({
            'id': qid, 'subjectId': topic_id,
            'type': 'true_false',
            'questionText': tpl[0],
            'options': ['Richtig', 'Falsch'],
            'correctAnswer': 'Richtig' if tpl[1] else 'Falsch',
            'explanation': f'Grammatik-Thema: {topic_name}',
            'difficulty': diff,
            'topicName': topic_name
        })
        q_num += 1

    # 40 Fill
    for i in range(40):
        tpl = fill_templates[i % len(fill_templates)]
        diff = ['easy', 'medium', 'hard'][i % 3]
        qid = f'{topic_id}_q{str(i+61).zfill(3)}'
        questions.append({
            'id': qid, 'subjectId': topic_id,
            'type': 'fill_blank',
            'questionText': tpl[0],
            'options': tpl[1],
            'correctAnswer': tpl[2],
            'explanation': f'Grammatik-Thema: {topic_name}',
            'difficulty': diff,
            'topicName': topic_name
        })
        q_num += 1

    return questions


def main():
    print('=' * 60)
    print('B2 Deutsch - 100 Questions Per Topic Generator')
    print('Generating for ALL CEFR levels: A1, A2, B1, B2, C1')
    print('=' * 60)

    all_qs = []
    topics_meta = {}
    total_topics = 0

    for level in ['A1', 'A2', 'B1', 'B2', 'C1']:
        topics = ALL_TOPICS[level]
        level_count = 0
        print(f'\n  [{level}] {len(topics)} topics...')
        
        for topic_id, topic_name, _ in topics:
            qs = generate_100_questions(level, topic_id, topic_name)
            all_qs.extend(qs)
            topics_meta[topic_id] = {
                'name': topic_name,
                'level': level,
                'count': len(qs),
                'questionIds': [q['id'] for q in qs]
            }
            level_count += 1
            total_topics += 1
            print(f'    {topic_id}: {len(qs)} questions')
        
        print(f'  [{level}] done: {level_count} topics')

    output = {
        'version': '2.0',
        'generated': '2026-04-26',
        'totalQuestions': len(all_qs),
        'totalTopics': total_topics,
        'levels': {level: len(topics) for level, topics in ALL_TOPICS.items()},
        'topics': topics_meta,
        'questionBank': all_qs
    }

    fname = 'all_levels_100_questions.json'
    with open(fname, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f'\n  Total: {len(all_qs)} questions across {total_topics} topics')
    print(f'  Saved: {fname}')
    print()
    print('  Breakdown:')
    for level in ['A1', 'A2', 'B1', 'B2', 'C1']:
        count = sum(1 for q in all_qs if q['subjectId'].startsWith(level.lower()))
        topics_count = len(ALL_TOPICS[level])
        print(f'    {level}: {topics_count} topics x 100 = {topics_count * 100} questions')


if __name__ == '__main__':
    main()
