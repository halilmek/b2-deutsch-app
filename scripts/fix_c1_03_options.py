import json

with open('app/src/main/assets/c1_03.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Fix questions with only 3 options
fixes = {
    26: ["zu beachten", "beachtet werden", "beachten", "zu beachtet"],
    30: ["zu warten", "gewartet werden", "warten", "zu gewartet"],
    32: ["zu lagern", "gelagert werden", "lagern", "zu gelagert"],
    34: ["zu behandeln", "behandelt werden", "behandeln", "zu behandelt"],
    36: ["zu bezahlen", "bezahlt werden", "bezahlen", "zu bezahlt"],
    38: ["zu analysieren", "analysiert werden", "analysieren", "zu analysiert"],
    40: ["auszufuellen", "ausgefuellt werden", "ausfuellen", "zu ausgefuellt"],
}

for idx_str, options in fixes.items():
    q = data['questions'][idx_str - 1]
    q['options'] = options

with open('app/src/main/assets/c1_03.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Verify
for i, q in enumerate(data['questions'], start=1):
    if len(q['options']) != 4:
        print(f"Q{i}: only {len(q['options'])} options")
print("All verified OK:", all(len(q['options']) == 4 for q in data['questions']))
print(f"Total: {len(data['questions'])} questions")
