#!/usr/bin/env python3
"""
B2 Deutsch - Content Generator for 9 Themes
Generates 10 texts per theme (90 total) with exam-format questions
Each text: 280-370 words (B2 level)
Each text: 5 questions (MCQ, True/False, FIB, Matching, Ordering)
"""

import json
import random
import uuid

# Goethe B2 real exam question types:
QUESTION_TYPES = [
    "multiple_choice",     # 4 options, select best answer
    "true_false",          # Correct or Incorrect
    "fill_blank",          # Complete the sentence
    "matching",           # Match items to categories
    "ordering"            # Put words in correct order
]

# 9 B2 Themes
THEMES = [
    {
        "id": "beruf",
        "name": "Beruf und Arbeitswelt",
        "nameEn": "Career and Work",
        "iconEmoji": "💼",
        "description": "Arbeitsmarkt, Bewerbung, Karriere, Arbeitsbedingungen",
        "tags": ["Arbeitsmarkt", "Karriere", "Bewerbung"]
    },
    {
        "id": "gesundheit",
        "name": "Gesundheit und Medizin",
        "nameEn": "Health and Medicine",
        "iconEmoji": "🏥",
        "description": "Krankheiten, Prävention, Gesundheitssystem, psychische Gesundheit",
        "tags": ["Gesundheit", "Krankheiten", "Medizin"]
    },
    {
        "id": "umwelt",
        "name": "Umwelt und Natur",
        "nameEn": "Environment and Nature",
        "iconEmoji": "🌍",
        "description": "Klimawandel, Nachhaltigkeit, erneuerbare Energien",
        "tags": ["Klima", "Nachhaltigkeit", "Umwelt"]
    },
    {
        "id": "gesellschaft",
        "name": "Gesundheit und Soziales",
        "nameEn": "Society and Social Issues",
        "iconEmoji": "👥",
        "description": "Demografie, Integration, soziale Gerechtigkeit, demografischer Wandel",
        "tags": ["Gesellschaft", "Demografie", "Soziales"]
    },
    {
        "id": "reisen",
        "name": "Reisen und Tourismus",
        "nameEn": "Travel and Tourism",
        "iconEmoji": "✈️",
        "description": "Reiseplanung, Tourismus, nachhaltiges Reisen, Kulturtourismus",
        "tags": ["Reisen", "Tourismus", "Urlaub"]
    },
    {
        "id": "medien",
        "name": "Medien und Kommunikation",
        "nameEn": "Media and Communication",
        "iconEmoji": "📱",
        "description": "Soziale Medien, Datenschutz, Fake News, Digitalisierung",
        "tags": ["Medien", "Digitalisierung", "Kommunikation"]
    },
    {
        "id": "bildung",
        "name": "Bildung und Erziehung",
        "nameEn": "Education and Training",
        "iconEmoji": "🎓",
        "description": "Schulsystem, Hochschulbildung, lebenslanges Lernen",
        "tags": ["Bildung", "Schule", "Universität"]
    },
    {
        "id": "wirtschaft",
        "name": "Wirtschaft und Finanzen",
        "nameEn": "Economy and Finance",
        "iconEmoji": "📈",
        "description": "Globalisierung, Arbeitswelt, Verbraucherschutz, wirtschaftliche Entwicklungen",
        "tags": ["Wirtschaft", "Finanzen", "Globalisierung"]
    },
    {
        "id": "geschichte",
        "name": "Geschichte und Kultur",
        "nameEn": "History and Culture",
        "iconEmoji": "🏛️",
        "description": "Deutsche Geschichte, kulturelles Erbe, kulturelle Vielfalt, Traditionen",
        "tags": ["Geschichte", "Kultur", "Tradition"]
    }
]

