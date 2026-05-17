#!/usr/bin/env python3
import json

# Read original file from git (clean, untranslated)
import subprocess
result = subprocess.run(['git', 'show', 'HEAD:app/src/main/assets/a2_10.json'],
                       capture_output=True, text=True,
                       cwd='/home/node/.openclaw/workspace/b2-deutsch-app')
original = json.loads(result.stdout)

# ─── DETAILED TRANSLATION MAP ───
# Each Turkish explanation → English translation
translations = {
    # Q1
    "zwar ... aber — 'Gerçi ... ama' (bir durumu kabul edip zıttını söyler).":
        "zwar ... aber — 'although ... but' (admits one fact while stating the opposite).",

    # Q2
    "Je ... desto/umso — 'Ne kadar ... o kadar'. Hem desto hem umso kullanılabilir.":
        "Je ... desto/umso — 'the more ... the more'. Both desto and umso can be used.",

    # Q3
    "da — sebep bildirir, weil ile aynıdır ancak cümle başında daha sık kullanılır.":
        "da — expresses a reason like 'because', but is more often used at the beginning of a sentence.",

    # Q4
    "obwohl — 'Rağmen' anlamında, yan cümle (fiil sonda) kurar.":
        "obwohl — 'although' means, it forms a subordinate clause (verb at the end).",

    # Q5
    "entweder ... oder — 'Ya ... ya da' (iki seçenekten biri).":
        "entweder ... oder — 'either ... or' (one of two options).",

    # Q6
    "obwohl — fiil cümle sonunda olduğu için obwohl kullanılmalı.":
        "obwohl — must be used because the verb is at the end of the clause.",

    # Q7
    "sowohl ... als auch — 'Hem ... hem de' (her ikisi de).":
        "sowohl ... als auch — 'both ... and' (both of them).",

    # Q8
    "deshalb — 'Bu yüzden' (zarf-bağlaç, fiil hemen arkasından gelir).":
        "deshalb — 'therefore' (adverbial conjunction, comes right after the verb).",

    # Q9
    "nicht nur ... sondern auch — 'Sadece ... değil, aynı zamanda'.":
        "nicht nur ... sondern auch — 'not only ... but also'.",

    # Q10
    "obwohl — cümle başında 'rağmen' anlamında yan cümle.":
        "obwohl — at the beginning of the sentence means 'although' — a subordinate clause.",

    # Q11
    "weder ... noch — 'Ne ... ne de' (her iki seçeneği de reddeder).":
        "weder ... noch — 'neither ... nor' (rejects both options).",

    # Q12
    "folglich — 'Sonuç olarak / bu nedenle' anlamında akademik bir bağlaç.":
        "folglich — 'consequently / for this reason' — an academic conjunction.",

    # Q13
    "trotzdem — 'Buna rağmen' (cümle ortasında fiilden önce gelir).":
        "trotzdem — 'nevertheless / however' (comes before the verb in the middle of a sentence).",

    # Q14
    "dass (nesne cümlesi) + um...zu (amaç cümlesi).":
        "dass (noun clause) + um...zu (purpose clause).",

    # Q15
    "Je ... desto/umso — kural: ilk kısım her zaman Je, ikinci kısım desto veya umso.":
        "Je ... desto/umso — rule: first part is always Je, second part is desto or umso.",

    # Q16
    "nicht nur ... sondern auch — iki olumlu durumu pekiştirir.":
        "nicht nur ... sondern auch — connects two positive situations.",

    # Q17
    "damit — amaç bildirir (özne iki cümlede farklıysa um...zu yerine kullanılır).":
        "damit — expresses purpose / intention (used instead of um...zu when the subject is different in both clauses).",

    # Q18
    "obwohl — 'Rağmen' (yan cümle yapısı, fiilolta).":
        "obwohl — 'although' (subordinate clause structure, verb at the end).",

    # Q19
    "weder ... noch — her iki seçeneği de reddeder ('ne ... ne de').":
        "weder ... noch — rejects both options ('neither ... nor').",

    # Q20
    "trotzdem / dennoch — 'Yine de / buna rağmen' anlamında her ikisi de uygundur.":
        "trotzdem / dennoch — both are suitable, meaning 'nevertheless / however'.",

    # Q21
    "obwohl — beklenmedik sonuç, karşıtlık bildirir.":
        "obwohl — unexpected result, expresses contrast.",

    # Q22
    "solange — devam eden koşul ('olduğu sürece').":
        "solange — continuing condition ('as long as').",

    # Q23
    "obgleich — obwohl ile eş anlamlı, yazılı ve resmi dilde kullanılır.":
        "obgleich — synonymous with obwohl, used in written and formal language.",

    # Q24
    "da — sebep bildiren bağlaç, yazılı dilde weil yerine kullanılır.":
        "da — causal conjunction, used instead of weil in written language.",

    # Q25
    "sodass — sonuç bildiren bağlaç ('öyle ki ...').":
        "sodass — consequence conjunction ('so that ...').",

    # Q26
    "weder ... noch — iki olumsuz seçeneği birleştirir.":
        "weder ... noch — combines two negative options.",

    # Q27
    "sowohl ... als auch — iki olumlu seçeneği birleştirir.":
        "sowohl ... als auch — combines two positive options.",

    # Q28
    "während — eş zamanlı karşıt durum ('iken' — iki olay aynı anda).":
        "während — simultaneous contrast ('while' — two events at the same time).",

    # Q29
    "um ... zu — amaç bildiren yapı (özne her iki cümlede aynı).":
        "um ... zu — purpose structure (the subject is the same in both clauses).",

    # Q30
    "wenn — koşul cümlesi (Konjunktiv II ile, 'als ob' benzeri yapı).":
        "wenn — conditional clause (with Konjunktiv II, structure similar to 'als ob').",

    # Q31
    "sofern not / nur wenn — her ikisi de olumsuz koşul bildirir.":
        "sofern not / nur wenn — both express a negative condition.",

    # Q32
    "obwohl — karşıtlık bildiren bağlaç.":
        "obwohl — contrast conjunction.",

    # Q33
    "nachdem — zamansal bağlaç, önceki eylem.":
        "nachdem — temporal conjunction, previous action.",

    # Q34
    "weil — sebep bildiren bağlaç.":
        "weil — causal conjunction.",

    # Q35
    "aber — karşıtlık bildiren bağlaç.":
        "aber — contrast conjunction.",

    # Q36
    "sondern — olumsuzdan sonra karşıt ifade.":
        "sondern — contrast statement after a negation.",

    # Q37
    "weil — sebep bildiren bağlaç.":
        "weil — causal conjunction.",

    # Q38
    "ob — dolaylı soru.":
        "ob — indirect question.",

    # Q39
    "obwohl — karşıtlık bildiren bağlaç.":
        "obwohl — contrast conjunction.",

    # Q40
    "denn — sebep bildiren bağlaç.":
        "denn — causal conjunction.",

    # Q41
    "weil — sebep bildiren bağlaç.":
        "weil — causal conjunction.",

    # Q42
    "damit — amaç bildiren bağlaç.":
        "damit — purpose conjunction.",

    # Q43
    "trotzdem — karşıtlık bildiren zarf.":
        "trotzdem — contrast adverb.",

    # Q44
    "weil — sebep bildiren bağlaç.":
        "weil — causal conjunction.",

    # Q45
    "trotzdem — karşıtlık bildiren zarf.":
        "trotzdem — contrast adverb.",

    # Q46
    "obwohl — karşıtlık bildiren bağlaç.":
        "obwohl — contrast conjunction.",

    # Q47
    "sondern — nicht nur ... sondern auch yapısı.":
        "sondern — part of the nicht nur ... sondern auch structure.",

    # Q48
    "weil — sebep bildiren bağlaç.":
        "weil — causal conjunction.",

    # Q49
    "obwohl — karşıtlık bildiren bağlaç.":
        "obwohl — contrast conjunction.",

    # Q50
    "damit — amaç bildiren bağlaç.":
        "damit — purpose conjunction.",

    # Q51
    "weil — sebep bildiren bağlaç.":
        "weil — causal conjunction.",

    # Q52
    "sodass — sonuç bildiren bağlaç ('öyle ki ...').":
        "sodass — consequence conjunction ('so that ...').",

    # Q53
    "obwohl — karşıtlık bildiren bağlaç.":
        "obwohl — contrast conjunction.",

    # Q54
    "nicht so / wie — karşılaştırma.":
        "nicht so / wie — comparison.",

    # Q55
    "obwohl — karşıtlık bildiren bağlaç.":
        "obwohl — contrast conjunction.",

    # Q56
    "obwohl ... trotzdem — karşıtlık.":
        "obwohl ... trotzdem — contrast.",

    # Q57
    "als — scheinbar karşılaştırma (als ob / als wenn).":
        "als — apparent comparison (als ob / als wenn).",

    # Q58
    "weil — sebep bildiren bağlaç.":
        "weil — causal conjunction.",

    # Q59
    "um ... zu — amaç bildiren yapı.":
        "um ... zu — purpose structure.",

    # Q60
    "weder ... noch — her iki seçeneği de reddeder.":
        "weder ... noch — rejects both options.",

    # Q61
    "wenn — koşul veya zaman bağlacı.":
        "wenn — conditional or temporal conjunction.",

    # Q62
    "obwohl — karşıtlık bildiren bağlaç.":
        "obwohl — contrast conjunction.",

    # Q63
    "als — geçmiş tek olay.":
        "als — a single past event.",

    # Q64
    "weil — sebep bildiren bağlaç.":
        "weil — causal conjunction.",

    # Q65
    "nicht nur ... sondern auch — pekiştirme.":
        "nicht nur ... sondern auch — reinforcement.",

    # Q66
    "damit — amaç bildiren bağlaç.":
        "damit — purpose conjunction.",

    # Q67
    "während — eş zamanlı bağlaç.":
        "während — simultaneous conjunction.",

    # Q68
    "wenn — tekrarlanan olay.":
        "wenn — repeated event.",

    # Q69
    "deshalb — sonuç bildiren zarf.":
        "deshalb — consequence adverb.",

    # Q70
    "obwohl — beklenmedik sonuç.":
        "obwohl — unexpected result.",

    # Q71
    "dass — nesne cümlesi.":
        "dass — noun clause.",

    # Q72
    "weder / noch — olumsuz birleşim.":
        "weder / noch — negative combination.",

    # Q73
    "entweder / oder — seçim.":
        "entweder / oder — choice.",

    # Q74
    "sobald — zaman bağlacı.":
        "sobald — temporal conjunction.",

    # Q75
    "obwohl — karşıtlık.":
        "obwohl — contrast.",

    # Q76
    "weil — sebep.":
        "weil — reason.",

    # Q77
    "da — sebep (yazılı dilde).":
        "da — reason (in written language).",

    # Q78
    "bevor — zaman bağlacı.":
        "bevor — temporal conjunction.",

    # Q79
    "sodass — sonuç.":
        "sodass — consequence.",

    # Q80
    "damit — amaç.":
        "damit — purpose.",
}

