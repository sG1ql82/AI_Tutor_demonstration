from quantitativeSkill import quantitativeSkill
import pickle
import sys

"""
with open('testSkill1.pkl', 'rb') as f:
    qSkill = pickle.load(f)
"""

with open('testSkill2.pkl', 'rb') as f:
    qSkill = pickle.load(f)

#print(qSkill)


while True:
    for question in qSkill.getQuestionBank():
        qSkill.setLastQuestion(question) 
        print("\n" + question + "\n")

        answer = input("Enter answer here, or \"quit\" to exit\n\n")
        if answer == "quit":
            sys.exit()

        print(qSkill.answerQuestion(answer) +"\n\n")


        qSkill.markQuestion()
    
            

        print("Mark: " + str(qSkill.getAnswerHistory()[-1]) + "\n")
        """
        try:
            mark = input("Enter whether you got the answer correct as True or False")
            qSkill.updateAnswerHistory(eval(mark))
        except:
            print("Answer must be 'True' or 'False'")
        """

        print(qSkill.getAnswerHistory())


