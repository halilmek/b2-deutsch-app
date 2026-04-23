# B2 Deutsch App — Firebase Setup Guide

Follow these steps to set up Firebase for the app. Do these on your computer (not in this chat).

---

## Step 1: Firebase Console Setup

### 1.1 Open Firebase Console
Go to: https://console.firebase.google.com/
Open project: **b2-deutsch-app**

### 1.2 Enable Authentication
1. Go to **Authentication** → **Sign-in method**
2. Enable **Email/Password**
3. Enable **Google** (optional, for Google Sign-In)

### 1.3 Create Firestore Database
1. Go to **Firestore** → **Create database**
2. Choose **Start in test mode** (we'll secure it later)
3. Select a location near your users

### 1.4 Enable Storage
1. Go to **Storage** → **Get started**
2. Choose **Start in test mode**

### 1.5 Get SHA-256 Fingerprint (for Google Sign-In)
```bash
# In your terminal, run:
keytool -list -v -keystore ~/.android/debug.keystore -alias androiddebugkey -storepass android -keypass android
```
Copy the **SHA-256** value and add it in:
**Project Settings** → **Your apps** → **Android app** → **SHA certificate fingerprint**

---

## Step 2: Download google-services.json

1. Go to **Project Settings** → **Your apps**
2. Click **Add app** → **Android**
3. Package name: `com.b2deutsch.app`
4. Download `google-services.json`
5. Place it in: `b2-deutsch-app/app/google-services.json`

✅ **This file is already in the project — just replace if you downloaded a newer one**

---

## Step 3: Deploy Security Rules

### Firestore Rules
1. Go to **Firestore** → **Rules**
2. Copy the content from `b2-deutsch-app/firestore.rules`
3. Paste into the Firebase Rules editor
4. Click **Publish**

### Storage Rules
1. Go to **Storage** → **Rules**
2. Copy the content from `b2-deutsch-app/storage.rules`
3. Paste into the Firebase Rules editor
4. Click **Publish**

---

## Step 4: Set Up Cloud Functions (Optional — for AI Evaluation)

### 4.1 Install Firebase CLI
```bash
npm install -g firebase-tools
```

### 4.2 Login
```bash
firebase login
```

### 4.3 Initialize Functions
```bash
cd b2-deutsch-app
firebase init functions
# Select: Yes to all defaults
# Choose Node.js 18
```

### 4.4 Deploy Functions
```bash
cd functions
npm install
firebase deploy --only functions
```

### 4.5 Add Environment Variables
In Firebase Console → **Project Settings** → **Environment Variables**:
- `MINIMAX_API_KEY` = your MiniMax API key
- `MINIMAX_API_URL` = https://api.minimax.io/v1/text/chatcompletion

---

## Step 5: Seed Initial Data (Optional)

Create your first level in Firestore:

1. Go to **Firestore** → **Start collection**
2. Collection ID: `levels`
3. Add document:
   - `id`: "B2"
   - `name`: "B2"
   - `description`: "Upper-Intermediate"
   - `order`: 4
   - `isLocked`: false

Repeat for A1, A2, B1, C1 with order 1, 2, 3, 5.

---

## Step 6: Open in Android Studio / VS Code

### In VS Code:
```bash
cd b2-deutsch-app
code .
```

### Install Extensions:
- **Flutter** (if using Flutter, but we're using Kotlin)
- **Kotlin** language support
- **Android iOS** extension pack

### Build:
```bash
# Using Gradle wrapper
./gradlew assembleDebug
```

Or open in **Android Studio** and click **Run**.

---

## Step 7: Connect MiniMax API (Writing/Speaking AI)

Edit `functions/index.js` and replace:
```javascript
const MINIMAX_API_KEY = process.env.MINIMAX_API_KEY; // Set in Firebase Console
```

Ask your MiniMax provider for the API endpoint and key.

---

## Troubleshooting

### "google-services.json is missing"
→ Download from Firebase Console → Project Settings → Your apps → Android

### "Auth not working"
→ Enable Email/Password in Firebase Console → Authentication → Sign-in method

### "Firestore permission denied"
→ Check that Security Rules are published (Step 3)

### "Gradle build failed"
→ Make sure you have Java 17 installed
```bash
java -version  # Should show 17.x
```

---

## Next Steps After Setup

1. ✅ Test login/signup
2. ✅ Verify level selection works
3. ✅ Add sample lessons via Firestore
4. ✅ Test quiz flow
5. ✅ Deploy Cloud Functions for writing evaluation
6. ✅ Submit to Play Store
