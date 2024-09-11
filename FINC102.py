import pickle

with open('FINC102.pkl', 'rb') as f:
    FINC102 = pickle.load(f)

print(FINC102.getUnitsSummary())

print("Enter the number of the unit you want to study\n")
for unit in FINC102.getUnits():
    print("-" + unit.getTitle() + "\n")

unitN = int(input())

unit = FINC102.initializeUnit(unitN)

prompt = ("Enter the number of the skill you want to learn:\n\n")



for skill in unit.getSkills():
    prompt += "-" + skill.getTitle() + "\n"


input = int(input(prompt))

skill = unit.getSkills()[input-1]
skill.tutor()