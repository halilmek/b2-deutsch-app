#!/usr/bin/env python3
"""Fix c1_04.json: add missing ids to questions 61-100 (positions 60-99)."""

import json

path = 'app/src/main/assets/c1_04.json'

with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

fixed = 0
for i, q in enumerate(data['questions']):
    qnum = i + 1  # 1-indexed
    if not q.get('id'):
        q['id'] = f'c1_04_q{qnum:03d}'
        fixed += 1

data['totalQuestions'] = len(data['questions'])

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Fixed {fixed} missing ids in {path}")
print(f"Total questions: {data['totalQuestions']}")

# Verify
with open(path, 'r', encoding='utf-8') as f:
    verify = json.load(f)
missing = [q.get('id') for q in verify['questions'] if not q.get('id')]
print(f"Remaining missing ids: {len(missing)}")
print(f"First id: {verify['questions'][0]['id']}, Last id: {verify['questions'][-1]['id']}")
