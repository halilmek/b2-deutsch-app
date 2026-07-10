# B2 Deutsch App — PROJECT STATUS

**Last Updated: 2026-07-06 (verified against live Firestore + local assets by Claude Code)**
**GitHub:** https://github.com/halilmek/b2-deutsch-app
**Firebase:** b2-deutsch-app
**Local App Path (Halil's machine):** `/Users/halilozturk/b2-deutsch-app`
**Firebase Credentials:** `/Users/halilozturk/Documents/b2-deutsch-app-firebase-adminsdk-fbsvc-4aa25c0ca2.json`

---

## 🚨🚨🚨 CORRECTION — 2026-07-06, discovered during Step 3: neither Firestore collection is actually live

**Everything below in "FIREBASE SYNC STATUS" about `grammarQuizBank` being what real users see is WRONG.** Tracing the quiz-results "hide explanation when absent" UI logic led to `LocalQuestionBank.kt`, and a full audit of every file read/write call site in that class shows:

- `LocalQuestionBank.getQuestionDetails()` — the function that actually supplies question text/options/answer/explanation to the running quiz — reads **exclusively** from `context.assets.open("$subjectId.json")`, i.e. the JSON bundled into the APK at build time. It never touches Firestore or any synced cache.
- `FirebaseSyncService` downloads Firestore collection **`moduleQuizQuestions`** (not `grammarQuizBank`) and calls `LocalQuestionBank.updateTopicFromFirebase()`, which writes a `"${subjectId}_fb.json"` file to internal storage via `context.openFileOutput(...)`.
- There is **no `context.openFileInput(...)` call anywhere in `LocalQuestionBank.kt`.** The `_fb.json` file that Firebase sync writes is never read back by anything. It's write-only, dead on arrival.
- `ContentRepository.getGrammarQuestionsBySubject()` (which reads `grammarQuizBank`) has **zero callers** anywhere in the ViewModel/Fragment layer — also dead code, never invoked.

**Net effect: question content for real users is 100% determined by whatever is bundled in the currently-installed APK (`app/src/main/assets/*.json`), baked in at the last Play Store release. Neither `grammarQuizBank` nor `moduleQuizQuestions` has any live effect on what users see, regardless of what's in either collection.** The only way to actually change content for real users is a new APK release with updated asset files.

**Consequences for this session's work:**
- Step 1 (backing up Firestore content into `content/`) is still valid and valuable — it's a legitimate data-loss-prevention measure regardless of whether the data is currently wired up to the running app.
- Step 2 "fixed" `import_and_sync.js` to write to `grammarQuizBank` instead of `moduleQuizQuestions` — but per the above, `moduleQuizQuestions` was actually the collection `FirebaseSyncService` *reads*, even though nothing downstream of that read has any effect either (the read-back is dead too). So Step 2's real-write execution (A1/A2/B1/C1/C2 → `grammarQuizBank`) had **zero effect on real users** — not because it was wrong to fix the collection-name bug, but because neither collection currently reaches a user's screen.
- Step 3 (backfilling `explanation` into Firestore) was about to repeat the same mistake — writing to a collection with no live path to users. **Stopped before doing any of that work.**
- The B2 content-contamination finding (duplicated placeholder question across 21/23 topics in `grammarQuizBank`) is **not currently affecting real users** either, by the same logic — though it would matter the moment anyone wires up a Firestore-backed content path (or if `grammarQuizBank` was populated by copying from a different source than intended, it's still worth fixing before it becomes live).
- Step 4 (kill hardcoded topic lists) is a **separate, still-valid concern** — that's about the *subject/topic list* (`SubjectListViewModel`'s hardcoded `getC1Subjects()` etc., and `FirebaseDataSource.getSubjectsByLevel()` always failing), not question *content*. The c2_11-invisible bug fixed last session was real and confirmed by that separate code path.

**✅ 2026-07-06: user decided — wire up the sync properly (option b).** Implemented:

1. **`LocalQuestionBank.getQuestionDetails()` now reads the Firebase-synced cache first.** Refactored to try `context.openFileInput("${subjectId}_fb.json")` before falling back to `context.assets.open("$subjectId.json")`. Shared parsing logic extracted into `findQuestionInJson()`. Verified with `./gradlew compileDebugKotlin` — builds clean, no new warnings.
2. **`import_and_sync.js` retargeted (again) — this time correctly — at `moduleQuizQuestions`,** the collection `FirebaseSyncService` actually queries. Doc shape now matches what `FirebaseSyncService`/`LocalQuestionBank.saveQuestionsJson()` expect: one doc per `subjectId` with a real `options` array (not pipe-delimited — that convention was specific to the still-dead `grammarQuizBank`), plus `explanation` (previously missing — Step 3's backfill happened automatically by including it from the start in the corrected schema).
3. **Versioning:** `FirebaseSyncService` keeps a single global version counter client-side and queries `version > currentVersion` across the whole collection — not per-topic. The script computes `newVersion = max(existing versions in the collection) + 1` and stamps every topic touched in a run with that same value, so future incremental syncs stay correct as long as this script remains the only writer.
4. **Checked for conflicts with pre-existing `moduleQuizQuestions` data first:** the 408 docs backed up in Step 1 were either one malformed topic-summary doc (`b2_04`, missing `version` entirely) or 406 orphaned individual-question docs, none with a `version` field — confirmed none of them were ever actually reachable by `FirebaseSyncService`'s `whereGreaterThan` query. No real user has ever received a synced update through this mechanism before today. Safe to proceed without any migration/cleanup of old data (left in place, harmless).
5. **Executed the real sync** for the same 71 non-B2 topics as before (A1/A2/B1/C1/C2), same B2 exclusion for the same contamination reason. Verified: 72 docs now have `version: 1` in `moduleQuizQuestions` (71 grammar topics + the correction includes recount — see table below), with real question-shaped data including `explanation`.

| Level | Topics synced | Questions synced |
|-------|---------------|-------------------|
| A1 | 15 | 1,100 |
| A2 | 15 | 1,710 |
| B1 | 15 | 1,501 |
| C1 | 15 | 1,528 |
| C2 | 12 | 1,240 |
| **B2** | **0 (deliberately excluded)** | **0** |

**This is now a genuinely live pipeline** — the next time the app runs on a device with `FirebaseSyncService.syncIfNeeded()` due (fresh install, or >7 days since last sync, or a manual `forceSync()`), these 71 topics will download and actually reach the quiz screen. **Not yet verified on an actual device/emulator** — this environment has no Android runtime available; recommend a manual on-device smoke test (fresh install or clear app data, open the app, confirm sync fires and a synced topic's content matches `content/grammar/`) before relying on this in production.

**Explanation-field gap report (Step 3, as instructed — not auto-generated, logged for a human content-authoring decision):** local content is missing `explanation` for exactly these already-known topics (all traced back to Step 1's Firestore-only export, which never had explanations to begin with):

| Level | Topics missing explanation | Questions affected |
|-------|------------------------------|----------------------|
| A1 | a1_11–a1_15 | 500 |
| A2 | a2_11–a2_15 | 500 |
| B1 | b1_11–b1_15 | 500 |
| C1 | c1_11–c1_15 | 500 |
| B2 | b2_07 only (partial — 40 of its 100 questions) | 40 |
| C2 | none | 0 |

Total: 2,040 questions across 21 topics have no explanation text anywhere (not lost by any script — they never had one; these are the topics that exist only in Firestore with no authored content behind them). **Not auto-generated.** This is a content-authoring task for a human/future session, not something to backfill silently.

**UI already handles missing explanations correctly, no changes needed:** checked both quiz-result code paths. `QuizResultAdapter.kt` sets `binding.tvExplanation.visibility = GONE` when `explanation.isEmpty()`. `QuizViewModel.submitQuiz()` applies `.ifEmpty { "Keine Erklärung verfügbar" }` before building each `WrongAnswer`, so `QuizResultFragment.createWrongAnswerCard()` always renders either the real explanation or that explicit placeholder — never a blank row. (Unrelated aside noticed in passing: `QuizResultFragment.kt`'s hardcoded strings — "Question $number", "Your answer:", "Correct answer:" — are in English while the rest of the app's UI is German; not fixed here, out of scope for this task.)

---

## 📋 OVERALL PROGRESS SUMMARY

**Two numbers matter here and they legitimately differ — see "Firestore Reality Check" below.**
`Local` = topics/questions bundled as JSON in `app/src/main/assets/` (what ships in the APK).
`Firestore` = topics live in the `grammarQuizBank` collection, read via `FirebaseDataSource.getGrammarQuestionsBySubject` for quiz questions. **Correction from last session:** the *subject/topic list itself* (`getSubjectsByLevel`) is hardcoded in `FirebaseDataSource.kt` to always `Result.failure(...)` — it is not "used when Firestore succeeds, falls back otherwise," it **never** queries Firestore. The hardcoded per-level lists in `SubjectListViewModel.kt` are the only path, always. See Open Item on `SubjectListViewModel` below (Step 4 in progress).

| Module | Local Topics | Local Questions | Firestore Topics | Firestore Questions | Target |
|--------|-------------|-----------------|-------------------|----------------------|--------|
| A1 | 10 | 600 | 15 | 1,500 (now `moduleQuizQuestions`, not `grammarQuizBank`) | 1,000 |
| A2 | 10 | 1,210 | 15 | 1,710 | ~1,000 |
| B1 | 10 | 1,001 | 15 | 1,501 | 1,000 |
| B2 | 24 | 2,321 | 23 | 0 (deliberately unsynced — contamination) | ~2,000 |
| C1 | 10 | 1,028 | 15 | 1,528 | 2,000 |
| **C2** | **12** | **1,320** | **12** | **1,320** | **~2,000** |
| **Total (local)** | **76** | **7,480** | | | **~8,000** |

*(This table is a snapshot from earlier in the session — see "STEP 4"/"STEP 5"/"ALL 5 STEPS COMPLETE" sections further down for the final, corrected state of the sync pipeline and content counts.)*

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
| 12 | c2_12 | Modalpartikeln im gehobenen Sprachgebrauch | 100 | ✅ Complete |

**C2 Total: 1,320 questions (target: ~2,000). Synced live to Firestore (`moduleQuizQuestions`) as of 2026-07-06 — see "Firebase Sync Status" below.**

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

1. ~~C2 sync to Firestore~~ **✅ RESOLVED 2026-07-06, corrected same day** — first synced to `grammarQuizBank` (found to be dead code, no effect on real users), then correctly re-synced to `moduleQuizQuestions` (the collection `FirebaseSyncService` actually reads) — all 1,240 C2 questions across 12 topics.
2. ~~`import_and_sync.js` targets the wrong collection~~ **✅ RESOLVED 2026-07-06 (twice)** — first "fixed" to `grammarQuizBank` based on an incorrect assumption about what's live; corrected same day to `moduleQuizQuestions` after tracing `LocalQuestionBank.kt`'s actual read paths. See "CORRECTION" section above for the full story.
3. **B2 content is contaminated with a duplicated placeholder question across 21/23 topics** (found in `grammarQuizBank`, not yet checked directly in `moduleQuizQuestions` but likely the same root content). Deliberately excluded from both sync runs. Blocks any real sync of B2 until a human decides the remediation strategy.
4. ~~Missing `explanation` field~~ **✅ RESOLVED 2026-07-06** — the corrected `moduleQuizQuestions` schema includes `explanation` from the start; synced topics now carry it. **Genuinely missing (not a sync bug) for 21 topics/2,040 questions** — see the "Explanation-field gap report" table above. Logged for a human content-authoring decision, not auto-generated.
5. ~~20 topics (`_11`–`_15` for A1/A2/B1/C1) exist only in Firestore, not in git~~ **✅ RESOLVED 2026-07-06** — exported to `content/grammar/*.json` and `content/firestore_backup/*.json` via `scripts/export_firestore_content.js` (Step 1).
6. **96 multiple-choice + 45 fill-blank questions in `grammarQuizBank` have a `correctAnswer` not present in their own `options`** (systematic — 1/topic for A2/B1/B2, 3/topic for C1, 0 for A1). Since `grammarQuizBank` turned out to be dead code, this specific instance doesn't currently reach real users — but the same content may well be duplicated into `moduleQuizQuestions` from whatever originally seeded it; not re-checked there. Logged as a separate future task regardless.
7. ~~`FirebaseDataSource.getSubjectsByLevel()` is hardcoded to always `Result.failure(...)`~~ **✅ RESOLVED 2026-07-06 (Step 4)** — see full writeup below.
8. **B2 descriptions:** Several B2 JSON files show "MISSING" description — should verify (unverified this session).
9. **c1_01:** at 127 questions, needs more to standardize to 100 or formalize as-is (unverified this session).
10. **`SubjectListViewModel.kt` topic-name drift** was the underlying disease Step 4 cured architecturally (see below), but the *specific* three-way name mismatch for `c1_08` (local JSON `topicName` vs. Firestore `topics.name` vs. the now-deleted hardcoded fallback) is a content-accuracy question, not a code bug — worth a human pass to pick one correct name and fix it at the source (local JSON + Firestore `topics` doc) whenever c1_08 is next touched.
11. **`topics/c1_11` has a corrupted `name` field** (`"Sentiments污染物"`, garbled English/Chinese mix). A second instance of this same corruption pattern was found in Step 4 in the (now-deleted) hardcoded fallback for `c1_10` (`"10. Partizipialkonstruktionen (把从句压缩为分词短语)"`) — both are gone now that `c1_10`'s hardcoded entry is deleted, but `topics/c1_11`'s Firestore doc still has the corrupted name. Not investigated further.
12. **c2_12 (Modalpartikeln):** only 20/100 questions written last session. Continue with q021–q100 in 20-question batches, following the existing pattern (see `scripts/create_c2_12.py`). **Unblocked — Step 5 is next.**
13. **Not verified on an actual Android device/emulator** — the `LocalQuestionBank`/`FirebaseSyncService` wiring fix, the `moduleQuizQuestions` sync pipeline, and Step 4's dynamic subject-list rewrite were all verified by code trace + `./gradlew assembleDebug` + `./gradlew testDebugUnitTest` + direct Firestore inspection only, since this environment has no Android runtime. Recommend a manual on-device test before trusting this in production: fresh install → confirm every level's subject list still populates correctly and descriptions/tips still render (especially A1 and B2, whose content moved from Kotlin into JSON this session) → force a sync → confirm downloaded content matches `content/grammar/`.
14. ~~Step 4 regression: B2's grammar topic list showed 12 extra "topics" (`b2_reading_01`–`_12`) with no quiz~~ **✅ RESOLVED 2026-07-06** — user-reported. Root cause: Step 4's `getSubjectsByLevel()` queried `topics` by `level` only, not `type`. `topics/b2_reading_01..12` are `type: "reading"` scaffolding placeholders (`textCount: 0, questionCount: 0` — matching PRODUCT_BACKLOG.md's unbuilt READ-010 "Premium A1-C1 readings" item), created for a future reading-comprehension feature, never populated with any passage or question anywhere. Fixed by adding `.whereEqualTo("type", "grammar")` to the query — this is the grammar-topics screen specifically (`SubjectListFragment`'s only caller of `loadSubjectsForLevel` when no category is set), so the filter is unambiguously correct, not a workaround. Verified directly against Firestore: B2 now returns exactly 23 topics (was 35). Checked all other levels — only B2 has any non-`grammar` topics, so no other level was affected.
15. **PRODUCT_BACKLOG.md significantly undersells real progress on Epics 6/7/8/9 (Vocabulary/Writing/Speaking/Peer Exams)** — it marks all of these "📋 TODO," but real Kotlin UI code and Cloud Functions already exist for several of them. See "🏗️ FEATURE COMPLETENESS AUDIT" below for the full, verified picture. Backlog should be corrected the next time someone works in these epics, rather than trusted at face value.

---

## 🏗️ FEATURE COMPLETENESS AUDIT (2026-07-06)

User asked to "keep coding until the app is finished" per the planning docs. Given this session's repeated pattern of docs not matching code, ran a dedicated audit (read-only) of the 5 areas with the biggest doc/reality gap before picking what to build. Findings, verified directly against source (not just the subagent's report):

| Area | Real status |
|------|-------------|
| **Vocabulary** | `VocabularyFragment` (~35 lines) shows a hardcoded `"Vocabulary coming soon!"` message. No ViewModel. `FirebaseDataSource.getVocabularyByLevel/Category` exist but nothing calls them. Was **not reachable from Home at all** (no card, no nav action) until this session. |
| **Writing** | `WritingFragment` has a real text-input UI with a 50-char minimum, but the submit button just sets `tvResult.text = "Evaluation feature coming soon!"` (literal `// TODO: Submit for AI evaluation` above it). **`functions/index.js` already has a fully-implemented `evaluateWriting()` Cloud Function** (MiniMax AI, prompt building, Firestore write-back, token estimation) that the Android app **never calls**. Home's "Writing" card used to route through `SubjectListFragment`'s fake `getWritingQuizSubjects()` placeholder list into the grammar-quiz system with a made-up `quizId` that matches no real content — a more broken/confusing dead end than the honest stub screen. |
| **Speaking** | Same shape as Writing: `SpeakingFragment` has two buttons (`btnAIPartner`, `btnPeerExam`) that are empty `// TODO` bodies. `functions/index.js` has a fully-implemented `evaluateSpeaking()` Cloud Function, unused. Was gated behind a premium check in `HomeFragment` but routed to the same kind of fake quiz-category dead end as Writing. |
| **Exams** | Real, working UI: `ExamsFragment`/`ExamActiveFragment` have a functioning timer, question flow, and progress tracking (already reachable from Home). But `getSampleQuestions()` returns 100% hardcoded placeholder text ("Option A/B/C/D") — zero Firestore-backed exam content exists anywhere. |
| **Lessons** | The most real of the five: `LessonsViewModel` calls `ContentRepository.getLessonsByLevel()` for real, falling back to 4 hardcoded sample lessons only if that fails. `LessonDetailFragment` similarly queries real content. Was **not reachable from Home at all** until this session (defined in `nav_graph.xml`, no card/action pointing to it). |

**Fixed this session (low-risk, no new epic — just made already-built work reachable, per explicit user approval):**
- `nav_graph.xml`: added `action_home_to_lessons`, `action_home_to_vocabulary`, `action_home_to_writing`, `action_home_to_speaking` (all four destinations already existed in the graph, just orphaned).
- `HomeFragment.kt`: Writing/Speaking cards now navigate to their real (draft) screens instead of the fake `SubjectList` category dead-end. Added click handlers for two new cards.
- `fragment_home.xml`: added "Wortschatz" (Vocabulary) and "Lektionen" (Lessons) cards — previously these two screens had literally no entry point in the UI at all.
- Verified: `./gradlew assembleDebug` clean, no new warnings.
- **Not verified on-device** (no Android runtime in this environment) — recommend confirming all 4 new nav paths actually open the right screen before relying on this.

**NOT done, deliberately, pending explicit direction (see below):** wiring Writing/Speaking to their Cloud Functions, seeding real Exams content, building out Vocabulary flashcards. These are real epics requiring product decisions (entitlement/quota rules, paid AI API cost exposure, Cloud Functions deployment/testing) that shouldn't be started without the user picking priority and confirming the AI-cost/infra risk explicitly.

---

## 📖 EPIC 6 — Vocabulary flashcards, built end-to-end (2026-07-07)

User picked Vocabulary as the next epic (self-contained, no paid AI API or Cloud Functions dependency, unlike Writing/Speaking). Built the full vertical slice: content, per-user spaced-repetition progress, flashcard UI, and navigation.

**Content:** 108 words across the 9 categories that already exist in Firestore's `themes` collection (`beruf`, `bildung`, `geschichte`, `gesellschaft`, `gesundheit`, `medien`, `reisen`, `umwelt`, `wirtschaft` — the same taxonomy already used for B2 reading topics, reused here instead of inventing a second one). `content/vocabulary/{category}.json` (git, source of truth) → `scripts/sync_vocabulary.js` → Firestore `vocabulary` collection (matches `VocabularyWord`'s field names exactly — `FirebaseDataSource.getVocabularyByLevel/getVocabularyByCategory` already existed and worked, just had zero documents to return before this). Verified: 108/108 unique ids, every word has all 3 languages + an example sentence, synced and confirmed directly against Firestore.

**Per-user progress — architectural note:** `VocabularyWord.isLearned`/`reviewCount`/`lastReviewed` exist on the data class but must never be read from or written to the shared Firestore content document (that would make one user's "learned" status visible to every other user of the same word). New `VocabularyProgressStore` (SharedPreferences, mirroring `LocalQuestionBank`'s existing local-progress pattern) tracks this per-device instead: a simple Leitner-style spacing (0/1/2/4/8/16-day intervals; "correct" advances the interval, "hard"/"wrong" resets it to due-immediately). `VocabularyViewModel` overlays this local state onto the Firestore-sourced words at read time.

**UI:** `VocabularyFragment` rewritten from its "coming soon" placeholder to a real category list (`VocabularyThemeAdapter`, word counts sourced from Firestore, categories with 0 words filtered out automatically — none currently, since all 9 are seeded). New `FlashcardFragment`: tap-to-flip card (German front; English/Turkish/example sentence on the back), three action buttons, deck built from words actually due for review (not just all words), completion state when the due-deck is empty.

**Also fixed in passing:** the `themes/gesellschaft` Firestore doc had `name: "Gesundheit und Soziales"` (copy-paste error from the `gesundheit` theme, given `gesellschaft` = society/social issues, not health) — corrected to `"Gesellschaft und Soziales"` directly in Firestore, since the new Vocabulary screen surfaces this name to real users.

**Nav:** added `flashcardFragment` + `action_vocabulary_to_flashcard` (level/category/categoryName args) to `nav_graph.xml`. `HomeFragment`'s "Wortschatz" card (added last session) already pointed at `vocabularyFragment`, now a real screen instead of a stub.

**Verified:** `./gradlew assembleDebug` clean, no new warnings. **Not verified on-device** (no Android runtime in this environment) — recommend a manual test before trusting this in production: open Wortschatz from Home → confirm all 9 categories show with correct word counts → open one → flip a card, tap all three answer buttons, confirm the deck advances and the completion screen appears after the last word.

**Scope note:** 12 words/category (108 total) is a deliberately modest starting set, matching the same "land a first batch, extend later" pattern used for grammar content this session — not a claim that vocabulary content is complete. `VOCAB-004` (mark known/learning — done via the 3 flashcard buttons), `VOCAB-005` (spaced repetition — done, simple Leitner spacing), `VOCAB-006` (audio pronunciation), `VOCAB-008` (progress tracking UI beyond the flashcard flow itself), and `VOCAB-009`/`VOCAB-010` remain open for a future session.

---

## 🏗️ STEP 4 — Killed hardcoded per-level subject lists (2026-07-06)

**Problem:** `SubjectListViewModel` had six near-identical hardcoded functions (`getA1Subjects()` … `getC2Subjects()`), each a `listOf(Subject(...), ...)` literal — a direct violation of `CLAUDE.md`'s "never hardcode a CEFR level" rule, and the root cause of the c2_11-invisible bug found last session (a topic simply missing from one of these lists is invisible, silently, with no error). `FirebaseDataSource.getSubjectsByLevel()` was hardcoded to always `Result.failure(...)`, so the Firestore `topics` collection (107 docs) was never actually read despite being fully populated — these six lists were the *only* code path, always, for every level.

**Also found while auditing what to preserve before deleting:** local asset JSON files for **A1 (all 10 topics) and B2 (22 of 23 topics)** had no `description`/`tips` fields at all — that content only existed as string literals inside the Kotlin hardcoded lists. Deleting those lists without migrating this content first would have silently erased real, curated German-language study content from what users see. Also discovered in passing: **`b2_03` was never in the hardcoded fallback list at all** (an invisible-topic bug identical in shape to last session's c2_11 case, just never previously noticed) — it will now show up correctly since it already existed in the Firestore `topics` collection.

**Fix, in order:**
1. Migrated all 32 affected topics' `description`/`tips` (verbatim, including markdown tables and emoji formatting) from the Kotlin source into both `app/src/main/assets/*.json` and `content/grammar/*.json`. Verified every topic except the pre-existing `b2_03` gap now has both fields populated.
2. `FirebaseDataSource.getSubjectsByLevel()` now runs a real query against `topics` (`whereEqualTo("level", level)`), mapping each doc through a new pure function `buildSubjectFromTopicMeta()` (in `data/model/SubjectMapper.kt`) with zero per-level or per-id branching.
3. `SubjectListViewModel.loadSubjectsForLevel()`: on Firestore success, each `Subject` is enriched with `description`/`tips`/`topicName` from the matching bundled asset file (instant, no network needed, no reason to skip it just because Firestore succeeded). On Firestore failure (offline), falls back to `discoverSubjectsFromAssets()`, which lists bundled files matching `{level}_NN.json` via `context.assets.list("")` and builds subjects purely from JSON content — same "no hardcoded list" property as the Firestore path.
4. Deleted `getDefaultSubjects()`, `getA1Subjects()` … `getC2Subjects()`, and the old asset-merge-onto-hardcoded-defaults version of `getDefaultSubjectsFromJson()` entirely (net ~1,050 lines removed from `SubjectListViewModel.kt`). Left `getReadingQuizSubjects`/`getListeningQuizSubjects`/`getWritingQuizSubjects`/`getSpeakingQuizSubjects` untouched — these were already level-agnostic (parameterized uniformly by `level`, no per-level branching), a different category of subject (quiz-type templates) out of scope for this fix.
5. `scripts/import_and_sync.js` now also writes a `topics/{subjectId}` doc alongside `moduleQuizQuestions/{subjectId}` on every sync, so this collection — now load-bearing for the app, not just decorative — stays accurate going forward.
6. Added `app/src/test/` (didn't exist before) with `SubjectMapperTest.kt`, proving a topic never referenced anywhere else in the codebase (`c2_99`, a made-up id) maps to a correct `Subject` with zero code changes — directly encodes the "add a topic → it appears" requirement.

**Verified:** `./gradlew assembleDebug` — clean, no new warnings (2 pre-existing unused-parameter warnings unchanged). `./gradlew testDebugUnitTest --tests SubjectMapperTest` — all 3 tests pass. Not verified on-device (see Open Item #13).

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

### c2_12 Modalpartikeln im gehobenen Sprachgebrauch — Questions Added ✅
| Batch | Questions | Script |
|-------|-----------|--------|
| q001–q020 | 20 (ja/doch/eben/halt/wohl/schon/ruhig/mal/denn/aber, register awareness) | `scripts/create_c2_12.py` |
| q021–q040 | 20 (bloß/nur/überhaupt/sowieso/ohnehin/allerdings/immerhin/freilich, register substitution) | `scripts/extend_c2_12_q021_q040.py` |
| q041–q060 | 20 (halt vs. eben regional split, na ja, particle stacking naturalness, formal rewrites) | `scripts/extend_c2_12_q041_q060.py` |
| q061–q080 | 20 (rhetorical schon, denn homonym vs. conjunction, nun, diachronic origin, register-inappropriate combos) | `scripts/extend_c2_12_q061_q080.py` |
| q081–q100 | 20 (denn syntactic restriction proof, zwar...aber, Abtönungspartikel term, exam-skill synthesis questions) | `scripts/extend_c2_12_q081_q100.py` |

**c2_12 Total: 100 questions** ✅ COMPLETE (target reached 🎉)
**All 100 questions marked `reviewed: false`** per ROLES.md's content workflow (AI-generated content is DRAFT until a human SME sets `reviewed: true`) — first topic in this repo to carry this field. `scripts/import_and_sync.js` now propagates it; older already-shipped content defaults to `reviewed: true` when the field is absent, so this doesn't retroactively flag existing content as unreviewed.
Validated: 100/100 unique ids, every `correctAnswer` present in its own `options`, build clean (`./gradlew assembleDebug`).
Synced to Firestore (`moduleQuizQuestions/c2_12`, version 2; `topics/c2_12` updated to `questionCount: 100`) — verified directly against Firestore.

**Also fixed last session:** `SubjectListViewModel.kt` `getC2Subjects()` was missing both `c2_11` and `c2_12` entries — c2_11 (100 questions, already existed) was invisible in the app before that fix. That whole hardcoded-list mechanism is now deleted (see Step 4 above); c2_12 didn't need any code change to reach 100 questions — this is the dynamic pipeline (Steps 1–4) working as intended.

---

## ✅ ALL 5 STEPS COMPLETE (2026-07-06)

1. **Backup** — Firestore content (grammarQuizBank + other collections) exported into `content/`, closing the git-history gap for topics `_11`–`_15`.
2. **Sync script fixed** — twice; first to the wrong-but-plausible `grammarQuizBank`, then corrected to `moduleQuizQuestions` (the collection actually read by `FirebaseSyncService`) after tracing `LocalQuestionBank.kt`.
3. **Explanation field** — included from the start in the corrected schema; genuine content gaps (21 topics/2,040 questions) reported, not auto-generated.
4. **Hardcoded topic lists killed** — `SubjectListViewModel` and `FirebaseDataSource.getSubjectsByLevel()` now dynamic, backed by a unit test; 32 topics' description/tips content migrated out of Kotlin before deletion to avoid data loss.
5. **c2_12 extended to 100 questions**, synced live.

**Still open, not addressed this session (see Open Items above for detail):** B2 content contamination (blocks any B2 Firestore sync), the 96+45 broken-`correctAnswer` questions, `c1_11`/`c1_10` corrupted-text findings, `c1_08` three-way name mismatch, `c1_01`/B2-description verification, and — most importantly — **no on-device verification was possible in this environment.** Recommend a manual smoke test before the next release: fresh install → browse every level's subject list → open a few topics (especially A1/B2, whose content moved from Kotlin to JSON) → confirm descriptions/tips render → complete a quiz → check quiz-results explanations.

---

## 🐛 TWO BUGS FIXED FROM MANUAL DEVICE TESTING (2026-07-07)

User did an actual on-device test pass (first real device verification this session's data pipeline/UI work has had) and found two bugs. Fixed both, scope held strictly to these two — no new features, no content work.

### Bug 1 — C2 level showed a lock icon, entering C2 showed no topics

**Root cause:** `LevelAdapter.kt` had a hardcoded `if (level.id == "C2")` special case (left over from before C2 had real content) that displayed a `"🔒 C2"` button on the C2 level card. Its click handler only showed a "Coming Soon" Toast and never called `onLevelClick` — unlike every other level, which navigates to `action_home_to_subjectList`. Because the button sat within the card's tappable bounds, a tap landing on it was consumed there instead of reaching the card's own click listener. `Level.isLocked` was correctly `false` for every level the whole time — this was a second, separate hardcoded gate that bypassed that flag entirely. Directly contradicts `docs/MONETIZATION_SPEC.md` (topic browsing free for every level) and `CLAUDE.md`'s "no hardcoded CEFR levels" rule.

**Data path was already healthy — verified before touching code:** queried Firestore directly, confirmed all 12 `c2_*` docs exist in `topics` with exactly the fields `buildSubjectFromTopicMeta` expects (`id`, `level`, `name`, `questionCount`, `type: "grammar"`); confirmed all 12 `c2_*.json` asset files exist for the offline fallback. So Step 4's dynamic topic-loading path was never the problem — C2 topics were fully ready, just unreachable because of the lock button intercepting the tap.

**Fix:** removed the C2 special case and `onC2Click` callback from `LevelAdapter.kt`/`HomeFragment.kt`, removed the now-dead `btnC2` view from `item_level.xml`. C2 now behaves identically to every other level. Also added a `Log.d`/`Log.e` in `FirebaseDataSource.getSubjectsByLevel()` reporting the Firestore query result count per level (requested, for on-device log verification).

**Found but out of scope, not touched:** `LocalQuestionBank.kt`'s `getAllTopicIds()`/`getAllC2TopicIds()` hardcode C2's topic count at 10, but C2 actually has 12 topics (`c2_11`/`c2_12` not covered). This affects grammar-quiz progress-tracking functions (`resetAllTopics`, `initializeFromAssets`) for those two specific topics — unrelated to the topic-*list* visibility bug just fixed, and outside this session's "fix ONLY these two bugs" scope. Flagging for a future session.

### Bug 2 — Flashcards didn't flip on tap

**Root cause:** `FlashcardFragment.kt` sets its click listener on `cardFlashcard` (the `MaterialCardView`), but the card's only direct child was a `NestedScrollView` filling the whole card. A ScrollView/NestedScrollView intercepts the touch stream for its own scroll-gesture detection and does not forward it as a click to its parent — so no matter where inside the card a user tapped, the touch was consumed before it could reach `cardFlashcard`'s own click detection. The click listener logic and `flipCard()`'s visibility toggle were both already correct; the bug was purely about which view in the hierarchy actually received the tap.

**Checked and ruled out the "data binding, not flip" alternative explicitly asked about:** `showCard()` already sets `tvEnglish`/`tvTurkish`/`tvExample` unconditionally on every card (not gated on flip state) — the back side's data was always correct, only its visibility toggle was unreachable.

**Fix:** removed the `NestedScrollView` (per instruction, preferred a simple robust visibility toggle over a fancy broken mechanism — there was no scroll requirement to begin with; flashcard content is a few short lines). The content `LinearLayout` is now a direct child of `cardFlashcard`, so a tap anywhere in the card bubbles straight to its click listener.

**Verified:** `./gradlew assembleDebug` clean for both fixes combined, no new warnings (same 2 pre-existing unused-parameter warnings as before, unchanged).

**Verified on device: PENDING (user will re-test).**

---

## 📋 CURRICULUM VISIBILITY — derived "Wird vorbereitet" topic state (2026-07-07, COMPLETE)

New requirement: show the full planned topic curriculum per level, including topics with no questions authored yet, instead of only showing topics once content exists. Built everything except the actual content addition, which is blocked on a real question (see below).

**Done, code-complete, verified via `./gradlew assembleDebug`/`testDebugUnitTest`:**

1. **`Subject.isComingSoon`** — new computed property (`questionCount <= 0`), not a stored field, not a per-topic-id list. Derived purely from whatever `questionCount` Firestore/asset metadata already supplied.
2. **`SubjectAdapter.kt`** — when `isComingSoon`, dims the card (`alpha = 0.55f`) and replaces the quiz-count text with `"🕒 Wird vorbereitet"`. Explicitly kept separate from `ivLock` (the premium-paywall icon) — this is a content-readiness state, not a paywall, and MONETIZATION_SPEC says all quizzes are free; conflating the two would visually lie about why the topic isn't available.
3. **`SubjectListFragment.kt`** — tapping a coming-soon topic (in the grammar/"Themen" flow specifically) now shows a Toast ("Dieses Thema wird noch vorbereitet und ist bald verfügbar.") instead of navigating. Gate is `subject.isComingSoon`, evaluated per-subject at click time — works for any level, no C2-specific branch anywhere in this code.
4. **`scripts/import_and_sync.js` hardened** — `planTopic()` used to call `data.questions.map(...)` directly, which throws if a placeholder content file has no `questions` key at all (as opposed to an empty array). Now defaults to `[]` and defaults `topicName` to the subjectId if absent, so a topic with zero questions syncs its metadata (`moduleQuizQuestions` doc + `topics` doc, both with `questionCount: 0`) without error. `applyTopic()` already handled an empty `questions` array fine — verified by reading the write path, no crash risk there.
5. **Verified the asset-fallback path needs no changes** — `SubjectListViewModel.discoverSubjectsFromAssets()` already reads `totalQuestions` via `json.optInt("totalQuestions", 0)` (safe default) and never touches the `questions` array for metadata purposes, so a placeholder asset file with `questions: []` (or a missing key) works today with zero code changes.
6. **Also fixed the tangential finding from last session**, as explicitly requested: `LocalQuestionBank.kt` hardcoded topic counts per level (A1/A2/B1/C1/C2 → 10, B2 → 23) across six near-identical `getAllXXTopicIds()` functions plus a duplicate hardcoded count map in the public `getAllTopicIds(level)`. Replaced all of it with `discoverAllTopicIdsFromAssets()` (used by `initializeFromAssets`/`resetAllTopics`) and a regex-based `getAllTopicIds(context, level)` — both derive topic IDs by scanning actual bundled asset file names (`{prefix}_NN.json`), no hardcoded level list, no hardcoded counts, matches the exact mechanism already used in `SubjectListViewModel`'s Step 4 fix. Updated the one external caller (`QuizViewModel.loadQuizzes()`, the legacy `QuizzesFragment` path) to pass `Context`.

**Part (a) resolved 2026-07-07 — user-approved C2 curriculum draft, now live as placeholders.** Since no canonical C2 topic list existed anywhere in the repo, drafted 9 additional C2-level topics (read the existing `c2_01`–`c2_12` titles first to avoid duplication, proposed distinct Goethe/telc-C2-appropriate topics, presented as a table, stopped for approval — user approved as-is):

| id | Titel |
|---|---|
| `c2_13` | Erweiterte Partizipialkonstruktionen |
| `c2_14` | Stilebenen & Registerwechsel |
| `c2_15` | Textkohäsion: Ellipsen, Pro-Formen & Sprachökonomie |
| `c2_16` | Ironie, rhetorische Mittel & Sprachbilder |
| `c2_17` | Erweiterte Vergleichs- und Gradationsstrukturen |
| `c2_18` | Erweiterte Genitivkonstruktionen & Attributstapelung |
| `c2_19` | Anglizismen & Sprachwandel im Deutschen |
| `c2_20` | Textsortenspezifische Stilmittel: Kommentar & Rezension |
| `c2_21` | Idiomatik & feste Wendungen im gehobenen Kontext |

Created via `scripts/create_c2_placeholder_topics.py`: `content/grammar/{id}.json` + `app/src/main/assets/{id}.json` for each, with real `topicName`/`description`, `tips: []`, `questions: []`, `totalQuestions: 0` — **deliberately zero questions, content generation is a separate task pending explicit go-ahead, not done here.**

Synced via the now-hardened `import_and_sync.js` (dry-run first, then real) — zero errors, exactly the scenario the hardening fix was for. **Verified directly against Firestore** (not just trusted the script's own success output):

| Collection | Result |
|---|---|
| `topics/{c2_13..c2_21}` | All 9 exist, correct `name`/`level: C2`/`type: grammar`/`questionCount: 0` |
| `moduleQuizQuestions/{c2_13..c2_21}` | All 9 exist, `totalQuestions: 0`, `questions: []`, `version: 3` |
| `topics` where `level==C2 && type==grammar` | **21 total** — 12 with real questions (`c2_01`–`c2_12`), 9 correctly flagged coming-soon (`c2_13`–`c2_21`) |

This is the full planned C2 curriculum now visible in Firestore. In the app (verified by code path, not on-device — see caveat below): `FirebaseDataSource.getSubjectsByLevel("C2")` returns all 21 (no `questionCount` filtering in the query, by design — coming-soon topics are meant to be *visible*, just not *navigable*); each maps through `buildSubjectFromTopicMeta` with `questionCount: 0`; `Subject.isComingSoon` evaluates true; `SubjectAdapter` dims the card and shows "🕒 Wird vorbereitet"; `SubjectListFragment`'s click handler shows the info Toast instead of navigating. `./gradlew assembleDebug` clean with the new assets bundled.

**Not verified on an actual device** (no Android runtime in this environment, consistent with every other UI change this session) — recommend confirming on next device test: open C2 → see 21 topics total, 9 visibly dimmed with "Wird vorbereitet" → tap one of the 9 → confirm it shows the info toast and does not navigate → tap a real topic (e.g. `c2_01`) → confirm normal navigation still works.

---

## 🔬 DIAGNOSIS ONLY (2026-07-07) — B2 contamination + broken-correctAnswer re-check, no content modified

User manually checked B2 on-device and found no contamination, correctly contradicting the "B2 is contaminated" open item. Re-ran the original checks across all four sources, read-only, nothing fixed or rewritten.

### B2 contamination ("___ ich in Deutschland ankam..." at q001/q021/q061/q081, and "Er hat sich gemeldet..." at q002/q022 — the original report only mentioned the first sentence at q001 and, for `b2_07/08/09` only, a second sentence at q002; the actual footprint is wider, see below)

| Source | Contaminated topics (excl. `b2_01`, which legitimately owns the first sentence as its real Konnektoren q001) |
|---|---|
| **`content/grammar/*.json`** (git source of truth) | **0** — clean |
| **`app/src/main/assets/*.json`** (bundled APK) | **0** — clean |
| **`moduleQuizQuestions`** (live Firestore, what `FirebaseSyncService` actually downloads) | **0** — clean. Only one B2 doc exists there at all (`b2_04`, a malformed leftover from before this session, no `version` field — never reachable by the sync query anyway). Checked its `questions[]` directly: no match for either placeholder sentence. |
| **`grammarQuizBank`** (live Firestore, confirmed dead code — nothing in the app calls `getGrammarQuestionsBySubject`) | **21 of 23 topics** (`b2_03`–`b2_23`, every topic except `b2_01`/`b2_02`) — **still contaminated, unfixed.** Each has *both* placeholder sentences, at *more* positions than originally documented: `q001`/`q021`/`q061`/`q081` (first sentence) **and** `q002`/`q022` (second sentence) — not just `b2_07`–`b2_09` as the original note said; all 21 topics carry both. |

### Broken `correctAnswer`-not-in-`options` (re-checked with a corrected, schema-aware comparison — see note below)

| Level | `content/` MC / fill | `assets/` MC / fill | `moduleQuizQuestions` MC / fill | `grammarQuizBank` MC / fill |
|---|---|---|---|---|
| A1 | 4 / 0 | 4 / 0 | 4 / 0 | 4 / 0 |
| A2 | 50 / 5 | 45 / 0 | 50 / 5 | 84 / 9 |
| B1 | 7 / 0 | 2 / 0 | 7 / 0 | 7 / 0 |
| B2 | 2 / 34 | 2 / 34 | *(not synced — 0 real B2 docs)* | 21 / 0 |
| C1 | 15 / 10 | 0 / 0 | 15 / 10 | 15 / 10 |
| C2 | 3 / 0 | 3 / 0 | 3 / 0 | 3 / 0 |
| **Total** | **81 / 49** | **56 / 34** | **79 / 15** | **134 / 19** |

**Correction to last session's check, found while re-verifying:** the original naive check (`correctAnswer in options`) produces false positives on ~40 questions repo-wide that use an alternate schema — `options: [{"text": ..., "isCorrect": true/false}]` object array instead of a flat string array. Re-checked properly this time (object-schema questions verified via their `isCorrect` flag matching `correctAnswer`, not just string membership). The numbers above are the corrected, schema-aware counts — they don't exactly match the previously-reported "96 MC + 45 fill" (which was `grammarQuizBank`-only, using the old naive check) because of that methodology fix, not because content changed.

**C1 assets showing 0/0 is not "already fixed":** `app/src/main/assets/` only has `c1_01`–`c1_10` (the original 10 curated topics); every C1 broken question found lives in `c1_11`–`c1_15`, which exist in `content/grammar/` and Firestore but were never bundled into the APK. Same underlying content, just not present in that particular source.

### Conclusion

1. **B2 contamination is real and still present, but confined entirely to `grammarQuizBank`, a Firestore collection with zero live effect on the app.** It was never "resolved" by any commit — it was correctly *contained*: last session's decision to exclude B2 from every sync into `moduleQuizQuestions` (the collection that actually reaches users) is exactly why it never propagated anywhere else. The user's on-device check is correct: B2 has no visible contamination because the only path from `grammarQuizBank` to a real screen is fully severed (confirmed in an earlier session — `ContentRepository.getGrammarQuestionsBySubject()` has zero callers).
2. **Broken `correctAnswer`/`options` questions are real** (not a false-positive artifact) and present in every source checked, at every level except a few clean spots — including `moduleQuizQuestions`, the live collection, for A1/A2/B1/C1/C2 (79 MC + 15 fill there specifically). This is a genuinely open, unresolved content-quality issue distinct from the B2 story, unaffected by anything done this session.
3. **No content was modified this turn.** Both issues remain exactly as open items, now with corrected, source-by-source numbers instead of a single conflated figure. Content repair for either is a separate task pending explicit go-ahead, same as C2 question generation.

---

## 🔧 BROKEN `correctAnswer` FIX EXECUTION (2026-07-09)

Following the diagnosis above, fixed the 79 broken `multiple_choice` + 15 broken `fill_blank` questions confirmed live in `moduleQuizQuestions`, across A1/A2/B1/C1/C2 (B2 out of scope — never synced there, per the diagnosis). `grammarQuizBank` untouched (dead code). No writing/speaking/exams work done. `content/grammar/*.json` fixed first (source of truth), then synced via `scripts/import_and_sync.js`; `app/src/main/assets/*.json` updated too wherever the topic file exists there.

Two corruption patterns emerged: (a) genuinely fixable single-question errors (typo/umlaut-stripped `correctAnswer`, missing option, dual-answer ambiguity, wrong `isCorrect` flag) — fixed minimally, preserving the original question; (b) a systemic **duplicate-placeholder pattern** — the exact same templated question copy-pasted verbatim across 4-5 unrelated topics regardless of subject matter — which can't be "fixed" without inventing content, so those were replaced with new topic-appropriate questions.

| Level | Fixed | Replaced | Total | Commit |
|---|---|---|---|---|
| A1 | 4 | 0 | 4 | `6a07e43` |
| A2 | 45 | 10 | 55 | `6b1df2b` |
| B1 | 2 | 5 | 7 | `2f0c6ac` |
| C1 | 0 | 20 (c1_12–c1_15 only) | 20 | `af415d8` |
| C2 | 3 | 0 | 3 | `0043497` |
| **Total** | **54** | **35** | **89** | |

All fixed/replaced questions marked `reviewed: false` (pending SME review, per `docs/ROLES.md`). Each level verified: schema-aware broken-check clean → dry-run sync → real sync → spot-checked directly in Firestore → `./gradlew assembleDebug` clean → committed → pushed.

**Per-level detail:**
- **A1** (`a1_04`): 4 questions had a correct article form missing from its own `options` — added the missing form.
- **A2** (`a2_01,05,06,07,08,09,10,11,12,13,14,15`): mostly umlaut-stripped/corrupted `correctAnswer` fixes and dual-answer (Turkish/English mix) disambiguation. Replaced 10: `a2_08_q116` (structurally broken, blank-count mismatch) plus the `a2_11/13/14/15` duplicate-placeholder pair (`q018`+`q078` each), which carried a question topically wrong for all four topics.
- **B1** (`b1_04,10,11,12,13,14,15`): 2 minimal fixes (subject-verb agreement, missing option). Replaced 5: `b1_11–b1_15_q014`, the same duplicate placeholder ("Das Buch, ___ ich gestern gekauft habe...") shared across 5 unrelated topics.
- **C1** (`c1_12,13,14,15`): all 20 replaced — same duplicate-placeholder pattern as B1, shared across 5 topics via 2 templates. New topic-appropriate content authored for the 4 topics with legible names (Konjunktionen: geschweige denn/zumal; Kausale/konditionale/konzessive Beziehungen; Textkohärenz: Konnektoren; Stilistische Varianten).
- **C2** (`c2_02,08,09`): 3 minimal fixes — 1 awkward option-text rewrite, 2 umlaut/typo corrections.

**Open blocker — `c1_11` NOT fixed:** 5 broken questions (`q007,020,027,067,087`) share the exact same duplicate-placeholder pattern as `c1_12`–`c1_15`, but `c1_11`'s `topicName` in the data is corrupted (renders as "Sentiments污染物" / similar garbled text), so its actual intended subject matter is unknown. Per "if anything unexpected surfaces, stop and report" — did not guess or fabricate a topic; needs the user to clarify what `c1_11` was supposed to be about before it can be fixed or replaced.

**Pre-existing gap confirmed (not fixed, out of scope):** `a2_11–15`, `b1_11–15`, `c1_11–15` are not bundled in `app/src/main/assets/` at all — only `content/grammar/` and Firestore have them. `content/grammar/` was updated for all of these; nothing to update on the assets side.

**Verified on device: PENDING** (user will re-test).

---

## ✅ CONTENT-REPAIR PHASE CLOSED (2026-07-09)

Three follow-up items fixed after the broken-`correctAnswer` execution above, closing out this phase of work.

**Item 1 — topic descriptions missing past topic 10 (every level except B2).** Root cause: `scripts/import_and_sync.js` wrote the Firestore `topics/{id}` doc with only `{id, level, name, type, questionCount}` — `description`/`tips` were silently dropped on every sync, for every topic, always. Invisible for topics 1–10 (and all of B2/C2) because `SubjectListViewModel.enrichFromAssetJson()` overlays description/tips from the bundled APK asset file when one exists. Topics `_11`–`_15` (A1/A2/B1/C1) were never bundled into `app/src/main/assets/`, so they had nothing to fall back to. Fixed: `import_and_sync.js` now writes description/tips to the `topics` doc; `TopicMeta`/`buildSubjectFromTopicMeta` (`SubjectMapper.kt`) and `FirebaseDataSource.getSubjectsByLevel()` now carry those fields through from Firestore. Backfilled description/tips onto all 83 existing `topics/{id}` docs that already had that content authored in `content/grammar/`, without bumping the `moduleQuizQuestions` version (so it didn't force a full question re-download). Commit `5dddd41`.

**Item 2 — raw options-object artifact reaching the quiz screen.** Root cause: two spots in `LocalQuestionBank.kt` never accounted for the object-array options schema (`[{"text":...,"isCorrect":...}]`, used for some questions to explicitly flag the correct option) — `findQuestionInJson()`'s `JSONArray.getString(index)` and `saveQuestionsJson()`'s unchecked `as? List<String>` cast on Firestore's raw data. Fixed with a schema-aware extractor at both spots. Confirmed affected (identical footprint in content/, assets, and live `moduleQuizQuestions`): only `a2_01` and `a2_02`, 40 questions total. Commit `e8dae51`.

**Item 3 — c1_11 retired.** Investigation (sampling all 100 questions, not just the 5 originally-flagged broken ones) found `c1_11` isn't one coherent topic: it mixes material already covered by `c1_01`/`c1_02`/`c1_03`/`c1_04`/`c1_05`, and repeats the same duplicate-placeholder contamination template found in `c1_12`–`c1_15` beyond the flagged questions (`q080`/`q100`, `q006`/`q086`). Its `topicName` was also corrupted ("Sentiments污染物"). Per user decision: retired rather than relabeled or salvaged. Original 100 questions preserved at `content/grammar/c1_11_retired.json` (never synced). Live `c1_11` is now a 0-question "Wird vorbereitet" placeholder (`topicName: "Thema wird noch festgelegt"`), same mechanism as `c2_13`–`c2_21`. Synced: `moduleQuizQuestions/c1_11` version 9, 0 questions; `topics/c1_11` questionCount 0. Commit `6a05045`.

### Closing verification (re-ran full checks against live Firestore after all three items)

| Level | Broken `correctAnswer`/`options` in `moduleQuizQuestions` | Raw `isCorrect`/`{text=` artifacts in options | Topics 1–10 have description | Topics `_11`–`_15` have description |
|---|---|---|---|---|
| A1 | 0 | 0 | ✅ all 10 | ❌ none (content gap, unauthored) |
| A2 | 0 | 0 | ✅ all 10 | ❌ none (content gap, unauthored) |
| B1 | 0 | 0 | ✅ all 10 | ❌ none (content gap, unauthored) |
| B2 | *(not synced — out of scope, unchanged)* | *(not synced)* | ✅ all 23, incl. `b2_11`–`b2_23` | n/a — `b2_03` alone has no description (pre-existing, unrelated single-topic gap) |
| C1 | 0 | 0 | ✅ all 10 | ❌ `c1_12`–`c1_15` unauthored; `c1_11` retired (0-question placeholder, description intentionally empty) |
| C2 | 0 | 0 | ✅ all 21, incl. `c2_13`–`c2_21` placeholders | n/a — full asset/Firestore coverage, no gap |

### Still open (not fixed this phase, flagged not fabricated)

- **Content gap:** `a1_11–15`, `a2_11–15`, `b1_11–15`, `c1_12–15` (18 topics) and `b2_03` (1 topic) have no `description`/`tips` authored anywhere. They render "No description available" — correct fallback behavior, not a bug. Needs a human content-authoring pass.
- **`c1_11`** now sits as an unplanned "Wird vorbereitet" placeholder with no real topic assigned — needs a curriculum decision (what C1 grammar point should fill that slot) whenever content authoring resumes.
- **B2 `grammarQuizBank` contamination** (documented in the DIAGNOSIS ONLY section above) remains untouched — dead code, zero live effect, unrelated to this phase.
- **Not verified on an actual device/emulator this session** (no Android runtime available in this environment) — `assembleDebug`/`compileDebugKotlin` clean throughout, but a manual on-device smoke test is recommended before relying on any of this in production.

**Content-repair phase closed.** No further content or code work performed beyond what's listed above.

---

---

## 🗑️ CONTENT-INTEGRITY PHASE CLOSED — 20 duplicate topics retired (2026-07-09)

While drafting the 20 missing topic descriptions authorized after the previous session's regression investigation, reading each topic's actual questions (not just the label) surfaced a much bigger problem than a missing description: **most of these topics have no real content behind them at all.**

**Finding:** within each sibling group, almost every question is byte-identical across all topics in the group — only the `topicName` label differs:

| Group | Identical positions across siblings | Genuinely unique content |
|---|---|---|
| `a1_11`–`a1_15` | **100 / 100** | none |
| `a2_11`–`a2_15` | 98 / 100 | only `q018`+`q078` (written in the earlier broken-answer fix) |
| `b1_11`–`b1_15` | 99 / 100 | only `q014` (same) |
| `c1_12`–`c1_15` | 95 / 100 | only `q007/020/027/067/087` (same) |
| `b2_03` | 50 / 50 vs. `b2_02` | none — literal duplicate of an already-authored topic |

Writing polished descriptions for these would have made hollow content look legitimate. Per user decision: **retired all 20**, same mechanism as `c1_11`'s earlier retirement — not a new pattern.

**What changed:**
- `content/grammar/{id}_retired.json` created for all 20 (full original question sets preserved for history, never synced).
- `content/grammar/{id}.json` rewritten as 0-question placeholders. For the 19 topics with a real, legitimate label (`a1_11`–`15`, `a2_11`–`15`, `b1_11`–`15`, `c1_12`–`15`), the real `topicName` was kept — these are reserved curriculum slots pending real content, same as `c2_13`–`c2_21`. For `b2_03` (a true duplicate of `b2_02`, no independent identity) and `c1_11` (corrupted name, retired earlier), a neutral placeholder name ("Thema wird noch festgelegt") was used instead.
- Synced via `scripts/import_and_sync.js` to `moduleQuizQuestions` + `topics` for all except `b2_03`.
- `b2_03` needed different handling: B2 is excluded from `moduleQuizQuestions` sync entirely (pre-existing `grammarQuizBank`-contamination decision), and its question count on-device comes from the bundled `app/src/main/assets/b2_03.json`, not Firestore. Updated that asset file directly to the 0-question placeholder, and wrote `topics/b2_03` via a targeted merge (not the full sync script) to avoid creating a `moduleQuizQuestions` doc for a B2 topic.
- Commits: `213e039` (A1), `0f9669a` (A2), `d73c0b0` (B1), `6c1bcbb` (C1), `4bba110` (B2).

### Final honest topic/question counts per level (verified against live Firestore)

| Level | Real topics (with content) | Placeholder topics ("Wird vorbereitet") | Total live questions |
|---|---|---|---|
| A1 | 10 (`a1_01`–`a1_10`) | 5 (`a1_11`–`a1_15`) | 600 |
| A2 | 10 (`a2_01`–`a2_10`) | 5 (`a2_11`–`a2_15`) | 1,210 |
| B1 | 10 (`b1_01`–`b1_10`) | 5 (`b1_11`–`b1_15`) | 1,001 |
| B2 | 22 (all except `b2_03`) | 1 (`b2_03`) | 2,271 *(not synced to `moduleQuizQuestions` — served from bundled assets only, per the standing B2 exclusion)* |
| C1 | 10 (`c1_01`–`c1_10`) | 5 (`c1_11`–`c1_15`) | 1,028 |
| C2 | 12 (`c2_01`–`c2_12`) | 9 (`c2_13`–`c2_21`) | 1,320 |

Every level now shows its real, content-backed topics plus dimmed coming-soon placeholders — no level has a topic whose label overstates what it actually contains.

### Still open

- **18 reserved curriculum slots** (`a1_11–15`, `a2_11–15`, `b1_11–15`, `c1_12–15`) need real question content authored from scratch — their labels are legitimate, real grammar points, just currently empty. This is a bulk-content-generation task, explicitly out of scope for this phase.
- **`c1_11` and `b2_03`** additionally need a topic *identity* decided (what grammar point should fill that slot) before content authoring can even start.
- **B2 `grammarQuizBank` contamination** (documented earlier) remains untouched — dead code, zero live effect.
- **Not verified on an actual device/emulator this session** — no Android runtime available in this environment. `assembleDebug` clean throughout.

**Content-integrity phase closed.** No further content or code work performed beyond what's listed above.

---

_Last updated: 2026-07-09_