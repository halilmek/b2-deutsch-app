# -*- coding: utf-8 -*-
"""
Creates 0-question placeholder metadata for the 9 approved C2 curriculum
topics (c2_13-c2_21) that don't have questions yet. These show up in the
app as dimmed "Wird vorbereitet" cards (Subject.isComingSoon derives this
purely from questionCount == 0 - see SubjectAdapter.kt/SubjectListFragment.kt).

Deliberately NOT generating any questions here - that's a separate task
pending explicit go-ahead. questions: [] / totalQuestions: 0 by design.

Writes to both content/grammar/ (git source of truth) and
app/src/main/assets/ (APK-bundled offline fallback), matching the existing
per-topic file convention.
"""
import json
import os

PLACEHOLDERS = [
    {
        "id": "c2_13",
        "name": "Erweiterte Partizipialkonstruktionen",
        "description": "Mehrstufige Partizipialattribute zur Verdichtung von Relativsätzen (z. B. \"der von den Wissenschaftlern lange erwartete Durchbruch\") — ein klassisches C2-Prüfungsthema."
    },
    {
        "id": "c2_14",
        "name": "Stilebenen & Registerwechsel",
        "description": "Bewusstes Erkennen und Produzieren von Registerunterschieden zwischen umgangssprachlich, neutral, formell und Amtsdeutsch."
    },
    {
        "id": "c2_15",
        "name": "Textkohäsion: Ellipsen, Pro-Formen & Sprachökonomie",
        "description": "Auslassungen und Verweismittel, die formelle/journalistische Texte kompakt halten (z. B. \"Er kam, sah und siegte\")."
    },
    {
        "id": "c2_16",
        "name": "Ironie, rhetorische Mittel & Sprachbilder",
        "description": "Metapher, Understatement, rhetorische Fragen — häufig in literarischen und journalistischen C2-Lesetexten."
    },
    {
        "id": "c2_17",
        "name": "Erweiterte Vergleichs- und Gradationsstrukturen",
        "description": "Gehobene Vergleichskonstruktionen jenseits von je…desto wie \"nicht zuletzt aufgrund\", \"umso mehr als\"."
    },
    {
        "id": "c2_18",
        "name": "Erweiterte Genitivkonstruktionen & Attributstapelung",
        "description": "Mehrfache Genitivattribute und komplexe NP-interne Attribution in formellen Texten."
    },
    {
        "id": "c2_19",
        "name": "Anglizismen & Sprachwandel im Deutschen",
        "description": "Erkennen und angemessener Umgang mit Anglizismen, Sprachpurismus-Debatte."
    },
    {
        "id": "c2_20",
        "name": "Textsortenspezifische Stilmittel: Kommentar & Rezension",
        "description": "Grammatische/stilistische Konventionen von Meinungstexten (wertende Adjektive, Abschwächungsformeln, argumentativ-konzessive Kombinationen)."
    },
    {
        "id": "c2_21",
        "name": "Idiomatik & feste Wendungen im gehobenen Kontext",
        "description": "Kollokationen und idiomatische Wendungen im akademischen/journalistischen Deutsch."
    }
]

for p in PLACEHOLDERS:
    data = {
        "subjectId": p["id"],
        "topicName": p["name"],
        "level": "C2",
        "description": p["description"],
        "tips": [],
        "questions": [],
        "totalQuestions": 0
    }
    for base in ["content/grammar", "app/src/main/assets"]:
        os.makedirs(base, exist_ok=True)
        path = f'{base}/{p["id"]}.json'
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Wrote {path}")

print(f"\nTotal placeholder topics created: {len(PLACEHOLDERS)}")
