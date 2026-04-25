# B2 Deutsch App — Session Guidance
## Developer Notes & Roadmap

**Last Updated:** 2026-04-25 14:00 UTC
**Session History:** PART 1 (Apr 25) + PART 2 (Apr 24)
**Append after every session using format: `## Session: [Date] — [Summary of work]`**

---

## 1. WHAT WE ARE BUILDING

### App Overview
**Name:** B2 Deutsch — Prüfungsvorbereitung
**Platform:** Android (Kotlin + Jetpack Compose)
**Package:** `com.b2deutsch.app`
**Firebase Project:** `b2-deutsch-app` (project_number: 419122108874)
**Repository:** https://github.com/halilmek/b2-deutsch-app

### Core Purpose
German language exam prep app for ALL CEFR levels (A1, A2, B1, B2, C1) — with AI-generated content and AI-powered practice features.

### Architecture
- Level-agnostic: same app supports all CEFR levels
- Level is a **filter parameter** in all Firestore queries
- Adding new levels = adding content only, no code changes
- Content from: 3rd party apps (Goethe, ÖSD, DW) + AI generation (MiniMax)

### Pricing Tiers
| Tier | Price | AI Speaking | Peer Exams | Writing Evals | Levels |
|------|-------|------------|------------|--------------|--------|
| Free | €0 | 10 min/day | 1/week (4/mo) | 1/week (4/mo) | B2 only |
| Standard | €5.99/mo | 20 min/day | 1/week (4/mo) | 5/month | B2 only |
| Premium | €9.99/mo | Unlimited | 2/week (8/mo) | 15/month | A1–C1 |

---

## 2. WHAT WE HAVE DONE

### ✅ Project Infrastructure
- [x] Android project scaffolded (Kotlin + Jetpack Compose)
- [x] Firebase project configured (Auth + Firestore + Storage)
- [x] GitHub repository created: `halilmek/b2-deutsch-app`
- [x] `google-services.json` present at `app/google-services.json`
- [x] Hilt dependency injection setup (AppModule.kt)

### ✅ Authentication (Phase 3)
- [x] LoginFragment with email/password
- [x] SignUpFragment with display name
- [x] AuthViewModel with Firebase Auth integration
- [x] Navigation: login → home flow
- [x] Logout functionality

### ✅ Home Screen (Phase 4)
- [x] HomeFragment with welcome message
- [x] Level selection grid (A1, A2, B1, B2, C1)
- [x] LevelAdapter with tap handling
- [x] Navigation buttons: Lessons, Quizzes, Vocabulary, Writing, Speaking
- [x] User progress display (streak, lessons completed)
- [x] HomeViewModel with data loading
- [x] Level selection scrolls to feature buttons (cosmetic fix)

### ✅ Lessons Module (Phase 4)
- [x] LessonsFragment with RecyclerView
- [x] LessonAdapter
- [x] LessonDetailFragment
- [x] ContentRepository for loading lessons from Firestore
- [x] LessonsViewModel

### ✅ Quiz Module (Phase 5)
- [x] QuizzesFragment
- [x] QuizActiveFragment (question display)
- [x] QuizResultFragment (score, pass/fail)
- [x] QuizViewModel
- [x] QuizAdapter
- [x] Question types: Multiple Choice, True/False, Fill-in-Blank
- [x] Content loaded from Firestore (filtered by level)
- [x] Sample quizzes with fallback when Firestore is empty

### ✅ Subject → Quiz → Results Flow (NEW!)
- [x] SubjectListFragment — shows all subjects for selected level
- [x] SubjectAdapter — subject cards with category badges
- [x] SubjectDetailFragment — explanation + tips + Start Quiz button
- [x] SubjectResultFragment — detailed results with explanations
- [x] QuizResultAdapter — per-question result display
- [x] B2 Default Subjects (in SubjectListViewModel):
  - Grammatik: Konjunktiv II, Passiv, Nebensätze, Nominalisierung
  - Lesen: Beruf, Gesundheit, Umwelt, Gesellschaft, Medien, Bildung
  - Wortschatz: Beruf-Vokabeln, Umwelt-Vokabeln
- [x] SubjectProgress & LevelProgress models
- [x] Category filter chips (Alle, Grammatik, Lesen, Wortschatz)

### ✅ Vocabulary Module (Phase 6)
- [x] VocabularyFragment (placeholder UI ready for flashcards)
- [x] VocabularyFragmentViewModel

### ✅ Writing & Speaking (Phase 9+)
- [x] WritingFragment (placeholder for AI writing evaluation)
- [x] SpeakingFragment (placeholder for AI speaking practice)
- [x] WritingRepository, SpeakingRepository

### ✅ Navigation System
- [x] nav_graph.xml with all fragment destinations (13 destinations)
- [x] Navigation actions between all screens
- [x] Start destination: loginFragment

### ✅ Data Layer
- [x] All model classes: User, Level, Lesson, Quiz, Vocabulary, Writing, Speaking, Reading
- [x] Repository layer: ContentRepository, UserRepository
- [x] FirebaseDataSource for Firestore access
- [x] Constants.kt with categories and quiz types

