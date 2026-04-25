# PRODUCT BACKLOG — B2 Deutsch App
## German Language Exam Preparation App
### CEFR Levels: A1, A2, B1, B2, C1

---

## 👤 USER PERSONAS

### Persona 1: Ayşe — The Serious Exam Candidate
- **Age:** 26
- **Goal:** Pass Goethe B2 exam in 3 months
- **Behavior:** Studies 1-2h daily, tracks progress meticulously, needs structured curriculum
- **Pain:** Expensive prep courses, limited speaking practice partners

### Persona 2: Mehmet — The Casual Learner
- **Age:** 22
- **Goal:** Improve German for job application
- **Behavior:** 30 min/day on commute, prefers mobile, likes gamification
- **Pain:** Gets bored easily, needs motivation hooks

### Persona 3: Zeynep — The Premium Learner
- **Age:** 30
- **Goal:** Achieve C1 for academic/research purposes
- **Behavior:** Willing to pay for quality, needs comprehensive coverage
- **Pain:** Limited time, wants efficient learning

---

## 🎯 VISION STATEMENT
> "B2 Deutsch is the most comprehensive German exam prep app — combining AI-powered practice with exam-format content across all CEFR levels, so learners can confidently pass Goethe, ÖSD, and DW exams without expensive courses."

---

## EPIC 1: Authentication & User Management
*User onboarding, account security, subscription management*

### User Stories

| ID | Story | Points | Priority | Status |
|----|-------|--------|----------|--------|
| AUTH-001 | **As a new user, I want to sign up with email/password** so I can create an account and access the app | 3 | P0 | ✅ Done |
| AUTH-002 | **As a user, I want to sign in with Google** so I can log in quickly without remembering passwords | 2 | P0 | ✅ Done |
| AUTH-003 | **As a logged-in user, I want to see my profile** so I can manage my account settings | 2 | P1 | 🔄 In Progress |
| AUTH-004 | **As a user, I want to log out** so I can switch accounts or secure my device | 1 | P0 | ✅ Done |
| AUTH-005 | **As a user, I want to see my subscription tier** so I know what features are available to me | 2 | P1 | 🔄 In Progress |
| AUTH-006 | **As a user, I want to upgrade to Premium** so I can access A1-C1 levels and unlimited AI features | 5 | P2 | 📋 TODO |
| AUTH-007 | **As a user, I want to reset my password** so I can recover my account if I forget my password | 3 | P1 | 📋 TODO |
| AUTH-008 | **As an admin, I want to manage user roles** so I can support premium users | 5 | P3 | 📋 TODO |

---

## EPIC 2: Level Selection & Navigation
*CEFR level browsing, level-based content filtering, navigation between modules*

### User Stories

| ID | Story | Points | Priority | Status |
|----|-------|--------|----------|--------|
| LEVEL-001 | **As a user, I want to see all CEFR levels (A1-C1)** so I can select my target level | 2 | P0 | ✅ Done |
| LEVEL-002 | **As a user, I tap a level and see relevant subjects** so I can focus on that level's content | 3 | P0 | ✅ Done |
| LEVEL-003 | **As a user, I want to see my current level badge** so I know which level I'm studying for | 1 | P1 | 🔄 In Progress |
| LEVEL-004 | **As a Premium user, I want to access all levels A1-C1** so I can prepare for any exam | 3 | P0 | 📋 TODO |
| LEVEL-005 | **As a Free/Standard user, I want to see only B2 content** so I know what's included in my tier | 2 | P1 | ✅ Done |
| LEVEL-006 | **As a user, I want quick access to all modules from home** so I can navigate without going through levels first | 3 | P1 | ✅ Done |

---

## EPIC 3: Reading Comprehension
*AI-generated B2 reading passages with exam-style questions, vocab, and tips*

### User Stories

