#!/usr/bin/env python3
import json, subprocess

# Read original from git (before any mangled translations)
result = subprocess.run(['git', 'show', 'HEAD:app/src/main/assets/a2_08.json'],
                       capture_output=True, text=True,
                       cwd='/home/node/.openclaw/workspace/b2-deutsch-app')
original = json.loads(result.stdout)

# ─── EXPLANATION TRANSLATIONS ───
translations = {
    "Plusquamperfekt: Nachdem cümlesinde önceki eylem (hatte + Partizip II).":
        "Plusquamperfekt: In a 'nachdem' clause, the earlier action uses Plusquamperfekt (hatte + Partizip II).",

    "abfahren (yer değiştirme): sein ile → Plusquamperfekt: war abgefahren.":
        "abfahren (change of location): uses sein → Plusquamperfekt: war abgefahren.",

    "lernen (geçişli): haben ile → Plusquamperfekt: hatte gelernt.":
        "lernen (transitive): uses haben → Plusquamperfekt: hatte gelernt.",

    "fliehen (yer değiştirme/durum değişikliği): sein ile → waren geflohen.":
        "fliehen (change of location/state): uses sein → Plusquamperfekt: waren geflohen.",

    "abschicken: önce gönderme işi bitti → Plusquamperfekt: hatte abgeschickt.":
        "abschicken: the sending was completed first → Plusquamperfekt: hatte abgeschickt.",

    "sinken (geçişsiz, azalma/düşme): sein ile → waren gesunken.":
        "sinken (intransitive, decrease/fall): uses sein → Plusquamperfekt: waren gesunken.",

    "sehen: geçmişte daha önce görme → Plusquamperfekt: hatte gesehen.":
        "sehen: seeing something earlier in the past → Plusquamperfekt: hatte gesehen.",

    "ankommen: varış eylemi daha önce gerçekleşti → Plusquamperfekt.":
        "ankommen: the arrival happened earlier → Plusquamperfekt.",

    "schlafen: yardımcı fiil haben → hatte geschlafen.":
        "schlafen: auxiliary verb haben → Plusquamperfekt: hatte geschlafen.",

    "beenden: 'Bitirmiş miydin?' → Plusquamperfekt sorusu: Hattest du beendet?":
        "beenden: 'Had you finished?' → Plusquamperfekt question: Hattest du beendet?",

    "ausziehen (yer değişikliği): sein ile → waren ausgezogen.":
        "ausziehen (change of location): uses sein → Plusquamperfekt: waren ausgezogen.",

    "ablehnen: reddetme eylemi pişmanlıktan önce → Plusquamperfekt.":
        "ablehnen: the rejection happened before the regret → Plusquamperfekt.",

    "sich legen (durum değişikliği): sein ile → Plusquamperfekt.":
        "sich legen (change of state): uses sein → Plusquamperfekt.",

    "sich trennen: dönüşlü fiiller daima haben ile → hatten getrennt.":
        "sich trennen: reflexive verbs always use haben → Plusquamperfekt: hatten getrennt.",

    "verfolgen (bir strateji izlemek): hadda verfolgt.":
        "verfolgen (to pursue/a strategy): uses haben → hatte verfolgt.",

    "erhalten: haberi alma anı, aramadan önce → Plusquamperfekt.":
        "erhalten: receiving the news, before the inquiry → Plusquamperfekt.",

    "frieren (doğa olayı): yardımcı fiil olarak haben tercih edilir → hatte gefroren.":
        "frieren (weather event): haben is preferred as auxiliary → hatte gefroren.",

    "lesen: okuma eylemi eksikliği → Plusquamperfekt: hatte gelesen.":
        "lesen: the reading action was lacking → Plusquamperfekt: hatte gelesen.",

    "abgeschlossen worden war":
        "war abgeschlossen worden",

    "Passiv Plusquamperfekt: war worden (worden = Partizip II von werden).":
        "Passiv Plusquamperfekt: war worden (worden = Partizip II of werden).",

    "stehlen: çalma eylemi şok olma anından önce → Plusquamperfekt.":
        "stehlen: the theft happened before the shock → Plusquamperfekt.",

    "vorschlagen: haben ile → Plusquamperfekt: hatte vorgelegt.":
        "vorschlagen: uses haben → Plusquamperfekt: hatte vorgelegt.",

    "übergreifen: yayılmak, yayılmış → haben ile kullanılır.":
        "übergreifen: to spread/extend → uses haben.",

    "ignorieren: görmezden gelmek → haben ile Plusquamperfekt.":
        "ignorieren: to ignore → uses haben → Plusquamperfekt.",

    "beginnen: başlamak → haben ile Plusquamperfekt: hatten begonnen.":
        "beginnen: to begin → uses haben → Plusquamperfekt: hatten begonnen.",

    "verlassen: terketmek → haben ile Plusquamperfekt.":
        "verlassen: to leave → uses haben → Plusquamperfekt.",

    "'kaum ... da' yapısında Plusquamperfekt → hatte angekündigt.":
        "'kaum ... da' structure with Plusquamperfekt → hatte angekündigt.",

    "obwohl ile zaman sırası: önce öğrenme → Plusquamperfekt.":
        "obwohl with time sequence: learning came first → Plusquamperfekt.",

    "manipulieren: geçmişte daha önce gerçekleşen eylem → Plusquamperfekt.":
        "manipulieren: an action that happened earlier in the past → Plusquamperfekt.",

    "abgeben: sunmak → haben ile Plusquamperfekt: hatten abgegeben.":
        "abgeben: to submit → uses haben → Plusquamperfekt: hatten abgegeben.",

    "einreichen: sunmak → haben ile Plusquamperfekt.":
        "einreichen: to submit → uses haben → Plusquamperfekt.",

    "fliehen (kaçmak): sein ile kullanılır → war geflohen.":
        "fliehen (to flee): uses sein → war geflohen.",

    "Konjunktiv II Vergangenheit — dolaylı anlatımda Plusquamperfekt.":
        "Konjunktiv II Vergangenheit — in indirect speech, Plusquamperfekt is used.",

    "abwägen: değerlendirmek → haben ile Plusquamperfekt.":
        "abwägen: to weigh/consider → uses haben → Plusquamperfekt.",

    "machen: ilişkili fiil → yapılmış olan eylem.":
        "machen: related verb → the action that had been done.",

    "Konjunktiv II Vergangenheit — koşul cümlesi.":
        "Konjunktiv II Vergangenheit — conditional clause.",

    "scheitern: başarısız olmak → sein ile → waren gescheitert.":
        "scheitern: to fail → uses sein → waren gescheitert.",

    "Präteritum + Plusquamperfekt kombinasyonu: schwiegen (Prät) + hatten gewusst.":
        "Präteritum + Plusquamperfekt combination: schwiegen (Prät) + hatten gewusst.",

    "Passiv Plusquamperfekt: vernichtet worden waren.":
        "Passiv Plusquamperfekt: vernichtet worden waren.",

    "Konjunktiv II Vergangenheit — karşı olgusal koşul.":
        "Konjunktiv II Vergangenheit — counterfactual condition.",

    "Insolvenz anmelden: haben ile Plusquamperfekt.":
        "Insolvenz anmelden: uses haben → Plusquamperfekt.",

    "hatte — Plusquamperfekt, beenden fiili haben ile.":
        "hatte — Plusquamperfekt, verb beenden uses haben.",

    "war — sein ile Plusquamperfekt (abfahren → sein).":
        "war — sein for Plusquamperfekt (abfahren → sein).",

    "hatte — Plusquamperfekt, finden fiili haben ile.":
        "hatte — Plusquamperfekt, verb finden uses haben.",

    "hatte — Plusquamperfekt, arbeiten fiili haben ile.":
        "hatte — Plusquamperfekt, verb arbeiten uses haben.",

    "konnten — Präteritum, können fiili.":
        "konnten — Präteritum of können.",

    "hatte — Plusquamperfekt, schlafen fiili haben ile.":
        "hatte — Plusquamperfekt, verb schlafen uses haben.",

    "veröffentlichten — Präteritum, veröffentlichen fiili.":
        "veröffentlichten — Präteritum of veröffentlichen.",

    "war — sein ile Plusquamperfekt (verschwinden → sein).":
        "war — sein for Plusquamperfekt (verschwinden → sein).",

    "hatte — Plusquamperfekt, lernen fiili haben ile.":
        "hatte — Plusquamperfekt, verb lernen uses haben.",

    "fanden — Präteritum, finden fiili.":
        "fanden — Präteritum of finden.",

    "hatte — Plusquamperfekt, sich vorbereiten have ile.":
        "hatte — Plusquamperfekt, verb sich vorbereiten uses haben.",

    "kamen — Präteritum, kommen fiili.":
        "kamen — Präteritum of kommen.",

    "hatte — Plusquamperfekt, erfahren fiili have ile.":
        "hatte — Plusquamperfekt, verb erfahren uses haben.",

    "hatten — Plusquamperfekt, spielen fiili have ile.":
        "hatten — Plusquamperfekt, verb spielen uses haben.",

    "begann — Präteritum, beginnen fiili.":
        "begann — Präteritum of beginnen.",

    "hatte — Plusquamperfekt, informieren fiili have ile.":
        "hatte — Plusquamperfekt, verb informieren uses haben.",

    "war — sein ile Plusquamperfekt (schließen → sein).":
        "war — sein for Plusquamperfekt (schließen → sein).",

    "verließen — Präteritum, verlassen fiili.":
        "verließen — Präteritum of verlassen.",

    "hatte — Plusquamperfekt, erklären fiili have ile.":
        "hatte — Plusquamperfekt, verb erklären uses haben.",

    "konnten — Präteritum, können fiili.":
        "konnten — Präteritum of können.",

    "Nachdem + Plusquamperfekt — önce gerçekleşen eylem.":
        "Nachdem + Plusquamperfekt — the action that happened first.",

    "Plusquamperfekt — Bevor'dan önceki eylem.":
        "Plusquamperfekt — the action before the 'Bevor' clause.",

    "Plusquamperfekt Passiv — war ausgeschaltet worden.":
        "Plusquamperfekt Passiv — war ausgeschaltet worden.",

    "Modal fiil + çift mastar (Ersatzinfinitiv), Plusquamperfekt: hatte aufschließen können.":
        "Modal verb + double infinitive (Ersatzinfinitiv), Plusquamperfekt: hatte aufschließen können.",

    "Nachdem + Plusquamperfekt.":
        "Nachdem + Plusquamperfekt.",

    "obwohl + Plusquamperfekt — önceki eylem.":
        "obwohl + Plusquamperfekt — the earlier action.",

    "abfahren — sein fiili ile, Plusquamperfekt: war abgefahren.":
        "abfahren — uses sein, Plusquamperfekt: war abgefahren.",

    "weil yan cümlesinde önceki eylem — Plusquamperfekt.":
        "weil subordinate clause — the earlier action → Plusquamperfekt.",

    "Plusquamperfekt — Bevor'dan önceki eylem.":
        "Plusquamperfekt — the action before the 'Bevor' clause.",

    "gekocht worden war":
        "war gekocht worden",

    "Plusquamperfekt Passiv — gekocht worden war.":
        "Plusquamperfekt Passiv — gekocht worden war.",

    "weil yan cümlesinde Plusquamperfekt.":
        "weil subordinate clause with Plusquamperfekt.",

    "verschlossen worden war":
        "war verschlossen worden",

    "Plusquamperfekt Passiv — dass yan cümlesinde.":
        "Plusquamperfekt Passiv — in a 'dass' subordinate clause.",

    "Plusquamperfekt — indirekt soru cümlesinde.":
        "Plusquamperfekt — in an indirect question clause.",

    "Nachdem + Plusquamperfekt.":
        "Nachdem + Plusquamperfekt.",

    "obwohl + Plusquamperfekt.":
        "obwohl + Plusquamperfekt.",

    "verbringen — have ile, Plusquamperfekt: hatte verbracht.":
        "verbringen — uses haben, Plusquamperfekt: hatte verbracht.",

    "weil yan cümlesinde Plusquamperfekt.":
        "weil subordinate clause with Plusquamperfekt.",

    "dass yan cümlesinde önceki eylem — Plusquamperfekt.":
        "'dass' subordinate clause — the earlier action → Plusquamperfekt.",

    "ankommen — sein fiili ile, Plusquamperfekt: waren angekommen.":
        "ankommen — uses sein, Plusquamperfekt: waren angekommen.",

    "dass yan cümlesinde Plusquamperfekt.":
        "'dass' subordinate clause with Plusquamperfekt.",
}

