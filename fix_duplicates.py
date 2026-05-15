#!/usr/bin/env python3
"""Fix duplicate function definitions in SubjectListViewModel.kt.

Original problem: getA2Subjects and getA1Subjects each appear TWICE.
Also: the first getA2Subjects (line 691) only has 1 subject (a2_01).
We need to:
1. Remove the duplicate getA2Subjects (lines 1011-?)
2. Remove the duplicate getA1Subjects (lines 1124-?)
3. Fix the first getA2Subjects to have 10 topics (a2_01 to a2_10)
"""

FILE = "app/src/main/java/com/b2deutsch/app/ui/subject/SubjectListViewModel.kt"

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

# ── Step 1: Remove duplicate getA2Subjects (second occurrence at line 1011) ─
# It starts at "    private fun getA2Subjects(): List<Subject> = listOf("
# and ends at "    )\n\n    private fun getA1Subjects"
# We need to find and remove this block

dup_a2_start_marker = '    private fun getA2Subjects(): List<Subject> = listOf(\n\n\n    private fun getC2Subjects'
# This pattern should uniquely identify the duplicate (second getA2Subjects followed by two blank lines then getC2Subjects)
dup_a2_start = content.find(dup_a2_start_marker)
if dup_a2_start >= 0:
    # Find the end of this block: "    )\n\n    private fun getC2Subjects"
    dup_a2_end = content.find('\n    )\n\n    private fun getC2Subjects', dup_a2_start)
    if dup_a2_end >= 0:
        block_to_remove = content[dup_a2_start:dup_a2_end + len('\n    )\n\n    private fun getC2Subjects')]
        content = content.replace(block_to_remove, '', 1)
        print("✅ Removed duplicate getA2Subjects")
    else:
        print("⚠️  Could not find end of duplicate getA2Subjects")
else:
    print("⚠️  Could not find duplicate getA2Subjects marker")

# ── Step 2: Remove duplicate getA1Subjects (second occurrence) ─
# It starts after the first getA2Subjects and ends before getC2Subjects
# Pattern: "    private fun getA1Subjects(): List<Subject> = listOf(\n        Subject(\n            id = \"a1_01\"..."
# It ends at "    )\n\n    private fun getC2Subjects"
dup_a1_start_marker = '    private fun getA1Subjects(): List<Subject> = listOf(\n        Subject(\n            id = "a1_01",\n            level = "A1",\n            name = "1. Verben konjugieren'
# Find first occurrence - it should be right after first getA2Subjects
# The duplicate should be after second getA2Subjects (which we just removed)
# Actually after removing second getA2Subjects, the remaining structure is:
# first getA2Subjects (line 691), first getA1Subjects (line 804), then... wait
# Let me re-check the structure after removal

# Actually, the structure in the original file is:
# - getB1Subjects (line 578)
# - getA2Subjects (line 691) ← FIRST, only has a2_01
# - getA1Subjects (line 804) ← FIRST, has 10 topics
# - getA2Subjects (line 1011) ← DUPLICATE, has 10 topics
# - getA1Subjects (line 1124) ← DUPLICATE, has 10 topics
# - getC2Subjects (line 1237)

# After removing the duplicate at line 1011:
# - getB1Subjects (line 578)
# - getA2Subjects (line 691) ← FIRST, only has a2_01
# - getA1Subjects (line 804) ← FIRST, has 10 topics
# - getC2Subjects (line ~1230 after removal)

# The second getA1Subjects starts at line 1124. After removing second getA2Subjects,
# the lines shift. But we can still identify it by content.

# Find duplicate getA1Subjects by looking for the one that comes AFTER the first getA1Subjects
# and has the same content as first getA1Subjects (a1_01 at top)
first_a1_pos = content.find('    private fun getA1Subjects(): List<Subject> = listOf(\n        Subject(\n            id = "a1_01",\n            level = "A1",\n            name = "1. Verben konjugieren')
print(f"First getA1Subjects found at char: {first_a1_pos}")

