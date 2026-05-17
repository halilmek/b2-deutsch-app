import json

with open('app/src/main/assets/a2_01.json') as f:
    data = json.load(f)

# Translation dict: exact match per question
translations = {
    "a2_01_q001": "The verb 'laufen' (to run/walk) takes 'lief' in Präteritum. This form is mainly used in written narratives such as novels, reports, and newspapers to describe past events.",
    "a2_01_q002": "The verb 'sein' (to be) takes 'war' in Präteritum (ich war, du warst, er war). This form is used in written language to describe past states.",
    "a2_01_q007": "The verbs 'können' (can/to be able to) and 'verbringen' (to spend time) in Präteritum. 'Können' becomes 'konnte' and 'verbringen' becomes 'verbrachte' in Präteritum.",
    "a2_01_q012": "The verb 'diskutieren' (to discuss) takes the regular Präteritum ending -te: 'diskutierte'. This form is commonly used in written narratives such as academic texts or reports.",
    "a2_01_q014": "The verb 'arbeiten' (to work) takes the regular Präteritum ending -te: 'arbeitete'. Here it describes a simultaneous past action or ongoing state.",
    "a2_01_q016": "The modal verb 'können' (can/to be able to) takes 'konnte' in Präteritum (ich konnte, du konntest, er konnte). Even in spoken German, modal verbs often use Präteritum instead of Perfekt.",
    "a2_01_q017": "The verb 'ausführen' (to carry out/to execute) is a separable prefix verb (trennbar). In Präteritum, the prefix is separated: 'führte aus'. The past participle is 'ausgeführt'.",
    "a2_01_q020": "The verb 'sein' (to be) in Präteritum 'war/waren' describes a long-lasting or ongoing past state or condition.",
    "a2_01_q021": "The construction 'kaum … da' in Präteritum means 'hardly … when'. This structure describes two events happening in quick succession in the past: 'Kaum war er angekommen, da rief sie an.'",
    "a2_01_q022": "The modal verb 'dürfen' (may/to be allowed to) takes 'durfte' in Präteritum. This is used for past permission or prohibition.",
    "a2_01_q023": "The verb 'spielen' (to play) takes the regular Präteritum ending -te: 'spielte'. In literary or narrative texts, Präteritum is preferred over Perfekt to describe past events.",
    "a2_01_q024": "The verb 'kennen' (to know/be acquainted with) takes 'kannte' in Präteritum. Here it appears in a Plusquamperfekt context, showing a past state that existed before another past event.",
    "a2_01_q025": "The verbs 'jubeln' (to cheer) and 'klatschen' (to clap) both take regular Präteritum endings (-te). Here they describe simultaneous past actions.",
    "a2_01_q027": "The verb 'wandern' (to hike) takes the regular Präteritum ending -te: 'wanderte'. Here it describes a repeated past action.",
    "a2_01_q028": "The modal verb 'müssen' (must/have to) in Präteritum connects with Konjunktiv II or Plusquamperfekt to express unfulfilled past obligations or regrets about what someone had to do.",
    "a2_01_q029": "The verb 'prägen' (to shape/to characterize) takes the regular Präteritum ending -te: 'prägte'. Here it is used in a historical narrative style.",
    "a2_01_q030": "The modal verb 'können' (can) in Präteritum combined with Konjunktiv II forms the 'would be able to' future construction.",
    "a2_01_q032": "The verb 'erklären' (to explain) is a regular (weak) verb. In Präteritum it takes the -te ending: 'erklärte'. Regular verbs add -te in Präteritum for all persons.",
    "a2_01_q035": "The verb 'spielen' (to play) in Präteritum: 'spielten'. This is the 1st/3rd person plural form of the regular weak verb conjugation.",
    "a2_01_q038": "The verb 'einstellen' (to hire/to adjust) is a separable prefix verb (trennbar). In Präteritum, the prefix 'ein-' is separated: 'stellte ein'. The past participle is 'eingestellt'.",
    "a2_01_q039": "The verb 'leben' (to live) takes the regular Präteritum ending -te: 'lebten'. This is the 1st/3rd person plural form.",
    "a2_01_q040": "The verb 'ankommen' (to arrive) is a separable prefix verb (trennbar). In Präteritum, the prefix 'an-' is separated: 'kam an'. The past participle is 'angekommen'.",
    "a2_01_q042": "The modal verb 'können' (can/to be able to) in Präteritum: 'konnte'. This is the ich/er form. Compare: ich konnte, du konntest, er konnte.",
    "a2_01_q043": "The verb 'entwickeln' (to develop) is a regular (weak) verb. In Präteritum it takes the -te ending: 'entwickelten'. This is the 1st/3rd person plural.",
    "a2_01_q045": "The modal verb 'können' (can/to be able to) in Präteritum: 'konnte'. This is used for past ability or possibility.",
    "a2_01_q047": "The reflexive verb 'sich beschweren' (to complain) takes the regular Präteritum ending -te: 'beschwerten'. Reflexive pronouns remain in the same position as in the present tense.",
}

# Apply translations
for q in data['questions']:
    qid = q['id']
    if qid in translations:
        q['explanation'] = translations[qid]

# Add description and tips
data['description'] = "Präteritum is the simple past tense in German, primarily used in written narratives such as novels, newspapers, and reports to describe past events. In spoken German, Perfekt is more common, but certain verbs—especially modal verbs (konnte, musste, durfte, wollte, sollte, hätte) and sein/haben—regularly appear in Präteritum even in conversation."

data['tips'] = """1. Written vs. Spoken: Präteritum is the standard past tense in writing (novels, newspapers, reports). In spoken German, Perfekt is preferred for most verbs, EXCEPT modal verbs and sein/haben, which commonly use Präteritum even in speech.

2. Weak (Regular) Verbs: Add -te to the verb stem for all persons: spielen → spiel-te, machen → macht-e, arbeiten → arbeit-ete. No vowel change in the stem.

3. Strong (Irregular) Verbs: These verbs change the vowel (Ablaut) in Präteritum: laufen → lief, finden → fand, schreiben → schrieb, lesen → las. The endings remain the same as weak verbs (-te is NOT added after the vowel change).

4. Modal Verbs (könen, müssen, dürfen, wollen, sollen, mögen): These always use Präteritum in both speech and writing over Perfekt: konnte, musste, durfte, wollte, sollte, mochte.

5. sein and haben: Both are essential in Präteritum for all contexts. Sein: war, warst, war, waren, wart, waren. Haben: hatte, hattest, hatte, hatten, hattet, hatten.

6. Separable Prefix Verbs (trennbar): In Präteritum, the prefix separates and goes to the end of the clause: ankommen → kam an, aufstehen → stand auf, einladen → lud ein.

7. Time Structure with Other Tenses: Präteritum combines with Plusquamperfekt (hatte gemacht / war gegangen) for events further in the past, and with Perfekt (hat gemacht) in spoken contexts for recent events.

8. Passive Voice in Präteritum: Formed with wurde + Partizip II: Das Haus wurde gebaut (The house was built). Plural: wurden + Partizip II.

9. Konjunktiv II Foundation: Präteritum forms are the basis for Konjunktiv II (indirect speech, hypotheticals): war → wäre, hatte → hätte, konnte → könnte, machte → machte (弱) or → würde machen (würde + Infinitiv)."""

print(f"Total questions: {len(data['questions'])}")

with open('app/src/main/assets/a2_01.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Done!")