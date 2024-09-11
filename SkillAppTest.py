import streamlit as st
from quantitativeSkill import quantitativeSkill
import pickle
import sys

if 'opened' not in st.session_state:
    st.session_state.opened = False

# Load the skill object into session state if not already loaded
def tutor(filename: str):
    if 'qSkill' not in st.session_state:
        with open(filename, 'rb') as f:
            st.session_state.qSkill = pickle.load(f)

    # Initialize other session state variables
    if 'count' not in st.session_state:
        st.session_state.count = -1

    if 'response' not in st.session_state:
        st.session_state.response = ""

    # Set the title of the webpage
    st.title(st.session_state.qSkill.getTitle())

    # Display some informational text
    st.write(st.session_state.qSkill.getExplanation())

    st.subheader("Problems")

    # Function to generate a new question
    def newQuestion():
        ## Make new questions and reset count if you run out of questions
        st.session_state.count += 1
        if st.session_state.count > 4:
            st.session_state.qSkill.generateQuestionBank()
            st.session_state.count = 0

        ## Set new question
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
            if st.session_state.qSkill.getNumeric() == False:
                st.markdown(st.session_state.qSkill.getLastQuestionSolution())
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
            #print("Updating with True")  # Debugging print statement
            st.session_state.qSkill.updateAnswerHistory(True)

        def update_false():
            #print("Updating with False")  # Debugging print statement
            st.session_state.qSkill.updateAnswerHistory(False)

        # Use checkboxes with callback functions
        st.write("Select the checkbox corresponding to whether your answer was true or false.")
        st.checkbox("True", key="true_checked", on_change=update_true)
        st.checkbox("False", key="false_checked", on_change=update_false)

        # Additional debugging to check session states
        #print("True checkbox state:", st.session_state.true_checked)
        #print("False checkbox state:", st.session_state.false_checked)

    def clear_text():
        st.session_state["input"] = ""

    # Button to generate a new question
    if st.button("New Question"):
        clear_text()
        newQuestion()
    

    ## initialize webpage containers as qSkill data fields
    question = st.session_state.qSkill.getQuestionBank()[st.session_state.count]
    st.session_state.qSkill.setLastQuestion(st.session_state.qSkill.getQuestionBank()[st.session_state.count])


    answer = st.session_state.qSkill.getLastResponse()

    questionSolution = st.session_state.qSkill.getLastQuestionSolution()

    ## catch IndexOutOfRange and display false as list is empty
    try:
        mark = st.session_state.qSkill.getAnswerHistory()[-1]
    except:
        mark = False

    # Display the current question
    st.markdown(question)

    # Text input for answer, triggers action on change
    LastR = st.session_state.qSkill.getLastResponse()


    st.session_state.response = st.text_input("Enter answer here, or 'quit' to exit:", key = "input")


    if(st.session_state.response != ""):
        st.session_state.qSkill.setLastResponse(st.session_state.response)  # Automatically call markQuestion when text is input

    if LastR != st.session_state.qSkill.getLastResponse():
        markQuestion()


    if(st.session_state.response != ""):
        st.markdown(questionSolution)
        st.write("Your solution: " + st.session_state.qSkill.getLastResponse())
        if mark == True:
            st.write("Correct")
        elif mark == False:
            st.write("Incorrect")

    if st.session_state.qSkill.getQCorrect() == 1:
        st.write(str(st.session_state.qSkill.getQCorrect()) + " question correct in a row out of 3 required for mastery")
    else:
        st.write(str(st.session_state.qSkill.getQCorrect()) + " questions correct in a row out of 3 required for mastery")

    st.progress(float(min(st.session_state.qSkill.getQCorrect() / 3, 1.0)))

    if st.session_state.qSkill.getMastered():
        st.write("You managed to get 3 questions correct in a row, skill mastered!")

    # Call the manual mark function if an error occurred
    #inputMark()

# Only display the selectbox if the tutor has not been opened yet
if not st.session_state.opened:
    # Create a placeholder for the selectbox
    selectbox_placeholder = st.empty()

    # Create the selectbox with None as default and a placeholder
    subject = selectbox_placeholder.selectbox(
        "Choose which skill you want to practice:",
        [None, "Factoring expressions", "Differentiating polynomials", 
        "Momentum conservation", "Linear equations", "Projectile motion", "Adding fractions"],
        format_func=lambda x: 'Select a topic...' if x is None else x
    )

    if subject is not None:
        st.session_state.opened = True
        st.session_state.selected_subject = subject
        selectbox_placeholder.empty()
        tutor(st.session_state.selected_subject)
else:
    tutor(st.session_state.selected_subject)
        
        
        