# Now find the second occurrence of this exact pattern (after first_a1_pos)
second_a1_search = content.find('    private fun getA1Subjects(): List<Subject> = listOf(\n        Subject(\n            id = "a1_01",\n            level = "A1",\n            name = "1. Verben konjugieren', first_a1_pos + 1)
print(f"Second getA1Subjects found at char: {second_a1_search}")

if second_a1_search >= 0:
    # Remove this duplicate block
    # It ends at "    )\n\n    private fun getC2Subjects"
    dup_a1_end = content.find('\n    )\n\n    private fun getC2Subjects', second_a1_search)
    if dup_a1_end >= 0:
        block_to_remove = content[second_a1_search:dup_a1_end + len('\n    )\n\n    private fun getC2Subjects')]
        content = content.replace(block_to_remove, '', 1)
        print("✅ Removed duplicate getA1Subjects")
    else:
        print("⚠️  Could not find end of duplicate getA1Subjects")
else:
    print("⚠️  Could not find second getA1Subjects")

# ── Step 3: Fix first getA2Subjects to have 10 topics ─
# The first getA2Subjects (line 691) only has a2_01. We need to add a2_02 through a2_10.

# Find the first getA2Subjects block
first_a2_start = content.find('    private fun getA2Subjects(): List<Subject> = listOf(\n        Subject(\n            id = "a2_01"')
# Find its end (at "    )\n\n    private fun getA1Subjects")
first_a2_end = content.find('\n    )\n\n    private fun getA1Subjects', first_a2_start)
if first_a2_start >= 0 and first_a2_end >= 0:
    # Get the current a2_01 subject content
    current_a2_block = content[first_a2_start:first_a2_end]
    # Check what's in there
    print(f"\nCurrent first getA2Subjects block length: {len(current_a2_block)}")
    print(f"Block preview: {repr(current_a2_block[:200])}")

