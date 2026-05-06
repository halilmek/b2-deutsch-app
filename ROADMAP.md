# B2 Deutsch App — Project Roadmap

**Last Updated:** 2026-05-06 21:51 UTC
**GitHub:** https://github.com/halilmek/b2-deutsch-app
**Firebase:** b2-deutsch-app

---

## 🏗️ WHAT WE'RE BUILDING

A **multi-level German language exam prep app** (A1, A2, B1, B2, C1) on Android. One app for all CEFR levels. Users practice with AI-generated content, quiz themselves, and track progress.

### App Architecture
- **Offline-first**: Questions bundled in app assets (JSON) + Firestore as cloud source
- **Active/Passive tracking**: Per-topic progress (10 Q/quiz, 100 Q/topic, looping system)
- **Two quiz systems**:
  1. **General Grammar Quizzes** → `grammarQuizBank` collection (all levels)
  2. **Module Quizzes** → `moduleQuizQuestions` collection (B2 exam module — konnektor-specific)

---

## 📌 PHASE 1 — Firebase Backend & Security ✅ DONE
- Firebase project: `b2-deutsch-app`
- Package: `com.b2deutsch.app`
- Auth: Email/Password + Google Sign-In
- Firestore DB: Active
- Storage: Active
- Analytics + Crashlytics: Enabled

---

## 📌 PHASE 2 — App Shell & Navigation ✅ DONE
- Navigation Component with nav_graph
- Home screen with level selector (A1–C1)
- Subject list per level
- Bottom navigation (Home, Profile, Settings)

---

## 📌 PHASE 3 — Quiz System (General Grammar) ✅ DONE

### Data Model

```
grammarQuizBank/
  {questionId}/
    id: string
    subjectId: string        # e.g. "b2_01"
    level: string            # "A1" | "A2" | "B1" | "B2" | "C1"
    type: string             # "multiple_choice"
    questionText: string
    options: string[]        # ["Als", "Wenn", "Während", "Bevor"]
    correctAnswer: string
    explanation: string
    difficulty: string       # "easy" | "medium" | "hard"
    topicName: string
    firebaseId: string
```

### Topics in grammarQuizBank

| Level | Topics | Questions | Status |
|-------|--------|-----------|--------|
| A1 | 15 topics | 1,500 Q | ✅ In assets + Firebase |
| A2 | 15 topics | 1,500 Q | ✅ In assets + Firebase |
| B1 | 15 topics | 1,500 Q | ✅ In assets + Firebase |
| B2 | 23 topics | ~2,340 Q | ✅ In assets (b2_01 to b2_14 complete, b2_15-b2_23 placeholder) |
| C1 | 15 topics | 1,500 Q | ✅ In assets + Firebase |

### Quiz Mechanics
- 10 random questions per quiz from **active** pool
- After quiz: 10 marked **passive** (solved)
- Active/Passive tracking via SharedPreferences
- After 90+ solved: completion message OR loop reset (oldest passive → active)
- Questions stored in `app/src/main/assets/b2_questions.json` (offline)

---

## 📌 PHASE 4 — B2 EXAM MODULE QUIZZES 🔄 MAJOR PROGRESS

### Purpose
B2 exam-style module questions with **specific grammar focus** — not general grammar.

### B2 Module — 23 Topics Status

| Topic # | subjectId | Topic Name | Questions | Description | Status |
|---------|-----------|-----------|-----------|-------------|--------|
| 1 | b2_01 | Konnektoren | ~146 | ✅ Complete | DONE |
| 2 | b2_02 | Verben und Ergänzungen | 50 | ⚠️ Partial — no topic entry in metadata | PARTIAL |
| 3 | b2_03 | Verben und Ergänzungen | 100 | ✅ Complete | DONE |
| 4 | b2_04 | Zeitformen in der Vergangenheit | 160 | ✅ Complete | DONE |
| 5 | b2_05 | Zeitformen der Zukunft | 120 | ✅ Complete | DONE |
| 6 | b2_06 | Futur mit werden | 125 | ✅ Complete | DONE |
| 7 | b2_07 | Angaben im Satz | 100 | ✅ Complete | DONE |
| 8 | b2_08 | Verneinung mit nicht | 100 | ✅ Complete | DONE |
| 9 | b2_09 | Negationswörter | 100 | ✅ Complete | DONE |
| 10 | b2_10 | Passiv Präteritum | 100 | ✅ Complete | DONE |
| 11 | b2_11 | Konjunktiv II der Vergangenheit | 100 | ✅ Complete | DONE |
| 12 | b2_12 | Konjunktiv II mit Modalverben | 120 | ✅ Complete (120 questions) | DONE |
| 13 | b2_13 | Pronomen: einander | 100 | ✅ Complete | DONE |
| 14 | b2_14 | Weiterführende Nebensätze | 100 | ✅ Complete | DONE |
| 15 | b2_15 | Präpositionen mit Genitiv | 100 | ⏳ Pending — placeholder | PENDING |
| 16 | b2_16 | je und desto/umso + Komparativ | 100 | ⏳ Pending — placeholder | PENDING |
| 17 | b2_17 | Nomen-Verb-Verbindungen | 100 | ⏳ Pending — placeholder | PENDING |
| 18 | b2_18 | Folgen ausdrücken | 100 | ⏳ Pending — placeholder | PENDING |
| 19 | b2_19 | Ausdrücke mit Präpositionen | 100 | ⏳ Pending — placeholder | PENDING |
| 20 | b2_20 | Irreale Konditionalsätze | 100 | ⏳ Pending — placeholder | PENDING |
| 21 | b2_21 | Relativsätze im Genitiv | 100 | ⏳ Pending — placeholder | PENDING |
| 22 | b2_22 | Konjunktiv I in der indirekten Rede | 100 | ⏳ Pending — placeholder | PENDING |
| 23 | b2_23 | Konjunktiv II in irrealen Vergleichssätzen | 100 | ⏳ Pending — placeholder | PENDING |