def translate(text):
    if not text:
        return text
    result = text
    for tr, en in sorted(translations.items(), key=lambda x: -len(x[0])):
        result = result.replace(tr, en)
    return result

translated_qs = []
for q in original['questions']:
    q = dict(q)
    q['explanation'] = translate(q.get('explanation', ''))
    q['sourceId'] = 'manual'
    translated_qs.append(q)

print(f"Translated {len(translated_qs)} questions")

# Spot check
for i in [0, 1, 4, 15, 31, 35, 63, 79]:
    q = translated_qs[i]
    print(f"Q{i+1}: [{q['correctAnswer']}] {q['explanation'][:100]}")

# ─── ADD 20 NEW QUESTIONS (q081-q100) ───
new_qs = [
    {
        "id": "a2_08_q081", "subjectId": "a2_08", "topicId": "a2_08", "topicName": "Plusquamperfekt",
        "sourceId": "manual", "originalId": "manual_081", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Bevor er das Buch ________, hatte er es schon drei Mal gelesen.",
        "options": ["gekauft hat", "gekauft", "kaufte", "wird kaufen"],
        "correctAnswer": "gekauft",
        "explanation": "Plusquamperfekt — 'bevor' introduces the later action, so the main clause uses Plusquamperfekt (hatte gekauft) for the action that happened first. In the shortened form, 'hatte' can be omitted: 'hatte er es schon drei Mal gelesen, bevor er es kaufte.'",
        "difficulty": "medium"
    },
    {
        "id": "a2_08_q082", "subjectId": "a2_08", "topicId": "a2_08", "topicName": "Plusquamperfekt",
        "sourceId": "manual", "originalId": "manual_082", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Nachdem die Prüfung ________, gingen die Studenten nach Hause.",
        "options": ["beendet war", "beendet wurde", "beendet worden war", "beendet hat"],
        "correctAnswer": "beendet war",
        "explanation": "Plusquamperfekt Passiv: 'beendet worden war' is the full form (war + Partizip II + worden). After 'nachdem', the earlier action uses Plusquamperfekt Passiv. The short form 'beendet war' is commonly used in spoken German.",
        "difficulty": "hard"
    },
    {
        "id": "a2_08_q083", "subjectId": "a2_08", "topicId": "a2_08", "topicName": "Plusquamperfekt",
        "sourceId": "manual", "originalId": "manual_083", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Ich ________ das Programm schon ________, bevor der Computer abstürzte.",
        "options": ["hatte / installiert", "habe / installiert", "war / installiert", "hatte / installieren"],
        "correctAnswer": "hatte / installiert",
        "explanation": "Plusquamperfekt: 'installieren' (transitive) uses haben. The installation had been completed before the crash. Structure: hatte + Partizip II + bevor clause.",
        "difficulty": "medium"
    },
    {
        "id": "a2_08_q084", "subjectId": "a2_08", "topicId": "a2_08", "topicName": "Plusquamperfekt",
        "sourceId": "manual", "originalId": "manual_084", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Er ________ nach Berlin ________, bevor er einen Job fand.",
        "options": ["war / gezogen", "hatte / gezogen", "zog / um", "war / umgezogen"],
        "correctAnswer": "war / gezogen",
        "explanation": "Plusquamperfekt with umziehen (change of residence): uses sein. 'war nach Berlin gezogen' = had moved to Berlin. The direction 'nach Berlin' requires 'sein', not 'haben'.",
        "difficulty": "medium"
    },
    {
        "id": "a2_08_q085", "subjectId": "a2_08", "topicId": "a2_08", "topicName": "Plusquamperfekt",
        "sourceId": "manual", "originalId": "manual_085", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Obwohl er viel ________, ________ er die Prüfung nicht bestanden.",
        "options": ["gelernt hatte / hatte", "gelernt hatte / hat", "lernte / hatte", "gelernt / hatte"],
        "correctAnswer": "gelernt hatte / hatte",
        "explanation": "obwohl + Plusquamperfekt: the learning (lernen, haben) had happened first, so 'hatte gelernt' in the obwohl clause. The main clause uses Präteritum or Perfekt. The tense sequence: past before past → Plusquamperfekt in the subordinate clause.",
        "difficulty": "hard"
    },
    {
        "id": "a2_08_q086",
        "subjectId": "a2_08", "topicId": "a2_08", "topicName": "Plusquamperfekt",
        "sourceId": "manual", "originalId": "manual_086", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Die Maschine ________ schon ________, bevor der Techniker kam.",
        "options": ["war / repariert worden", "hatte / repariert worden", "wurde / repariert", "hatte / repariert"],
        "correctAnswer": "war / repariert worden",
        "explanation": "Plusquamperfekt Passiv: the machine had been repaired before the technician came. 'war repariert worden' = was (state after action) + Partizip II + worden (process). The auxiliary 'werden' makes it passive.",
        "difficulty": "hard"
    },
    {
        "id": "a2_08_q087",
        "subjectId": "a2_08", "topicId": "a2_08", "topicName": "Plusquamperfekt",
        "sourceId": "manual", "originalId": "manual_087", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Sie ________ das Projekt ________, bevor die Deadline kam.",
        "options": ["hatte / abgeschlossen", "hatte / abzuschließen", "hat / abgeschlossen", "war / abgeschlossen"],
        "correctAnswer": "hatte / abgeschlossen",
        "explanation": "Plusquamperfekt: 'abgeschlossen' (Partizip II of abschließen, transitive, haben) had been completed before the deadline. 'Hatte abgeschlossen' = had completed.",
        "difficulty": "medium"
    },
    {
        "id": "a2_08_q088",
        "subjectId": "a2_08", "topicId": "a2_08", "topicName": "Plusquamperfekt",
        "sourceId": "manual", "originalId": "manual_088", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Kaum ________ er sich ________, ________ das Telefon.",
        "options": ["hatte / hingesetzt / klingelte", "hatte / hingesetzt / hat geklingelt", "setzte / hin / klingelte", "hatte / hingesetzt / war geklingelt"],
        "correctAnswer": "hatte / hingesetzt / klingelte",
        "explanation": "'kaum ... da' structure: barely had he sat down when the telephone rang. The main clause uses Präteritum (klingelte), the subordinate clause uses Plusquamperfekt (hatte sich hingesetzt). This is a specific German tense pattern for sudden sequential events.",
        "difficulty": "hard"
    },
    {
        "id": "a2_08_q089",
        "subjectId": "a2_08", "topicId": "a2_08", "topicName": "Plusquamperfekt",
        "sourceId": "manual", "originalId": "manual_089", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Die Sonne ________ schon ________, als wir ankamen.",
        "options": ["war / untergegangen", "hatte / untergegangen", "ging / unter", "war / untergehen"],
        "correctAnswer": "war / untergegangen",
        "explanation": "Plusquamperfekt with untergehen (setting of the sun): uses sein. 'war untergegangen' = had set. When describing two past events, the earlier one uses Plusquamperfekt and the later one uses Präteritum or Perfekt.",
        "difficulty": "easy"
    },
    {
        "id": "a2_08_q090",
        "subjectId": "a2_08", "topicId": "a2_08", "topicName": "Plusquamperfekt",
        "sourceId": "manual", "originalId": "manual_090", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Er ________ das Buch nicht ________, weil er es verloren ________.",
        "options": ["konnte / lesen / hatte", "konnte / lesen / hat", "hatte / gelesen / hatte", "konnte / gelesen / hatte"],
        "correctAnswer": "konnte / lesen / hatte",
        "explanation": "Modal verb + double infinitive (Ersatzinfinitiv) in Plusquamperfekt: 'hatte lesen können' = had been able to read. In Plusquamperfekt with modal verbs, the past participle of the modal is replaced by the infinitive. The loss (hatte verloren) is the earlier action.",
        "difficulty": "hard"
    },
    {
        "id": "a2_08_q091",
        "subjectId": "a2_08", "topicId": "a2_08", "topicName": "Plusquamperfekt",
        "sourceId": "manual", "originalId": "manual_091", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Wir ________ uns schon ________, bevor das Meeting begann.",
        "options": ["hatten / vorbereitet", "haben / vorbereitet", "hatten / vorzubereiten", "waren / vorbereitet"],
        "correctAnswer": "hatten / vorbereitet",
        "explanation": "Plusquamperfekt with sich vorbereiten (reflexive, transitive): uses haben. 'hatten uns vorbereitet' = had prepared ourselves. Reflexive verbs always use haben in Plusquamperfekt.",
        "difficulty": "medium"
    },
    {
        "id": "a2_08_q092",
        "subjectId": "a2_08", "topicId": "a2_08", "topicName": "Plusquamperfekt",
        "sourceId": "manual", "originalId": "manual_092", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Als ich ankam, ________ der Zug schon ________.",
        "options": ["war / abgefahren", "hatte / abgefahren", "ist / abgefahren", "war / abfahren"],
        "correctAnswer": "war / abgefahren",
        "explanation": "Plusquamperfekt with abfahren (departure, change of location): uses sein. 'war abgefahren' = had departed. When 'als' introduces a single past event and another event happened before it, Plusquamperfekt is used in the earlier clause.",
        "difficulty": "easy"
    },
    {
        "id": "a2_08_q093",
        "subjectId": "a2_08", "topicId": "a2_08", "topicName": "Plusquamperfekt",
        "sourceId": "manual", "originalId": "manual_093", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Bevor sie die Stelle ________, ________ sie fünf Jahre in Berlin ________.",
        "options": ["annahm / hatte / gelebt", "annahm / hat / gelebt", "nahm an / hatte / gelebt", "nahm an / lebte"],
        "correctAnswer": "annahm / hatte / gelebt",
        "explanation": "'bevor' connects two actions; the one BEFORE 'bevor' uses Plusquamperfekt with hatten + Partizip II. Here 'hatte in Berlin gelebt' = had lived in Berlin. The later action (annahm) is in Präteritum.",
        "difficulty": "medium"
    },
    {
        "id": "a2_08_q094",
        "subjectId": "a2_08", "topicId": "a2_08", "topicName": "Plusquamperfekt",
        "sourceId": "manual", "originalId": "manual_094", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Nachdem das Feuer ________ ________, kam die Feuerwehr.",
        "options": ["gelöscht worden war", "hatte / gelöscht", "war / gelöscht worden", "wurde / gelöscht"],
        "correctAnswer": "gelöscht worden war",
        "explanation": "Plusquamperfekt Passiv: the fire had been extinguished before the fire brigade came. 'war gelöscht worden' = was (state) + Partizip II (löschen) + worden (passive auxiliary). The shorter form 'gelöscht worden war' is common in spoken German.",
        "difficulty": "hard"
    },
    {
        "id": "a2_08_q095",
        "subjectId": "a2_08", "topicId": "a2_08", "topicName": "Plusquamperfekt",
        "sourceId": "manual", "originalId": "manual_095", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Er ________ die Nachricht ________, bevor er ins Bett ________.",
        "options": ["hatte / gelesen / ging", "hat / gelesen / ging", "las / hatte / gegangen", "hatte / gelesen / war gegangen"],
        "correctAnswer": "hatte / gelesen / ging",
        "explanation": "Plusquamperfekt with lesen (transitive, haben). The reading had happened before going to bed. 'Ging' (Präteritum of gehen) is used for the later action. Note: 'ins Bett gehen' uses sein (ging), but here the subject went to bed — the going is the later action, not the Plusquamperfekt.",
        "difficulty": "medium"
    },
    {
        "id": "a2_08_q096",
        "subjectId": "a2_08", "topicId": "a2_08", "topicName": "Plusquamperfekt",
        "sourceId": "manual", "originalId": "manual_096", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Obwohl die Firma viel ________, ________ sie Insolvenz anmelden ________.",
        "options": ["investiert hatte / musste", "investierte / hatte / anzumelden", "hatte / investiert / anzumelden", "investierte / investiert / anzumelden"],
        "correctAnswer": "investiert hatte / musste",
        "explanation": "obwohl + Plusquamperfekt: the investment had happened before the necessity to declare insolvency. 'Hatte investiert' (Plusquamperfekt) is in the obwohl clause. The main clause 'musste Insolvenz anmelden' uses Präteritum of müssen.",
        "difficulty": "hard"
    },
    {
        "id": "a2_08_q097",
        "subjectId": "a2_08", "topicId": "a2_08", "topicName": "Plusquamperfekt",
        "sourceId": "manual", "originalId": "manual_097", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Kaum ________ wir Platz ________, ________ die Vorstellung auch schon ________.",
        "options": ["hatten / genommen / begann", "hatten / genommen / hat begonnen", "haben / genommen / begann", "hatten / eingenommen / begann"],
        "correctAnswer": "hatten / genommen / begann",
        "explanation": "'kaum ... da' structure: barely had we taken our seats when the performance already began. Main clause: Präteritum (begann), subordinate: Plusquamperfekt (hatten Platz genommen). 'Platz nehmen' = to take a seat.",
        "difficulty": "hard"
    },
    {
        "id": "a2_08_q098",
        "subjectId": "a2_08", "topicId": "a2_08", "topicName": "Plusquamperfekt",
        "sourceId": "manual", "originalId": "manual_098", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Das Kind ________ schon ________, bevor die Eltern kamen.",
        "options": ["war / eingeschlafen", "hatte / eingeschlafen", "hat / eingeschafen", "war / schlafen"],
        "correctAnswer": "war / eingeschlafen",
        "explanation": "Plusquamperfekt with einschlafen (to fall asleep, change of state): uses sein. 'War eingeschlafen' = had fallen asleep. The child was already asleep before the parents arrived.",
        "difficulty": "easy"
    },
    {
        "id": "a2_08_q099",
        "subjectId": "a2_08", "topicId": "a2_08", "topicName": "Plusquamperfekt",
        "sourceId": "manual", "originalId": "manual_099", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Nachdem die Regierung die Maßnahmen ________ ________, besserten sich die Zahlen.",
        "options": ["ergriffen hatte", "hatte ergriffen", "ergriffen worden war", "hatte / ergriffen"],
        "correctAnswer": "ergriffen hatte",
        "explanation": "Plusquamperfekt: after the government had taken the measures, the numbers improved. 'Ergriffen' (Partizip II of ergreifen, transitive, haben) uses hatte + Partizip II. The 'had taken' happened before the improvement.",
        "difficulty": "medium"
    },
    {
        "id": "a2_08_q100",
        "subjectId": "a2_08", "topicId": "a2_08", "topicName": "Plusquamperfekt",
        "sourceId": "manual", "originalId": "manual_100", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Er ________ das Angebot ________, aber er ________ es sich noch einmal ________.",
        "options": ["hatte / abgelehnt / hätte / überlegen sollen", "hat / abgelehnt / sollte / überlegen", "hatte / abgelehnt / sollte / überlegen", "hat / abgelehnt / hätte / überlegt"],
        "correctAnswer": "hatte / abgelehnt / hätte / überlegen sollen",
        "explanation": "Konjunktiv II Vergangenheit (past counterfactual): 'Er hätte es sich überlegen sollen' = he should have reconsidered it (but didn't). 'Hatte abgelehnt' is Plusquamperfekt for the earlier action. The contrast between the rejection and the unfulfilled reconsideration creates the counterfactual meaning.",
        "difficulty": "hard"
    },
]

