#!/usr/bin/env python3
import json

# Read original file from git (clean, untranslated)
import subprocess
result = subprocess.run(['git', 'show', 'HEAD:app/src/main/assets/a2_09.json'],
                       capture_output=True, text=True,
                       cwd='/home/node/.openclaw/workspace/b2-deutsch-app')
original = json.loads(result.stdout)

# ─── EXPLANATION TRANSLATIONS ───
exp_translations = {
    "erzählen von + Dativ → von dem. 'Bahsetmek' (von etwas/jemandem erzählen).":
        "erzählen von + Dativ → von dem. 'to tell about' (to talk about something/someone).",

    "die Firma (dişil) genitif → deren. 'Onun ürünleri dünya çapında tanınıyor'.":
        "die Firma (feminine) genitive → deren. 'Its products are recognized worldwide'.",

    "sich freuen über + Akkusativ. 'Nichts' gibi belgisiz kelimelerden sonra wo(r)- yapısı.":
        "sich freuen über + Akkusativ. After indefinite words like 'Nichts', the wo(r)- structure is used.",

    "'in dem' (Dativ) ve 'wo' her ikisi de doğru — yer bildiren ifadelerde.":
        "'in dem' (Dativ) and 'wo' are both correct — for place expressions.",

    "Kunden (çoğul) Dativ → denen. 'Anbieten + Dativ' (teklif etmek).":
        "Kunden (plural) Dativ → denen. 'Anbieten + Dativ' (to offer).",

    "sich verlassen auf + Akkusativ → Relativsatz: auf den (man sich verlassen kann).":
        "sich verlassen auf + Akkusativ → Relativsatz: auf den (that one can rely on).",

    "Alles, etwas, nichts gibi belgisiz kelimelerden sonra was kullanılır.":
        "After indefinite pronouns like Alles, etwas, nichts, was is used.",

    "der Autor (eril) genitif → dessen. 'Onun yeni kitabı bestseller oldu'.":
        "der Autor (masculine) genitive → dessen. 'His new book became a bestseller'.",

    "sich befinden in + Dativ (nerede?) → in der Krise.":
        "sich befinden in + Dativ (where?) → in der Krise (in the crisis).",

    "das Kind (nötr) genitif → dessen. 'Çocuğun ebeveynleri'.":
        "das Kind (neuter) genitive → dessen. 'The child's parents'.",

    "Süperlatif sıfatlardan (das Schönste) sonra was kullanılır.":
        "was is used after superlative adjectives (das Schönste).",

    "reisen in + Akkusativ (wohin?) → in die Stadt (hareket yönü).":
        "reisen in + Akkusativ (where to?) → in die Stadt (direction of movement).",

    "sich beziehen auf + Akkusativ → auf die (Argumente).":
        "sich beziehen auf + Akkusativ → auf die (arguments).",

    "überrascht sein über + Akkusativ. Genitif ile: über dessen Entscheidung.":
        "überrascht sein über + Akkusativ. With genitive: über dessen Entscheidung.",

    "'Dinge' somut bir nesne olarak auf die kullanılır. worauf de doğru olabilir.":
        "For 'Dinge' as a concrete object, auf die is used. worauf can also be correct.",

    "Studentin (dişil) Dativ → der. 'Kime borç verdim?' (Kime verdim?).":
        "Studentin (feminine) Dativ → der. 'To whom did I lend money?' (Kime verdim?).",

    "warten auf + Akkusativ → auf den (Moment).":
        "warten auf + Akkusativ → auf den (moment).",

    "lachen über + Akkusativ → über das (şey) ve worüber her ikisi de doğru.":
        "lachen über + Akkusativ → über das (thing) and worüber are both correct.",

    "die Bäume (çoğul) genitif → deren. 'Ağaçların yaprakları'.":
        "die Bäume (plural) genitive → deren. 'The trees' leaves'.",

    "Alles (belgisiz zamir) ile başlayan cümlelerde was kullanılır.":
        "was is used in sentences beginning with Alles (indefinite pronoun).",

    "dessen — Genitiv, maskulin (Forschungsergebnisse = sahiplik).":
        "dessen — Genitive, masculine (Forschungsergebnisse = possession).",

    "die — Akkusativ, çoğul (Maßnahmen = nesne).":
        "die — Akkusativ, plural (Maßnahmen = object).",

    "was — belirsiz öncülle (genau das) gelen relatif zamir.":
        "was — relative pronoun that follows an indefinite antecedent (genau das).",

    "der — Dativ, feminin (anvertrauen + Dativ).":
        "der — Dativ, feminine (anvertrauen + Dativ).",

    "dessen — Genitiv, maskulin (Hauptsitz = sahiplik).":
        "dessen — Genitive, masculine (Hauptsitz = possession).",

    "was — alles öncülüyle gelen relatif zamir.":
        "was — relative pronoun following an 'alles' antecedent.",

    "in der — Präposition + Dativ, feminin (leben in + Dativ).":
        "in der — Preposition + Dativ, feminine (leben in + Dativ).",

    "dessen — Genitiv, maskulin (Aussagen = sahiplik).":
        "dessen — Genitive, masculine (Aussagen = possession).",

    "für die — Präposition + Akkusativ, çoğul.":
        "für die — Preposition + Akkusativ, plural.",

    "wer — bağımsız relatif zamir, cümle tamamlanmış.":
        "wer — independent relative pronoun, sentence is complete.",

    "das — Akkusativ, nötr (Urteil = nesne).":
        "das — Akkusativ, neuter (Urteil = object).",

    "deren — Genitiv, çoğul (Gutachten = sahiplik).":
        "deren — Genitive, plural (Gutachten = possession).",

    "was — etwas öncülüyle gelen relatif zamir.":
        "was — relative pronoun following an 'etwas' antecedent.",

    "warum / weshalb — her ikisi de neden relatif zarfı olarak doğru.":
        "warum / weshalb — both are correct as reason relative adverbs.",

    "auf der — Präposition + Dativ, feminin (basieren auf + Dativ).":
        "auf der — Preposition + Dativ, feminine (basieren auf + Dativ).",

    "der — Nominativ, maskulin (özne konumunda).":
        "der — Nominativ, masculine (in subject position).",

    "womit / mit dem — her ikisi de doğru; womit = Präpositionaladverb.":
        "womit / mit dem — both are correct; womit = prepositional adverb.",

    "deren — Genitiv, çoğul (Verträge = sahiplik).":
        "deren — Genitive, plural (Verträge = possession).",

    "deren — Genitiv, feminin (Konsequenzen = sahiplik).":
        "deren — Genitive, feminine (Konsequenzen = possession).",

    "der — Nominativ, maskulin (der Student = özne).":
        "der — Nominativ, masculine (der Student = subject).",

    "das — Akkusativ, nötr (das Buch = nesne).":
        "das — Akkusativ, neuter (das Buch = object).",

    "deren — Genitiv, feminin (Auto = Die Frau'nun oluşan).":
        "deren — Genitive, feminine (Auto = belonging to Die Frau).",

    "dem — Dativ, maskulin (sprechen mit + Dativ).":
        "dem — Dativ, masculine (sprechen mit + Dativ).",

    "deren — Genitiv, feminin (Produkte = die Firma'nın ürünleri).":
        "deren — Genitive, feminine (Produkte = the company's products).",

    "die — Nominativ, çoğul (die Studenten = özne).":
        "die — Nominativ, plural (die Studenten = subject).",

    "den — Akkusativ, maskulin (treffen + Akkusativ).":
        "den — Akkusativ, masculine (treffen + Akkusativ).",

    "deren — Genitiv, feminin (Meinung = die Kollegin'ın görüşü).":
        "deren — Genitive, feminine (Meinung = the colleague's opinion).",

    "in dem — Dativ, nötr (stattfinden in + Dativ).":
        "in dem — Dativ, neuter (stattfinden in + Dativ).",

    "denen — Dativ, çoğul (helfen + Dativ).":
        "denen — Dativ, plural (helfen + Dativ).",

    "dessen — Genitiv, maskulin (Roman = der Autor'un romanı).":
        "dessen — Genitive, masculine (Roman = the author's novel).",

    "die — Akkusativ, feminin (besuchen + Akkusativ).":
        "die — Akkusativ, feminine (besuchen + Akkusativ).",

    "dessen — Genitiv, maskulin (Forschung = der Wissenschaftler'ın araştırması).":
        "dessen — Genitive, masculine (Forschung = the scientist's research).",

    "denen — Dativ, çoğul (diskutieren mit + Dativ).":
        "denen — Dativ, plural (diskutieren mit + Dativ).",

    "den — Akkusativ, maskulin (sehen + Akkusativ).":
        "den — Akkusativ, masculine (sehen + Akkusativ).",

    "deren — Genitiv, feminin (Unterricht = die Lehrerin'ın dersi).":
        "deren — Genitive, feminine (Unterricht = the teacher's lesson).",

    "denen — Dativ, çoğul (schicken an + Dativ).":
        "denen — Dativ, plural (schicken an + Dativ).",

    "dessen — Genitiv, maskulin (Fahrrad = der Junge'ın bisikleti).":
        "dessen — Genitive, masculine (Fahrrad = the boy's bicycle).",

    "die — Akkusativ, feminin (arbeiten für + Akkusativ).":
        "die — Akkusativ, feminine (arbeiten für + Akkusativ).",

    "deren — Genitiv, feminin (Vortrag = die Professorin'ın konuşması).":
        "deren — Genitive, feminine (Vortrag = the professor's lecture).",

    "dessen — Genitiv, maskulin, bezieht sich auf 'der Kollege'.":
        "dessen — Genitive, masculine, refers to 'der Kollege'.",

    "mit dem — Dativ, maskulin.":
        "mit dem — Dativ, masculine.",

    "in der — Dativ, Feminin.":
        "in der — Dativ, feminine.",

    "über das — Akkusativ, Neutrum.":
        "über das — Akkusativ, neuter.",

    "auf das — Akkusativ, Neutrum.":
        "auf das — Akkusativ, neuter.",

    "deren — Genitiv, Feminin.":
        "deren — Genitive, feminine.",

    "was — nach 'das, alles, nichts' verwendet.":
        "was — used after 'das, alles, nichts'.",

    "der — Dativ, Feminin (geben + Dativ).":
        "der — Dativ, feminine (geben + Dativ).",

    "in dem — Dativ, maskulin.":
        "in dem — Dativ, masculine.",

    "der — Nominativ, maskulin.":
        "der — Nominativ, masculine.",

    "vor dem — Dativ, Neutrum.":
        "vor dem — Dativ, neuter.",

    "mit der — Dativ, Feminin.":
        "mit der — Dativ, feminine.",

    "dem — Dativ, 'wer' bezieht sich auf 'dem'.":
        "dem — Dativ, 'wer' refers to 'dem'.",

    "wovor — Relativsatz mit Fragewort-Ersatz (vor + Dativ).":
        "wovor — Relative clause with interrogative replacement (vor + Dativ).",

    "von der — Dativ, Feminin.":
        "von der — Dativ, feminine.",

    "deren — Genitiv Plural (die Wohnung, deren Fenster).":
        "deren — Genitive plural (die Wohnung, deren Fenster).",

    "an dem — Dativ, maskulin.":
        "an dem — Dativ, masculine.",

    "was — nach 'alles' verwendet.":
        "was — used after 'alles'.",

    "auf die — Akkusativ, Feminin.":
        "auf die — Akkusativ, feminine.",

    "dessen — Genitiv, maskulin.":
        "dessen — Genitive, masculine.",
}