### ✅ B2 Reading Comprehension Content

**Data Models:**
- [x] `B2ReadingModels.kt` — ReadingText, QuestionMC/TF/FIB, VocabEntry
- [x] `Reading.kt` — ReadingPassage, ReadingQuestion, ListeningExercise

**12 B2 Topics (GoetheInstitut curriculum):**
```
1. 💼 Beruf und Arbeitswelt          7. ✈️ Reisen und Tourismus
2. 🏥 Gesundheit und Medizin          8. 📈 Wirtschaft und Finanzen
3. 🌍 Umwelt und Natur               9. 🎭 Kultur und Freizeit
4. 👥 Gesellschaft und Soziales      10. 🔬 Wissenschaft und Technik
5. 📱 Medien und Kommunikation       11. 🏛️ Politik und Zeitgeschehen
6. 🎓 Bildung und Erziehung          12. 💬 Beziehungen
```

**Content Status:**
| Topic | Content | Texts | Questions | Status |
|-------|---------|-------|-----------|--------|
| 1 | Beruf und Arbeitswelt | 10 | 50 | ✅ Complete |
| 2 | Gesundheit und Medizin | 10 | 50 | ✅ Complete |
| 3 | Umwelt und Natur | 10 | 50 | ✅ Complete |
| 4 | Gesellschaft und Soziales | 10 | 50 | ✅ Complete |
| 5 | Medien und Kommunikation | 1 | 5 | ⚠️ Sample only |
| 6–12 | Remaining topics | 0 | 0 | ❌ TODO |

**Per Text:**
- 280–370 B2-level German words
- 5 questions: 3× Multiple Choice + 1× True/False + 1× Fill-in-Blank
- 8 vocabulary items (German / English / Turkish)
- 1 exam tip
- Real source URL reference

**Per Question:**
- Correct answer + full explanation
- Easy-to-remember format

### ✅ Firebase Import
- [x] `firebase_import.js` — imports topics, readings, questions, vocabulary to Firestore
- [x] `node_modules/firebase-admin` installed on server
- [x] Run: `node firebase_import.js --all b2_reading_topics.json b2_reading_topics_4_12.json`

### ✅ Content Files Created
| File | Purpose | Status |
|------|---------|--------|
| `B2ReadingModels.kt` | Kotlin data models | ✅ |
| `b2_reading_topics.json` | All 12 topic definitions | ✅ |
| `b2_reading_topics_4_12.json` | Topic 4 content (10 texts) | ✅ |
| `b2_reading_topics_4_5.json` | Topics 4+5 combined | ✅ |
| `b2_reading_texts_part1.json` | Topics 1-3 (has parse issues) | ⚠️ |
| `QUICKSTART_B2_READING_QUIZ.md` | 15-question instant quiz | ✅ |
| `GENERAL_RESOURCES.md` | Sources for A1–C1, B2 strategies | ✅ |
| `firebase_import.js` | Firestore import script | ✅ |
| `gen_topics_4_to_12.py` | Topic 4 generator (working) | ✅ |
| `gen_topics_5_to_12.py` | Topics 5-12 generator (has bug) | ⚠️ |
| `B2_READING_FINAL.json` | Topic 4 clean version | ✅ |

### ✅ Documentation
- [x] ROADMAP.md — 12-phase development plan
- [x] ARCHITECTURE.md — Multi-level (A1-C1) architecture design
- [x] SETUP_GUIDE.md — Initial setup instructions
- [x] PROJECT_STATUS.md — Master status document (UPDATED after every session)
- [x] MEMORY.md — Updated with project context

---

## 3. WHAT WE ARE GOING TO MAKE

### 🔴 PRIORITY 1 — Level Navigation (BUG) ✅ FIXED
**Fixed:** Tap B2 → sets level + navigates to SubjectListFragment

---

### 🔴 PRIORITY 2 — Firebase Data Import
**On MacBook (local machine):**
```bash
cd ~/b2-deutsch-app/content/reading
npm install firebase-admin
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/serviceAccountKey.json
node firebase_import.js --all b2_reading_topics.json b2_reading_topics_4_12.json
```

**Files needed on MacBook:**
- `b2_reading_topics.json` (small — paste directly)
- `b2_reading_topics_4_12.json` (large — download from server)
- `firebase_import.js` (from server)
- `package.json` + `node_modules/` (firebase-admin)

**Firestore Collections Created:**
- `/topics/{id}` — 12 topic documents
- `/readings/{id}` — Reading passages + metadata
- `/readings/{id}/questions/{id}` — 5 questions per reading
- `/readings/{id}/vocabulary/{id}` — 8 vocab items per reading

---

### 🔴 PRIORITY 3 — Build & Test APK
```bash
# On MacBook with Android Studio
cd ~/b2-deutsch-app
./gradlew assembleDebug

# Install on connected phone
adb install app/build/outputs/apk/debug/app-debug.apk
```

---

