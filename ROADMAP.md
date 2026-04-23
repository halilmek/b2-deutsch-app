# B2 Deutsch App — Complete Roadmap

**Goal:** Publish a high-quality German B2 exam prep app on the Google Play Store.

---

## Phase 1 — Firebase Backend & Security
*Duration: 2–3 days*

### 1.1 Firebase Project Setup ✅ (Done)
- Project: `b2-deutsch-app`
- Package: `com.b2deutsch.app`

### 1.2 Enable Firebase Services
- **Authentication** → Enable Email/Password + Google Sign-In
- **Firestore** → Create database (start in test mode, secure later)
- **Analytics** → Enable Firebase Analytics
- **Crashlytics** → Enable for bug tracking
- **App Distribution** → Optional, for testing

### 1.3 Firestore Data Model

```
users/
  {userId}/
    email: string
    displayName: string
    createdAt: timestamp
    progress/
      completedLessons: string[]
      quizScores: map
      streak: number
      lastActive: timestamp

lessons/
  {lessonId}/
    title: string
    description: string
    category: string (grammar|vocabulary|reading|listening)
    level: string ("B2")
    order: number
    content/
      sections: array of content blocks
    duration: number (minutes)
    isPremium: boolean

quizzes/
  {quizId}/
    lessonId: string (reference)
    title: string
    questions/
      {questionId}/
        type: string (multiple_choice|true_false|fill_blank)
        questionText: string
        options: string[] (for multiple_choice)
        correctAnswer: string
        explanation: string
    passingScore: number

vocabulary/
  {wordId}/
    german: string
    english: string
    turkish: string
    partOfSpeech: string
    exampleSentence: string
    category: string
    difficulty: string ("B2")
```

### 1.4 Security Rules

**Firestore Rules:**
```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // Users can read/write only their own profile
    match /users/{userId} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }
    // Anyone can read lessons and quizzes (published content)
    match /lessons/{lessonId} {
      allow read: if true;
      allow write: if request.auth != null && get(/databases/$(database)/documents/users/$(request.auth.uid)).data.isAdmin == true;
    }
    match /quizzes/{quizId} {
      allow read: if true;
      allow write: if request.auth != null && get(/databases/$(database)/documents/users/$(request.auth.uid)).data.isAdmin == true;
    }
    // Vocabulary accessible to authenticated users
    match /vocabulary/{wordId} {
      allow read: if request.auth != null;
      allow write: if request.auth != null && get(/databases/$(database)/documents/users/$(request.auth.uid)).data.isAdmin == true;
    }
  }
}
```

### 1.5 Firebase App Check
- Enable App Check for Firestore (reCAPTCHA v3)
- Prevents unauthorized API access

---

## Phase 2 — App Architecture & Core Infrastructure
*Duration: 3–4 days*

### 2.1 Project Structure
```
com.b2deutsch.app/
├── data/
│   ├── model/          # Data classes (User, Lesson, Quiz, etc.)
│   ├── repository/     # Repository pattern for data access
│   ├── remote/         # Firebase calls
│   └── local/          # SharedPreferences, Room (if needed)
├── di/                 # Dependency injection (Hilt)
├── ui/
│   ├── auth/           # Login, Register, Forgot Password
│   ├── home/           # Home screen
│   ├── lessons/        # Lesson list & detail
│   ├── quiz/           # Quiz flow & results
│   ├── vocabulary/      # Flashcards, word lists
│   ├── progress/       # User progress & stats
│   └── settings/       # App settings
├── util/               # Extensions, constants, helpers
└── B2DeutschApp.kt     # Application class
```

### 2.2 Navigation
- Bottom Navigation with 4 tabs: Home, Lessons, Vocabulary, Profile
- Navigation Component for fragment transitions
- Deep linking for shared content

### 2.3 Dependency Injection (Hilt)
- All Firebase references
- All repositories
- ViewModels

### 2.4 State Management
- ViewModel + StateFlow/LiveData
- Sealed classes for UI states (Loading, Success, Error)

---

## Phase 3 — Authentication
*Duration: 2 days*

### 3.1 Screens
- Splash screen (check auth state)
- Login screen (email/password)
- Register screen (email, password, display name)
- Forgot password screen
- Email verification screen

### 3.2 Firebase Auth Flow
- Email/password sign-up with verification
- Google Sign-In (OAuth)
- Persistent auth state (auto-login)
- Sign-out

### 3.3 Profile Screen
- Display name & email
- Edit profile
- Change password
- Delete account

---

## Phase 4 — Lessons Module
*Duration: 3–4 days*

### 4.1 Lesson Categories (B2 Exam Areas)
- **Grammatik** (Grammar)
- **Wortschatz** (Vocabulary)
- **Leseverstehen** (Reading Comprehension)
- **Hörverstehen** (Listening Comprehension) — future
- **Schreiben** (Writing) — future
- **Mündliche Kommunikation** (Speaking) — future

