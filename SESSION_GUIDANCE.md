# B2 Deutsch App — Session Guidance
## Developer Notes & Roadmap

**Last Updated:** 2026-04-25 16:00 UTC
**Session History:** See SESSION LOG at bottom
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
- [x] GitHub repository: `halilmek/b2-deutsch-app`
- [x] `google-services.json` at `app/google-services.json`
- [x] Hilt dependency injection setup (AppModule.kt)

### ✅ Authentication (Phase 3)
- [x] LoginFragment with email/password
- [x] SignUpFragment with display name
- [x] AuthViewModel with Firebase Auth
- [x] Navigation: login → home flow
- [x] Logout functionality

### ✅ Home Dashboard (SIMPLIFIED — Phase 3)
- [x] HomeFragment — minimal layout
- [x] NO streak/lessons cards (removed)
- [x] NO feature buttons (removed — simplified)
- [x] Level selection grid (A1, A2, B1, B2, C1)
- [x] **Red logout button — top-right corner**
- [x] **Bottom logout text link**
- [x] **Exams button visible next to C1 level**

### ✅ Subject → Quiz → Results Flow
- [x] SubjectListFragment — shows all subjects for selected level
- [x] SubjectAdapter — subject cards with category badges
- [x] SubjectDetailFragment — explanation + tips + Start Quiz button
- [x] SubjectResultFragment — detailed results with explanations
- [x] QuizResultAdapter — per-question result display
- [x] Category filter chips (Alle, Grammatik, Lesen, Wortschatz)

### ✅ Exams Module (CORE FEATURE — NEW!)
- [x] ExamsFragment — shows 4 exam types per level
- [x] ExamActiveFragment — timer, questions, navigation
- [x] ExamResultFragment — score display, pass/fail, encouragement
- [x] C1 Exams button next to C1 level card
- [x] 4 Exam Types: Leseverstehen, Hörverstehen, Schreiben, Sprechen
- [x] Navigation: Home → Exams → ExamActive → ExamResult

### ✅ B2 Reading Comprehension Content
- [x] 40 texts, 200 questions, 320 vocabulary items (Topics 1-4)
- [x] Topics 5-12 still needed

### ✅ Navigation System
- [x] nav_graph.xml with all fragment destinations (16 destinations)
- [x] Navigation actions between all screens
- [x] Start destination: loginFragment

### ✅ Documentation
- [x] ROADMAP.md, ARCHITECTURE.md, SETUP_GUIDE.md
- [x] PROJECT_STATUS.md — Master status (UPDATED after every session)
- [x] PRODUCT_BACKLOG.md — 13 epics, 103 user stories
- [x] SESSION_GUIDANCE.md — This file

---

## 3. WHAT WE ARE GOING TO MAKE

### 🔴 PRIORITY 1 — Topic Content in SubjectList
Each subject should show:
- Topic heading (clickable)
- Short description (max 100 words)
- Sample questions
- Quiz immediately below

### 🔴 PRIORITY 2 — Firebase Data Import
**On MacBook:**
```bash
cd ~/b2-deutsch-app/content/reading
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json
node firebase_import.js --all b2_reading_topics.json b2_reading_topics_4_12.json
```

### 🔴 PRIORITY 3 — Build & Test APK
```bash
cd ~/b2-deutsch-app && ./gradlew assembleDebug
adb install app/build/outputs/apk/debug/app-debug.apk
```

### 🟡 PRIORITY 4 — Complete Topics 5–12 Content
- 8 topics × 10 texts = 80 more texts needed
- Each text: 5 questions + 8 vocab + 1 exam tip

### 🟡 PRIORITY 5 — Exams for All Levels (A1-C1)
Currently exams only show for C1. Need to extend to all levels.

---

## 📋 SESSION LOG

### Session: 2026-04-25 16:00 UTC
**Summary:** Major UI overhaul + Exams module added.

**Home Screen Changes:**
- Removed streak/lessons cards (top section)
- Removed feature buttons (Lessons, Quizzes, Vocabulary, Writing, Speaking, Themen & Fächer)
- Kept only: Header with welcome + red logout button, Level grid, Bottom logout text
- Red logout button in top-right corner

**Level Grid Changes:**
- Added "📝 Exams" button next to C1 level card
- LevelAdapter with onExamsClick callback
- Level data class with hasExams flag

**New Exams Module (CORE FEATURE):**
- ExamsFragment — 4 exam types for selected level:
  - 📖 Leseverstehen (60 min, 10 questions)
  - 🎧 Hörverstehen (40 min, 10 questions)
  - ✍️ Schreiben (75 min, 1 task)
  - 🎤 Sprechen (15 min, 2 parts)
- ExamActiveFragment — timer countdown, question display, radio button answers, prev/next navigation
- ExamResultFragment — score card, pass/fail, encouragement message

**Navigation Flow:**
- Home → Tap Level → SubjectList
- Home → Tap "Exams" on C1 → ExamsFragment
- Exams → Tap Exam → ExamActiveFragment (with timer)
- ExamActive → Finish → ExamResultFragment

**Files Created:**
- `ExamsFragment.kt`, `ExamActiveFragment.kt`, `ExamResultFragment.kt`
- `fragment_exams.xml`, `fragment_exam_active.xml`, `fragment_exam_result.xml`
- `item_level.xml` (updated with Exams button)
- `Level.kt` (updated with hasExams flag)
- `LevelAdapter.kt` (updated with onExamsClick)
- `nav_graph.xml` (updated with exams navigation)
- `dimens.xml` (new)

**Next:** Add topic content to SubjectList (each topic with description + sample questions + quiz)

---

### Session: 2026-04-25 14:48 UTC
**Summary:** Pushed all 116 files to GitHub. Created PRODUCT_BACKLOG.md with 13 epics, 103 user stories.

**Files Created:**
- `PRODUCT_BACKLOG.md` — Complete backlog with epics, user stories, priorities
- `push-to-github.js` — Node.js GitHub API script

---

## 🚨 KNOWN ISSUES

1. **SubjectList needs topic content** — Each subject needs description, sample questions, quiz below
2. **Firebase not populated** — Need service account key to run import
3. **No APK built/tested** — Need Android Studio + phone

---

## 📁 KEY FILE LOCATIONS

| File | Location |
|------|----------|
| Android project | `/home/node/.openclaw/workspace/b2-deutsch-app/` |
| Reading content | `content/reading/` |
| Firebase import | `content/reading/firebase_import.js` |
| Quick quiz | `content/reading/QUICKSTART_B2_READING_QUIZ.md` |
| Project status | `b2-deutsch-app/PROJECT_STATUS.md` |
| Product backlog | `b2-deutsch-app/PRODUCT_BACKLOG.md` |

---

## 📝 QUICK COMMANDS

```bash
# Update from GitHub
cd ~/b2-deutsch-app && git pull origin main

# Push to GitHub (from server)
cd /home/node/.openclaw/workspace && node push-to-github.js

# Build APK (on MacBook)
cd ~/b2-deutsch-app && ./gradlew assembleDebug
```

---

_Last updated: 2026-04-25 16:00 UTC_
