from Course import Course
import pickle

FINC102 = Course("FINC102: Business Mathematics")

base_path = r"/Users/simongeertsema/Library/CloudStorage/OneDrive-Personal/AI/AI_Tutoring/"
file_name = "FINC102.pdf"

course_outline = FINC102.pdf_to_string(file_path = base_path, file_name = file_name)

print(course_outline)

FINC102.generateSummary(course_outline)
FINC102.generateUnits()

print(FINC102.getSummary())

with open('FINC102.pkl', 'wb') as f:
    pickle.dump(FINC102, f)

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