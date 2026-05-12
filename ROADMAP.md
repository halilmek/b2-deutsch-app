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

---

## 📋 Module Naming Convention

- JSON files: `app/src/main/assets/b2_XX.json` (e.g. `b2_09.json`, `b2_17.json`)
- Topics: `b2_01` through `b2_23`
- Sync script: `scripts/import_and_sync.js <b2_XX>`

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

## 🧠 How to Make Me Remember (per session)

Halil, here's how to set me up quickly each session:

### Option A — At session start, just say:
> "Load project: b2-deutsch-app. GitHub: halilmek, token: [TOKEN]. Firebase creds on your Mac."

### Option B — I auto-read from these files (already set up):
- `MEMORY.md` — long-term memory (loaded in main session)
- `TOOLS.md` — current project state and credentials
- `memory/YYYY-MM-DD.md` — daily session logs

### Option C — Give me a task directly:
> "Fix b2_16 topicName and add description" → I do it, push to GitHub, you pull + sync.

---

## 📄 File Locations in Sandbox

```
b2-deutsch-app/
├── app/
│   └── src/
│       └── main/
│           ├── assets/          # b2_XX.json files
│           │   ├── b2_09.json
│           │   ├── b2_10.json
│           │   └── ...
│           └── java/.../
│               └── SubjectListViewModel.kt  # topic names + descriptions
└── scripts/
    └── import_and_sync.js       # Firebase sync script
```