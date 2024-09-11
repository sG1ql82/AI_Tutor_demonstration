# @ Author Simon Geertsema 21/07/23
# Draft OpenAI API backend
#

from openai import OpenAI
from dotenv import load_dotenv
import json
import PyPDF2
import os


## Set the virtual environment
load_dotenv("/Users/Paul/OneDrive/AI/AI Tutoring/.env")

client = OpenAI()

# File variables
# /Users/simongeertsema/Library/CloudStorage/OneDrive-Personal/Documents/ML projects/AI Learning
base_path = r"C:\Users\Paul\OneDrive\AI/AI Tutoring"
file_name = "FINC102.pdf"
#COMP162_CourseOutline.pdf
#MATH140Info2024.pdf
#FINC102_Business Mathematics.pdf

# Concatenate for file path
file_path = base_path + "/" + file_name 

def pdf_to_string(file):
    # Initialize a PDF reader object
    pdf_reader = PyPDF2.PdfReader(file)

    # Initialize an empty string to store the content
    pdf_text = ""
    
    # Iterate through each page and extract text
    for page_num in range(len(pdf_reader.pages)):
        # Get the page
        page = pdf_reader.pages[page_num]
        # Extract text from the page and add it to the pdf_text string
        pdf_text += page.extract_text()
        
    return pdf_text

# Open file
with open(file_path, 'rb') as file:
    pdf_content = pdf_to_string(file)

    # Run course summary through GPT4o
    MODEL="gpt-4o"

    SYSTEM_PROMPT = """ You are to provide a detailed summary of the academic content of the course given, which will be used to construct resources for students to learn.
    Firstly break down the course into a few key units. For each unit, write the relevant skills for the unit in the form ["skill1", "skill2", ... "skilln"] as python lists. Ignore course information like readings, academic policy, etc, and focus
    purely on the course curriculum. """

    completion = client.chat.completions.create(
      model=MODEL,
      messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": pdf_content},
      ]
    )
    print("Assistant: " + completion.choices[0].message.content)







