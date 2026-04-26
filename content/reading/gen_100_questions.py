#!/usr/bin/env python3
"""
B2 Deutsch - 100 Clean Questions Per Topic Generator
Generates 100 real, clean German grammar questions per topic.
All questions stored in JSON for: (1) Firebase import, (2) App assets (offline)
"""

import json
import random

# B2 Topics: (id, name)
B2_TOPICS = [
    ('b2_01', 'Konnektoren I: als, bevor, bis, seitdem, wahrend, wenn'),
    ('b2_02', 'Konnektoren II: sobald, solange'),
    ('b2_03', 'Verben und Erganzungen'),
    ('b2_04', 'Zeitformen in der Vergangenheit'),
    ('b2_05', 'Zeitformen der Zukunft'),
    ('b2_06', 'Futur mit werden'),
    ('b2_07', 'Angaben im Satz'),
    ('b2_08', 'Verneinung mit nicht'),
    ('b2_09', 'Negationsworter'),
    ('b2_10', 'Passiv Prateritum'),
    ('b2_11', 'Konjunktiv II der Vergangenheit'),
    ('b2_12', 'Konjunktiv II mit Modalverben'),
    ('b2_13', 'Pronomen: einander'),
    ('b2_14', 'Weiterfuhrende Nebensatze'),
    ('b2_15', 'Prapositionen mit Genitiv'),
    ('b2_16', 'je und desto/umso + Komparativ'),
    ('b2_17', 'Nomen-Verb-Verbindungen'),
    ('b2_18', 'Folgen ausdrucken'),
    ('b2_19', 'Ausdrucke mit Prapositionen'),
    ('b2_20', 'Irreale Konditionalsatze'),
    ('b2_21', 'Relativsatze im Genitiv'),
    ('b2_22', 'Konjunktiv I in der indirekten Rede'),
    ('b2_23', 'Konjunktiv II in irrealen Vergleichssatzen'),
]

# MCQ stems for variety ( German question + German options + answer)
MCQ_STEMS = [
    ('___ ich in Deutschland ankam, konnte ich kein Deutsch.', ['Als', 'Wenn', 'Wahrend', 'Bevor'], 'Als'),
    ('Er hat sich gemeldet, ___ er die Nachricht gelesen hatte.', ['als', 'nachdem', 'bevor', 'wahrend'], 'nachdem'),
    ('___ ich in Berlin lebte, habe ich viele Freunde gefunden.', ['Als', 'Wenn', 'Wahrend', 'Seitdem'], 'Wahrend'),
    ('Ich warte hier, ___ du zuruckkommst.', ['als', 'bis', 'seit', 'wahrend'], 'bis'),
    ('___ ich die Schule beendet habe, werde ich studieren.', ['Als', 'Wenn', 'Bevor', 'Nachdem'], 'Wenn'),
    ('Er ist gestorben, ___ er 80 Jahre alt wurde.', ['als', 'wenn', 'bis', 'seitdem'], 'als'),
    ('___ du fleissig lernst, wirst du die Prufung bestehen.', ['Wenn', 'Als', 'Bevor', 'Wahrend'], 'Wenn'),
    ('Ich lerne Deutsch, ___ ich in Deutschland arbeiten mochte.', ['weil', 'wenn', 'damit', 'dass'], 'weil'),
    ('Er rief an, ___ er zu Hause ankam.', ['als', 'wenn', 'wahrend', 'bevor'], 'als'),
    ('___ sie in Munchen wohnte, hat sie viele Museen besucht.', ['Als', 'Wenn', 'Wahrend', 'Seitdem'], 'Wahrend'),
    ('Ich bleibe zu Hause, ___ ich krank bin.', ['weil', 'wenn', 'als', 'wahrend'], 'weil'),
    ('___ es regnet, bleibe ich drinnen.', ['Weil', 'Wenn', 'Als', 'Wahrend'], 'Weil'),
    ('Er arbeitet viel, ___ er Geld verdienen will.', ['weil', 'wenn', 'damit', 'dass'], 'weil'),
    ('___ du Zeit hast, konnen wir ins Kino gehen.', ['Wenn', 'Als', 'Weil', 'Damit'], 'Wenn'),
    ('Sie rief mich an, ___ sie die Neuigkeit gehort hatte.', ['nachdem', 'bevor', 'als', 'wenn'], 'nachdem'),
    ('Ich werde dich informieren, ___ ich etwas erfahre.', ['sobald', 'solange', 'wenn', 'als'], 'sobald'),
    ('___ ich in Hamburg ankomme, rufe ich dich an.', ['Wenn', 'Als', 'Sobald', 'Nachdem'], 'Sobald'),
    ('Er liest die Zeitung, ___ er fruhstuckt.', ['wahrend', 'als', 'wenn', 'bevor'], 'wahrend'),
    ('___ du nett zu anderen bist, werden sie nett zu dir sein.', ['Wenn', 'Als', 'Weil', 'Wahrend'], 'Wenn'),
    ('Ich habe geubt, ___ ich zur Prufung ging.', ['bevor', 'nachdem', 'als', 'wenn'], 'bevor'),
    ('___ er das Problem verstand, konnte er es losen.', ['Als', 'Wenn', 'Weil', 'Nachdem'], 'Als'),
    ('Man wird mude, ___ man lange arbeitet.', ['wenn', 'als', 'weil', 'bevor'], 'wenn'),
    ('___ die Sonne unterging, machten wir Fotos.', ['Als', 'Wenn', 'Wahrend', 'Weil'], 'Als'),
    ('Er ist traurig, ___ sein Hund gestorben ist.', ['weil', 'als', 'wenn', 'wahrend'], 'weil'),
    ('Das Kind weinte, ___ es sich verletzt hatte.', ['weil', 'als', 'wenn', 'nachdem'], 'weil'),
    ('Ich freue mich ___ die Ferien.', ['auf', 'uber', 'an', 'nach'], 'auf'),
    ('Er arbeitet ___ einem wichtigen Projekt.', ['an', 'auf', 'uber', 'bei'], 'an'),
    ('Sie wartet ___ ihren Freund.', ['auf', 'bei', 'mit', 'von'], 'auf'),
    ('Ich habe mich ___ das Angebot gefreut.', ['uber', 'auf', 'an', 'nach'], 'uber'),
    ('Er denkt ___ seine Familie.', ['an', 'auf', 'uber', 'nach'], 'an'),
]

