import json

with open('app/src/main/assets/a2_01.json') as f:
    data = json.load(f)

print(f"Current: {len(data['questions'])}")

new_qs = [
    {
        "id": "a2_01_q091",
        "subjectId": "a2_01",
        "topicId": "a2_01",
        "topicName": "Präteritum",
        "sourceId": "manual",
        "originalId": "manual_091",
        "level": "B2",
        "type": "multiple_choice",
        "questionText": "Während er gestern durch den Park ________, ________ er plötzlich einen alten Freund.",
        "options": [
            {"text": "spazierte / traf", "isCorrect": True},
            {"text": "spazieren / traf", "isCorrect": False},
            {"text": "spaziert / treffen", "isCorrect": False},
            {"text": "spazieren würde / traf", "isCorrect": False}
        ],
        "correctAnswer": "spazierte / traf",
        "explanation": "Präteritum is used to describe two simultaneous past events in a 'Während' (while) construction. 'Spazieren' (to stroll) is a weak verb: spazierte. 'Treffen' (to meet) is a strong verb with vowel change e→a: er traf. Both actions happened simultaneously in the past.",
        "questionNumber": 91
    },
    {
        "id": "a2_01_q092",
        "subjectId": "a2_01",
        "topicId": "a2_01",
        "topicName": "Präteritum",
        "sourceId": "manual",
        "originalId": "manual_092",
        "level": "B2",
        "type": "multiple_choice",
        "questionText": "Obwohl das Unternehmen letztes Jahr große Verluste ________, ________ es seine Mitarbeiter nicht entlassen.",
        "options": [
            {"text": "machte / konnte", "isCorrect": True},
            {"text": "gemacht hat / kann", "isCorrect": False},
            {"text": "machen würde / konnte", "isCorrect": False},
            {"text": "mache / kann", "isCorrect": False}
        ],
        "correctAnswer": "machte / konnte",
        "explanation": "Both 'machen' (to do/make) and the modal 'könen' (to be able to) use Präteritum in written German. 'Machen' → machte (weak verb Präteritum). 'Können' → konnte (modal verb Präteritum). Modal verbs regularly take Präteritum even in spoken German, making 'konnte' more natural here than 'kann'.",
        "questionNumber": 92
    },
    {
        "id": "a2_01_q093",
        "subjectId": "a2_01",
        "topicId": "a2_01",
        "topicName": "Präteritum",
        "sourceId": "manual",
        "originalId": "manual_093",
        "level": "B2",
        "type": "multiple_choice",
        "questionText": "Bevor die Wissenschaftler die Ergebnisse ________, ________ sie monatelang an den Experimenten ________.",
        "options": [
            {"text": "veröffentlichen / haben / gearbeitet", "isCorrect": False},
            {"text": "veröffentlichten / hatten / gearbeitet", "isCorrect": True},
            {"text": "veröffentlichen würden / haben / arbeiten", "isCorrect": False},
            {"text": "veröffentlicht / hatten / gearbeitet", "isCorrect": False}
        ],
        "correctAnswer": "veröffentlichten / hatten / gearbeitet",
        "explanation": "'Bevor' (before) introduces a temporal clause where the action before the main event uses Plusquamperfekt (hatten gearbeitet). The main clause uses Präteritum (veröffentlichten). The scientists had been working for months BEFORE publishing the results.",
        "questionNumber": 93
    },
    {
        "id": "a2_01_q094",
        "subjectId": "a2_01",
        "topicId": "a2_01",
        "topicName": "Präteritum",
        "sourceId": "manual",
        "originalId": "manual_094",
        "level": "B2",
        "type": "multiple_choice",
        "questionText": "Es ________, dass der Minister die Entscheidung bereits im Vorjahr ________ ________.",
        "options": [
            {"text": "hieß / getroffen", "isCorrect": False},
            {"text": "heißt / traf", "isCorrect": False},
            {"text": "hieß / getroffen hatte", "isCorrect": True},
            {"text": "heißt / getroffen", "isCorrect": False}
        ],
        "correctAnswer": "hieß / getroffen hatte",
        "explanation": "'Es hieß' means 'it was said/reported' (indirect information). The result clause uses Plusquamperfekt (hatte getroffen) because the decision was made even earlier than the reporting. This creates a past-within-past structure: decision made → then it was said.",
        "questionNumber": 94
    },
    {
        "id": "a2_01_q095",
        "subjectId": "a2_01",
        "topicId": "a2_01",
        "topicName": "Präteritum",
        "sourceId": "manual",
        "originalId": "manual_095",
        "level": "B2",
        "type": "multiple_choice",
        "questionText": "Während des gesamten Gesprächs ________ sie kein Wort, obwohl sie normalerweise sehr redselig ________.",
        "options": [
            {"text": "sagte / war", "isCorrect": True},
            {"text": "sagt / ist", "isCorrect": False},
            {"text": "sagen würde / wäre", "isCorrect": False},
            {"text": "gesagt / gewesen war", "isCorrect": False}
        ],
        "correctAnswer": "sagte / war",
        "explanation": "Präteritum describes a past habitual state: she was usually very talkative (war redselig), but during the conversation she didn't say a single word (sagte). The contrast is between normal behavior (war) and the specific past event (sagte).",
        "questionNumber": 95
    },
    {
        "id": "a2_01_q096",
        "subjectId": "a2_01",
        "topicId": "a2_01",
        "topicName": "Präteritum",
        "sourceId": "manual",
        "originalId": "manual_096",
        "level": "B2",
        "type": "multiple_choice",
        "questionText": "Als Kind ________ er jeden Sommer an die Ostsee, weil seine Eltern dort ein Ferienhaus ________.",
        "options": [
            {"text": "fuhr / hatten", "isCorrect": True},
            {"text": "fährt / haben", "isCorrect": False},
            {"text": "gefahren war / gehabt hatten", "isCorrect": False},
            {"text": "fahren würde / haben würden", "isCorrect": False}
        ],
        "correctAnswer": "fuhr / hatten",
        "explanation": "Präteritum describes a habitual past action (Als Kind = as a child): er fuhr jeden Sommer (he drove/goes every summer). 'Hatten' is Präteritum of 'haben' to describe the parents' possession of the holiday house in the past. Both are simple Präteritum — no Perfekt or Plusquamperfekt needed for these simultaneous past habits.",
        "questionNumber": 96
    },
    {
        "id": "a2_01_q097",
        "subjectId": "a2_01",
        "topicId": "a2_01",
        "topicName": "Präteritum",
        "sourceId": "manual",
        "originalId": "manual_097",
        "level": "B2",
        "type": "multiple_choice",
        "questionText": "Die Polizei ________ den Tatort, bevor die Journalisten ________ ________.",
        "options": [
            {"text": "sicherte / berichten", "isCorrect": False},
            {"text": "sichert / berichten durften", "isCorrect": False},
            {"text": "sicherte / berichten durften", "isCorrect": True},
            {"text": "hat gesichert / berichten konnten", "isCorrect": False}
        ],
        "correctAnswer": "sicherte / berichten durften",
        "explanation": "'Sichern' (to secure) is a weak verb: sicherte. The modal 'dürfen' (to be allowed to) in Präteritum is 'durften'. Before the police secured the scene, the journalists were NOT allowed to report. Präteritum + modal verb combination is standard in written German.",
        "questionNumber": 97
    },
    {
        "id": "a2_01_q098",
        "subjectId": "a2_01",
        "topicId": "a2_01",
        "topicName": "Präteritum",
        "sourceId": "manual",
        "originalId": "manual_098",
        "level": "B2",
        "type": "multiple_choice",
        "questionText": "________ du gewusst, dass er so reagieren ________, ________ du es ihm wahrscheinlich nicht erzählt.",
        "options": [
            {"text": "Hast / hat / hast", "isCorrect": False},
            {"text": "Hättest / hätte / hättest", "isCorrect": True},
            {"text": "Hättest / hätte / hättest", "isCorrect": True},
            {"text": "Hättest / hätte / hättest", "isCorrect": True}
        ],
        "correctAnswer": "Hättest / hätte / hättest",
        "explanation": "This is a conditional sentence with Konjunktiv II (Präteritum-based). The HÄTTE-construction expresses a hypothetical past condition: 'If you had known…' The inverted form 'Hättest du gewusst' (without 'Wenn') is the Würde-conversational form of Konjunktiv II. All three verbs use Konjunktiv II forms of Präteritum: hättest / hätte / hättest.",
        "questionNumber": 98
    },
    {
        "id": "a2_01_q099",
        "subjectId": "a2_01",
        "topicId": "a2_01",
        "topicName": "Präteritum",
        "sourceId": "manual",
        "originalId": "manual_099",
        "level": "B2",
        "type": "multiple_choice",
        "questionText": "Obwohl er versprochen ________, pünktlich zu kommen, ________ er erst eine Stunde später ________.",
        "options": [
            {"text": "hat / ist / angekommen", "isCorrect": False},
            {"text": "hatte / ist / angekommen", "isCorrect": False},
            {"text": "hatte / kam / an", "isCorrect": True},
            {"text": "habe / kam / an", "isCorrect": False}
        ],
        "correctAnswer": "hatte / kam / an",
        "explanation": "'Obwohl' (although) introduces a concessive clause. The past perfect 'hatte versprochen' (had promised) explains the expectation. The main clause uses simple Präteritum 'kam an' because it describes the actual past event. The modal 'kommen' with 'an-' is a separable verb: 'kam an' (Präteritum), 'ist angekommen' (Perfekt).",
        "questionNumber": 99
    },
    {
        "id": "a2_01_q100",
        "subjectId": "a2_01",
        "topicId": "a2_01",
        "topicName": "Präteritum",
        "sourceId": "manual",
        "originalId": "manual_100",
        "level": "B2",
        "type": "multiple_choice",
        "questionText": "Das Gebäude ________ im 19. Jahrhundert ________ und seitdem mehrmals renoviert ________.",
        "options": [
            {"text": "wurde / erbaut / worden", "isCorrect": True},
            {"text": "ist / erbaut / worden", "isCorrect": False},
            {"text": "wurde / erbauen / werden", "isCorrect": False},
            {"text": "war / erbaut / geworden", "isCorrect": False}
        ],
        "correctAnswer": "wurde / erbaut / worden",
        "explanation": "This is the Präteritum Passiv (passive voice in simple past). 'Wurde erbaut' = was built (Präteritum + Partizip II). The second part 'worden' is part of the Perfekt Passiv construction: 'ist renoviert worden' (has been renovated). Note: In Präteritum Passiv, the auxiliary is 'wurde/wurden', not 'ward/warden'.",
        "questionNumber": 100
    },
    {
        "id": "a2_01_q101",
        "subjectId": "a2_01",
        "topicId": "a2_01",
        "topicName": "Präteritum",
        "sourceId": "manual",
        "originalId": "manual_101",
        "level": "B2",
        "type": "multiple_choice",
        "questionText": "Wenn sie mehr Zeit ________ ________, ________ sie das Projekt sicherlich früher ________ ________ ________.",
        "options": [
            {"text": "gehabt / hätte / abgeschlossen", "isCorrect": True},
            {"text": "hatte / hat / abgeschlossen", "isCorrect": False},
            {"text": "gehabt / hat / abschließen", "isCorrect": False},
            {"text": "hätte / hätte / abschließen", "isCorrect": False}
        ],
        "correctAnswer": "gehabt / hätte / abgeschlossen",
        "explanation": "This is a conditional sentence (Konjunktiv II, Plusquamperfekt). The 'Wenn' clause uses Plusquamperfekt to express an unfulfilled past condition: 'If she had had more time…' The main clause uses Konjunktiv II with hättest/hätte: 'she would certainly have finished earlier.'",
        "questionNumber": 101
    },
    {
        "id": "a2_01_q102",
        "subjectId": "a2_01",
        "topicId": "a2_01",
        "topicName": "Präteritum",
        "sourceId": "manual",
        "originalId": "manual_102",
        "level": "B2",
        "type": "multiple_choice",
        "questionText": "Der Zeuge ________, dass der Angeklagte zum Tatzeitpunkt nicht am Tatort ________ ________ ________.",
        "options": [
            {"text": "behauptete / gewesen / sei", "isCorrect": False},
            {"text": "behauptet / gewesen / war", "isCorrect": False},
            {"text": "behauptete / gewesen / wäre", "isCorrect": True},
            {"text": "behauptet / gewesen / sei", "isCorrect": False}
        ],
        "correctAnswer": "behauptete / gewesen / wäre",
        "explanation": "This is indirect speech in past tense (indirekte Rede, Vergangenheit). The witness said the accused was not at the scene. The reporting verb 'behaupten' is in Präteritum (behauptete). The subordinate clause uses Konjunktiv II 'wäre' (from 'war/wären') because it reports information that cannot be verified — the accused supposedly was NOT there.",
        "questionNumber": 102
    },
    {
        "id": "a2_01_q103",
        "subjectId": "a2_01",
        "topicId": "a2_01",
        "topicName": "Präteritum",
        "sourceId": "manual",
        "originalId": "manual_103",
        "level": "B2",
        "type": "multiple_choice",
        "questionText": "Nachdem die Firma in Konkurs ________, ________ viele Mitarbeiter ihre Arbeitsplätze ________.",
        "options": [
            {"text": "gegangen war / haben / verloren", "isCorrect": False},
            {"text": "gegangen ist / hatten / verloren", "isCorrect": False},
            {"text": "gegangen war / hatten / verloren", "isCorrect": True},
            {"text": "ging / haben / verlieren", "isCorrect": False}
        ],
        "correctAnswer": "gegangen war / hatten / verloren",
        "explanation": "'Nachdem' (after) triggers Plusquamperfekt in the subordinate clause: 'Die Firma in Konkurs gegangen war.' The main clause also uses Plusquamperfekt 'hatten verloren' because the job losses were a direct consequence of the bankruptcy — both are completed before the narrative time.",
        "questionNumber": 103
    },
    {
        "id": "a2_01_q104",
        "subjectId": "a2_01",
        "topicId": "a2_01",
        "topicName": "Präteritum",
        "sourceId": "manual",
        "originalId": "manual_104",
        "level": "B2",
        "type": "multiple_choice",
        "questionText": "Es ________ lange, bis die Behörden auf die Beschwerde ________ ________ ________.",
        "options": [
            {"text": "dauerte / reagiert / haben", "isCorrect": False},
            {"text": "dauerte / reagiert / hatten", "isCorrect": True},
            {"text": "dauert / reagieren / würden", "isCorrect": False},
            {"text": "dauerte / reagieren / haben", "isCorrect": False}
        ],
        "correctAnswer": "dauerte / reagiert / hatten",
        "explanation": "'Es dauerte lange' (it took a long time) — Präteritum in the main clause. 'Bis' (until) introduces the result. The subordinate clause uses Plusquamperfekt 'reagiert hatten' because the authorities' reaction also happened in the past relative to the main narrative time.",
        "questionNumber": 104
    },
    {
        "id": "a2_01_q105",
        "subjectId": "a2_01",
        "topicId": "a2_01",
        "topicName": "Präteritum",
        "sourceId": "manual",
        "originalId": "manual_105",
        "level": "B2",
        "type": "multiple_choice",
        "questionText": "________ das Experiment misslang, ________ die Forscher ihre Hypothese ________ ________ ________.",
        "options": [
            {"text": "Weil / haben / überdenken", "isCorrect": False},
            {"text": "Da / mussten / überdenken", "isCorrect": True},
            {"text": "Wenn / würden / überdenken", "isCorrect": False},
            {"text": "Obwohl / konnten / überdenken", "isCorrect": False}
        ],
        "correctAnswer": "Da / mussten / überdenken",
        "explanation": "'Da' (because/since) introduces a causal clause. The experiment failed (misslang = Präteritum of misslingen), therefore the researchers HAD to reconsider their hypothesis. 'Müssen' in Präteritum is 'mussten' — expressing a past obligation. 'Überdenken' stays in infinitive after the modal.",
        "questionNumber": 105
    },
    {
        "id": "a2_01_q106",
        "subjectId": "a2_01",
        "topicId": "a2_01",
        "topicName": "Präteritum",
        "sourceId": "manual",
        "originalId": "manual_106",
        "level": "B2",
        "type": "multiple_choice",
        "questionText": "Bevor er die Stelle ________, ________ er bereits fünf Jahre im Ausland ________ ________ ________.",
        "options": [
            {"text": "antrat / hatte / gearbeitet", "isCorrect": True},
            {"text": "antritt / hat / gearbeitet", "isCorrect": False},
            {"text": "antreten würde / hatte / arbeiten", "isCorrect": False},
            {"text": "antrat / hat / arbeiten", "isCorrect": False}
        ],
        "correctAnswer": "antrat / hatte / gearbeitet",
        "explanation": "'Bevor' (before) introduces the subordinate clause with Plusquamperfekt: 'bevor er antrat' (before he took the position). The main clause 'hatte bereits fünf Jahre gearbeitet' (had already worked) uses Plusquamperfekt because the five years of working abroad were completed before he took the new job.",
        "questionNumber": 106
    },
    {
        "id": "a2_01_q107",
        "subjectId": "a2_01",
        "topicId": "a2_01",
        "topicName": "Präteritum",
        "sourceId": "manual",
        "originalId": "manual_107",
        "level": "B2",
        "type": "multiple_choice",
        "questionText": "Man ________ damals nicht, dass diese Erfindung die Welt so grundlegend ________ ________ ________.",
        "options": [
            {"text": "ahnte / verändern / würde", "isCorrect": True},
            {"text": "ahnt / verändern / wird", "isCorrect": False},
            {"text": "ahnte / verändert / hat", "isCorrect": False},
            {"text": "ahnte / verändern / werde", "isCorrect": False}
        ],
        "correctAnswer": "ahnte / verändern / würde",
        "explanation": "'Ahnte' is Präteritum of 'ahnen' (to suspect/guess). The 'dass' clause uses würde + Infinitiv (würde verändern) to express a future-in-the-past: they didn't suspect that this invention WOULD change the world so fundamentally. This is the würde-Konjunktiv form for future possibility in the past.",
        "questionNumber": 107
    },
    {
        "id": "a2_01_q108",
        "subjectId": "a2_01",
        "topicId": "a2_01",
        "topicName": "Präteritum",
        "sourceId": "manual",
        "originalId": "manual_108",
        "level": "B2",
        "type": "multiple_choice",
        "questionText": "Die Konferenz ________ planmäßig statt, obwohl mehrere Referenten kurzfristig ________ ________ ________.",
        "options": [
            {"text": "fand / abgesagt / haben", "isCorrect": False},
            {"text": "findet / absagen / würden", "isCorrect": False},
            {"text": "fand / abgesagt / hatten", "isCorrect": True},
            {"text": "fand / absagen / mussten", "isCorrect": False}
        ],
        "correctAnswer": "fand / abgesagt / hatten",
        "explanation": "'Fand statt' is Präteritum of 'stattfinden' (to take place). 'Obwohl' (although) introduces the contrast. The subordinate clause uses Plusquamperfekt 'hatten absagen müssen' (had to cancel) because the cancellation happened before the conference took place. The modal 'mussten' is integrated into the Plusquamperfekt form.",
        "questionNumber": 108
    },
    {
        "id": "a2_01_q109",
        "subjectId": "a2_01",
        "topicId": "a2_01",
        "topicName": "Präteritum",
        "sourceId": "manual",
        "originalId": "manual_109",
        "level": "B2",
        "type": "multiple_choice",
        "questionText": "________ er die Warnungen ernst genommen ________, ________ der Unfall vielleicht vermieden ________ ________ ________.",
        "options": [
            {"text": "Wenn / hätte / wäre / werden", "isCorrect": False},
            {"text": "Hätte / hätte / wäre / werden können", "isCorrect": True},
            {"text": "Wenn / hat / ist / werden", "isCorrect": False},
            {"text": "Hätte / hat / ist / werden", "isCorrect": False}
        ],
        "correctAnswer": "Hätte / hätte / wäre / werden können",
        "explanation": "This is an inverted conditional sentence (Konjunktiv II, Plusquamperfekt). 'Hätte er die Warnungen ernst genommen' = If he had taken the warnings seriously. The result clause uses Konjunktiv II 'wäre vermieden worden können' (would have been able to be avoided). Double passive-in-subjunctive: 'worden' is the past participle of 'werden' (the passive auxiliary).",
        "questionNumber": 109
    },
    {
        "id": "a2_01_q110",
        "subjectId": "a2_01",
        "topicId": "a2_01",
        "topicName": "Präteritum",
        "sourceId": "manual",
        "originalId": "manual_110",
        "level": "B2",
        "type": "multiple_choice",
        "questionText": "Während der gesamten Verhandlung ________ die Parteien keinen Kompromiss, bis der Vermittler einen neuen Vorschlag ________ ________ ________.",
        "options": [
            {"text": "fanden / unterbreitet / hat", "isCorrect": False},
            {"text": "fanden / unterbreitete", "isCorrect": True},
            {"text": "finden / unterbreiten / würde", "isCorrect": False},
            {"text": "fanden / unterbreitet / hatte", "isCorrect": False}
        ],
        "correctAnswer": "fanden / unterbreitet / hatte",
        "explanation": "'Bis' (until) introduces the point when the mediator finally made a proposal. The subordinate clause uses Plusquamperfekt 'unterbreitet hatte' because the proposal came after the prolonged negotiations. The main clause 'fanden keinen Kompromiss' uses Präteritum for the extended period of failed negotiations.",
        "questionNumber": 110
    }
]

data['questions'].extend(new_qs)
print(f"Updated: {len(data['questions'])}")

with open('app/src/main/assets/a2_01.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Done!")