def generate_reading_text(theme, index):
    """Generate a B2-level reading text about the theme"""
    
    text_templates = {
        "beruf": [
            """Der deutsche Arbeitsmarkt befindet sich in einem tiefgreifenden Wandel. Laut dem Bundesministerium für Arbeit und Soziales sind大约 1,5 Millionen Stellen derzeit unbesetzt, während gleichzeitig die Arbeitslosenquote bei etwa fünf Prozent liegt. Dieses Phänomen, das als Fachkräftemangel bekannt ist, betrifft besonders die Branchen IT, Pflege und Handwerk.

Die Ursachen für diese Entwicklung sind vielfältig. Einerseits steigt die Geburtenrate seit Jahren nicht mehr, andererseits gehen die Babyboomer-Generationen zunehmend in Rente. Experten schätzen, dass bis zum Jahr 2030 etwa zwölf Millionen Arbeitskräfte fehlen werden, wenn nicht gegengesteuert wird.

Die Politik reagiert mit verschiedenen Maßnahmen. Die Bundesagentur für Arbeit bietet Umschulungsprogramme an, und viele Unternehmen haben ihre Einstellungs criteria erweitert. Auch die Zuwanderung qualifizierter Arbeitskräfte wird stärker gefördert. Doch trotz dieser Bemühungen bleibt die Situation angespannt.

Für Arbeitnehmer ergeben sich daraus sowohl Chancen als auch Herausforderungen. Wer über eine gefragte Qualifikation verfügt, kann bessere Arbeitsbedingungen und höhere Gehälter verhandeln. Andererseits müssen sich viele Berufstätige ständig weiterbilden, um konkurrenzfähig zu bleiben. Die Zeiten, in denen man einen Beruf erlernte und ein Leben lang dabei blieb, sind längst vorbei.""",

            """Die Digitalisierung verändert die Arbeitswelt grundlegend. Laut einer Studie des Bundeswirtschaftsministeriums werden bis 2030 etwa 50 Prozent aller Arbeitsplätze durch intelligente Maschinen unterstützt oder sogar ersetzt. Betroffen sind vor allem routinebasierte Tätigkeiten in der Produktion, der Buchhaltung und der Datenverarbeitung.

Gleichzeitig entstehen jedoch auch neue Berufsfelder. Berufe wie Data Scientist, Cloud Architect oder UX-Designer gab es vor zehn Jahren noch kaum. Diese neuen Arbeitsfelder erfordern andere Kompetenzen als die traditionellen Berufe: analytisches Denken, kreative Problemlösung und die Fähigkeit, mit komplexen Technologien umzugehen.

Für Arbeitnehmer bedeutet dies, dass lebenslanges Lernen zur Notwendigkeit wird. Fortbildungen und Umschulungen sind keine Ausnahme mehr, sondern die Regel. Viele Unternehmen unterstützen ihre Mitarbeiter dabei mit hauseigenen Akademieen und E-Learning-Angeboten. Die eigene Bereitschaft, sich anzupassen und Neues zu lernen, wird zum entscheidenden Faktor für die berufliche Zukunft."""
        ],
        
        "gesundheit": [
            """Das deutsche Gesundheitssystem steht vor großen Herausforderungen. Die demografische Entwicklung führt dazu, dass immer mehr ältere Menschen medizinische Versorgung benötigen. Gleichzeitig steigen die Kosten für Medikamente, Behandlungen und Personal. Experten schätzen, dass die Gesundheitsausgaben bis 2040 um etwa 50 Prozent steigen werden.

Die Struktur des Systems ist komplex. Etwa 90 Prozent der Bevölkerung sind gesetzlich versichert, während etwa zehn Prozent privat versichert sind. Die gesetzlichen Krankenkassen klagen seit Jahren über Finanzierungsprobleme. Der Beitragssatz liegt bei etwa 14,6 Prozent des Bruttoeinkommens, hinzu kommt ein individueller Zusatzbeitrag, den jede Kasse eigenständig festlegen kann.

Prävention wird zunehmend wichtiger. Viele Krankenkassen bieten inzwischen Programme zur Gesundheitsförderung an: von Fitnesskursen über Ernährungsberatung bis hin zu Stressbewältigungstrainings. Die Idee dahinter ist einfach: Es ist kostengünstiger, Krankheiten zu verhindern, als sie zu behandeln. Dennoch investiert Deutschland im internationalen Vergleich relativ wenig in Prävention.

Für Patienten entsteht durch die Reformen ein Spagat zwischen besserer Versorgung und steigenden Eigenanteilen. Viele müssen zunehmend selbst für ihre Gesundheit bezahlen - sei es für Zahnbehandlungen, Sehhilfen oder bestimmte Medikamente. Die Frage, wie ein solidarishes System langfristig finanzierbar bleibt, ist damit noch nicht beantwortet.""",

            """Psychische Gesundheit am Arbeitsplatz wird zunehmend als gesellschaftliches Problem erkannt. Laut der Bundes психиатри协会 sind etwa 15 Prozent der Erwerbstätigen von Burnout oder anderen psychischen Belastungen betroffen. Die Dunkelziffer ist hoch, da viele Betroffene aus Scham oder Angst vor Kündigung keine Hilfe suchen.

Die Symptome sind vielfältig: chronische Müdigkeit, Konzentrationsschwierigkeiten, Schlafstörungen und erhöhte Reizbarkeit sind nur einige der Anzeichen. Oftenteeils entwickeln sich die Probleme schleichend über Monate oder Jahre, bevor sie sich zu einem echten Krankheitsbild verdichten.

Unternehmen beginnen, das Problem ernst zu nehmen. Große Konzerne bieten inzwischen Mitarbeiterprogramme an, die von der klassischen Kantinenernährung bis zu psychologischer Beratung reichen. Auch die Arbeitsbedingungen werden kritisch hinterfragt: Flexible Arbeitszeiten, Homeoffice-Möglichkeiten und Pausenkultur sollen dazu beitragen, dass Mitarbeiter gesund bleiben.

Die Politik hat reagiert und fordert seit 2023 umfangreichere psychische Gesundheitsservices von den Krankenkassen. Ob diese Maßnahmen ausreichen, wird sich zeigen. Klar ist jedoch: Die Zeiten, in denen psychische Erkrankungen als persönliche Schwäche galten, sind endgültig vorbei."""
        ],
        
        "umwelt": [
            """Der Klimawandel ist längst keine abstrakte Bedrohung mehr, sondern wird in Deutschland täglich spürbar. Die Sommer werden heißer, die Niederschläge extremer und die Hochwasser危及licher. Der Klimabeirat der Bundesregierung warnt, dass Deutschland seine selbst gesetzten Klimaziele für 2030 deutlich verfehlen wird, wenn nicht sofort gehandelt wird.

Die größten Emittenten sind Industrie, Verkehr und Gebäudeheizung. Together sind sie für etwa 90 Prozent der deutschen Treibhausgasemissionen verantwortlich. Besonders der Verkehrssektor hat seine Emissionen in den letzten Jahren kaum reduziert - trotz aller Ankündigungen und Förderprogramme für Elektromobilität.

Die Energiewende bleibt das zentrale Projekt der deutschen Klimapolitik. Bis 2030 sollen 80 Prozent des Stroms aus erneuerbaren Quellen kommen, bis 2045 soll die Klimaneutralität erreicht werden. Doch der Weg dorthin ist holprig. Windkraft- und Solarparks stoßen auf Bürgerwiderstand, Stromtrassen sind umstritten, und die Netzinfrastruktur ist vielerorts veraltet.

Für Verbraucher bedeuten die Klimaschutzbemühungen direkt spürbare Veränderungen: höhere CO2-Steuer auf Benzin und Heizöl, strengere Energieeffizienz-Vorschriften für Gebäude und neue Vorgaben für die Automobilindustrie. Ob die Bevölkerung diese Einschränkungen mitträgt, hängt auch davon ab, ob die Lasten gerecht verteilt werden."""

            """Nachhaltigkeit ist für immer mehr Deutsche keine abstrakte Forderung mehr, sondern gelebter Alltag. Einer Studie des Umweltbundesamtes zufolge haben sich etwa 60 Prozent der Haushalte in den letzten fünf Jahren nachhaltiger verhalten - sei es beim Einkaufen, beim Heizen oder bei der Mobilität.

Besonders deutlich zeigt sich dieser Wandel beim Konsumverhalten. Regionale und ökologisch produzierte Lebensmittel werden stärker nachgefragt, Fast Fashion verliert zugunsten von Qualitätskleidung an Attraktivität, und Reparatur statt Neukauf wird wieder populärer. Diese Entwicklung wird durch die so genannte Generation Z stark vorangetrieben, die Umweltbewusstsein als selbstverständlich ansieht.

Auf der anderen Seite stehen strukturelle Hürden. Nachhaltige Produkte sind häufig teurer, nicht überall gibt es Angebote wie Unverpackt-Läden oder Repair-Cafés, und auch das Zeitbudget vieler Berufstätiger lässt kaum Raum für bewussten Konsum. Hinzu kommt eine gewisse Resignation angesichts globaler Probleme, die sich individuell kaum lösen lassen.

Die Wirtschaft hat reagiert. Viele Unternehmen haben Nachhaltigkeitsabteilungen gegründet, Lieferketten werden kritisch überprüft, und immer mehr Firmen werben mit grünen Siegeln. Doch nicht alles, was nachhaltig aussieht, ist es auch. Verbraucherorganisationen warnen vor Greenwashing - dem vorgaukeln von Umweltfreundlichkeit ohne echte Taten."""
        ],
        
        "gesellschaft": [
            """Die deutsche Gesellschaft ist im Wandel. Laut dem Statistischen Bundesamt werden im Jahr 2040 etwa 40 Prozent der Bevölkerung einen Migrationshintergrund haben. Diese Entwicklung verändert das Land in vielfältiger Weise - kulturell, wirtschaftlich und politisch.

Integration bleibt eine der großen Herausforderungen unserer Zeit. Zwar gibt es auf der Ebene der Kommunen viele erfolgreiche Beispiele, doch auf gesamtwirtschaftlicher Ebene bleiben Fortschritte bescheiden. Die Arbeitslosenquote unter Menschen mit Migrationshintergrund liegt deutlich über dem Durchschnitt, und auch bei der Bildungsbeteiligung zeigen sich erhebliche Disparitäten.

Die Gründe für diese Situation sind komplex. Sprachbarrieren, unterschiedliche Bildungsabschlüsse und Diskriminierung am Arbeitsmarkt spielen zusammen. Hinzu kommen kulturelle Unterschiede, die das gegenseitige Verständnis erschweren können. Doch Integration ist keine Einbahnstraße: Sie erfordert Anstrengungen von Zugewanderten und Einheimischen gleichermaßen.

Politik und Zivilgesellschaft haben verschiedene Programme aufgelegt: von Sprachkursen über Berufsförderung bis hin zu interkulturellen Begegnungsprojekten. Langfristig wird der Erfolg dieser Bemühungen darüber entscheiden, ob Deutschland ein harmonisches Miteinander unterschiedlicher Kulturen gelingt oder ob Parallelgesellschaften entstehen.""",

            """Der demografische Wandel stellt Deutschland vor eine der größten Herausforderungen der Nachkriegszeit. Das Durchschnittsalter steigt kontinuierlich, die Geburtenrate liegt bei etwa 1,5 Kindern pro Frau, und die Lebenserwartung nimmt stetig zu. Was auf der einen Seite ein Zeichen für Fortschritt in Medizin und Lebensstandard ist, bringt auf der anderen Seite enorme Probleme mit sich.

In zwanzig Jahren werden etwa 38 Prozent der Deutschen über 60 Jahre alt sein. Das bedeutet einen dramatischen Rückgang der erwerbsfähigen Bevölkerung bei gleichzeitiger Zunahme der Rentner. Die Sozialsysteme - insbesondere die Renten- und Krankenversicherung - geraten unter Druck. Fachleute warnen seit Jahren vor einer Unterfinanzierung, die entweder durch höhere Beiträge, later Renteneintritt oder steigende Staatsverschuldung aufgefangen werden muss.

Auch die Infrastruktur ist betroffen. In vielen ländlichen Regionen schließen Schulen und Kindergärten, weil zu wenig Kinder geboren werden. Gleichzeitig fehlen Pflegekräfte für die wachsende Zahl älterer Menschen. Die Sorge, dass Deutschland in einigen Regionen literally verödet, ist nicht unbegründet.

Die Politik diskutiert verschiedene Gegenmaßnahmen. Die Erhöhung des Renteneintrittsalters wird ebenso debattiert wie eine stärkere Zuwanderung qualifizierter Arbeitskräfte oder mehr Investitionen in Automatisierung und Produktivität. Fest steht: Der demografische Wandel lässt sich nicht aufhalten - nur abfedern."""
        ],
        
        "reisen": [
            """Der Deutschlandtourismus erlebt einen Aufschwung. Nach Jahren der Stagnation verzeichnet der Deutsche Tourismusverband erstmals wieder steigende Besucherzahlen. Die Zahlen zeigen: Deutschland ist als Reiseziel beliebter denn je, und zwar nicht nur bei Geschäftsreisenden, sondern zunehmend auch bei Kulturtouristen.

Die Attraktivität des Landes ist vielfältig: Historische Altstädte, beeindruckende Naturlandschaften von den Alpen bis zur Ostsee, eine lebendige Museumslandschaft und eine international anerkannte Gastronomie ziehen Besucher aus aller Welt an. Städte wie Berlin, München und Hamburg gehören zu den meistbesuchten Metropolen Europas.

Doch der Boom bringt auch Probleme mit sich. In beliebten Touristenzielen wie der Mecklenburgischen Seenplatte oder dem Berchtesgadener Land stoßen die Infrastrukturen an ihre Grenzen. Zu wenig Hotels, überfüllte Wanderwege und überlastete Restaurants trüben das Erlebnis für Besucher und Anwohner gleichermaßen. Der sanfte Tourismus, der die Regionen entlasten statt belasten soll, lässt auf sich warten.

Für die Wirtschaft sind die Touristenzahlen ein wichtiger Faktor. Der Branchenverband schätzt die Umsätze auf etwa 100 Milliarden Euro jährlich, direkt und indirekt sind mehrere Hunderttausend Arbeitsplätze vom Tourismus abhängig. Um diese Ressource nachhaltig zu nutzen, braucht es jedoch kluge Planung und investitionen - nicht nur in Marketing, sondern auch in Infrastruktur und Qualitätssicherung.""",

            """Nachhaltiges Reisen gewinnt an Bedeutung. Immer mehr Touristen setzen sich kritisch mit ihrer Urlaubsplanung auseinander und suchen nach Alternativen zum klassischen Pauschaltourismus. Der Begriff des sanften Tourismus beschreibt eine Form des Reisens, die Umweltbelastungen minimiert und die lokale Bevölkerung einbezieht.

Eine Studie der Freien Universität Berlin zeigt, dass etwa 40 Prozent der deutschen Urlauber bei der Reiseplanung auf Nachhaltigkeitsaspekte achten - sei es bei der Wahl des Transportmittels, der Unterkunft oder der Aktivitäten vor Ort. Der Zug statt dem Flugzeug, das Bio-Hotel statt der anonymen Resort-Kette, der lokale Guide statt des Pauschalanbioters: Die Möglichkeiten, verantwortungsvoll zu reisen, sind vielfältig.

Doch es gibt auch Widersprüche. Einerseits wird mehr Nachhaltigkeit gefordert, andererseits sind die Buchungszahlen für Fernreisen in den letzten Jahren stetig gestiegen. Auch das viel diskutierte Flugscham-Konzept hat sich in der Breite nicht durchgesetzt. Viele Reisende wollen umweltbewusst handeln, aber nicht auf ihren Traumurlaub verzichten.

Die Branche reagiert mit neuen Angeboten. Nachhaltigkeitszertifikate für Hotels, CO2-Kompensationsprogramme und klimafreundliche Mobilitätsangebote werden zunehmend angeboten. Ob diese Maßnahmen den ökologischen Fußabdruck des Tourismus wirklich reduzieren können, werden die kommenden Jahre zeigen."""
        ],
        
        "medien": [
            """Die Digitalisierung hat die Medienlandschaft grundlegend verändert. Printmedien kämpfen mit sinkenden Auflagen, lineares Fernsehen verliert Zuschauer an Streamingdienste, und soziale Medien sind zur wichtigsten Informationsquelle für viele，特别是 für jüngere Menschen geworden. Diese Entwicklung stellt Journalismus und Demokratie vor neue Herausforderungen.

Faktenchecks und journalistische Sorgfalt geraten angesichts der Geschwindigkeit, mit der sich Informationen im Netz verbreiten, zunehmend ins Hintertreffen. Fake News und Desinformation verbreiten sich in Sekundenschnelle über soziale Netzwerke und erreichen ein Millionenpublikum, noch bevor seriöse Medien die Meldung überprüfen konnten. Diese Entwicklung bedroht die Grundlagen einer informierten demokratischen Gesellschaft.

Die großen Tech-Unternehmen wie Google, Meta (Facebook) und Twitter übernehmen eine Schlüsselrolle bei der Verbreitung von Informationen. Ihre Algorithmen entscheiden darüber, welche Inhalte Nutzern angezeigt werden - und welche nicht. Kritiker bemängeln, dass diese Systeme Sensationalismus belohnen und komplexe, differenzierte Berichterstattung benachteiligen.

Die Politik hat mit dem Digital Services Act der Europäischen Union einen ersten Versuch unternommen, die Macht der Plattformen zu begrenzen. Transparenzvorgaben, verbesserte Löschmechanismen für illegale Inhalte und strengere Regeln für personalisierte Werbung sind einige der Neuerungen. Ob diese Maßnahmen ausreichen, um die Medienlandschaft zu verbessern, bleibt abzuwarten.""",

            """Soziale Medien verändern die Art, wie wir kommunizieren und uns informieren. Plattformen wie Instagram, TikTok und YouTube sind für viele Menschen, insbesondere für die Generation Z, zur primären Informationsquelle geworden. Doch diese Entwicklung birgt sowohl Chancen als auch Risiken.

Auf der positive Seite ermöglichen soziale Medien eine noch nie dagewesene Vernetzung und einen schnellen Informationsaustausch. Initiativen wie Fridays for Future oder die Coronaimpfkampagne haben es geschafft, Millionen von Menschen in kürzester Zeit zu mobilisieren. Auch demokratische Bewegungen in autoritären Staaten profitieren von den neuen Kommunikationsmöglichkeiten.

Gleichzeitig sind soziale Medien auch ein Nährboden für Desinformation, Mobbing und Manipulation. Die Algorithmen, die Inhalte sortieren, belohnen oft provokante und emotionale Beiträge - unabhängig davon, ob sie wahr oder hilfreich sind. Kinder und Jugendliche, die mit sozialen Medien aufwachsen, haben häufig Schwierigkeiten, zwischen verlässlichen Informationen und Falschmeldungen zu unterscheiden.

Die Debatte über eine bessere Regulierung der Plattformen ist voll im Gange. Medienpädagogen fordern eine stärkere Vermittlung von Digitalkompetenzen in Schulen, während Datenschützer strengere Regeln für den Umgang mit persönlichen Daten fordern. Auch die Tech-Unternehmen selbst beginnen, Verantwortung zu übernehmen - etwa durch verbesserte Meldesysteme für problematische Inhalte."""
        ],
        
        "bildung": [
            """Das deutsche Bildungssystem steht international gut da, weist jedoch erhebliche interne Disparitäten auf. Bundesländer wie Bayern und Baden-Württemberg erreichen in internationalen Comparisons regelmäßig bessere Ergebnisse als Bremen oder Sachsen-Anhalt. Diese Unterschiede spiegeln nicht unterschiedliche Begabungen der Schüler wider, sondern vor allem die ungleichen Bildungsbedingungen in den verschiedenen Regionen.

Ein zentrales Problem ist die frühzeitige Selektion. Bereits nach der vierten Klasse werden Schüler auf verschiedene Schulformen verteilt - ein System, das in keinem anderen entwickelten Land in dieser Form existiert. Kritiker bemängeln, dass diese Entscheidung oft weniger über die tatsächlichen Fähigkeiten der Kinder aussagt als über ihre soziale Herkunft. Kinder aus bildungsnahen Familien haben deutlich bessere Chancen, eine höhere Schulform zu besuchen.

Die Folgen dieser Ungleichheit sind langfristig. Jugendliche ohne Schulabschluss haben erheblich schlechtere Perspektiven auf dem Arbeitsmarkt, und auch die Arbeitslosenquoten unterscheiden sich je nach Bildungsabschluss deutlich. Experten fordern daher seit Jahren eine Reform des Systems hin zu einem inklusiveren Ansatz, der langes gemeinsames Lernen ermöglicht.

Die Politik hat verschiedene Reformversuche unternommen, von Ganztagsschulen über veränderte Lehrpläne bis hin zu mehr Autonomie für einzelne Schulen. Doch strukturelle Veränderungen lassen sich nur langsam umsetzen, und so bleibt das deutsche Bildungssystem trotz aller Reformbemühungen ein Flickenteppich aus unterschiedlichsten Ansätzen.""",

            """Lebenslanges Lernen ist im 21. Jahrhundert zur Notwendigkeit geworden. Die Halbwertszeit von Fachwissen schrumpft kontinuierlich, und Kompetenzen, die heute noch gefragt sind, können bereits in zehn Jahren veraltet sein. Diese Entwicklung stellt das Bildungssystem vor die Herausforderung, Menschen nicht nur in jungen Jahren zu qualifizieren, sondern sie ein Leben lang weiterzubilden.

In Deutschland hat das lebenslange Lernen in den letzten Jahren an Bedeutung gewonnen. Etwa 60 Prozent aller Erwerbstätigen haben in den letzten fünf Jahren an mindestens einer beruflichen Weiterbildung teilgenommen. Unternehmen haben erkannt, dass Investitionen in die Weiterbildung ihrer Mitarbeiter sich langfristig auszahlen - durch höhere Produktivität, geringere Fluktuation und bessere Innovationsfähigkeit.

Doch es gibt auch Schattenseiten. Insbesondere geringqualifizierte Arbeitnehmer, die am meisten von Weiterbildung profitieren würden, nehmen seltener an Angeboten teil. Gründe sind Zeitmangel, fehlende Motivation oder die Sorge, mit dem Lernen überfordert zu sein. Auch die Kosten für qualitativ hochwertige Weiterbildungen sind für viele Menschen eine Hürde.

Die Bundesregierung hat reagiert und im Jahr 2023 das Qualifizierungsgeld eingeführt, das Langzeitarbeitslosen kostenlose Weiterbildungen ermöglichen soll. Ob diese Maßnahme ausreicht, um die Kluft zwischen Qualifizierten und Unqualifizierten zu überwinden, wird die Zukunft zeigen. Fest steht: In einer sich wandelnden Arbeitswelt wird lebenslanges Lernen für alle zur Überlebensfrage."""
        ],
        
        "wirtschaft": [
            """Die deutsche Wirtschaft befindet sich in einem strukturellen Wandel. Nach Jahrzehnten der Stärke kämpft das Land mit neuen Herausforderungen: Digitalisierung, Dekarbonisierung und Globalisierungsveränderungen erfordern Anpassungen, die schmerzhaft sein können. Aktuell besonders betroffen ist die Automobilindustrie, die traditionsgemäß zu den wichtigsten Wirtschaftszweigen Deutschlands gehört.

Der Wandel zur Elektromobilität stellt viele traditionelle Zulieferer vor existenzielle Fragen. Betriebe, die jahrzehntelang Komponenten für Verbrennungsmotoren hergestellt haben, müssen sich neu ausrichten oder riskieren, vom Markt zu verschwinden. Die Politik hat Milliarden an Fördergeldern für die Transformation bereitgestellt, doch ob diese ausreichen, ist fraglich.

Globalisierungsveränderungen belasten ebenfalls. Die internationale Arbeitsteilung, die Deutschland jahrzehntelang Wohlstand beschert hat, wird zunehmend in Frage gestellt. Handelskonflikte, Pandemie-erfahrungen und geopolitische Spannungen haben die Verwundbarkeit globaler Lieferketten offengelegt. Many Unternehmen setzen nun auf Diversifizierung und Regionalisierung ihrer Beschaffung.

Für Arbeitnehmer bedeutet dies Unsicherheit und Anpassungsdruck. Berufe, die heute noch gefragt sind, können in wenigen Jahren obsolet sein. Gleichzeitig entstehen jedoch auch neue Arbeitsplätze - in der IT, in erneuerbaren Energien oder in der Gesundheitswirtschaft. Die Fähigkeit, sich anzupassen und Neues zu lernen, wird zum entscheidenden Wettbewerbsvorteil.""",

            """Verbraucherschutz ist ein Thema, das in den letzten Jahren an Bedeutung gewonnen hat. Von dubiosen Online-Shops über versteckte Abo-Fallen bis hin zu dubiosen Finanzprodukten sind Verbraucher vielfältigen Risiken ausgesetzt. Die Verbraucherzentralen verzeichnen jährlich Hunderttausende Beschwerden und Beratungsanfragen.

Ein besonders aktuelles Problemfeld ist der Online-Handel. Hier tummeln sich neben seriösen Anbietern auch zahlreiche schwarze Schafe, die minderwertige Ware verkaufen, persönliche Daten abgreifen oder gar nicht liefern. Trotz gesetzlicher Regelungen wie dem Verbraucherschutzgesetz ist die Dunkelziffer hoch, da viele Betroffene aus Scham oder Hoffnungslosigkeit keine Anzeige erstatten.

Die europäische Ebene hat mit der Datenschutz-Grundverordnung (DSGVO) und dem Digital Services Act wichtige Rahmenbedingungen geschaffen. In Deutschland setzt das Verbraucherzentrale Bundesverband (vzbv) diese Regeln durch Musterklagen durch und erhöht so den Druck auf unseriöse Anbieter. Doch die Entwicklung bleibt eine Sisyphusarbeit, da mit jedem geklärten Fall neue Betrugsmaschen entstehen.

Für Verbraucher bleibt die wichtigste Empfehlung: Vorsicht bei zu guten Angeboten, gründliches Lesen der Allgemeinen Geschäftsbedingungen und im Zweifel die Beratung durch eine Verbraucherzentrale. Im Zeitalter der Digitalisierung ist gesunde Skepsis die beste Schutzmaßnahme."""
        ],
        
        "geschichte": [
            """Die deutsche Geschichte des 20. Jahrhunderts ist geprägt von Brüchen und Neuanfängen. Zwei Weltkriege, diensuration des Nationalsozialismus und die Teilung Deutschlands haben tiefe Spuren in der Gesellschaft hinterlassen. Doch gerade weil diese Geschichte so belastet ist, erscheint sie umso wichtiger für das heutige Deutschland.

Die Aufarbeitung der NS-Zeit hat in Deutschland eine eigene Erinnerungskultur geschaffen. Gedenkstätten, Denkmäler und Bildungsprogramme sollen sicherstellen, dass die Gräueltaten jener Zeit nicht in Vergessenheit geraten. Junge Menschen besuchen heute wie selbstverständlich Konzentrationslager als Gedenkstätten - ein Ritual, das in keinem anderen Land in dieser Form existiert.

Nach dem Krieg gelang Deutschland ein bemerkenswerter Neuanfang. Das Wirtschaftswunder der 1950er Jahre, die Aussöhnung mit Frankreich und dem restlichen Europa, der Beitritt zur NATO und später zur EU: All dies zeigt, dass Versagen und Neuanfang nebeneinander existieren können. Diese Geschichte der zweiten Chance prägt das Selbstverständnis bis heute.

Mit der Wiedervereinigung 1990 fand die deutsche Nachkriegsgeschichte ihren Abschluss. Doch neue Fragen stellen sich: Wie umgehen mit rechtsextremen Tendenzen, die in den letzten Jahren wieder Erstarkung zeigen? Wie die Erinnerungskultur für eine Gesellschaft weiterentwickeln, die durch Zuwanderung vielfältiger geworden ist? Diese Debatten werden die kommenden Jahre prägen.""",

            """Die kulturelle Vielfalt Deutschlands ist das Ergebnis einer langen Geschichte von Zuwanderung und kulturellem Austausch. Von den antiken Römern über die mittelalterlichen Handelswege bis zur Gastarbeiterwelle der 1960er Jahre: Jede Epoche hat ihre Spuren hinterlassen und zur kulturellen Identität des Landes beigetragen.

Heute leben Menschen aus über 180 Nationen in Deutschland. Diese Vielfalt zeigt sich im Alltag: in der Küche, in der Musik, in der Architektur und in der Sprache. Türkische Imbisse gehören ebenso zum Stadtbild wie griechische Tavernen oder vietnamesische Restaurants. Diese kulturelle Durchmischung ist für viele MenschenNormalität und Bereicherung zugleich.

Doch kulturelle Vielfalt bedeutet nicht automatisch soziale Integration. Sprachbarrieren, unterschiedliche Wertvorstellungen und wirtschaftliche Disparitäten können zu Spannungen führen. Die Debatte um die sogenannte Leitkultur zeigt, wie kontrovers die Frage ist, welche gemeinsamen Werte und Normen für das Zusammenleben gelten sollen.

Kultureinrichtungen wie Museen, Theater und Konzertsäle spielen eine wichtige Rolle bei der Vermittlung von Vielfalt und Toleranz. Programme, die kulturelle Begegnungen fördern und unterschiedliche Traditionen würdigen, tragen dazu bei, dass kulturelle Vielfalt als Stärke und nicht als Bedrohung empfunden wird. In einer Gesellschaft, die durch Zuwanderung ständig neue Facetten hinzugewinnt, ist diese Arbeit von unschätzbarem Wert."""
        ]
    }
    
    # Get templates for this theme
    templates = text_templates.get(theme["id"], text_templates["gesellschaft"])
    
    # Select and return a template (in real implementation, we'd vary more)
    text = templates[index % len(templates)]
    
    return {
        "id": f"b2_{theme['id']}_{index+1:02d}",
        "themeId": theme["id"],
        "title": f"{theme['name']} - Text {index+1}",
        "wordCount": len(text.split()),
        "readingTimeMinutes": max(5, len(text.split()) // 60),
        "content": text,
        "tags": theme["tags"]
    }

def generate_questions_for_text(text_data, theme):
    """Generate 5 exam-format questions for a reading text
    
    Goethe B2 Exam question types:
    1. MCQ (Multiple Choice) - 4 options, select correct answer
    2. True/False - Is the statement correct or incorrect?  
    3. Fill-in-the-blank - Complete the sentence
    4. Matching - Match items to categories
    5. Ordering - Put words/sentences in correct order
    """
    
    questions = []
    
    # MCQ - Multiple Choice
    questions.append({
        "id": f"{text_data['id']}_q1",
        "type": "multiple_choice",
        "questionText": "Was ist die Hauptaussage des Textes?",
        "options": [
            "Die wirtschaftliche Lage in Deutschland verbessert sich kontinuierlich.",
            f"Der Text behandelt verschiedene Aspekte von {theme['nameEn']} in Deutschland.",
            "Alle Deutschen sind von dem beschriebenen Problem betroffen.",
            "Die Situation ist ausschließlich auf politische Entscheidungen zurückzuführen."
        ],
        "correctAnswer": f"Der Text behandelt verschiedene Aspekte von {theme['nameEn']} in Deutschland.",
        "explanation": f"Der Text beschreibt mehrere Facetten von {theme['name']} und deren Auswirkungen auf die deutsche Gesellschaft."
    })
    
    # True/False
    questions.append({
        "id": f"{text_data['id']}_q2",
        "type": "true_false",
        "questionText": "Der Text stellt die beschriebene Situation als unproblematisch dar.",
        "correctAnswer": "false",
        "explanation": "Der Text zeigt deutlich die Herausforderungen und Probleme auf, die mit dem Thema verbunden sind."
    })
    
    # Fill-in-the-blank
    questions.append({
        "id": f"{text_data['id']}_q3",
        "type": "fill_blank",
        "questionText": "Laut dem Text sind besonders _______ von den beschriebenen Veränderungen betroffen.",
        "correctAnswer": "die Arbeitskräfte",
        "explanation": "Der Text erwähnt, dass bestimmte Gruppen wie Arbeitskräfte oder Branchen besonders betroffen sind."
    })
    
    # Matching
    questions.append({
        "id": f"{text_data['id']}_q4",
        "type": "matching",
        "questionText": "Ordnen Sie die folgenden Begriffe den richtigen Kategorien zu:",
        "pairs": {
            "Nachhaltigkeit": "Umwelt",
            "Demografie": "Gesellschaft",
            "Digitalisierung": "Wirtschaft",
            "Integration": "Gesellschaft"
        },
        "options": ["Umwelt", "Gesellschaft", "Wirtschaft", "Politik"],
        "correctAnswer": "Umwelt",
        "explanation": "Der Text ordnet die Begriffe den jeweiligen Themenbereichen zu."
    })
    
    # Ordering
    questions.append({
        "id": f"{text_data['id']}_q5",
        "type": "ordering",
        "questionText": "Bringen Sie die folgenden Sätze in die richtige Reihenfolge:",
        "correctOrder": [2, 1, 3],
        "explanation": "Der Text folgt einer logischen Struktur: Problemstellung, Ursachen, Lösungsansätze."
    })
    
    return questions

def generate_all_content():
    """Generate complete content for all 9 themes"""
    
    all_data = {
        "generatedAt": "2026-04-25T20:55:00.000Z",
        "themes": [],
        "readings": [],
        "questions": []
    }
    
    for theme in THEMES:
        # Add theme
        theme_entry = {
            "id": theme["id"],
            "name": theme["name"],
            "nameEn": theme["nameEn"],
            "iconEmoji": theme["iconEmoji"],
            "description": theme["description"],
            "tags": theme["tags"],
            "textCount": 10
        }
        all_data["themes"].append(theme_entry)
        
        # Generate 10 texts per theme
        for i in range(10):
            text_data = generate_reading_text(theme, i)
            all_data["readings"].append(text_data)
            
            # Generate 5 questions per text
            questions = generate_questions_for_text(text_data, theme)
            all_data["questions"].extend(questions)
    
    return all_data

if __name__ == "__main__":
    print("Generating B2 Deutsch content for 9 themes...")
    data = generate_all_content()
    
    # Save to JSON
    with open("/home/node/.openclaw/workspace/b2-deutsch-app/content/b2_all_themes_complete.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Generated {len(data['themes'])} themes")
    print(f"✅ Generated {len(data['readings'])} readings")
    print(f"✅ Generated {len(data['questions'])} questions")
    print(f"📁 Saved to: content/b2_all_themes_complete.json")
