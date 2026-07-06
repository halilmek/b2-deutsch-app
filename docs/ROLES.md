# ROLES.md — Roles & Responsibilities

In a solo/AI-agent project, one person (or one agent session) wears one of these hats at a time. When an agent starts a task, it must state which role it is acting in. Role definitions keep quality gates intact even without a real team.

## 1. Product Owner (PO)
**Mission:** Decide *what* gets built and in which order.
- Maintains PRODUCT_BACKLOG.md (priorities, acceptance criteria)
- Defines free vs premium boundaries (source of truth: MONETIZATION_SPEC.md)
- Rejects scope creep: no feature enters a sprint without a backlog item
- Validates: "Does this help a user pass the exam?" If no → deprioritize

## 2. Architect
**Mission:** Protect the level-agnostic design and data model.
- Owns ARCHITECTURE.md; any Firestore schema change requires updating it first
- Reviews: no hardcoded levels, no client-side AI keys, repositories take `level` param
- Decides where logic lives: app vs Cloud Functions (rule: anything involving money, quotas, or AI keys → Functions)

## 3. Android Developer
**Mission:** Implement features in Kotlin.
- Follows MVVM structure under `com.b2deutsch.app/` (data / di / ui / util)
- Writes ViewModels testable without Android framework where possible
- Never trusts client state for entitlements — always reads server verdict
- Keeps UI text in `strings.xml`

## 4. Backend/Functions Developer
**Mission:** Cloud Functions, Firestore rules, quota enforcement.
- Implements: AI evaluation endpoints (writing/speaking feedback), weekly quota counters, subscription webhook handling (Google Play Billing → Firestore `users/{id}/entitlements`)
- Firestore rules deny-by-default; premium collections readable only with valid entitlement
- Logs token usage per AI call (`tokensUsed`) for cost monitoring

## 5. QA / Test Engineer
**Mission:** Nothing ships untested.
- Unit tests for quiz scoring, quota logic, date/week-reset logic (timezone: Europe/Berlin)
- Entitlement test matrix (minimum):
  | Case | Expected |
  |---|---|
  | Free user opens grammar lesson | ✅ allowed |
  | Free user starts exam | ❌ paywall |
  | Premium user, 2nd exam same week | ❌ quota message |
  | Premium user, unlimited reading questions | ✅ allowed |
  | Week rollover (Mon 00:00 Berlin) | quota resets |
- Manual smoke test before any release: login → lesson → quiz → paywall → purchase (test track)

## 6. Content Engineer
**Mission:** Question banks, lessons, songs, audio.
- All content in `content/` as JSON, validated by `scripts/` before upload to Firestore
- AI-generated content is DRAFT until human (SME) review flag is set (`reviewed: true`)
- Song lyrics: AI-written, checked for grammar accuracy AND level-appropriateness; max 1 min audio
- Never delete published content; version it (`v2` suffix or `deprecated: true`)

## 7. Release Manager
**Mission:** Get builds to Google Play safely.
- Versioning: semver in `build.gradle` (`versionName`), bump `versionCode` every upload
- Order: internal testing track → closed beta → production
- Checks: ProGuard rules, google-services.json is the correct project, no debug flags
- Maintains release notes (DE + TR)

---
**Rule of thumb for agents:** if a task spans multiple roles, do them in the lifecycle order in AGENT_WORKFLOW.md §2, announcing each role switch.
