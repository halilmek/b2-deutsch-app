# B2 Deutsch App — Multi-Level Architecture

## Core Design Principle
**Level-Agnostic Core** — All screens, logic, and data models are designed to work with ANY CEFR level (A1, A2, B1, B2, C1). Adding a new level = adding content only, no new code.

---

## Data Model — Level-Agnostic

### Firestore Structure

```
users/
  {userId}/
    email: string
    displayName: string
    createdAt: timestamp
    progress/
      {level}/{contentId}: { status, score, completedAt }
      currentLevel: string ("B2" initially)
      streak: number
      lastActive: timestamp

levels/
  {levelId}/           # "A1", "A2", "B1", "B2", "C1"
    name: string        # "Level A1", "Elementary", etc.
    description: string
    order: number       # Display order (1=A1, 2=A2, 3=B1, 4=B2, 5=C1)
    isLocked: boolean   # Future: unlock after completing previous level
    iconUrl: string

lessons/
  {lessonId}/
    level: string      # "A1" | "A2" | "B1" | "B2" | "C1"
    category: string    # "grammar" | "vocabulary" | "reading" | "listening" | "writing" | "speaking"
    title: string
    description: string
    order: number
    duration: number    # Estimated minutes
    isPremium: boolean
    content: array of Section objects

quizzes/
  {quizId}/
    level: string
    lessonId: string   # Link to related lesson
    title: string
    taskType: string   # "reading" | "listening" | "writing" | "speaking"
    timeLimit: number  # Minutes
    passingScore: number
    questions: array of Question objects

vocabulary/
  {wordId}/
    level: string
    german: string
    english: string
    turkish: string
    partOfSpeech: string
    exampleSentence: string
    category: string   # Topic (e.g., "Arbeit", "Gesundheit")
    audioUrl: string   # Optional: TTS audio for pronunciation

writingSubmissions/
  {subId}/
    userId: string
    level: string
    taskType: string   # "formal_email" | "essay" | "letter" etc.
    prompt: string
    userText: string
    evaluation: object # AI feedback
    score: number
    evaluatedAt: timestamp
    tokensUsed: number

speakingSessions/
  {sessionId}/
    userId: string
    level: string
    partnerType: string  # "ai" | "peer"
    peerUserId: string    # If partnerType == "peer"
    topic: string
    duration: number
    recordingUrl: string
    transcript: string
    evaluation: object   # AI feedback
    score: number
    completedAt: timestamp

# Reading passages — pre-generated AI content
readingPassages/
  {passageId}/
    level: string
    category: string    # "education" | "technology" | "health" | "society" | etc.
    title: string
    content: string     # German text (300-500 words for B2)
    source: string      # "AI_GENERATED"
    questions: array    # Embedded reading comprehension questions
    createdAt: timestamp

# Listening content
listeningExercises/
  {exerciseId}/
    level: string
    category: string
    title: string
    audioUrl: string    # Firebase Storage URL
    transcript: string # Full transcript for AI evaluation
    duration: number
    questions: array    # Listening comprehension questions
    difficulty: string # "easy" | "medium" | "hard"
```

---

## App Navigation Structure

```
SplashScreen
    │
    ▼
AuthGate (if not logged in)
    │
    ▼
LevelSelectionScreen      ← NEW: Top-level selection
    │
    ├──► A1 (locked/unlocked based on progress)
    ├──► A2
    ├──► B1
    ├──► B2 ◄── Default
    └──► C1

After Level Selected:
    │
    ▼
HomeScreen (filtered by level)
    │
    ├──► LessonsTab
    │       └──► LessonDetailScreen → LessonContentScreen
    │
    ├──► QuizzesTab
    │       └──► QuizIntroScreen
    │              └──► QuizQuestionScreen (one q at a time)
    │                     └──► QuizResultsScreen
    │
    ├──► VocabularyTab
    │       └──► FlashcardScreen
    │              └──► WordDetailScreen
    │
    └──► ProfileTab
            ├──► ProgressScreen (level-specific stats)
            ├──► SettingsScreen
            └──► SubscriptionScreen
```

---

## Level Module — Code Structure

Each feature works with any level — the `level` field is a parameter:

