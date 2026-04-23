# B2 Deutsch App

Android app project set up with Firebase (Auth, Firestore, Analytics).

## Project Structure

```
b2-deutsch-app/
├── app/
│   ├── google-services.json   ← Firebase config (already added)
│   ├── build.gradle           ← App-level build with Firebase deps
│   ├── proguard-rules.pro
│   └── src/main/
│       ├── AndroidManifest.xml
│       ├── java/com/b2deutsch/app/
│       │   ├── B2DeutschApp.kt       ← Application class
│       │   └── ui/
│       │       └── MainActivity.kt   ← Main screen
│       └── res/
│           ├── layout/activity_main.xml
│           └── values/{strings,colors,themes}.xml
├── build.gradle              ← Root build with AGP + Google Services plugin
├── settings.gradle
├── gradle.properties         ← AndroidX enabled
└── gradle/wrapper/
    └── gradle-wrapper.properties
```

## To Build

1. Open in Android Studio (or VS Code with Android extensions)
2. Sync Gradle
3. Run on emulator or device

## Next Steps

- [ ] Design main UI screens (lessons, quizzes, progress)
- [ ] Set up Firebase Auth (login/signup)
- [ ] Set up Firestore data model for B2 German content
- [ ] Add navigation
- [ ] Add actual lesson/quiz content
