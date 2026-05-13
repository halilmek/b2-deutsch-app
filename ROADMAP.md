# B2 Deutsch App — Roadmap

## Recently Done
- [x] **A1 expanded: 20 → 30 questions per topic** (2026-05-13) — Q21-Q30 added to all 10 topics; commit `308bbe8`; total A1 = 300 questions
- [x] Fix duplicate getA2Subjects/getA1Subjects function definitions (lines 1011/1124, 223 lines removed)
- [x] Fix leftover blank lines after duplicate removal
- [x] Fix LocalQuestionBank to initialize all level topic IDs (A1-C2, not just B2)
- [x] Fix resetAllTopics to cover all levels A1-C2
- [x] Add `level` argument to SubjectDetailFragment navigation (bug: "app shows B2 topics when user returns to A1 list")
- [x] Add comprehensive logging to SubjectDetailFragment and SubjectListViewModel
- [x] Add tips + descriptions to all A1 topics in SubjectListViewModel.kt (with `quizCount = 5`)
- [x] Add tips + descriptions to all A2, B1, C1, C2 topics in SubjectListViewModel.kt
- [x] **A1 JSON questions fully replaced** (10 topics × 10 questions = 100 total) with user's new question set; answers matched to user's provided answer key; topics: Verben konjugieren, Nomen+Artikel, Praesens, Akkusativ, Dativ, Praepositionen, Verben mit Praepositionen, Perfekt, Modalverben, Saetze+Wortstellung; pushed in `fbf0105`
- [x] A2 JSON question files created
- [x] B1 JSON question files created
- [x] C1 JSON question files created
- [x] C2 JSON question files created

## Known Issues / Debugging

### Issue: Descriptions and tips empty on A1 topic detail screen
**Symptom:** User sees quiz count (5) but no description and no tips.
**Root cause identified:** SubjectDetailFragment was calling `loadSubjectsForLevel("B2")` by default instead of the actual level. Now fixed with:
1. Added `level` argument to SubjectDetailFragment navigation
2. SubjectDetailFragment now receives and uses the correct level

**Debug logs to check (logcat filter: SubjectDetail | SubjectListVM):**
- `📥 Arguments — subjectId=..., subjectName=..., level=...` — did we get the right level?
- `📤 loadSubjectsForLevel(A1) for subjectId=...` — correct level called?
- `✅ MATCHED subjectId=... | description len=... | tips=...` — did we find the right subject?
- `📝 description[0..80]: ...` — is description populated?
- `💡 tips count: ...` — are tips populated?

### Issue: B2 topics shown instead of A1 after returning to topic list
**Root cause:** The SubjectListViewModel uses a shared LiveData `_subjects`. When user navigates back, the old B2 data might still be cached.
**Fix applied:**
1. Pass `level` correctly through navigation
2. SubjectDetailFragment now calls `loadSubjectsForLevel(A1)` instead of defaulting to B2

## Pending Fixes
- b2_15: missing description
- b2_16: topicName wrong + missing description
- b2_02: Has questions in JSON but no topic entry in app

## Content Sync Status

## Content Sync Status

### Firebase (Firestore)
- b2_01 to b2_23: Synced ✅
- a1_01 to a1_10: ⚠️ Pending sync — 300 questions ready (expanded 2026-05-13)
- a2_01 to a2_10: NOT YET synced ⚠️
- b1_01 to b1_10: NOT YET synced ⚠️
- c1_01 to c1_10: NOT YET synced ⚠️
- c2_01 to c2_10: NOT YET synced ⚠️

### Local JSON files (assets/)
- a1_01.json ✅ (50 questions)
- a1_02.json ✅ (50 questions)
- a1_03.json ✅ (49 questions)
- a1_04.json ✅ (49 questions)
- a1_05.json ✅ (49 questions)
- a1_06.json ✅ (48 questions)
- a1_07.json ✅ (50 questions)
- a1_08.json ✅ (50 questions)
- a1_09.json ✅ (50 questions)
- a1_10.json ✅ (50 questions)
- a2_01.json to a2_10.json ✅
- b1_01.json to b1_10.json ✅
- b2_01.json to b2_23.json ✅
- c1_01.json to c1_10.json ✅
- c2_01.json to c2_10.json ✅

## Next Steps
1. **Sync A1 to Firebase** (a1_01–a1_10, 300 questions) — run from local machine
2. **Halil pulls latest, clears app data, rebuilds**
3. **Check logcat for SubjectDetail | SubjectListVM tags** to verify level is passed correctly
4. **Sync A2-B1-C1-C2 JSON to Firestore** once questions are ready
5. **Fix b2_15, b2_16, b2_02** pending topics

## Build & Sync Commands

```bash
# Pull latest
cd /Users/halilozturk/b2-deutsch-app
git pull origin main

# Sync A1 questions to Firestore
export GOOGLE_APPLICATION_CREDENTIALS="/Users/halilozturk/Documents/b2-deutsch-app-firebase-adminsdk-fbsvc-4aa25c0ca2.json"
node scripts/import_and_sync.js a1_01 a1_02 a1_03 a1_04 a1_05 a1_06 a1_07 a1_08 a1_09 a1_10

# Sync A2 questions
node scripts/import_and_sync.js a2_01 a2_02 a2_03 a2_04 a2_05 a2_06 a2_07 a2_08 a2_09 a2_10
```

## Technical Notes

### Navigation bug (fixed)
- SubjectDetailFragment received `level` as argument but never used it — always passed "B2" to ViewModel
- Fixed: `loadSubject()` now uses `subjectLevel` field (set from navigation argument)

### LocalQuestionBank init bug (fixed)
- `initializeFromAssets()` only called `getAllB2TopicIds()` — A1/A2/B1/C1/C2 JSON files were never loaded into the question pool
- Fixed: now initializes all level topic IDs (A1-C2)

### Duplicate function definitions (fixed)
- getA2Subjects() and getA1Subjects() were each defined TWICE
- Second copy was leftover from the previous A1/A2 expansion script
- Fixed: removed duplicate function blocks (223 lines removed)