| ID | Story | Points | Priority | Status |
|----|-------|--------|----------|--------|
| READ-001 | **As a user, I want to read German passages** on topics like Beruf, Gesundheit, Umwelt so I can practice reading comprehension | 5 | P0 | ✅ Done (Topics 1-4) |
| READ-002 | **As a user, I want to answer multiple choice questions** about each passage so I can test my understanding | 3 | P0 | ✅ Done |
| READ-003 | **As a user, I want to answer true/false questions** so I can practice that exam format | 3 | P0 | ✅ Done |
| READ-004 | **As a user, I want to answer fill-in-the-blank questions** so I can practice that exam format | 3 | P0 | ✅ Done |
| READ-005 | **As a user, I want to see vocabulary for each passage** so I can learn new words in context | 3 | P0 | ✅ Done |
| READ-006 | **As a user, I want to see exam tips** for each topic so I can improve my strategy | 2 | P0 | ✅ Done |
| READ-007 | **As a user, I want to see explanations for wrong answers** so I can learn from my mistakes | 3 | P0 | ✅ Done |
| READ-008 | **As a user, I want to filter readings by topic** so I can focus on subjects I find difficult | 3 | P1 | 📋 TODO |
| READ-009 | **As a user, I want new readings added monthly** so content stays fresh and comprehensive | 5 | P2 | 📋 TODO |
| READ-010 | **As a Premium user, I want to access A1-C1 readings** so I can practice at any level | 8 | P1 | 📋 TODO |
| READ-011 | **As a user, I want to mark readings as completed** so I can track my progress | 2 | P2 | 📋 TODO |
| READ-012 | **As a user, I want to re-read passages I've completed** so I can review before exams | 2 | P2 | 📋 TODO |

---

## EPIC 4: Subject → Quiz → Results Flow
*Structured learning paths: choose subject → learn → practice → see results*

### User Stories

| ID | Story | Points | Priority | Status |
|----|-------|--------|----------|--------|
| SUBJ-001 | **As a user, I want to see subjects grouped by category** (Grammatik, Lesen, Wortschatz) so I can navigate to what I need | 3 | P0 | ✅ Done |
| SUBJ-002 | **As a user, I want to filter subjects by category** so I can find Grammatik or Lesen quickly | 2 | P0 | ✅ Done |
| SUBJ-003 | **As a user, I tap a subject and see its description + tips** so I understand what I'm about to learn | 3 | P0 | ✅ Done |
| SUBJ-004 | **As a user, I want to start a quiz from a subject** so I can test my knowledge | 2 | P0 | ✅ Done |
| SUBJ-005 | **As a user, I want to see detailed quiz results** with explanations for each question so I can learn from mistakes | 5 | P0 | ✅ Done |
| SUBJ-006 | **As a user, I want to see my score as a percentage** so I know if I passed or failed | 2 | P0 | ✅ Done |
| SUBJ-007 | **As a user, I want to see the correct answers** after completing a quiz so I can study the material | 3 | P0 | ✅ Done |
| SUBJ-008 | **As a user, I want to go back to subject list after results** so I can try another subject | 1 | P1 | ✅ Done |
| SUBJ-009 | **As a user, I want to track which subjects I've completed** so I know my learning progress | 5 | P1 | 🔄 In Progress |
| SUBJ-010 | **As a Premium user, I want to access grammar subjects across A1-C1** so I can master all grammar topics | 5 | P1 | 📋 TODO |
| SUBJ-011 | **As a user, I want to see how many quizzes exist per subject** so I know how much practice is available | 2 | P2 | 📋 TODO |
| SUBJ-012 | **As a user, I want to see "Recommended next" subject** after completing one so I know what to study next | 3 | P2 | 📋 TODO |

---

## EPIC 5: Quiz System
*Full quiz experience: question display, answer selection, scoring, completion*

### User Stories

