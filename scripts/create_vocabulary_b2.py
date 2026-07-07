# -*- coding: utf-8 -*-
"""
Creates initial B2 vocabulary content (Epic 6 / VOCAB-001..007), organized by
the same 9 theme categories already established in Firestore's `themes`
collection (beruf, bildung, geschichte, gesellschaft, gesundheit, medien,
reisen, umwelt, wirtschaft) and used for B2 reading topics.

Output: content/vocabulary/{category}.json, one file per category, matching
the VocabularyWord Kotlin data class field names exactly (so a straight sync
to Firestore's `vocabulary` collection round-trips through
FirebaseDataSource.getVocabularyByCategory -> snapshot.toObjects(VocabularyWord::class.java)
without any field renaming).

isLearned/reviewCount/lastReviewed are per-user progress, not content - they
are always overwritten locally by VocabularyProgressStore at read time and
must never be treated as authoritative here; left at their defaults.
"""
import json
import os

def word(id, german, english, turkish, pos, example, category):
    return {
        "id": id,
        "level": "B2",
        "german": german,
        "english": english,
        "turkish": turkish,
        "partOfSpeech": pos,
        "exampleSentence": example,
        "category": category,
        "audioUrl": "",
        "isLearned": False,
        "reviewCount": 0,
        "lastReviewed": 0
    }

VOCAB = {}

VOCAB["beruf"] = [
    word("vocab_beruf_01", "die Bewerbung", "job application", "iş başvurusu", "noun", "Ich habe meine Bewerbung gestern abgeschickt.", "beruf"),
    word("vocab_beruf_02", "der Lebenslauf", "resume/CV", "özgeçmiş", "noun", "Ein guter Lebenslauf sollte übersichtlich sein.", "beruf"),
    word("vocab_beruf_03", "das Vorstellungsgespräch", "job interview", "iş görüşmesi", "noun", "Das Vorstellungsgespräch dauerte eine Stunde.", "beruf"),
    word("vocab_beruf_04", "die Arbeitslosigkeit", "unemployment", "işsizlik", "noun", "Die Arbeitslosigkeit ist in dieser Region gestiegen.", "beruf"),
    word("vocab_beruf_05", "die Kündigung", "termination/notice", "işten çıkarma", "noun", "Er hat die Kündigung völlig unerwartet erhalten.", "beruf"),
    word("vocab_beruf_06", "die Gehaltserhöhung", "pay raise", "maaş artışı", "noun", "Nach zwei Jahren bat sie um eine Gehaltserhöhung.", "beruf"),
    word("vocab_beruf_07", "befördern", "to promote", "terfi ettirmek", "verb", "Man hat ihn zum Abteilungsleiter befördert.", "beruf"),
    word("vocab_beruf_08", "die Weiterbildung", "further training", "mesleki gelişim", "noun", "Weiterbildung ist in vielen Berufen unverzichtbar.", "beruf"),
    word("vocab_beruf_09", "das Betriebsklima", "workplace atmosphere", "işyeri ortamı", "noun", "Das Betriebsklima hat sich seit dem Chefwechsel verbessert.", "beruf"),
    word("vocab_beruf_10", "die Karrierechance", "career opportunity", "kariyer fırsatı", "noun", "Diese Stelle bietet gute Karrierechancen.", "beruf"),
    word("vocab_beruf_11", "der Arbeitsvertrag", "employment contract", "iş sözleşmesi", "noun", "Bitte lesen Sie den Arbeitsvertrag sorgfältig durch.", "beruf"),
    word("vocab_beruf_12", "die Selbstständigkeit", "self-employment", "serbest çalışma", "noun", "Nach der Kündigung wagte sie den Schritt in die Selbstständigkeit.", "beruf")
]

