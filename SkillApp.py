import streamlit as st
from quantitativeSkill import quantitativeSkill
import pickle
import sys


# Load the skill object into session state if not already loaded
def tutor(filename: str, title_placeholder, explanation_placeholder, question_placeholder, input_placeholder):
    if 'qSkill' not in st.session_state:
        with open(filename, 'rb') as f:
            st.session_state.qSkill = pickle.load(f)

    # Initialize other session state variables
    if 'count' not in st.session_state:
        st.session_state.count = -1

    if 'response' not in st.session_state:
        st.session_state.response = ""

    # Clear and update the placeholders
    title_placeholder.empty()
    explanation_placeholder.empty()
    question_placeholder.empty()
    input_placeholder.empty()

    # Set the title of the webpage
    title_placeholder.title(st.session_state.qSkill.getTitle())

    # Display some informational text
    explanation_placeholder.write(st.session_state.qSkill.getExplanation())

    question_placeholder.subheader("Problems")

    # Function to generate a new question
    def newQuestion():
        # Make new questions and reset count if you run out of questions
        st.session_state.count += 1
        if st.session_state.count > 4:
            st.session_state.qSkill.generateQuestionBank()
            st.session_state.count = 0

        # Set new question
        st.session_state.qSkill.setLastQuestion(st.session_state.qSkill.getQuestionBank()[st.session_state.count])
        st.session_state.qSkill.setLastQuestionSolution("")
        st.session_state.qSkill.setLastResponse("")

    # Function to mark the current question
    def markQuestion():
        if st.session_state.qSkill.getLastResponse() == "quit":
            sys.exit()
        elif st.session_state.qSkill.getLastResponse() != "":
            st.session_state.qSkill.answerQuestion(st.session_state.qSkill.getLastResponse())
            st.session_state.qSkill.markQuestion()
            st.session_state.response = ""
            if not st.session_state.qSkill.getNumeric():
                question_placeholder.markdown(st.session_state.qSkill.getLastQuestionSolution())
                inputMark()
            else:
                st.rerun()

    def inputMark():
        # Initialize session state variables if not already present
        if 'true_checked' not in st.session_state:
            st.session_state.true_checked = False
        if 'false_checked' not in st.session_state:
            st.session_state.false_checked = False

        # Define callback functions to update answer history
        def update_true():
            st.session_state.qSkill.updateAnswerHistory(True)

        def update_false():
            st.session_state.qSkill.updateAnswerHistory(False)

        # Use checkboxes with callback functions
        question_placeholder.write("Select the checkbox corresponding to whether your answer was true or false.")
        question_placeholder.checkbox("True", key="true_checked", on_change=update_true)
        question_placeholder.checkbox("False", key="false_checked", on_change=update_false)

    def clear_text():
        st.session_state["input"] = ""

    # Button to generate a new question
    if question_placeholder.button("New Question"):
        clear_text()
        newQuestion()

    # Initialize webpage containers as qSkill data fields
    question = st.session_state.qSkill.getQuestionBank()[st.session_state.count]
    st.session_state.qSkill.setLastQuestion(st.session_state.qSkill.getQuestionBank()[st.session_state.count])

    answer = st.session_state.qSkill.getLastResponse()

    questionSolution = st.session_state.qSkill.getLastQuestionSolution()

    # Display the current question
    question_placeholder.markdown(question)

    # Text input for answer, triggers action on change
    st.session_state.response = input_placeholder.text_input("Enter answer here, or 'quit' to exit:", key="input")

    if st.session_state.response != "":
        st.session_state.qSkill.setLastResponse(st.session_state.response)

    if st.session_state.qSkill.getLastResponse() != "":
        markQuestion()
        question_placeholder.markdown(questionSolution)
        question_placeholder.write("Your solution: " + st.session_state.qSkill.getLastResponse())

        try:
            mark = st.session_state.qSkill.getAnswerHistory()[-1]
            if mark:
                question_placeholder.write("Correct")
            else:
                question_placeholder.write("Incorrect")
        except IndexError:
            pass

    question_placeholder.progress(min(st.session_state.qSkill.getQCorrect() / 3, 1.0))

    if st.session_state.qSkill.getMastered():
        question_placeholder.write("You managed to get 3 questions correct in a row, skill mastered!")


# Initialize session state for tracking the selected subject and stopping flag
if 'current_subject' not in st.session_state:
    st.session_state.current_subject = None

# Create placeholders for various components
title_placeholder = st.empty()
explanation_placeholder = st.empty()
question_placeholder = st.empty()
input_placeholder = st.empty()

# Create the selectbox with None as default and a placeholder
subject = st.selectbox(
    "Choose which skill you want to practice:",
    [None, "Factoring expressions", "Differentiating polynomials", 
     "Momentum conservation", "Linear equations", "Projectile motion"],
    format_func=lambda x: 'Select a topic...' if x is None else x
)

# If a new subject is selected
if subject != st.session_state.current_subject:
    # Update the current subject
    st.session_state.current_subject = subject

    # Clear and restart the tutor function for the new subject
    if subject is not None:
        tutor(subject, title_placeholder, explanation_placeholder, question_placeholder, input_placeholder)
