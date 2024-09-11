import streamlit as st
from quantitativeSkill import quantitativeSkill
import pickle
import sys
import streamlit as st

with open('testSkill2.pkl', 'rb') as f:
    qSkill = pickle.load(f)

count = 0

# Set the title of the webpage
st.title(qSkill.getTitle())

# Display some informational text
st.write(qSkill.getExplanation())

st.subheader("Problems")

problem = st.empty()

answer = st.text_input("Enter answer here, or 'quit' to exit:")

solution = st.empty()

mark = st.empty()


def newQuestion(count, problem):
## make new questions and reset count if you run out of questions
    if count > 4:
        qSkill.generateQuestionBank()
        count = 0

    ## set new question and display it
    qSkill.setLastQuestion(qSkill.getQuestionBank()[count]) 
    problem = st.markdown(qSkill.getQuestionBank()[count])

    ## increment counter
    count = count + 1

def markQuestion(answer, solution, mark):
    if answer == "quit":
            sys.exit()
    else:
        solution = st.markdown(qSkill.answerQuestion(answer) +"\n\n")
        qSkill.markQuestion()

        mark = st.write("Mark: " + str(qSkill.getAnswerHistory()[-1]) + "\n")

if st.button("New Question"):
    newQuestion(count, problem)

if st.button("Mark Question"):
    markQuestion(answer, solution, mark)
     




    



