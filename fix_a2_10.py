#!/usr/bin/env python3
import json, re

with open('app/src/main/assets/a2_10.json') as f:
    data = json.load(f)

# ─── TRANSLATION MAP ───
# Order: longest first to avoid partial replacements
tmap = [
    # Full Turkish phrases → English
    ("bir durumu kabul edip zıttını söyler", "admits one fact while stating the opposite"),
    ("sebep bildirir, weil ile aynıdır ancak cümle başında daha sık kullanılır",
     "expresses a reason like \"because\", but is more often used at the beginning of a sentence"),
    ("iki cümle birbirine bağlar", "connects two sentences"),
    ("her iki seçeneği de reddeder", "rejects both options"),
    ("her iki seçeneği de uygundur", "both options are suitable"),
    ("iki olumlu durumu pekiştirir", "connects two positive situations"),
    ("iki olumsuz durumu bağlar", "connects two negative situations"),
    ("iki olumlu durumu bağlar", "connects two positive situations"),
    ("iki olumsuz seçeneği birleştirir", "combines two negative options"),
    ("iki olumlu seçeneği birleştirir", "combines two positive options"),
    ("olumlu durumları bağlar", "connects positive situations"),
    ("olumsuz durumları bağlar", "connects negative situations"),
    ("iki seçenekten biri", "one of two options"),
    ("her ikisi de uygundur", "both are suitable"),
    ("her iki durumda da", "in both cases"),
    ("fiil cümle sonunda olduğu için", "because the verb is at the end of the clause"),
    ("fiil cümle sonunda", "verb at the end of the clause"),
    ("cümle ortasında fiilden önce gelir", "comes before the verb in the middle of a sentence"),
    ("fiil hemen arkasından gelir", "comes right after the verb"),
    ("cümle başında daha sık kullanılır", "is more often used at the beginning of a sentence"),
    ("cümle başında 'rağmen' anlamında yan cümle", "at the beginning of the sentence means 'although' — subordinate clause"),
    ("yan cümle (fiil sonda)", "subordinate clause (verb at the end)"),
    ("yan cümle yapısı, fiilolta", "subordinate clause structure, verb at the end"),
    ("yan cümle yapısı", "subordinate clause structure"),
    ("yan cümle", "subordinate clause"),
    ("nesne cümlesi", "noun clause"),
    ("amaç cümlesi", "purpose clause"),
    ("devam eden koşul ('olduğu sürece')", "continuing condition ('as long as')"),
    ("devam eden koşul", "continuing condition"),
    ("eş anlamlı, yazılı ve resmi dilde kullanılır",
     "synonymous, used in written and formal language"),
    ("akademik bir bağlaç", "an academic conjunction"),
    ("zarf-bağlaç", "adverbial conjunction"),
    ("bağlaç zarfı", "conjunction adverb"),
    ("eş zamanlı karşıt durum ('iken' — iki olay aynı anda)",
     "simultaneous contrast ('while' — two events at the same time"),
    ("koşul cümlesi (Konjunktiv II ile, 'als ob' benzeri yapı)",
     "conditional clause (with Konjunktiv II, structure similar to 'als ob')"),
    ("koşul cümlesi", "conditional clause"),
    ("her iki cümlede aynı", "the subject is the same in both clauses"),
    ("her iki cümlede farklıysa", "if the subject is different in both clauses"),
    ("özne her iki cümlede aynı", "the subject is the same in both clauses"),
    ("özne iki cümlede farklıysa", "if the subject is different in two clauses"),
    ("her ikisi de olumsuz koşul bildirir", "both express a negative condition"),
    ("dolaylı soru", "indirect question"),
    ("zamansal bağlaç, önceki eylem", "temporal conjunction, previous action"),
    ("olumsuzdan sonra karşıt ifade", "contrast after a negative"),
    ("karşılaştırma", "comparison"),
    ("karşıtlık bildiren bağlaç", "contrast conjunction"),
    ("karşıtlık bildiren zarf", "contrast adverb"),
    ("sonuç bildiren bağlaç", "consequence conjunction"),
    ("sebep bildiren bağlaç", "causal conjunction"),
    ("olduğu sürece", "as long as"),
    ("özne farklıysa", "if the subject is different"),
    ("yerine kullanılır", "is used instead"),
    ("olduğu için", "because"),
    ("hem de", "also"),
    # Answers - specific Turkish answer patterns
    ("Hem A hem B doğru", "Both A and B are correct"),
    ("Hem B hem C doğru", "Both B and C are correct"),
    ("Hem A hem C doğru", "Both A and C are correct"),
    ("A ve B doğru", "Both A and B are correct"),
    # Inside answers
    ("weil anlamında", "means 'because'"),
    ("deshalb anlamında", "means 'therefore'"),
    ("olduğu sürece", "as long as"),
    # German conjunction explanations with Turkish
    ("Gerçi ... ama'", "although... but'"),
    ("Gerçi ... ama", "although... but"),
    ("Ya ... ya da", "either ... or"),
    ("Ne ... ne de", "neither ... nor"),
    ("hem ... hem de", "both ... and"),
    ("Sadece ... değil, aynı zamanda", "not only ... but also"),
    ("Yine de / buna rağmen", "Nevertheless / however"),
    ("Ne kadar ... o kadar", "the more ... the more"),
    ("beklenmedik sonuç, karşıtlık bildirir", "unexpected result, expresses contrast"),
    # Shorter words
    ("Rağmen", "Although"),
    ("buna rağmen", "nevertheless"),
    ("Bu yüzden", "Therefore"),
    ("Sonuç olarak", "Consequently"),
    ("bu nedenle", "for this reason"),
    ("öyle ki ...", "so that ..."),
    ("öyle ki", "so that"),
    ("ikisi de", "both"),
    ("her iki", "both"),
    ("her zaman", "always"),
    ("kullanılabilir", "can be used"),
    ("kullanılır", "is used"),
    ("kullanılmalı", "must be used"),
    ("kurar", "forms"),
    ("gelir", "comes"),
    ("sebep", "reason"),
    ("sonuç", "consequence"),
    ("zıtlık", "contrast"),
    ("koşul", "condition"),
    ("amaç", "purpose"),
    ("ekleme", "addition"),
    ("zaman", "time"),
    ("anlamında", "means"),
    ("olduğu", "which is"),
    ("olan", "which is"),
    ("olmayan", "which is not"),
    ("aynı", "same"),
    ("farklı", "different"),
    ("de", "also"),
    ("ve", "and"),
    ("ile", "with"),
    ("için", "for"),
    ("olarak", "as"),
    ("daha", "more"),
    ("en", "most"),
    ("çok", "very"),
    ("hepsi", "all"),
    ("yalnız", "only"),
    ("sadece", "only"),
    ("şayet", "if"),
    ("eğer", "if"),
    ("madem", "since"),
    ("aksine", "on the contrary"),
    ("halbuki", "whereas"),
    ("oysa", "while"),
    ("lakin", "however"),
    ("fakat", "but"),
    ("artı", "plus"),
    ("üstelik", "moreover"),
    ("ya da", "or"),
    ("veya", "or"),
    ("çünkü", "because"),
    ("rağmen", "despite"),
    ("dolayı", "due to"),
    ("sebebiyle", "because of"),
    ("kadar", "as much as"),
    ("den sonra", "after"),
    ("den önce", "before"),
    ("süresince", "during"),
    ("itibaren", "since"),
    ("boyunca", "throughout"),
    ("karşı", "against"),
    ("doğru", "correct"),
    ("yanlış", "wrong"),
    ("göre", "according to"),
    ("ait", "belongs to"),
    ("birlikte", "together with"),
    ("yoksa", "otherwise"),
    ("olursa", "if it happens"),
    ("birkaç", "a few"),
    ("herhangi", "any"),
    ("bazı", "some"),
    ("tüm", "all"),
    ("az", "less"),
    ("bir", "a"),
    ("birçok", "many"),
    ("hepsini", "all"),
    ("başka", "another"),
    ("yalnız", "only"),
    ("niye", "why"),
    ("nasıl", "how"),
    ("ne", "what"),
    ("kim", "who"),
    ("nerede", "where"),
    ("ne zaman", "when"),
]