# Now build the correct 10-topic A2 block
a2_subjects = '''    private fun getA2Subjects(): List<Subject> = listOf(
        Subject(
            id = "a2_01",
            level = "A2",
            name = "1. Präteritum (war, hatte, machte)",
            nameShort = "Präteritum",
            description = "Das Präteritum wird hauptsächlich in der geschriebenen Sprache und in formellen Situationen verwendet. Die wichtigsten Verben sind sein, haben und die Modalverben. Im Alltag wird es weniger häufig benutzt.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 1,
            quizCount = 5
        ),
        Subject(
            id = "a2_02",
            level = "A2",
            name = "2. Perfekt (haben/sein + Partizip II)",
            nameShort = "Perfekt",
            description = "Das Perfekt ist die wichtigste Vergangenheitsform im Alltag. Verwendung: haben oder sein als Hilfsverb + Partizip II. Die meisten Verben benutzen haben, nur Bewegungsverben und sein/werden benutzen sein.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 2,
            quizCount = 5
        ),
        Subject(
            id = "a2_03",
            level = "A2",
            name = "3. Verben mit Präpositionen (AC)",
            nameShort = "Verben + Präpositionen",
            description = "Bestimmte Verben erfordern bestimmte Präpositionen im Akkusativ oder Dativ: denken an (+A), warten auf (+A), sprechen über (+A), helfen bei (+D), sich freuen über (+A).",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 3,
            quizCount = 5
        ),
        Subject(
            id = "a2_04",
            level = "A2",
            name = "4. Wechselpräpositionen (in, auf, an, über, vor, zwischen, hinter, unter)",
            nameShort = "Wechselpräpositionen",
            description = "Wechselpräpositionen wechseln zwischen Akkusativ (Richtung) und Dativ (Ort): in, auf, an, über, vor, zwischen, hinter, unter. Akkusativ = wohin? Dativ = wo?",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 4,
            quizCount = 5
        ),
        Subject(
            id = "a2_05",
            level = "A2",
            name = "5. Nebensätze (dass, ob, weil, wenn, als)",
            nameShort = "Nebensätze",
            description = "Nebensätze werden eingeleitet durch: dass (dass), ob (ob), weil (weil), wenn (wenn), als (als), bevor (bevor), damit (damit), obwohl (obwohl). Das Verb steht am Satzende.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 5,
            quizCount = 5
        ),
        Subject(
            id = "a2_06",
            level = "A2",
            name = "6. Reflexive Verben (sich freuen, sich erinnern, sich befinden)",
            nameShort = "Reflexive Verben",
            description = "Reflexive Verben: sich freuen über (+A), sich erinnern an (+A), sich befinden in (+D), sich ärgern über (+A), sich interessieren für (+A). Das Reflexivpronomen richtet sich nach der Person und Kasus.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 6,
            quizCount = 5
        ),
        Subject(
            id = "a2_07",
            level = "A2",
            name = "7. Imperativ (Mach! Macht! Machen Sie!)",
            nameShort = "Imperativ",
            description = "Der Imperativ wird verwendet um Anweisungen zu geben: du-Form (Mach!), ihr-Form (Macht!), Sie-Form (Machen Sie!). Der Imperativ wird vor allem in informellen und formellen Kontexten verwendet.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 7,
            quizCount = 5
        ),
        Subject(
            id = "a2_08",
            level = "A2",
            name = "8. Plusquamperfekt (hatte gemacht, war gegangen)",
            nameShort = "Plusquamperfekt",
            description = "Das Plusquamperfekt beschreibt Handlungen, die vor einer anderen vergangenen Handlung stattfanden. Struktur: hatte/war + Partizip II. Es wird oft mit Präteritum oder Perfekt verwendet.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 8,
            quizCount = 5
        ),
        Subject(
            id = "a2_09",
            level = "A2",
            name = "9. Relativsätze (der, die, das, wer, was)",
            nameShort = "Relativsätze",
            description = "Relativsätze werden mit der/die/das eingeleitet und geben zusätzliche Informationen über ein Nomen. Das Verb steht am Ende des Relativsatzes. Die Relativpronomen richten sich nach dem Kasus des Verbs.",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 9,
            quizCount = 5
        ),
        Subject(
            id = "a2_10",
            level = "A2",
            name = "10. Konjunktionen (und, aber, oder, denn, sondern, deshalb, trotzdem)",
            nameShort = "Konjunktionen",
            description = "Die wichtigsten Konjunktionen: und (und), aber (aber), oder (oder), denn (denn), sondern (sondern), deshalb (deshalb), trotzdem (trotzdem), daher (daher), außerdem (außerdem).",
            category = Constants.Categories.GRAMMAR,
            iconEmoji = "📝",
            order = 10,
            quizCount = 5
        )
    )'''

# Replace the first getA2Subjects block (which currently only has a2_01)
# Find the block: from "    private fun getA2Subjects()" to "    )\n\n    private fun getA1Subjects"
old_start = content.find('    private fun getA2Subjects(): List<Subject> = listOf(\n        Subject(\n            id = "a2_01"')
old_end = content.find('\n    )\n\n    private fun getA1Subjects', old_start)
if old_start >= 0 and old_end >= 0:
    old_block = content[old_start:old_end + len('\n    )\n\n    private fun getA1Subjects')]
    content = content.replace(old_block, a2_subjects + '\n\n    private fun getA1Subjects', 1)
    print("✅ Replaced first getA2Subjects with 10-topic version")
else:
    print("⚠️  Could not find first getA2Subjects block to replace")

with open(FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("\n✅ All fixes applied!")

# Verify
with open(FILE, "r") as f:
    verify = f.read()
a2_count = verify.count('            id = "a2_')
print(f"A2 subject count in file: {a2_count}")
EOF