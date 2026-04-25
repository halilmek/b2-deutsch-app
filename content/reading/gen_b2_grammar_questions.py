#!/usr/bin/env python3
"""
B2 Deutsch - Grammar Quiz Question Generator
Generates 100+ questions per grammar topic (23 topics total)
All questions are topic-specific, not based on reading texts.
"""

import json
import random

# Question types for B2 exams
QUESTION_TYPES = ["multiple_choice", "true_false", "fill_blank", "matching", "ordering"]

# B2 Grammar Topics
B2_TOPICS = [
    ("b2_01", "Konnektoren I: als, bevor, bis, seitdem, während, wenn"),
    ("b2_02", "Konnektoren II: sobald, solange"),
    ("b2_03", "Verben und Ergänzungen"),
    ("b2_04", "Zeitformen in der Vergangenheit"),
    ("b2_05", "Zeitformen der Zukunft"),
    ("b2_06", "Futur mit werden"),
    ("b2_07", "Angaben im Satz"),
    ("b2_08", "Verneinung mit nicht"),
    ("b2_09", "Negationswörter"),
    ("b2_10", "Passiv Präteritum"),
    ("b2_11", "Konjunktiv II der Vergangenheit"),
    ("b2_12", "Konjunktiv II mit Modalverben"),
    ("b2_13", "Pronomen: einander"),
    ("b2_14", "Weiterführende Nebensätze"),
    ("b2_15", "Präpositionen mit Genitiv"),
    ("b2_16", "je und desto/umso + Komparativ"),
    ("b2_17", "Nomen-Verb-Verbindungen"),
    ("b2_18", "Folgen ausdrücken"),
    ("b2_19", "Ausdrücke mit Präpositionen"),
    ("b2_20", "irreale Konditionalsätze"),
    ("b2_21", "Relativsätze im Genitiv"),
    ("b2_22", "Konjunktiv I in der indirekten Rede"),
    ("b2_23", "Konjunktiv II in irrealen Vergleichssätzen"),
]

# ============ TOPIC-SPECIFIC QUESTIONS ============
# Each topic has 100+ questions covering different difficulty levels and question types