def translate(text):
    if not text:
        return text
    result = text
    for tr, en in sorted(tmap, key=lambda x: -len(x[0])):
        result = result.replace(tr, en)
    return result

# ─── TRANSLATE EXISTING 80 QUESTIONS ───
translated_questions = []
for q in data['questions']:
    q = dict(q)
    q['correctAnswer'] = translate(q.get('correctAnswer', ''))
    q['explanation'] = translate(q.get('explanation', ''))
    q['sourceId'] = 'manual'
    translated_questions.append(q)

print(f"Translated {len(translated_questions)} questions")

# ─── ADD 20 NEW QUESTIONS (q081-q100) ───
# Based on: Konjunktionen topic covering wenn/als/falls, nested clauses,
# Konjunktiv II patterns, and common traps

new_qs = [
    {
        "id": "a2_10_q081",
        "subjectId": "a2_10",
        "topicId": "a2_10",
        "topicName": "Konjunktionen",
        "sourceId": "manual",
        "originalId": "manual_081",
        "level": "A2",
        "type": "multiple_choice",
        "questionText": "______ du morgen Zeit hast, können wir zusammen lernen.",
        "options": ["Wenn", "Als", "Obwohl", "Damit"],
        "correctAnswer": "Wenn",
        "explanation": "wenn — conditional conjunction ('if'), used for future or general conditions. Note: wenn can mean 'when' (temporal) or 'if' (conditional) depending on context.",
        "difficulty": "medium"
    },
    {
        "id": "a2_10_q082",
        "subjectId": "a2_10",
        "topicId": "a2_10",
        "topicName": "Konjunktionen",
        "sourceId": "manual",
        "originalId": "manual_082",
        "level": "A2",
        "type": "multiple_choice",
        "questionText": "Ich war schon müde, ______ ich ins Bett ging.",
        "options": ["wenn", "als", "weil", "obwohl"],
        "correctAnswer": "als",
        "explanation": "als — temporal conjunction for a single past event ('when'). wenn is used for repeated or future events. Here: a single past event → als.",
        "difficulty": "medium"
    },
    {
        "id": "a2_10_q083",
        "subjectId": "a2_10",
        "topicId": "a2_10",
        "topicName": "Konjunktionen",
        "sourceId": "manual",
        "originalId": "manual_083",
        "level": "A2",
        "type": "multiple_choice",
        "questionText": "______ es regnet, bleibe ich zu Hause.",
        "options": ["Weil", "Obwohl", "Wenn", "Damit"],
        "correctAnswer": "Wenn",
        "explanation": "wenn — conditional conjunction ('if'), here expresses a general condition. weil would express a reason for something already true.",
        "difficulty": "easy"
    },
    {
        "id": "a2_10_q084",
        "subjectId": "a2_10",
        "topicId": "a2_10",
        "topicName": "Konjunktionen",
        "sourceId": "manual",
        "originalId": "manual_084",
        "level": "A2",
        "type": "multiple_choice",
        "questionText": "Er ist nicht gekommen, ______ er krank war.",
        "options": ["weil", "obwohl", "wenn", "damit"],
        "correctAnswer": "weil",
        "explanation": "weil — causal conjunction ('because'). Here the reason is given for the consequence (not coming). obwohl would mean 'although' — the opposite.",
        "difficulty": "easy"
    },
    {
        "id": "a2_10_q085",
        "subjectId": "a2_10",
        "topicId": "a2_10",
        "topicName": "Konjunktionen",
        "sourceId": "manual",
        "originalId": "manual_085",
        "level": "A2",
        "type": "multiple_choice",
        "questionText": "______ die Sonne scheint, gehen wir spazieren.",
        "options": ["Weil", "Obwohl", "Wenn", "Damit"],
        "correctAnswer": "Wenn",
        "explanation": "wenn — conditional conjunction for a general/future condition ('if'). weil would be grammatically correct but changes the meaning to causal ('because').",
        "difficulty": "medium"
    },
    {
        "id": "a2_10_q086",
        "subjectId": "a2_10",
        "topicId": "a2_10",
        "topicName": "Konjunktionen",
        "sourceId": "manual",
        "originalId": "manual_086",
        "level": "A2",
        "type": "multiple_choice",
        "questionText": "Das Buch war ______ teuer ______ ich es nicht kaufen konnte.",
        "options": ["sowohl / als auch", "weder / noch", "entweder / oder", "zwar / aber"],
        "correctAnswer": "zwar / aber",
        "explanation": "zwar ... aber — 'although ... but'. This structure admits one fact (expensive) while stating the opposite consequence (couldn't buy it).",
        "difficulty": "medium"
    },
    {
        "id": "a2_10_q087",
        "subjectId": "a2_10",
        "topicId": "a2_10",
        "topicName": "Konjunktionen",
        "sourceId": "manual",
        "originalId": "manual_087",
        "level": "A2",
        "type": "multiple_choice",
        "questionText": "Er lernt Deutsch, ______ er in Deutschland studieren will.",
        "options": ["weil", "obwohl", "wenn", "damit"],
        "correctAnswer": "weil",
        "explanation": "weil — causal conjunction ('because'). The reason for learning German is given here (wanting to study in Germany).",
        "difficulty": "easy"
    },
    {
        "id": "a2_10_q088",
        "subjectId": "a2_10",
        "topicId": "a2_10",
        "topicName": "Konjunktionen",
        "sourceId": "manual",
        "originalId": "manual_088",
        "level": "A2",
        "type": "multiple_choice",
        "questionText": "______ sie gut Deutsch sprach, konnte sie die Prüfung bestehen.",
        "options": ["Weil", "Obwohl", "Wenn", "Damit"],
        "correctAnswer": "Weil",
        "explanation": "weil — causal conjunction ('because'). Her good German is the reason she could pass the exam.",
        "difficulty": "easy"
    },
    {
        "id": "a2_10_q089",
        "subjectId": "a2_10",
        "topicId": "a2_10",
        "topicName": "Konjunktionen",
        "sourceId": "manual",
        "originalId": "manual_089",
        "level": "A2",
        "type": "multiple_choice",
        "questionText": "Sie ist sehr intelligent, ______ sie lernt wenig.",
        "options": ["weil", "obwohl", "wenn", "damit"],
        "correctAnswer": "obwohl",
        "explanation": "obwohl — contrast conjunction ('although'). The fact (intelligent) contradicts the expectation (learning little). This is a typical contrast structure.",
        "difficulty": "medium"
    },
    {
        "id": "a2_10_q090",
        "subjectId": "a2_10",
        "topicId": "a2_10",
        "topicName": "Konjunktionen",
        "sourceId": "manual",
        "originalId": "manual_090",
        "level": "A2",
        "type": "multiple_choice",
        "questionText": "______ es spät war, haben wir das Projekt noch fertiggestellt.",
        "options": ["Weil", "Obwohl", "Wenn", "Damit"],
        "correctAnswer": "Obwohl",
        "explanation": "obwohl — contrast conjunction ('although'). Being late contradicts the result (finishing the project). If we used weil, it would mean 'because it was late, we finished' — which changes the meaning.",
        "difficulty": "medium"
    },
    {
        "id": "a2_10_q091",
        "subjectId": "a2_10",
        "topicId": "a2_10",
        "topicName": "Konjunktionen",
        "sourceId": "manual",
        "originalId": "manual_091",
        "level": "A2",
        "type": "multiple_choice",
        "questionText": "Er spricht ______ Deutsch ______ Französisch.",
        "options": ["sowohl / als auch", "entweder / oder", "weder / noch", "zwar / aber"],
        "correctAnswer": "sowohl / als auch",
        "explanation": "sowohl ... als auch — 'both ... and'. Connects two positive abilities (German AND French).",
        "difficulty": "easy"
    },
    {
        "id": "a2_10_q092",
        "subjectId": "a2_10",
        "topicId": "a2_10",
        "topicName": "Konjunktionen",
        "sourceId": "manual",
        "originalId": "manual_092",
        "level": "A2",
        "type": "multiple_choice",
        "questionText": "Ich habe ______ Zeit ______ Geld — ich kann nicht reisen.",
        "options": ["weder / noch", "sowohl / als auch", "entweder / oder", "zwar / aber"],
        "correctAnswer": "weder / noch",
        "explanation": "weder ... noch — 'neither ... nor'. Both conditions (time AND money) are missing. This is a negative combination of two elements.",
        "difficulty": "medium"
    },
    {
        "id": "a2_10_q093",
        "subjectId": "a2_10",
        "topicId": "a2_10",
        "topicName": "Konjunktionen",
        "sourceId": "manual",
        "originalId": "manual_093",
        "level": "A2",
        "type": "multiple_choice",
        "questionText": "Du kannst ______ heute kommen ______ morgen — wie du willst.",
        "options": ["entweder / oder", "sowohl / als auch", "weder / noch", "zwar / aber"],
        "correctAnswer": "entweder / oder",
        "explanation": "entweder ... oder — 'either ... or'. Two possible options are given, one of which will be chosen. The choice is open.",
        "difficulty": "easy"
    },
    {
        "id": "a2_10_q094",
        "subjectId": "a2_10",
        "topicId": "a2_10",
        "topicName": "Konjunktionen",
        "sourceId": "manual",
        "originalId": "manual_094",
        "level": "A2",
        "type": "multiple_choice",
        "questionText": "______ du fleißig lernst, ______ wirst du die Prüfung bestehen.",
        "options": ["Wenn / dann", "Weil / deshalb", "Obwohl / aber", "Sowohl / als auch"],
        "correctAnswer": "Wenn / dann",
        "explanation": "wenn ... dann — conditional pattern ('if ... then'). The dann clause uses normal word order (subject + verb) because it's the main clause, not a subordinate clause.",
        "difficulty": "medium"
    },
    {
        "id": "a2_10_q095",
        "subjectId": "a2_10",
        "topicId": "a2_10",
        "topicName": "Konjunktionen",
        "sourceId": "manual",
        "originalId": "manual_095",
        "level": "A2",
        "type": "multiple_choice",
        "questionText": "Er ist so müde, ______ er sofort einschlief.",
        "options": ["dass", "weil", "obwohl", "wenn"],
        "correctAnswer": "dass",
        "explanation": "dass — noun clause conjunction ('that'). Here it introduces a result clause after 'so...dass' pattern. The verb is at the end in the dass-clause.",
        "difficulty": "medium"
    },
    {
        "id": "a2_10_q096",
        "subjectId": "a2_10",
        "topicId": "a2_10",
        "topicName": "Konjunktionen",
        "sourceId": "manual",
        "originalId": "manual_096",
        "level": "A2",
        "type": "multiple_choice",
        "questionText": "Sie hat mir geholfen, ______ ich erfolgreich war.",
        "options": ["weil", "damit", "obwohl", "wenn"],
        "correctAnswer": "damit",
        "explanation": "damit — purpose conjunction ('so that / in order that'). The help was given with the intention of achieving a result (success).",
        "difficulty": "medium"
    },
    {
        "id": "a2_10_q097",
        "subjectId": "a2_10",
        "topicId": "a2_10",
        "topicName": "Konjunktionen",
        "sourceId": "manual",
        "originalId": "manual_097",
        "level": "A2",
        "type": "multiple_choice",
        "questionText": "______ ich gestern krank war, bin ich nicht zur Arbeit gegangen.",
        "options": ["Weil", "Obwohl", "Wenn", "Damit"],
        "correctAnswer": "Weil",
        "explanation": "weil — causal conjunction ('because'). The reason for not going to work is given. Because I was sick → I didn't go.",
        "difficulty": "easy"
    },
    {
        "id": "a2_10_q098",
        "subjectId": "a2_10",
        "topicId": "a2_10",
        "topicName": "Konjunktionen",
        "sourceId": "manual",
        "originalId": "manual_098",
        "level": "A2",
        "type": "multiple_choice",
        "questionText": "Nicht nur ______ er fleißig, ______ half er auch anderen.",
        "options": ["war / sondern", "ist / aber", "war / und", "hat / aber"],
        "correctAnswer": "war / sondern",
        "explanation": "nicht nur ... sondern auch — 'not only ... but also'. This is a two-part correlating conjunction. The second part requires sondern (not aber) to properly contrast and add.",
        "difficulty": "medium"
    },
    {
        "id": "a2_10_q099",
        "subjectId": "a2_10",
        "topicId": "a2_10",
        "topicName": "Konjunktionen",
        "sourceId": "manual",
        "originalId": "manual_099",
        "level": "A2",
        "type": "multiple_choice",
        "questionText": "Er ist so stark, ______ er drei Koffer allein tragen kann.",
        "options": ["dass", "weil", "obwohl", "wenn"],
        "correctAnswer": "dass",
        "explanation": "dass — introduces a result clause after 'so...dass' ('so...that'). The result is that he can carry three suitcases alone.",
        "difficulty": "medium"
    },
    {
        "id": "a2_10_q100",
        "subjectId": "a2_10",
        "topicId": "a2_10",
        "topicName": "Konjunktionen",
        "sourceId": "manual",
        "originalId": "manual_100",
        "level": "A2",
        "type": "multiple_choice",
        "questionText": "Sie trägt immer einen Schirm, ______ es regnet oder nicht.",
        "options": ["weil", "obwohl", "wenn", "damit"],
        "correctAnswer": "obwohl",
        "explanation": "obwohl — 'regardless of whether'. The umbrella is carried even when it is NOT raining — contradictory behavior that obwohl captures perfectly.",
        "difficulty": "hard"
    },
]