**Progress: 14/23 topics complete (b2_01 to b2_14)**
**9 topics remaining: b2_15 to b2_23**

### Topics with Updated Descriptions (Beschreibung)

| Topic | Description Status |
|-------|-------------------|
| b2_10 | ✅ Turkish→English grammar explanation for Passiv Präteritum |
| b2_11 | ✅ Turkish→English grammar explanation for Konjunktiv II der Vergangenheit |
| b2_12 | ✅ Turkish→English grammar explanation for Konjunktiv II mit Modalverben + modalverb table |
| b2_13 | ✅ Turkish→English grammar explanation for Pronomen: einander + 17-form table |
| b2_14 | ✅ Turkish→English grammar explanation for Weiterführende Nebensätze + conjunction table |

---

## 📋 FIRESTORE SYNC PRIORITY

All completed topics need Firestore sync. Run on local machine:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/Users/halilozturk/Documents/b2-deutsch-app-firebase-adminsdk-fbsvc-4aa25c0ca2.json"
cd /Users/halilozturk/b2-deutsch-app
node scripts/import_and_sync.js b2_08 b2_09 b2_10 b2_11 b2_12 b2_13 b2_14
```

---

## 📌 PHASE 5 — A1–C1 EXAM MODULE QUIZZES ⏳ PENDING
- Generate konnektor-specific questions for A1, A2, B1, C1 levels
- Same structure: module / topicNumber / topicName / konnektor fields
- Different difficulty per level

---

## 📌 PHASE 6 — Reading Comprehension ⏳ PENDING
- AI-generated B2 reading passages (300-400 words each)
- 10 passages per topic × 12 topics
- MCQ questions per passage (4 options, 1 correct)
- Stored in `readingPassages` + `passageQuestions` collections

---

## 📌 PHASE 7 — Vocabulary & Flashcards ⏳ PENDING
- 5,000+ vocabulary entries (A1–C1)
- Spaced repetition system
- Bundled in app assets

---

## 📌 PHASE 8 — Writing Practice ⏳ PENDING
- User submits text → AI evaluates → feedback + score
- Prompt library per topic and level

---

## 📌 PHASE 9 — Speaking Practice (AI Partner) ⏳ PENDING
- Conversational AI partner that adapts to B2 level
- Voice interaction (text-to-speech + speech-to-text)
- Topic cards for conversational practice

---

## 📌 PHASE 10 — Peer Speaking Exams ⏳ PENDING
- Two users role-play exam scenario
- AI evaluates both participants
- Transcription + feedback

---

## 📌 PHASE 11 — Progress & Gamification ⏳ PENDING
- Streak tracking
- Badges and achievements
- Per-level statistics
- Leaderboard

---

## 📌 PHASE 12 — Play Store Release ⏳ PENDING
- APK build and testing
- Store listing copy
- Screenshots and graphics
- Pricing: Free / Standard (€5.99/mo) / Premium (€9.99/mo)

---

## 🔑 PRICING TIERS

| Tier | Price | AI Speaking | Peer Exams | Writing Evals | Levels |
|------|-------|------------|------------|--------------|--------|
| Free | €0 | 10 min/day | 1/week | 1/week | B2 only |
| Standard | €5.99/mo | 20 min/day | 1/week | 5/month | B2 only |
| Premium | €9.99/mo | Unlimited | 2/week | 15/month | A1–C1 |

---

_Last updated: 2026-05-06 21:51 UTC_
_Update after: every topic content change, every Firestore sync, every new feature_