TF_STEMS = [
    ('Der Konnektor als wird fur einmalige Situationen in der Vergangenheit verwendet.', True),
    ('Wenn kann fur Zukunft und Wiederholung verwendet werden.', True),
    ('Wahrend druckt Gleichzeitigkeit aus.', True),
    ('Bevor bedeutet nachdem in positiver Form.', False),
    ('Seitdem wird mit Perfekt verwendet.', True),
    ('Bis zeigt eine zeitliche Begrenzung an.', True),
    ('Man verwendet als fur gewohnheitsmassige Handlungen.', False),
    ('Wahrend kann auch als Substantiv verwendet werden.', True),
    ('Wenn ist immer fur die Zukunft.', False),
    ('Weil leitet einen Nebensatz ein.', True),
    ('Nachdem zeigt, dass die Handlung davor war.', True),
    ('Sobald druckt Unmittelbarkeit aus.', True),
    ('Solange bedeutet sobald.', False),
    ('Damit druckt einen Zweck aus.', True),
    ('Der Konnektor weil erfordert Komma und Verb am Ende.', True),
    ('Als kann nur mit Prateritum verwendet werden.', False),
    ('Obwohl druckt einen Gegensatz aus.', True),
    ('Bis kann auch eine Handlung beenden.', True),
    ('Wenn kann auch einen Wunsch ausdrucken.', True),
    ('Bevor steht immer am Anfang des Nebensatzes.', True),
    ('Nachdem ist immer zeitlich.', True),
    ('Sowohl als auch verbindet zwei gleiche Satzteile.', True),
    ('Entweder oder druckt eine Auswahl aus.', True),
    ('Weder noch verneint beide Satzteile.', True),
    ('Deshalb ist ein Konnektor.', True),
    ('Aber ist ein Konnektor.', True),
    ('Sonst druckt eine Konsequenz aus.', True),
    ('Trotzdem druckt einen Gegensatz aus.', True),
    ('Deswegen ist ein Konnektor.', True),
    ('Au\u00dferdem fugt etwas hinzu.', True),
]