# Answer translations
answer_translations = {
    "Hem A hem B doğru": "Both A and B are correct",
    "Hem B hem C doğru": "Both B and C are correct",
    "Hem A hem C doğru": "Both A and C are correct",
    "A ve B doğru": "Both A and B are correct",
    "da (weil anlamında)": "da (means 'because')",
    "folglich (deshalb anlamında)": "folglich (means 'therefore')",
}

translated_qs = []
for q in original['questions']:
    q = dict(q)
    orig_exp = q.get('explanation', '')
    orig_ans = q.get('correctAnswer', '')

    # Translate explanation
    q['explanation'] = translations.get(orig_exp, orig_exp)

    # Translate answer
    q['correctAnswer'] = answer_translations.get(orig_ans, orig_ans)

    q['sourceId'] = 'manual'
    translated_qs.append(q)

print(f"Translated {len(translated_qs)} questions")
# Verify
for i in [0, 1, 2, 3, 4, 5, 8, 14, 20, 30]:
    q = translated_qs[i]
    print(f"Q{i+1}: [{q['correctAnswer']}] {q['explanation'][:100]}")

print()

# ─── ADD 20 NEW QUESTIONS ───
new_qs = [
    {
        "id": "a2_10_q081", "subjectId": "a2_10", "topicId": "a2_10", "topicName": "Konjunktionen",
        "sourceId": "manual", "originalId": "manual_081", "level": "A2",
        "type": "multiple_choice",
        "questionText": "______ du morgen Zeit hast, können wir zusammen lernen.",
        "options": ["Wenn", "Als", "Obwohl", "Damit"],
        "correctAnswer": "Wenn",
        "explanation": "wenn — conditional conjunction ('if'), used for future or general conditions. wenn can mean 'when' (temporal) or 'if' (conditional) depending on context.",
        "difficulty": "medium"
    },
    {
        "id": "a2_10_q082", "subjectId": "a2_10", "topicId": "a2_10", "topicName": "Konjunktionen",
        "sourceId": "manual", "originalId": "manual_082", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Ich war schon müde, ______ ich ins Bett ging.",
        "options": ["wenn", "als", "weil", "obwohl"],
        "correctAnswer": "als",
        "explanation": "als — temporal conjunction for a single past event ('when'). wenn is used for repeated or future events. Here: a single past event → als.",
        "difficulty": "medium"
    },
    {
        "id": "a2_10_q083", "subjectId": "a2_10", "topicId": "a2_10", "topicName": "Konjunktionen",
        "sourceId": "manual", "originalId": "manual_083", "level": "A2",
        "type": "multiple_choice",
        "questionText": "______ es regnet, bleibe ich zu Hause.",
        "options": ["Wenn", "Weil", "Obwohl", "Damit"],
        "correctAnswer": "Wenn",
        "explanation": "wenn — conditional conjunction ('if'), here expresses a general condition. weil would express a reason for something already true.",
        "difficulty": "easy"
    },
    {
        "id": "a2_10_q084", "subjectId": "a2_10", "topicId": "a2_10", "topicName": "Konjunktionen",
        "sourceId": "manual", "originalId": "manual_084", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Er ist nicht gekommen, ______ er krank war.",
        "options": ["weil", "obwohl", "wenn", "damit"],
        "correctAnswer": "weil",
        "explanation": "weil — causal conjunction ('because'). Here the reason is given for the consequence (not coming). obwohl would mean 'although' — the opposite.",
        "difficulty": "easy"
    },
    {
        "id": "a2_10_q085", "subjectId": "a2_10", "topicId": "a2_10", "topicName": "Konjunktionen",
        "sourceId": "manual", "originalId": "manual_085", "level": "A2",
        "type": "multiple_choice",
        "questionText": "______ die Sonne scheint, gehen wir spazieren.",
        "options": ["Weil", "Obwohl", "Wenn", "Damit"],
        "correctAnswer": "Wenn",
        "explanation": "wenn — conditional conjunction for a general/future condition ('if'). weil would be grammatically correct but changes the meaning to causal ('because').",
        "difficulty": "medium"
    },
    {
        "id": "a2_10_q086", "subjectId": "a2_10", "topicId": "a2_10", "topicName": "Konjunktionen",
        "sourceId": "manual", "originalId": "manual_086", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Das Buch war ______ teuer ______ ich es nicht kaufen konnte.",
        "options": ["sowohl / als auch", "weder / noch", "entweder / oder", "zwar / aber"],
        "correctAnswer": "zwar / aber",
        "explanation": "zwar ... aber — 'although ... but'. This structure admits one fact (expensive) while stating the opposite consequence (couldn't buy it).",
        "difficulty": "medium"
    },
    {
        "id": "a2_10_q087", "subjectId": "a2_10", "topicId": "a2_10", "topicName": "Konjunktionen",
        "sourceId": "manual", "originalId": "manual_087", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Er lernt Deutsch, ______ er in Deutschland studieren will.",
        "options": ["weil", "obwohl", "wenn", "damit"],
        "correctAnswer": "weil",
        "explanation": "weil — causal conjunction ('because'). The reason for learning German is given here (wanting to study in Germany).",
        "difficulty": "easy"
    },
    {
        "id": "a2_10_q088", "subjectId": "a2_10", "topicId": "a2_10", "topicName": "Konjunktionen",
        "sourceId": "manual", "originalId": "manual_088", "level": "A2",
        "type": "multiple_choice",
        "questionText": "______ sie gut Deutsch sprach, konnte sie die Prüfung bestehen.",
        "options": ["Weil", "Obwohl", "Wenn", "Damit"],
        "correctAnswer": "Weil",
        "explanation": "weil — causal conjunction ('because'). Her good German is the reason she could pass the exam.",
        "difficulty": "easy"
    },
    {
        "id": "a2_10_q089", "subjectId": "a2_10", "topicId": "a2_10", "topicName": "Konjunktionen",
        "sourceId": "manual", "originalId": "manual_089", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Sie ist sehr intelligent, ______ sie lernt wenig.",
        "options": ["weil", "obwohl", "wenn", "damit"],
        "correctAnswer": "obwohl",
        "explanation": "obwohl — contrast conjunction ('although'). The fact (intelligent) contradicts the expectation (learning little). This is a typical contrast structure.",
        "difficulty": "medium"
    },
    {
        "id": "a2_10_q090", "subjectId": "a2_10", "topicId": "a2_10", "topicName": "Konjunktionen",
        "sourceId": "manual", "originalId": "manual_090", "level": "A2",
        "type": "multiple_choice",
        "questionText": "______ es spät war, haben wir das Projekt noch fertiggestellt.",
        "options": ["Weil", "Obwohl", "Wenn", "Damit"],
        "correctAnswer": "Obwohl",
        "explanation": "obwohl — contrast conjunction ('although'). Being late contradicts the result (finishing the project). Using weil would mean 'because it was late, we finished' — changing the meaning.",
        "difficulty": "medium"
    },
    {
        "id": "a2_10_q091", "subjectId": "a2_10", "topicId": "a2_10", "topicName": "Konjunktionen",
        "sourceId": "manual", "originalId": "manual_091", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Er spricht ______ Deutsch ______ Französisch.",
        "options": ["sowohl / als auch", "entweder / oder", "weder / noch", "zwar / aber"],
        "correctAnswer": "sowohl / als auch",
        "explanation": "sowohl ... als auch — 'both ... and'. Connects two positive abilities (German AND French).",
        "difficulty": "easy"
    },
    {
        "id": "a2_10_q092", "subjectId": "a2_10", "topicId": "a2_10", "topicName": "Konjunktionen",
        "sourceId": "manual", "originalId": "manual_092", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Ich habe ______ Zeit ______ Geld — ich kann nicht reisen.",
        "options": ["weder / noch", "sowohl / als auch", "entweder / oder", "zwar / aber"],
        "correctAnswer": "weder / noch",
        "explanation": "weder ... noch — 'neither ... nor'. Both conditions (time AND money) are missing. This is a negative combination of two elements.",
        "difficulty": "medium"
    },
    {
        "id": "a2_10_q093", "subjectId": "a2_10", "topicId": "a2_10", "topicName": "Konjunktionen",
        "sourceId": "manual", "originalId": "manual_093", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Du kannst ______ heute kommen ______ morgen — wie du willst.",
        "options": ["entweder / oder", "sowohl / als auch", "weder / noch", "zwar / aber"],
        "correctAnswer": "entweder / oder",
        "explanation": "entweder ... oder — 'either ... or'. Two possible options are given, one of which will be chosen. The choice is open.",
        "difficulty": "easy"
    },
    {
        "id": "a2_10_q094", "subjectId": "a2_10", "topicId": "a2_10", "topicName": "Konjunktionen",
        "sourceId": "manual", "originalId": "manual_094", "level": "A2",
        "type": "multiple_choice",
        "questionText": "______ du fleißig lernst, ______ wirst du die Prüfung bestehen.",
        "options": ["Wenn / dann", "Weil / deshalb", "Obwohl / aber", "Sowohl / als auch"],
        "correctAnswer": "Wenn / dann",
        "explanation": "wenn ... dann — conditional pattern ('if ... then'). The dann clause uses normal word order (subject + verb) because it is the main clause, not a subordinate clause.",
        "difficulty": "medium"
    },
    {
        "id": "a2_10_q095", "subjectId": "a2_10", "topicId": "a2_10", "topicName": "Konjunktionen",
        "sourceId": "manual", "originalId": "manual_095", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Er ist so müde, ______ er sofort einschlief.",
        "options": ["dass", "weil", "obwohl", "wenn"],
        "correctAnswer": "dass",
        "explanation": "dass — noun clause conjunction ('that'). Here it introduces a result clause after 'so...dass' pattern. The verb is at the end in the dass-clause.",
        "difficulty": "medium"
    },
    {
        "id": "a2_10_q096", "subjectId": "a2_10", "topicId": "a2_10", "topicName": "Konjunktionen",
        "sourceId": "manual", "originalId": "manual_096", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Sie hat mir geholfen, ______ ich erfolgreich war.",
        "options": ["weil", "damit", "obwohl", "wenn"],
        "correctAnswer": "damit",
        "explanation": "damit — purpose conjunction ('so that / in order that'). The help was given with the intention of achieving a result (success).",
        "difficulty": "medium"
    },
    {
        "id": "a2_10_q097", "subjectId": "a2_10", "topicId": "a2_10", "topicName": "Konjunktionen",
        "sourceId": "manual", "originalId": "manual_097", "level": "A2",
        "type": "multiple_choice",
        "questionText": "______ ich gestern krank war, bin ich nicht zur Arbeit gegangen.",
        "options": ["Weil", "Obwohl", "Wenn", "Damit"],
        "correctAnswer": "Weil",
        "explanation": "weil — causal conjunction ('because'). The reason for not going to work is given. Because I was sick → I didn't go.",
        "difficulty": "easy"
    },
    {
        "id": "a2_10_q098", "subjectId": "a2_10", "topicId": "a2_10", "topicName": "Konjunktionen",
        "sourceId": "manual", "originalId": "manual_098", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Nicht nur ______ er fleißig, ______ half er auch anderen.",
        "options": ["war / sondern", "ist / aber", "war / und", "hat / aber"],
        "correctAnswer": "war / sondern",
        "explanation": "nicht nur ... sondern auch — 'not only ... but also'. This is a two-part correlating conjunction. The second part requires sondern (not aber) to properly contrast and add.",
        "difficulty": "medium"
    },
    {
        "id": "a2_10_q099", "subjectId": "a2_10", "topicId": "a2_10", "topicName": "Konjunktionen",
        "sourceId": "manual", "originalId": "manual_099", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Er ist so stark, ______ er drei Koffer allein tragen kann.",
        "options": ["dass", "weil", "obwohl", "wenn"],
        "correctAnswer": "dass",
        "explanation": "dass — introduces a result clause after 'so...dass' ('so...that'). The result is that he can carry three suitcases alone.",
        "difficulty": "medium"
    },
    {
        "id": "a2_10_q100", "subjectId": "a2_10", "topicId": "a2_10", "topicName": "Konjunktionen",
        "sourceId": "manual", "originalId": "manual_100", "level": "A2",
        "type": "multiple_choice",
        "questionText": "Sie trägt immer einen Schirm, ______ es regnet oder nicht.",
        "options": ["weil", "obwohl", "wenn", "damit"],
        "correctAnswer": "obwohl",
        "explanation": "obwohl — 'regardless of whether'. The umbrella is carried even when it is NOT raining — a contradictory behavior that obwohl captures perfectly.",
        "difficulty": "hard"
    },
]

