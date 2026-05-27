import json

with open('app/src/main/assets/c1_03.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

data['description'] = (
    "Passiversatzformen — At C1 level, relying solely on Vorgangspassiv (werden + Partizip II) makes your text sound repetitive. "
    "Passiversatzformen are semantically passive (subject undergoes the action) but use active verbs, adjectives, or fixed expressions. "
    "The three core structures are: (1) 'sein + zu + Infinitiv' — replaces können (possibility) or müssen (necessity); "
    "(2) 'sich lassen + Infinitiv' — replaces können exclusively (possibility); "
    "(3) adjectives in -bar/-lich — turn action into capability adjective (e.g., 'ist lesbar' = kann gelesen werden). "
    "Advanced C1 forms: Das Gerundiv ('die noch zu prüfenden Dokumente') as adjectives before nouns with passive necessity meaning; "
    "Passiv-Funktionsverbgefüge (noun-verb combinations like 'steht zur Diskussion', 'findet Anwendung', 'stößt auf Kritik') replacing passive verbs in formal/official German. "
    "Key trap: 'Das Auto ist zu reparieren' = passive (car needs fixing); 'Ich habe das Auto zu reparieren' = active (I must fix the car). "
    "Exam tip: Mix forms across paragraphs to demonstrate full syntactic control."
)

data['tips'] = [
    "'sein + zu + Infinitiv' is the ultimate C1 structure: 'Die Ergebnisse sind einzusehen' = können (possibility) or 'Die Regeln sind zu beachten' = müssen (necessity). Always use the INFINITIVE, not the past participle.",
    "'sich lassen + Infinitiv' ONLY replaces können (possibility): 'Das Problem lässt sich lösen' = 'Das Problem kann gelöst werden'. NEVER use it for müssen. Use the infinitive, not the past participle.",
    "Trap to avoid: 'Das Auto ist zu reparieren' = PASSIVE meaning (the car is to be fixed). 'Ich habe das Auto zu reparieren' = ACTIVE meaning (I have to fix the car). 'haben + zu' = personal obligation; 'sein + zu' = passive necessity.",
    "Adjectives in -bar/-lich express capability: 'lesbar' (can be read), 'vermeidbar' (can be avoided), 'unverzeihlich' (cannot be forgiven). These are one-word passive substitutes used as predicate adjectives.",
    "Das Gerundiv (zu + Partizip I as adjective attribute): 'die noch zu prüfenden Dokumente' (the documents still to be examined). It means MUST/SOLL and replaces 'die Dokumente, die noch geprüft werden müssen'. Decline properly: zu prüfenden, zu lösende, zu beachtenden.",
    "Passiv-Funktionsverbgefüge: formal noun-verb replacements — 'steht zur Diskussion' (= wird diskutiert), 'zur Anwendung kommen' (= wird angewendet), 'stößt auf Kritik' (= wird kritisiert), 'findet eine Lösung' (= wird gelöst).",
    "Quick selection for writing: KÖNNEN → 'lässt sich machen' or 'ist machbar/ist zu machen'. MÜSSEN → 'muss gemacht werden' or 'ist zu machen'. Mix forms across paragraphs for C1 variety."
]

with open('app/src/main/assets/c1_03.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated c1_03 description and tips")
print("Description:", data['description'][:80], "...")
print("Tips:", len(data['tips']))
