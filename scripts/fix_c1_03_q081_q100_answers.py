import json

with open('app/src/main/assets/c1_03.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Fix correctAnswers for q081-q100 to match exact option text
fixes = {
    "c1_03_q081": "Das Paket laesst sich leicht schicken.",
    "c1_03_q082": "Das Formular laesst sich ausfuellen.",
    "c1_03_q084": "Die Aufgabe ist zu erledigen.",
    "c1_03_q086": "Sowohl B als auch C sind korrekte Passiversatzformen.",
    "c1_03_q087": "Die Rechnung hat bis Freitag zu bezahlen.",
    "c1_03_q088": "Das Problem laesst sich nicht ignorieren.",
    "c1_03_q089": "Die neuen Vorschriften sind beachtbar.",
    "c1_03_q090": "'haben + zu + Infinitiv' hat ein persoenliches Subjekt (Person als Handlungstraeger); 'Sein + zu + Infinitiv' hat oft ein sachliches Subjekt.",
    "c1_03_q091": "laesst sich / reparieren",
    "c1_03_q092": "sich lassen + Infinitiv",
    "c1_03_q093": "Die Ergebnisse sind nicht anzuzweifeln.",
    "c1_03_q094": "-bar",
    "c1_03_q095": "Die Unterlagen sind bis Montag einzureichen.",
    "c1_03_q096": "Sie koennen immer durch 'sich lassen + Infinitiv' ersetzt werden.",
    "c1_03_q097": "Der Konflikt laesst sich durch Dialog loesen. / Der Konflikt ist durch Dialog zu loesen.",
    "c1_03_q098": "Der Mieter hat die Wohnung bis Ende des Monats zu raumen.",
    "c1_03_q099": "Die Klausel kann so nicht akzeptiert werden.",
    "c1_03_q100": "'Sein + zu + Infinitiv' - die Einwaende muessen beruecksichtigt werden",
}

for q in data['questions']:
    if q['id'] in fixes:
        old = q['correctAnswer']
        q['correctAnswer'] = fixes[q['id']]
        if q['correctAnswer'] not in q['options']:
            print(f"STILL BAD {q['id']}: '{q['correctAnswer']}' not in options")
        else:
            print(f"Fixed {q['id']}: '{old}' -> '{q['correctAnswer']}'")

# Also fix q093 option (was mangled)
data['questions'][92]['options'][2] = "Die Ergebnisse haben sich nicht anzuzweifeln."

with open('app/src/main/assets/c1_03.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Final verification
ok = True
for q in data['questions']:
    if q['correctAnswer'] not in q['options']:
        print(f"BAD {q['id']}: correctAnswer not in options")
        ok = False
    if len(q['options']) != 4:
        print(f"BAD {q['id']}: {len(q['options'])} options")
        ok = False
print(f"All OK: {ok}, Total questions: {len(data['questions'])}")