# ─── ANSWER TRANSLATIONS ───
ans_translations = {
    "Hem B hem C doğru": "Both B and C are correct",
    "A ve B doğru": "Both A and B are correct",
}

# ─── TRANSLATE QUESTIONS ───
translated_qs = []
for q in original['questions']:
    q = dict(q)
    orig_exp = q.get('explanation', '')
    orig_ans = q.get('correctAnswer', '')
    q['explanation'] = exp_translations.get(orig_exp, orig_exp)
    q['correctAnswer'] = ans_translations.get(orig_ans, orig_ans)
    q['sourceId'] = 'manual'
    translated_qs.append(q)

print(f"Translated {len(translated_qs)} questions")

# Spot check
for i in [0, 1, 2, 3, 4, 8, 19, 29, 34, 37]:
    q = translated_qs[i]
    print(f"Q{i+1}: [{q['correctAnswer']}] {q['explanation'][:100]}")

print()

# ─── ADD 20 NEW QUESTIONS (q081-q100) ───
new_qs = [
    {
        "id": "a2_09_q081", "subjectId": "a2_09", "topicId": "a2_09", "topicName": "Relativsätze",
        "sourceId": "manual", "originalId": "manual_081", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Der Forscher, ____________ die Ergebnisse veröffentlicht hat, wurde ausgezeichnet.",
        "options": ["dessen", "deren", "der", "den"],
        "correctAnswer": "dessen",
        "explanation": "dessen — Genitive, masculine (refers to 'der Forscher'). The researcher's results were published. Genitive marks possession.",
        "difficulty": "medium"
    },
    {
        "id": "a2_09_q082", "subjectId": "a2_09", "topicId": "a2_09", "topicName": "Relativsätze",
        "sourceId": "manual", "originalId": "manual_082", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Das Buch, ____________ ich gestern gelesen habe, war sehr spannend.",
        "options": ["das", "der", "die", "den"],
        "correctAnswer": "das",
        "explanation": "das — Akkusativ, neuter (refers to 'das Buch'). The book that I read yesterday was very exciting. The relative pronoun agrees with its antecedent in gender, number, and case.",
        "difficulty": "easy"
    },
    {
        "id": "a2_09_q083", "subjectId": "a2_09", "topicId": "a2_09", "topicName": "Relativsätze",
        "sourceId": "manual", "originalId": "manual_083", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Die Frau, ____________ wir gestern getroffen haben, ist unsere neue Chefin.",
        "options": ["die", "der", "das", "den"],
        "correctAnswer": "die",
        "explanation": "die — Akkusativ, feminine (refers to 'die Frau'). The relative pronoun is in Akkusativ because the verb 'treffen' requires Akkusativ.",
        "difficulty": "easy"
    },
    {
        "id": "a2_09_q084", "subjectId": "a2_09", "topicId": "a2_09", "topicName": "Relativsätze",
        "sourceId": "manual", "originalId": "manual_084", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Nichts, ____________ du gesagt hast, ist wahr.",
        "options": ["was", "das", "wer", "wo"],
        "correctAnswer": "was",
        "explanation": "was — After indefinite pronouns like 'Nichts', 'Alles', 'Etwas', the relative pronoun 'was' is always used. This is a fixed rule in German.",
        "difficulty": "easy"
    },
    {
        "id": "a2_09_q085", "subjectId": "a2_09", "topicId": "a2_09", "topicName": "Relativsätze",
        "sourceId": "manual", "originalId": "manual_085", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Der Lehrer, ____________ ich vertraue, hat mir geholfen.",
        "options": ["den", "der", "dem", "dessen"],
        "correctAnswer": "dem",
        "explanation": "dem — Dativ, masculine. The verb 'vertrauen + Dativ' requires Dativ. Therefore 'der Lehrer' in Dativ is 'dem'. Note: 'vertrauen' takes Dativ, not Akkusativ.",
        "difficulty": "medium"
    },
    {
        "id": "a2_09_q086", "subjectId": "a2_09", "topicId": "a2_09", "topicName": "Relativsätze",
        "sourceId": "manual", "originalId": "manual_086", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Alles, ____________ ich weiß, ist, dass er Recht hatte.",
        "options": ["was", "das", "es", "wer"],
        "correctAnswer": "was",
        "explanation": "was — After 'Alles' (indefinite pronoun), 'was' is the required relative pronoun. This also applies to 'Etwas', 'Nichts', and similar words.",
        "difficulty": "easy"
    },
    {
        "id": "a2_09_q087", "subjectId": "a2_09", "topicId": "a2_09", "topicName": "Relativsätze",
        "sourceId": "manual", "originalId": "manual_087", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Die Studentin, ____________ die Universität empfohlen hat, ist sehr kompetent.",
        "options": ["deren", "dessen", "die", "welche"],
        "correctAnswer": "deren",
        "explanation": "deren — Genitive, feminine. The university recommended the student (student's abilities). Genitive marks that the university is the source/reason. Whose recommendation? → deren.",
        "difficulty": "medium"
    },
    {
        "id": "a2_09_q088", "subjectId": "a2_09", "topicId": "a2_09", "topicName": "Relativsätze",
        "sourceId": "manual", "originalId": "manual_088", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Das Gebäude, ____________ wir vorbeigehen, ist sehr alt.",
        "options": ["an dem", "das", "der", "wo"],
        "correctAnswer": "an dem",
        "explanation": "an dem — Dativ, neuter. The verb 'vorbeigehen an + Dativ' requires Dativ. 'Das Gebäude' in Dativ is 'das' → 'an dem'. Note: 'wo' is NOT used for people.",
        "difficulty": "medium"
    },
    {
        "id": "a2_09_q089", "subjectId": "a2_09", "topicId": "a2_09", "topicName": "Relativsätze",
        "sourceId": "manual", "originalId": "manual_089", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Die Personen, ____________ ich mich gewandt habe, waren sehr hilfsbereit.",
        "options": ["denen", "die", "der", "deren"],
        "correctAnswer": "denen",
        "explanation": "denen — Dativ, plural. The verb 'sich wenden an + Akkusativ' creates an Akkusativ relationship in the relative clause, but 'gewandt' (sich wenden) requires Dativ for the person being addressed. Wait — actually 'sich wenden an' takes Akkusativ for the person: 'an wen?' → die Personen → Akkusativ → die, NOT denen. Let me recheck: 'sich wenden an' → Ich wende mich an die Personen → Akkusativ → die Personen → relative pronoun = die. Actually the correct answer here is: the verb 'helfen' requires Dativ, not 'sich wenden'. Let me reconsider. The verb in the relative clause is 'sich gewandt habe' — 'sich wenden an + Akkusativ': 'an die Personen' → Akkusativ → die. But wait, looking at the question, it says 'Die Personen, an die ich mich gewandt habe' — an + Akkusativ → die → Akkusativ plural = die. So the answer should be 'die'. Actually 'an wen?' → wen is Akkusativ of 'wer' → die Personen → Akkusativ = die. So the answer is 'die'. Let me re-read: The sentence is 'Die Personen, an ____________ ich mich gewandt habe'. The preposition 'an' takes Akkusativ → 'an die Personen' → 'an die' → the relative pronoun is the object of 'an' → Akkusativ plural = die. So answer = die.",
        "difficulty": "hard"
    },
    {
        "id": "a2_09_q090", "subjectId": "a2_09", "topicId": "a2_09", "topicName": "Relativsätze",
        "sourceId": "manual", "originalId": "manual_090", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Er hat mir geholfen, ____________ ich sehr dankbar bin.",
        "options": ["worüber", "darüber", "über das", "was"],
        "correctAnswer": "darüber",
        "explanation": "darüber — Demonstrative pronoun + preposition ('darüber' = 'über das' = 'about that'). In relative clauses, 'wo(r)-' replaces ' Präposition + was' after indefinite antecedents. However, 'das' as a demonstrative antecedent often uses 'darüber' rather than 'worüber'. Actually worüber = wo + über + was → used after things. After 'es' (it), use 'darüber'. The answer 'darüber' refers to 'the help'.",
        "difficulty": "hard"
    },
    {
        "id": "a2_09_q091", "subjectId": "a2_09", "topicId": "a2_09", "topicName": "Relativsätze",
        "sourceId": "manual", "originalId": "manual_091", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Die Kinder, ____________ die Eltern berufstätig sind, kommen nachmittags in die Kita.",
        "options": ["deren", "deren", "deren", "deren"],
        "correctAnswer": "deren",
        "explanation": "deren — Genitive, plural (refers to 'die Kinder'). Whose parents? → deren. This is a genitive relationship: the children (whose parents are employed). 'Deren' agrees with the antecedent in gender and number (feminine/plural for possession).",
        "difficulty": "medium"
    },
    {
        "id": "a2_09_q092", "subjectId": "a2_09", "topicId": "a2_09", "topicName": "Relativsätze",
        "sourceId": "manual", "originalId": "manual_092", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Das Haus, ____________ wir Miete zahlen, gehört einem Architekten.",
        "options": ["das", "dem", "an das", "wo"],
        "correctAnswer": "dem",
        "explanation": "dem — Dativ, neuter. The verb 'Miete zahlen für + Akkusativ' — wait actually 'zahlen für + Akkusativ' → 'für das Haus' → Akkusativ → das. But looking at the sentence, 'wo' is location (where)? Actually the key is: 'Das Haus, für das wir Miete zahlen' → 'für das' → Dativ or Akkusativ? 'zahlen für' takes Akkusativ → 'für das Haus' → but 'zahlen' can also be used with Dativ in some contexts. Let me think: 'für etwas Miete zahlen' → Akkusativ. So 'das' would be correct. Wait, but the options include 'dem'. Let me reconsider: 'Das Haus, dem wir Miete zahlen' — if it were Dativ, it would mean 'to the house' which doesn't work. 'Miete zahlen für' → Akkusativ → das. But actually 'das' as Akkusativ neuter = 'das Haus' → correct answer would be 'das'. Let me reconsider the sentence: 'Das Haus, ____________ wir Miete zahlen' — what preposition goes with 'Miete zahlen'? You pay rent FOR something → 'für' → Akkusativ → 'für das Haus' → 'das'. So answer = das.",
        "difficulty": "hard"
    },
    {
        "id": "a2_09_q093", "subjectId": "a2_09", "topicId": "a2_09", "topicName": "Relativsätze",
        "sourceId": "manual", "originalId": "manual_093", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Der Kollege, mit ____________ ich im Büro sitze, ist sehr freundlich.",
        "options": ["dem", "der", "den", "dessen"],
        "correctAnswer": "dem",
        "explanation": "dem — Dativ, masculine. The preposition 'mit' requires Dativ. 'Der Kollege' in Dativ is 'dem' → 'mit dem'. The colleague with whom I sit in the office.",
        "difficulty": "easy"
    },
    {
        "id": "a2_09_q094", "subjectId": "a2_09", "topicId": "a2_09", "topicName": "Relativsätze",
        "sourceId": "manual", "originalId": "manual_094", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Das ist das Problem, ____________ ich mich nicht lösen kann.",
        "options": ["das", "worüber", "woran", "damit"],
        "correctAnswer": "worüber",
        "explanation": "worüber — After indefinite pronouns like 'etwas', the wo(r)- prepositional structure is used. 'sich beschäftigen mit + Dativ' → 'womit' → but here the verb is 'lösen' which requires 'an + Dativ' → 'woran'. Wait: 'sich beschäftigen mit' → 'womit'; 'sich konzentrieren auf + Akkusativ' → 'worauf'; 'sich freuen über + Akkusativ' → 'worüber'. The problem is 'das Problem' — with what? 'an dem Problem arbeiten' → 'woran'. But the verb is 'lösen' → you solve a problem → 'ein Problem lösen' → Akkusativ → 'das Problem' → 'das'. So worüber doesn't fit 'lösen'. The answer should be 'das'. But actually re-reading: 'Das ist das Problem, worüber ich mich nicht freue' — no. 'worüber' comes from 'sich ärgern über + Akkusativ' → 'worüber ich mich ärgere'. For 'lösen', the relative pronoun would be 'das' (Akkusativ, neuter) referring back to 'das Problem'.",
        "difficulty": "hard"
    },
    {
        "id": "a2_09_q095", "subjectId": "a2_09", "topicId": "a2_09", "topicName": "Relativsätze",
        "sourceId": "manual", "originalId": "manual_095", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Die Zeit, ____________ wir in dieser Stadt verbracht haben, war wunderbar.",
        "options": ["die", "der", "das", "denen"],
        "correctAnswer": "die",
        "explanation": "die — Akkusativ, feminine (refers to 'die Zeit'). The time that we spent in this city. Note: 'verbringen' takes Akkusativ, so the relative pronoun is in Akkusativ.",
        "difficulty": "easy"
    },
    {
        "id": "a2_09_q096", "subjectId": "a2_09", "topicId": "a2_09", "topicName": "Relativsätze",
        "sourceId": "manual", "originalId": "manual_096", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Der Film, ____________ ich mich sehr gefreut habe, war enttäuschend.",
        "options": ["darüber", "worüber", "das", "der"],
        "correctAnswer": "darüber",
        "explanation": "darüber — After 'der Film' (definite antecedent), the demonstrative form 'darüber' is used, not 'worüber'. However, 'worüber' is also grammatically possible but less common with definite antecedents. In A2 level, 'darüber' is the expected answer when the antecedent is definite and specific. Actually with a definite antecedent ('der Film'), both 'worüber' and 'über den' are possible. But the option includes 'darüber' as A and 'worüber' as B. 'darüber' = 'über den Film' = 'about the film'. Since this is A2, either could work but 'darüber' is more commonly tested with definite nouns.",
        "difficulty": "medium"
    },
    {
        "id": "a2_09_q097", "subjectId": "a2_09", "topicId": "a2_09", "topicName": "Relativsätze",
        "sourceId": "manual", "originalId": "manual_097", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Die Frau, ____________ Auto gestohlen wurde, hat Anzeige erstattet.",
        "options": ["deren", "dessen", "die", "welche"],
        "correctAnswer": "deren",
        "explanation": "deren — Genitive, feminine. The woman's car was stolen. Whose car? → deren. Note: 'deren' is used for feminine and plural nouns in genitive, regardless of case role in the relative clause.",
        "difficulty": "easy"
    },
    {
        "id": "a2_09_q098", "subjectId": "a2_09", "topicId": "a2_09", "topicName": "Relativsätze",
        "sourceId": "manual", "originalId": "manual_098", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Das Beste, ____________ mir passieren konnte, ist passiert.",
        "options": ["was", "das", "es", "welches"],
        "correctAnswer": "was",
        "explanation": "was — After superlatives (das Beste = the best), the relative pronoun 'was' is always used. This is a fixed grammatical rule: superlative + was.",
        "difficulty": "easy"
    },
    {
        "id": "a2_09_q099", "subjectId": "a2_09", "topicId": "a2_09", "topicName": "Relativsätze",
        "sourceId": "manual", "originalId": "manual_099", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Der Mann, ____________ ich dich gestern kennenlernen wollte, ist leider nicht gekommen.",
        "options": ["mit dem", "der", "den", "an den"],
        "correctAnswer": "mit dem",
        "explanation": "mit dem — Dativ, masculine. The verb 'kennenlernen' doesn't take a preposition directly, but the sentence implies 'mit dem Mann' (with the man). The preposition 'mit' requires Dativ → 'mit dem'.",
        "difficulty": "easy"
    },
    {
        "id": "a2_09_q100", "subjectId": "a2_09", "topicId": "a2_09", "topicName": "Relativsätze",
        "sourceId": "manual", "originalId": "manual_100", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Die Schüler, ____________ die Leistungen sich verbessert haben, wurden gelobt.",
        "options": ["deren", "deren", "deren", "deren"],
        "correctAnswer": "deren",
        "explanation": "deren — Genitive, plural. Whose performances improved? → deren (the students'). The relative pronoun 'deren' agrees with the antecedent in gender and number, and its case is determined by the role it plays in the relative clause (here: genitive as subject of 'sich verbessert haben').",
        "difficulty": "medium"
    },
]

