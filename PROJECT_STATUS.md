# B2 Deutsch App — PROJECT STATUS

**Last Updated:** 2026-05-01
**GitHub:** https://github.com/halilmek/b2-deutsch-app
**Firebase:** b2-deutsch-app

---

## ✅ WHAT WE COMPLETED (2026-05-01)

### 7 Errors Fixed in Topic 5 — Futur mit werden (b2_06)
While reviewing the full question set, I found and fixed 7 errors:

| Q# | Error | Fix |
|----|-------|-----|
| q029 | Used "wurde" (Präteritum — past tense) in a Futur chapter | → "wird" (Futur I) |
| q071 | Answer "fährt ab" used Präsens instead of Futur mit werden | → "wird abfahren" |
| q073 | Answer "findet statt" used Präsens instead of Futur mit werden | → "wird stattfinden" |
| q074 | Answer "fängt an" used Präsens instead of Futur mit werden | → "wird anfangen" |
| q076 | Futur II missing Partizip II: "werde haben" | → "werde gehabt haben" |
| q088 | Futur II missing auxiliary: "wird bekommen" | → "wird bekommen haben" |
| q089 | Answer "fängt an" used Präsens instead of Futur mit werden | → "wird anfangen" |

**b2_06 → v1.3 | Pushed to GitHub:** `a02eb02d7ab7024a0d8bfad9ff74096114edcc67`

### 25 New Questions Added to Topic 5 — Futur mit werden
Huma provided 25 additional MCQ questions for b2_06. All verified against answer key. Added to b2_06.json as q101–q125.

| Q# | Topic | Grammar Point | Answer |
|----|-------|--------------|--------|
| 1–16 | Futur I werden conjugation | ich→werde, du→wirst, er→wird, wir→werden, ihr→werdet, Sie→werden | (various) |
| 17–20 | Futur I in Nebensatz | Verb am Ende: "bestehen wird", "lösen werden" | (various) |
| 21–23 | Futur II double-gap | "werde ... abgeschlossen haben", "wird ... verändert haben" | (various) |
| 24 | Meta — Futur I conjugation | "Morgen _____ ich früh aufstehen." → werde | A |
| 25 | Nebensatz word order | "Ich glaube, dass _____." → "sie kommen wird" | B |

**b2_06 total: 125 questions → quizCount: 13**
**Pushed to GitHub:** `549e1078010161aabfba0d4643471e7714233788`

### Topic Numbering Fixed
- SubjectListViewModel.kt: b2_06 order=5, b2_07 order=6
- Pushed: `c8aad35bfd05f0b21dbd8b0cb8a1cf6c4a723eaf`

---

## 📋 TOPIC CONTENT SUMMARY

| # | subjectId | Topic Name | Questions | QuizCount | Content Quality |
|---|----------|-----------|-----------|-----------|----------------|
| 1 | b2_01 | Konnektoren & Verben | 96+50 | ~15 | ✅ Complete |
| 2 | b2_04 | Zeitformen der Vergangenheit | 160 | 16 | ✅ Complete |
| 3 | b2_05 | Zeitformen der Zukunft | 120 | 12 | ✅ Complete |
| **4** | **b2_06** | **Futur mit werden** | **125** | **13** | ✅ **125 Q, v1.3 (7 errors fixed)** |
| 5 | b2_07 | Angaben im Satz | 100 | 10 | ⏳ Pending |
| 6 | b2_08 | Verneinung mit nicht | 100 | 10 | ⏳ Pending |
| 7 | b2_09 | Negationswörter | 100 | 10 | ⏳ Pending |
| 8 | b2_10 | Passiv Präteritum | 100 | 10 | ⏳ Pending |
| 9 | b2_11 | Konjunktiv II der Vergangenheit | 100 | 10 | ⏳ Pending |
| 10 | b2_12 | Konjunktiv II mit Modalverben | 100 | 10 | ⏳ Pending |
| 11 | b2_13 | Pronomen: einander | 100 | 10 | ⏳ Pending |
| 12 | b2_14 | Weiterführende Nebensätze | 100 | 10 | ⏳ Pending |
| 13 | b2_15 | Präpositionen mit Genitiv | 100 | 10 | ⏳ Pending |
| 14 | b2_16 | je und desto/umso | 100 | 10 | ⏳ Pending |
| 15 | b2_17 | Nomen-Verb-Verbindungen | 100 | 10 | ⏳ Pending |
| 16 | b2_18 | Folgen ausdrücken | 100 | 10 | ⏳ Pending |
| 17 | b2_19 | Ausdrücke mit Präpositionen | 100 | 10 | ⏳ Pending |
| 18 | b2_20 | Irreale Konditionalsätze | 100 | 10 | ⏳ Pending |
| 19 | b2_21 | Relativsätze im Genitiv | 100 | 10 | ⏳ Pending |
| 20 | b2_22 | Konjunktiv I in der indirekten Rede | 100 | 10 | ⏳ Pending |
| 21 | b2_23 | Konjunktiv II in irrealen Vergleichssätzen | 100 | 10 | ⏳ Pending |
| 22 | — | (Reserve) | — | — | ⏳ Pending |