```
com.b2deutsch.app/
├── data/
│   ├── model/
│   │   ├── Level.kt          # CEFR level enum
│   │   ├── Lesson.kt
│   │   ├── Quiz.kt
│   │   ├── Question.kt
│   │   ├── Vocabulary.kt
│   │   ├── UserProgress.kt
│   │   └── WritingSubmission.kt
│   ├── repository/
│   │   ├── LevelRepository.kt   # Fetch available levels
│   │   ├── LessonRepository.kt # Filter by level
│   │   ├── QuizRepository.kt
│   │   ├── VocabularyRepository.kt
│   │   └── UserRepository.kt
│   └── remote/
│       └── FirebaseDataSource.kt
├── di/
│   └── AppModule.kt
├── ui/
│   ├── auth/
│   ├── level/                    ← NEW: Level selection
│   │   ├── LevelSelectionFragment.kt
│   │   └── LevelAdapter.kt
│   ├── home/
│   ├── lessons/
│   ├── quiz/
│   ├── vocabulary/
│   ├── writing/                  ← NEW: Writing practice
│   │   ├── WritingPromptScreen.kt
│   │   ├── WritingEditorScreen.kt
│   │   └── WritingResultScreen.kt
│   ├── speaking/                 ← NEW: Speaking practice
│   │   ├── SpeakingPartnerScreen.kt
│   │   ├── PeerExamScreen.kt
│   │   └── SpeakingResultScreen.kt
│   └── profile/
└── util/
    └── Constants.kt               # CEFR_LEVELS = ["A1","A2","B1","B2","C1"]
```

---

## Key Architectural Decisions

### 1. Level as a Filter, Not a Separate App
- All repositories accept `level: String` as a parameter
- No hardcoded level logic in UI — all content filtered from Firestore
- Adding A1 just means adding content documents with `level: "A1"`

### 2. Content is Future-Proof
- Pre-generated reading passages and listening exercises stored in Firestore
- Audio files in Firebase Storage (not Firestore)
- Question types are standardized across all levels

### 3. Speaking Partner — Level-Aware
- System prompt includes current level for appropriate difficulty
- Peer exams lock both users to the same level
- AI responses adapt vocabulary complexity to the selected level

### 4. Progress Tracking Per Level
```kotlin
data class UserProgress(
    val currentLevel: String = "B2",
    val levelProgress: Map<String, LevelProgress> = emptyMap()
)

data class LevelProgress(
    val lessonsCompleted: Int = 0,
    val quizzesTaken: Int = 0,
    val averageScore: Double = 0.0,
    val vocabularyLearned: Int = 0,
    val streak: Int = 0
)
```

### 5. Subscription Per Level Access
- Free tier: B2 only (or all levels with limitations)
- Premium: Full access to all levels
- No level-specific subscriptions — one app, all levels

---

## Multi-Level Content Strategy

### Sources (as mentioned: 3rd party apps)
- Goethe-Institut past papers (publicly available samples)
- ÖSD exam materials (some free samples)
- DW (Deutsche Welle) — free A1-C1 resources
- AI-generated passages using MiniMax (for quantity)

### Content Generation Pipeline
1. Define B2 exam format (from official exam specs)
2. Use MiniMax to generate passages/questions matching format
3. Human review (optional for MVP)
4. Upload to Firestore
5. Same pipeline for A1, A2, B1, C1 — just different prompts

### Question Types Per Level

| Skill | A1/A2 | B1 | B2 | C1 |
|-------|-------|----|----|-----|
| Reading | Multiple choice, True/False | Multiple choice, Gap fill | All B2 types + matching | Complex texts, nuanced questions |
| Listening | Short dialogues | Longer conversations | Lecture-style | Academic presentations |
| Writing | Fill forms, short notes | Informal letter, blog post | Formal email, essay | Report, proposal |
| Speaking | Introduce self, basic questions | Describe experience | Discuss topic, argue point | Academic discussion, debate |

---

## Implementation Priority

1. **Level selection screen** (new) — wrap existing B2 app in level context
2. **Refactor all repositories** to accept level parameter
3. **Add level field** to all content types
4. **Future:** Content import script for A1, A2, B1, C1

---

_Last updated: 2026-04-23_
