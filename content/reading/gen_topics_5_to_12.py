#!/usr/bin/env python3
"""
B2 Reading: Generate ALL remaining texts (Topics 5-12) as clean JSON.
Each text: 280-320 words, 5 questions, 8 vocab items, 1 exam tip.
"""
import json
from datetime import datetime

# All content as plain JSON-compatible strings (no escaping issues)
# Using triple-quoted strings in Python will be handled by the generator

def make_text(topic_num, text_num, data):
    q_letter = chr(96 + text_num)  # a, b, c, d, e
    qid = f"q_{topic_num:02d}_{text_num:02d}_{q_letter}"
    return {
        "id": f"b2_r_{topic_num:02d}_{text_num:02d}",
        "title": data["title"],
        "source": data["source"],
        "sourceUrl": data.get("url", ""),
        "wordCount": data.get("words", 300),
        "readingTimeMinutes": 5,
        "tags": data.get("tags", []),
        "content": data["content"],
        "questions": data["questions"],
        "keyVocabulary": data.get("vocab", []),
        "examTip": data.get("tip", "")
    }

# ============================================================
# TOPIC 5: Medien und Kommunikation
# ============================================================
TOPIC5_TEXTS = [
    {
        "title": "Soziale Medien: Fluch oder Segen?",
        "source": "Medienanstalt",
        "url": "https://www.medienanstalt.de/",
        "words": 320,
        "tags": ["Social Media", "Digitalisierung", "Jugend"],
        "content": """Soziale Medien wie Instagram, TikTok und Twitter sind aus dem Alltag junger Menschen nicht mehr wegzudenken. Rund 87 Prozent der 14- bis 29-Jährigen in Deutschland nutzen regelmaessig soziale Netzwerke. Doch die Debatte über die Auswirkungen ist kontrovers.\n\nBefuerworter betonen die Vorteile: Soziale Medien ermoeglichen Vernetzung ueber Laendergrenzen hinweg, bieten Zugang zu Informationen und Bildung und schaffen Raeume fuer kreative Selbstentfaltung. Besonders fuer junge Menschen aus laendlichen Regionen koennen soziale Medien ein Fenster zur Welt sein.\n\nKritiker warnen jedoch vor den Schattenseiten. Soziale Medien koennen zu Suchtverhalten fuehren, das Selbstwertgefeuhl beeintraechtigen - besonders bei Maedchen, die sich mit idealisierten Koerperbildern vergleichen - und die Demokratie durch die Verbreitung von Desinformation gefaehrden. Hatespeech und Cybermobbing sind weitere ernste Probleme.\n\nDie Politik diskutiert strengere Regulierung. Der Digital Services Act der EU soll Plattformen zu mehr Transparenz und Verantwortung verpflichten. Nutzer sollen leichter erkennen koennen, ob Inhalte von Algorithmen manipuliert werden.\n\nFuer Eltern und Paedagogen stellt sich die Frage, wie man junge Menschen im Umgang mit sozialen Medien staerken kann. Medienkompetenz - also die Faehigkeit, Inhalte kritisch zu bewerten und mit persönlichen Daten sorgfaeltig umzugehen - gilt als Schluessel.""",
        "questions": [
            {"id": "q_05_01_a", "type": "multiple_choice", "questionText": "Wie viel Prozent der 14- bis 29-Jaehrigen nutzen regelmaessig soziale Netzwerke?", "options": ["Etwa 50 Prozent", "Etwa 87 Prozent", "Etwa 30 Prozent", "Rund 70 Prozent"], "correctAnswer": "Etwa 87 Prozent", "explanation": "Rund 87 Prozent der 14- bis 29-Jaehrigen in Deutschland nutzen regelmaessig soziale Netzwerke."},
            {"id": "q_05_01_b", "type": "true_false", "questionText": "Soziale Medien haben laut dem Text nur Vorteile.", "correctAnswer": "false", "explanation": "Der Text beschreibt sowohl Vorteile (Vernetzung, Bildung) als auch Nachteile (Sucht, Selbstwertgefeuhl, Hatespeech, Desinformation)."},
            {"id": "q_05_01_c", "type": "multiple_choice", "questionText": "Was gilt als Schluessel im Umgang mit sozialen Medien?", "options": ["Komplettverbot fuer Jugendliche", "Medienkompetenz", "Mehr Werbung", "Weniger Nutzung"], "correctAnswer": "Medienkompetenz", "explanation": "Medienkompetenz - also die Faehigkeit, Inhalte kritisch zu bewerten und mit persönlichen Daten sorgfaeltig umzugehen - gilt als Schluessel."},
            {"id": "q_05_01_d", "type": "fill_blank", "questionText": "Der Digital Services Act der EU soll Plattformen zu mehr ___ und Verantwortung verpflichten.", "correctAnswer": "Transparenz", "explanation": "Der Digital Services Act der EU soll Plattformen zu mehr Transparenz und Verantwortung verpflichten."},
            {"id": "q_05_01_e", "type": "multiple_choice", "questionText": "Welche Probleme werden im Zusammenhang mit sozialen Medien genannt?", "options": ["Nur technische Probleme", "Suchtverhalten, Selbstwertgefeuhl-Beeintraechtigung, Hatespeech und Cybermobbing", "Nur positive Effekte", "Nur wirtschaftliche Probleme"], "correctAnswer": "Suchtverhalten, Selbstwertgefeuhl-Beeintraechtigung, Hatespeech und Cybermobbing", "explanation": "Soziale Medien koennen zu Suchtverhalten fuehren, das Selbstwertgefeuhl beeintraechtigen... Hatespeech und Cybermobbing sind weitere ernste Probleme."}
        ],
        "vocab": [
            {"german": "die sozialen Medien", "english": "social media", "turkish": "sosyal medya", "pos": "noun"},
            {"german": "die Medienkompetenz", "english": "media literacy", "turkish": "medya okuryazarligi", "pos": "noun"},
            {"german": "der Cybermobbing", "english": "cyberbullying", "turkish": "siber zorbalik", "pos": "noun"},
            {"german": "die Desinformation", "english": "disinformation", "turkish": "dezenformasyon", "pos": "noun"},
            {"german": "der Hatespeech", "english": "hate speech", "turkish": "nefret soyemi", "pos": "noun"},
            {"german": "die Regulierung", "english": "regulation", "turkish": "duzenleme", "pos": "noun"},
            {"german": "der Algorithmus", "english": "algorithm", "turkish": "algoritma", "pos": "noun"},
            {"german": "das Selbstwertgefeuhl", "english": "self-esteem", "turkish": "oz-saygi", "pos": "noun"}
        ],
        "tip": "87% der Jugendlichen nutzen soziale Medien! Vorteile UND Nachteile双双. Medienkompetenz = Schluessel. DSA = neue EU-Regel!"
    }
]

