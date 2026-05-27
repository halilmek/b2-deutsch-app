import json

with open('app/src/main/assets/c1_02.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

data['description'] = (
    "Indirekte Rede & Konjunktiv I — Konjunktiv I is the standard tool for objective reporting in German. "
    "By using Konjunktiv I, the speaker signals neutrality: 'I am reporting what someone said, without confirming or denying it.' "
    "The core challenge: many Konjunktiv I forms are identical to Indikativ (especially ich/wir/sie plural), so they must be replaced by Konjunktiv II or würde + infinitive. "
    "Only er/sie/es 3rd-person-singular forms are reliably unique and used directly. "
    "Past tense in indirect speech always uses Konjunktiv I of haben/sein + Partizip II (e.g., er habe, sie hätten). "
    "Future tense uses würde/werde + infinitive. "
    "Commands are paraphrased with sollen in Konjunktiv I (e.g., 'Er riet ihm, er solle nicht mehr rauchen'). "
    "The verb 'sein' is unique in ALL persons (ich sei, er sei, wir seien) and never needs replacement. "
    "At C1 level, dropping 'dass' and using main-clause word order in the subordinate is the mark of advanced academic style."
)

data['tips'] = [
    "Golden Rule of Substitution: Konjunktiv I identical to Indikativ → replace with Konjunktiv II or würde + infinitive. "
    "Safe zone: er/sie/es 3rd-person-singular always looks unique (er habe, er gehe, er wisse). "
    "Identical-to-Indikativ persons: ich (habe), wir (haben), sie/Sie plural (haben) → use Konjunktiv II.",
    "Past tense (Vergangenheit) — all past tenses collapse to: Konjunktiv I of haben/sein (habe/sei) + Partizip II. "
    "Example: 'Er sagte, er habe das gesehen.' (Perfekt) / 'Sie sagten, sie wären nach Hause gegangen.' (Konjunktiv II because plural haben = Indikativ).",
    "Future tense (Zukunft): würde/werde + Infinitive. Plural 'werden' = Indikativ, so: 'sie würden sagen' (not 'sie werden sagen').",
    "Commands: use sollen in Konjunktiv I (er solle, sie sollten) — NOT the imperative verb in Konjunktiv I directly.",
    "The verb 'sein': ich sei, du seist, er sei, wir seien, ihr seiet, sie seien — ALWAYS unique, NEVER replace with Konjunktiv II.",
    "Without 'dass' (academic elegance): main-clause word order in the subordinate. "
    "C1 Style: 'Der Kanzler erklärte, die Reformen seien alternativlos.' (verb-second, kein dass).",
    "Konjunktiv II signals doubt if used when Konjunktiv I would have been possible: 'Er sagte, er hätte Zeit' (subtle doubt vs neutral 'er habe Zeit').",
    "Passive in indirect speech: Konjunktiv I of werden + Partizip II: 'Das Projekt werde abgeschlossen' (present passive). "
    "Passive past:sei + Partizip II + worden: 'Das Projekt sei abgeschlossen worden'."
]

with open('app/src/main/assets/c1_02.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated description and tips")
print("Description:", data['description'][:80], "...")
print("Tips count:", len(data['tips']))