---

## 🚀 HOW TO PUSH NEW QUESTIONS

```bash
cd /Users/halilozturk/b2-deutsch-app

# Push Topic 5 (b2_06) to GitHub + Firestore
node scripts/import_and_sync.js b2_06

# Push multiple topics
node scripts/import_and_sync.js b2_06 b2_07

# Push ALL topics
node scripts/import_and_sync.js
```

---

## 📋 REMAINING WORK

### Must Do
- [ ] Firestore push for b2_06: run `node scripts/import_and_sync.js b2_06`
- [ ] b2_07–b2_22 have placeholder content (need real grammar questions)

### Should Do
- [ ] Test FirebaseSyncService end-to-end with new content
- [ ] Add pull-to-refresh for manual sync trigger

### Future
- [ ] AI Speaking Partner integration
- [ ] AI Writing Evaluation
- [ ] Peer Speaking Exams

---

## 🔧 SESSION LOG

### 2026-05-01 (Second Session) — 25 New Questions for Futur mit werden

Huma provided 25 MCQ questions for topic 5 (Futur mit werden) via chat.
All verified correct against the answer key provided. Added to b2_06.json as q101–q125.

**Questions breakdown:**
- Q1–16 (16 Q): Futur I werden conjugation — ich→werde, du→wirst, er/sie/es→wird, wir→werden, ihr→werdet, Sie→werden
- Q17–20 (4 Q): Futur I in Nebensatz — verb at end: "bestehen wird", "lösen werden", "studieren wird", "schneien wird"
- Q21–23 (3 Q): Futur II double-gap: "werde ... abgeschlossen haben", "wird ... verändert haben", "wird ... gewesen sein"
- Q24 (1 Q): Meta: "Morgen _____ ich früh aufstehen." → wird conjugation
- Q25 (1 Q): Nebensatz word order: "Ich glaube, dass _____." → "sie kommen wird"

**Result:** b2_06 now has **125 questions → quizCount: 13**
**GitHub:** `549e1078010161aabfba0d4643471e7714233788`

### 2026-05-01 (First Session) — Topic Numbering Fix

SubjectListViewModel.kt had wrong `order` values for b2_06 and b2_07:
- b2_06: order was 4 → fixed to **5**
- b2_07: order was 5 → fixed to **6**

**GitHub:** `c8aad35bfd05f0b21dbd8b0cb8a1cf6c4a723eaf`

### 2026-04-29 — Dynamic quizCount + Futur mit werden Generated

- SubjectListFragment.kt computes `quizCount = (totalQuestions + 9) / 10` at runtime
- b2_06.json (Futur mit werden): 100 Q generated (30 MCQ + 30 T/F + 40 Fill)
- b2_05.json: 120 Q (unchanged)

### 2026-04-28 — Topics 1+2 Merged

Topics 1 and 2 merged into b2_01 (Konnektoren + Verben und Ergänzungen).
Module now has 22 topics (was 23).

---

_Last updated: 2026-05-01 10:15 UTC_
