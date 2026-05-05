# B2 Deutsch App — Session Guidance
## Developer Notes & Roadmap

**Last Updated:** 2026-04-25 20:20 UTC
**Session History:** See SESSION LOG at bottom

---

## 1. WHAT WE ARE BUILDING

### App Overview
**Name:** B2 Deutsch — Prüfungsvorbereitung
**Platform:** Android (Kotlin + Jetpack Compose)
**Package:** `com.b2deutsch.app`
**Firebase Project:** `b2-deutsch-app`
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
- [x] Hilt dependency injection setup

### ✅ Authentication
- [x] LoginFragment with email/password
- [x] SignUpFragment with display name
- [x] AuthViewModel with Firebase Auth
- [x] Navigation: login → home flow
- [x] Logout functionality

### ✅ Home Dashboard (SIMPLIFIED — 2026-04-25)
- [x] Header with welcome message
- [x] Level selection grid (A1, A2, B1, B2, C1)
- [x] **Red "📝 EXAMS" card** below C1 level
- [x] NO streak/lessons cards (removed)
- [x] NO feature buttons (removed)
- [x] NO logout buttons (removed)

### ✅ Subject → Quiz → Results Flow
- [x] SubjectListFragment — **23 numbered B2 topics** (no category filters)
- [x] SubjectAdapter
- [x] SubjectDetailFragment — description + tips + "Quiz starten" button
- [x] SubjectResultFragment — detailed results with explanations
- [x] QuizResultAdapter for per-question display
- [x] **NO "Zurück zur Übersicht" button** (removed)

### ✅ 23 B2 Grammar Topics (2026-04-25)
Each topic has: 2-paragraph description, examples, learning tips, quiz button

| # | Topic | Turkish |
|---|-------|---------|
| 1 | Konnektoren: als, bevor, bis, seitdem, während, wenn | Bağlaçlar |
| 2 | Konnektoren: sobald, solange | Bağlaçlar |
| 3 | Verben und Ergänzungen | Fiiller ve Tamamlayıcılar |
| 4 | Zeitformen in der Vergangenheit | Geçmiş Zaman |
| 5 | Zeitformen der Zukunft | Gelecek Zaman |
| 6 | Futur mit werden | Gelecek Zaman |
| 7 | Angaben im Satz | Cümledeki İfadeler |
| 8 | Verneinung mit nicht | Olumsuzluk |
| 9 | Negationswörter | Olumsuzluk Kelimeleri |
| 10 | Passiv Präteritum | Edilgen Yapı |
| 11 | Konjunktiv II der Vergangenheit | Geçmiş Zaman Konj. II |
| 12 | Konjunktiv II mit Modalverben | Modal Fiiller |
| 13 | Pronomen: einander | Zamirler |
| 14 | Weiterführende Nebensätze | Yan Cümlecikler |
| 15 | Präpositionen mit Genitiv | Genitiv ile Prepozisyonlar |
| 16 | je und desto/umso + Komparativ | Karşılaştırmalar |
| 17 | Nomen-Verb-Verbindungen | İsim-Fiil Bağlantıları |
| 18 | Folgen ausdrücken | Sonuçları İfade Etme |
| 19 | Ausdrücke mit Präpositionen | Prepozisyonlarla İfadeler |
| 20 | irreale Konditionalsätze | Gerçek Dışı Koşul |
| 21 | Relativsätze im Genitiv | İlgili Cümleler |
| 22 | Konjunktiv I in der indirekten Rede | Dolaylı Anlatım |
| 23 | Konjunktiv II in irrealen Vergleichssätzen | Gerçek Dışı Karşılaştırma |

### ✅ Exams Module (CORE FEATURE)
- [x] ExamsFragment — 4 exam types per level
- [x] ExamActiveFragment — timer, questions, navigation
- [x] ExamResultFragment — score display, pass/fail
- [x] Navigation: Home → Exams → ExamActive → ExamResult

### ✅ B2 Reading Comprehension Content
- [x] 40 texts, 200 questions, 320 vocabulary items (Topics 1-4)
- [x] Topics 5-12 still needed

### ✅ Documentation
- [x] ROADMAP.md
- [x] ARCHITECTURE.md
- [x] PRODUCT_BACKLOG.md — 13 epics, 103 user stories
- [x] SESSION_GUIDANCE.md — This file
- [x] PROJECT_STATUS.md

---

## 3. NEXT STEPS

