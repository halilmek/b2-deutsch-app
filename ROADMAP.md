# b2-deutsch-app — Project Roadmap & Agent Memory

> ⚠️ **TOKEN NEEDED**: Halil provides at start of each session
> Store token in `~/.openclaw/workspace/TOOLS.md` at runtime — never hardcode
> Remote URL format: `https://[TOKEN]@github.com/halilmek/b2-deutsch-app.git`

---

## 📁 Project Structure

- **Local Mac path**: `/Users/halilozturk/b2-deutsch-app`
- **Sandbox path**: `/home/node/.openclaw/workspace/b2-deutsch-app`
- **GitHub repo**: `https://github.com/halilmek/b2-deutsch-app`
- **Firebase creds**: `/Users/halilozturk/Documents/b2-deutsch-app-firebase-adminsdk-fbsvc-4aa25c0ca2.json`
- **google-services.json**: `/Users/halilozturk/Downloads/google-services.json`

---

## 🔄 Standard Workflow

1. **I code in sandbox** → commit → push to GitHub
2. **Halil pulls** on his Mac: `git pull origin main`
3. **Halil syncs to Firestore**: `node scripts/import_and_sync.js <module>`

---

## 🔑 GitHub Push Constraints
- **Never put raw tokens in files that get pushed to GitHub** → use placeholders
- Sandbox pushes work via token-in-URL ✅

---

## 📋 Module Naming
- JSON: `app/src/main/assets/b2_XX.json` or `a1_XX.json`
- Topics: b2_01–b2_23, a1_01–a1_10, a2_01–a2_10, etc.
- Sync: `scripts/import_and_sync.js <module>`

---

## 📝 Documentation Rule

After every task, update ROADMAP.md with WHAT we did + FILES CHANGED.

---

## 🗺️ Roadmap — Done & Next

### ✅ Completed (2026-05-12)
- [x] `b2_17`–`b2_23`: 100 questions each + descriptions + tips ✅
- [x] **C2 button** added to level selector + HomeViewModel fix ✅
- [x] **A2, B1, C1, C2**: each expanded to 10 grammar topics ✅
- [x] **A1 JSON files**: 10 files × 50 MCQ = 500 questions ✅
  - a1_01: Verben konjugieren | a1_02: Nomen und Artikel | a1_03: Präsens
  - a1_04: Akkusativ | a1_05: Dativ | a1_06: Präpositionen
  - a1_07: Verben mit Präpositionen | a1_08: Perfekt | a1_09: Modalverben | a1_10: Sätze bilden
- [x] **A1/A2/B1/C1/C2 descriptions**: fixed Chinese characters → German ✅

### 🚨 Pending Fixes
- [ ] `b2_15`: missing description
- [ ] `b2_16`: topicName wrong + missing description

### 📋 Backlog
- `b2_02`: Has questions but no topic entry in app
- A2, B1, C1, C2: topics defined but no questions yet (quizCount = 0)

---

## 📚 How We Do Things

### Add questions to existing topic
1. Edit `app/src/main/assets/b2_XX.json` or `a1_XX.json`
2. Add question objects (keep `id` unique: `b2_XX_q001`, etc.)
3. Update `totalQuestions`
4. Commit + push + sync

### Fix topicName or description
1. Edit `SubjectListViewModel.kt` — find the b2_XX entry
2. Update the field
3. Commit + push + sync

---

## 🧠 Session Start

Say: "Ready for b2-deutsch-app. Token: [TOKEN]"

---

## 📄 Key Files

```
b2-deutsch-app/
├── app/src/main/assets/          # b2_XX.json, a1_XX.json — question data
├── app/src/main/java/.../
│   └── SubjectListViewModel.kt   # topic names + descriptions
└── scripts/
    └── import_and_sync.js        # Firebase sync script
```