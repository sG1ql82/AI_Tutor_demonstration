from Skill import Skill
from Unit import Unit
#linearEQ = Skill("Mathematical proof by induction")
#linearEQ.generateExplanation()
#linearEQ.setUse4o(False)

#print(linearEQ.getExplanation())

#print(linearEQ)

#linearEQ.generateQuestionBank()

#linearEQ.tutor()

algebra = Unit("Solving algebra equations")

algebra.setSkills([Skill("Solving linear equations"),
                  Skill("Solving quadratic equations by factoring"),
                  Skill("Solving 2-variable linear systems"),
                  Skill("Algebra word problems")]
                )


algebra.teachSkill("Solving 2-variable linear systems")



"""
while True:
    print(linearEQ.generateQuestion())

    answer = input("Enter answer here, or \"quit\" to exit")

    if answer == "quit":
        break

    print(linearEQ.answerQuestion(answer))
    print(linearEQ.markQuestion())
    print(linearEQ.getMasteryLevel())
"""

