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

### c2_12 Modalpartikeln im gehobenen Sprachgebrauch — Questions Added 🔄
| Batch | Questions | Commit |
|-------|-----------|--------|
| q001–q020 | 20 (ja/doch/eben/halt/wohl/schon/ruhig/mal/denn/aber, register awareness) | `scripts/create_c2_12.py` |

**c2_12 Total: 20 questions (target: 100)** 🔄 In Progress
**Also fixed:** `SubjectListViewModel.kt` `getC2Subjects()` was missing both `c2_11` and `c2_12` entries — c2_11 (100 questions, already existed) was invisible in the app before this fix.

---

_Last updated: 2026-07-06_