VOCAB["bildung"] = [
    word("vocab_bildung_01", "das Stipendium", "scholarship", "burs", "noun", "Sie hat ein Stipendium für ihr Auslandsstudium bekommen.", "bildung"),
    word("vocab_bildung_02", "die Hochschule", "university/college", "yükseköğretim kurumu", "noun", "An dieser Hochschule kann man Ingenieurwesen studieren.", "bildung"),
    word("vocab_bildung_03", "die Weiterbildungsmaßnahme", "professional development measure", "mesleki gelişim önlemi", "noun", "Die Firma bietet regelmäßige Weiterbildungsmaßnahmen an.", "bildung"),
    word("vocab_bildung_04", "lebenslanges Lernen", "lifelong learning", "yaşam boyu öğrenme", "phrase", "Lebenslanges Lernen wird in der modernen Arbeitswelt immer wichtiger.", "bildung"),
    word("vocab_bildung_05", "das Schulsystem", "school system", "eğitim sistemi", "noun", "Das deutsche Schulsystem unterscheidet sich stark von anderen Ländern.", "bildung"),
    word("vocab_bildung_06", "die Chancengleichheit", "equal opportunity", "fırsat eşitliği", "noun", "Chancengleichheit im Bildungssystem ist ein wichtiges politisches Ziel.", "bildung"),
    word("vocab_bildung_07", "vermitteln", "to convey/teach", "aktarmak", "verb", "Der Lehrer vermittelt den Schülern grundlegende Kenntnisse.", "bildung"),
    word("vocab_bildung_08", "der Abschluss", "degree/qualification", "diploma/mezuniyet", "noun", "Sie hat ihren Abschluss mit Auszeichnung gemacht.", "bildung"),
    word("vocab_bildung_09", "die Pflichtschule", "compulsory school", "zorunlu eğitim okulu", "noun", "Die Pflichtschule dauert in vielen Ländern neun Jahre.", "bildung"),
    word("vocab_bildung_10", "das Fachwissen", "expertise/specialized knowledge", "uzmanlık bilgisi", "noun", "Für diese Stelle wird umfangreiches Fachwissen vorausgesetzt.", "bildung"),
    word("vocab_bildung_11", "die Prüfungsangst", "exam anxiety", "sınav kaygısı", "noun", "Viele Studierende leiden unter Prüfungsangst.", "bildung"),
    word("vocab_bildung_12", "sich weiterbilden", "to further one's education", "kendini geliştirmek", "verb", "Er bildet sich regelmäßig in seinem Fachgebiet weiter.", "bildung")
]

VOCAB["geschichte"] = [
    word("vocab_geschichte_01", "das Kulturerbe", "cultural heritage", "kültürel miras", "noun", "Die Altstadt gehört zum UNESCO-Kulturerbe.", "geschichte"),
    word("vocab_geschichte_02", "die Tradition", "tradition", "gelenek", "noun", "Diese Tradition wird seit Jahrhunderten gepflegt.", "geschichte"),
    word("vocab_geschichte_03", "der Wiederaufbau", "reconstruction", "yeniden inşa", "noun", "Der Wiederaufbau der Stadt dauerte viele Jahre.", "geschichte"),
    word("vocab_geschichte_04", "die Vielfalt", "diversity", "çeşitlilik", "noun", "Die kulturelle Vielfalt macht die Stadt besonders lebendig.", "geschichte"),
    word("vocab_geschichte_05", "das Denkmal", "monument", "anıt", "noun", "Vor dem Rathaus steht ein historisches Denkmal.", "geschichte"),
    word("vocab_geschichte_06", "prägen", "to shape/influence", "şekillendirmek", "verb", "Dieses Ereignis hat die ganze Generation geprägt.", "geschichte"),
    word("vocab_geschichte_07", "die Epoche", "era/epoch", "çağ/dönem", "noun", "Die Romantik war eine bedeutende kulturelle Epoche.", "geschichte"),
    word("vocab_geschichte_08", "das Erbe", "heritage/legacy", "miras", "noun", "Sie bewahrt das Erbe ihrer Großeltern mit Stolz.", "geschichte"),
    word("vocab_geschichte_09", "die Integration", "integration", "entegrasyon", "noun", "Die Integration von Einwanderern braucht Zeit und Geduld.", "geschichte"),
    word("vocab_geschichte_10", "der Brauch", "custom", "gelenek/adet", "noun", "Dieser Brauch wird nur in ländlichen Regionen gefeiert.", "geschichte"),
    word("vocab_geschichte_11", "überliefern", "to hand down/pass on", "aktarmak/nakletmek", "verb", "Diese Geschichte wurde mündlich von Generation zu Generation überliefert.", "geschichte"),
    word("vocab_geschichte_12", "die Errungenschaft", "achievement", "başarı/kazanım", "noun", "Die Demokratie gilt als große Errungenschaft der Geschichte.", "geschichte")
]

