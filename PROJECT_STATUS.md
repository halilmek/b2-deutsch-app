# B2 Deutsch App — PROJECT STATUS

**Last Updated:** 2026-04-25 13:10 UTC
**GitHub:** https://github.com/halilmek/b2-deutsch-app
**Firebase Project:** b2-deutsch-app (project_number: 419122108874)

---

## 📋 MASTER TODO LIST

### 🔴 CRITICAL — Do These First

- [ ] **Firebase Import** — Push reading content to Firestore
  - Run: `node content/reading/firebase_import.js --all`
  - Requires: `GOOGLE_APPLICATION_CREDENTIALS` set to service account key path
  - Location: `content/reading/`

- [ ] **Build APK** — Compile and test on phone
  - Run: `./gradlew assembleDebug`
  - Install: `adb install app/build/outputs/apk/debug/app-debug.apk`

- [ ] **google-services.json** — Must be in `app/google-services.json`
  - Download from Firebase Console → Project Settings → Your apps → Download

---

### 🟡 IMPORTANT — Before Play Store

- [ ] **Play Store Account** — Create developer account ($25 one-time)
  - URL: https://play.google.com/console
  - Credentials needed: credit card, Google account

- [ ] **App Signing Key** — Generated automatically by Android Studio
  - Keystore: `~/.android/debug.keystore` (for debug builds)
  - For release: Generate a new keystore and save the credentials SECURELY

- [ ] **App Icons & Screenshots** — Required for Play Store listing
  - Icon: 512x512 PNG
  - Screenshots: Phone (1080x1920), Tablet (optional)

- [ ] **Privacy Policy URL** — Required for Play Store
  - Can use: https://halilmek.github.io/b2-deutsch-app/privacy.html (needs creating)

- [ ] **Write app description** — For Play Store listing (in German)

---

### 🟢 NICE TO HAVE — Future Phases

- [ ] **Topics 5-12 content** — Generate remaining 8 topics (80 more texts)
  - Script: `content/reading/gen_topics_5_to_12.py`
  - Fix apostrophe escaping issues first

- [ ] **Writing practice feature** — AI evaluation of written German
- [ ] **Speaking practice feature** — AI conversation partner
- [ ] **A1, A1, B1, C1 levels** — Expand beyond B2

---

## ✅ COMPLETED WORK

### Project Setup
- [x] Android project scaffolded (Kotlin + Jetpack Compose)
- [x] Firebase project configured (Auth + Firestore + Storage)
- [x] GitHub repository created: halilmek/b2-deutsch-app
- [x] Package name: `com.b2deutsch.app`

### Authentication (Phase 3)
- [x] LoginFragment with email/password
- [x] SignUpFragment with display name
- [x] AuthViewModel with Firebase Auth integration
- [x] Navigation: login → home flow
- [x] Logout functionality

### Home Screen (Phase 4)
- [x] HomeFragment with welcome message
- [x] Level selection grid (A1, A2, B1, B2, C1)
- [x] LevelAdapter with tap handling
- [x] Navigation buttons: Lessons, Quizzes, Vocabulary, Writing, Speaking
- [x] User progress display (streak, lessons completed)
- [x] HomeViewModel with data loading

### Lessons Module (Phase 4)
- [x] LessonsFragment with RecyclerView
- [x] LessonAdapter
- [x] LessonDetailFragment
- [x] ContentRepository for loading lessons from Firestore

### Quiz Module (Phase 5)
- [x] QuizzesFragment
- [x] QuizActiveFragment (question display, multiple choice, true/false, fill-blank)
- [x] QuizResultFragment (score, pass/fail)
- [x] QuizViewModel
- [x] QuizAdapter
- [x] Content loaded from Firestore

### Vocabulary Module (Phase 6)
- [x] VocabularyFragment (placeholder UI ready for flashcards)

### Writing & Speaking (Phase 9+)
- [x] WritingFragment (placeholder for AI writing evaluation)
- [x] SpeakingFragment (placeholder for AI speaking practice)

### Navigation
- [x] nav_graph.xml with all fragment destinations
- [x] Navigation actions between all screens
- [x] Start destination: loginFragment

