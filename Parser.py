# @Author Simon Geertsema
# Code to parse text


# Variables 
base_path = r"C:\Users\Paul\OneDrive\Documents\ML projects\AI Learning"
file_name = "MATH140Info2024.pdf"
  
# Concatenate for file path
file_path = base_path + "/" + file_name 

import PyPDF2

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

# Example usage
with open(file_path, 'rb') as file:
    pdf_content = pdf_to_string(file)
    print(pdf_content)