### 4.2 Lesson Card UI
- Thumbnail, title, description
- Duration estimate
- Completion badge
- Premium lock icon (optional)

### 4.3 Lesson Detail Screen
- Lesson content sections (text, images, examples)
- Mark as complete button
- Related quizzes shortcut

### 4.4 Lesson Content Types
- Text sections with formatting
- Example sentences (German + English + Turkish)
- Grammar tables
- Highlighted key phrases

---

## Phase 5 — Quiz Module
*Duration: 3–4 days*

### 5.1 Quiz Types
- Multiple choice (single answer)
- Multiple choice (multiple answers)
- True/False
- Fill in the blank

### 5.2 Quiz Flow
1. Quiz intro (title, question count, time estimate)
2. Question screen (one question at a time)
3. Progress indicator
4. Submit → Results screen
5. Results: score, pass/fail, correct answers review
6. Explanation for each answer

### 5.3 Quiz Results
- Score percentage
- Pass/fail threshold (e.g., 70%)
- Correct/incorrect breakdown
- Option to retry or go to next lesson

---

## Phase 6 — Vocabulary Module
*Duration: 2–3 days*

### 6.1 Flashcard System
- Swipe cards (front: German word, back: translation + example)
- Audio pronunciation (Text-to-Speech or recorded)
- Mark as "learned" or "needs practice"

### 6.2 Word Lists
- Categorized by topic (e.g., "Arbeit", "Gesundheit", "Umwelt")
- Search functionality
- Filter by learned/unlearned

### 6.3 Spaced Repetition
- Simple SRS: words marked "hard" appear more often
- Track review sessions

---

## Phase 7 — Progress & Gamification
*Duration: 2 days*

### 7.1 Progress Tracking
- Lessons completed / total
- Quiz scores per category
- Vocabulary learned count
- Daily streak

### 7.2 Gamification
- Daily streak counter
- Achievement badges:
  - "First Lesson" — Complete your first lesson
  - "Perfect Score" — Get 100% on any quiz
  - "Week Warrior" — 7-day streak
  - "Vocabulary Master" — Learn 100 words
- Weekly progress summary

### 7.3 Statistics Screen
- Pie chart of category progress
- Line graph of quiz scores over time
- Streak calendar

---

## Phase 8 — UI/UX Polish
*Duration: 2–3 days*

### 8.1 Design System
- Color palette: German-inspired (Schwarz, Rot, Gold accents)
- Typography: Readable, clean
- Consistent spacing & corner radii
- Dark mode support

### 8.2 Animations
- Card flip animation (flashcards)
- Progress bar animations
- Success/confetti on achievements
- Smooth navigation transitions

### 8.3 Accessibility
- Content descriptions for images
- Minimum touch target sizes (48dp)
- Color contrast compliance

---

## Phase 9 — Firebase Setup (Content)
*Duration: ongoing*

### 9.1 Seed Content (Minimum Viable)
- 5–10 grammar lessons with content
- 2–3 quizzes per lesson
- 100 vocabulary words across categories

### 9.2 Content Categories (B2 Topics)
- Beruf (Career/Work)
- Gesundheit (Health)
- Umwelt (Environment)
- Gesellschaft (Society)
- Reisen (Travel)
- Medien (Media)
- Bildung (Education)

---

## Phase 10 — Play Store Listing
*Duration: 2–3 days*

### 10.1 App Signing
- Create Keystore for release signing
- Register Play Store Developer Account ($25 one-time)
- Create app in Play Console
- Link Firebase to Play Console (optional: crash reports)

### 10.2 Store Listing Assets

**App Name:**
B2 Deutsch — Prüfungsvorbereitung

**Short Description (80 chars):**
German B2 exam prep with lessons, quizzes & vocabulary.

**Full Description (4000 chars):**
- Lead with the problem: "Preparing for the German B2 exam?"
- Features list (bullet points)
- Social proof: "Join thousands of learners..."
- Call to action

**Screenshots (min 2):**
- Phone: 1080×1920 PNG/JPG
- Tablet: 1200×1800 PNG/JPG
- Show main screens: Home, Lesson, Quiz, Results

**Graphic Assets:**
- App icon (512×512 PNG)
- Feature graphic (1024×500 PNG)
- Privacy policy URL (required)

### 10.3 Content Rating
- Complete questionnaire: "Education" category
- B2 German exam content is appropriate for all ages
- No mature content

### 10.4 Pricing & Distribution
- Free with ads (optional) OR free with premium features
- Select countries for distribution
- Privacy policy URL required

---

## Phase 11 — Pre-Launch Checklist
*Duration: 1 day*

