# B2 Deutsch App — PROJECT STATUS

**Last Updated:** 2026-04-28
**GitHub:** https://github.com/halilmek/b2-deutsch-app
**Firebase:** b2-deutsch-app

---

## ✅ WHAT WE COMPLETED (2026-04-28)

### Bug Fixes

| Issue | Fix |
|-------|-----|
| **Topic ID mismatch** | Added missing `b2_02` to SubjectListViewModel — all topics now load correct JSON files |
| **Topic 2 showing Topic 1 questions** | Fixed by aligning subjectId ordering with JSON file names |
| **SharedPreferences corruption** | Bumped to `quiz_progress_prefs_v6` + `INIT_VERSION=2` — forces clean init on update |
| **Topic 3 quizCount=10** | Updated to `quizCount=16` (160 questions ÷ 10 per quiz = 16 sessions) |
| **Missing Context import** | Added `android.content.Context` and `SharedPreferences` imports to LocalQuestionBank.kt |

### New Content (Topic 3 — Zeitformen der Vergangenheit)

**b2_04.json now has 160 real questions:**
- q001–q060: Perfekt (haben/sein, trennbar/untrennbar verbs)
- q061–q080: Perfekt gemischte Übungen (reflexive, strong verbs)
- q081–q120: Präteritum (strong & weak verbs)
- q121–q160: Plusquamperfekt (Nachdem/Because/Obwohl clauses)
- Topic name: "Zeitformen der Vergangenheit (Perfekt, Präteritum, Plusquamperfekt)"

### New Files Created

| File | Purpose |
|------|---------|
| `scripts/firestore_import_topic3.js` | One-time import of b2_04 questions to Firestore |
| `scripts/import_and_sync.js` | **Option A** — push JSON to BOTH GitHub assets AND Firestore in one command |
| `data/sync/FirebaseSyncService.kt` | App-side sync: checks Firestore once per week, downloads new content |
| `data/local/LocalQuestionBank.kt` | Updated with `updateTopicFromFirebase()` for sync support |

### Firebase Sync Architecture (Admin-Push Model)

```
ADMIN SIDE                              APP SIDE
─────────────────────────────────      ─────────────────────────────────
You add questions to JSON
       ↓
node scripts/import_and_sync.js        ← You run this
       ↓
Push to GitHub (assets/)                ← Version in assets increments
Push to Firestore (moduleQuizQuestions) ← version: N → N+1
       ↓                                        ↓
Content updated in Firestore           User opens app
                                           ↓
                                    FirebaseSyncService checks:
                                    "last sync > 7 days ago?"
                                           ↓
                                     YES → queries Firestore for version > currentVersion
                                           ↓
                                     Downloads new questions → saves to SharedPreferences
                                           ↓
                                     NO → skip, use cached local data
                                           ↓
                                    App goes OFFLINE — no Firebase calls during quiz
```

**Sync Rules:**
- Firebase only called on app launch (once per week maximum)
- All quiz content served from local SharedPreferences (offline-first)
- You control when content updates — run `import_and_sync.js` and users get it within 7 days

---

## 📊 CURRENT CONTENT STATE

### Real Content (Manually Created)
| subjectId | topicName | Questions | QuizCount | File | Status |
|-----------|-----------|-----------|-----------|------|--------|
| b2_01 | Konnektoren | 96 | 10 | b2_01.json | ✅ |
| b2_02 | Verben und Ergänzungen | 50 | 5 | b2_02.json | ✅ |
| b2_03 | Verben und Ergänzungen | 50 | 5 | b2_03.json | ⚠️ Duplicate of b2_02 |
| b2_04 | Zeitformen der Vergangenheit | 160 | **16** | b2_04.json | ✅ |
| b2_05–b2_23 | Placeholders | 100 each | 10 | b2_05.json...b2_23.json | ❌ Wrong content |

### Topic Quiz Counts (SubjectListViewModel)
| Topic | subjectId | quizCount | totalQuestions ÷ 10 |
|------|-----------|-----------|---------------------|
| 1. Konnektoren | b2_01 | 10 | 96 ÷ 10 = 9.6 → 10 ✅ |
| 2. Verben und Ergänzungen | b2_02 | 5 | 50 ÷ 10 = 5 ✅ |
| 3. Zeitformen | b2_04 | **16** | 160 ÷ 10 = 16 ✅ |
| 4. Zeitformen der Zukunft | b2_05 | 10 | (placeholder) |

---

