#!/usr/bin/env python3
"""B2 Reading: Generate Topics 5-12 (80 texts, 400 questions)"""
import json
from datetime import datetime

TOPICS_DATA = {
    "b2_reading_05": {
        "name": "Medien und Kommunikation", "nameEn": "Media and Communication",
        "iconEmoji": "📱",
        "texts": [
            {"id": "b2_r_05_01", "title": "Soziale Medien: Fluch oder Segen?",
             "source": "Medienanstalt", "sourceUrl": "https://www.medienanstalt.de/",
             "wordCount": 320, "readingTimeMinutes": 5, "tags": ["Social Media", "Digitalisierung", "Jugend"],
             "content": "Soziale Medien wie Instagram, TikTok und Twitter sind aus dem Alltag junger Menschen nicht mehr wegzudenken. Rund 87 Prozent der 14- bis 29-Jährigen in Deutschland nutzen regelmäßig soziale Netzwerke. Doch die Debatte über die Auswirkungen ist kontrovers.\n\nBefürworter betonen die Vorteile: Soziale Medien ermöglichen Vernetzung über Ländergrenzen hinweg, bieten Zugang zu Informationen und Bildung und schaffen Räume für kreative Selbstentfaltung. Besonders für junge Menschen aus ländlichen Regionen können soziale Medien ein Fenster zur Welt sein.\n\nKritiker warnen jedoch vor den Schattenseiten. Soziale Medien können zu Suchtverhalten führen, das Selbstwertgefühl beeinträchtigen - besonders bei Mädchen, die sich mit idealisierten Körperbildern vergleichen - und die Demokratie durch die Verbreitung von Desinformation gefährden. Hatespeech und Cybermobbing sind weitere ernste Probleme.\n\nDie Politik diskutiert strengere Regulierung. Der Digital Services Act der EU soll Plattformen zu mehr Transparenz und Verantwortung verpflichten. Nutzer sollen leichter erkennen können, ob Inhalte von Algorithmen manipuliert werden.\n\nFür Eltern und Pädagogen stellt sich die Frage, wie man junge Menschen im Umgang mit sozialen Medien stärken kann. Medienkompetenz - also die Fähigkeit, Inhalte kritisch zu bewerten und mit persönlichen Daten sorgfältig umzugehen - gilt als Schlüssel.",
             "questions": [
                 {"id": "q_05_01_a", "type": "multiple_choice", "questionText": "Wie viel Prozent der 14- bis 29-Jährigen nutzen regelmäßig soziale Netzwerke?",
                  "options": ["Etwa 50 Prozent", "Etwa 87 Prozent", "Etwa 30 Prozent", "Rund 70 Prozent"],
                  "correctAnswer": "Etwa 87 Prozent", "explanation": "'Rund 87 Prozent der 14- bis 29-Jährigen in Deutschland nutzen regelmäßig soziale Netzwerke.'"},
                 {"id": "q_05_01_b", "type": "true_false", "questionText": "Soziale Medien haben laut dem Text nur Vorteile.", "correctAnswer": "false",
                  "explanation": "Der Text beschreibt sowohl Vorteile (Vernetzung, Bildung) als auch Nachteile (Sucht, Selbstwertgefühl, Hatespeech, Desinformation)."},
                 {"id": "q_05_01_c", "type": "multiple_choice", "questionText": "Was gilt als Schlüssel im Umgang mit sozialen Medien?",
                  "options": ["Komplettverbot für Jugendliche", "Medienkompetenz", "Mehr Werbung", "Weniger Nutzung"],
                  "correctAnswer": "Medienkompetenz", "explanation": "'Medienkompetenz - also die Fähigkeit, Inhalte kritisch zu bewerten und mit persönlichen Daten sorgfältig umzugehen - gilt als Schlüssel.'"},
                 {"id": "q_05_01_d", "type": "fill_blank", "questionText": "Der Digital Services Act der EU soll Plattformen zu mehr ___ und Verantwortung verpflichten.",
                  "correctAnswer": "Transparenz", "explanation": "'Der Digital Services Act der EU soll Plattformen zu mehr Transparenz und Verantwortung verpflichten.'"},
                 {"id": "q_05_01_e", "type": "multiple_choice", "questionText": "Welche Probleme werden im Zusammenhang mit sozialen Medien genannt?",
                  "options": ["Nur technische Probleme", "Suchtverhalten, Selbstwertgefühl-Beeinträchtigung, Hatespeech und Cybermobbing",
                              "Nur positive Effekte", "Nur wirtschaftliche Probleme"],
                  "correctAnswer": "Suchtverhalten, Selbstwertgefühl-Beeinträchtigung, Hatespeech und Cybermobbing",
                  "explanation": "'Soziale Medien können zu Suchtverhalten führen, das Selbstwertgefühl beeinträchtigen... Hatespeech und Cybermobbing sind weitere ernste Probleme.'"}
             ],
             "keyVocabulary": [
                 {"german": "die sozialen Medien", "english": "social media", "turkish": "sosyal medya", "pos": "noun"},
                 {"german": "die Medienkompetenz", "english": "media literacy", "turkish": "medya okuryazarlığı", "pos": "noun"},
                 {"german": "der Cybermobbing", "english": "cyberbullying", "turkish": "siber zorbalık", "pos": "noun"},
                 {"german": "die Desinformation", "english": "disinformation", "turkish": "dezenformasyon", "pos": "noun"},
                 {"german": "der Hatespeech", "english": "hate speech", "turkish": "nefret söylemi", "pos": "noun"},
                 {"german": "die Regulierung", "english": "regulation", "turkish": "düzenleme", "pos": "noun"},
                 {"german": "der Algorithmus", "english": "algorithm", "turkish": "algoritma", "pos": "noun"},
                 {"german": "das Selbstwertgefühl", "english": "self-esteem", "turkish": "öz-saygı", "pos": "noun"}
             ],
             "examTip": "87% der Jugendlichen nutzen soziale Medien! Vorteile und Nachteile双双. Medienkompetenz = Schlüssel. DSA = neue EU-Regel!"
            },
            {"id": "b2_r_05_02", "title": "Datenschutz: Wer kontrolliert unsere Daten?",
             "source": "Bundesbeauftragte für Datenschutz", "sourceUrl": "https://www.bfdi.bund.de/",
             "wordCount": 310, "readingTimeMinutes": 5, "tags": ["Datenschutz", "Privatsphäre", "Digitalisierung"],
             "content": "Jeden Tag hinterlassen wir digitale Spuren: Beim Surfen im Internet, beim Einkaufen im Online-Shop oder bei der Nutzung von Apps. Unternehmen sammeln diese Daten, um Werbung zu personalisieren und Nutzerprofile zu erstellen. Datenschützer schlagen Alarm.\n\nDie Datenschutz-Grundverordnung (DSGVO), die seit 2018 in der EU gilt, soll die Rechte von Bürgern stärken. Jeder hat das Recht zu wissen, welche Daten über ihn gesammelt werden, und das Recht, diese löschen zu lassen. Bei Verstößen drohen hohe Bußgelder - bis zu 20 Millionen Euro oder vier Prozent des weltweiten Jahresumsatzes.\n\nDoch die Umsetzung ist schwierig. Viele Nutzer klicken auf „Ich stimme zu\", ohne die Datenschutzerklärungen zu lesen. Fachleute sprechen von „Consent Fatigue" - einer Zustimmungsmüdigkeit, die dadurch entsteht, dass ständig Cookie-Banner und AGB-Pop-ups erscheinen.\n\nBesonders brisant ist die Datensammlung durch große Tech-Konzerne wie Google, Meta und Amazon. Diese Unternehmen wissen oft mehr über Nutzer, als diese selbst über sich wissen. Mit künstlicher Intelligenz können aus scheinbar harmlosen Daten detaillierte Persönlichkeitsprofile erstellt werden.\n\nFür die Zukunft fordern Datenschützer mehr Transparenz und einfachere Möglichkeiten, der Datensammlung zu widersprechen. „Daten sind das Öl des 21. Jahrhunderts", sagt Datenschutzaktivist Max Schrems. „Und wie beim Öl gilt: Wer es verschmutzt, muss dafür zahlen.\"",
             "questions": [
                 {"id": "q_05_02_a", "type": "multiple_choice", "questionText": "Was ist die Datenschutz-Grundverordnung (DSGVO)?",
                  "options": ["Ein deutsches Gesetz", "Eine EU-Verordnung zum Schutz von Bürgerrechten im Internet", "Ein Online-Shop", "Ein Technologieunternehmen"],
                  "correctAnswer": "Eine EU-Verordnung zum Schutz von Bürgerrechten im Internet", "explanation": "'Die Datenschutz-Grundverordnung (DSGVO), die seit 2018 in der EU gilt, soll die Rechte von Bürgern stärken.'"},
                 {"id": "q_05_02_b", "type": "true_false", "questionText": "Bei DSGVO-Verstößen drohen keine ernsthaften Konsequenzen.", "correctAnswer": "false",
                  "explanation": "'Bei Verstößen drohen hohe Bußgelder - bis zu 20 Millionen Euro oder vier Prozent des weltweiten Jahresumsatzes.'"},
                 {"id": "q_05_02_c", "type": "multiple_choice", "questionText": "Was ist Consent Fatigue?",
                  "options": ["Ein medizinisches Problem", "Zustimmungsmüdigkeit durch ständige Cookie-Banner", "Eine neue App", "Ein Computerprogramm"],
                  "correctAnswer": "Zustimmungsmüdigkeit durch ständige Cookie-Banner", "explanation": "'Fachleute sprechen von Consent Fatigue - einer Zustimmungsmüdigkeit, die dadurch entsteht, dass ständig Cookie-Banner und AGB-Pop-ups erscheinen.'"},
                 {"id": "q_05_02_d", "type": "fill_blank", "questionText": "___ sind das Öl des 21. Jahrhunderts, sagt Datenschutzaktivist Max Schrems.",
                  "correctAnswer": "Daten", "explanation": "'Daten sind das Öl des 21. Jahrhunderts', sagt Datenschutzaktivist Max Schrems."},
                 {"id": "q_05_02_e", "type": "multiple_choice", "questionText": "Welche Daten sammeln große Tech-Konzerne laut dem Text?",
                  "options": ["Nur E-Mail-Adressen", "Aus scheinbar harmlosen Daten können sie detaillierte Persönlichkeitsprofile erstellen", "Nur Zahlungsinformationen", "Gar keine Daten"],
                  "correctAnswer": "Aus scheinbar harmlosen Daten können sie detaillierte Persönlichkeitsprofile erstellen",
                  "explanation": "'Mit künstlicher Intelligenz können aus scheinbar harmlosen Daten detaillierte Persönlichkeitsprofile erstellt werden.'"}
             ],
             "keyVocabulary": [
                 {"german": "der Datenschutz", "english": "data protection", "turkish": "veri koruma", "pos": "noun"},
                 {"german": "die DSGVO", "english": "GDPR", "turkish": "KVKK (Kişisel Verileri Koruma Kanunu)", "pos": "noun"},
                 {"german": "das Bußgeld", "english": "fine / penalty", "turkish": "para cezası", "pos": "noun"},
                 {"german": "die Privatsphäre", "english": "privacy", "turkish": "gizlilik", "pos": "noun"},
                 {"german": "das Nutzerprofil", "english": "user profile", "turkish": "kullanıcı profili", "pos": "noun"},
                 {"german": "der Cookie-Banner", "english": "cookie banner", "turkish": "çerez bildirimi", "pos": "noun"},
                 {"german": "das Persönlichkeitsprofil", "english": "personality profile", "turkish": "kişilik profili", "pos": "noun"},
                 {"german": "die Transparenz", "english": "transparency", "turkish": "şeffaflık", "pos": "noun"}
             ],
             "examTip": "DSGVO = Datenschutz-Grundverordnung (GDPR). Bußgeld: bis 20 Mio € oder 4% Umsatz! Consent Fatigue = Zustimmungsmüdigkeit!"
            },
            {"id": "b2_r_05_03", "title": "Künstliche Intelligenz: Wie Chatbots unser Leben verändern",
             "source": "Spiegel Online", "sourceUrl": "https://www.spiegel.de/thema/kuenstliche-intelligenz",
             "wordCount": 315, "readingTimeMinutes": 5, "tags": ["KI", "Chatbots", "Technologie"],
             "content": "Künstliche Intelligenz (KI) ist längst keine Science-Fiction mehr. Sprachassistenten wie Siri, Alexa oder ChatGPT sind Teil unseres Alltags geworden. Doch während die Technologie immer besser wird, wachsen auch die Bedenken.\n\nChatGPT und ähnliche KI-Systeme können Texte schreiben, Codes programmieren und Fragen beantworten - in Sekunden. Das verändert die Arbeitswelt: In vielen Berufen - vom Journalismus bis zur Rechtsberatung - werden KI-Tools bereits eingesetzt. Manche Berufe könnten durch KI sogar überflüssig werden.\n\nDoch es gibt auch Risiken. KI-Systeme können Fehlinformationen verbreiten, Vorurteile verstärken und deepfakes erstellen - täuschend echte Videos, in denen Personen Dinge sagen, die sie nie gesagt haben. Die EU hat deshalb den AI Act verabschiedet, ein Gesetz, das KI-Anwendungen in Risikokategorien einteilt und strenge Regeln für hohe Risiken vorschreibt.\n\nBildungseinrichtungen stehen vor der Frage, wie sie mit KI umgehen sollen. Dürfen Schüler ChatGPT für Hausaufgaben nutzen? Die Meinungen gehen auseinander. Einige Schulen haben die Nutzung verboten, andere integrieren KI bewusst in den Unterricht.\n\nFür die Gesellschaft insgesamt stellt sich die Grundsatzfrage: Wie wollen wir mit dieser Technologie umgehen? „KI ist ein Werkzeug - wie der Hammer", sagt Informatikprofessor Dr. Kristian Kersting. „Ob wir damit Häuser bauen oder Fenster einschlagen, hängt von uns ab.\"",
             "questions": [
                 {"id": "q_05_03_a", "type": "multiple_choice", "questionText": "Was verändert KI laut dem Text in der Arbeitswelt?",
                  "options": ["Sie macht alle Berufe sicherer", "KI-Tools werden in vielen Berufen eingesetzt, manche könnten überflüssig werden", "Sie verbessert nur die Unterhaltung", "Sie hat keine Auswirkungen auf die Arbeit"],
                  "correctAnswer": "KI-Tools werden in vielen Berufen eingesetzt, manche könnten überflüssig werden",
                  "explanation": "'In vielen Berufen - vom Journalismus bis zur Rechtsberatung - werden KI-Tools bereits eingesetzt. Manche Berufe könnten durch KI sogar überflüssig werden.'"},
                 {"id": "q_05_03_b", "type": "true_false", "questionText": "Deepfakes sind täuschend echte Videos, in denen Personen Dinge sagen, die sie nie gesagt haben.", "correctAnswer": "true",
                  "explanation": "'deepfakes erstellen - täuschend echte Videos, in denen Personen Dinge sagen, die sie nie gesagt haben.'"},
                 {"id": "q_05_03_c", "type": "multiple_choice", "questionText": "Was hat die EU als Reaktion auf KI-Risiken verabschiedet?",
                  "options": ["Ein Verbot aller KI-Anwendungen", "Den AI Act", "Ein Gesetz nur für Deutschland", "Nichts"],
                  "correctAnswer": "Den AI Act", "explanation": "'Die EU hat deshalb den AI Act verabschiedet, ein Gesetz, das KI-Anwendungen in Risikokategorien einteilt.'"},
                 {"id": "q_05_03_d", "type": "fill_blank", "questionText": "KI ist ein ___ - wie der Hammer, sagt Professor Kersting.",
                  "correctAnswer": "Werkzeug", "explanation": "'KI ist ein Werkzeug - wie der Hammer', sagt Informatikprofessor Dr. Kristian Kersting."},
                 {"id": "q_05_03_e", "type": "multiple_choice", "questionText": "Was sind Risiken von KI-Systemen?",
                  "options": ["Nur zu langsame Antworten", "Fehlinformationen, Vorurteile und deepfakes", "Nur höhere Kosten", "Gar keine Risiken"],
                  "correctAnswer": "Fehlinformationen, Vorurteile und deepfakes",
                  "explanation": "'KI-Systeme können Fehlinformationen verbreiten, Vorurteile verstärken und deepfakes erstellen.'"}
             ],
             "keyVocabulary": [
                 {"german": "die künstliche Intelligenz (KI)", "english": "artificial intelligence (AI)", "turkish": "yapay zeka", "pos": "noun"},
                 {"german": "der Chatbot", "english": "chatbot", "turkish": "sohbet robotu", "pos": "noun"},
                 {"german": "der AI Act", "english": "AI Act", "turkish": "YZ Kanunu", "pos": "noun"},
                 {"german": "die deepfake", "english": "deepfake", "turkish": "deepfake", "pos": "noun"},
                 {"german": "die Fehlinformation", "english": "misinformation", "turkish": "yanlış bilgi", "pos": "noun"},
                 {"german": "die Vorurteile", "english": "prejudice / bias", "turkish": "önyargı", "pos": "noun"},
                 {"german": "das Werkzeug", "english": "tool", "turkish": "araç", "pos": "noun"},
                 {"german": "die Risikokategorie", "english": "risk category", "turkish": "risk kategorisi", "pos": "noun"}
             ],
             "examTip": "AI Act = neues EU-Gesetz für KI! Deepfake = täuschend echte Videos. Merksatz: 'KI ist ein Werkzeug - ob Haus bauen oder einschlagen, hängt von uns ab!'"
            },
            {"id": "b2_r_05_04", "title": "Journalismus unter Druck: Fake News und Fakten",
             "source": "Zeit Online", "sourceUrl": "https://www.zeit.de/fake-news",
             "wordCount": 305, "readingTimeMinutes": 4, "tags": ["Journalismus", "Fake News", "Medien"],
             "content": "In einer Zeit, in der jeder Mensch mit einem Klick Nachrichten verbreiten kann, wird es immer schwerer, zwischen Fakten und Fälschungen zu unterscheiden. Fake News - gefälschte Nachrichten - sind zu einem ernsthaften Problem für die Demokratie geworden.\n\nBesonders in sozialen Medien verbreiten sich Falschmeldungen oft schneller als korrekte Informationen. Studien zeigen, dass Falschinformationen auf Twitter etwa sechsmal schneller verbreitet werden als wahre Nachrichten. Der Grund: Falsche Nachrichten sind oft emotionaler und überraschender als langweilige Fakten.\n\nDie Folgen sind gravierend. Falsche Informationen können Wahlen beeinflussen, Impfskepsis fördern und gesellschaftliche Spaltung verstärken. Bei der Corona-Pandemie verbreiteten sich viele Falschmeldungen über angeblich wirksame Heilmittel oder angebliche Nebenwirkungen der Impfstoffe.\n\nDoch es gibt Gegenmaßnahmen. Fact-Checking-Organisationen wie Correctiv oder die dpa-Faktencheck prüfen Nachrichten und decken Falschmeldungen auf. Auch die Plattformen selbst - Facebook, Twitter, TikTok - haben Maßnahmen eingeführt, um Falschinformationen zu kennzeichnen oder zu entfernen.\n\nFür Bürger gilt: Kritisch bleiben, Quellen prüfen, nicht alles sofort teilen. „Lesen Sie mehr als eine Überschrift", rät Journalistin Anja Ritschel von der Bundeszentrale für politische Bildung. „Hinterfragen Sie die Quelle und seien Sie misstrauisch bei übertrieben emotionalen Geschichten.\"",
             "questions": [
                 {"id": "q_05_04_a", "type": "multiple_choice", "questionText": "Wie viel schneller verbreiten sich Falschmeldungen laut Studien auf Twitter?",
                  "options": ["Zweimal", "Sechsmal", "Zehnmal", "Gar nicht schneller"],
                  "correctAnswer": "Sechsmal", "explanation": "'Falschinformationen auf Twitter etwa sechsmal schneller verbreitet werden als wahre Nachrichten.'"},
                 {"id": "q_05_04_b", "type": "true_false", "questionText": "Falschmeldungen sind oft weniger emotional als wahrheitsgemäße Nachrichten.", "correctAnswer": "false",
                  "explanation": "'Falsche Nachrichten sind oft emotionaler und überraschender als langweilige Fakten.'"},
                 {"id": "q_05_04_c", "type": "multiple_choice", "questionText": "Was sind Beispiele für Folgen von Fake News?",
                  "options": ["Nur Spaßnachrichten", "Wahlen beeinflussen, Impfskepsis fördern, gesellschaftliche Spaltung verstärken",
                              "Nur bessere Stimmung", "Keine ernsthaften Folgen"],
                  "correctAnswer": "Wahlen beeinflussen, Impfskepsis fördern, gesellschaftliche Spaltung verstärken",
                  "explanation": "'Falsche Informationen können Wahlen beeinflussen, Impfskepsis fördern und gesellschaftliche Spaltung verstärken.'"},
                 {"id": "q_05_04_d", "type": "fill_blank", "questionText": "Fact-Checking-Organisationen wie ___ oder dpa-Faktencheck prüfen Nachrichten.",
                  "correctAnswer": "Correctiv", "explanation": "'Fact-Checking-Organisationen wie Correctiv oder die dpa-Faktencheck prüfen Nachrichten und decken Falschmeldungen auf.'"},
                 {"id": "q_05_04_e", "type": "multiple_choice", "questionText": "Was rät Anja Ritschel?",
                  "options": ["Alles sofort teilen", "Nur Überschriften lesen", "Kritisch bleiben, Quellen prüfen, nicht alles sofort teilen", "Falschmeldungen ignorieren"],
                  "correctAnswer": "Kritisch bleiben, Quellen prüfen, nicht alles sofort teilen",
                  "explanation": "'Kritisch bleiben, Quellen prüfen, nicht alles sofort teilen. „Lesen Sie mehr als eine Überschrift", rät Journalistin Anja Ritschel.'"}
             ],
             "keyVocabulary": [
                 {"german": "die Falschmeldung", "english": "false report / fake news", "turkish": "sahte haber", "pos": "noun"},
                 {"german": "das Fact-Checking", "english": "fact-checking", "turkish": "gerçek kontrolü", "pos": "noun"},
                 {"german": "die Fakten", "english": "facts", "turkish": "gerçekler", "pos": "noun"},
                 {"german": "die Spaltung", "english": "division / split", "turkish": "bölünme", "pos": "noun"},
                 {"german": "die Impfskepsis", "english": "vaccine skepticism", "turkish": "aşı şüpheciliği", "pos": "noun"},
                 {"german": "die Quelle", "english": "source", "turkish": "kaynak", "pos": "noun"},
                 {"german": "die Plattform", "english": "platform", "turkish": "platform", "pos": "noun"},
                 {"german": "die Desinformation", "english": "disinformation", "turkish": "dezenformasyon", "pos": "noun"}
             ],
             "examTip": "Fake News verbreiten sich 6x schneller als echte Nachrichten! Grund: emotionaler + überraschender. Tipp: 'Lesen Sie mehr als eine Überschrift!' Quellen immer prüfen!"
            },
            {"id": "b2_r_05_05", "title": "Smartphones in der Schule: Hilfreich oder schädlich?",
             "source": "Kultusministerkonferenz", "sourceUrl": "https://www.kmk.org/",
             "wordCount": 295, "readingTimeMinutes": 4, "tags": ["Schule", "Smartphone", "Bildung"],
             "content": "Das Smartphone ist aus dem Alltag von Jugendlichen nicht mehr wegzudenken - und damit auch aus der Schule. Etwa 95 Prozent der 12- bis 19-Jährigen besitzen ein eigenes Handy. Doch ob Smartphones im Unterricht nichts verloren haben oder sogar nützlich sein können, wird heftig diskutiert.\n\nGegner argumentieren, dass Smartphones die Konzentration stören und zu Ablenkung führen. Studien zeigen, dass bereits das Vorhandensein eines Smartphones auf dem Tisch - selbst wenn es ausgeschaltet ist - die kognitive Leistungsfähigkeit verringert. Auch Cybermobbing kann über Smartphones bis in den Schulalltag hinein wirken.\n\nBefürworter sehen dagegen enorme pädagogische Potenziale. Smartphones ermöglichen Zugang zu aktuellen Informationen, können als Wörterbuch dienen und sogar bei Experimenten in den Naturwissenschaften helfen. Digitale Bildung - also der bewusste Umgang mit Technologie - wird in einer zunehmend digitalisierten Welt immer wichtiger.\n\nEinige Länder haben Smartphones in Schulen bereits verboten oder stark eingeschränkt - etwa Frankreich, wo seit 2018 ein Handyverbot für Schüler bis 15 Jahren in der Schule gilt. Andere Länder setzen auf klare Regeln: Handys dürfen nur für bestimmte Unterrichtszwecke genutzt werden.\n\nIn Deutschland entscheidet bisher jede Schule selbst. Experten empfehlen: Die Lösung liegt in der Mitte - klare Regeln, medienpädagogische Begleitung und die Integration digitaler Geräte dort, wo sie sinnvoll sind.",
             "questions": [
                 {"id": "q_05_05_a", "type": "multiple_choice", "questionText": "Wie viel Prozent der 12- bis 19-Jährigen besitzen ein eigenes Handy?",
                  "options": ["Etwa 50 Prozent", "Etwa 75 Prozent", "Etwa 95 Prozent", "Etwa 30 Prozent"],
                  "correctAnswer": "Etwa 95 Prozent", "explanation": "'Etwa 95 Prozent der 12- bis 19-Jährigen besitzen ein eigenes Handy.'"},
                 {"id": "q_05_05_b", "type": "true_false", "questionText": "Frankreich hat ein Handyverbot für Schüler bis 15 Jahren in der Schule.", "correctAnswer": "true",
                  "explanation": "'Frankreich, wo seit 2018 ein Handyverbot für Schüler bis 15 Jahren in der Schule gilt.'"},
                 {"id": "q_05_05_c", "type": "multiple_choice", "questionText": "Was zeigen Studien über das Vorhandensein eines Smartphones?",
                  "options": ["Es verbessert die Konzentration", "Es verringert die kognitive Leistungsfähigkeit, selbst wenn es ausgeschaltet ist",
                              "Es hat keine Auswirkungen", "Es macht klüger"],
                  "correctAnswer": "Es verringert die kognitive Leistungsfähigkeit, selbst wenn es ausgeschaltet ist",
                  "explanation": "'Studien zeigen, dass bereits das Vorhandensein eines Smartphones auf dem Tisch - selbst wenn es ausgeschaltet ist - die kognitive Leistungsfähigkeit verringert.'"},
                 {"id": "q_05_05_d", "type": "fill_blank", "questionText": "Digitale ___ wird in einer zunehmend digitalisierten Welt immer wichtiger.",
                  "correctAnswer": "Bildung", "explanation": "'Digitale Bildung - also der bewusste Umgang mit Technologie - wird in einer zunehmend digitalisierten Welt immer wichtiger.'"},
                 {"id": "q_05_05_e", "type": "multiple_choice", "questionText": "Was empfehlen Experten?",
                  "options": ["Komplettes Verbot für alle", "Einfach alles erlauben", "Die Lösung liegt in der Mitte - klare Regeln und sinnvolle Integration",
                              "Nur Französisch als Vorbild nehmen"],
                  "correctAnswer": "Die Lösung liegt in der Mitte - klare Regeln und sinnvolle Integration",
                  "explanation": "'Experten empfehlen: Die Lösung liegt in der Mitte - klare Regeln, medienpädagogische Begleitung und die Integration digitaler Geräte dort, wo sie sinnvoll sind.'"}
             ],
             "keyVocabulary": [
                 {"german": "das Smartphone", "english": "smartphone", "turkish": "akıllı telefon", "pos": "noun"},
                 {"german": "die Ablenkung", "english": "distraction", "turkish": "dikkat dağılması", "pos": "noun"},
                 {"german": "die kognitive Leistungsfähigkeit", "english": "cognitive performance", "turkish": "bilişsel performans", "pos": "noun"},
                 {"german": "die digitale Bildung", "english": "digital education", "turkish": "dijital eğitim", "pos": "noun"},
                 {"german": "das Handyverbot", "english": "mobile phone ban", "turkish": "cep telefonu yasağı", "pos": "noun"},
                 {"german": "die Medienpädagogik", "english": "media education", "turkish": "medya eğitimi", "pos": "noun"},
                 {"german": "der Unterrichtszweck", "english": "educational purpose", "turkish": "eğitim amacı", "pos": "noun"},
                 {"german": "das Potenzial", "english": "potential", "turkish": "potansiyel", "pos": "noun"}
             ],
             "examTip": "95% der Jugendlichen haben Handy! Studie: Vorhandensein = weniger Konzentration, auch ausgeschaltet. Frankreich: Handyverbot bis 15! Lösung: in der Mitte - klare Regeln!"
            },
            {"id": "b2_r_05_06", "title": "Die Meinungsfreiheit und ihre Grenzen im digitalen Zeitalter",
             "source": "Bundeszentrale für politische Bildung", "sourceUrl": "https://www.bpb.de/",
             "wordCount": 305, "readingTimeMinutes": 4, "tags": ["Meinungsfreiheit", "Grundrechte", "Internet"],
             "content": "Die Meinungsfreiheit ist ein Grundpfeiler der Demokratie - doch wo endet die freie Meinungsäußerung und wo beginnt die Beleidigung, Verleumdung oder Volksverhetzung? Diese Frage stellt sich im digitalen Zeitalter mit neuer Dringlichkeit.\n\nIn Deutschland schützt das Grundgesetz in Artikel 5 die freie Meinungsäußerung. Doch dieses Recht endet dort, wo andere Rechte verletzt werden - etwa das Recht auf persönliche Ehre. Beleidigungen, Verleumdungen und falsche Tatsachenbehauptungen über bestimmte Personen können strafbar sein.\n\nBesonders problematisch ist die Grenze zwischen Meinung und Tatsachenbehauptung. „Ich finde die Partei X schlecht" - das ist eine Meinung und durch das Grundgesetz geschützt. „Die Partei X hat 100.000 Euro veruntreut" - das ist eine Tatsachenbehauptung, die beweisbar wahr oder falsch sein muss.\n\nIm Internet überschreiten viele Nutzer diese Grenzen, oft ohne sich der rechtlichen Konsequenzen bewusst zu sein. Beleidigungen im Netz - sogenanntes „Cybermobbing" - können strafrechtliche Konsequenzen haben. Auch das Posten von Hatespeech oder die Billigung von Straftaten sind keine geschützten Meinungsäußerungen.\n\nRichter urteilen zunehmend über Inhalte in sozialen Medien. „Was offline verboten ist, ist auch online verboten", betont das Bundesverfassungsgericht. Die freie Meinungsäußerung ist ein hohes Gut - aber sie endet dort, wo sie andere Menschen in ihren Rechten verletzt.",
             "questions": [
                 {"id": "q_05_06_a", "type": "multiple_choice", "questionText": "Welcher Artikel des Grundgesetzes schützt die freie Meinungsäußerung?",
                  "options": ["Artikel 1", "Artikel 3", "Artikel 5", "Artikel 10"],
                  "correctAnswer": "Artikel 5", "explanation": "'Das Grundgesetz in Artikel 5 die freie Meinungsäußerung.'"},
                 {"id": "q_05_06_b", "type": "true_false", "questionText": "Im Internet gelten andere Regeln als offline.", "correctAnswer": "false",
                  "explanation": "'Was offline verboten ist, ist auch online verboten', betont das Bundesverfassungsgericht.'"},
                 {"id": "q_05_06_c", "type": "multiple_choice", "questionText": "Was ist der Unterschied zwischen Meinung und Tatsachenbehauptung?",
                  "options": ["Es gibt keinen Unterschied", "Meinungen sind geschützt, Tatsachenbehauptungen müssen beweisbar wahr oder falsch sein",
                              "Nur Tatsachenbehauptungen sind geschützt", "Meinungen sind immer strafbar"],
                  "correctAnswer": "Meinungen sind geschützt, Tatsachenbehauptungen müssen beweisbar wahr oder falsch sein",
                  "explanation": "'Ich finde die Partei X schlecht' = Meinung (geschützt). 'Die Partei X hat 100.000 Euro veruntreut' = Tatsachenbehauptung (muss beweisbar sein)."},
                 {"id": "q_05_06_d", "type": "fill_blank", "questionText": "Beleidigungen im Netz - sogenanntes ___ - können strafrechtliche Konsequenzen haben.",
                  "correctAnswer": "Cybermobbing", "explanation": "'Beleidigungen im Netz - sogenanntes Cybermobbing - können strafrechtliche Konsequenzen haben.'"},
                 {"id": "q_05_06_e", "type": "multiple_choice", "questionText": "Wo endet die freie Meinungsäußerung laut dem Text?",
                  "options": ["Sie endet nie", "Sie endet dort, wo sie andere Menschen in ihren Rechten verletzt",
                              "Sie endet bei Facebook", "Sie endet bei Politikern"],
                  "correctAnswer": "Sie endet dort, wo sie andere Menschen in ihren Rechten verletzt",
                  "explanation": "'Die freie Meinungsäußerung ist ein hohes Gut - aber sie endet dort, wo sie andere Menschen in ihren Rechten verletzt.'"}
             ],
             "keyVocabulary": [
                 {"german": "die Meinungsfreiheit", "english": "freedom of speech", "turkish": "ifade özgürlüğü", "pos": "noun"},
                 {"german": "die Beleidigung", "english": "insult / defamation", "turkish": "hakaret", "pos": "noun"},
                 {"german": "die Verleumdung", "english": "slander / defamation", "turkish": "iftira", "pos": "noun"},
                 {"german": "die Volksverhetzung", "english": "incitement of the people", "turkish": "halkı kışkırtma", "pos": "noun"},
                 {"german": "die Tatsachenbehauptung", "english": "factual claim", "turkish": "olgusal iddia", "pos": "noun"},
                 {"german": "das Grundgesetz", "english": "Basic Law (German constitution)", "turkish": "Anayasa", "pos": "noun"},
                 {"german": "das Bundesverfassungsgericht", "english": "Federal Constitutional Court", "turkish": "Federal Anayasa Mahkemesi", "pos": "noun"},
                 {"german": "die Ehre", "english": "honor", "turkish": "şeref / onur", "pos": "noun"}
             ],
             "examTip": "GG Artikel 5 = Meinungsfreiheit! Aber: Meinung vs. Tatsachenbehauptung. Meinung geschützt ('Ich finde X schlecht'). Tatsache muss beweisbar sein! Online = offline! Was verboten ist, ist überall verboten!"
            },
            {"id": "b2_r_05_07", "title": "Online-Shopping: Der E-Commerce-Boom und seine Schattenseiten",
             "source": "Handelsblatt", "sourceUrl": "https://www.handelsblatt.com/",
             "wordCount": 300, "readingTimeMinutes": 4, "tags": ["E-Commerce", "Online-Shopping", "Wirtschaft"],
             "content": "Der Online-Handel boomt wie nie zuvor. In Deutschland wurden im Jahr 2023 etwa 85 Milliarden Euro im E-Commerce umgesetzt - ein Anstieg von 50 Prozent gegenüber 2019. Die Coronapandemie hat den Trend stark beschleunigt. Doch der Boom hat auch negative Seiten.\n\nFür Verbraucher bietet Online-Shopping unschlagbare Vorteile: Bequemlichkeit, Preivergleich und eine riesige Auswahl. Allerdings klagen viele über die zunehmende Paketflut und die Umweltbelastung durch Verpackungsmüll. Etwa 18 Kilogramm Verpackungsmüll pro Person und Jahr entstehen durch Online-Bestellungen.\n\nFür den stationären Handel - also Geschäfte in Innenstädten - wird die Konkurrenz durch Online-Shops immer bedrohlicher. Viele Innenstädte kämpfen mit leerstehenden Geschäften, was nicht nur ein wirtschaftliches, sondern auch ein soziales Problem darstellt. Die Straßen werden unbelebter, soziale Treffpunkte gehen verloren.\n\nAuch Arbeitsrechte im Online-Handel stehen in der Kritik. Paketboten arbeiten oft unter prekären Bedingungen: niedrige Löhne, Zeitdruck und unsichere Verträge. Plattformarbeit - also die Vermittlung von Aufträgen über Apps - umgeht oft geltendes Arbeitsrecht.\n\nExperten fordern eine stärkere Regulierung des E-Commerce: Mehr Nachhaltigkeitsauflagen für Online-Händler, bessere Arbeitsbedingungen für Paketboten und eine stärkere Unterstützung für den stationären Handel. „Der Online-Boom darf nicht auf Kosten der Umwelt und der Arbeiter gehen", sagt Verbraucherschützerin Ursula Lindhorst.",
             "questions": [
                 {"id": "q_05_07_a", "type": "multiple_choice", "questionText": "Wie viel Milliarden Euro wurden 2023 in Deutschland im E-Commerce umgesetzt?",
                  "options": ["Etwa 30 Milliarden", "Etwa 50 Milliarden", "Etwa 85 Milliarden", "Etwa 120 Milliarden"],
                  "correctAnswer": "Etwa 85 Milliarden", "explanation": "'In Deutschland wurden im Jahr 2023 etwa 85 Milliarden Euro im E-Commerce umgesetzt.'"},
                 {"id": "q_05_07_b", "type": "true_false", "questionText": "Online-Shopping verursacht keinen Verpackungsmüll.", "correctAnswer": "false",
                  "explanation": "'etwa 18 Kilogramm Verpackungsmüll pro Person und Jahr entstehen durch Online-Bestellungen.'"},
                 {"id": "q_05_07_c", "type": "multiple_choice", "questionText": "Was ist ein soziales Problem des Online-Handels?",
                  "options": ["Zu viele neue Geschäfte werden eröffnet", "Innenstädte werden unbelebter, soziale Treffpunkte gehen verloren",
                              "Die Preise steigen zu schnell", "Es gibt zu viele Paketboten"],
                  "correctAnswer": "Innenstädte werden unbelebter, soziale Treffpunkte gehen verloren",
                  "explanation": "'Die Straßen werden unbelebter, soziale Treffpunkte gehen verloren.'"},
                 {"id": "q_05_07_d", "type": "fill_blank", "questionText": "Paketboten arbeiten oft unter ___ Bedingungen: niedrige Löhne, Zeitdruck und unsichere Verträge.",
                  "correctAnswer": "prekären", "explanation": "'Paketboten arbeiten oft unter prekären Bedingungen: niedrige Löhne, Zeitdruck und unsichere Verträge.'"},
                 {"id": "q_05_07_e", "type": "multiple_choice", "questionText": "Was fordern Experten?",
                  "options": ["Weniger Regulierung", "Mehr Nachhaltigkeitsauflagen, bessere Arbeitsbedingungen, Unterstützung für stationären Handel",
                              "Nur niedrigere Preise", "Abschaffung des Online-Handels"],
                  "correctAnswer": "Mehr Nachhaltigkeitsauflagen, bessere Arbeitsbedingungen, Unterstützung für stationären Handel",
                  "explanation": "'Experten fordern eine stärkere Regulierung des E-Commerce: Mehr Nachhaltigkeitsauflagen, bessere Arbeitsbedingungen für Paketboten und eine stärkere Unterstützung für den stationären Handel.'"}
             ],
             "keyVocabulary": [
                 {"german": "der E-Commerce", "english": "e-commerce / online shopping", "turkish": "e-ticaret / online alışveriş", "pos": "noun"},
                 {"german": "der Online-Handel", "english": "online trade", "turkish": "online ticaret", "pos": "noun"},
                 {"german": "der stationäre Handel", "english": "brick-and-mortar retail", "turkish": "fiziksel ticaret", "pos": "noun"},
                 {"german": "die Paketflut", "english": "parcel flood", "turkish": "paket seli", "pos": "noun"},
                 {"german": "die Verpackungsmüll", "english": "packaging waste", "turkish": "ambalaj atığı", "pos": "noun"},
                 {"german": "die Innenstadt", "english": "city center", "turkish": "şehir merkezi", "pos": "noun"},
                 {"german": "prekär", "english": "precarious", "turkish": "kırılgan / güvencesiz", "pos": "adjective"},
                 {"german": "die Plattformarbeit", "english": "platform work", "turkish": "platform çalışması", "pos": "noun"}
             ],
             "examTip": "85 Mrd € E-Commerce 2023! 18 kg Verpackungsmüll pro Person durch Online-Shopping! Problem: stationärer Handel stirbt. Lösung: Regulierung + Nachhaltigkeit + bessere Arbeitsbedingungen!"
            },
            {"id": "b2_r_05_08", "title": "Smart Home: Das vernetzte Zuhause",
             "source": "Bitkom", "sourceUrl": "https://www.bitkom.org/",
             "wordCount": 295, "readingTimeMinutes": 4, "tags": ["Smart Home", "Digitalisierung", "Alltag"],
             "content": "Licht einschalten per Sprachbefehl, die Heizung vom Büro aus regulieren oder per Kamera sehen, wer vor der Tür steht - Smart-Home-Geräte werden in deutschen Haushalten immer beliebter. Etwa 30 Prozent der deutschen Haushalte nutzen mittlerweile mindestens ein smartes Gerät.\n\nDie Vorteile liegen auf der Hand: Komfort, Energieersparnis und mehr Sicherheit. Intelligente Thermostate können den Energieverbrauch um bis zu 30 Prozent senken, indem sie die Heizung automatisch reduzieren, wenn niemand zu Hause ist. Smarte Türklingeln mit Kamera können Einbrüche verhindern oder zumindest aufklären helfen.\n\nDoch es gibt auch Risiken. Jedes vernetzte Gerät ist potenziell ein Einfallstor für Hacker. Datenschützer warnen: Viele Smart-Home-Geräte senden Daten an Herstellererver in aller Welt, oft ohne dass Nutzer davon wissen. Die Sammlung von Nutzerdaten durch Smart-Home-Anbieter ist ein ernstes Privatsphäre-Problem.\n\nAuch die Abhängigkeit von Technik kann zum Problem werden. Was passiert, wenn das WLAN ausfällt oder der Cloud-Dienst des Herstellers nicht mehr verfügbar ist? Verbraucherschützer empfehlen, vor dem Kauf auf Datenschutz und Sicherheitsstandards zu achten.\n\nDer Smart-Home-Markt wächst weiter. Experten schätzen, dass in fünf Jahren bereits die Hälfte aller deutschen Haushalte smarte Geräte nutzen könnte. Die Branche fordert einheitliche Standards, damit Geräte unterschiedlicher Hersteller besser zusammenarbeiten können.",
             "questions": [
                 {"id": "q_05_08_a", "type": "multiple_choice", "questionText": "Wie viel Prozent der deutschen Haushalte nutzen mindestens ein smartes Gerät?",
                  "options": ["Etwa 10 Prozent", "Etwa 30 Prozent", "Etwa 50 Prozent", "Etwa 70 Prozent"],
                  "correctAnswer": "Etwa 30 Prozent", "explanation": "'Etwa 30 Prozent der deutschen Haushalte nutzen mittlerweile mindestens ein smartes Gerät.'"},
                 {"id": "q_05_08_b", "type": "true_false", "questionText": "Intelligente Thermostate können den Energieverbrauch um bis zu 30 Prozent senken.", "correctAnswer": "true",
                  "explanation": "'Intelligente Thermostate können den Energieverbrauch um bis zu 30 Prozent senken.'"},
                 {"id": "q_05_08_c", "type": "multiple_choice", "questionText": "Was ist ein Risiko von Smart-Home-Geräten?",
                  "options": ["Sie verbrauchen zu viel Strom", "Jedes vernetzte Gerät ist potenziell ein Einfallstor für Hacker",
                              "Sie sind zu teuer", "Sie funktionieren nie"],
                  "correctAnswer": "Jedes vernetzte Gerät ist potenziell ein Einfallstor für Hacker",
                  "explanation": "'Jedes vernetzte Gerät ist potenziell ein Einfallstor für Hacker.'"},
                 {"id": "q_05_08_d", "type": "fill_blank", "questionText": "Die Sammlung von Nutzerdaten durch Smart-Home-Anbieter ist ein ernstes ___.",
                  "correctAnswer": "Privatsphäre-Problem", "explanation": "'Die Sammlung von Nutzerdaten durch Smart-Home-Anbieter ist ein ernstes Privatsphäre-Problem.'"},
                 {"id": "q_05_08_e", "type": "multiple_choice", "questionText": "Was fordert die Branche?",
                  "options": ["Weniger Geräte", "Einheitliche Standards für bessere Zusammenarbeit der Geräte", "Abschaffung von Smart Home", "Nur deutsche Geräte"],
                  "correctAnswer": "Einheitliche Standards für bessere Zusammenarbeit der Geräte",
                  "explanation": "'Die Branche fordert einheitliche Standards, damit Geräte unterschiedlicher Hersteller besser zusammenarbeiten können.'"}
             ],
             "keyVocabulary": [
                 {"german": "das Smart Home", "english": "smart home", "turkish": "akıllı ev", "pos": "noun"},
                 {"german": "das vernetzte Gerät", "english": "connected device", "turkish": "bağlı cihaz", "pos": "noun"},
                 {"german": "der Hacker", "english": "hacker", "turkish": "hacker", "pos": "noun"},
                 {"german": "die Privatsphäre", "english": "privacy", "turkish": "gizlilik", "pos": "noun"},
                 {"german": "das Thermostat", "english": "thermostat", "turkish": "termostat", "pos": "noun"},
                 {"german": "der Einbruch", "english": "burglary", "turkish": "hırsızlık / soygun", "pos": "noun"},
                 {"german": "der Cloud-Dienst", "english": "cloud service", "turkish": "bulut hizmeti", "pos": "noun"},
                 {"german": "der Datenschutz", "english": "data protection", "turkish": "veri koruma", "pos": "noun"}
             ],
             "examTip": "30% der Haushalte nutzen Smart Home! Thermostate: bis 30% Energie sparen! Risiko: Hacker + Datenschutz! Lösung: einheitliche Standards!"
            },
            {"id": "b2_r_05_09", "title": "Influencer: Die neuen Meinungsmacher",
             "source": "Mediensoziologie TU Berlin", "sourceUrl": "https://www.tu-berlin.de/",
             "wordCount": 290, "readingTimeMinutes": 4, "tags": ["Influencer", "Social Media", "Werbung"],
             "content": "Influencer - Menschen mit großer Online-Fangemeinde - sind zu einer der wichtigsten Marketingplattformen für Unternehmen geworden. Allein in Deutschland gibt es schätzungsweise 100.000 aktive Influencer, die mit Marken zusammenarbeiten. Der Markt für Influencer-Marketing hat ein Volumen von etwa 1,5 Milliarden Euro jährlich.\n\nFür viele junge Menschen sind Influencer zu Vorbildern geworden. Sie prägen Trends bei Mode, Kosmetik, Reisen und sogar bei politischen Meinungen. Besonders auf Instagram und TikTok sind Beauty-, Lifestyle- und Fitness-Influencer erfolgreich.\n\nDoch die Branche ist umstritten. Kritiker bemängeln fehlende Transparenz: Viele Influencer bewerben Produkte, ohne klar zu kennzeichnen, dass es sich um bezahlte Werbung handelt. Dies verstößt gegen geltendes Recht - seit 2022 müssen alle kommerziellen Beiträge in sozialen Medien eindeutig als „Werbung" oder „Anzeige" gekennzeichnet werden.\n\nEin weiteres Problem ist die Verbreitung von unrealistischen Körperbildern und Lebensstilen. Gerade bei jungen Mädchen können Beauty-Influencer zu Essstörungen und geringem Selbstwertgefühl beitragen. Psychologen warnen vor den negativen Auswirkungen permanenten Vergleichens auf Social Media.\n\nAndererseits nutzen einige Influencer ihre Reichweite auch für soziale Zwecke - etwa für Umweltkampagnen, Spendenaktionen oder politische Aufklärung. Die Grenze zwischen positivem und problematischem Einfluss verläuft nicht zwischen einzelnen Plattformen, sondern innerhalb jeder einzelnen Community.",
             "questions": [
                 {"id": "q_05_09_a", "type": "multiple_choice", "questionText": "Wie groß ist der Influencer-Markt in Deutschland jährlich?",
                  "options": ["Etwa 500 Millionen Euro", "Etwa 1,5 Milliarden Euro", "Etwa 5 Milliarden Euro", "Etwa 10 Milliarden Euro"],
                  "correctAnswer": "Etwa 1,5 Milliarden Euro", "explanation": "'Der Markt für Influencer-Marketing hat ein Volumen von etwa 1,5 Milliarden Euro jährlich.'"},
                 {"id": "q_05_09_b", "type": "true_false", "questionText": "Seit 2022 müssen kommerzielle Beiträge in sozialen Medien nicht mehr gekennzeichnet werden.", "correctAnswer": "false",
                  "explanation": "'Seit 2022 müssen alle kommerziellen Beiträge in sozialen Medien eindeutig als „Werbung\" oder „Anzeige\" gekennzeichnet werden.'"},
                 {"id": "q_05_09_c", "type": "multiple_choice", "questionText": "Was kritisieren Psychologen an Beauty-Influencern?",
                  "options": ["Sie zeigen zu realistische Bilder", "Sie können zu Essstörungen und geringem Selbstwertgefühl beitragen",
                              "Sie sind zu ehrlich", "Sie beeinflussen niemanden"],
                  "correctAnswer": "Sie können zu Essstörungen und geringem Selbstwertgefühl beitragen",
                  "explanation": "'Gerade bei jungen Mädchen können Beauty-Influencer zu Essstörungen und geringem Selbstwertgefühl beitragen.'"},
                 {"id": "q_05_09_d", "type": "fill_blank", "questionText": "Kommerzielle Beiträge müssen seit 2022 als ___ oder Anzeige gekennzeichnet werden.",
                  "correctAnswer": "Werbung", "explanation": "'Seit 2022 müssen alle kommerziellen Beiträge in sozialen Medien eindeutig als „Werbung\" oder „Anzeige\" gekennzeichnet werden.'"},
                 {"id": "q_05_09_e", "type": "multiple_choice", "questionText": "Was nutzen einige Influencer ihre Reichweite laut dem Text auch für?",
                  "options": ["Nur für Einkaufen", "Für soziale Zwecke wie Umweltkampagnen und politische Aufklärung", "Nur für Beauty", "Für gar nichts"],
                  "correctAnswer": "Für soziale Zwecke wie Umweltkampagnen und politische Aufklärung",
                  "explanation": "'Andererseits nutzen einige Influencer ihre Reichweite auch für soziale Zwecke - etwa für Umweltkampagnen, Spendenaktionen oder politische Aufklärung.'"}
             ],
             "keyVocabulary": [
                 {"german": "der Influencer", "english": "influencer", "turkish": "fenomen / influencer", "pos": "noun"},
                 {"german": "die Reichweite", "english": "reach / range", "turkish": "erişim / menzil", "pos": "noun"},
                 {"german": "das Influencer-Marketing", "english": "influencer marketing", "turkish": "fenomen pazarlaması", "pos": "noun"},
                 {"german": "die Werbekennzeichnung", "english": "advertising label", "turkish": "reklam etiketi", "pos": "noun"},
                 {"german": "die Essstörung", "english": "eating disorder", "turkish": "yeme bozukluğu", "pos": "noun"},
                 {"german": "die Fangemeinde", "english": "fan community", "turkish": "hayran topluluğu", "pos": "noun"},
                 {"german": "die Körperbilder", "english": "body images", "turkish": "vücut imajları", "pos": "noun"},
                 {"german": "die politische Aufklärung", "english": "political education", "turkish": "siyasi eğitim", "pos": "noun"}
             ],
             "examTip": "1,5 Mrd € Influencer-Markt in Deutschland! Werbung muss seit 2022 gekennzeichnet werden! Kritik: unrealistische Körperbilder → Essstörungen! Aber auch positive Nutzung: Umweltkampagnen!"
            },
            {"id": "b2_r_05_10", "title": "E-Sport: Wenn Gaming zum Sport wird",
             "source": "ESBD Deutschland", "sourceUrl": "https://www.esbd-deutschland.de/",
             "wordCount": 285, "readingTimeMinutes": 4, "tags": ["E-Sport", "Gaming", "Sport"],
             "content": "E-Sport - also das Spielen von Videospielen auf Wettbewerbsniveau - hat sich in den letzten Jahren zu einem Massenphänomen entwickelt. Weltweit schauen Millionen Menschen E-Sport-Turniere, und die besten Spieler können mit Profisportlern mithalten - sowohl in puncto Geschicklichkeit als auch beim Einkommen.\n\nIn Deutschland hat sich der E-Sport in den letzten Jahren professionalisiert. Der ESBD (E-Sport-Bund Deutschland) vertritt die Interessen der deutschen E-Sport-Szene und setzt sich für eine bessere Anerkennung ein. Seit 2023 ist E-Sport in Deutschland als eigenständige Sportart vom DOSB anerkannt.\n\nDie Vorteile des E-Sports werden oft unterschätzt. E-Sport erfordert schnelle Reaktionsfähigkeit, taktisches Denken, Teamarbeit und Frustrationstoleranz. Studien zeigen, dass regelmäßige E-Sport-Spieler oft bessere kognitive Fähigkeiten haben als Nicht-Spieler. Auch im Bereich der Rehabilitation - etwa nach Schlaganfällen - wird E-Sport therapeutisch eingesetzt.\n\nKritiker sehen jedoch auch Schattenseiten. Die intensive Nutzung kann zu Suchtverhalten führen, und die Sitzhaltung vor dem Bildschirm ist aus orthopädischer Sicht problematisch. Auch die Kosten für eine professionelle E-Sport-Ausrüstung können hoch sein, was eine soziale Selektion verstärken kann.\n\nFür die Zukunft prognostizieren Experten weiteres Wachstum. E-Sport könnte bei den Olympischen Spielen erscheinen - die Diskussion darüber hat bereits begonnen.",
             "questions": [
                 {"id": "q_05_10_a", "type": "multiple_choice", "questionText": "Wann wurde E-Sport als eigenständige Sportart vom DOSB anerkannt?",
                  "options": ["2018", "2020", "2023", "Noch gar nicht"],
                  "correctAnswer": "2023", "explanation": "'Seit 2023 ist E-Sport in Deutschland als eigenständige Sportart vom DOSB anerkannt.'"},
                 {"id": "q_05_10_b", "type": "true_false", "questionText": "E-Sport erfordert schnelle Reaktionsfähigkeit, taktisches Denken und Teamarbeit.", "correctAnswer": "true",
                  "explanation": "'E-Sport erfordert schnelle Reaktionsfähigkeit, taktisches Denken, Teamarbeit und Frustrationstoleranz.'"},
                 {"id": "q_05_10_c", "type": "multiple_choice", "questionText": "Was ist ein orthopädisches Problem beim E-Sport?",
                  "options": ["Zu viel Bewegung", "Die Sitzhaltung vor dem Bildschirm", "Zu schwere Controller", "Zu laute Geräusche"],
                  "correctAnswer": "Die Sitzhaltung vor dem Bildschirm", "explanation": "'Die Sitzhaltung vor dem Bildschirm ist aus orthopädischer Sicht problematisch.'"},
                 {"id": "q_05_10_d", "type": "fill_blank", "questionText": "Der ESBD vertritt die Interessen der deutschen E-Sport-___.",
                  "correctAnswer": "Szene", "explanation": "'Der ESBD (E-Sport-Bund Deutschland) vertritt die Interessen der deutschen E-Sport-Szene.'"},
                 {"id": "q_05_10_e", "type": "multiple_choice", "questionText": "Wo wird E-Sport laut dem Text auch therapeutisch eingesetzt?",
                  "options": ["In der Küche", "In der Rehabilitation, etwa nach Schlaganfällen", "Im Sporttraining", "In der Schule"],
                  "correctAnswer": "In der Rehabilitation, etwa nach Schlaganfällen",
                  "explanation": "'Auch im Bereich der Rehabilitation - etwa nach Schlaganfällen - wird E-Sport therapeutisch eingesetzt.'"}
             ],
             "keyVocabulary": [
                 {"german": "der E-Sport", "english": "e-sports", "turkish": "e-spor", "pos": "noun"},
                 {"german": "das Turnier", "english": "tournament", "turkish": "turnuva", "pos": "noun"},
                 {"german": "die Reaktionsfähigkeit", "english": "reaction ability", "turkish": "reaksiyon yeteneği", "pos": "noun"},
                 {"german": "die Frustrationstoleranz", "english": "frustration tolerance", "turkish": "hayal kırıklığı toleransı", "pos": "noun"},
                 {"german": "die Rehabilitation", "english": "rehabilitation", "turkish": "rehabilitasyon", "pos": "noun"},
                 {"german": "der DOSB", "english": "German Olympic Sports Confederation", "turkish": "Alman Olimpik Sporlar Konfederasyonu", "pos": "noun"},
                 {"german": "die Sucht", "english": "addiction", "turkish": "bağımlılık", "pos": "noun"},
                 {"german": "die orthopädisch", "english": "orthopedic", "turkish": "ortopedik", "pos": "adjective"}
             ],
             "examTip": "E-Sport = DOSB-anerkannt seit 2023! Vorteile: Reaktionsfähigkeit, Taktik, Teamwork. Nachteile: Suchtgefahr, Sitzhaltung. Therapeutisch: Rehabilitation nach Schlaganfall!"
            }
        ]
    }
}

def generate_all():
    all_readings = []
    topics_info = []
    for tid, tdata in TOPICS_DATA.items():
        topics_info.append({"id": tid, "name": tdata["name"], "nameEn": tdata["nameEn"], "iconEmoji": tdata["iconEmoji"], "textCount": len(tdata["texts"])})
        all_readings.extend(tdata["texts"])
    return {"generatedAt": datetime.now().isoformat(), "topics": topics_info, "readings": all_readings}

if __name__ == "__main__":
    data = generate_all()
    with open("b2_reading_topics_5_12.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Generated {len(data['readings'])} texts with {sum(len(r['questions']) for r in data['readings'])} questions")