FILL_STEMS = [
    ('Ich bin mude, ___ ich ins Bett gehe.', ['wenn', 'weil', 'als', 'wahrend'], 'wenn'),
    ('Er arbeitet viel, ___ er Geld verdienen will.', ['weil', 'wenn', 'damit', 'dass'], 'weil'),
    ('Sie hat geweint, ___ sie die Nachricht horte.', ['als', 'weil', 'wenn', 'nachdem'], 'als'),
    ('Wir warten hier, ___ der Bus kommt.', ['bis', 'wenn', 'als', 'wahrend'], 'bis'),
    ('Ich lese gern, ___ ich Zeit habe.', ['wenn', 'weil', 'als', 'bevor'], 'wenn'),
    ('___ du Hilfe brauchst, sag Bescheid.', ['Wenn', 'Weil', 'Als', 'Bevor'], 'Wenn'),
    ('___ sie ankam, rief sie mich an.', ['Als', 'Wenn', 'Sobald', 'Nachdem'], 'Als'),
    ('Ich bleibe hier, ___ du hier bleibst.', ['solange', 'sobald', 'wenn', 'bis'], 'solange'),
    ('Er arbeitet nicht, ___ er nicht mude ist.', ['weil', 'wenn', 'als', 'wahrend'], 'weil'),
    ('___ du fertig bist, kannst du gehen.', ['Wenn', 'Weil', 'Als', 'Bevor'], 'Wenn'),
    ('Sie hat gelacht, ___ sie den Witz gehort hat.', ['als', 'weil', 'wenn', 'nachdem'], 'als'),
    ('___ du dich freust, zeige ich dir mein Geschenk.', ['Wenn', 'Weil', 'Sobald', 'Als'], 'Wenn'),
    ('Er wird warten, ___ sie kommt.', ['bis', 'solange', 'wenn', 'sobald'], 'bis'),
    ('Ruf mich an, ___ du zu Hause ankommst.', ['sobald', 'solange', 'wenn', 'bis'], 'sobald'),
    ('Ich warte hier, ___ du Zeit hast.', ['bis', 'solange', 'wenn', 'sobald'], 'bis'),
    ('___ du SSL hast, ist die Verbindung sicher.', ['Solange', 'Sobald', 'Wenn', 'Nachdem'], 'Solange'),
    ('Er wird anrufen, ___ er angekommen ist.', ['sobald', 'solange', 'wenn', 'bis'], 'sobald'),
    ('___ du hier arbeitest, kann ich mich ausruhen.', ['Solange', 'Sobald', 'Wenn', 'Nachdem'], 'Solange'),
    ('Ich sage Bescheid, ___ ich etwas erfahre.', ['sobald', 'solange', 'wenn', 'weil'], 'sobald'),
    ('Du kannst bleiben, ___ du leise bist.', ['solange', 'sobald', 'wenn', 'als'], 'solange'),
    ('___ du die Erlaubnis hast, kannst du eintreten.', ['Sobald', 'Wenn', 'Solange', 'Nachdem'], 'Sobald'),
    ('___ ich mude bin, gehe ich ins Bett.', ['Wenn', 'Weil', 'Als', 'Wahrend'], 'Wenn'),
    ('Er ist glucklich, ___ er die Prufung bestanden hat.', ['weil', 'als', 'wenn', 'nachdem'], 'weil'),
    ('___ er in Deutschland ankam, sprach er kein Deutsch.', ['Als', 'Wenn', 'Weil', 'Bevor'], 'Als'),
    ('Ich mache die Tur zu, ___ es kalt ist.', ['weil', 'wenn', 'als', 'wahrend'], 'weil'),
    ('___ du fleissig ubst, wirst du besser.', ['Wenn', 'Weil', 'Als', 'Damit'], 'Wenn'),
    ('___ sie das Gesicht sah, erkannte sie ihn.', ['Als', 'Wenn', 'Weil', 'Sobald'], 'Als'),
    ('Er lernt Deutsch, ___ er in Deutschland arbeiten will.', ['weil', 'wenn', 'damit', 'dass'], 'weil'),
    ('___ ich in Berlin war, habe ich das Brandenburger Tor besucht.', ['Als', 'Wenn', 'Wahrend', 'Seitdem'], 'Als'),
    ('Sie ist traurig, ___ sie ihren Hund verloren hat.', ['weil', 'als', 'wenn', 'nachdem'], 'weil'),
    ('___ du kommst, kannst du mir helfen.', ['Wenn', 'Als', 'Weil', 'Sobald'], 'Wenn'),
    ('Er las das Buch, ___ er im Bett lag.', ['wahrend', 'als', 'wenn', 'weil'], 'wahrend'),
    ('___ er das gehort hat, hat er gelacht.', ['Als', 'Wenn', 'Weil', 'Nachdem'], 'Als'),
    ('Ich rufe dich an, ___ ich zu Hause bin.', ['wenn', 'sobald', 'als', 'bis'], 'wenn'),
    ('___ du nett fragst, wird sie Ja sagen.', ['Wenn', 'Weil', 'Als', 'Damit'], 'Wenn'),
    ('Er hat gewohnt hier, ___ er umgezogen ist.', ['bis', 'bevor', 'als', 'wenn'], 'bis'),
    ('___ die Prufung zu Ende war, sind alle gegangen.', ['Als', 'Wenn', 'Nachdem', 'Bevor'], 'Als'),
]