### Data Layer
- [x] All model classes: User, Level, Lesson, Quiz, Vocabulary, Writing, Speaking
- [x] Repository layer: ContentRepository, UserRepository
- [x] FirebaseDataSource for Firestore access
- [x] Hilt dependency injection setup (AppModule.kt)

### Reading Comprehension Content (Phase 9)
- [x] **Data models** — `B2ReadingModels.kt` — ReadingText, Question, VocabEntry
- [x] **Quiz UI** — QuizActiveFragment, QuizzesFragment, QuizResultFragment, QuizViewModel, QuizAdapter
- [x] **Repository layer** — ContentRepository, FirebaseDataSource
- [x] **Content files** — 12 topic definitions
- [x] **Topic 4 content** — 10 texts, 50 questions, 80 vocabulary entries (Gesellschaft)
- [x] **Topic 5 sample** — 1 text sample (Medien und Kommunikation)
- [x] **Topics 1-3** — Partial content (in b2_reading_texts_part1.json, has parse issues)
- [x] **Quiz quickstart** — 15-question ready-to-use quiz (QUICKSTART_B2_READING_QUIZ.md)
- [x] **Firebase import script** — firebase_import.js (ready to run)

### Project Documentation
- [x] ROADMAP.md — 12-phase development plan
- [x] ARCHITECTURE.md — Multi-level (A1-C1) architecture design
- [x] SETUP_GUIDE.md — Initial setup instructions

---

## 🗂️ PROJECT STRUCTURE

```
b2-deutsch-app/
├── app/
│   ├── google-services.json          ✅ Present
│   ├── build.gradle
│   └── src/main/
│       ├── java/com/b2deutsch/app/
│       │   ├── B2DeutschApp.kt         # Application class
│       │   ├── data/
│       │   │   ├── model/              # User, Level, Lesson, Quiz, Vocabulary, etc.
│       │   │   ├── repository/         # ContentRepository, UserRepository
│       │   │   └── remote/             # FirebaseDataSource
│       │   ├── di/                     # Hilt AppModule
│       │   ├── ui/
│       │   │   ├── auth/               # LoginFragment, SignUpFragment, AuthViewModel
│       │   │   ├── home/               # HomeFragment, HomeViewModel
│       │   │   ├── lessons/            # LessonsFragment, LessonAdapter, LessonDetailFragment
│       │   │   ├── level/              # LevelAdapter (A1-C1 grid)
│       │   │   ├── quiz/               # QuizActive, Quizzes, QuizResult fragments + ViewModel
│       │   │   ├── vocabulary/         # VocabularyFragment
│       │   │   ├── speaking/           # SpeakingFragment
│       │   │   ├── writing/            # WritingFragment
│       │   │   └── MainActivity.kt
│       │   └── util/                   # Constants.kt
│       └── res/
│           ├── layout/                 # 15 layout files
│           ├── navigation/             # nav_graph.xml
│           └── values/                # strings, colors, themes
├── content/reading/
│   ├── B2ReadingModels.kt             # Data class definitions
│   ├── B2_READING_CONTENT.kt          # Inline reading content
│   ├── B2_READING_FINAL.json           # Merged complete content
│   ├── b2_reading_topics.json          # 12 topic definitions
│   ├── b2_reading_topics_4_12.json     # Topic 4 content (Gesellschaft) - COMPLETE
│   ├── b2_reading_topics_4_5.json      # Topics 4+5 combined
│   ├── b2_reading_texts_part1.json     # Topics 1-3 content (parse issues)
│   ├── QUICKSTART_B2_READING_QUIZ.md   # 15 ready-to-use questions
│   ├── firebase_import.js              # Firestore import script
│   ├── gen_all_topics.py              # Generator for topics 5-12 (needs fix)
│   └── gen_topics_4_to_12.py          # Topic 4 generator (working)
├── build.gradle
├── settings.gradle
├── gradle.properties
├── ROADMAP.md
├── ARCHITECTURE.md
└── SETUP_GUIDE.md
```

---

## 🔐 CREDENTIALS & SECRETS