## 🚀 HOW TO PUSH NEW QUESTIONS

### Option A: Sync Single Topic
```bash
cd /Users/halilozturk/b2-deutsch-app

# Set credentials
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/firebase-key.json

# Push Topic 3 (b2_04) to GitHub + Firestore
node scripts/import_and_sync.js b2_04

# Push multiple topics
node scripts/import_and_sync.js b2_04 b2_05 b2_06

# Push ALL topics
node scripts/import_and_sync.js
```

### What Happens
1. Reads `app/src/main/assets/b2_XX.json`
2. Increments `version` field in Firestore (v1 → v2 → v3...)
3. Pushes updated JSON to GitHub assets
4. App detects newer version → syncs on next open

### Firebase Document Structure
```
moduleQuizQuestions/b2_04/
  id: "b2_04"
  subjectId: "b2_04"
  module: "B2"
  topicName: "Zeitformen der Vergangenheit"
  totalQuestions: 160
  version: 3  ← increments each time you push
  questions: [array of 160 question objects]
  updatedAt: Timestamp

moduleQuizQuestions/b2_04_q001  ← individual doc
moduleQuizQuestions/b2_04_q002
...
moduleQuizQuestions/b2_04_q160
```

---

## 📋 REMAINING WORK

### Must Fix
- [ ] b2_03.json is duplicate of b2_02 — delete or replace with new content
- [ ] b2_05–b2_23 have wrong placeholder content (Konnektor questions instead of real topics)

### Should Do
- [ ] Add Firebase `version` field support to `import_and_sync.js` — currently creates/updates
- [ ] Test FirebaseSyncService end-to-end after publishing Topic 4+ content
- [ ] Add pull-to-refresh in app for manual sync trigger

### Future
- [ ] Topic 4 (Zeitformen der Zukunft) — need real questions
- [ ] AI Speaking Partner integration
- [ ] AI Writing Evaluation
- [ ] Peer Speaking Exams

---

## 🏗️ ARCHITECTURE SUMMARY

### Question Loading Flow (OFFLINE)
```
User taps Topic 3 → QuizViewModel.startQuiz("b2_04")
  → LocalQuestionBank.getNextQuiz(context, "b2_04")
    → Reads from SharedPreferences (active/pool)
      → Question IDs → b2_04.json for details
```

### Question Sync Flow (WEEKLY)
```
App launch → FirebaseSyncService.syncIfNeeded()
  → Check: last sync > 7 days ago?
    → NO: skip
    → YES: query Firestore for version > currentVersion
      → Download new questions
      → LocalQuestionBank.updateTopicFromFirebase()
      → Save to SharedPreferences
      → Update last_sync_timestamp
```

### SharedPreferences (v6) Keys
```
quiz_progress_prefs_v6:
  init_version = 2
  active_b2_04 = ["b2_04_q001", "b2_04_q002", ...]
  passive_b2_04 = ["b2_04_q005", ...]  (solved)
  count_b2_04 = 160

firebase_sync_prefs:
  last_sync_timestamp = 1714300800000
  sync_version = 1
```

---

## 🔑 KEY FILES

| File | Purpose |
|------|---------|
| `app/src/main/assets/b2_01.json` | Topic 1: Konnektoren (96 Q) |
| `app/src/main/assets/b2_02.json` | Topic 2: Verben und Ergänzungen (50 Q) |
| `app/src/main/assets/b2_04.json` | Topic 3: Zeitformen (160 Q) ✅ MAIN FOCUS |
| `scripts/import_and_sync.js` | **Push to GitHub + Firestore** (Option A) |
| `scripts/firestore_import_topic3.js` | One-time Firestore import |
| `data/sync/FirebaseSyncService.kt` | Weekly sync logic (app-side) |
| `data/local/LocalQuestionBank.kt` | Question bank, progress tracking |
| `ui/subject/SubjectListViewModel.kt` | Defines all 23 B2 subjects with quizCount |
| `B2DeutschApp.kt` | App init — calls FirebaseSyncService on launch |

---

## 🧪 TESTING CHECKLIST

After `import_and_sync.js`:
- [ ] `git pull` on Mac → rebuild APK
- [ ] Uninstall old APK → fresh install
- [ ] Topic 3 should show: 16 quizzes available, 160 questions
- [ ] Check Firestore: `moduleQuizQuestions/b2_04` has `version: N`
- [ ] Next push to same topic → version increments → users get update within 7 days

---

_Last updated: 2026-04-28 20:40 UTC_