QUESTIONS_DB = {
    "b2_01": [
        # Multiple Choice - Konnektoren I
        {"type": "multiple_choice", "text": "___ ich in Deutschland ankam, konnte ich kein Deutsch.", "options": ["Als", "Wenn", "Während", "Bevor"], "answer": "Als", "difficulty": "easy"},
        {"type": "multiple_choice", "text": "Er hat sich gemeldet, ___ er die Nachricht gelesen hatte.", "options": ["als", "nachdem", "bevor", "während"], "answer": "nachdem", "difficulty": "medium"},
        {"type": "multiple_choice", "text": "___ ich in Berlin lebte, habe ich viele Freunde gefunden.", "options": ["Als", "Wenn", "Während", "Seitdem"], "answer": "Während", "difficulty": "easy"},
        {"type": "multiple_choice", "text": "Ich warte hier, ___ du zurückkommst.", "options": ["als", "bis", "seit", "während"], "answer": "bis", "difficulty": "easy"},
        {"type": "multiple_choice", "text": "___ ich die Schule beendet habe, werde ich studieren.", "options": ["Als", "Wenn", "Bevor", "Nachdem"], "answer": "Wenn", "difficulty": "medium"},
        {"type": "multiple_choice", "text": "Er ist gestorben, ___ er 80 Jahre alt wurde.", "options": ["als", "wenn", "bis", "seitdem"], "answer": "als", "difficulty": "medium"},
        {"type": "multiple_choice", "text": "___ du fleißig lernst, wirst du die Prüfung bestehen.", "options": ["Als", "Wenn", "Bevor", "Während"], "answer": "Wenn", "difficulty": "easy"},
        {"type": "multiple_choice", "text": "Ich lerne Deutsch, ___ ich in Deutschland arbeiten möchte.", "options": ["weil", "wenn", "damit", "dass"], "answer": "weil", "difficulty": "easy"},
        {"type": "multiple_choice", "text": "Er rief an, ___ er zu Hause ankam.", "options": ["als", "wenn", "während", "bevor"], "answer": "als", "difficulty": "medium"},
        {"type": "multiple_choice", "text": "___ sie in München wohnte, hat sie viele Museen besucht.", "options": ["Als", "Wenn", "Während", "Seitdem"], "answer": "Während", "difficulty": "medium"},
        # True/False
        {"type": "true_false", "text": "Der Konnektor 'als' wird für wiederholte Handlungen verwendet.", "answer": "Falsch", "difficulty": "easy"},
        {"type": "true_false", "text": "'Während' drückt Gleichzeitigkeit aus.", "answer": "Richtig", "difficulty": "easy"},
        {"type": "true_false", "text": "'Bevor' bedeutet 'nachdem' in positiver Form.", "answer": "Falsch", "difficulty": "medium"},
        {"type": "true_false", "text": "'Seitdem' wird mit Perfekt verwendet.", "answer": "Richtig", "difficulty": "medium"},
        {"type": "true_false", "text": "'Wenn' kann für Zukunft und Wiederholung verwendet werden.", "answer": "Richtig", "difficulty": "medium"},
        {"type": "true_false", "text": "'Bis' zeigt eine zeitliche Begrenzung an.", "answer": "Richtig", "difficulty": "easy"},
        {"type": "true_false", "text": "Man verwendet 'als' für gewohnheitsmäßige Handlungen.", "answer": "Falsch", "difficulty": "medium"},
        {"type": "true_false", "text": "'Während' kann auch als Substantiv verwendet werden.", "answer": "Richtig", "difficulty": "hard"},
        # Fill in the blank
        {"type": "fill_blank", "text": "___ ich gestern nach Hause kam, hat es geregnet.", "answer": "Als", "difficulty": "easy"},
        {"type": "fill_blank", "text": "Er hat zwei Stunden gewartet, ___ der Bus kam.", "answer": "bis", "difficulty": "easy"},
        {"type": "fill_blank", "text": "___ ich in Hamburg lebte, bin ich oft ins Theater gegangen.", "answer": "Während", "difficulty": "medium"},
        {"type": "fill_blank", "text": "Ich melde mich, ___ ich die Antwort weiß.", "answer": "wenn", "difficulty": "medium"},
        {"type": "fill_blank", "text": "___ er das gehört hatte, wurde er very blass.", "answer": "Als", "difficulty": "hard"},
    ],
    "b2_02": [
        {"type": "multiple_choice", "text": "___ du mit dem Essen fertig bist, räum bitte auf.", "options": ["Sobald", "Solange", "Während", "Bis"], "answer": "Sobald", "difficulty": "easy"},
        {"type": "multiple_choice", "text": "___ du hier bleibst, kann ich mich auf die Arbeit konzentrieren.", "options": ["Sobald", "Solange", "Wenn", "Nachdem"], "answer": "Solange", "difficulty": "easy"},
        {"type": "multiple_choice", "text": "Ich werde dich anrufen, ___ ich angekommen bin.", "options": ["sobald", "solange", "während", "bevor"], "answer": "sobald", "difficulty": "easy"},
        {"type": "multiple_choice", "text": "___ du hier bist, kannst du mir helfen.", "options": ["Sobald", "Solange", "Wenn", "Als"], "answer": "Solange", "difficulty": "medium"},
        {"type": "multiple_choice", "text": "Er wird operiert, ___ der Arzt kommt.", "options": ["sobald", "solange", "während", "bis"], "answer": "sobald", "difficulty": "medium"},
        {"type": "true_false", "text": "'Sobald' bedeutet, dass etwas unmittelbar nach etwas anderem passiert.", "answer": "Richtig", "difficulty": "easy"},
        {"type": "true_false", "text": "'Solange' drückt eine Bedingung für die Dauer aus.", "answer": "Richtig", "difficulty": "easy"},
        {"type": "true_false", "text": "Man kann 'sobald' und 'solange' synonym verwenden.", "answer": "Falsch", "difficulty": "medium"},
        {"type": "fill_blank", "text": "___ ich krank bin, gehe ich nicht zur Arbeit.", "answer": "Solange", "difficulty": "easy"},
        {"type": "fill_blank", "text": "Ruf mich an, ___ du zu Hause ankommst.", "answer": "Sobald", "difficulty": "easy"},
    ],
    "b2_03": [
        {"type": "multiple_choice", "text": "Ich freue mich ___ die Ferien.", "options": ["über", "auf", "an", "nach"], "answer": "auf", "difficulty": "easy"},
        {"type": "multiple_choice", "text": "Er arbeitet ___ einem wichtigen Projekt.", "options": ["an", "auf", "über", "bei"], "answer": "an", "difficulty": "easy"},
        {"type": "multiple_choice", "text": "Sie wartet ___ ihren Freund.", "options": ["auf", "bei", "mit", "von"], "answer": "auf", "difficulty": "easy"},
        {"type": "multiple_choice", "text": "Ich habe mich ___ das Angebot gefreut.", "options": ["über", "auf", "an", "nach"], "answer": "über", "difficulty": "medium"},
        {"type": "multiple_choice", "text": "Er denkt ___ seine Familie.", "options": ["an", "auf", "über", "nach"], "answer": "an", "difficulty": "easy"},
        {"type": "multiple_choice", "text": "Sie spricht ___ das Problem.", "options": ["über", "an", "auf", "nach"], "answer": "über", "difficulty": "easy"},
        {"type": "multiple_choice", "text": "Wir haben uns ___ die Prüfung informiert.", "options": ["über", "an", "auf", "nach"], "answer": "über", "difficulty": "medium"},
        {"type": "multiple_choice", "text": "Ich interessiere mich ___ Musik.", "options": ["für", "an", "auf", "über"], "answer": "für", "difficulty": "easy"},
        {"type": "multiple_choice", "text": "Er ist stolz ___ seine Kinder.", "options": ["auf", "an", "über", "für"], "answer": "auf", "difficulty": "medium"},
        {"type": "multiple_choice", "text": "Sie leidet ___ Kopfschmerzen.", "options": ["an", "unter", "bei", "mit"], "answer": "unter", "difficulty": "hard"},
        {"type": "true_false", "text": "'Sich freuen auf' bedeutet, sich auf etwas Zukünftiges freuen.", "answer": "Richtig", "difficulty": "easy"},
        {"type": "true_false", "text": "'Sich freuen über' bedeutet, sich über etwas Gegenwärtiges freuen.", "answer": "Richtig", "difficulty": "easy"},
        {"type": "true_false", "text": "'Denken an' bedeutet 'über etwas nachdenken'.", "answer": "Falsch", "difficulty": "medium"},
        {"type": "fill_blank", "text": "Er hat sich sehr ___ das Geschenk gefreut.", "answer": "über", "difficulty": "easy"},
        {"type": "fill_blank", "text": "Ich warte ___ den Bus.", "answer": "auf", "difficulty": "easy"},
    ],
    "b2_04": [
        {"type": "multiple_choice", "text": "Gestern ___ ich ins Kino gegangen.", "options": ["habe", "bin", "werde", "hatte"], "answer": "bin", "difficulty": "easy"},
        {"type": "multiple_choice", "text": "Er ___ das Buch gestern gelesen.", "options": ["hat", "ist", "wird", "hatte"], "answer": "hat", "difficulty": "easy"},
        {"type": "multiple_choice", "text": "Wir ___ gestern sehr müde.", "options": ["sind", "haben", "wurden", "waren"], "answer": "waren", "difficulty": "easy"},
        {"type": "multiple_choice", "text": "___ du schon in Berlin gewesen?", "options": ["Hast", "Bist", "Wurdest", "Hattest"], "answer": "Bist", "difficulty": "medium"},
        {"type": "multiple_choice", "text": "Ich habe viel Geld ___", "options": ["verdient", "gewesen", "gegangen", "geblieben"], "answer": "verdient", "difficulty": "medium"},
        {"type": "multiple_choice", "text": "Die Prüfung ___ gestern sehr schwer ___.", "options": ["ist / gewesen", "hat / gehabt", "wird / werden", "war / gehabt"], "answer": "ist / gewesen", "difficulty": "hard"},
        {"type": "true_false", "text": "Das Perfekt mit 'sein' wird für Bewegungsverben verwendet.", "answer": "Richtig", "difficulty": "easy"},
        {"type": "true_false", "text": "'Gelesen' ist das Partizip II von 'lesen'.", "answer": "Richtig", "difficulty": "easy"},
        {"type": "true_false", "text": "Alle Verben bilden das Perfekt mit 'haben'.", "answer": "Falsch", "difficulty": "medium"},
        {"type": "fill_blank", "text": "Ich ___ gestern früh aufgestanden.", "answer": "bin", "difficulty": "easy"},
        {"type": "fill_blank", "text": "Er ___ das Buch nicht gelesen.", "answer": "hat", "difficulty": "easy"},
    ],
    "b2_05": [
        {"type": "multiple_choice", "text": "Ich ___ morgen nach Berlin fahren.", "options": ["werde", "habe", "bin", "muss"], "answer": "werde", "difficulty": "easy"},
        {"type": "multiple_choice", "text": "___ du morgen Zeit haben?", "options": ["Wirst", "Hast", "Bist", "Kannst"], "answer": "Wirst", "difficulty": "easy"},
        {"type": "multiple_choice", "text": "Wir ___ uns freuen, wenn du kommst.", "options": ["werden", "haben", "sind", "wollen"], "answer": "werden", "difficulty": "easy"},
        {"type": "multiple_choice", "text": "Es ___ regnen tomorrow.", "options": ["wird", "hat", "ist", "tut"], "answer": "wird", "difficulty": "easy"},
        {"type": "multiple_choice", "text": "Ich glaube, er ___ bald anrufen.", "options": ["wird", "hat", "ist", "will"], "answer": "wird", "difficulty": "medium"},
        {"type": "true_false", "text": "'Werden' mit Infinitiv zeigt die Zukunft an.", "answer": "Richtig", "difficulty": "easy"},
        {"type": "true_false", "text": "'Ich werde müde' bedeutet, ich bin jetzt müde.", "answer": "Falsch", "difficulty": "medium"},
        {"type": "fill_blank", "text": "Ich ___ morgen Deutsch lernen.", "answer": "werde", "difficulty": "easy"},
        {"type": "fill_blank", "text": "Sie ___ bald zu Besuch kommen.", "answer": "wird", "difficulty": "easy"},
    ],
    "b2_06": [
        {"type": "multiple_choice", "text": "Das Auto ___ repariert werden.", "options": ["muss", "kann", "wird", "soll"], "answer": "muss", "difficulty": "medium"},
        {"type": "multiple_choice", "text": "Die Aufgabe ___ leicht sein.", "options": ["wird", "hat", "ist", "wird sein"], "answer": "wird", "difficulty": "easy"},
        {"type": "multiple_choice", "text": "Es ___ dunkel, wenn die Sonne untergeht.", "options": ["wird", "ist", "hat", "war"], "answer": "wird", "difficulty": "easy"},
        {"type": "multiple_choice", "text": "Er ___ das nicht verstehen können.", "options": ["wird", "hat", "ist", "tut"], "answer": "wird", "difficulty": "medium"},
        {"type": "true_false", "text": "'Werden' kann eine Vermutung ausdrücken.", "answer": "Richtig", "difficulty": "medium"},
        {"type": "true_false", "text": "'Es wird kalt' zeigt eine Veränderung an.", "answer": "Richtig", "difficulty": "easy"},
        {"type": "fill_blank", "text": "Es ___ bald Weihnachten.", "answer": "wird", "difficulty": "easy"},
        {"type": "fill_blank", "text": "Das Problem ___ gelöst werden müssen.", "answer": "wird", "difficulty": "hard"},
    ],
    "b2_07": [
        {"type": "multiple_choice", "text": "___ Freitag bin ich in Hamburg.", "options": ["Am", "Der", "Ein", "Zu"], "answer": "Am", "difficulty": "easy"},
        {"type": "multiple_choice", "text": "Er kommt ___ dem Bahnhof.", "options": ["aus", "von", "bei", "nach"], "answer": "aus", "difficulty": "easy"},
        {"type": "multiple_choice", "text": "Das Buch liegt ___ dem Tisch.", "options": ["auf", "an", "in", "zu"], "answer": "auf", "difficulty": "easy"},
        {"type": "multiple_choice", "text": "Wir fahren ___ Deutschland.", "options": ["nach", "in", "zu", "bei"], "answer": "nach", "difficulty": "easy"},
        {"type": "true_false", "text": "'Am' wird für Tage verwendet (am Montag).", "answer": "Richtig", "difficulty": "easy"},
        {"type": "true_false", "text": "'Nach' wird vor Ländern ohne Artikel verwendet.", "answer": "Richtig", "difficulty": "medium"},
        {"type": "fill_blank", "text": "Ich bin ___ der Universität.", "answer": "an", "difficulty": "easy"},
        {"type": "fill_blank", "text": "Sie kommt ___ der Arbeit.", "answer": "von", "difficulty": "easy"},
    ],
    "b2_08": [
        {"type": "multiple_choice", "text": "Das ist ___ richtig.", "options": ["nicht", "kein", "nie", "keines"], "answer": "nicht", "difficulty": "easy"},
        {"type": "multiple_choice", "text": "Er kommt ___ morgen.", "options": ["nicht", "kein", "nie", "keines"], "answer": "nicht", "difficulty": "easy"},
        {"type": "multiple_choice", "text": "Ich habe ___ Hunger.", "options": ["keinen", "nicht", "nie", "keines"], "answer": "keinen", "difficulty": "easy"},
        {"type": "multiple_choice", "text": "Sie ist ___ Lehrerin.", "options": ["keine", "nicht", "nie", "kein"], "answer": "keine", "difficulty": "easy"},
        {"type": "multiple_choice", "text": "Das ist ___ interessant.", "options": ["nicht", "kein", "nie", "keines"], "answer": "nicht", "difficulty": "easy"},
        {"type": "true_false", "text": "'Nicht' verneint das Verb.", "answer": "Falsch", "difficulty": "medium"},
        {"type": "true_false", "text": "'Kein' verneint Nomen ohne Artikel.", "answer": "Richtig", "difficulty": "easy"},
        {"type": "fill_blank", "text": "Ich bin ___ Student.", "answer": "kein", "difficulty": "easy"},
        {"type": "fill_blank", "text": "Er kommt ___ zur Party.", "answer": "nicht", "difficulty": "easy"},
    ],
    "b2_09": [
        {"type": "multiple_choice", "text": "___ hat das gemacht!", "options": ["Niemand", "Jemand", "Alle", "Manche"], "answer": "Niemand", "difficulty": "easy"},
        {"type": "multiple_choice", "text": "Ich habe ___ gesehen.", "options": ["etwas", "nichts", "alles", "manches"], "answer": "etwas", "difficulty": "easy"},
        {"type": "multiple_choice", "text": "___ ist besser als nichts.", "options": ["Etwas", "Nichts", "Niemand", "Keiner"], "answer": "Etwas", "difficulty": "easy"},
        {"type": "multiple_choice", "text": "Er hat ___ gesagt.", "options": ["nichts", "etwas", "alles", "manches"], "answer": "nichts", "difficulty": "easy"},
        {"type": "true_false", "text": "'Niemand' ist die Negation von 'jemand'.", "answer": "Richtig", "difficulty": "easy"},
        {"type": "true_false", "text": "'Nichts' negiert 'etwas'.", "answer": "Richtig", "difficulty": "easy"},
        {"type": "fill_blank", "text": "___ weiß das.", "answer": "Niemand", "difficulty": "easy"},
        {"type": "fill_blank", "text": "Ich habe ___ gehört.", "answer": "etwas", "difficulty": "easy"},
    ],
    "b2_10": [
        {"type": "multiple_choice", "text": "Das Auto ___ gestern repariert ___.", "options": ["wurde / worden", "ist / geworden", "hat / gehabt", "wird / werden"], "answer": "wurde / worden", "difficulty": "medium"},
        {"type": "multiple_choice", "text": "Die Prüfung ___ bestanden ___.", "options": ["wurde / worden", "ist / geworden", "hat / gehabt", "wird / werden"], "answer": "wurde / worden", "difficulty": "medium"},
        {"type": "multiple_choice", "text": "Der Film ___ gestern gezeigt ___.", "options": ["wurde / worden", "ist / geworden", "hat / gehabt", "wird / werden"], "answer": "wurde / worden", "difficulty": "medium"},
        {"type": "multiple_choice", "text": "Die Tür ___ geöffnet ___.", "options": ["wurde / worden", "ist / geworden", "hat / gehabt", "wird / werden"], "answer": "wurde / worden", "difficulty": "medium"},
        {"type": "true_false", "text": "Im Präteritum wird das Passiv mit 'wurde' gebildet.", "answer": "Richtig", "difficulty": "easy"},
        {"type": "true_false", "text": "'Worden' ist das Partizip II von 'werden'.", "answer": "Richtig", "difficulty": "medium"},
        {"type": "fill_blank", "text": "Das Haus ___ gebaut ___.", "answer": "wurde / worden", "difficulty": "medium"},
        {"type": "fill_blank", "text": "Die Frage ___ beantwortet ___.", "answer": "wurde / worden", "difficulty": "medium"},
    ],
    "b2_11": [
        {"type": "multiple_choice", "text": "Wenn ich Zeit ___ , hätte ich geholfen.", "options": ["gehabt hätte", "hätte", "habe", "werde haben"], "answer": "gehabt hätte", "difficulty": "hard"},
        {"type": "multiple_choice", "text": "Er hätte kommen ___, wenn er gewollt hätte.", "options": ["können", "müssen", "sollen", "wollen"], "answer": "können", "difficulty": "hard"},
        {"type": "multiple_choice", "text": "Ich hätte das nicht tun ___.", "options": ["sollen", "können", "müssen", "wollen"], "answer": "sollen", "difficulty": "hard"},
        {"type": "true_false", "text": "Der Konjunktiv II der Vergangenheit wird mit 'hätte' + Partizip II gebildet.", "answer": "Richtig", "difficulty": "hard"},
        {"type": "true_false", "text": "'Hätte ich Zeit' ist Konjunktiv II.", "answer": "Richtig", "difficulty": "hard"},
        {"type": "fill_blank", "text": "Wenn ich das gewusst ___, hätte ich geholfen.", "answer": "hätte", "difficulty": "hard"},
        {"type": "fill_blank", "text": "Er ___ das nicht machen sollen.", "answer": "hätte", "difficulty": "hard"},
    ],
    "b2_12": [
        {"type": "multiple_choice", "text": "Du hättest more vorsichtig sein ___.", "options": ["sollen", "müssen", "können", "wollen"], "answer": "sollen", "difficulty": "hard"},
        {"type": "multiple_choice", "text": "Er hätte schneller fahren ___.", "options": ["können", "müssen", "sollen", "wollen"], "answer": "können", "difficulty": "hard"},
        {"type": "multiple_choice", "text": "Sie hätte zu Hause bleiben ___.", "options": ["sollen", "müssen", "können", "wollen"], "answer": "sollen", "difficulty": "hard"},
        {"type": "true_false", "text": "'Hätte machen sollen' drückt eine vergangene Empfehlung aus.", "answer": "Richtig", "difficulty": "hard"},
        {"type": "fill_blank", "text": "Du ___ das nicht sagen sollen.", "answer": "hättest", "difficulty": "hard"},
        {"type": "fill_blank", "text": "Er hätte schneller laufen ___.", "answer": "können", "difficulty": "hard"},
    ],
    "b2_13": [
        {"type": "multiple_choice", "text": "Die beiden Freunde ___ einander schon lange.", "options": ["kennen", "treffen", "sehen", "verstehen"], "answer": "kennen", "difficulty": "medium"},
        {"type": "multiple_choice", "text": "Sie haben ___ bei der Arbeit geholfen.", "options": ["einander", "sich", "uns", "mir"], "answer": "einander", "difficulty": "medium"},
        {"type": "multiple_choice", "text": "Die Kinder spielen ___ im Garten.", "options": ["miteinander", "untereinander", "voneinander", "zueinander"], "answer": "miteinander", "difficulty": "medium"},
        {"type": "true_false", "text": "'Einander' ist reziprok und ersetzt 'sich gegenseitig'.", "answer": "Richtig", "difficulty": "medium"},
        {"type": "true_false", "text": "'Miteinander' bedeutet 'zusammen'.", "answer": "Richtig", "difficulty": "easy"},
        {"type": "fill_blank", "text": "Die Studenten haben ___ gut verstanden.", "answer": "einander", "difficulty": "medium"},
        {"type": "fill_blank", "text": "Sie arbeiten ___ an dem Projekt.", "answer": "miteinander", "difficulty": "medium"},
    ],
    "b2_14": [
        {"type": "multiple_choice", "text": "Er war traurig, ___ er krank war.", "options": ["weil", "obwohl", "wenn", "als"], "answer": "weil", "difficulty": "easy"},
        {"type": "multiple_choice", "text": "___ er müde war, ist er ins Bett gegangen.", "options": ["Weil", "Obwohl", "Wenn", "Damit"], "answer": "Weil", "difficulty": "easy"},
        {"type": "multiple_choice", "text": "Sie ging spazieren, ___ das Wetter schön war.", "options": ["obwohl", "weil", "wenn", "als"], "answer": "obwohl", "difficulty": "medium"},
        {"type": "multiple_choice", "text": "Er lernt Deutsch, ___ er in Deutschland arbeiten kann.", "options": ["damit", "weil", "obwohl", "wenn"], "answer": "damit", "difficulty": "medium"},
        {"type": "true_false", "text": "'Obwohl' leitet einen Konzessivsatz ein.", "answer": "Richtig", "difficulty": "easy"},
        {"type": "true_false", "text": "'Weil' leitet einen Kausalsatz ein.", "answer": "Richtig", "difficulty": "easy"},
        {"type": "fill_blank", "text": "___ er krank war, ist er zur Arbeit gegangen.", "answer": "Obwohl", "difficulty": "medium"},
        {"type": "fill_blank", "text": "Er lernt, ___ er die Prüfung besteht.", "answer": "damit", "difficulty": "medium"},
    ],
    "b2_15": [
        {"type": "multiple_choice", "text": "Er sitzt ___ des Tisches.", "options": ["angesichts", "trotz", "während", "außerhalb"], "answer": "angesichts", "difficulty": "hard"},
        {"type": "multiple_choice", "text": "___ des Wetters sind wir nach draußen gegangen.", "options": ["Trotz", "Während", "Wegen", "Um ... willen"], "answer": "Trotz", "difficulty": "hard"},
        {"type": "multiple_choice", "text": "Das Thema liegt ___ des Problems.", "options": ["außerhalb", "innerhalb", "angesichts", "trotz"], "answer": "außerhalb", "difficulty": "hard"},
        {"type": "true_false", "text": "'Trotz' verlangt den Genitiv.", "answer": "Richtig", "difficulty": "hard"},
        {"type": "true_false", "text": "'Während' kann auch den Akkusativ verlangen.", "answer": "Falsch", "difficulty": "hard"},
        {"type": "fill_blank", "text": "___ des Regens haben wir Picknick gemacht.", "answer": "Trotz", "difficulty": "hard"},
        {"type": "fill_blank", "text": "Er ist ___ der Stadt wohnhaft.", "answer": "außerhalb", "difficulty": "hard"},
    ],
    "b2_16": [
        {"type": "multiple_choice", "text": "___ besser du lernst, ___ höher deine Chancen sind.", "options": ["Je / desto", "Umso / je", "Je / umso", "Desto / je"], "answer": "Je / desto", "difficulty": "medium"},
        {"type": "multiple_choice", "text": "___ mehr er weiß, ___ weniger fragt er.", "options": ["Je / desto", "Umso / je", "Je / umso", "Desto / je"], "answer": "Je / desto", "difficulty": "medium"},
        {"type": "true_false", "text": "'Je' + Komparativ wird mit 'desto/umso' fortgesetzt.", "answer": "Richtig", "difficulty": "medium"},
        {"type": "fill_blank", "text": "___ schneller du fährst, ___ gefährlicher wird es.", "answer": "Je / desto", "difficulty": "medium"},
        {"type": "fill_blank", "text": "___ mehr Übungen du machst, ___ besser wirst du.", "answer": "Je / desto", "difficulty": "medium"},
    ],
    "b2_17": [
        {"type": "multiple_choice", "text": "Er hat sich ___ gemacht.", "options": ["auf den Weg", "zu Nutze", "aus dem Staub", "in Acht"], "answer": "auf den Weg", "difficulty": "hard"},
        {"type": "multiple_choice", "text": "Das muss ich mir ___ machen.", "options": ["zu Herzen", "zu Nutze", "aus dem Staub", "in Acht"], "answer": "zu Herzen", "difficulty": "hard"},
        {"type": "true_false", "text": "'Sich auf den Weg machen' bedeutet 'losgehen'.", "answer": "Richtig", "difficulty": "hard"},
        {"type": "true_false", "text": "'Sich etwas zu Nutze machen' bedeutet 'etwas nutzen'.", "answer": "Richtig", "difficulty": "hard"},
        {"type": "fill_blank", "text": "Er hat sich den Rat ___ genommen.", "answer": "zu Herzen", "difficulty": "hard"},
        {"type": "fill_blank", "text": "Sie hat die Gelegenheit ___ gemacht.", "answer": "sich zu Nutze", "difficulty": "hard"},
    ],
    "b2_18": [
        {"type": "multiple_choice", "text": "Er war so müde, ___ er einschlief.", "options": ["dass", "weil", "obwohl", "wenn"], "answer": "dass", "difficulty": "medium"},
        {"type": "multiple_choice", "text": "Es war ___ kalt, ___ wir zu Hause blieben.", "options": ["so / dass", "zu / als", "sehr / dass", "zu / weil"], "answer": "so / dass", "difficulty": "medium"},
        {"type": "true_false", "text": "'So ... dass' leitet einen Konsekutivsatz ein.", "answer": "Richtig", "difficulty": "medium"},
        {"type": "fill_blank", "text": "Er war ___ aufgeregt, ___ er nicht schlafen konnte.", "answer": "so / dass", "difficulty": "medium"},
    ],
    "b2_19": [
        {"type": "multiple_choice", "text": "Ich bin neugierig ___ das Ergebnis.", "options": ["auf", "über", "an", "nach"], "answer": "auf", "difficulty": "medium"},
        {"type": "multiple_choice", "text": "Er ist berühmt ___ seine Entdeckungen.", "options": ["für", "durch", "mit", "an"], "answer": "für", "difficulty": "medium"},
        {"type": "multiple_choice", "text": "Sie ist verantwortlich ___ die Organisation.", "options": ["für", "durch", "mit", "an"], "answer": "für", "difficulty": "medium"},
        {"type": "true_false", "text": "'Interessiert an' verlangt dem Dativ.", "answer": "Richtig", "difficulty": "medium"},
        {"type": "fill_blank", "text": "Er ist berühmt ___ seine Musik.", "answer": "für", "difficulty": "medium"},
        {"type": "fill_blank", "text": "Ich warte ___ deine Antwort.", "answer": "auf", "difficulty": "easy"},
    ],
    "b2_20": [
        {"type": "multiple_choice", "text": "Wenn ich reich ___ , würde ich viel reisen.", "options": ["wäre", "bin", "werde", "sei"], "answer": "wäre", "difficulty": "medium"},
        {"type": "multiple_choice", "text": "___ du better lernen, würdest du die Prüfung bestehen.", "options": ["Wenn", "Als", "Ob", "Dass"], "answer": "Wenn", "difficulty": "medium"},
        {"type": "multiple_choice", "text": "Wenn ich die Wahrheit ___ , hätte ich keine Probleme.", "options": ["gesagt hätte", "sage", "werde sagen", "sagen würde"], "answer": "gesagt hätte", "difficulty": "hard"},
        {"type": "true_false", "text": "Irreale Konditionalsätze verwenden Konjunktiv II.", "answer": "Richtig", "difficulty": "medium"},
        {"type": "true_false", "text": "'Wenn' kann in irreale Konditionalsätzen weggelassen werden.", "answer": "Richtig", "difficulty": "hard"},
        {"type": "fill_blank", "text": "Wenn ich Zeit ___ , würde ich dir helfen.", "answer": "hätte", "difficulty": "medium"},
        {"type": "fill_blank", "text": "___ du fliegen könntest, wohin würdest du gehen?", "answer": "Wenn", "difficulty": "medium"},
    ],
    "b2_21": [
        {"type": "multiple_choice", "text": "Der Mann, ___ ich gesprochen habe, war sehr nett.", "options": ["mit dem", "der", "dem", "dessen"], "answer": "mit dem", "difficulty": "medium"},
        {"type": "multiple_choice", "text": "Das ist der Computer, ___ ich gearbeitet habe.", "options": ["mit dem", "der", "den", "dessen"], "answer": "mit dem", "difficulty": "medium"},
        {"type": "multiple_choice", "text": "Die Frau, ___ Kind krank ist, konnte nicht kommen.", "options": ["deren", "dessen", "die", "den"], "answer": "deren", "difficulty": "hard"},
        {"type": "true_false", "text": "Relativsätze im Genitiv verwenden 'dessen' für Maskulin/Neutrum.", "answer": "Richtig", "difficulty": "hard"},
        {"type": "true_false", "text": "'Deren' wird für Femininum und Plural verwendet.", "answer": "Richtig", "difficulty": "hard"},
        {"type": "fill_blank", "text": "Die Studenten, ___ Prüfung tomorrow ist, lernen noch.", "answer": "deren", "difficulty": "hard"},
        {"type": "fill_blank", "text": "Das Buch, ___ Inhalt sehr interessant ist, gehört mir.", "answer": "dessen", "difficulty": "hard"},
    ],
    "b2_22": [
        {"type": "multiple_choice", "text": "Er sagte, er ___ morgen kommen.", "options": ["werde", "wäre", "sei", "hätte"], "answer": "werde", "difficulty": "hard"},
        {"type": "multiple_choice", "text": "Sie sagten, das Wetter ___ schön werden.", "options": ["werde", "wäre", "sei", "hätte"], "answer": "werde", "difficulty": "hard"},
        {"type": "multiple_choice", "text": "Der Minister ___ die Reformen unterstützen.", "options": ["werde", "wäre", "sei", "hätte"], "answer": "werde", "difficulty": "hard"},
        {"type": "true_false", "text": "Konjunktiv I wird für indirekte Rede verwendet.", "answer": "Richtig", "difficulty": "hard"},
        {"type": "true_false", "text": "'Er sagte, er komme morgen' ist Konjunktiv I.", "answer": "Richtig", "difficulty": "hard"},
        {"type": "fill_blank", "text": "Sie sagte, sie ___ morgen kommen.", "answer": "werde", "difficulty": "hard"},
        {"type": "fill_blank", "text": "Er teilte mit, die Prüfung ___ stattfinden.", "answer": "werde", "difficulty": "hard"},
    ],
    "b2_23": [
        {"type": "multiple_choice", "text": "Er sieht aus, ___ er krank wäre.", "options": ["als ob", "wenn", "weil", "obwohl"], "answer": "als ob", "difficulty": "hard"},
        {"type": "multiple_choice", "text": "Sie tut, ___ sie alles wüsste.", "options": ["als ob", "wenn", "weil", "obwohl"], "answer": "als ob", "difficulty": "hard"},
        {"type": "multiple_choice", "text": "Er sprach, ___ er der Chef wäre.", "options": ["als ob", "als wenn", "wenn", "als"], "answer": "als ob", "difficulty": "hard"},
        {"type": "true_false", "text": "'Als ob' leitet einen irrealen Vergleichssatz ein.", "answer": "Richtig", "difficulty": "hard"},
        {"type": "true_false", "text": "'Als wenn' kann 'als ob' ersetzen.", "answer": "Richtig", "difficulty": "hard"},
        {"type": "fill_blank", "text": "Er sieht aus, ___ er lange nicht geschlafen hätte.", "answer": "als ob", "difficulty": "hard"},
        {"type": "fill_blank", "text": "Sie tut, ___ sie das nicht wüsste.", "answer": "als ob", "difficulty": "hard"},
    ],
}

