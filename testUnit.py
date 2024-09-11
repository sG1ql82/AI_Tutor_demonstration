from Unit import Unit
from Skill import Skill
"""
algebra = Unit("Solving algebra equations")

algebra.setSkills([Skill("Solving linear equations"),
                  Skill("Solving quadratic equations by factoring"),
                  Skill("Solving 2-variable linear systems"),
                  Skill("Algebra word problems")]
                )
prompt = ("Choose which skill you want to learn by entering the name of the skill:\n\n")

for skill in algebra.getSkills():
    prompt += "-" + skill.getTitle() + "\n"


skill = algebra.getSkill(input(prompt))

skill.tutor()
"""

"""
physics = Unit("Basics of calculus")

physics.generateSkillsTitle()

skillList = physics.getSkills()

for skill in physics.getSkills():
    print("-" + skill.getTitle() + "\n")
"""