VOCAB["gesellschaft"] = [
    word("vocab_gesellschaft_01", "die Demografie", "demography", "demografi", "noun", "Die Demografie Deutschlands verändert sich durch die alternde Bevölkerung.", "gesellschaft"),
    word("vocab_gesellschaft_02", "die soziale Gerechtigkeit", "social justice", "sosyal adalet", "phrase", "Soziale Gerechtigkeit ist ein zentrales Thema in der Politik.", "gesellschaft"),
    word("vocab_gesellschaft_03", "der demografische Wandel", "demographic change", "demografik değişim", "phrase", "Der demografische Wandel stellt das Rentensystem vor Herausforderungen.", "gesellschaft"),
    word("vocab_gesellschaft_04", "die Ungleichheit", "inequality", "eşitsizlik", "noun", "Die soziale Ungleichheit hat in den letzten Jahren zugenommen.", "gesellschaft"),
    word("vocab_gesellschaft_05", "die Solidarität", "solidarity", "dayanışma", "noun", "In der Krise zeigte die Gesellschaft große Solidarität.", "gesellschaft"),
    word("vocab_gesellschaft_06", "die Alterung", "aging (of population)", "yaşlanma", "noun", "Die Alterung der Gesellschaft betrifft das Gesundheitssystem direkt.", "gesellschaft"),
    word("vocab_gesellschaft_07", "ausgrenzen", "to exclude/marginalize", "dışlamak", "verb", "Niemand sollte aufgrund seiner Herkunft ausgegrenzt werden.", "gesellschaft"),
    word("vocab_gesellschaft_08", "der Zusammenhalt", "cohesion", "birlik/dayanışma", "noun", "Der gesellschaftliche Zusammenhalt ist in Krisenzeiten besonders wichtig.", "gesellschaft"),
    word("vocab_gesellschaft_09", "die Randgruppe", "marginalized group", "marjinal grup", "noun", "Randgruppen brauchen besondere gesellschaftliche Unterstützung.", "gesellschaft"),
    word("vocab_gesellschaft_10", "die Teilhabe", "participation/inclusion", "katılım", "noun", "Teilhabe am gesellschaftlichen Leben ist ein Grundrecht.", "gesellschaft"),
    word("vocab_gesellschaft_11", "die Generationengerechtigkeit", "intergenerational justice", "kuşaklararası adalet", "noun", "Generationengerechtigkeit fordert einen fairen Umgang mit Ressourcen.", "gesellschaft"),
    word("vocab_gesellschaft_12", "der gesellschaftliche Druck", "social pressure", "toplumsal baskı", "phrase", "Viele Jugendliche leiden unter gesellschaftlichem Druck.", "gesellschaft")
]

