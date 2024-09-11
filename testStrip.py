import re

def extract_answer(text):
    # Regular expression to find text between ###
    match = re.search(r'###(.*?)###', text)
    
    if match:
        # Return the extracted answer (without ###)
        return match.group(1)  # No need for strip unless you expect extra whitespace
    else:
        return None

# Example usage
solution_text = "The derivative of the polynomial at x = 3 is 12. ###12###"
answer = extract_answer(solution_text)

print(f"Extracted answer: {answer}")