| ID | Story | Points | Priority | Status |
|----|-------|--------|----------|--------|
| QUIZ-001 | **As a user, I want to see one question at a time** so I can focus on each question individually | 2 | P0 | ✅ Done |
| QUIZ-002 | **As a user, I want to select an answer by tapping** so the interaction is simple and mobile-friendly | 2 | P0 | ✅ Done |
| QUIZ-003 | **As a user, I want to see my selected answer highlighted** so I know what I chose | 1 | P0 | ✅ Done |
| QUIZ-004 | **As a user, I want to advance to the next question** so I can complete the quiz | 2 | P0 | ✅ Done |
| QUIZ-005 | **As a user, I want to see a progress indicator** so I know how many questions remain | 2 | P0 | ✅ Done |
| QUIZ-006 | **As a user, I want to see my final score after the quiz** so I know how I performed | 2 | P0 | ✅ Done |
| QUIZ-007 | **As a user, I want to see pass/fail status** (70% pass threshold) so I know if I passed | 2 | P0 | ✅ Done |
| QUIZ-008 | **As a user, I want a countdown timer** for timed exam practice so I can simulate real exam conditions | 5 | P1 | 📋 TODO |
| QUIZ-009 | **As a user, I want to review my answers after quiz** so I can study mistakes | 3 | P1 | ✅ Done |
| QUIZ-010 | **As a user, I want to retake a quiz** so I can improve my score | 3 | P1 | 📋 TODO |
| QUIZ-011 | **As a user, I want to see a quiz summary** (time taken, accuracy per question type) so I can analyze my performance | 5 | P2 | 📋 TODO |
| QUIZ-012 | **As a user, I want to share my quiz result** so I can show friends my progress | 3 | P3 | 📋 TODO |

---

## EPIC 6: Vocabulary & Flashcards
*Vocabulary learning with spaced repetition, flashcard study mode*

### User Stories

| ID | Story | Points | Priority | Status |
|----|-------|--------|----------|--------|
| VOCAB-001 | **As a user, I want to see vocabulary lists organized by topic** so I can learn words in context | 3 | P0 | 📋 TODO |
| VOCAB-002 | **As a user, I want to study flashcards** so I can memorize vocabulary effectively | 5 | P0 | 📋 TODO |
| VOCAB-003 | **As a user, I want to flip cards to see translation** so I can test my memory | 2 | P0 | 📋 TODO |
| VOCAB-004 | **As a user, I want to mark words as "known" or "learning"** so the app prioritizes difficult words | 3 | P0 | 📋 TODO |
| VOCAB-005 | **As a user, I want spaced repetition** so I review words at optimal intervals for memory | 8 | P1 | 📋 TODO |
| VOCAB-006 | **As a user, I want audio pronunciation** for each word so I can improve my pronunciation | 5 | P2 | 📋 TODO |
| VOCAB-007 | **As a user, I want example sentences** for each word so I understand usage | 3 | P1 | 📋 TODO |
| VOCAB-008 | **As a user, I want to track my vocabulary progress** so I see how many words I've learned | 3 | P1 | 📋 TODO |
| VOCAB-009 | **As a Premium user, I want vocabulary for all levels A1-C1** so I can expand my word bank | 5 | P2 | 📋 TODO |
| VOCAB-010 | **As a user, I want daily vocabulary reminders** so I maintain my study habit | 5 | P2 | 📋 TODO |

---

## EPIC 7: Writing Practice with AI Evaluation
*User submits writing → AI evaluates → feedback + score*

### User Stories