### 🔴 NEXT — b2_10 Content Generation
1. Generate 100 questions for b2_10 Passiv Präteritum
2. Push to GitHub + Firestore
3. Continue with b2_11 through b2_23

### 🔴 AFTER THAT — Complete Remaining Topics
1. b2_10 through b2_23 — all need real content (currently placeholders)
2. Push each topic to Firestore after completion
3. ~15 topics remaining × ~100 questions each

### 🔴 FIREBASE SYNC (from local machine)
```bash
cd /Users/halilozturk/b2-deutsch-app
node scripts/import_and_sync.js b2_08   # push completed topic
node scripts/import_and_sync.js b2_09   # push next topic
```

---

## 📋 SESSION LOG

### Session: 2026-05-05 21:27 UTC — b2_09 COMPLETE at 100 Questions! (v1.5)
**Summary:** b2_09 fully expanded from 20 to 100 questions across 5 batches.

**b2_09 Question Batches:**
- q001-q020 (v1.1): Initial 20 + 7 Lerntipps — nichts, nie/niemals, niemand, kein, nirgends, weder...noch
- q021-q040 (v1.2): +20 — nichts, niemand, nirgends, nie, jemand contexts
- q041-q060 (v1.3): +20 — nichts/kein/nie/Niemand/nirgendwo/niemals
- q061-q080 (v1.4): +20 — weder...noch, jemand/niemand, nichts/niemand/nirgendwo/nie/kein
- q081-q100 (v1.5): +20 — ohne, nicht nur...sondern auch, noch nie, nicht mehr, Wo...auch, Als, zeitweise

**Next Topic:** b2_10 Passiv Präteritum

---

### Session: 2026-05-05 21:18 UTC — b2_09 Negationswörter Replaced + 7 Lerntipps Added
**Summary:** b2_09 had 100 wrong placeholder questions (Konnektoren content). Replaced all with 20 real Negationswörter questions + 7 Lerntipps.

**b2_09 What Was Done:**
- Deleted 100 wrong placeholder questions
- Added 20 real questions (q001-q020): nichts, nie/niemals, niemand (3 cases), kein, nirgends/nirgendwo, weder...noch, keiner
- Added 7 Lerntipps: nichts, nie/niemals, niemand, kein, nirgends/nirgendwo, weder...noch, keiner/keine/kein
- Lerntipps include: title, content (with Beispiele), icon

**Next Topic:** b2_09 needs 80 more questions (q021-q100). Then b2_10 Passiv Präteritum.

---

### Session: 2026-05-05 20:38 UTC — b2_08 Expanded to 100 Questions!
**Summary:** b2_08 Verneinung mit nicht expanded from 20 to 100 questions across 5 batches.

**b2_08 Question Batches Added:**
- q101-q120 (v1.2): Initial 20 — nicht vs kein, Perfekt, nicht...sondern
- q121-q140 (v1.3): +20 — trennbare Verben, Zeitausdrücke, Possessivpronomen
- q141-q160 (v1.4): +20 — Infinitivsatz, Mastar grupları, Nomen, Redewendungen (kein/nichts)
- q161-q180 (v1.5): +20 — Perfekt, Modalverben, einfache nicht-Fragen
- q181-q200 (v1.6): +20 — Perfekt, Nebensatz, Passiv, Infinitivsatz mit zu, Relativsatz

**Files Updated:**
- `app/src/main/assets/b2_08.json` — version 1.6, 100 questions
- `PROJECT_STATUS.md` — updated topic table + session log
- `PRODUCT_BACKLOG.md` — ADMIN-002 updated (Topics 1-8 now complete)

**Next Topic to Work On:** b2_10 Passiv Präteritum

---

### Session: 2026-04-25 18:30 UTC
**Summary:** Major UI overhaul — simplified home, 23 numbered B2 topics, removed filters.

**Home Screen (Simplified):**
- Removed streak/lessons cards
- Removed feature buttons
- Removed logout buttons
- Added red EXAMS card below C1

**Subject List:**
- Removed: Alle, Grammatik, Lesen, Wortschatz chips
- Added: 23 numbered grammar topics with Turkish explanations
- Each topic: 2 paragraphs description + examples + tips
- "Quiz starten" button kept, "Zurück zur Übersicht" removed

**Bug Fixes:**
- QuizResult import (data model not ui.quiz)
- selectedId type mismatch
- exams_to_exams navigation
- gray_600, gray_700, gray_100 colors added

---

_Last updated: 2026-05-05 21:04 UTC_