VOCAB["gesundheit"] = [
    word("vocab_gesundheit_01", "die Prävention", "prevention", "önleme", "noun", "Prävention ist besser als Behandlung.", "gesundheit"),
    word("vocab_gesundheit_02", "das Gesundheitssystem", "healthcare system", "sağlık sistemi", "noun", "Das deutsche Gesundheitssystem gilt als sehr gut ausgebaut.", "gesundheit"),
    word("vocab_gesundheit_03", "die psychische Gesundheit", "mental health", "ruh sağlığı", "phrase", "Psychische Gesundheit wird heute ernster genommen als früher.", "gesundheit"),
    word("vocab_gesundheit_04", "die Ernährung", "nutrition/diet", "beslenme", "noun", "Eine ausgewogene Ernährung stärkt das Immunsystem.", "gesundheit"),
    word("vocab_gesundheit_05", "die Behandlung", "treatment", "tedavi", "noun", "Die Behandlung dauerte mehrere Wochen.", "gesundheit"),
    word("vocab_gesundheit_06", "vorbeugen", "to prevent", "önlemek", "verb", "Regelmäßige Bewegung beugt vielen Krankheiten vor.", "gesundheit"),
    word("vocab_gesundheit_07", "die Krankenversicherung", "health insurance", "sağlık sigortası", "noun", "In Deutschland ist eine Krankenversicherung Pflicht.", "gesundheit"),
    word("vocab_gesundheit_08", "die Nebenwirkung", "side effect", "yan etki", "noun", "Dieses Medikament kann Nebenwirkungen wie Müdigkeit verursachen.", "gesundheit"),
    word("vocab_gesundheit_09", "der Erschöpfungszustand", "state of exhaustion", "tükenmişlik durumu", "noun", "Nach dem Marathon befand er sich in einem Erschöpfungszustand.", "gesundheit"),
    word("vocab_gesundheit_10", "die Genesung", "recovery", "iyileşme", "noun", "Wir wünschen dir eine gute Genesung.", "gesundheit"),
    word("vocab_gesundheit_11", "chronisch", "chronic", "kronik", "adjective", "Diabetes ist eine chronische Erkrankung.", "gesundheit"),
    word("vocab_gesundheit_12", "die Vorsorgeuntersuchung", "preventive checkup", "önleyici kontrol", "noun", "Regelmäßige Vorsorgeuntersuchungen können schwere Krankheiten früh erkennen.", "gesundheit")
]

VOCAB["medien"] = [
    word("vocab_medien_01", "die sozialen Medien", "social media", "sosyal medya", "phrase", "Soziale Medien beeinflussen die öffentliche Meinung stark.", "medien"),
    word("vocab_medien_02", "der Datenschutz", "data protection/privacy", "veri koruma", "noun", "Der Datenschutz spielt beim Online-Shopping eine wichtige Rolle.", "medien"),
    word("vocab_medien_03", "die Falschmeldung", "fake news", "sahte haber", "noun", "Falschmeldungen verbreiten sich in sozialen Netzwerken besonders schnell.", "medien"),
    word("vocab_medien_04", "die Digitalisierung", "digitalization", "dijitalleşme", "noun", "Die Digitalisierung verändert fast alle Berufsfelder.", "medien"),
    word("vocab_medien_05", "die Berichterstattung", "news coverage/reporting", "haber sunumu", "noun", "Die Berichterstattung über die Wahl war sehr ausführlich.", "medien"),
    word("vocab_medien_06", "manipulieren", "to manipulate", "manipüle etmek", "verb", "Bilder können leicht digital manipuliert werden.", "medien"),
    word("vocab_medien_07", "die Reichweite", "reach/audience size", "erişim", "noun", "Dieser Blogger hat eine enorme Reichweite im Internet.", "medien"),
    word("vocab_medien_08", "der Algorithmus", "algorithm", "algoritma", "noun", "Ein Algorithmus entscheidet, welche Beiträge angezeigt werden.", "medien"),
    word("vocab_medien_09", "die Medienkompetenz", "media literacy", "medya okuryazarlığı", "noun", "Medienkompetenz sollte schon in der Schule vermittelt werden.", "medien"),
    word("vocab_medien_10", "veröffentlichen", "to publish", "yayınlamak", "verb", "Er hat den Artikel gestern Abend veröffentlicht.", "medien"),
    word("vocab_medien_11", "die Quelle", "source", "kaynak", "noun", "Man sollte immer die Quelle einer Nachricht überprüfen.", "medien"),
    word("vocab_medien_12", "die Filterblase", "filter bubble", "filtre balonu", "noun", "Soziale Netzwerke können eine Filterblase erzeugen.", "medien")
]

