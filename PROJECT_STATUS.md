# B2 Deutsch App — PROJECT STATUS

**Last Updated:** 2026-04-28
**GitHub:** https://github.com/halilmek/b2-deutsch-app
**Firebase:** b2-deutsch-app

---

## 🔧 WHAT WE FIXED (2026-04-28)

### Bug: Topic ID Mismatch — Topics Showing Wrong Questions

**Problem:** Topic 2 in the app ("Verben und Ergänzungen") was loading Topic 1 (Konnektoren) questions. Topic 3 was loading Topic 2 questions, etc.

**Root Cause:** The app code (SubjectListViewModel) had a numbering gap — it jumped from `b2_01` → `b2_03`, skipping `b2_02`. The JSON files were named sequentially starting from `b2_01`, so:
- `b2_01.json` (file) = Topic 1 Konnektoren ✅
- `b2_02.json` (file) = Topic 2 Verben ✅
- But the app expected: `b2_03` = Topic 2, `b2_04` = Topic 3 (because `b2_02` didn't exist in code)

This caused every topic to load from the wrong file (always shifted by 1 down from where it should be).

**Solution (Option A):** Added the missing `b2_02` subject entry to SubjectListViewModel, shifting all subsequent topic IDs by +1.

### Changes Made

**1. SubjectListViewModel.kt** — Added `b2_02` (Verben und Ergänzungen):
```
Before: b2_01, b2_03, b2_04, b2_05 ... b2_23
After:  b2_01, b2_02, b2_04, b2_05 ... b2_23
```

**2. JSON Files** — All 23 files verified and aligned to subject ID mapping:
| File | subjectId | topicName | Questions | Status |
|------|-----------|-----------|-----------|--------|
| b2_01.json | b2_01 | Konnektoren | 96 | ✅ Real content |
| b2_02.json | b2_02 | Verben und Ergänzungen | 50 | ✅ Real content |
| b2_03.json | b2_03 | Verben und Ergänzungen | 50 | ⚠️ Duplicate of b2_02 |
| b2_04.json | b2_04 | Zeitformen der Zukunft | 100 | ⚠️ Placeholder (wrong first Q) |
| b2_05.json | b2_05 | Futur mit werden | 100 | ⚠️ Placeholder |
| ... | ... | ... | 100 | ⚠️ Placeholders |
| b2_23.json | b2_23 | Reserve | 100 | ⚠️ Placeholder |

**3. LocalQuestionBank.kt** — Updated:
- Uses per-topic JSON files (`{subjectId}.json`) instead of single `b2_questions.json`
- Uses `quiz_progress_prefs_v6` (forces clean init on update)
- `INIT_VERSION = 2` — version check clears old corrupt SharedPreferences
- Debug logs added with tag `LQB`

**4. gradle.properties** — kapt JVM args for JDK 21 compatibility:
```
kapt.use.worker.api=false
org.gradle.jvmargs=--add-opens=jdk.compiler/com.sun.tools.javac.main=ALL-UNNAMED (and 4 more)
```

---

## 📊 CURRENT CONTENT STATE

### ✅ Topics with Real Content (manually created / verified)
| subjectId | topicName | Questions | Source |
|-----------|-----------|-----------|--------|
| b2_01 | Konnektoren | 96 | Real (12 per konnektor: als, bevor, bis, seitdem, während, wenn, sobbing, solange) |
| b2_02 | Verben und Ergänzungen | 50 | Real (fill-in-blank: mich/mir, mich/mir, auf/an, etc.) |

### ⚠️ Topics with Placeholder Content (need real questions)
| subjectId | topicName | Current State |
|-----------|-----------|---------------|
| b2_03 | Verben und Ergänzungen | ❌ Duplicate of b2_02 — same 50 questions |
| b2_04 | Zeitformen der Zukunft | ❌ All questions show Konnektor text instead of real content |
| b2_05 | Futur mit werden | ❌ Placeholder |
| b2_06 | Angaben im Satz | ❌ Placeholder |
| b2_07 | Angaben im Satz | ❌ Duplicate placeholder |
| b2_08–b2_23 | Various | ❌ All placeholders (wrong content) |

**Note:** Topics 3–23 all contain the WRONG content — they show Konnektor questions instead of their actual topic content. This is because the original `b2_questions.json` was corrupted (Topics 3–23 all contained Topic 1 duplicate content).

### 📋 Remaining Work
1. **Fill b2_03.json** with proper Verben questions (or delete it — it's a duplicate of b2_02)
2. **Fill b2_04–b2_23** with real grammar questions per topic
3. **Delete b2_questions.json** (no longer used, removed locally)

---

## 🏗️ ARCHITECTURE SUMMARY

### Question Loading Flow
```
User taps Topic 2 (Verben) in SubjectListFragment
  → QuizViewModel.startQuiz("b2_02")
    → LocalQuestionBank.getNextQuiz(context, "b2_02")
      → Opens b2_02.json from assets
      → Returns 10 questions from ACTIVE pool (from SharedPreferences)
```

### Per-Topic JSON File Structure
```json
{
  "version": "1.0",
  "subjectId": "b2_02",
  "topicName": "Verben und Ergänzungen",
  "totalQuestions": 50,
  "questions": [
    {
      "id": "b2_02_q001",
      "subjectId": "b2_02",
      "type": "fill_blank",
      "questionText": "Ich muss ___ beeilen, sonst verpasse ich den Zug.",
      "options": ["mich", "mir", "sich", "dir"],
      "correctAnswer": "mir",
      "explanation": "'sich beeilen' is reflexive...",
      "difficulty": "medium",
      "topicName": "Verben und Ergänzungen"
    }
  ]
}
```

### SharedPreferences (v6) Key Structure
```
quiz_progress_prefs_v6:
  init_version = 2 (forces clean init on version change)
  active_b2_01 = ["b2_01_q001", "b2_01_q002", ...]  (unsolved question IDs)
  passive_b2_01 = ["b2_01_q005", ...]  (solved question IDs)
  count_b2_01 = 96  (total questions for this topic)
  active_b2_02 = ["b2_02_q001", ...]
  passive_b2_02 = []
  count_b2_02 = 50
  ...
```

---

## 📁 KEY FILES

| File | Purpose |
|------|---------|
| `app/src/main/assets/b2_01.json` | Topic 1: Konnektoren (96 Q) — REAL ✅ |
| `app/src/main/assets/b2_02.json` | Topic 2: Verben und Ergänzungen (50 Q) — REAL ✅ |
| `app/src/main/assets/b2_03.json` | Topic 3: Verben und Ergänzungen (50 Q) — DUPLICATE ⚠️ |
| `app/src/main/assets/b2_04–b2_23.json` | Placeholder topics (100 Q each) — WRONG ❌ |
| `app/src/main/assets/b2_questions.json` | OLD — deleted, no longer used |
| `LocalQuestionBank.kt` | Reads per-topic JSON, manages progress via SharedPreferences |
| `SubjectListViewModel.kt` | Defines all 23 B2 subjects with display order |
| `QuizViewModel.kt` | Manages quiz session, calls LocalQuestionBank |
| `gradle.properties` | JDK 21 kapt workaround, build config |

---

## 🧪 TESTING CHECKLIST

After each code change:
- [ ] Build APK (`./gradlew assembleRelease`)
- [ ] Uninstall old APK from test device (SharedPreferences is versioned but clean slate is safer)
- [ ] Install new APK, create fresh account
- [ ] Topic 1 (Konnektoren): verify 10 Konnektor questions appear
- [ ] Topic 2 (Verben und Ergänzungen): verify 10 Verb questions appear, NOT Konnektor
- [ ] Topic 3: verify correct content per topic
- [ ] Log check: `adb logcat | grep -E "LQB|QuizActive"` should show `subjectId=b2_02` for Topic 2

---

_Last updated: 2026-04-28 16:20 UTC_