translated_qs.extend(new_qs)
print(f"\nTotal after adding 20: {len(translated_qs)}")

# ─── ADD DESCRIPTION AND TIPS ───
description = (
    "Plusquamperfekt (Past Perfect) describes an action that happened BEFORE another past action. "
    "It is the past equivalent of Perfekt. While Perfekt relates a past action to the present, "
    "Plusquamperfekt relates two past actions to each other — showing that one happened first. "
    "It is mainly used in subordinate clauses introduced by 'nachdem', 'bevor', 'als', 'weil', 'obwohl', "
    "or after 'kaum ... da'."
)

tips = (
    "KEY RULES:\n"
    "1. How to form Plusquamperfekt:\n"
    "   - With haben: hatte / hattest / hatte / hatten + Partizip II\n"
    "   - With sein: war / warst / war / waren + Partizip II\n\n"
    "2. When to use Plusquamperfekt:\n"
    "   - After 'nachdem' (after): the action in the 'nachdem' clause is always BEFORE the main clause.\n"
    "     Example: Nachdem er gegessen hatte, ging er. (He ate first, THEN went.)\n"
    "   - After 'bevor' (before): the main clause action is first.\n"
    "     Example: Er ging, bevor er gegessen hatte. (He went first, THEN ate.)\n"
    "   - After 'als' (when): for a single past event that happened before another.\n"
    "     Example: Als ich angekommen war, begann die Besprechung.\n\n"
    "3. sein vs. haben:\n"
    "   - Verbs of movement (change of place): sein — e.g., gehen, fahren, fliegen, kommen, abfahren, ankommen, umziehen\n"
    "   - Reflexive verbs: always haben — e.g., sich vorbereiten, sich trennen, sich hinlegen\n"
    "   - Weather verbs (as events): haben — e.g., geregnet, geschneit\n"
    "   - All transitive/intransitive verbs without movement: haben\n\n"
    "4. Passive Plusquamperfekt:\n"
    "   war / waren + Partizip II + worden (short form: Partizip II + worden war)\n"
    "   Example: Das Haus war schon verkauft worden.\n\n"
    "5. Modal verb + infinitive (Ersatzinfinitiv) in Plusquamperfekt:\n"
    "   hatte / hattest / hatte / hatten + Infinitive (NOT Partizip II)\n"
    "   Example: Er hatte das nicht machen können. (NOT 'gemacht gekonnt')\n\n"
    "6. 'kaum ... da' pattern:\n"
    "   Kaum hatte er sich hingesetzt, klingelte das Telefon.\n"
    "   (Barely had he sat down when the telephone rang.)\n\n"
    "COMMON TRAPS:\n"
    "- Confusing 'nachdem' and 'bevor': 'nachdem' = the subordinate action is FIRST; 'bevor' = the main clause action is first.\n"
    "- Using Perfekt instead of Plusquamperfekt after 'nachdem': always use Plusquamperfekt after 'nachdem' in written German.\n"
    "- Using sein for reflexive verbs: reflexive verbs always use haben.\n"
    "- Using the past participle of a modal verb instead of the infinitive in Ersatzinfinitiv: 'hatte machen können' NOT 'hatte gemacht gekonnt'.\n"
    "- Forgetting that some intransitive verbs use sein (movement, change of state): e.g., sterben, sinken, fliehen, ankommen, ein schlafen, umziehen.\n"
    "- Mixing up 'kaum ... als' and 'kaum ... da': in modern German, 'kaum ... da' is standard, though 'kaum ... als' is also acceptable in some regions."
)

original['description'] = description
original['tips'] = tips
original['totalQuestions'] = len(translated_qs)
original['questions'] = translated_qs

# Check for remaining Turkish
import re
remaining = []
for q in translated_qs:
    for key in ['correctAnswer', 'explanation']:
        val = q.get(key, '')
        if re.search(r'[ÇçĞğİıŞş]', val):
            remaining.append(f"{q['id']}: {val[:60]}")
print(f"\nRemaining Turkish chars: {len(remaining)}")
if remaining:
    for r in remaining: print(f"  {r}")

with open('app/src/main/assets/a2_08.json', 'w', encoding='utf-8') as f:
    json.dump(original, f, ensure_ascii=False, indent=2)

print("✅ Saved!")
print(f"   Total questions: {len(translated_qs)}")