translated_questions.extend(new_qs)
print(f"Total questions after adding new ones: {len(translated_questions)}")

# ─── ADD TOPIC DESCRIPTION AND TIPS ───
data['description'] = (
    "Konjunktionen (conjunctions) are words that connect clauses or sentences. "
    "In German, they are divided into two main groups: coordinating conjunctions (nebenordnend) "
    "and subordinating conjunctions (unterordnend). The key difference lies in word order: "
    "in subordinate clauses, the verb moves to the end of the clause."
)
data['tips'] = (
    "KEY RULES:\n"
    "1. Verb position in subordinate clauses: The conjugated verb ALWAYS goes at the end of the clause. "
    "Example: Ich bin müde, weil ich nicht geschlafen habe. (NOT 'weil ich nicht habe geschlafen')\n\n"
    "2. Coherent pairs (zweiteilige Konjunktionen): These fixed combinations cannot be rearranged:\n"
    "   - sowohl ... als auch (both ... and)\n"
    "   - entweder ... oder (either ... or)\n"
    "   - weder ... noch (neither ... nor)\n"
    "   - nicht nur ... sondern auch (not only ... but also)\n"
    "   - zwar ... aber (although ... but)\n\n"
    "3. wenn vs als: wenn is for repeated or general events ('whenever') and for conditions ('if'). "
    "als is for a single past event ('when'). Example: Als ich ein Kind war, lebte ich in Berlin. (one-time past)\n\n"
    "4. obwohl vs trotzdem: obwohl introduces a subordinate clause (verb at end). "
    "trotzdem is a conjunctive adverb (comes before verb in main clause). Example: "
       "Obwohl es regnete, ging ich aus. / Es regnete, trotzdem ging ich aus.\n\n"
    "5. Word order after conjunctions: In MAIN clauses, the verb comes immediately after the conjunction. "
    "In SUBORDINATE clauses, the verb goes to the end. Example of a main clause after 'und': "
    "Ich lernte Deutsch und ich fing an zu lesen. (NOT 'und ich fing an zu lesen' is also acceptable — this is a special case with 'und')\n\n"
    "COMMON TRAPS:\n"
    "- 'Weil' with verb at the end: Weil ich habe keine Zeit. → Weil ich keine Zeit habe.\n"
    "- Mixing up 'obwohl' and 'trotzdem' positions: Obwohl is a conjunction (verb-end), trotzdem is an adverb (verb-first).\n"
    "- Using 'und' with verb-end: 'Und' is a coordinating conjunction — it does NOT move the verb to the end like subordinating conjunctions do."
)

data['totalQuestions'] = len(translated_questions)
data['questions'] = translated_questions

with open('app/src/main/assets/a2_10.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ a2_10.json updated successfully!")
print(f"   Total questions: {len(translated_questions)}")
print(f"   Description: {data['description'][:60]}...")
print(f"   Tips length: {len(data['tips'])} chars")