| ID | Story | Points | Priority | Status |
|----|-------|--------|----------|--------|
| WRITE-001 | **As a user, I want to write essays in a text editor** so I can practice writing | 3 | P0 | 📋 TODO |
| WRITE-002 | **As a user, I want to choose a writing prompt/topic** so I can practice specific exam tasks | 3 | P0 | 📋 TODO |
| WRITE-003 | **As a user, I want AI to evaluate my writing** so I get instant feedback on my essay | 8 | P0 | 📋 TODO |
| WRITE-004 | **As a user, I want a score for task completion** (did I answer the question?) | 3 | P0 | 📋 TODO |
| WRITE-005 | **As a user, I want a score for coherence/structure** (organization, paragraphs, transitions) | 3 | P0 | 📋 TODO |
| WRITE-006 | **As a user, I want a score for grammar** (accuracy of German grammar) | 3 | P0 | 📋 TODO |
| WRITE-007 | **As a user, I want a score for vocabulary range** (word choice, sophistication) | 3 | P0 | 📋 TODO |
| WRITE-008 | **As a user, I want detailed written feedback** explaining my mistakes so I can improve | 5 | P0 | 📋 TODO |
| WRITE-009 | **As a user, I want examples of improved sentences** so I can see better alternatives | 3 | P1 | 📋 TODO |
| WRITE-010 | **As a user, I want to track my writing history** so I see my improvement over time | 5 | P2 | 📋 TODO |
| WRITE-011 | **As a Premium user, I want 15 writings evaluated/month** so I have enough practice | 3 | P1 | 📋 TODO |
| WRITE-012 | **As a Standard user, I want 5 writings evaluated/month** so I have some AI feedback | 3 | P1 | 📋 TODO |
| WRITE-013 | **As a Free user, I want 1 writing evaluated/month** so I can try the feature | 3 | P2 | 📋 TODO |

---

## EPIC 8: Speaking Practice with AI Partner
*AI conversation partner that adapts to CEFR level*

### User Stories

| ID | Story | Points | Priority | Status |
|----|-------|--------|----------|--------|
| SPEAK-001 | **As a user, I want to practice speaking with an AI partner** so I can improve my spoken German | 8 | P0 | 📋 TODO |
| SPEAK-002 | **As a user, AI should adapt to my CEFR level** so the conversation is appropriate for my skill | 5 | P0 | 📋 TODO |
| SPEAK-003 | **As a user, I want topic-based conversations** (e.g., "At the doctor", "Job interview") so I practice relevant scenarios | 3 | P0 | 📋 TODO |
| SPEAK-004 | **As a user, I want AI to correct my mistakes gently** so I learn without feeling embarrassed | 5 | P1 | 📋 TODO |
| SPEAK-005 | **As a user, I want to record my voice** so AI can evaluate my pronunciation | 3 | P0 | 📋 TODO |
| SPEAK-006 | **As a user, I want feedback on my pronunciation** so I can improve my accent | 5 | P1 | 📋 TODO |
| SPEAK-007 | **As a user, I want feedback on my fluency** so I know if I speak too slowly or hesitantly | 3 | P2 | 📋 TODO |
| SPEAK-008 | **As a Premium user, I want unlimited AI speaking practice** so I can practice as much as I want | 5 | P1 | 📋 TODO |
| SPEAK-009 | **As a Standard user, I want 20 min/day AI speaking** so I have daily practice | 3 | P1 | 📋 TODO |
| SPEAK-010 | **As a Free user, I want 10 min/day AI speaking** so I can try the feature | 3 | P2 | 📋 TODO |
| SPEAK-011 | **As a user, I want conversation summaries** after each session so I can review what I learned | 3 | P2 | 📋 TODO |

---

## EPIC 9: Peer Speaking Exams
*Two users role-play an exam scenario, AI evaluates both*

### User Stories

| ID | Story | Points | Priority | Status |
|----|-------|--------|----------|--------|
| PEER-001 | **As a user, I want to join a peer exam room** so I can practice with another learner | 5 | P0 | 📋 TODO |
| PEER-002 | **As an examiner, I want to see exam questions/topic** so I can guide the exam | 3 | P0 | 📋 TODO |
| PEER-003 | **As two users, we want to exchange voice messages** back-and-forth so we simulate a real exam | 8 | P0 | 📋 TODO |
| PEER-004 | **As a user, I want a 15-minute max session timer** so exams stay within exam duration | 3 | P0 | 📋 TODO |
| PEER-005 | **As a user, I want AI to transcribe and evaluate both speakers** after the session so I get feedback | 8 | P0 | 📋 TODO |
| PEER-006 | **As a user, I want to see scores for: task completion, fluency, grammar, pronunciation** so I know my strengths | 5 | P0 | 📋 TODO |
| PEER-007 | **As a Premium user, I want 8 peer exams/month** so I have regular partner practice | 3 | P1 | 📋 TODO |
| PEER-008 | **As a Standard user, I want 4 peer exams/month** so I have some partner practice | 3 | P1 | 📋 TODO |
| PEER-009 | **As a Free user, I want 1 peer exam/month** so I can try the feature | 3 | P2 | 📋 TODO |
| PEER-010 | **As a user, I want to be matched with a partner** so I don't have to find my own partner | 5 | P2 | 📋 TODO |

