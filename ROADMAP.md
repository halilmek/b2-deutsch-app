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
From sandbox:
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

- **From sandbox (Linux)**: Can push directly using token in URL → works ✅
- **From Halil's Mac**: Use normal `git push origin main` → works ✅
- **Never put raw tokens in files that get pushed to GitHub** → use placeholders

---

## 📋 Module Naming Convention

- JSON files: `app/src/main/assets/b2_XX.json` (e.g. `b2_09.json`, `b2_17.json`)
- Topics: `b2_01` through `b2_23`
- Sync script: `scripts/import_and_sync.js <b2_XX>`

---

## 📝 Documentation Rule (IMPORTANT)

After every task, update ROADMAP.md with:
1. **WHAT** we did — the feature/fix
2. **METHOD/TECHNIQUE** — how we did it (patterns, file changes, approach)
3. **FILES CHANGED** — which files were modified

This way future-me knows HOW we built things, not just WHAT.

---

## 🗺️ Roadmap (Known Issues & Backlog)

### 🚨 Pending Fixes
- [ ] `b2_16`: topicName says "Nomen-Verb-Verbindungen" but should be "je und desto/umso + Komparativ"
- [ ] `b2_16`: missing description (Turkish → English grammar explanation)
- [ ] `b2_15`: missing description (Turkish → English grammar explanation)

### 📝 In Progress
- [ ] NVV content for `b2_17` (20 questions added ✅, topicName ✅, description ✅)

### 📋 Backlog
- `b2_18` to `b2_23`: Placeholder modules, need full content
- `b2_02`: Has questions but no topic entry in app

---

## 📚 Completed Methods/Techniques Log

### How to add a new topic (b2_XX)
1. Create `app/src/main/assets/b2_XX.json` with questions array
2. Add topic entry in `SubjectListViewModel.kt` with:
   - `id = "b2_XX"`
   - `topicName` (German)
   - `description` (Turkish → English grammar explanation)
   - `tips` (optional study tips)
3. Add `100` (or custom count) questions in JSON
4. Sync: `node scripts/import_and_sync.js b2_XX`

### How to fix a topicName or description
1. Edit `SubjectListViewModel.kt` — find the b2_XX entry
2. Update `topicName` or `description` field
3. Commit + push + sync same module

### How to add questions to existing topic
1. Edit `app/src/main/assets/b2_XX.json`
2. Add new question objects to the array
3. Commit + push + sync

---

## 🧠 How to Make Me Ready Each Session

### At session start:
> "Ready for b2-deutsch-app. Token: [TOKEN]"

I will:
1. Read `TOOLS.md` for project paths and state
2. Read `ROADMAP.md` for current backlog
3. Configure git remote with provided token

### Give me a task directly:
> "Fix b2_16 topicName and add description" → I do it, push, you pull + sync.

---

## 📄 Key Files in Sandbox

```
b2-deutsch-app/
├── app/src/main/assets/          # b2_XX.json — question data
├── app/src/main/java/.../
│   └── SubjectListViewModel.kt   # topic names + descriptions + tips
└── scripts/
    └── import_and_sync.js        # Firebase sync script
```