| Item | Status | Notes |
|------|--------|-------|
| GitHub Token | ⚠️ SECURE — NEVER commit | Stored in OpenClaw server only |
| Firebase Project | ✅ Active | `b2-deutsch-app`, Project ID: `b2-deutsch-app` |
| Firebase Storage | ✅ Active | `b2-deutsch-app.firebasestorage.app` |
| google-services.json | ✅ Present | Located at `app/google-services.json` |
| Service Account Key | ❌ MISSING | Needed for firebase_import.js |

### Where to Get Secrets

1. **google-services.json** — Already present at `app/google-services.json`

2. **Firebase Service Account** (for import script)
   - Firebase Console → Project Settings → Service Accounts → Generate new private key

3. **Play Store Publisher Account**
   - https://play.google.com/console → Sign up ($25)

---

## 🚨 KNOWN ISSUES

### 2026-04-25 — Level Selection Doesn't Navigate
**Problem:** Tapping on a level (A1-C1) in the home grid only calls `setCurrentLevel()` but doesn't navigate anywhere.

**Root Cause:** `LevelAdapter.onLevelClick` only sets the level in HomeViewModel — no navigation action is triggered.

**Impact:** User can select a level but doesn't see level-specific content.

**Fix Options:**
1. Add `selectedLevel` argument to lessons/quizzes fragments
2. When user taps a level then "Lessons" — filter lessons by that level
3. Or: tap on level navigates directly to a level detail screen

---

## 📍 CURRENT STATE

### What Works
- ✅ Complete Android app scaffold with Navigation Component
- ✅ Firebase Auth (email/password sign-up + login)
- ✅ Home screen with level selection (A1-C1) and feature buttons
- ✅ Lessons, Quizzes, Vocabulary, Writing, Speaking screens (UI ready)
- ✅ Level-agnostic architecture (same app supports all CEFR levels)
- ✅ Reading content (topic 4 complete, 15-question quiz ready)
- ✅ Content data models and Firebase import script

### What Doesn't Work Yet
- ❌ No data in Firebase — need to run import script
- ❌ Level selection doesn't navigate or filter content
- ❌ Lessons/Quizzes don't receive level filter parameter
- ❌ Vocabulary/Speaking/Writing are placeholders (no AI integration yet)
- ❌ No APK built/tested

### Next Immediate Steps
1. Download Firebase service account key → run `node firebase_import.js --all`
2. Fix level navigation: tap level → filter lessons/quizzes by level
3. Build APK: `./gradlew assembleDebug`
4. Install on phone: `adb install app/build/outputs/apk/debug/app-debug.apk`

---

## 📞 PLAY STORE PUBLISHING CHECKLIST

When ready to publish:

- [ ] Developer account created at https://play.google.com/console
- [ ] App name: "B2 Deutsch — Prüfungsvorbereitung"
- [ ] Short description (80 chars) — in German
- [ ] Full description (4000 chars) — in German
- [ ] Category: Education → Language
- [ ] Content rating: Everyone (no mature content)
- [ ] Icon: 512x512 PNG
- [ ] Screenshots: At least 2 phone screenshots
- [ ] Privacy Policy URL (can use GitHub Pages)
- [ ] App released (APK or AAB) uploaded
- [ ] Pricing: Free (or set price)
- [ ] Countries: All or specific
- [ ] Human-readable version note (what's new)

---

## 📝 QUICK COMMANDS REFERENCE

```bash
# Update project from GitHub
cd ~/b2-deutsch-app
git pull origin main

# Import content to Firebase (after setting credentials)
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/serviceAccountKey.json
cd ~/b2-deutsch-app/content/reading
node firebase_import.js --all b2_reading_topics.json b2_reading_topics_4_12.json

# Build debug APK
cd ~/b2-deutsch-app
./gradlew assembleDebug

# Install on connected phone
adb install app/build/outputs/apk/debug/app-debug.apk
```

---

## 📊 CODE STATS

| Metric | Count |
|--------|-------|
| Kotlin files | 35 |
| XML layout files | 15 |
| Navigation destinations | 13 |
| Content topics | 12 (4 partially populated) |
| Quiz questions (quickstart) | 15 |
| Vocabulary entries (topic 4) | 80 |

---

_Last updated: 2026-04-25 13:10 UTC_