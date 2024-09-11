import pickle

with open('testSkill1.pkl', 'rb') as f:
    qSkill = pickle.load(f)

    print(qSkill.getAnswerHistory())

    qSkill.updateAnswerHistory(True)

    print(qSkill.getAnswerHistory())