# Fix Q089, Q090, Q092, Q094, Q096 (they have wrong/messy explanations from my thinking out loud)
# Let me rewrite them cleanly
new_qs_fixed = [
    {
        "id": "a2_09_q081", "subjectId": "a2_09", "topicId": "a2_09", "topicName": "Relativsätze",
        "sourceId": "manual", "originalId": "manual_081", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Der Forscher, ____________ die Ergebnisse veröffentlicht hat, wurde ausgezeichnet.",
        "options": ["dessen", "deren", "der", "den"],
        "correctAnswer": "dessen",
        "explanation": "dessen — Genitive, masculine (refers to 'der Forscher'). The researcher's results were published. Genitive marks possession.",
        "difficulty": "medium"
    },
    {
        "id": "a2_09_q082", "subjectId": "a2_09", "topicId": "a2_09", "topicName": "Relativsätze",
        "sourceId": "manual", "originalId": "manual_082", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Das Buch, ____________ ich gestern gelesen habe, war sehr spannend.",
        "options": ["das", "der", "die", "den"],
        "correctAnswer": "das",
        "explanation": "das — Akkusativ, neuter (refers to 'das Buch'). The relative pronoun agrees with its antecedent in gender, number, and case. Here 'das Buch' is the object of 'gelesen habe' → Akkusativ.",
        "difficulty": "easy"
    },
    {
        "id": "a2_09_q083", "subjectId": "a2_09", "topicId": "a2_09", "topicName": "Relativsätze",
        "sourceId": "manual", "originalId": "manual_083", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Die Frau, ____________ wir gestern getroffen haben, ist unsere neue Chefin.",
        "options": ["die", "der", "das", "den"],
        "correctAnswer": "die",
        "explanation": "die — Akkusativ, feminine (refers to 'die Frau'). The verb 'treffen' requires Akkusativ. The relative pronoun must match its antecedent's gender, number, and case.",
        "difficulty": "easy"
    },
    {
        "id": "a2_09_q084", "subjectId": "a2_09", "topicId": "a2_09", "topicName": "Relativsätze",
        "sourceId": "manual", "originalId": "manual_084", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Nichts, ____________ du gesagt hast, ist wahr.",
        "options": ["was", "das", "wer", "wo"],
        "correctAnswer": "was",
        "explanation": "was — After indefinite pronouns like 'Nichts', 'Alles', 'Etwas', the relative pronoun 'was' is always used. This is a fixed rule: indefinite pronoun antecedent → was.",
        "difficulty": "easy"
    },
    {
        "id": "a2_09_q085", "subjectId": "a2_09", "topicId": "a2_09", "topicName": "Relativsätze",
        "sourceId": "manual", "originalId": "manual_085", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Der Lehrer, ____________ ich vertraue, hat mir geholfen.",
        "options": ["den", "der", "dem", "dessen"],
        "correctAnswer": "dem",
        "explanation": "dem — Dativ, masculine. The verb 'vertrauen' requires Dativ (vertrauen + Dativ). 'Der Lehrer' in Dativ is 'dem' → 'dem ich vertraue'.",
        "difficulty": "medium"
    },
    {
        "id": "a2_09_q086", "subjectId": "a2_09", "topicId": "a2_09", "topicName": "Relativsätze",
        "sourceId": "manual", "originalId": "manual_086", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Alles, ____________ ich weiß, ist, dass er Recht hatte.",
        "options": ["was", "das", "es", "wer"],
        "correctAnswer": "was",
        "explanation": "was — After 'Alles' (indefinite pronoun), 'was' is the required relative pronoun. This also applies to 'Etwas', 'Nichts', and superlative nouns.",
        "difficulty": "easy"
    },
    {
        "id": "a2_09_q087", "subjectId": "a2_09", "topicId": "a2_09", "topicName": "Relativsätze",
        "sourceId": "manual", "originalId": "manual_087", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Die Studentin, ____________ die Universität empfohlen hat, ist sehr kompetent.",
        "options": ["deren", "dessen", "die", "welche"],
        "correctAnswer": "deren",
        "explanation": "deren — Genitive, feminine. The university recommended the student. Whose recommendation? → deren. 'Deren' agrees with the antecedent (feminine singular) and marks possession.",
        "difficulty": "medium"
    },
    {
        "id": "a2_09_q088", "subjectId": "a2_09", "topicId": "a2_09", "topicName": "Relativsätze",
        "sourceId": "manual", "originalId": "manual_088", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Das Gebäude, ____________ wir vorbeigehen, ist sehr alt.",
        "options": ["an dem", "das", "der", "wo"],
        "correctAnswer": "an dem",
        "explanation": "an dem — Dativ, neuter. The verb 'vorbeigehen an + Dativ' requires Dativ. 'Das Gebäude' in Dativ is 'dem' → 'an dem wir vorbeigehen'. Note: 'wo' is NOT used for people or specific objects.",
        "difficulty": "medium"
    },
    {
        "id": "a2_09_q089", "subjectId": "a2_09", "topicId": "a2_09", "topicName": "Relativsätze",
        "sourceId": "manual", "originalId": "manual_089", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Die Personen, ____________ ich mich gewandt habe, waren sehr hilfsbereit.",
        "options": ["denen", "die", "der", "an die"],
        "correctAnswer": "an die",
        "explanation": "an die — Akkusativ, plural. The verb 'sich wenden an + Akkusativ' requires Akkusativ for the person. 'An die Personen' → 'an die' is the correct form. The relative pronoun must reflect the preposition's case requirement.",
        "difficulty": "hard"
    },
    {
        "id": "a2_09_q090", "subjectId": "a2_09", "topicId": "a2_09", "topicName": "Relativsätze",
        "sourceId": "manual", "originalId": "manual_090", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Er hat mir geholfen, ____________ ich sehr dankbar bin.",
        "options": ["darüber", "worüber", "an das", "was"],
        "correctAnswer": "darüber",
        "explanation": "darüber — 'darüber' = 'über diese Hilfe' (about this help). After a definite antecedent ('das') with a prepositional complement, German uses 'da(r)-' forms. Compare: 'Die Hilfe, worüber ich mich freue' (indefinite/wo(r)-) vs. 'Die Hilfe, darüber bin ich dankbar' (definite/da(r)-). Here the antecedent is a clause, so 'darüber' is appropriate.",
        "difficulty": "hard"
    },
    {
        "id": "a2_09_q091", "subjectId": "a2_09", "topicId": "a2_09", "topicName": "Relativsätze",
        "sourceId": "manual", "originalId": "manual_091", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Die Kinder, ____________ die Eltern berufstätig sind, kommen nachmittags in die Kita.",
        "options": ["deren", "deren", "deren", "deren"],
        "correctAnswer": "deren",
        "explanation": "deren — Genitive, plural (refers to 'die Kinder'). Whose parents? → deren. 'Deren' agrees with the antecedent (plural) and marks possession. The parents are employed = die Kinder, deren Eltern berufstätig sind.",
        "difficulty": "medium"
    },
    {
        "id": "a2_09_q092", "subjectId": "a2_09", "topicId": "a2_09", "topicName": "Relativsätze",
        "sourceId": "manual", "originalId": "manual_092", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Das Haus, ____________ wir Miete zahlen, gehört einem Architekten.",
        "options": ["das", "dem", "an das", "wo"],
        "correctAnswer": "das",
        "explanation": "das — Akkusativ, neuter. The verb combination 'Miete zahlen für + Akkusativ' requires Akkusativ. 'Für das Haus' → 'das'. The house that we pay rent for. Note: some verbs with 'für' can also take Dativ in regional usage, but 'zahlen für' consistently takes Akkusativ.",
        "difficulty": "medium"
    },
    {
        "id": "a2_09_q093", "subjectId": "a2_09", "topicId": "a2_09", "topicName": "Relativsätze",
        "sourceId": "manual", "originalId": "manual_093", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Der Kollege, mit ____________ ich im Büro sitze, ist sehr freundlich.",
        "options": ["dem", "der", "den", "dessen"],
        "correctAnswer": "dem",
        "explanation": "dem — Dativ, masculine. The preposition 'mit' requires Dativ. 'Der Kollege' in Dativ is 'dem' → 'mit dem ich im Büro sitze'. This is a standard preposition + relative pronoun construction.",
        "difficulty": "easy"
    },
    {
        "id": "a2_09_q094", "subjectId": "a2_09", "topicId": "a2_09", "topicName": "Relativsätze",
        "sourceId": "manual", "originalId": "manual_094", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Das ist das Problem, ____________ ich mich nicht kümmern kann.",
        "options": ["das", "worüber", "woran", "damit"],
        "correctAnswer": "das",
        "explanation": "das — Akkusativ, neuter. The verb 'kümmern um + Akkusativ' requires Akkusativ. 'Das Problem' in Akkusativ is 'das' → 'das Problem, um das ich mich nicht kümmern kann'. Note: in colloquial German, 'woran' is also possible with 'kümmern', but 'das' (Akkusativ) is the standard A2 answer.",
        "difficulty": "hard"
    },
    {
        "id": "a2_09_q095", "subjectId": "a2_09", "topicId": "a2_09", "topicName": "Relativsätze",
        "sourceId": "manual", "originalId": "manual_095", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Die Zeit, ____________ wir in dieser Stadt verbracht haben, war wunderbar.",
        "options": ["die", "der", "das", "denen"],
        "correctAnswer": "die",
        "explanation": "die — Akkusativ, feminine (refers to 'die Zeit'). The verb 'verbringen' takes Akkusativ. The time that we spent in this city was wonderful.",
        "difficulty": "easy"
    },
    {
        "id": "a2_09_q096", "subjectId": "a2_09", "topicId": "a2_09", "topicName": "Relativsätze",
        "sourceId": "manual", "originalId": "manual_096", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Der Film, ____________ ich mich gefreut habe, war enttäuschend.",
        "options": ["darüber", "worüber", "das", "der"],
        "correctAnswer": "worüber",
        "explanation": "worüber — The verb 'sich freuen über + Akkusativ' uses 'worüber' after indefinite or general antecedents. After 'der Film' (definite), both 'worüber' and 'darüber' are possible, but 'worüber' is the more standard A2 answer. 'worüber' = 'über den Film'. Note: 'darüber' is used after a definite, specific antecedent in formal German.",
        "difficulty": "medium"
    },
    {
        "id": "a2_09_q097", "subjectId": "a2_09", "topicId": "a2_09", "topicName": "Relativsätze",
        "sourceId": "manual", "originalId": "manual_097", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Die Frau, ____________ Auto gestohlen wurde, hat Anzeige erstattet.",
        "options": ["deren", "dessen", "die", "welche"],
        "correctAnswer": "deren",
        "explanation": "deren — Genitive, feminine. The woman's car was stolen. Whose car? → deren. 'Deren' is used for feminine singular and plural nouns in genitive to mark possession.",
        "difficulty": "easy"
    },
    {
        "id": "a2_09_q098", "subjectId": "a2_09", "topicId": "a2_09", "topicName": "Relativsätze",
        "sourceId": "manual", "originalId": "manual_098", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Das Beste, ____________ mir passieren konnte, ist passiert.",
        "options": ["was", "das", "es", "welches"],
        "correctAnswer": "was",
        "explanation": "was — After superlatives (das Beste = the best), the relative pronoun 'was' is always used. This is a fixed grammatical rule: superlative + was. Other examples: das Schönste, was ich je gesehen habe.",
        "difficulty": "easy"
    },
    {
        "id": "a2_09_q099", "subjectId": "a2_09", "topicId": "a2_09", "topicName": "Relativsätze",
        "sourceId": "manual", "originalId": "manual_099", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Der Mann, ____________ ich dich gestern kennenlernen wollte, ist leider nicht gekommen.",
        "options": ["mit dem", "der", "den", "an den"],
        "correctAnswer": "mit dem",
        "explanation": "mit dem — Dativ, masculine. The implied preposition 'mit' (with) requires Dativ. 'Der Mann' in Dativ is 'dem' → 'mit dem ich dich kennenlernen wollte' (the man with whom I wanted to introduce you yesterday).",
        "difficulty": "easy"
    },
    {
        "id": "a2_09_q100", "subjectId": "a2_09", "topicId": "a2_09", "topicName": "Relativsätze",
        "sourceId": "manual", "originalId": "manual_100", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Die Schüler, ____________ die Leistungen sich verbessert haben, wurden gelobt.",
        "options": ["deren", "deren", "deren", "deren"],
        "correctAnswer": "deren",
        "explanation": "deren — Genitive, plural. Whose performances improved? → deren (the students' performances). 'Deren' agrees with the antecedent in gender and number (plural = feminine form 'deren') and shows possession.",
        "difficulty": "medium"
    },
]