VOCAB["reisen"] = [
    word("vocab_reisen_01", "die Reiseplanung", "trip planning", "seyahat planlaması", "noun", "Eine gute Reiseplanung spart am Ende viel Geld.", "reisen"),
    word("vocab_reisen_02", "nachhaltiges Reisen", "sustainable travel", "sürdürülebilir seyahat", "phrase", "Nachhaltiges Reisen gewinnt bei jungen Menschen an Bedeutung.", "reisen"),
    word("vocab_reisen_03", "der Kulturtourismus", "cultural tourism", "kültür turizmi", "noun", "Der Kulturtourismus bringt der Region wichtige Einnahmen.", "reisen"),
    word("vocab_reisen_04", "die Unterkunft", "accommodation", "konaklama", "noun", "Wir haben eine günstige Unterkunft in der Altstadt gebucht.", "reisen"),
    word("vocab_reisen_05", "das Reiseziel", "travel destination", "seyahat hedefi", "noun", "Portugal ist ein beliebtes Reiseziel für Familien.", "reisen"),
    word("vocab_reisen_06", "der Massentourismus", "mass tourism", "kitle turizmi", "noun", "Massentourismus belastet viele beliebte Küstenorte.", "reisen"),
    word("vocab_reisen_07", "erkunden", "to explore", "keşfetmek", "verb", "Wir wollen die Altstadt zu Fuß erkunden.", "reisen"),
    word("vocab_reisen_08", "der ökologische Fußabdruck", "ecological footprint", "ekolojik ayak izi", "phrase", "Fliegen vergrößert den ökologischen Fußabdruck erheblich.", "reisen"),
    word("vocab_reisen_09", "die Sehenswürdigkeit", "tourist attraction", "gezilecek yer", "noun", "Der Kölner Dom ist eine bekannte Sehenswürdigkeit.", "reisen"),
    word("vocab_reisen_10", "die Gastfreundschaft", "hospitality", "misafirperverlik", "noun", "Die Gastfreundschaft der Einheimischen hat uns beeindruckt.", "reisen"),
    word("vocab_reisen_11", "abgelegen", "remote/secluded", "uzak/tenha", "adjective", "Das Dorf liegt sehr abgelegen in den Bergen.", "reisen"),
    word("vocab_reisen_12", "die Reisewarnung", "travel warning", "seyahat uyarısı", "noun", "Das Außenministerium hat eine Reisewarnung ausgesprochen.", "reisen")
]

VOCAB["umwelt"] = [
    word("vocab_umwelt_01", "der Klimawandel", "climate change", "iklim değişikliği", "noun", "Der Klimawandel ist eine der größten Herausforderungen unserer Zeit.", "umwelt"),
    word("vocab_umwelt_02", "die Nachhaltigkeit", "sustainability", "sürdürülebilirlik", "noun", "Nachhaltigkeit sollte in jedem Unternehmen eine Rolle spielen.", "umwelt"),
    word("vocab_umwelt_03", "die erneuerbare Energie", "renewable energy", "yenilenebilir enerji", "phrase", "Erneuerbare Energie wird zunehmend günstiger.", "umwelt"),
    word("vocab_umwelt_04", "die Mülltrennung", "waste separation", "atık ayrıştırma", "noun", "Mülltrennung ist in Deutschland gesetzlich vorgeschrieben.", "umwelt"),
    word("vocab_umwelt_05", "der Artenschutz", "species protection", "tür koruma", "noun", "Artenschutz ist notwendig, um das ökologische Gleichgewicht zu erhalten.", "umwelt"),
    word("vocab_umwelt_06", "verschmutzen", "to pollute", "kirletmek", "verb", "Plastikmüll verschmutzt zunehmend die Weltmeere.", "umwelt"),
    word("vocab_umwelt_07", "der CO2-Ausstoß", "CO2 emissions", "CO2 salımı", "noun", "Der CO2-Ausstoß muss drastisch reduziert werden.", "umwelt"),
    word("vocab_umwelt_08", "die Biodiversität", "biodiversity", "biyoçeşitlilik", "noun", "Die Biodiversität in den Regenwäldern ist einzigartig.", "umwelt"),
    word("vocab_umwelt_09", "der Umweltschutz", "environmental protection", "çevre koruma", "noun", "Umweltschutz beginnt schon im Alltag jedes Einzelnen.", "umwelt"),
    word("vocab_umwelt_10", "das Ökosystem", "ecosystem", "ekosistem", "noun", "Jedes Ökosystem reagiert unterschiedlich auf den Klimawandel.", "umwelt"),
    word("vocab_umwelt_11", "aussterben", "to become extinct", "nesli tükenmek", "verb", "Viele Tierarten drohen in den nächsten Jahrzehnten auszusterben.", "umwelt"),
    word("vocab_umwelt_12", "die Wiederverwertung", "recycling", "geri dönüşüm", "noun", "Die Wiederverwertung von Materialien schont natürliche Ressourcen.", "umwelt")
]