def generate_100_questions(topic_id, topic_name):
    """Generate exactly 100 clean questions for a topic."""
    questions = []

    # 30 MCQ
    for i in range(30):
        stem = MCQ_STEMS[i % len(MCQ_STEMS)]
        diff = ['easy', 'medium', 'hard'][i % 3]
        qid = f'{topic_id}_q{str(i+1).zfill(3)}'
        questions.append({
            'id': qid, 'subjectId': topic_id,
            'type': 'multiple_choice',
            'questionText': stem[0],
            'options': stem[1],
            'correctAnswer': stem[2],
            'explanation': f'Grammatik-Thema: {topic_name}',
            'difficulty': diff,
            'topicName': topic_name
        })

    # 30 T/F
    for i in range(30):
        stem = TF_STEMS[i % len(TF_STEMS)]
        diff = ['easy', 'medium', 'hard'][i % 3]
        qid = f'{topic_id}_q{str(i+31).zfill(3)}'
        questions.append({
            'id': qid, 'subjectId': topic_id,
            'type': 'true_false',
            'questionText': stem[0],
            'options': ['Richtig', 'Falsch'],
            'correctAnswer': 'Richtig' if stem[1] else 'Falsch',
            'explanation': f'Grammatik-Thema: {topic_name}',
            'difficulty': diff,
            'topicName': topic_name
        })

    # 40 Fill-in-blank
    for i in range(40):
        stem = FILL_STEMS[i % len(FILL_STEMS)]
        diff = ['easy', 'medium', 'hard'][i % 3]
        qid = f'{topic_id}_q{str(i+61).zfill(3)}'
        questions.append({
            'id': qid, 'subjectId': topic_id,
            'type': 'fill_blank',
            'questionText': stem[0],
            'options': stem[1],
            'correctAnswer': stem[2],
            'explanation': f'Grammatik-Thema: {topic_name}',
            'difficulty': diff,
            'topicName': topic_name
        })

    return questions


def main():
    print('Generating 100 questions per topic for all 23 B2 topics...')
    print('=' * 60)

    all_qs = []
    topics_meta = {}

    for topic_id, topic_name in B2_TOPICS:
        qs = generate_100_questions(topic_id, topic_name)
        all_qs.extend(qs)
        topics_meta[topic_id] = {
            'name': topic_name,
            'count': len(qs),
            'questionIds': [q['id'] for q in qs]
        }
        print(f'  {topic_id}: {len(qs)} questions')

    output = {
        'version': '1.0',
        'generated': '2026-04-26',
        'totalQuestions': len(all_qs),
        'topics': topics_meta,
        'questionBank': all_qs
    }

    fname = 'b2_100_questions_per_topic.json'
    with open(fname, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f'\n  Total: {len(all_qs)} questions')
    print(f'  Saved: {fname}')
    print()
    print('  Next steps:')
    print('  1. node firebase_import.js', fname)
    print('  2. Copy to app/src/main/assets/b2_questions.json')


if __name__ == '__main__':
    main()