---

## EPIC 10: Progress Tracking & Gamification
*Streaks, badges, statistics, achievements, level completion*

### User Stories

| ID | Story | Points | Priority | Status |
|----|-------|--------|----------|--------|
| PROG-001 | **As a user, I want to track my daily streak** so I'm motivated to study every day | 3 | P0 | 🔄 In Progress |
| PROG-002 | **As a user, I want to see lessons completed count** so I know how much I've studied | 2 | P0 | 🔄 In Progress |
| PROG-003 | **As a user, I want to earn badges for achievements** so I feel rewarded for my progress | 5 | P1 | 📋 TODO |
| PROG-004 | **As a user, I want to see per-level progress** so I know how close I am to completing B2 | 3 | P1 | 📋 TODO |
| PROG-005 | **As a user, I want to see per-subject progress** so I know which subjects I've mastered | 3 | P1 | 📋 TODO |
| PROG-006 | **As a user, I want weekly progress summaries** so I can review my learning | 5 | P2 | 📋 TODO |
| PROG-007 | **As a user, I want to see my rank on a leaderboard** so I can compete with other learners | 8 | P2 | 📋 TODO |
| PROG-008 | **As a user, I want streak freeze** so I don't lose my streak if I miss a day | 3 | P2 | 📋 TODO |
| PROG-009 | **As a user, I want to see time studied statistics** so I can track my learning investment | 3 | P3 | 📋 TODO |
| PROG-010 | **As a Premium user, I want complete analytics dashboard** so I have full insight into my progress | 5 | P2 | 📋 TODO |

---

## EPIC 11: Home Dashboard
*Main screen, level grid, feature buttons, daily motivation*

### User Stories

| ID | Story | Points | Priority | Status |
|----|-------|--------|----------|--------|
| HOME-001 | **As a user, I want to see my welcome message** so the app feels personalized | 1 | P0 | ✅ Done |
| HOME-002 | **As a user, I want to see the CEFR level grid** so I can select my level | 2 | P0 | ✅ Done |
| HOME-003 | **As a user, I want feature buttons** (Lessons, Quizzes, Vocabulary, Writing, Speaking, Subjects) so I can access all modules | 2 | P0 | ✅ Done |
| HOME-004 | **As a user, I want to see my current streak** so I'm motivated to continue | 1 | P0 | ✅ Done |
| HOME-005 | **As a user, I want to see lessons completed count** so I see my progress | 1 | P0 | ✅ Done |
| HOME-006 | **As a user, I want to see my current level indicator** so I know which level is active | 1 | P0 | ✅ Done |
| HOME-007 | **As a user, I want a logout button** so I can sign out of my account | 1 | P0 | ✅ Done |
| HOME-008 | **As a user, I want daily motivational tips** so I feel encouraged | 3 | P3 | 📋 TODO |
| HOME-009 | **As a user, I want to see recommended next action** so I know what to study next | 3 | P3 | 📋 TODO |

---

## EPIC 12: Content Management (Admin)
*AI content generation, Firestore content management, Firebase imports*

### User Stories