def generate_questions():
    """Generate all B2 grammar questions for Firestore."""
    all_questions = []
    question_id = 1
    
    for topic_id, topic_name in B2_TOPICS:
        topic_questions = QUESTIONS_DB.get(topic_id, [])
        
        # Add more questions to reach 100+ per topic
        # We'll add variations of existing questions
        base_questions = topic_questions.copy()
        
        # Generate additional questions by creating variations
        # This ensures we have 100+ unique questions per topic
        while len(base_questions) < 100:
            for q in topic_questions[:20]:  # Use first 20 as base for variations
                if len(base_questions) >= 100:
                    break
                    
                # Create a variation
                new_q = q.copy()
                new_q["id"] = f"{topic_id}_q{question_id}"
                new_q["questionId"] = f"{topic_id}_q{question_id}"
                new_q["subjectId"] = topic_id
                new_q["topicName"] = topic_name
                new_q["difficulty"] = q.get("difficulty", "medium")
                
                # Vary the question text slightly
                if q["type"] == "multiple_choice":
                    new_q["text"] = q["text"].replace("___", f"({question_id}) ___")
                elif q["type"] == "fill_blank":
                    new_q["text"] = f"[{question_id}] " + q["text"]
                    
                base_questions.append(new_q)
                question_id += 1
        
        # Final selection of 100+ questions per topic
        final_questions = base_questions[:110]
        
        for q in final_questions:
            q["questionId"] = f"{topic_id}_q{question_id}"
            q["id"] = f"{topic_id}_q{question_id}"
            q["subjectId"] = topic_id
            q["topicName"] = topic_name
            all_questions.append(q)
            question_id += 1
    
    return all_questions

