# B2 Deutsch App — PROJECT STATUS

**Last Updated:** 2026-04-26 23:50 UTC
**GitHub:** https://github.com/halilmek/b2-deutsch-app
**Firebase Project:** b2-deutsch-app (project_number: 419122108874)
**Firebase Storage:** b2-deutsch-app.firebasestorage.app

---

## 🔴 CRITICAL — b2_questions.json WAS CORRUPTED

**What happened:** The `gen_merged_topic1.py` script (run during Topic 1 merge) copied the same 96 konnektor questions across ALL 22 topics in `b2_questions.json`. Every topic 2–23 was filled with duplicate copies of Topic 1's questions.

**Total questions in JSON:** 2,246 | **Unique texts:** 191 | **Duplicates:** 2,005

**Fix applied (2026-04-26):**
- Added 50 Topic 2 questions to `b2_questions.json`
- Bumped SharedPreferences `quiz_progress_prefs_v4` to clear cached questions
- Topic 2 now has correct 50 questions in local JSON
- Topic 1 was already correct in JSON (96 konnektor questions)

---

## 📋 CURRENT QUESTION STATUS

### Local `b2_questions.json`
| Topic | ID | Questions | Content | Status |
|-------|-----|---------|---------|--------|
| 1 | b2_01 | 96 | Konnektoren (als, bevor, bis...) | ✅ Correct |
| 2 | b2_02 | 50 | Verben und Ergänzungen (Reflexive + Präpositionen) | ✅ Correct |
| 3-23 | b2_03–b2_23 | 100 each | **ALL WRONG** — duplicate konnektor questions | ❌ Need rebuild |

### Firebase `moduleQuizQuestions`
| Topic | Questions | Content | Status |
|-------|-----------|---------|--------|
| 1 | 96 | Konnektoren | ✅ Ready |
| 2 | 50 | Verben und Ergänzungen | ✅ Ready |
| 3-23 | 0 | — | ❌ Need import |

---

## 🔌 APP FLOW (How Questions Are Loaded)

```
Quiz starts
    │
    ▼
QuizViewModel.startQuiz(subjectId)
    │
    ▼
LocalQuestionBank.getNextQuiz(context, subjectId)
    │
    ├─► Reads from b2_questions.json (LOCAL ASSET)
    │
    ├─► topicId = "b2_01" → gets 96 questions from JSON
    │
    └─► topicId = "b2_02" → gets 50 questions from JSON ✅ NEW
            │
            ▼
    SharedPreferences tracks active/passive Q IDs
```

**Firebase `moduleQuizQuestions` is NOT read by the app yet.**
It exists as a cloud backup and for future sync features.

---

## 📌 TOPIC LIST (B2 — 22 Topics)

| # | ID | Topic Name | Questions in JSON | Questions in Firebase |
|---|-----|------------|-----------------|---------------------|
| 1 | b2_01 | Konnektoren | 96 ✅ | 96 ✅ |
| 2 | b2_02 | Verben und Ergänzungen | 50 ✅ | 50 ✅ |
| 3 | b2_03 | Zeitformen in der Vergangenheit | 100 ❌ | 0 |
| 4 | b2_04 | Zeitformen der Zukunft | 100 ❌ | 0 |
| 5 | b2_05 | Futur mit werden | 100 ❌ | 0 |
| 6 | b2_06 | Angaben im Satz | 100 ❌ | 0 |
| 7 | b2_07 | Verneinung mit nicht | 100 ❌ | 0 |
| 8 | b2_08 | Negationswörter | 100 ❌ | 0 |
| 9 | b2_09 | Passiv Präteritum | 100 ❌ | 0 |
| 10 | b2_10 | Konjunktiv II der Vergangenheit | 100 ❌ | 0 |
| 11 | b2_11 | Konjunktiv II mit Modalverben | 100 ❌ | 0 |
| 12 | b2_12 | Pronomen: einander | 100 ❌ | 0 |
| 13 | b2_13 | Weiterführende Nebensätze | 100 ❌ | 0 |
| 14 | b2_14 | Präpositionen mit Genitiv | 100 ❌ | 0 |
| 15 | b2_15 | je und desto/umso + Komparativ | 100 ❌ | 0 |
| 16 | b2_16 | Nomen-Verb-Verbindungen | 100 ❌ | 0 |
| 17 | b2_17 | Folgen ausdrücken | 100 ❌ | 0 |
| 18 | b2_18 | Ausdrücke mit Präpositionen | 100 ❌ | 0 |
| 19 | b2_19 | Irreale Konditionalsätze | 100 ❌ | 0 |
| 20 | b2_20 | Relativsätze im Genitiv | 100 ❌ | 0 |
| 21 | b2_21 | Konjunktiv I in der indirekten Rede | 100 ❌ | 0 |
| 22 | b2_22 | Konjunktiv II in irrealen Vergleichssätze | 100 ❌ | 0 |

---

## 🛠️ WHAT NEEDS TO BE DONE

### Priority 1 — Topics 3–23: Rebuild JSON Content
- Generate 100 proper grammar questions per topic
- Match Firebase schema: `{id, subjectId, level, questionText, options, correctAnswer, explanation, type, difficulty, tags}`
- You provide curated questions OR I generate with AI

### Priority 2 — Firebase Import for Topics 3–23
- Create import scripts per topic (same as `firebase_import_topic2_verben.js`)
- Run on MacBook after regenerating `b2_questions.json`

### Priority 3 — App Enhancement (Future)
- Add Firebase fallback: if topic not found in `b2_questions.json`, query `moduleQuizQuestions` by topicNumber
- This enables cloud sync and content updates without app rebuilds

---

## 📁 KEY FILES

### Firebase Scripts
- `content/reading/firebase_import_konnektoren.js` — Topic 1 (96 Q) → Firebase ✅
- `content/reading/firebase_import_topic2_verben.js` — Topic 2 (50 Q) → Firebase ✅
- `content/reading/firebase_fix_bis.js` — Fix 3 wrong bis questions in Firebase ✅
- `content/reading/firebase_delete_old_konnektoren.js` — Cleanup script (ran, found 0 docs)

### App Files
- `app/src/main/assets/b2_questions.json` — Local question bank (CORRUPTED — needs fix for Topics 3–23)
- `app/src/main/java/.../LocalQuestionBank.kt` — Active/passive tracking, SharedPreferences v4
- `app/src/main/java/.../QuizViewModel.kt` — Quiz logic, reads from LocalQuestionBank

### Architecture
- **Primary source:** `b2_questions.json` (local asset, bundled in app)
- **Cloud backup:** Firebase `moduleQuizQuestions` (per-topic collections)
- **Progress:** SharedPreferences (offline, fast)
- **Two collections:** `grammarQuizBank` (general) + `moduleQuizQuestions` (B2 module)

---

## 🔗 FIREBASE CONSOLE LINKS

- **moduleQuizQuestions:** https://console.firebase.google.com/project/b2-deutsch-app/firestore/data~2FmoduleQuizQuestions
- **grammarQuizBank:** https://console.firebase.google.com/project/b2-deutsch-app/firestore/data~2FgrammarQuizBank
- **Firestore Rules:** https://console.firebase.google.com/project/b2-deutsch-app/firestore/rules

---

_Last updated: 2026-04-26 23:50 UTC_
