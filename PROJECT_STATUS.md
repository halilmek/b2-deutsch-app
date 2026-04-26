# B2 Deutsch App — PROJECT STATUS

**Last Updated:** 2026-04-26
**GitHub:** https://github.com/halilmek/b2-deutsch-app
**Firebase Project:** b2-deutsch-app (project_number: 419122108874)
**Firebase Storage:** b2-deutsch-app.firebasestorage.app

---

## 🟢 BUILDING RIGHT NOW

### B2 Module — Konnektoren Questions (Topic 1)

**File:** `content/reading/b2_konnektoren_questions.md`

**96 questions prepared** (12 per konnektor):
| Konnektor | Questions | Ready? |
|-----------|-----------|--------|
| als | 12 | ✅ Ready — needs review |
| bevor | 12 | ✅ Ready — needs review |
| bis | 12 | ✅ Ready — needs review |
| seitdem | 12 | ✅ Ready — needs review |
| während | 12 | ✅ Ready — needs review |
| wenn | 12 | ✅ Ready — needs review |
| sobbing | 12 | ✅ Ready — needs review |
| solange | 12 | ✅ Ready — needs review |

**Question format:**
```
id: "b2_01_als_q001"
module: "B2"
topicNumber: "1. Topic"
topicName: "Konnektoren"
konnektor: "als"
questionText: "___ ich in Deutschland ankam, konnte ich kein Deutsch."
options: ["Wenn", "Als", "Während", "Bevor"]
correctAnswer: "Als"
explanation: "\"Als\" wird für einmalige Situationen in der Vergangenheit verwendet..."
difficulty: "easy"
level: "B2"
```

**Topics 2–23:** Pending — need to be generated with same structure

---

## ✅ COMPLETED

### 1. LocalQuestionBank — Offline 100 Q/Topic System
- **File:** `app/src/main/java/com/b2deutsch/app/data/local/LocalQuestionBank.kt`
- Questions loaded from `app/src/main/assets/b2_questions.json` (offline)
- Active/Passive tracking via SharedPreferences
- 10 random questions per quiz from active pool
- Loop reset after 90+ solved
- `getAllTopicIds(level)` — returns topic IDs for any level

### 2. QuizViewModel — Updated
- Uses LocalQuestionBank instead of Firestore for quiz questions
- `startQuiz()`, `startNextQuiz()`, `retryQuiz()`, `resetTopicProgress()`
- `loadQuizzes(level)` — loads topic list for QuizzesFragment
- `isComplete`, `quizMessage`, `errorMessage` LiveData

### 3. Result Screens — Updated
- `fragment_quiz_result.xml`: progress bar, completion banner
- `fragment_subject_result.xml`: Next Quiz button, progress display
- `QuizResultFragment.kt` + `SubjectResultFragment.kt`: observe new LiveData

### 4. QuestionResult Data Class
- Added to `Quiz.kt` — fixes QuizResultAdapter compile error

### 5. Missing Colors Fixed
- `colors.xml`: added `orange_100`, `orange_800`, `green_700`

### 6. 100 Q/Topic Generator (All Levels)
- **File:** `gen_all_levels_100q.py`
- 83 topics × 100 questions = **8,300 total**
- A1: 15 topics, A2: 15, B1: 15, B2: 23, C1: 15
- **Not yet pushed to Firebase** (API key restricted)

### 7. Firebase Data Structure (Two Collections)
```
grammarQuizBank/      — General grammar (all levels, all types)
moduleQuizQuestions/  — B2 exam module (konnektor-specific, MCQ only)
```

---

## 🔴 BLOCKED / NEEDS ATTENTION

### Firebase Import — BLOCKED
- All API keys are Android/JS-client restricted
- Cannot write to Firestore from server script
- **Solution options:**
  1. Set Firestore rules to `allow read, write: if true` → import from server
  2. Create unrestricted server API key → import from server
  3. Run import from MacBook with Firebase CLI

