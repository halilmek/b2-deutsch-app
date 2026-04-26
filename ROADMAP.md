# B2 Deutsch App — Project Roadmap

**Last Updated:** 2026-04-26
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
    options: string[]         # ["Als", "Wenn", "Während", "Bevor"]
    correctAnswer: string
    explanation: string
    difficulty: string        # "easy" | "medium" | "hard"
    topicName: string
    firebaseId: string
```

### Topics in grammarQuizBank

| Level | Topics | Questions | Status |
|-------|--------|-----------|--------|
| A1 | 15 topics | 1,500 Q | ✅ In assets + Firebase |
| A2 | 15 topics | 1,500 Q | ✅ In assets + Firebase |
| B1 | 15 topics | 1,500 Q | ✅ In assets + Firebase |
| B2 | 23 topics | 2,300 Q | ✅ In assets + Firebase |
| C1 | 15 topics | 1,500 Q | ✅ In assets + Firebase |

### Quiz Mechanics
- 10 random questions per quiz from **active** pool
- After quiz: 10 marked **passive** (solved)
- Active/Passive tracking via SharedPreferences
- After 90+ solved: completion message OR loop reset (oldest passive → active)
- Questions stored in `app/src/main/assets/b2_questions.json` (offline)

---

## 📌 PHASE 4 — B2 EXAM MODULE QUIZZES 🔄 IN PROGRESS

### Purpose
B2 exam-style module questions with **specific konnektor focus** — not general grammar.

### Structure: Topics → Sub-Topics → Questions

**B2 Module Structure (23 Topics):**

| Topic # | Topic Name | Sub-Topics | Status |
|---------|-----------|-----------|--------|
| 1. Topic | Konnektoren | als, bevor, bis, seitdem, während, wenn, sobald, solange | 🔄 96 Q (12 per konnektor) — NEEDS REVIEW |
| 2. Topic | Verben und Ergänzungen | TODO | ⏳ Pending |
| 3. Topic | Zeitformen in der Vergangenheit | TODO | ⏳ Pending |
| 4. Topic | Zeitformen der Zukunft | TODO | ⏳ Pending |
| 5. Topic | Futur mit werden | TODO | ⏳ Pending |
| 6. Topic | Angaben im Satz | TODO | ⏳ Pending |
| 7. Topic | Verneinung mit nicht | TODO | ⏳ Pending |
| 8. Topic | Negationswörter | TODO | ⏳ Pending |
| 9. Topic | Passiv Präteritum | TODO | ⏳ Pending |
| 10. Topic | Konjunktiv II der Vergangenheit | TODO | ⏳ Pending |
| 11. Topic | Konjunktiv II mit Modalverben | TODO | ⏳ Pending |
| 12. Topic | Pronomen: einander | TODO | ⏳ Pending |
| 13. Topic | Weiterführende Nebensätze | TODO | ⏳ Pending |
| 14. Topic | Präpositionen mit Genitiv | TODO | ⏳ Pending |
| 15. Topic | je und desto/umso + Komparativ | TODO | ⏳ Pending |
| 16. Topic | Nomen-Verb-Verbindungen | TODO | ⏳ Pending |
| 17. Topic | Folgen ausdrücken | TODO | ⏳ Pending |
| 18. Topic | Ausdrücke mit Präpositionen | TODO | ⏳ Pending |
| 19. Topic | Irreale Konditionalsätze | TODO | ⏳ Pending |
| 20. Topic | Relativsätze im Genitiv | TODO | ⏳ Pending |
| 21. Topic | Konjunktiv I in der indirekten Rede | TODO | ⏳ Pending |
| 22. Topic | Konjunktiv II in irrealen Vergleichssätzen | TODO | ⏳ Pending |
| 23. Topic | (Reserve) | TODO | ⏳ Pending |

### Data Model — moduleQuizQuestions

```
moduleQuizQuestions/
  {questionId}/                  # e.g. "b2_01_als_q001"
    id: string
    module: string                # "B2"
    topicNumber: string           # "1. Topic"
    topicName: string             # "Konnektoren"
    konnektor: string             # "als" | "bevor" | "bis" | "seitdem" | "während" | "wenn" | "sobald" | "solange"
    questionText: string
    options: string[]
    correctAnswer: string
    explanation: string
    difficulty: string            # "easy" | "medium" | "hard"
    level: string                # "B2"
```

### Two Separate Collections

| Collection | Purpose | Question Type | Question Count |
|------------|---------|---------------|---------------|
| `grammarQuizBank` | General grammar practice (all levels) | MCQ + T/F + Fill | 8,300 (bundled in assets) |
| `moduleQuizQuestions` | B2 exam module (konnektor-specific) | MCQ only | 96+ (in progress) |

**Key rule:** Never mix general grammar and module exam questions in the same collection.

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

_Last updated: 2026-04-26_
