# CLAUDE.md — Agent Entry Point

Before doing ANYTHING in this repo, read in this order:
1. `docs/AGENT_WORKFLOW.md` — the mandatory process for every task
2. `docs/ROLES.md` — announce which role you are acting in
3. `docs/MONETIZATION_SPEC.md` — required if the task touches quizzes, exams, writing, speaking, or payments
4. `ARCHITECTURE.md` — data model & level-agnostic design rules
5. `PROJECT_STATUS.md` — current state; update it before ending your session

Hard rules (violations = rejected work):
- No secrets/API keys in the repo or in the Android app. AI calls only via `functions/`.
- Entitlements & weekly quotas enforced server-side.
- No hardcoded CEFR levels.
- Update `PROJECT_STATUS.md` at session end.
