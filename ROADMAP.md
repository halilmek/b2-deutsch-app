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

### Step 1 — I code in sandbox
I work in `/home/node/.openclaw/workspace/b2-deutsch-app`. Halil tells me what to build/fix.

### Step 2 — I push to GitHub
```bash
cd /home/node/.openclaw/workspace/b2-deutsch-app
git remote set-url origin "https://[TOKEN]@github.com/halilmek/b2-deutsch-app.git"
git add .
git commit -m "description"
git push origin main
```

### Step 3 — Halil pulls on his Mac
```bash
cd /Users/halilozturk/b2-deutsch-app
git pull origin main
```

### Step 4 — Halil syncs to Firestore
```bash
export GOOGLE_APPLICATION_CREDENTIALS="/Users/halilozturk/Documents/b2-deutsch-app-firebase-adminsdk-fbsvc-4aa25c0ca2.json"
cd /Users/halilozturk/b2-deutsch-app
node scripts/import_and_sync.js <module>   # e.g. b2_09, b2_10, etc.
```

---

## 🔑 GitHub Push Constraints
- **Never put raw tokens in files that get pushed to GitHub** → use placeholders
- Sandbox pushes work via token-in-URL ✅

---

## 📋 Module Naming Convention

- JSON files: `app/src/main/assets/b2_XX.json`
- Topics: `b2_01` through `b2_23`
- Sync script: `scripts/import_and_sync.js <b2_XX>`

---

## 📝 Documentation Rule

After every task, update ROADMAP.md:
1. **WHAT** we did
2. **FILES CHANGED**

---

## 🗺️ Roadmap — What's Done & What's Next

### ✅ Completed
- [x] `b2_17`: 100 Nomen-Verb-Verbindungen questions ✅, description ✅ (2026-05-12)
- [x] `b2_18`: 100 Folgen ausdrücken questions ✅, description ✅, tips ✅ (2026-05-12)
- [x] `b2_19`: 100 Ausdrücke mit Präpositionen questions ✅, description ✅, tips ✅ (2026-05-12)

### 🚨 Pending Fixes
- [ ] `b2_15`: missing description
- [ ] `b2_16`: topicName wrong + missing description

### 📋 Backlog
- `b2_02`: Has questions but no topic entry in app
- `b2_18` to `b2_23`: other modules may need content review

---

## 📚 How We Do Things

### Add questions to existing topic
1. Edit `app/src/main/assets/b2_XX.json`
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
├── app/src/main/assets/          # b2_XX.json — question data
├── app/src/main/java/.../
│   └── SubjectListViewModel.kt   # topic names + descriptions
└── scripts/
    └── import_and_sync.js        # Firebase sync script
```