translated_qs.extend(new_qs)
print(f"\nTotal questions: {len(translated_qs)}")

# ─── ADD TOPIC DESCRIPTION AND TIPS ───
description = (
    "Konjunktionen (conjunctions) are words that connect clauses or sentences. "
    "In German, they are divided into two main groups: coordinating conjunctions (nebenordnend) "
    "and subordinating conjunctions (unterordnend). The key difference lies in word order: "
    "in subordinate clauses, the verb moves to the end of the clause."
)

tips = (
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
    "5. wenn vs weil: wenn expresses a condition ('if') and introduces a subordinate clause. "
    "weil expresses a reason ('because'). Example: Wenn es regnet, bleibe ich zu Hause. (condition) "
    "vs. Ich bleibe zu Hause, weil es regnet. (reason)\n\n"
    "6. Word order after 'und': 'Und' is a coordinating conjunction — it does NOT move the verb to the end. "
    "The verb stays in normal position: Ich lernte Deutsch und las viele Bücher.\n\n"
    "COMMON TRAPS:\n"
    "- 'Weil' with verb at the end: Weil ich habe keine Zeit. → Weil ich keine Zeit habe.\n"
    "- Mixing up 'obwohl' and 'trotzdem' positions: Obwohl is a conjunction (verb-end), trotzdem is an adverb (verb-first).\n"
    "- Using 'als' for future/repeated events: Use 'wenn' for future and repeated events, 'als' only for single past events.\n"
    "- Forgetting that 'sondern' only follows a negation: sondern is used after 'nicht' to introduce a contrast, not after affirmative clauses."
)

original['description'] = description
original['tips'] = tips
original['totalQuestions'] = len(translated_qs)
original['questions'] = translated_qs

with open('app/src/main/assets/a2_10.json', 'w', encoding='utf-8') as f:
    json.dump(original, f, ensure_ascii=False, indent=2)

print("✅ a2_10.json updated successfully!")
print(f"   Questions: {len(translated_qs)}")
print(f"   Description: {description[:80]}...")
print(f"   Tips: {len(tips)} chars")