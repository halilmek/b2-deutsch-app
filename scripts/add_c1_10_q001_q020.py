#!/usr/bin/env python3
"""Add c1_10 (Textkohäsion & Diskursmarker) — 20 questions."""

import json, os

path = "app/src/main/assets/c1_10.json"
data = json.load(open(path, "r", encoding="utf-8"))

print(f"c1_10 has {data['totalQuestions']} questions in {path}")
print(f"Split: easy={sum(1 for q in data['questions'] if q['difficulty']=='easy')}, "
      f"medium={sum(1 for q in data['questions'] if q['difficulty']=='medium')}, "
      f"hard={sum(1 for q in data['questions'] if q['difficulty']=='hard')}")