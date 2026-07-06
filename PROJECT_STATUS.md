# B2 Deutsch App — PROJECT STATUS

**Last Updated: 2026-07-06 (verified against live Firestore + local assets by Claude Code)**
**GitHub:** https://github.com/halilmek/b2-deutsch-app
**Firebase:** b2-deutsch-app
**Local App Path (Halil's machine):** `/Users/halilozturk/b2-deutsch-app`
**Firebase Credentials:** `/Users/halilozturk/Documents/b2-deutsch-app-firebase-adminsdk-fbsvc-4aa25c0ca2.json`

---

## 📋 OVERALL PROGRESS SUMMARY

**Two numbers matter here and they legitimately differ — see "Firestore Reality Check" below.**
`Local` = topics/questions bundled as JSON in `app/src/main/assets/` (what ships in the APK).
`Firestore` = topics live in the `grammarQuizBank` collection, read via `FirebaseDataSource.getGrammarQuestionsBySubject` for quiz questions. **Correction from last session:** the *subject/topic list itself* (`getSubjectsByLevel`) is hardcoded in `FirebaseDataSource.kt` to always `Result.failure(...)` — it is not "used when Firestore succeeds, falls back otherwise," it **never** queries Firestore. The hardcoded per-level lists in `SubjectListViewModel.kt` are the only path, always. See Open Item on `SubjectListViewModel` below (Step 4 in progress).

| Module | Local Topics | Local Questions | Firestore Topics | Firestore Questions | Target |
|--------|-------------|-----------------|-------------------|----------------------|--------|
| A1 | 10 | 600 | 15 | 1,500 | 1,000 |
| A2 | 10 | 1,210 | 15 | 1,500 | ~1,000 |
| B1 | 10 | 1,001 | 15 | 1,500 | 1,000 |
| B2 | 24 | 2,321 | 23 | 2,260 | ~2,000 |
| C1 | 10 | 1,028 | 15 | 1,500 | 2,000 |
| **C2** | **12** | **1,240** | **0** | **0** | **~2,000** |
| **Total (local)** | **76** | **7,400** | | | **~8,000** |

**Resolved (previously flagged as open, verified 2026-07-06):**
- A1 "600 vs 1,000" discrepancy: not a bug — 10 local topics × 60 questions = 600 is simply what exists in the repo; the "1,000" was a stale target number, not an actual count.
- A2/B1 Firestore sync: **done, and then some** — Firestore's `grammarQuizBank` has 15 topics × 100 q each for A1/A2/B1/C1 (topics `_11` through `_15`), i.e. more than what's in this git repo.

**✅ RESOLVED 2026-07-06 (Step 1 of data-integrity fix): Firestore content backed up into git.** `scripts/export_firestore_content.js` exported every non-user Firestore collection into `content/`. Verified counts exactly matched expectations:

| Level | Topics | Questions | Missing locally (no `app/src/main/assets` file) |
|-------|--------|-----------|--------------------------------------------------|
| A1 | 15 | 1,500 | a1_11–a1_15 |
| A2 | 15 | 1,500 | a2_11–a2_15 |
| B1 | 15 | 1,500 | b1_11–b1_15 |
| B2 | 21 | 2,260 | (none) |
| C1 | 15 | 1,500 | c1_11–c1_15 |

Output: `content/grammar/<subjectId>.json` (81 files, reshaped to match the asset-file schema — array `options`, `topicName` from the `topics` collection where available). These imported files have empty `description`/`tips`/`explanation` (not stored in Firestore) and are marked `_importedFromFirestore: true, _needsContentReview: true` — **they are a safety-net backup, not reviewed content, and should not silently replace an asset file.** Also backed up as raw dumps: `content/firestore_backup/{levels,moduleQuizQuestions,readings,themes,topics}.json` (`quizBank`/`lessons`/`quizzes`/`vocabulary`/`readingPassages`/`listeningExercises` collections don't currently exist in Firestore — nothing to back up there). User-data collections (`users`, `userProgress`, `writingSubmissions`, `speakingSessions`) were deliberately excluded — this is a content backup, not a PII export.

**🚨 NEW FINDING while validating the backup — broken content already live in production:** 96 multiple-choice questions (+45 fill_blank) in `grammarQuizBank` have a `correctAnswer` that is not among their own `options` — e.g. `a2_01_q018`: options `["gut","besser","am besten","gute"]`, correctAnswer `"beste"` (not offered). Verified against the raw Firestore doc directly, not an export-script artifact. Pattern is systematic, not random: **A1 clean (0)**, **A2/B1/B2: exactly 1 broken question per topic**, **C1: exactly 3 per topic** — the identical question/options text repeating verbatim across unrelated topics suggests a template/placeholder got seeded into a fixed slot when `grammarQuizBank` was originally populated, not scattered human content errors. Real users hitting these questions cannot answer correctly no matter what they pick. **Not fixed — logged as Open Item, decided by user to handle as a separate future task, not blocking steps 2–5.**

---

## 📋 A1 MODULE ✅

| # | subjectId | Topic Name | Questions | Status |
|---|----------|-----------|-----------|--------|
| 1 | a1_01 | Nomen und Artikel | 60 | ⚠️ Check |
| 2 | a1_02 | Veraenderungen der Nomen | 60 | ⚠️ Check |
| 3 | a1_03 | Personalpronomen | 60 | ⚠️ Check |
| 4 | a1_04 | Akkusativ (Wen-Fall) | 60 | ⚠️ Check |
| 5 | a1_05 | Dativ (Wem-Fall) | 60 | ⚠️ Check |
| 6 | a1_06 | Praepositionen | 60 | ⚠️ Check |
| 7 | a1_07 | Verben mit Praepositionen | 60 | ⚠️ Check |
| 8 | a1_08 | Perfekt (haben/sein + Partizip II) | 60 | ⚠️ Check |
| 9 | a1_09 | Modalverben | 60 | ⚠️ Check |
| 10 | a1_10 | Saetze bilden / Wortstellung | 60 | ⚠️ Check |

**A1 Total: 600 questions** (discrepancy: files show 600, status reported 1,000)

---

## 📋 A2 MODULE ✅

| # | subjectId | Topic Name | Questions | Status |
|---|----------|-----------|-----------|--------|
| 1 | a2_01 | Präteritum | 110 | ✅ Complete |
| 2 | a2_02 | Perfekt | 100 | ✅ Complete |
| 3 | a2_03 | Verben mit Präpositionen | 100 | ✅ Complete |
| 4 | a2_04 | Wechselpräpositionen | 100 | ✅ Complete |
| 5 | a2_05 | Nebensätze | 120 | ✅ Complete |
| 6 | a2_06 | Reflexive Verben | 120 | ✅ Complete |
| 7 | a2_07 | Imperativ | 120 | ✅ Complete |
| 8 | a2_08 | Plusquamperfekt | 160 | ✅ Complete |
| 9 | a2_09 | Relativsätze | 160 | ✅ Complete |
| 10 | a2_10 | Konjunktionen | 120 | ✅ Complete |

**A2 Total: 1,210 questions**

---

## 📋 B1 MODULE ✅

| # | subjectId | Topic Name | Questions | Status |
|---|----------|-----------|-----------|--------|
| 1 | b1_01 | Nebensätze | 100 | ✅ Complete |
| 2 | b1_02 | Konjunktiv II | 100 | ✅ Complete |
| 3 | b1_03 | Passiv | 101 | ✅ Complete |
| 4 | b1_04 | Modalverben im Konjunktiv II | 100 | ✅ Complete |
| 5 | b1_05 | Nominalisierung | 100 | ✅ Complete |
| 6 | b1_06 | Relativsätze im Genitiv | 100 | ✅ Complete |
| 7 | b1_07 | Konnektoren | 100 | ✅ Complete |
| 8 | b1_08 | Perfekt und Präteritum | 100 | ✅ Complete |
| 9 | b1_09 | Verben mit festen Präpositionen | 100 | ✅ Complete |
| 10 | b1_10 | Partizipien als Adjektive | 100 | ✅ Complete |

**B1 Total: 1,001 questions (target: 1,000) 🎉**

---

## 📋 B2 MODULE ✅

| # | subjectId | Topic Name | Questions | Status |
|---|----------|-----------|-----------|--------|
| 1 | b2_01 | Konnektoren | 96 | ✅ Complete |
| 2 | b2_02 | Verben und Ergaenzungen | 50 | ✅ Complete |
| 3 | b2_03 | Verben und Ergaenzungen | 50 | ✅ Complete |
| 4 | b2_04 | Zeitformen in der Vergangenheit | 160 | ✅ Complete |
| 5 | b2_05 | Zeitformen der Zukunft | 120 | ✅ Complete |
| 6 | b2_06 | Futur mit werden | 125 | ✅ Complete |
| 7 | b2_07 | Angaben im Satz | 100 | ✅ Complete |
| 8 | b2_08 | Verneinung mit nicht | 100 | ✅ Complete |
| 9 | b2_09 | Negationswoerter | 100 | ✅ Complete |
| 10 | b2_10 | Passiv Präteritum | 100 | ✅ Complete |
| 11 | b2_11 | Konjunktiv II der Vergangenheit | 100 | ✅ Complete |
| 12 | b2_12 | Konjunktiv II mit Modalverben | 120 | ✅ Complete |
| 13 | b2_13 | Pronomen: einander | 100 | ✅ Complete |
| 14 | b2_14 | Weiterfuehrende Nebensaetze | 100 | ✅ Complete |
| 15 | b2_15 | Praepositionen mit Genitiv | 100 | ✅ Complete |
| 16 | b2_16 | je und desto/umso + Komparativ | 100 | ✅ Complete |
| 17 | b2_17 | Nomen-Verb-Verbindungen | 100 | ✅ Complete |
| 18 | b2_18 | — | 100 | ✅ Complete |
| 19 | b2_19 | — | 100 | ✅ Complete |
| 20 | b2_20 | — | 100 | ✅ Complete |
| 21 | b2_21 | — | 100 | ✅ Complete |
| 22 | b2_22 | — | 100 | ✅ Complete |
| 23 | b2_23 | — | 100 | ✅ Complete |

**B2 Total: 2,321 questions**

---

## 📋 C1 MODULE 🔄 (In Progress)

| # | ID | Topic | Questions | Status |
|---|----|-------|-----------|--------|
| 1 | c1_01 | Nominalstil & Verbalstil | 127 | 🔄 In Progress |
| 2 | c1_02 | Indirekte Rede & Konjunktiv I | 100 | ✅ Complete |
| 3 | c1_03 | Passiversatzformen | 100 | ✅ Complete |
| 4 | c1_04 | Funktionsverbgefaeche | 100 | ✅ Complete |
| 5 | c1_05 | Partizipialattribute & Relativsatzformen | 100 | ✅ Complete |
| 6 | c1_06 | Modalverben im C1-Kontext | 100 | ✅ Complete |
| 7 | c1_07 | Wortbildung: Komposita & Derivation | 100 | ✅ Complete |
| 8 | c1_08 | Konnektoren & Satzverknuepfung (C1) | 100 | ✅ Complete |
| 9 | c1_09 | Infinitiv- & Nebensatzkonstruktionen (C1) | 100 | ✅ Complete |
| 10 | c1_10 | Textkohaesion & Diskursmarker (C1) | 101 | ✅ Complete |

**C1 Total: 1,048 questions (target: 2,000)**

---

## 📋 C2 MODULE 🔄 (In Progress)

| # | ID | Topic | Questions | Status |
|---|----|-------|-----------|--------|
| 1 | c2_01 | Nominalstil & Verbalstil | 100 | ✅ Complete |
| 2 | c2_02 | Erweiterte Konzessivstrukturen | 120 | ✅ Complete |
| 3 | c2_03 | Konjunktiv I | 180 | ✅ Complete (extended from 100) |
| 4 | c2_04 | Komplexe Satzgefüge (3+ Ebenen) | 100 | ✅ Complete |
| 5 | c2_05 | Passiversatzformen & Funktionale Verbkonstruktionen | 100 | ✅ Complete |
| 6 | c2_06 | Funktionsverbgefuge | 100 | ✅ Complete (extended from 80) |
| 7 | c2_07 | Erweiterte Konditionalstrukturen | 120 | ✅ Extended |
| 8 | c2_08 | Finale/Modale Nebensatzkonstruktionen | 100 | ✅ Complete |
| 9 | c2_09 | Wissenschaftliche Diskursmarker | 100 | ✅ Complete |
| 10 | c2_10 | Argumentationsstrategien | 100 | ✅ Complete |
| 11 | c2_11 | Nominalkomposita & Fachterminologie | 100 | ✅ Complete (was missing from app's C2 subject list — fixed 2026-07-06) |
| 12 | c2_12 | Modalpartikeln im gehobenen Sprachgebrauch | 20 | 🔄 In Progress (initial batch; extend to 100 in next session) |

**C2 Total: 1,240 questions (target: ~2,000). Not yet synced to Firestore at all (0 docs in `grammarQuizBank` for c2_*) — currently served entirely via bundled local assets + the hardcoded fallback subject list, same as it's always been for C2.**

---

## 📋 FIREBASE SYNC STATUS

**Live app reads grammar questions from the `grammarQuizBank` Firestore collection** (`FirebaseDataSource.getGrammarQuestionsBySubject`), with `Question` docs shaped as `{ id, subjectId, level, questionText, options: "opt1|opt2|opt3|opt4" (pipe-delimited STRING, not array), correctAnswer, difficulty, type }` — notably **no `explanation` field**.

**⚠️ `scripts/import_and_sync.js` writes to the WRONG collection.** It pushes to `moduleQuizQuestions`, which nothing in the app reads. Running it does not actually update what users see via Firestore — it only updates the GitHub-hosted asset file (and only for topics that already exist on GitHub; it can't create brand-new topic files, since it fetches a SHA first). Treat any "synced via import_and_sync.js" claim as GitHub-only, not Firestore-verified, until this script is fixed to target `grammarQuizBank` with the correct doc shape.

**⚠️ Likely silent bug:** because `grammarQuizBank` docs have no `explanation` field, any level whose Firestore fetch succeeds (currently A1/A2/B1/B2/C1 — anything except C2) probably shows blank/missing answer explanations in the quiz results screen (SUBJ-007 / READ-007 in PRODUCT_BACKLOG.md claim this is ✅ Done). C2 is unaffected only because Firestore has zero C2 topics, so it always falls back to the local JSON (which does have `explanation`). Worth a dedicated investigation session — not fixed here, out of scope for the C2 content task.

**🚨🚨 CRITICAL — 2026-07-06, Step 2 work: `grammarQuizBank` B2 content is systemically contaminated with a duplicated placeholder question.** While dry-running the fixed sync script (`node scripts/import_and_sync.js --dry-run`), 21 of 23 B2 topics (`b2_03` through `b2_23`) were found to share the **exact same question as `q001`**: `"___ ich in Deutschland ankam, konnte ich kein Deutsch."` (a temporal-clause/Konnektoren question). `b2_07`, `b2_08`, and `b2_09` additionally share the identical `q002` too. This means real B2 users hitting Firestore today are very likely seeing this same off-topic question repeated across most B2 quizzes, regardless of what the quiz claims to be about (e.g. `b2_09` is supposed to be "Negationswörter" but its `q001`/`q002` are about temporal clauses, not negation). Verified directly against raw Firestore docs, not a script artifact.

This is a different, larger-scope problem than the "no `explanation` field" or "96 broken `correctAnswer`" findings above — it looks like whatever process originally populated `grammarQuizBank` for B2 seeded a shared template block across nearly every topic. **B2 remains completely untouched in Firestore** — the real sync (see below) was deliberately run for A1/A2/B1/C1/C2 only. B2 needs a human decision on remediation strategy before any write happens there (e.g. per-topic: does local `content/grammar/b2_XX.json` win outright, does Firestore need a targeted cleanup pass, or something else).

**✅ 2026-07-06: real sync executed for A1/A2/B1/C1/C2 (user-approved, B2 excluded).** Ran `node scripts/import_and_sync.js` (no `--dry-run`) for all 71 non-B2 topics. Verified directly against Firestore afterward:

| Level | Firestore Topics | Firestore Questions (before → after) |
|-------|------------------|----------------------------------------|
| A1 | 15 | 1,500 → 1,500 (unchanged, already matched) |
| A2 | 15 | 1,500 → 1,710 |
| B1 | 15 | 1,500 → 1,521 |
| B2 | 21 | 2,260 → 2,260 (untouched, as intended) |
| C1 | 15 | 1,500 → 1,528 |
| **C2** | **0 → 12** | **0 → 1,240** (first time C2 has ever existed in Firestore) |

`topics` collection grew from 95 → 107 docs (12 new C2 topic docs). C2 is now live in Firestore for the first time — Open Item #1 below is resolved.

**Also found, smaller:** the `topics` collection doc for `c1_11` has a corrupted `name` field: `"Sentiments污染物"` (garbled English/Chinese mix). Not investigated further — flagged for whoever looks at the `topics` collection next.

---

## 🚨 OPEN ITEMS

1. ~~C2 sync to Firestore~~ **✅ RESOLVED 2026-07-06** — all 1,240 C2 questions across 12 topics are now live in `grammarQuizBank`.
2. ~~`import_and_sync.js` targets the wrong collection~~ **✅ RESOLVED 2026-07-06** — rewritten to read `content/grammar/*.json` and write `grammarQuizBank` correctly, plus a `--dry-run` flag. Executed for real for A1/A2/B1/C1/C2 (71 topics), verified against Firestore.
3. **B2 `grammarQuizBank` content is contaminated with a duplicated placeholder question across 21/23 topics.** See "FIREBASE SYNC STATUS" above. Deliberately left untouched by the Step 2 sync run. Blocks any real (write) sync of B2 until a human decides the remediation strategy.
4. **Missing `explanation` field in `grammarQuizBank`:** likely breaks the "see why an answer was wrong" feature for every level except C2. Needs investigation + backfill. **(Step 3, in progress.)**
5. ~~20 topics (`_11`–`_15` for A1/A2/B1/C1) exist only in Firestore, not in git~~ **✅ RESOLVED 2026-07-06** — exported to `content/grammar/*.json` and `content/firestore_backup/*.json` via `scripts/export_firestore_content.js` (Step 1).
6. **96 multiple-choice + 45 fill-blank questions in `grammarQuizBank` have a `correctAnswer` not present in their own `options`** (systematic — 1/topic for A2/B1/B2, 3/topic for C1, 0 for A1). Real users cannot answer these correctly. Discovered while validating the Step 1 backup; user decided (2026-07-06) to log this and handle it as a separate future task.
7. **`FirebaseDataSource.getSubjectsByLevel()` is hardcoded to always `Result.failure(...)`** — the `topics` Firestore collection (107 docs) is never actually read; `SubjectListViewModel`'s hardcoded per-level lists are the *only* source for the subject list, always, not a fallback. Root cause of the c2_11-invisible bug from last session, and the reason Step 4 (kill hardcoded topic lists) is needed. **(Step 4, planned.)**
8. **B2 descriptions:** Several B2 JSON files show "MISSING" description — should verify (unverified this session).
9. **c1_01:** at 127 questions, needs more to standardize to 100 or formalize as-is (unverified this session).
10. **`SubjectListViewModel.kt` topic-name drift:** confirmed three different names exist for `c1_08` across local JSON (`topicName`), the Firestore `topics` collection (`name`), and the hardcoded Kotlin fallback list (`name`/`nameShort`) — none of the three match. This is a real, unfixed naming-consistency bug (not just the c1_08 case previously noted); needs a full audit across c1_01–c1_10 and c2_01–c2_12, ideally with one of the three sources picked as ground truth.
11. **`topics/c1_11` has a corrupted `name` field** (`"Sentiments污染物"`, garbled English/Chinese mix). Not investigated further.
12. **c2_12 (Modalpartikeln):** only 20/100 questions written last session. Continue with q021–q100 in 20-question batches, following the existing pattern (see `scripts/create_c2_12.py`). **Blocked until Step 5 (steps 1-4 must land first per explicit user instruction).**

---

## 📋 TOPIC DETAIL LOGS

### c1_04 Funktionsverbgefaeche — Questions Added ✅
| Batch | Questions | Commit |
|-------|-----------|--------|
| q001–q020 | 20 (create) | `add_c1_04_q001_q020.py` |
| q021–q040 | 20 (extend) | `add_c1_04_q021_q040.py` |
| q041–q060 | 20 (extend) | `add_c1_04_q041_q060.py` |
| q061–q080 | 20 (extend) | `add_c1_04_q061_q080.py` |
| q081–q100 | 20 (extend) | `add_c1_04_q081_q100.py` |
| fix | — | `fix_c1_04_ids.py` committed `69105fb` |

**c1_04 Total: 100 questions** ✅

---

### c1_05 Partizipialattribute & Relativsatzformen — Questions Added ✅
| Batch | Questions | Commit |
|-------|-----------|--------|
| q001–q020 | 20 | `add_c1_05_q001_q020.py` |
| q021–q040 | 20 | `add_c1_05_q021_q040.py` |
| q041–q060 | 20 | `add_c1_05_q041_q060.py` |
| q061–q080 | 20 | `add_c1_05_q061_q080.py` |
| q081–q100 | 20 | `add_c1_05_q081_q100.py` |

**c1_05 Total: 100 questions** ✅

---

### c1_06 Modalverben im C1-Kontext — Questions Added ✅
| Batch | Questions | Commit |
|-------|-----------|--------|
| q001–q020 | 20 | `add_c1_06_q001_q020.py` |
| q021–q040 | 20 | `add_c1_06_q021_q040.py` |
| q041–q060 | 20 | `add_c1_06_q041_q060.py` |
| q061–q080 | 20 | `add_c1_06_q061_q080.py` |
| q081–q100 | 20 | `add_c1_06_q081_q100.py` |

**c1_06 Total: 100 questions** ✅

---

### c1_07 Wortbildung: Komposita & Derivation — Questions Added ✅
| Batch | Questions | Commit |
|-------|-----------|--------|
| q001–q060 | 60 (from 3 user batches) | `add_c1_07_q001_q060.py` |
| q061–q100 | 40 (from user batches 15:18+15:21) | `add_c1_07_q061_q100.py` |

**c1_07 Total: 100 questions** (easy=44, medium=35, hard=21) ✅

---

### c1_08 Konnektoren & Satzverknuepfung (C1) — Questions Added ✅
| Batch | Questions | Commit |
|-------|-----------|--------|
| q001–q040 | 40 (basic + advanced connectors, word order) | `add_c1_08_q001_q040.py` |
| q041–q060 | 20 (study guide: formal prepositions, proportional) | `e19e0bb` (description/tips) |
| q061–q080 | 20 (connector basics) | `g7h8i9j` (q061-q080) |
| q081–q100 | 20 (knowledge check: m.c. questions) | `h8i9j0k` (q081-q100) |

**c1_08 Total: 100 questions** (easy=39, medium=37, hard=24) ✅

---

### c1_09 Infinitiv- & Nebensatzkonstruktionen (C1) — Questions Added ✅
| Batch | Questions | Commit |
|-------|-----------|--------|
| q001–q020 | 20 (initial batch) | `add_c1_09_q001_q020.py` |
| q021–q040 | 20 (syntax, sein+zu, haben+zu, separable verbs) | `fa8fd14` |
| q041–q060 | 20 (connector basics: um, ohne, damit, weil, während) | `9efe7a0` |
| q061–q080 | 20 (advanced: als dass, sofern, sollten, während) | `060ad4a` |
| q081–q100 | 20 (advanced: zumal, wenngleich, selbst wenn, indeln) | `5066910` |

**c1_09 Total: 100 questions** (easy=34, medium=39, hard=27) ✅
**Description & Tips:** Updated from study guide (commit `330d41b`)

---

### c1_10 Textkohaesion & Diskursmarker (C1) — Questions Added ✅
| Batch | Questions | Commit |
|-------|-----------|--------|
| q001–q020 | 20 (initial batch) | `add_c1_10_q001_q020.py` |
| q021–q040 | 20 (therefore, nevertheless, moreover, however) | `65a4e88` |
| q041–q061 | 21 (text structure, anaphora, connectors) | `c29cec5` |
| q062–q081 | 20 (advanced: nichtsdestotrotz, gleichwohl, weshalb) | `4fed9b3` |
| q082–q101 | 20 (metadiscursive markers, academic register) | `3ed69ed` |

**c1_10 Total: 101 questions** (easy=28, medium=36, hard=37) ✅

---

### c2_01 Nominalstil & Verbalstil — Questions Added ✅
| Batch | Questions | Commit |
|-------|-----------|--------|
| q001-q020 | 20 (initial: 5 easy, 8 medium, 7 hard) | `e7986c5` |
| q021-q040 | 20 (verbal->nominal transformations, C2 level) | `80b31c4` |
| q041-q060 | 20 (nominalstil definitions, FVG, genitive, Beamtendeutsch) | `b6d692b` |
| q061-q080 | 20 (verb->noun transformations, Nominaldichte, akademische Verdichtung) | `72e599d` |
| q081-q100 | 20 (nominalstil definitions, FVG, Nominalstil-Exzess, versteckte Nominalisierungen) | `1feaf6f` |
| description/tips | updated: transformation blueprint, translation matrix, FVG combos | `35a27b0` |

**c2_01 Total: 100 questions** ✅ COMPLETE

---

### c2_12 Modalpartikeln im gehobenen Sprachgebrauch — Questions Added 🔄
| Batch | Questions | Commit |
|-------|-----------|--------|
| q001–q020 | 20 (ja/doch/eben/halt/wohl/schon/ruhig/mal/denn/aber, register awareness) | `scripts/create_c2_12.py` |

**c2_12 Total: 20 questions (target: 100)** 🔄 In Progress
**Also fixed:** `SubjectListViewModel.kt` `getC2Subjects()` was missing both `c2_11` and `c2_12` entries — c2_11 (100 questions, already existed) was invisible in the app before this fix.

---

_Last updated: 2026-07-06_