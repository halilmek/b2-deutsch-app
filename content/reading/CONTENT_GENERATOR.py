#!/usr/bin/env python3
"""
B2 Deutsch — Reading Content Generator
=======================================
Generates B2-level reading texts and quiz questions.
Run: python3 CONTENT_GENERATOR.py --topic 3 --count 10

Topics:
  1 = Beruf und Arbeitswelt          (DONE)
  2 = Gesundheit und Medizin         (DONE)
  3 = Umwelt und Natur               (DONE)
  4 = Gesellschaft und Soziales
  5 = Medien und Kommunikation
  6 = Bildung und Erziehung
  7 = Reisen und Tourismus
  8 = Wirtschaft und Finanzen
  9 = Kultur und Freizeit
  10 = Wissenschaft und Technik
  11 = Politik und Zeitgeschehen
  12 = Beziehungen und persönliche Erfahrungen
"""

import json
import uuid
import argparse
from datetime import datetime

# ============================================================
# TOPIC TEMPLATES
# Each topic has 10 texts = 50 questions total
# ============================================================

TOPICS = {
    "b2_reading_03": {
        "name": "Umwelt und Natur",
        "nameEn": "Environment and Nature",
        "iconEmoji": "🌍",
        "texts": [
            {
                "id": "b2_r_03_01", "title": "Klimawandel: Die Erde erwärmt sich", "source": "Umweltbundesamt",
                "sourceUrl": "https://www.umweltbundesamt.de/", "wordCount": 340, "readingTimeMinutes": 5,
                "tags": ["Klimawandel", "Treibhausgase", "Pariser Abkommen"],
                "content": """Der Klimawandel ist die größte Herausforderung unserer Zeit. Nach Angaben des Umweltbundesamtes hat sich die globale Durchschnittstemperatur seit der industriellen Revolution um etwa 1,2 Grad Celsius erhöht. Das klingt wenig, hat aber massive Auswirkungen auf das Klima weltweit.

Die Folgen sind bereits sichtbar: Gletscher schmelzen, der Meeresspiegel steigt, und extreme Wetterereignisse wie Hitzewellen, Dürren und Überschwemmungen werden häufiger. In Deutschland nahmen die sommerlichen Hitzetage in den letzten Jahrzehnten deutlich zu.

Die Hauptursache des Klimawandels ist der Ausstoß von Treibhausgasen, insbesondere Kohlendioxid (CO2). Dieses Gas entsteht hauptsächlich durch die Verbrennung fossiler Brennstoffe wie Kohle, Erdöl und Erdgas – also durch Stromerzeugung, Verkehr und Industrie.

Um die Erderwärmung zu begrenzen, hat sich die internationale Staatengemeinschaft im Pariser Klimaabkommen von 2015 das Ziel gesetzt, die globale Erwärmung auf 1,5 bis 2 Grad Celsius zu begrenzen. Um dieses Ziel zu erreichen, müssen die CO2-Emissionen drastisch reduziert werden – idealerweise bis 2050 auf nahezu null.

Deutschland hat sich zum Ziel gesetzt, bis 2045 klimaneutral zu werden. Das bedeutet, dass kaum noch Treibhausgase ausgestoßen werden sollen. Erreicht werden soll dies durch den Ausbau erneuerbarer Energien, die Elektrifizierung des Verkehrs und die Verbesserung der Energieeffizienz von Gebäuden.

Kritiker bemängeln, dass die bisherigen Maßnahmen nicht ausreichen und die Klimaziele nicht erreicht werden. Befürworter betonen jedoch, dass der Wandel bereits begonnen hat – und dass jede Maßnahme zählt.""",
                "questions": [
                    {"id": "q_03_01_a", "type": "multiple_choice", "questionText": "Um wie viel Grad hat sich die globale Durchschnittstemperatur erhöht?", "options": ["Etwa 0,5 Grad", "Etwa 1,2 Grad", "Etwa 3 Grad", "Etwa 5 Grad"], "correctAnswer": "Etwa 1,2 Grad", "explanation": "Das Umweltbundesamt gibt an: 'um etwa 1,2 Grad Celsius'"},
                    {"id": "q_03_01_b", "type": "true_false", "questionText": "Die Hauptursache des Klimawandels ist der Ausstoß von Treibhausgasen.", "correctAnswer": "true", "explanation": "Der Text bestätigt: 'Die Hauptursache des Klimawandels ist der Ausstoß von Treibhausgasen.'"},
                    {"id": "q_03_01_c", "type": "multiple_choice", "questionText": "Welches Ziel hat das Pariser Klimaabkommen?", "options": ["Die Erwärmung auf 5 Grad begrenzen", "Die Erwärmung auf 1,5 bis 2 Grad begrenzen", "Klimaneutralität bis 2030", "Abschaffung aller Industrie"], "correctAnswer": "Die Erwärmung auf 1,5 bis 2 Grad begrenzen", "explanation": "Das Pariser Abkommen Ziel: 'die globale Erwärmung auf 1,5 bis 2 Grad Celsius zu begrenzen.'"},
                    {"id": "q_03_01_d", "type": "fill_blank", "questionText": "Fossile Brennstoffe wie Kohle und Erdöl setzen beim Verbrennen ___ (CO2) frei.", "correctAnswer": "Kohlendioxid", "explanation": "Hauptursache: 'hauptsächlich durch die Verbrennung fossiler Brennstoffe wie Kohle, Erdöl und Erdgas'"},
                    {"id": "q_03_01_e", "type": "multiple_choice", "questionText": "Bis wann soll Deutschland klimaneutral werden?", "options": ["Bis 2030", "Bis 2045", "Bis 2050", "Bis 2060"], "correctAnswer": "Bis 2045", "explanation": "Deutschland hat sich das Ziel gesetzt: 'bis 2045 klimaneutral zu werden.'"}
                ],
                "keyVocabulary": [
                    {"german": "der Klimawandel", "english": "climate change", "turkish": "iklim değişikliği", "pos": "noun"},
                    {"german": "die Erderwärmung", "english": "global warming", "turkish": "küresel ısınma", "pos": "noun"},
                    {"german": "das Treibhausgas", "english": "greenhouse gas", "turkish": "sera gazı", "pos": "noun"},
                    {"german": "die CO2-Emission", "english": "CO2 emission", "turkish": "CO2 emisyonu", "pos": "noun"},
                    {"german": "die erneuerbare Energie", "english": "renewable energy", "turkish": "yenilenebilir enerji", "pos": "noun"},
                    {"german": "die Klimaneutralität", "english": "climate neutrality", "turkish": "iklim nötrlüğü", "pos": "noun"},
                    {"german": "der Meeresspiegel", "english": "sea level", "turkish": "deniz seviyesi", "pos": "noun"},
                    {"german": "die Hitzewelle", "english": "heatwave", "turkish": "sıcak hava dalgası", "pos": "noun"}
                ],
                "examTip": "Zahlen merken: +1,2°C seit Industrialisierung. Pariser Abkommen: 1,5-2°C Grenze. Deutschland: Klimaneutral bis 2045."
            },
            {
                "id": "b2_r_03_02", "title": "Erneuerbare Energien: Die Zukunft ist solar", "source": "Fraunhofer ISE",
                "sourceUrl": "https://www.ise.fraunhofer.de/", "wordCount": 320, "readingTimeMinutes": 5,
                "tags": ["Solarenergie", "Windkraft", "Energiewende"],
                "content": """Erneuerbare Energien sind auf dem Vormarsch. Im Jahr 2023 stammten in Deutschland erstmals mehr als 50 Prozent des Stroms aus erneuerbaren Quellen – vor allem aus Windkraft und Solarenergie. Das ist ein historischer Meilenstein auf dem Weg zur Klimaneutralität.

Die Solarenergie boomt besonders. Dank sinkender Modulkosten und verbesserter Technologie ist Photovoltaik heute die günstigste Form der Stromerzeugung überhaupt. Auch auf deutschen Dächern sieht man immer häufiger Solaranlagen – nicht nur auf Einfamilienhäusern, sondern auch auf Gewerbegebäuden und Parkplätzen.

Die Windkraft bleibt jedoch der wichtigste erneuerbare Energieträger in Deutschland. Onshore-Windkraftanlagen – also Windräder an Land – liefern den größten Anteil des Ökostroms. Offshore-Windparks in der Nord- und Ostsee ergänzen die Erzeugung, sind aber teurer und technisch anspruchsvoller.

Eine Herausforderung bleibt die Speicherung von Energie. Solar- und Windkraft liefern nicht rund um die Uhr Strom, sondern nur dann, wenn die Sonne scheint oder der Wind weht. Deshalb werden große Batteriespeicher und sogenannte Power-to-X-Technologien entwickelt, die überschüssigen Strom in Wasserstoff oder synthetische Kraftstoffe umwandeln.

Netzbetreiber stehen vor der Aufgabe, das Stromnetz fit für die Energiewende zu machen. Das bedeutet: mehr Verbindungsleitungen zwischen Nord- und Südeutschland, intelligente Netze, die Angebot und Nachfrage in Echtzeit steuern, und ein besserer Ausbau der Ladeinfrastruktur für Elektroautos.

Experten sind sich einig: Die Energiewende ist möglich, wenn der politische Wille da ist und die Investitionen weiter fließen. „Wir haben die Technologie", sagt Professor Volker Quaschning von der Hochschule für Technik und Wirtschaft. „Jetzt geht es um Geschwindigkeit.\"""",
                "questions": [
                    {"id": "q_03_02_a", "type": "multiple_choice", "questionText": "Wie viel Prozent des Stroms stammten 2023 in Deutschland aus erneuerbaren Quellen?", "options": ["Etwa 30 Prozent", "Mehr als 50 Prozent", "Etwa 20 Prozent", "Rund 80 Prozent"], "correctAnswer": "Mehr als 50 Prozent", "explanation": "Historischer Meilenstein: 'Im Jahr 2023 stammten in Deutschland erstmals mehr als 50 Prozent des Stroms aus erneuerbaren Quellen.'"},
                    {"id": "q_03_02_b", "type": "true_false", "questionText": "Solarenergie ist heute die teuerste Form der Stromerzeugung.", "correctAnswer": "false", "explanation": "Das Gegenteil ist wahr: 'Photovoltaik ist heute die günstigste Form der Stromerzeugung überhaupt.'"},
                    {"id": "q_03_02_c", "type": "multiple_choice", "questionText": "Was ist die größte Herausforderung bei Solar- und Windenergie?", "options": ["Zu teuer", "Zu laut", "Speicherung von Energie", "Zu gefährlich"], "correctAnswer": "Speicherung von Energie", "explanation": "'Eine Herausforderung bleibt die Speicherung von Energie. Solar- und Windkraft liefern nicht rund um die Uhr Strom...'"},
                    {"id": "q_03_02_d", "type": "fill_blank", "questionText": "Power-___-Technologien wandeln überschüssigen Strom in Wasserstoff um.", "correctAnswer": "to-X", "explanation": "Der Text erwähnt 'sogenannte Power-to-X-Technologien'"},
                    {"id": "q_03_02_e", "type": "multiple_choice", "questionText": "Was liefert den größten Anteil des Ökostroms in Deutschland?", "options": ["Solarenergie", "Wasserkraft", "Onshore-Windkraftanlagen", "Biomasse"], "correctAnswer": "Onshore-Windkraftanlagen", "explanation": "'Onshore-Windkraftanlagen – also Windräder an Land – liefern den größten Anteil des Ökostroms.'"}
                ],
                "keyVocabulary": [
                    {"german": "die Solarenergie", "english": "solar energy", "turkish": "güneş enerjisi", "pos": "noun"},
                    {"german": "die Windkraft", "english": "wind power", "turkish": "rüzgar enerjisi", "pos": "noun"},
                    {"german": "die Photovoltaik", "english": "photovoltaics", "turkish": "fotovoltaik", "pos": "noun"},
                    {"german": "der Ökostrom", "english": "green electricity", "turkish": "yeşil elektrik", "pos": "noun"},
                    {"german": "die Energiewende", "english": "energy transition", "turkish": "enerji dönüşümü", "pos": "noun"},
                    {"german": "der Batteriespeicher", "english": "battery storage", "turkish": "batarya depolama", "pos": "noun"},
                    {"german": "die Ladeinfrastruktur", "english": "charging infrastructure", "turkish": "şarj altyapısı", "pos": "noun"},
                    {"german": "der Wasserstoff", "english": "hydrogen", "turkish": "hidrojen", "pos": "noun"}
                ],
                "examTip": "Wichtige Trends: Solar wird günstiger, Windkraft liefert den meisten Ökostrom, Speicherung ist die Herausforderung!"
            },
            {
                "id": "b2_r_03_03", "title": "Mülltrennung in Deutschland", "source": "Grüner Punkt",
                "sourceUrl": "https://www.gruener-punkt.de/", "wordCount": 295, "readingTimeMinutes": 4,
                "tags": ["Mülltrennung", "Recycling", "Nachhaltigkeit"],
                "content": """Mülltrennung gehört in Deutschland zum Alltag wie kaum ein anderes Land. Das duale System, auch „Grüner Punkt" genannt, sorgt seit 1991 dafür, dass Verpackungen recycelt werden. Doch trotzdem landen noch immer zu viele Wertstoffe im Restmüll.

In Deutschland gibt es in der Regel fünf verschiedene Tonnen: Die Biotonne für organische Abfälle wie Essensreste und Gartenabfälle. Die Gelbe Tonne oder der Gelbe Sack für Verpackungen aus Plastik, Metall und Verbundstoffen. Die Papiertonne für Zeitungen, Kartons und ähnliches. Die Glastonne für Einmachgläser und Flaschen – getrennt nach Farbe. Und schließlich die graue oder schwarze Restmülltonne für alles, was nicht recyclebar ist.

Doch viele Menschen sind unsicher, was genau in welche Tonne gehört. „Verpackungen aus Styropor gehören nicht in die Gelbe Tonne, obwohl das viele denken", erklärt Maria Schneider, Sprecherin des Verbands der Deutschenviromentechnik. Styroporverpackungen werden in Deutschland bisher kaum recycelt und sollten in den Restmüll.

Besonders die Biotonne wird oft falsch befüllt. Kunststoffbeutel, selbst wenn sie biologisch abbaubar sind, gehören nicht hinein. Nur losere organische Abfälle oder Papierbeutel sind erlaubt. Der Bioabfall wird in Vergärungsanlagen zu Biogas und Kompost verarbeitet.

Experten raten: Weniger Müll produzieren ist besser als Müll trennen. „Die beste Verpackung ist die, die gar nicht erst entsteht", sagt Schneider. Unverpackt-Läden, Mehrwegflaschen und regionale Produkte helfen, den Müllberg zu reduzieren.""",
                "questions": [
                    {"id": "q_03_03_a", "type": "multiple_choice", "questionText": "Wie viele verschiedene Tonnen gibt es in Deutschland typischerweise?", "options": ["Drei", "Vier", "Fünf", "Sechs"], "correctAnswer": "Fünf", "explanation": "Der Text zählt auf: Biotonne, Gelbe Tonne, Papiertonne, Glastonne, Restmülltonne = 5 Tonnen."},
                    {"id": "q_03_03_b", "type": "true_false", "questionText": "Styroporverpackungen können in Deutschland problemlos recycelt werden.", "correctAnswer": "false", "explanation": "'Styroporverpackungen werden in Deutschland bisher kaum recycelt und sollten in den Restmüll.'"},
                    {"id": "q_03_03_c", "type": "multiple_choice", "questionText": "Was passiert mit dem Bioabfall?", "options": ["Er wird verbrannt", "Er wird zu Biogas und Kompost verarbeitet", "Er wird ins Meer geleitet", "Er wird gelagert"], "correctAnswer": "Er wird zu Biogas und Kompost verarbeitet", "explanation": "'Der Bioabfall wird in Vergärungsanlagen zu Biogas und Kompost verarbeitet.'"},
                    {"id": "q_03_03_d", "type": "fill_blank", "questionText": "Das duale System heißt umgangssprachlich auch '___ ___'.", "correctAnswer": "Grüner Punkt", "explanation": "Der Text erwähnt: 'Das duale System, auch „Grüner Punkt" genannt, sorgt seit 1991 dafür...'"},
                    {"id": "q_03_03_e", "type": "multiple_choice", "questionText": "Was ist laut Maria Schneider die beste Verpackung?", "options": ["Recycelbare Verpackung", "Biologisch abbaubare Verpackung", "Die Verpackung, die gar nicht erst entsteht", "Glasverpackung"], "correctAnswer": "Die Verpackung, die gar nicht erst entsteht", "explanation": "Direktes Zitat: '„Die beste Verpackung ist die, die gar nicht erst entsteht."'"}
                ],
                "keyVocabulary": [
                    {"german": "die Mülltrennung", "english": "waste separation", "turkish": "çöp ayrıştırma", "pos": "noun"},
                    {"german": "das Recycling", "english": "recycling", "turkish": "geri dönüşüm", "pos": "noun"},
                    {"german": "die Biotonne", "english": "organic waste bin", "turkish": "organik atık kutusu", "pos": "noun"},
                    {"german": "die Gelbe Tonne", "english": "yellow bin (packaging)", "turkish": "sarı atık kutusu (ambalaj)", "pos": "noun"},
                    {"german": "der Restmüll", "english": "residual waste", "turkish": "artan çöp", "pos": "noun"},
                    {"german": "der Kompost", "english": "compost", "turkish": "kompost", "pos": "noun"},
                    {"german": "das Biogas", "english": "biogas", "turkish": "biyogaz", "pos": "noun"},
                    {"german": "unverpackt", "english": "packaging-free", "turkish": "paketlemesiz", "pos": "adjective"}
                ],
                "examTip": "Mülltrennung ist ein klassisches B2-Alltagsthema. Merke: 5 Tonnen, Styropor = Restmüll, Bioabfall = Biogas!"
            },
            {
                "id": "b2_r_03_04", "title": "Artenschutz: Das Insektensterben stoppen", "source": "BUND",
                "sourceUrl": "https://www.bund.net/", "wordCount": 310, "readingTimeMinutes": 5,
                "tags": ["Artenschutz", "Insektensterben", "Biodiversität"],
                "content": """Die速度和Diversität der Insekten in Deutschland nimmt dramatisch ab. Studien zeigen, dass die Biomasse der Fluginsekten in den letzten 30 Jahren um mehr als 75 Prozent zurückgegangen ist. Das hat fatale Folgen für das gesamte Ökosystem.

Insekten sind nicht nur lästige „Krabbeltiere", sondern sie erfüllen lebenswichtige Funktionen: Sie bestäuben Pflanzen, zersetzen organische Abfälle und bilden die Nahrungsgrundlage für Vögel, Fische und andere Tiere. Ohne Insekten würde die Natur zusammenbrechen.

Die Ursachen für das Insektensterben sind vielfältig. An erster Stelle steht die industrielle Landwirtschaft mit ihrem massiven Einsatz von Pestiziden und Kunstdünger. Monokulturen bieten kaum Nahrung und Lebensraum für Insekten. Auch der Verlust von Blühflächen, Hecken und natürlichen Gewässern spielt eine große Rolle.

Städte und Gärten tragen ebenfalls zum Problem bei. Schottergärten statt Blumenwiesen, gemähte Rasenflächen und der Einsatz von Pestiziden in Privathaushalten reduzieren den Lebensraum zusätzlich.

Um gegenzusteuern, gibt es verschiedene Initiativen. Der „Insektenschutzbrief" der Bundesregierung sieht strengere Regeln für Pestizide und mehr Blühflächen vor. Naturschutzorganisationen wie der BUND rufen Bürger auf, Insektenhotels aufzustellen und in ihren Gärten auf Blühpflanzen zu setzen.

Auch die Landwirtschaft wird zum Umdenken aufgefordert. Ökologische Landwirtschaft, die auf Pestizide verzichtet, und die Förderung von Blühstreifen an Feldern können helfen, das Insektensterben zu stoppen.""",
                "questions": [
                    {"id": "q_03_04_a", "type": "multiple_choice", "questionText": "Um wie viel Prozent ist die Biomasse der Fluginsekten in 30 Jahren zurückgegangen?", "options": ["Etwa 25 Prozent", "Mehr als 75 Prozent", "Etwa 50 Prozent", "Weniger als 10 Prozent"], "correctAnswer": "Mehr als 75 Prozent", "explanation": "Studien zeigen: 'die Biomasse der Fluginsekten in den letzten 30 Jahren um mehr als 75 Prozent zurückgegangen'"},
                    {"id": "q_03_04_b", "type": "true_false", "questionText": "Ohne Insekten würde die Natur zusammenbrechen.", "correctAnswer": "true", "explanation": "'Ohne Insekten würde die Natur zusammenbrechen' – sie bestäuben, zersetzen und sind Nahrungsgrundlage."},
                    {"id": "q_03_04_c", "type": "multiple_choice", "questionText": "Was ist die HAUPTUrsache für das Insektensterben?", "options": ["Klimawandel", "Industrielle Landwirtschaft mit Pestiziden", "Zu viele Vögel", "Waldbrände"], "correctAnswer": "Industrielle Landwirtschaft mit Pestiziden", "explanation": "'An erster Stelle steht die industrielle Landwirtschaft mit ihrem massiven Einsatz von Pestiziden und Kunstdünger.'"},
                    {"id": "q_03_04_d", "type": "fill_blank", "questionText": "Monokulturen bieten kaum Nahrung und ___ für Insekten.", "correctAnswer": "Lebensraum", "explanation": "'Monokulturen bieten kaum Nahrung und Lebensraum für Insekten.'"},
                    {"id": "q_03_04_e", "type": "multiple_choice", "questionText": "Was können Privathaushalte laut dem Text für Insekten tun?", "options": ["Mehr Schottergärten anlegen", "Insektenhotels aufstellen und Blühpflanzen setzen", "Mehr Rasen mähen", "Pestizide verwenden"], "correctAnswer": "Insektenhotels aufstellen und Blühpflanzen setzen", "explanation": "'Naturschutzorganisationen... rufen Bürger auf, Insektenhotels aufzustellen und in ihren Gärten auf Blühpflanzen zu setzen.'"}
                ],
                "keyVocabulary": [
                    {"german": "das Insektensterben", "english": "insect extinction", "turkish": "böcek ölümü", "pos": "noun"},
                    {"german": "die Biodiversität", "english": "biodiversity", "turkish": "biyoçeşitlilik", "pos": "noun"},
                    {"german": "das Ökosystem", "english": "ecosystem", "turkish": "ecosystem", "pos": "noun"},
                    {"german": "die Bestäubung", "english": "pollination", "turkish": "tozlaşma", "pos": "noun"},
                    {"german": "das Pestizid", "english": "pesticide", "turkish": "zirai ilaç", "pos": "noun"},
                    {"german": "die Monokultur", "english": "monoculture", "turkish": "monokültür", "pos": "noun"},
                    {"german": "der Blühstreifen", "english": "flowering strip", "turkish": "çiçekli alan şeridi", "pos": "noun"},
                    {"german": "das Insektenhotel", "english": "insect hotel", "turkish": "böcek oteli", "pos": "noun"}
                ],
                "examTip": "75% Rückgang der Insektenbiomasse = alarmierend! Hauptursache: Pestizide + Monokultur. Lösungen: Insektenhotels, Blühpflanzen, Ökolandwirtschaft!"
            },
            {
                "id": "b2_r_03_05", "title": "Wasser sparen: Jeder Tropfen zählt", "source": "Umweltbundesamt",
                "sourceUrl": "https://www.umweltbundesamt.de/wasser", "wordCount": 280, "readingTimeMinutes": 4,
                "tags": ["Wassersparen", "Ressourcen", "Nachhaltigkeit"],
                "content": """Wasser ist kostbar – auch in Deutschland, wo es auf den ersten Blick genug davon gibt. Doch der Klimawandel verändert die Wasserverfügbarkeit: Heiße Sommer führen zu Trockenheit, Grundwasserpegel sinken, und manche Regionen kämpfen bereits mit Wasserknappheit.

Der durchschnittliche Wasserverbrauch in Deutschland liegt bei etwa 120 Litern pro Person und Tag. Das ist mehr als in vielen anderen europäischen Ländern. Zum Vergleich: In Dänemark liegt der Verbrauch bei nur 80 Litern, in Italien bei 170 Litern – dort ist es aber auch wärmer.

Die größten Wasserverbraucher im Haushalt sind Duschen und Baden (etwa 40 Liter), die Toilettenspülung (etwa 30 Liter) und der Wäschewaschen (etwa 20 Liter). Beim Gießen im Garten und beim Auto waschen kommt einiges dazu.

Einfache Maßnahmen helfen, Wasser zu sparen: Unterwegs Zähne putzen statt bei laufendem Wasser spart bis zu 10 Liter pro Putzen. Eine wassersparende Duschbrause verbraucht statt 15 nur 8 Liter pro Minute. Tropfende Wasserhähne sollten sofort repariert werden – ein tropfender Hahn verbraucht bis zu 5.000 Liter im Jahr.

Experten empfehlen auch, Regenwasser zu sammeln und für die Gartenbewässerung zu nutzen. Grauwasser – also leicht verschmutztes Wasser aus Dusche oder Waschbecken – kann für die Toilettenspülung wiederverwendet werden. So lässt sich der Wasserverbrauch um bis zu 30 Prozent senken.""",
                "questions": [
                    {"id": "q_03_05_a", "type": "multiple_choice", "questionText": "Wie hoch ist der durchschnittliche Wasserverbrauch in Deutschland pro Person und Tag?", "options": ["Etwa 60 Liter", "Etwa 120 Liter", "Etwa 200 Liter", "Etwa 50 Liter"], "correctAnswer": "Etwa 120 Liter", "explanation": "'Der durchschnittliche Wasserverbrauch in Deutschland liegt bei etwa 120 Litern pro Person und Tag.'"},
                    {"id": "q_03_05_b", "type": "true_false", "questionText": "In Dänemark ist der Wasserverbrauch höher als in Deutschland.", "correctAnswer": "false", "explanation": "'In Dänemark liegt der Verbrauch bei nur 80 Litern' – weniger als in Deutschland (120 Liter)."},
                    {"id": "q_03_05_c", "type": "multiple_choice", "questionText": "Was ist der größte Wasserverbraucher im Haushalt?", "options": ["Auto waschen", "Duschen und Baden", "Gartenarbeit", "Trinken"], "correctAnswer": "Duschen und Baden", "explanation": "'Die größten Wasserverbraucher im Haushalt sind Duschen und Baden (etwa 40 Liter)'"},
                    {"id": "q_03_05_d", "type": "fill_blank", "questionText": "Ein tropfender Wasserhahn kann bis zu ___ Liter Wasser im Jahr verbrauchen.", "correctAnswer": "5.000", "explanation": "'ein tropfender Hahn verbraucht bis zu 5.000 Liter im Jahr'"},
                    {"id": "q_03_05_e", "type": "multiple_choice", "questionText": "Um wie viel Prozent kann der Wasserverbrauch durch simple Maßnahmen gesenkt werden?", "options": ["Bis zu 10 Prozent", "Bis zu 30 Prozent", "Bis zu 60 Prozent", "Nur minimal"], "correctAnswer": "Bis zu 30 Prozent", "explanation": "'So lässt sich der Wasserverbrauch um bis zu 30 Prozent senken' durch Regenwasser und Grauwasser-Nutzung."}
                ],
                "keyVocabulary": [
                    {"german": "der Wasserverbrauch", "english": "water consumption", "turkish": "su tüketimi", "pos": "noun"},
                    {"german": "die Wasserknappheit", "english": "water scarcity", "turkish": "su kıtlığı", "pos": "noun"},
                    {"german": "das Grundwasser", "english": "groundwater", "turkish": "yeraltı suyu", "pos": "noun"},
                    {"german": "die Trockenheit", "english": "drought", "turkish": "kuraklık", "pos": "noun"},
                    {"german": "der tropfende Wasserhahn", "english": "dripping tap", "turkish": "sızdıran musluk", "pos": "noun"},
                    {"german": "das Regenwasser", "english": "rainwater", "turkish": "yağmur suyu", "pos": "noun"},
                    {"german": "Grauwasser", "english": "greywater", "turkish": "gri su (kullanılmış su)", "pos": "noun"},
                    {"german": "die Wassersparbrause", "english": "water-saving shower head", "turkish": "su tasarruflu duş başlığı", "pos": "noun"}
                ],
                "examTip": "Zahlen merken: 120 L/Tag in Deutschland, 80 L in Dänemark, 5.000 L durch tropfenden Hahn. Einsparpotenzial: bis 30%!"
            },
            {
                "id": "b2_r_03_06", "title": "E-Auto vs. Verbrenner: Die Debatte", "source": "Spiegel Online",
                "sourceUrl": "https://www.spiegel.de/auto/", "wordCount": 330, "readingTimeMinutes": 5,
                "tags": ["E-Mobilität", "Autoverkehr", "Klimaschutz"],
                "content": """Der Verbrennungsmotor hat in Deutschland 历史lich gesehen eine lange Tradition. Doch die Zeiten ändern sich: Ab 2035 dürfen in der EU keine Neuwagen mit Benzin- oder Dieselmotor mehr zugelassen werden. Die Frage ist nicht mehr OB, sondern WANN das E-Auto den Verbrenner ablöst.

Die Vorteile von Elektroautos sind klar: Sie fahren lokal emissionsfrei, sind leiser und haben einen deutlich höheren Wirkungsgrad. Während bei einem Verbrenner nur etwa 20 Prozent der Energie aus Benzin tatsächlich in Bewegung umgewandelt werden, sind es beim E-Auto etwa 80 Prozent.

Doch es gibt auch Kritikpunkte. Die Batterieproduktion ist ressourcenintensiv und erfordert seltene Erden und Lithium. Die Reichweite von E-Autos ist immer noch geringer als bei traditionellen Autos, und die Ladeinfrastruktur ist noch nicht flächendeckend. Zudem ist die CO2-Bilanz eines E-Autos nur dann wirklich gut, wenn der Strom aus erneuerbaren Quellen stammt.

 Befürworter der E-Mobilität betonen jedoch, dass sich die Technologie rasant weiterentwickelt. Die Reichweiten steigen, die Batteriekosten sinken, und das Laden wird immer schneller. Auch das Problem der Rohstoffe soll durch Recycling und neue Batterietechnologien gelöst werden.

Für den Klimaschutz ist der Umstieg auf Elektromobilität ein wichtiger Baustein – aber nicht die einzige Lösung. Fahrradfahren, öffentlicher Nahverkehr und Carsharing sind equally wichtig, um den Autoverkehr und damit die CO2-Emissionen insgesamt zu reduzieren.""",
                "questions": [
                    {"id": "q_03_06_a", "type": "multiple_choice", "questionText": "Ab wann dürfen in der EU keine Neuwagen mit Verbrennungsmotor mehr zugelassen werden?", "options": ["Ab 2025", "Ab 2030", "Ab 2035", "Ab 2040"], "correctAnswer": "Ab 2035", "explanation": "'Ab 2035 dürfen in der EU keine Neuwagen mit Benzin- oder Dieselmotor mehr zugelassen werden.'"},
                    {"id": "q_03_06_b", "type": "true_false", "questionText": "Der Wirkungsgrad eines E-Autos ist niedriger als das eines Verbrenners.", "correctAnswer": "false", "explanation": "'Während bei einem Verbrenner nur etwa 20 Prozent der Energie tatsächlich in Bewegung umgewandelt werden, sind es beim E-Auto etwa 80 Prozent.'"},
                    {"id": "q_03_06_c", "type": "multiple_choice", "questionText": "Was sind Kritikpunkte am E-Auto? (Zwei richtige Antworten)", "options": ["Zu leise", "Batterieproduktion ist ressourcenintensiv", "Zu teuer in der Wartung", "Reichweite noch geringer als bei Verbrennern", "Keine Lademöglichkeiten in Städten"], "correctAnswer": "Batterieproduktion ist ressourcenintensiv, Reichweite noch geringer als bei Verbrennern", "explanation": "Text nennt: ressourcenintensive Batterieproduktion und geringere Reichweite als Kritikpunkte."},
                    {"id": "q_03_06_d", "type": "fill_blank", "questionText": "Der ___ eines E-Autos liegt bei etwa 80 Prozent.", "correctAnswer": "Wirkungsgrad", "explanation": "'beim E-Auto etwa 80 Prozent' Wirkungsgrad im Vergleich zu 20% beim Verbrenner."},
                    {"id": "q_03_06_e", "type": "multiple_choice", "questionText": "Was ist neben E-Mobilität ebenfalls wichtig für den Klimaschutz?", "options": ["Mehr Autobahnen bauen", "Fahrradfahren, öffentlicher Nahverkehr und Carsharing", "Mehr Benzinautos produzieren", "Flugreisen fördern"], "correctAnswer": "Fahrradfahren, öffentlicher Nahverkehr und Carsharing", "explanation": "'Fahrradfahren, öffentlicher Nahverkehr und Carsharing sind equally wichtig, um den Autoverkehr und damit die CO2-Emissionen insgesamt zu reduzieren.'"}
                ],
                "keyVocabulary": [
                    {"german": "das Elektroauto / E-Auto", "english": "electric car", "turkish": "elektrikli araba", "pos": "noun"},
                    {"german": "der Verbrennungsmotor", "english": "combustion engine", "turkish": "içten yanmalı motor", "pos": "noun"},
                    {"german": "der Wirkungsgrad", "english": "efficiency", "turkish": "verimlilik", "pos": "noun"},
                    {"german": "die Reichweite", "english": "range", "turkish": "menzil / menfaat", "pos": "noun"},
                    {"german": "die Ladeinfrastruktur", "english": "charging infrastructure", "turkish": "şarj altyapısı", "pos": "noun"},
                    {"german": "die Batterie", "english": "battery", "turkish": "batarya", "pos": "noun"},
                    {"german": "die seltene Erden", "english": "rare earths", "turkish": "nadir toprak elementleri", "pos": "noun"},
                    {"german": "der Carsharing", "english": "car sharing", "turkish": "araç paylaşımı", "pos": "noun"}
                ],
                "examTip": "2035 = Ende für Verbrenner in der EU. E-Auto: 80% Wirkungsgrad vs. Verbrenner: 20%. E-Mobilität ist nicht die einzige Lösung – ÖPNV, Fahrrad, Carsharing zählen auch!"
            },
            {
                "id": "b2_r_03_07", "title": "Plastik in den Ozeanen: Eine tickende Zeitbombe", "source": "WWF",
                "sourceUrl": "https://www.wwf.de/", "wordCount": 305, "readingTimeMinutes": 4,
                "tags": ["Meeresverschmutzung", "Plastik", "Umweltschutz"],
                "content": """Jährlich gelangen etwa 8 Millionen Tonnen Plastik in die Weltmeere. Das entspricht einem Müllwagen, der jede Minute ins Meer gekippt wird. Dieses Plastik zerfällt in winzige Partikel, sogenannte Mikroplastik, das von Meerestieren gefressen wird und so in die Nahrungskette des Menschen gelangt.

Besonders betroffen ist der sogenannte Great Pacific Garbage Patch – ein riesiger Plastikteppich im Pazifik, der mittlerweile größer ist als ganz Mitteleuropa. Aber auch in der Nordsee und in deutschen Flüssen findet sich zunehmend Plastikmüll.

Die Folgen für die Tierwelt sind verheerend. Meeresschildkröten verwechseln Plastiktüten mit Quallen und ersticken. Seevögel sterben an Plastikteilen in ihrem Magen. Fische nehmen Mikroplastik über ihre Nahrung auf. Schätzungen zufolge haben 90 Prozent aller Seevögel bereits Plastik in ihrem Verdauungssystem.

Doch es gibt auch Hoffnung. Internationale Abkommen wie das „Basler Übereinkommen\" und die EU-Richtlinie gegen Plastikeinwegprodukte sind wichtige Schritte. In Deutschland sind seit 2021 bestimmte Einwegplastikprodukte wie Strohhalme und Einwegbesteck verboten.

Auf individueller Ebene können Verbraucher viel tun: Mehrwegflaschen verwenden, auf Mikroplastik in Kosmetikprodukten achten, und beim Einkauf auf unverpackte Produkte zurückgreifen. Jede Maßnahme zählt – denn die Ozeane sind das Lebenselixier unseres Planeten.""",
                "questions": [
                    {"id": "q_03_07_a", "type": "multiple_choice", "questionText": "Wie viel Plastik gelangt jährlich in die Weltmeere?", "options": ["Etwa 500.000 Tonnen", "Etwa 2 Millionen Tonnen", "Etwa 8 Millionen Tonnen", "Etwa 20 Millionen Tonnen"], "correctAnswer": "Etwa 8 Millionen Tonnen", "explanation": "'Jährlich gelangen etwa 8 Millionen Tonnen Plastik in die Weltmeere.'"},
                    {"id": "q_03_07_b", "type": "true_false", "questionText": "Mikroplastik kann über die Nahrungskette in den Menschen gelangen.", "correctAnswer": "true", "explanation": "'Mikroplastik... wird von Meerestieren gefressen und so in die Nahrungskette des Menschen gelangt.'"},
                    {"id": "q_03_07_c", "type": "multiple_choice", "questionText": "Was ist der Great Pacific Garbage Patch?", "options": ["Ein Meeresnationalpark", "Ein riesiger Plastikteppich im Pazifik", "Eine Reinigungsanlage", "Ein Fischarten-Schutzgebiet"], "correctAnswer": "Ein riesiger Plastikteppich im Pazifik", "explanation": "'ein riesiger Plastikteppich im Pazifik, der mittlerweile größer ist als ganz Mitteleuropa'"},
                    {"id": "q_03_07_d", "type": "fill_blank", "questionText": "Seit 2021 sind in Deutschland bestimmte Einwegplastikprodukte wie ___ und Einwegbesteck verboten.", "correctAnswer": "Strohhalme", "explanation": "'In Deutschland sind seit 2021 bestimmte Einwegplastikprodukte wie Strohhalme und Einwegbesteck verboten.'"},
                    {"id": "q_03_07_e", "type": "multiple_choice", "questionText": "Wie viel Prozent aller Seevögel haben laut Schätzungen Plastik im Verdauungssystem?", "options": ["Etwa 30 Prozent", "Etwa 60 Prozent", "Etwa 90 Prozent", "Etwa 10 Prozent"], "correctAnswer": "Etwa 90 Prozent", "explanation": "'Schätzungen zufolge haben 90 Prozent aller Seevögel bereits Plastik in ihrem Verdauungssystem.'"}
                ],
                "keyVocabulary": [
                    {"german": "die Meeresverschmutzung", "english": "ocean pollution", "turkish": "deniz kirliliği", "pos": "noun"},
                    {"german": "das Mikroplastik", "english": "microplastic", "turkish": "mikroplastik", "pos": "noun"},
                    {"german": "die Nahrungskette", "english": "food chain", "turkish": "besin zinciri", "pos": "noun"},
                    {"german": "der Plastikteppich", "english": "plastic patch", "turkish": "plastik örtüsü", "pos": "noun"},
                    {"german": "das Meerestier", "english": "marine animal", "turkish": "deniz canlısı", "pos": "noun"},
                    {"german": "die Meeresschildkröte", "english": "sea turtle", "turkish": "deniz kaplumbağası", "pos": "noun"},
                    {"german": "das Einwegplastik", "english": "single-use plastic", "turkish": "tek kullanımlık plastik", "pos": "noun"},
                    {"german": "der Seevogel", "english": "seabird", "turkish": "deniz kuşu", "pos": "noun"}
                ],
                "examTip": "8 Mio Tonnen Plastik pro Jahr ins Meer. 90% der Seevögel haben Plastik im Magen. Great Pacific Garbage Patch > Mitteleuropa! Lösungen: Mehrweg, unverpackt, EU-Verbote!"
            },
            {
                "id": "b2_r_03_08", "title": "Nachhaltigkeit im Alltag: Kleine Schritte, große Wirkung", "source": "Stiftung Warentest",
                "sourceUrl": "https://www.stiftung-warentest.de/", "wordCount": 290, "readingTimeMinutes": 4,
                "tags": ["Nachhaltigkeit", "Alltag", "Umweltschutz"],
                "content": """Nachhaltigkeit ist längst kein Nischenthema mehr. Immer mehr Menschen fragen sich, wie sie im Alltag umweltbewusster leben können. Doch oft fehlt das Wissen, wo man anfangen soll. Die gute Nachricht: Schon kleine Veränderungen können einen großen Unterschied machen.

Beim Einkaufen lohnt es sich, saisonales und regionales Obst und Gemüse zu wählen. Tomaten aus Spanien im deutschen Winter haben eine schlechte CO2-Bilanz, während Äpfel aus der Region im Herbst kaum Transportwege haben. Auch Bio-Produkte schneiden in der Regel ökologisch besser ab, sind aber oft teurer.

Beim Heizen lässt sich viel Energie sparen. Jedes Grad weniger Raumtemperatur spart etwa sechs Prozent Heizkosten. Eine仆 Programmierbare Heizungssteuerung kann den Energieverbrauch zusätzlich senken. Auch Dämmung von Fenstern und Türen ist eine langfristige Investition, die sich auszahlt.

Beim Einkauf von Kleidung ist Fast Fashion ein Problem. Mode, die zu sehr niedrigen Preisen angeboten wird, ist oft von schlechter Qualität und wird nach wenigen Tragen weggeworfen. Qualitätskleidung, die länger hält, ist nachhaltiger – auch wenn sie anfangs teurer ist.

Schließlich ist auch die Ernährung ein wichtiger Hebel. Eine ausgewogene, pflanzenbasierte Ernährung mit weniger Fleisch ist nicht nur gesünder, sondern reduziert auch den ökologischen Fußabdruck. „Jeder kann etwas tun", sagt Umweltpsychologin Dr. Katharina Schultz. „Es geht nicht darum, perfekt zu sein, sondern bewusster zu handeln.\"""",
                "questions": [
                    {"id": "q_03_08_a", "type": "multiple_choice", "questionText": "Was kann man beim Heizen tun, um Energie zu sparen?", "options": ["Heizung immer auf Maximum stellen", "Jedes Grad weniger spart etwa sechs Prozent Heizkosten", "Fenster offen lassen", "Nur abends heizen"], "correctAnswer": "Jedes Grad weniger spart etwa sechs Prozent Heizkosten", "explanation": "'Jedes Grad weniger Raumtemperatur spart etwa sechs Prozent Heizkosten.'"},
                    {"id": "q_03_08_b", "type": "true_false", "questionText": "Tomaten aus Spanien haben im deutschen Winter eine gute CO2-Bilanz.", "correctAnswer": "false", "explanation": "'Tomaten aus Spanien im deutschen Winter haben eine schlechte CO2-Bilanz' wegen der langen Transportwege."},
                    {"id": "q_03_08_c", "type": "multiple_choice", "questionText": "Was ist Fast Fashion?", "options": ["Qualitätskleidung für Sport", "Günstige Mode in schlechter Qualität, die schnell weggeworfen wird", "Wintermode", "Secondhand-Kleidung"], "correctAnswer": "Günstige Mode in schlechter Qualität, die schnell weggeworfen wird", "explanation": "'Mode, die zu sehr niedrigen Preisen angeboten wird, ist oft von schlechter Qualität und wird nach wenigen Tragen weggeworfen.'"},
                    {"id": "q_03_08_d", "type": "fill_blank", "questionText": "Eine ausgewogene, pflanzenbasierte Ernährung mit weniger Fleisch reduziert den ökologischen ___.", "correctAnswer": "Fußabdruck", "explanation": "'reduziert auch den ökologischen Fußabdruck' – sog. ökologischer Fußabdruck misst Umweltauswirkung."},
                    {"id": "q_03_08_e", "type": "multiple_choice", "questionText": "Was empfiehlt Dr. Katharina Schultz?", "options": ["Perfekt sein müssen", "Bewusster handeln, nicht perfekt sein", "Nur theoretisch über Nachhaltigkeit nachdenken", "Auf alles verzichten"], "correctAnswer": "Bewusster handeln, nicht perfekt sein", "explanation": "Direktes Zitat: 'Es geht nicht darum, perfekt zu sein, sondern bewusster zu handeln.'"}
                ],
                "keyVocabulary": [
                    {"german": "die Nachhaltigkeit", "english": "sustainability", "turkish": "sürdürülebilirlik", "pos": "noun"},
                    {"german": "saisonal", "english": "seasonal", "turkish": "mevsimsel", "pos": "adjective"},
                    {"german": "regional", "english": "regional / local", "turkish": "yerel / bölgesel", "pos": "adjective"},
                    {"german": "die Dämmung", "english": "insulation", "turkish": "yalıtım", "pos": "noun"},
                    {"german": "der ökologische Fußabdruck", "english": "ecological footprint", "turkish": "ekolojik ayak izi", "pos": "noun"},
                    {"german": "Fast Fashion", "english": "fast fashion", "turkish": "hızlı moda", "pos": "noun"},
                    {"german": "pflanzenbasiert", "english": "plant-based", "turkish": "bitki bazlı", "pos": "adjective"},
                    {"german": "das Heizkosten", "english": "heating costs", "turkish": "ısınma masrafları", "pos": "noun"}
                ],
                "examTip": "Jedes Grad weniger = 6% Heizkosten sparen! Saisonal + regional essen. Fast Fashion = Umweltproblem. Bewusstsein wichtiger als Perfektion!"
            },
            {
                "id": "b2_r_03_09", "title": "Waldsterben: Der Klimawandel bedroht unsere Wälder", "source": "Bundeswaldinventur",
                "sourceUrl": "https://www.bundeswaldinventur.de/", "wordCount": 310, "readingTimeMinutes": 5,
                "tags": ["Wälder", "Klimawandel", "Naturschutz"],
                "content": """Deutschlands Wälder leiden unter dem Klimawandel. Dürresommer, Stürme und Borkenkäferbefall haben in den letzten Jahren zu massiven Waldschäden geführt. Etwa 180.000 Hektar Wald – das entspricht der Fläche von Saarland – sind in den letzten fünf Jahren verloren gegangen.

Der Wald erfüllt lebenswichtige Funktionen: Er filtert die Luft, speichert CO2, produziert Sauerstoff und ist Lebensraum für unzählige Tier- und Pflanzenarten. Ein gesunder Wald kann nur dann funktionieren, wenn er ausreichend Wasser bekommt. Doch die zunehmenden Dürreperioden setzen unseren Wäldern stark zu.

Besonders betroffen sind die Fichtenwälder. Sie machen etwa ein Viertel der deutschen Waldfläche aus und sind besonders anfällig für Trockenheit und Borkenkäfer. Der Borkenkäfer vermehrt sich bei warmen Temperaturen explosionsartig und kann ganze Wälder zerstören.

Die Forstwirtschaft reagiert mit der Pflanzung klimaresilienterer Baumarten. Nicht mehr nur Fichten und Kiefern, sondern vermehrt Buchen, Eichen und Douglasien werden angepflanzt. Diese Arten kommen besser mit trockenen Bedingungen zurecht.

Auch Bürger können helfen: Das Pflanzen von Bäumen über Initiativen wie „Plant for the Planet\" oder die Waldjugend ist eine Möglichkeit, den Wald zu unterstützen. Wichtig ist auch, bestehende Wälder nicht unnötig zu betreten und Müll zu vermeiden. Denn jeder gepflanzte Baum zählt – im Kampf gegen den Klimawandel.""",
                "questions": [
                    {"id": "q_03_09_a", "type": "multiple_choice", "questionText": "Wie viel Waldfläche ist in den letzten fünf Jahren verloren gegangen?", "options = ["Etwa 10.000 Hektar", "Etwa 180.000 Hektar (Fläche von Saarland)", "Etwa 1 Million Hektar", "Nur wenige Hektar"], "correctAnswer": "Etwa 180.000 Hektar (Fläche von Saarland)", "explanation": "'Etwa 180.000 Hektar Wald – das entspricht der Fläche von Saarland – sind in den letzten fünf Jahren verloren gegangen.'"},
                    {"id": "q_03_09_b", "type": "true_false", "questionText": "Der Borkenkäfer vermehrt sich bei kalten Temperaturen explosionsartig.", "correctAnswer": "false", "explanation": "'Der Borkenkäfer vermehrt sich bei warmen Temperaturen explosionsartig' – nicht bei kalten."},
                    {"id": "q_03_09_c", "type": "multiple_choice", "questionText": "Welche Baumart ist laut dem Text besonders anfällig für Trockenheit?", "options": ["Eiche", "Buche", "Fichte", "Douglasie"], "correctAnswer": "Fichte", "explanation": "'Besonders betroffen sind die Fichtenwälder... besonders anfällig für Trockenheit und Borkenkäfer.'"},
                    {"id": "q_03_09_d", "type": "fill_blank", "questionText": "Die Forstwirtschaft reagiert mit der Pflanzung klimaresilienterer ___arten.", "correctAnswer": "Baum", "explanation": "'Die Forstwirtschaft reagiert mit der Pflanzung klimaresilienterer Baumarten. Nicht mehr nur Fichten... sondern vermehrt Buchen, Eichen und Douglasien.'"},
                    {"id": "q_03_09_e", "type": "multiple_choice", "questionText": "Welche Funktionen erfüllt der Wald? (Zwei Antworten)", "options": ["CO2 speichern", "Sauerstoff produzieren", "Müll entsorgen", "Verkehr regeln", "Häuser bauen"], "correctAnswer": "CO2 speichern, Sauerstoff produzieren", "explanation": "'Er filtert die Luft, speichert CO2, produziert Sauerstoff und ist Lebensraum für unzählige Tier- und Pflanzenarten.'"}
                ],
                "keyVocabulary": [
                    {"german": "das Waldsterben", "english": "forest dieback", "turkish": "orman ölümü", "pos": "noun"},
                    {"german": "der Borkenkäfer", "english": "bark beetle", "turkish": "kabuk böceği", "pos": "noun"},
                    {"german": "die Dürreperiode", "english": "drought period", "turkish": "kuraklık dönemi", "pos": "noun"},
                    {"german": "die Fichte", "english": "spruce", "turkish": "ladin ağacı", "pos": "noun"},
                    {"german": "klimaresilient", "english": "climate-resilient", "turkish": "iklime dayanıklı", "pos": "adjective"},
                    {"german": "die CO2-Speicherung", "english": "CO2 storage", "turkish": "CO2 depolama", "pos": "noun"},
                    {"german": "die Forstwirtschaft", "english": "forestry", "turkish": "orman işletmeciliği", "pos": "noun"},
                    {"german": "die Baumart", "english": "tree species", "turkish": "ağaç türü", "pos": "noun"}
                ],
                "examTip": "180.000 Hektar verloren = Fläche von Saarland! Fichten = besonders anfällig. Borkenkäfer liebt Wärme. Zukunft: Buchen, Eichen, Douglasien pflanzen!"
            },
            {
                "id": "b2_r_03_10", "title": "Atomkraft: Ausstieg und die Folgen", "source": "Tagesschau",
                "sourceUrl": "https://www.tagesschau.de/atomkraft/",
                "wordCount": 315, "readingTimeMinutes": 5,
                "tags": ["Atomkraft", "Energie", "Klimapolitik"],
                "content": """Deutschland hat 2023 den Ausstieg aus der Atomkraft abgeschlossen. Die letzten drei Kernkraftwerke – Isar 2, Neckarwestheim 2 und Emsland – wurden vom Netz genommen. Damit ist Deutschland das erste große Industrieland, das vollständig auf Kernenergie verzichtet.

Befürworter der Kernkraft sehen darin einen Fehler. Sie argumentieren, dass Atomkraft CO2-frei sei und damit dem Klimaschutz diene. Bei der Stromerzeugung entstehen keine Treibhausgase – im Gegensatz zu Kohle oder Gas. Zudem sei Kernkraft rund um die Uhr verfügbar, also grundlastfähig, und nicht von Wind oder Sonne abhängig.

Kritiker der Kernkraft betonen jedoch die Risiken: Die Nahrung von Tschernobyl und Fukushima ist noch heute allgegenwärtig. Atommüll bleibt Jahrtausende lang gefährlich und muss sicher gelagert werden. In Deutschland gibt es bisher kein Endlager für hochradioaktiven Müll. Auch die Kosten für Rückbau und Entsorgung sind enorm.

Mit dem Atomausstieg ist die Diskussion jedoch nicht beendet. In vielen europäischen Ländern – darunter Frankreich, Großbritannien und Polen – wird über den Bau neuer Kernkraftwerke nachgedacht oder bereits gebaut. Diese Länder sehen in der Kernkraft eine CO2-arme Brückentechnologie.

Für Deutschland bleibt die Herausforderung bestehen: Wie kann die Stromversorgung gesichert werden, wenn weder Kernkraft noch Kohlestrom zur Verfügung stehen? Die Antwort liegt in einem schnelleren Ausbau erneuerbarer Energien, besserer Speichertechnologie und einem europäischen Stromverbund.""",
                "questions": [
                    {"id": "q_03_10_a", "type": "multiple_choice", "questionText": "Welche drei Kernkraftwerke wurden als letzte in Deutschland abgeschaltet?", "options": ["Isar 1, Neckarwestheim 1, Emsland", "Isar 2, Neckarwestheim 2, Emsland", "Fukushima, Tschernobyl, Brokdorf", "Alle gleichzeitig"], "correctAnswer": "Isar 2, Neckarwestheim 2, Emsland", "explanation": "'Die letzten drei Kernkraftwerke – Isar 2, Neckarwestheim 2 und Emsland – wurden vom Netz genommen.'"},
                    {"id": "q_03_10_b", "type": "true_false", "questionText": "Bei der Stromerzeugung durch Kernkraft entstehen Treibhausgase.", "correctAnswer": "false", "explanation": "'Bei der Stromerzeugung entstehen keine Treibhausgase – im Gegensatz zu Kohle oder Gas.'"},
                    {"id": "q_03_10_c", "type": "multiple_choice", "questionText": "Was ist ein Hauptkritikpunkt der Kernkraftgegner?", "options": ["Zu teuer im Bau", "Atommüll bleibt Jahrhunderte gefährlich und es gibt kein Endlager in Deutschland", "Zu leise", "Strom fällt zu oft aus"], "correctAnswer": "Atommüll bleibt Jahrhunderte gefährlich und es gibt kein Endlager in Deutschland", "explanation": "'Atommüll bleibt Jahrtausende lang gefährlich und muss sicher gelagert werden. In Deutschland gibt es bisher kein Endlager.'"},
                    {"id": "q_03_10_d", "type": "fill_blank", "questionText": "Frankreich, Großbritannien und Polen sehen in der Kernkraft eine CO2-arme ___.", "correctAnswer": "Brückentechnologie", "explanation": "'Diese Länder sehen in der Kernkraft eine CO2-arme Brückentechnologie.'"},
                    {"id": "q_03_10_e", "type": "multiple_choice", "questionText": "Was ist Deutschland laut dem Text in Bezug auf Atomausstieg?", "options": ["Das zweite große Industrieland", "Das erste große Industrieland ohne Atomkraft", "Das einzige Land weltweit", "Gar kein Industrieland"], "correctAnswer": "Das erste große Industrieland ohne Atomkraft", "explanation": "'Deutschland ist das erste große Industrieland, das vollständig auf Kernenergie verzichtet.'"}
                ],
                "keyVocabulary": [
                    {"german": "die Atomkraft", "english": "nuclear power", "turkish": "nükleer enerji", "pos": "noun"},
                    {"german": "der Atomausstieg", "english": "nuclear phase-out", "turkish": "nükleer enerjiden çıkış", "pos": "noun"},
                    {"german": "der Atommüll", "english": "nuclear waste", "turkish": "nükleer atık", "pos": "noun"},
                    {"german": "das Endlager", "english": "final repository", "turkish": "kalıcı depolama alanı", "pos": "noun"},
                    {"german": "grundlastfähig", "english": "baseload-capable", "turkish": "temel yük kapasiteli", "pos": "adjective"},
                    {"german": "die Brückentechnologie", "english": "bridge technology", "turkish": "köprü teknolojisi", "pos": "noun"},
                    {"german": "der Rückbau", "english": "decommissioning", "turkish": "söküm / imha", "pos": "noun"},
                    {"german": "der Stromverbund", "english": "power grid interconnection", "turkish": "elektrik şebeke bağlantısı", "pos": "noun"}
                ],
                "examTip": "Atomausstieg 2023: Isar 2, Neckarwestheim 2, Emsland = die letzten 3! Vorteil: CO2-frei. Nachteil: Atommüll-Jahrtausende. Debatte weiterhin in Europa!"
            }
        ]
    }
}

def generate_topic_json(topic_id: str, count: int = 10) -> dict:
    """Generate JSON for a specific topic's readings."""
    if topic_id not in TOPICS:
        return {"error": f"Topic {topic_id} not found. Available: {list(TOPICS.keys())}"}
    
    topic = TOPICS[topic_id]
    readings = topic["texts"][:count]
    
    return {
        "topic": {
            "id": topic_id,
            "name": topic["name"],
            "nameEn": topic["nameEn"],
            "iconEmoji": topic["iconEmoji"],
            "textCount": len(readings),
            "questionCount": len(readings) * 5
        },
        "readings": readings
    }

def export_for_firebase(topic_id: str) -> str:
    """Export topic readings as Firestore-compatible JSON."""
    data = generate_topic_json(topic_id)
    return json.dumps(data, indent=2, ensure_ascii=False)

def export_all_topics() -> str:
    """Export all topics as one large JSON file."""
    all_readings = []
    topics_list = []
    
    for topic_id, topic_data in TOPICS.items():
        topics_list.append({
            "id": topic_id,
            "name": topic_data["name"],
            "nameEn": topic_data["nameEn"],
            "iconEmoji": topic_data["iconEmoji"]
        })
        all_readings.extend(topic_data["texts"])
    
    return json.dumps({
        "topics": topics_list,
        "readings": all_readings
    }, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="B2 Reading Content Generator")
    parser.add_argument("--topic", type=str, help="Topic ID (e.g., b2_reading_03)")
    parser.add_argument("--count", type=int, default=10, help="Number of texts to generate")
    parser.add_argument("--export", type=str, help="Export to file")
    parser.add_argument("--export-all", action="store_true", help="Export all topics")
    
    args = parser.parse_args()
    
    if args.export_all:
        content = export_all_topics()
        filename = args.export or "b2_reading_ALL_topics.json"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Exported all topics to {filename}")
    
    elif args.topic:
        content = export_for_firebase(args.topic)
        filename = args.export or f"{args.topic}.json"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Exported {args.topic} to {filename}")
    
    else:
        print("Available topics:")
        for tid, tdata in TOPICS.items():
            print(f"  {tid}: {tdata['name']} ({len(tdata['texts'])} texts)")