### B2 Topics 2–23 Questions — PENDING
- Topic 1 (Konnektoren) 96 Q: **ready, needs review**
- Topics 2–23: **not started**
- Need same structure: module / topicNumber / topicName / konnektor

---

## 📋 WHAT NEEDS TO BE DONE

### Immediately:
- [ ] **REVIEW Topic 1 questions** (96 konnektor questions above)
- [ ] **PUSH Topic 1 to Firebase** (`moduleQuizQuestions` collection)
- [ ] **DELETE old `grammarQuizBank` B2 module questions** from Firebase
- [ ] **Generate Topics 2–23** with same konnektor-specific structure

### Short-term:
- [ ] **Push Topics 2–23** to `moduleQuizQuestions` collection (one by one for review)
- [ ] **Build module quiz UI** in Android app to use `moduleQuizQuestions`
- [ ] **Separate navigation**: "Module Quiz" vs "General Quiz"

### Medium-term:
- [ ] **A1–C1 module questions** — same structure
- [ ] **Reading passages** — AI-generated
- [ ] **Vocabulary flashcards**

---

## 📁 KEY FILES

| File | Purpose |
|------|---------|
| `app/src/main/assets/b2_questions.json` | 8,300 general grammar questions (offline bundle) |
| `content/reading/all_levels_100_questions.json` | Source JSON for all levels |
| `content/reading/b2_konnektoren_questions.md` | **Current work — Topic 1 questions (96 Q)** |
| `content/reading/gen_all_levels_100q.py` | 100Q/topic generator script |
| `content/reading/firebase_import_rest.js` | Firebase import script (needs server API key) |
| `app/src/main/java/com/b2deutsch/app/data/local/LocalQuestionBank.kt` | Offline question bank + progress tracking |
| `app/src/main/java/com/b2deutsch/app/ui/quiz/QuizViewModel.kt` | Quiz logic |

---

## 📊 FIREBASE COLLECTIONS

### grammarQuizBank (General Grammar)
- **8,300 questions** — A1 (1,500), A2 (1,500), B1 (1,500), B2 (2,300), C1 (1,500)
- 83 topics × 100 questions
- Fields: id, subjectId, type, questionText, options, correctAnswer, difficulty, topicName, level
- **NOT yet pushed to Firebase** (blocked by API key)

### moduleQuizQuestions (B2 Exam Module)
- **96 questions** (Topic 1 only — als, bevor, bis, seitdem, während, wenn, sobbing, solange)
- Fields: id, module, topicNumber, topicName, konnektor, questionText, options, correctAnswer, explanation, difficulty, level
- **Ready to push** — needs user review first

---

## 🗂️ MODULE QUIZ DATA MODEL

```kotlin
// moduleQuizQuestions collection schema
data class ModuleQuestion(
    val id: String,           // "b2_01_als_q001"
    val module: String,       // "B2"
    val topicNumber: String,  // "1. Topic"
    val topicName: String,    // "Konnektoren"
    val konnektor: String,    // "als"
    val questionText: String,
    val options: List<String>,
    val correctAnswer: String,
    val explanation: String,
    val difficulty: String,    // "easy" | "medium" | "hard"
    val level: String        // "B2"
)
```

---

## 📅 RECENT COMMITS

| Date | Commit | Description |
|------|--------|-------------|
| 2026-04-26 | `4ede3f7` | feat: 100-questions-per-topic offline quiz system |
| 2026-04-26 | `3a1ab66` | feat: add A1-A2-B1-C1 question banks + all-levels generator |
| 2026-04-26 | `6cfb314` | fix: add missing color resources |
| 2026-04-26 | `8c6eaaa` | fix: correct QuestionResult import in QuizResultAdapter |
| 2026-04-26 | `0c6a4e8` | fix: add loadQuizzes+quizzes to QuizViewModel |

---

_Last updated: 2026-04-26 21:17 UTC_