| ID | Story | Points | Priority | Status |
|----|-------|--------|----------|--------|
| ADMIN-001 | **As a developer, I want to generate B2 reading content via AI** so I can scale content quickly | 13 | P0 | 📋 TODO |
| ADMIN-002 | **As a developer, I want to import content to Firestore** so content appears in the app | 5 | ✅ Done (Topics 1-4) |
| ADMIN-003 | **As a developer, I want to manage content via JSON files** so non-technical content can be added | 3 | 📋 TODO |
| ADMIN-004 | **As a developer, I want quiz questions auto-generated per reading** so I don't have to write them manually | 8 | 📋 TODO |
| ADMIN-005 | **As a developer, I want to track content completion status** so I know what's missing | 3 | 📋 TODO |
| ADMIN-006 | **As a developer, I want to add new B2 topics easily** so the curriculum grows over time | 5 | 📋 TODO |
| ADMIN-007 | **As a developer, I want A1-C1 content structure** so all levels have proper content | 13 | 📋 TODO |

---

## EPIC 13: Firebase Backend & Data
*Firestore data models, Firebase Auth, Firebase Storage, Security Rules*

### User Stories

| ID | Story | Points | Priority | Status |
|----|-------|--------|----------|--------|
| FB-001 | **As a developer, I want Firebase Auth working** so users can sign up/log in | 3 | ✅ Done |
| FB-002 | **As a developer, I want Firestore data structure** for readings, questions, vocabulary, users, progress | 5 | 🔄 In Progress |
| FB-003 | **As a developer, I want Firebase Storage for audio files** so listening content works | 5 | 📋 TODO |
| FB-004 | **As a developer, I want proper security rules** so users can only read/write their own data | 5 | 📋 TODO |
| FB-005 | **As a developer, I want analytics integration** so I can track user behavior | 5 | 📋 TODO |
| FB-006 | **As a developer, I want Firebase Crashlytics** so I can track and fix crashes | 3 | 📋 TODO |

---

## 📊 SUMMARY STATISTICS

| Metric | Count |
|--------|-------|
| **Total Epics** | 13 |
| **Total User Stories** | 103 |
| **✅ Done** | 23 |
| **🔄 In Progress** | 8 |
| **📋 TODO** | 72 |

### Priority Breakdown
- **P0 (Must Have):** 42 stories
- **P1 (Should Have):** 35 stories  
- **P2 (Nice to Have):** 21 stories
- **P3 (Later):** 5 stories

### Effort Breakdown (Story Points)
- **1-2 points:** 33 stories (quick wins)
- **3-5 points:** 53 stories (medium)
- **8-13 points:** 17 stories (epics in themselves)

---

## 🚀 MVP (Minimum Viable Product) — First Release

### Must Have for MVP:
1. ✅ AUTH-001, AUTH-002, AUTH-004 (Auth basic)
2. ✅ LEVEL-001, LEVEL-002, LEVEL-005, LEVEL-006 (Level selection)
3. ✅ SUBJ-001 → SUBJ-008 (Subject → Quiz → Results flow)
4. ✅ QUIZ-001 → QUIZ-009 (Quiz system)
5. ✅ READ-001 → READ-007 (Reading comprehension)
6. ✅ HOME-001 → HOME-007 (Home dashboard)
7. ✅ PROG-001, PROG-002 (Basic progress tracking)
8. ✅ FB-001, FB-002 (Firebase basics)

### MVP Estimated: ~34 story points across all epics

---

## 📅 RELEASE PLANNING

### Release 1.0 — MVP (Month 1)
- Auth + Level Selection + Home Dashboard
- Subject → Quiz → Results Flow
- B2 Reading (Topics 1-4) + Quiz
- Basic Progress (Streaks, Counters)
- Firebase Backend

### Release 1.1 — +Vocabulary (Month 2)
- Flashcard system
- Vocabulary lists per topic
- Spaced repetition

### Release 1.2 — +Writing AI (Month 2-3)
- Writing practice with AI evaluation
- Writing history tracking

### Release 1.3 — +Speaking AI (Month 3)
- AI speaking partner
- Voice recording + pronunciation feedback

### Release 1.4 — +Peer Exams (Month 3-4)
- Peer exam rooms
- AI evaluation of both speakers

### Release 2.0 — +A1-C1 All Levels (Month 4-5)
- Expand content to all CEFR levels
- Premium tier launch

---

_Last updated: 2026-04-25_
_Maintain: Add new stories here as features are discovered or requested_
