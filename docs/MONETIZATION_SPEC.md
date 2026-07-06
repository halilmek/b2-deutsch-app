# MONETIZATION_SPEC.md — Entitlement Rules (Source of Truth)

**Core principle:** Static content (no runtime AI cost) is FREE. Anything requiring an active AI reaction/feedback is PREMIUM.

Any code touching quizzes, exams, writing or speaking MUST conform to this table. Client hides UI; **server enforces**.

## Tiers

| Feature | Free | Premium |
|---|---|---|
| Grammar lessons & general info | ✅ Unlimited | ✅ Unlimited |
| Grammar songs (1-min audio, Suno-generated) | ✅ Unlimited | ✅ Unlimited |
| Reading questions (self-scored, static) | ✅ **Unlimited** | ✅ Unlimited |
| Listening questions (static audio, self-scored) | ✅ **Unlimited** | ✅ Unlimited |
| Multiple-choice grammar quizzes (static) | ✅ Unlimited | ✅ Unlimited |
| Writing task + **AI feedback** | ❌ | ✅ **Max 1 / week** |
| Speaking session + **AI evaluation** | ❌ | ✅ **Max 1 / week** |
| Full mock exam (includes AI-evaluated writing/speaking parts) | ❌ | ✅ **Max 1 / week** |

> Rationale: static content costs nothing at runtime and drives installs/retention; the paywall sits exactly where marginal cost exists (AI evaluation calls). Free users can even WRITE an essay — but AI feedback requires premium (good upsell moment: "Dein Text ist fertig — hol dir Feedback mit Premium").

## Quota Mechanics
- Week = ISO week, resets **Monday 00:00 Europe/Berlin**.
- Counters at `users/{uid}/quota/{isoWeek}`: `{ exam: 0|1, writing: 0|1, speaking: 0|1 }`.
- Incremented **atomically in a Cloud Function** when the session *starts* (prevents restart abuse). Abandoned session within 5 min may be refunded once (Function decides).
- Client reads quota doc for messaging ("Nächste Prüfung: Montag").

## Entitlement Source
- Google Play Billing subscription → Play Developer Notifications → Cloud Function → `users/{uid}/entitlement: { active, plan, expiresAt }`.
- Firestore rules deny-by-default. AI-feedback endpoints (Cloud Functions) verify `entitlement.active` AND quota before calling the AI. Static content collections readable by any authenticated user.
- Never derive premium status from a client-cached flag.

## Writing Flow (Premium AI feedback, 1/week)
1. Server serves a level-appropriate exam topic (from `content/` prompt bank). Topic browsing itself is free.
2. User answers by **typing OR voice recording** (on-device Android SpeechRecognizer → transcript; free).
3. Cloud Function sends transcript + rubric to AI → structured feedback (grammar, vocabulary, structure, task fulfilment, CEFR-style score).
4. Stored in `writingSubmissions/` with `tokensUsed`.

## Speaking Flow (Premium AI evaluation, 1/week)
1. Exam-format timed parts (e.g. B2: Vortrag + Diskussion). Timer client-side, timestamps validated server-side.
2. **Not a free-flowing chat.** User answers each prompt within its time window.
3. After session end, all answer transcripts evaluated in ONE AI call → feedback + score.
4. Stored in `speakingSessions/`.

## Content Production (offline, one-time costs)
- Songs: generated in batch via Suno paid plan (commercial rights — verify plan terms before publishing), stored in Firebase Storage. One song per topic, no per-user cost.
- Reading passages, listening scripts/audio, MC questions: generated offline via `scripts/`, human-reviewed (`reviewed: true`), uploaded to Firestore/Storage.

## Cost Guardrails
- Max 2 runtime AI calls per premium user per week (1 writing + 1 speaking; mock exam consumes both slots or counts as `exam`, PO decision).
- `tokensUsed` logged on every AI call; weekly cost query in `scripts/`.