translated_qs.extend(new_qs_fixed)
print(f"\nTotal questions: {len(translated_qs)}")

# ─── ADD DESCRIPTION AND TIPS ───
description = (
    "Relativsätze (relative clauses) are subordinate clauses that describe or provide additional "
    "information about a noun (antecedent). The relative pronoun replaces the noun and must agree "
    "with it in gender, number, and case — while the case is also determined by the preposition "
    "or verb inside the relative clause."
)

tips = (
    "KEY RULES:\n"
    "1. Determine the case in 3 steps:\n"
    "   Step 1: Identify the antecedent's gender and number (der, die, das; die plural).\n"
    "   Step 2: Find the role of the relative clause (verb with preposition, or just the relative pronoun as subject/object).\n"
    "   Step 3: Combine: the relative pronoun takes the case from its role inside the clause, but matches gender/number of the antecedent.\n\n"
    "2. Relative Pronouns by Case:\n"
    "   - Nominativ: der / die / das / die (plural)\n"
    "   - Akkusativ: den / die / das / die (plural)\n"
    "   - Dativ: dem / der / dem / denen (plural)\n"
    "   - Genitiv: dessen / deren / dessen / deren (plural)\n\n"
    "3. Preposition + Relative Pronoun: The preposition determines the case, the antecedent determines gender/number.\n"
    "   Example: warten auf + Akkusativ → Der Bus, auf den ich warte (der Bus = maskulin, auf + Akkusativ = den).\n\n"
    "4. 'was' after indefinite pronouns: After Alles, Etwas, Nichts, and superlatives (das Schönste), use 'was'.\n"
    "   Example: Alles, was ich weiß, ist Geheimnis.\n\n"
    "5. 'wo(r)-' compounds: After indefinite antecedents (das, alles, nichts, etwas), use wo(r)- + preposition.\n"
    "   Example: Er hat mir geholfen, wofür ich ihm danke.\n"
    "   ⚠️ Do NOT use wo(r)- for people!\n"
    "   Correct: Der Mann, auf den ich warte. ❌ NOT: Der Mann, worauf ich warte.\n\n"
    "6. Genitive: dessen (masculine/neuter) and deren (feminine/plural) show possession.\n"
    "   Example: Die Frau, deren Auto gestohlen wurde, hat Anzeige erstattet.\n\n"
    "COMMON TRAPS:\n"
    "- Confusing Dativ and Akkusativ with two-way prepositions (an, auf, in, über, unter, vor): always check the verb's requirement.\n"
    "- Using 'wo-' for people: wo- is ONLY for things, abstract concepts, or the entire previous clause.\n"
    "- Mixing up 'dessen' and 'deren': dessen = masculine/neuter singular; deren = feminine/plural.\n"
    "- Forgetting that 'denen' is the only plural form in Dativ (not 'die').\n"
    "- After superlatives: always use 'was', never 'das' or 'der/die/das'."
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
        if re.search(r'[ÇçĞğİıÖöŞşÜü]', val):
            remaining.append(f"{q['id']} {key}: {val}")
print(f"Remaining Turkish chars: {len(remaining)}")
if remaining:
    for r in remaining:
        print(f"  {r}")

with open('app/src/main/assets/a2_09.json', 'w', encoding='utf-8') as f:
    json.dump(original, f, ensure_ascii=False, indent=2)

print("✅ Saved!")
print(f"   Total questions: {len(translated_qs)}")