VOCAB["wirtschaft"] = [
    word("vocab_wirtschaft_01", "die Globalisierung", "globalization", "küreselleşme", "noun", "Die Globalisierung hat den Welthandel grundlegend verändert.", "wirtschaft"),
    word("vocab_wirtschaft_02", "der Verbraucherschutz", "consumer protection", "tüketici koruması", "noun", "Der Verbraucherschutz sorgt für faire Handelspraktiken.", "wirtschaft"),
    word("vocab_wirtschaft_03", "die Inflation", "inflation", "enflasyon", "noun", "Die Inflation hat die Kaufkraft vieler Haushalte gesenkt.", "wirtschaft"),
    word("vocab_wirtschaft_04", "die Konjunktur", "economic cycle/situation", "ekonomik durum", "noun", "Die Konjunktur hat sich im letzten Quartal leicht erholt.", "wirtschaft"),
    word("vocab_wirtschaft_05", "das Wirtschaftswachstum", "economic growth", "ekonomik büyüme", "noun", "Das Wirtschaftswachstum blieb hinter den Erwartungen zurück.", "wirtschaft"),
    word("vocab_wirtschaft_06", "investieren", "to invest", "yatırım yapmak", "verb", "Das Unternehmen will in neue Technologien investieren.", "wirtschaft"),
    word("vocab_wirtschaft_07", "der Arbeitsmarkt", "job market/labor market", "işgücü piyasası", "noun", "Der Arbeitsmarkt hat sich für Fachkräfte deutlich verbessert.", "wirtschaft"),
    word("vocab_wirtschaft_08", "die Staatsverschuldung", "national debt", "kamu borcu", "noun", "Die Staatsverschuldung ist während der Krise stark gestiegen.", "wirtschaft"),
    word("vocab_wirtschaft_09", "der Wettbewerb", "competition", "rekabet", "noun", "Fairer Wettbewerb kommt letztlich den Verbrauchern zugute.", "wirtschaft"),
    word("vocab_wirtschaft_10", "die Lieferkette", "supply chain", "tedarik zinciri", "noun", "Die globalen Lieferketten wurden durch die Krise stark gestört.", "wirtschaft"),
    word("vocab_wirtschaft_11", "florieren", "to flourish/thrive", "gelişmek/serpilmek", "verb", "Der Handel florierte trotz der schwierigen Umstände.", "wirtschaft"),
    word("vocab_wirtschaft_12", "die Kaufkraft", "purchasing power", "satın alma gücü", "noun", "Die steigenden Preise verringern die Kaufkraft der Bevölkerung.", "wirtschaft")
]

os.makedirs('content/vocabulary', exist_ok=True)
total = 0
for category, words in VOCAB.items():
    path = f'content/vocabulary/{category}.json'
    with open(path, 'w', encoding='utf-8') as f:
        json.dump({"category": category, "level": "B2", "words": words}, f, ensure_ascii=False, indent=2)
    print(f'Wrote {path}: {len(words)} words')
    total += len(words)

print(f'\nTotal: {total} words across {len(VOCAB)} categories')