- [ ] All Firebase security rules updated
- [ ] App tested on multiple device sizes (small phone, tablet)
- [ ] Dark mode tested
- [ ] No hardcoded test values in release build
- [ ] ProGuard/R8 minification enabled
- [ ] Crashlytics reporting verified
- [ ] Privacy policy published (can be a simple Google Docs link)
- [ ] App icon and graphics meet Play Store specs
- [ ] Screenshots taken with real content (not placeholder data)
- [ ] Test APK / AAB installed on physical device and tested

---

## Phase 12 — Launch & Post-Launch
*Duration: 1 day launch + ongoing*

### 12.1 Launch
- Upload AAB (Android App Bundle) to Play Console
- Submit for review (typically 1–3 days)
- Monitor review status

### 12.2 Post-Launch
- Monitor Crashlytics & Analytics dashboard
- Collect user reviews — respond to them
- Fix bugs reported by users
- Add more content regularly
- Plan feature updates (speaking exercises, more quizzes)

### 12.3 Future Enhancements (Post-Launch)
- Push notifications (Firebase Cloud Messaging)
- Listening exercises (audio files in Firebase Storage)
- Speaking practice (record & compare)
- User-generated content (community flashcards)
- Leaderboards
- Subscription/premium model

---

## Estimated Timeline

| Phase | Task | Duration |
|-------|------|----------|
| 1 | Firebase Backend & Security | 2–3 days |
| 2 | App Architecture | 3–4 days |
| 3 | Authentication | 2 days |
| 4 | Lessons Module | 3–4 days |
| 5 | Quiz Module | 3–4 days |
| 6 | Vocabulary Module | 2–3 days |
| 7 | Progress & Gamification | 2 days |
| 8 | UI/UX Polish | 2–3 days |
| 9 | Content Seeding | Ongoing |
| 10 | Play Store Listing | 2–3 days |
| 11 | Pre-Launch Checklist | 1 day |
| 12 | Launch | 1 day + ongoing |

**Total MVP: ~15–20 working days**

---

## Budget Estimate

| Item | Cost |
|------|------|
| Google Play Developer Account | $25 (one-time) |
| Domain for privacy policy | $0–$12/year |
| Firebase Spark Plan (free) | $0 |
| Optional: Firebase Blaze (pay-as-you-go) | ~$0–$5/month |
| Optional: Premium content hosting | $0–$20/month |

**Total minimum cost to launch: $25**

---

## Pricing Tiers (Finalized)

*Last updated: 2026-04-23 19:03 UTC*

| | **Free** | **Standard** | **Premium** |
|--|---------|-------------|-------------|
| **Price** | €0 | €5.99/month | €9.99/month |
| AI speaking practice | 10 min/day | 20 min/day | Unlimited |
| Peer speaking exams | 1/week (4/month) | 1/week (4/month) | 2/week (8/month) |
| Writing evaluations | 1/week (4/month) | 5/month | 15/month |
| All CEFR levels | ❌ (B2 only) | ❌ (B2 only) | ✅ (A1–C1) |
| Mock exams (full) | ❌ | 1/month | 2/month |
| Progress tracking | Basic | Full | Full + detailed |

### Cost to Serve (Per User Per Month)

| Tier | AI Practice Cost | Storage | Total |
|------|-----------------|---------|-------|
| Free | ~$0.16 | ~$0.01 | ~$0.17 |
| Standard | ~$0.40 | ~$0.02 | ~$0.42 |
| Premium | ~$0.60 | ~$0.05 | ~$0.65 |

### Gross Margin (Per User Per Month)

| Tier | Price | Your Cost | Margin |
|------|-------|-----------|--------|
| Free | €0 | $0.17 | — (free tier, growth investment) |
| Standard | €5.99 | ~$0.42 | **€5.57** (~93% margin) |
| Premium | €9.99 | ~$0.65 | **€9.34** (~93% margin) |

### Pay-Per-Use (Optional Add-On)

| Item | Price | Cost | Margin |
|------|-------|------|--------|
| Single peer exam | €0.99 | ~$0.01 | ~€0.98 |
| Exam pack (5) | €3.99 | ~$0.05 | ~€3.94 |
| Exam pack (10) | €6.99 | ~$0.10 | ~€6.89 |
| Writing eval (one-off) | €0.50 | ~$0.003 | ~€0.50 |

### Peer Speaking Exam — How It Works

1. User A (examiner) and User B (candidate) join a peer exam room
2. AI shares topic and questions with User A only (examiner sees them)
3. Both users record audio messages back and forth (15 min max)
4. Conversation ends when time expires or both confirm done
5. AI transcribes all recordings → evaluates both users → delivers feedback
6. **AI only runs once per session** — cost: ~$0.01/session

### Usage Limits — Why Conservative?

- Initial user base is unknown — keep server costs minimal
- Standard: 4 peer exams/month = 1 per week (enough for serious prep)
- Premium: 8 peer exams/month = 2 per week (for intensive learners)
- Both tiers have same peer exam limit — premium difference is unlimited AI practice + all levels