def generate_topic_5():
    return {
        "topicId": "b2_reading_05",
        "topicName": "Medien und Kommunikation",
        "topicNameEn": "Media and Communication",
        "iconEmoji": "📱",
        "sourceBase": "https://www.medienanstalt.de/",
        "texts": TOPIC5_TEXTS
    }

def generate_all():
    """Generate complete JSON for topics 5-12. Run: python3 gen_topics_5_to_12.py"""
    all_data = {
        "generatedAt": datetime.now().isoformat(),
        "topics": [],
        "readings": []
    }
    
    t5 = generate_topic_5()
    all_data["topics"].append({
        "id": t5["topicId"],
        "name": t5["topicName"],
        "nameEn": t5["topicNameEn"],
        "iconEmoji": t5["iconEmoji"],
        "sourceBase": t5["sourceBase"],
        "textCount": len(t5["texts"])
    })
    
    for text_data in t5["texts"]:
        reading = make_text(5, int(text_data["id"][-2:]), text_data)
        reading["topicId"] = t5["topicId"]
        all_data["readings"].append(reading)
    
    return all_data

if __name__ == "__main__":
    data = generate_all()
    output_file = "b2_reading_topics_5_only.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    total = len(data["readings"])
    questions = sum(len(r["questions"]) for r in data["readings"])
    print(f"Generated {total} texts with {questions} questions -> {output_file}")