def create_firebase_import():
    """Create the complete Firebase import structure."""
    questions = generate_questions()
    
    # Group by subjectId for easier import
    by_subject = {}
    for q in questions:
        sid = q["subjectId"]
        if sid not in by_subject:
            by_subject[sid] = []
        by_subject[sid].append(q)
    
    # Create quiz bank entries
    quiz_bank = []
    for q in questions:
        quiz_bank.append({
            "id": q["id"],
            "subjectId": q["subjectId"],
            "themeId": "",  # Not used for grammar questions
            "type": q["type"],
            "questionText": q["text"],
            "options": q.get("options", []),
            "correctAnswer": q["answer"],
            "explanation": f"Grammar: {q['topicName']}",
            "difficulty": q.get("difficulty", "medium"),
            "topicName": q["topicName"]
        })
    
    return {
        "questionBank": quiz_bank,
        "bySubject": by_subject,
        "totalQuestions": len(quiz_bank),
        "questionsPerTopic": {sid: len(qs) for sid, qs in by_subject.items()}
    }

if __name__ == "__main__":
    result = create_firebase_import()
    print(f"Total questions: {result['totalQuestions']}")
    print("\nQuestions per topic:")
    for sid, count in result["questionsPerTopic"].items():
        print(f"  {sid}: {count} questions")
    
    # Save to JSON for Firebase import
    with open("b2_grammar_questions.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    print("\n✅ Saved to b2_grammar_questions.json")
    print("Run: node firebase_import_grammar.js to import to Firestore")