### 🟡 PRIORITY 4 — Complete Topics 5–12 Content
**Remaining work:**
- 8 topics × 10 texts = 80 more texts needed
- Each text: 5 questions + 8 vocab + 1 exam tip
- Fix `gen_topics_5_to_12.py` apostrophe escaping issues
- Or rebuild as pure JSON data (no Python string escaping)

**Content update cadence:**
- +1 new text per topic per month
- Monthly content refresh

---

### 🟡 PRIORITY 5 — Fix Topics 1–3 JSON
**Problem:** `b2_reading_texts_part1.json` has curly-quote escaping issues (Python parser breaks).

**Solution:** Run `gen_topics_4_to_12.py` to regenerate Topics 1-3 from embedded Python strings, then merge.

---

### 🟢 PRIORITY 6 — AI Features (Future Phases)

**Writing Practice:**
- User submits text → AI evaluates → feedback + score
- Use MiniMax API for evaluation
- WritingRepository + WritingFragment ready

**Speaking Practice:**
- AI conversation partner (adapts to B2 level)
- Voice input/output
- SpeakingRepository + SpeakingFragment ready

**Peer Speaking Exams:**
- Two users role-play exam scenario
- AI evaluates both users' performance
- Cost: ~$0.01/session

---

### 🟢 PRIORITY 7 — Vocabulary Flashcards
- Swipe cards (front: German, back: English/Turkish)
- Audio pronunciation (Text-to-Speech)
- Mark as "learned" or "needs practice"
- Spaced repetition system

---

### 🟢 PRIORITY 8 — Gamification
- Daily streak counter
- Achievement badges (First Lesson, Perfect Score, Week Warrior, Vocabulary Master)
- Progress tracking per level

---

### 🟢 PRIORITY 9 — Play Store Publishing
**Checklist:**
- [ ] Developer account ($25) at https://play.google.com/console
- [ ] App icons (512×512 PNG)
- [ ] Screenshots (1080×1920 phone)
- [ ] Privacy policy URL
- [ ] German app description
- [ ] AAB bundle upload

---

## 📋 SESSION LOG

### ✅ Product Backlog & Documentation
- [x] PRODUCT_BACKLOG.md — 13 epics, 103 user stories (P0-P3 priorities)
- [x] USER_PERSONAS.md — Ayşe, Mehmet, Zeynep personas
- [x] Full release planning (R1.0 MVP → R2.0 All Levels)

### Session: 2026-04-25 14:48 UTC
**Summary:** Pushed all 116 files to GitHub. Created PRODUCT_BACKLOG.md with 13 epics, 103 user stories.

**New Files:**
- `PRODUCT_BACKLOG.md` — Complete backlog with epics, user stories, priorities, estimates
- `push-to-github.js` — Node.js GitHub API script (works without git CLI)

**Next:** Continue building - add real quiz content, vocabulary system, or writing module

---

### Session: 2026-04-24 (PART 2)
**Summary:** Built complete B2 Reading Comprehension content engine — 4 topics × 10 texts × 5 questions, Firebase import script, quick-start quiz.

**Files Created:**
- `B2ReadingModels.kt`, `b2_reading_topics.json`, `b2_reading_topics_4_12.json`
- `QUICKSTART_B2_READING_QUIZ.md`, `GENERAL_RESOURCES.md`
- `firebase_import.js`, `gen_topics_4_to_12.py`
- Multiple generator scripts (some with bugs)

**Key accomplishment:** 40 texts + 200 questions + 320 vocabulary items ready for Firestore

---

## 🚨 KNOWN ISSUES

1. **Level navigation bug** — Tap B2 → no navigation (PRIORITY 1)
2. **`b2_reading_texts_part1.json`** — Curly-quote parsing breaks JSON (PRIORITY 5)
3. **`gen_topics_5_to_12.py`** — Apostrophe escaping in Python strings (PRIORITY 4)
4. **Firebase not populated** — Need service account key to run import (PRIORITY 2)
5. **No APK built/tested** — Need Android Studio + phone (PRIORITY 3)

---

## 📁 KEY FILE LOCATIONS

| File | Location |
|------|----------|
| Android project | `/home/node/.openclaw/workspace/b2-deutsch-app/` |
| Reading content | `content/reading/` |
| Firebase import | `content/reading/firebase_import.js` |
| Quick quiz | `content/reading/QUICKSTART_B2_READING_QUIZ.md` |
| Project status | `b2-deutsch-app/PROJECT_STATUS.md` |
| Roadmap | `b2-deutsch-app/ROADMAP.md` |
| Architecture | `b2-deutsch-app/ARCHITECTURE.md` |

---

## 📝 QUICK COMMANDS

```bash
# Update from GitHub
cd ~/b2-deutsch-app && git pull origin main

# Import content to Firebase (on MacBook)
cd ~/b2-deutsch-app/content/reading
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json
node firebase_import.js --all b2_reading_topics.json b2_reading_topics_4_12.json

# Build APK (on MacBook with Android Studio)
cd ~/b2-deutsch-app && ./gradlew assembleDebug

# Install on phone
adb install app/build/outputs/apk/debug/app-debug.apk
```

---

_Last updated: 2026-04-25 14:00 UTC_
_Update after every session following the format in SESSION LOG section_
