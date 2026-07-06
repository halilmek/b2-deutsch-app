# AGENT_WORKFLOW.md — Development Process for AI Agents & Contributors

> **Read this first.** Any agent (Claude Code, Copilot, etc.) or human starting work on this repo must follow this process. Read ARCHITECTURE.md, PROJECT_STATUS.md and ROLES.md before writing code.

## 0. Project Summary
Android (Kotlin) German exam-prep app (A1–C1, B2 first). Firebase backend (Auth, Firestore, Storage, Cloud Functions). Freemium model — see MONETIZATION_SPEC.md for exact entitlement rules. Level-agnostic core: adding a level = adding content, never new code paths.

## 1. Golden Rules
1. **Never hardcode a CEFR level** in UI or logic. `level: String` is always a parameter.
2. **Never put API keys, tokens, or secrets in the repo.** AI calls go through Cloud Functions (`functions/`), never directly from the app.
3. **Entitlement checks are server-side.** Client UI may hide buttons, but quotas (1 exam/week etc.) are enforced in Firestore rules + Cloud Functions. Client-side-only checks are a bug.
4. **Small commits, one concern per commit.** Conventional Commits format: `feat:`, `fix:`, `content:`, `docs:`, `refactor:`, `test:`.
5. **Update PROJECT_STATUS.md at the end of every session** — what was done, what's next, open blockers.
6. **Don't regenerate existing content.** Question banks live in `content/`. Extend, don't overwrite.

## 2. Standard Task Lifecycle
Every task goes through these phases. Skip nothing.

| Phase | Owner (see ROLES.md) | Output |
|---|---|---|
| 1. Pick task | Product Owner role | Item from PRODUCT_BACKLOG.md, acceptance criteria written |
| 2. Design check | Architect role | Confirm fit with ARCHITECTURE.md; if it changes data model → update ARCHITECTURE.md first |
| 3. Implement | Developer role | Kotlin code + Firestore rules if needed |
| 4. Test | QA role | Unit tests for logic; manual test checklist for UI; entitlement edge cases MUST be tested |
| 5. Content | Content Engineer role | Only if task involves questions/lessons/audio |
| 6. Document & close | Developer role | Update PROJECT_STATUS.md, mark backlog item done |

## 3. Definition of Done
A task is done only when:
- [ ] Builds with `./gradlew assembleDebug` without warnings introduced by the change
- [ ] Entitlement rules (free vs premium, weekly quotas) respected server-side
- [ ] No secrets committed (`git diff` reviewed)
- [ ] Strings externalized to `res/values/strings.xml` (app UI is German/Turkish-ready)
- [ ] PROJECT_STATUS.md updated
- [ ] Firestore rules updated + noted if data model changed

## 4. Branch & PR Convention
- `main` = always buildable
- Feature branches: `feat/<short-name>`, content branches: `content/<level>-<topic>`
- Agents working locally may commit directly to a feature branch, never force-push `main`.

## 5. Session Start Checklist (for AI agents)
1. `git pull` and read PROJECT_STATUS.md (current state) 
2. Read the backlog item you're assigned
3. Read MONETIZATION_SPEC.md if the task touches quizzes/exams/writing/speaking
4. State your plan in 3–5 bullet points before editing files
5. Work → test → update docs → commit

## 6. Directory Map
```
app/          Android app (Kotlin)
functions/    Cloud Functions (AI calls, quota enforcement, TTS)
content/      Question banks, lessons, song lyrics (JSON) — source of truth
scripts/      Python content-generation & upload scripts
docs/         This folder: process, roles, monetization spec
```
