# B2 Deutsch App — PROJECT STATUS

**Last Updated:** 2026-05-01
**GitHub:** https://github.com/halilmek/b2-deutsch-app
**Firebase:** b2-deutsch-app

---

## ✅ WHAT WE COMPLETED (2026-05-01)

### 20 New Questions for Topic 6 — Angaben im Satz (b2_07)
Huma provided 20 new MCQ questions about "Angaben im Satz" (adverbial phrases in sentences). Each question shows a German sentence and asks a question (Wann/Wo/Warum/Wie/Mit wem). Verified against answer key.

| Q# | Sentence | Question | Answer |
|----|---------|---------|--------|
| 1 | Ich habe gestern im Büro lange gearbeitet. | Wann habe ich gearbeitet? | **gestern** (B) |
| 2 | Er fährt wegen des schlechten Wetters nicht. | Warum fährt er nicht? | **wegen des schlechten Wetters** (A) |
| 3 | Sie wohnt seit zwei Jahren in Berlin. | Seit wann wohnt sie in Berlin? | **seit zwei Jahren** (B) |
| 4 | Wir gehen am Wochenende ins Kino. | Wann gehen wir ins Kino? | **am Wochenende** (B) |
| 5 | Er arbeitet im Büro sehr konzentriert. | Wo arbeitet er? | **im Büro** (A) |
| 6 | Ich bleibe wegen meiner Krankheit zu Hause. | Warum bleibe ich zu Hause? | **wegen meiner Krankheit** (B) |
| 7 | Sie fährt mit dem Bus zur Arbeit. | Wie fährt sie zur Arbeit? | **mit dem Bus** (B) |
| 8 | Er hat heute Morgen schnell gefrühstückt. | Wann hat er gefrühstückt? | **heute Morgen** (B) |
| 9 | Wir treffen uns im Park um 18 Uhr. | Wo treffen wir uns? | **im Park** (A) |
| 10 | Er hat aus Angst nichts gesagt. | Warum hat er nichts gesagt? | **aus Angst** (C) |
| 11 | Ich habe gestern wegen des Regens mit dem Auto gearbeitet. | Warum habe ich mit dem Auto gearbeitet? | **wegen des Regens** (B) |
| 12 | Sie lernt jeden Tag zu Hause fleißig. | Wo lernt sie? | **zu Hause** (C) |
| 13 | Er ist wegen eines Termins früh gegangen. | Warum ist er gegangen? | **wegen eines Termins** (B) |
| 14 | Wir haben gestern im Restaurant gut gegessen. | Wie haben wir gegessen? | **gut** (A) |
| 15 | Sie bleibt heute wegen der Prüfung zu Hause. | Wann bleibt sie zu Hause? | **heute** (B) |
| 16 | Er hat im Büro mit seinem Chef gesprochen. | Mit wem hat er gesprochen? | **mit seinem Chef** (B) |
| 17 | Ich gehe morgen wegen eines Meetings ins Büro. | Wann gehe ich ins Büro? | **morgen** (A) |
| 18 | Sie hat im Urlaub in Spanien entspannt. | Wo hat sie entspannt? | **in Spanien** (B) |
| 19 | Er arbeitet aus finanziellen Gründen am Wochenende. | Warum arbeitet er am Wochenende? | **aus finanziellen Gründen** (B) |
| 20 | Wir fahren mit dem Zug nach Berlin. | Wie fahren wir nach Berlin? | **mit dem Zug** (B) |

**b2_07 → v1.1 | 120 questions total → quizCount: 12**
**Pushed to GitHub:** `6513152d2c5528a2fd4cbbf3532325dfae90c232`

### Fix Rotation Restart + Fill Blank UI (QuizActiveFragment)
Two bugs fixed in one commit:

1. **Rotation restart bug:** Fragment was calling `viewModel.startQuiz()` unconditionally in `onViewCreated()`. Every rotation recreated the ViewModel and restarted the quiz. Fixed by checking `if (viewModel.currentQuiz.value == null)` before starting a new quiz — if a quiz is already in progress, it resumes it instead of restarting.

2. **Fill-in-blank UI:** Added proper `EditText` input fields for `fill_blank` type questions. Supports 1-blank and 2-blank questions with separate input fields. Answers are combined with a space ("word1 word2") before storing. State is restored on rotation.

**Pushed to GitHub:** `c55f1942d5faa3018a0226e9518846b1cb4dcdc7`

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
| 5 | b2_07 | Angaben im Satz | 120 | 12 | ✅ **120 Q (20 new from Huma + 100 existing)** |
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

_Last updated: 2026-05-01 10:40 UTC_
