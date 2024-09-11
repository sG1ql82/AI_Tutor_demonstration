
from abstractSkill import abstractSkill
import GPT
import random
import math
import re

class quantitativeSkill(abstractSkill):
    def __init__(self, title: str, explanation: str = "", prompt: str = "", numeric: bool = False):
        super().__init__(title, explanation, prompt)
        self.numeric = numeric
    
    def generateExplanation(self):
        if self.explanation == "":
            system = """You are to generate an explanation of how to do the following academic skill for part of an online course, assuming the relevant prior background. 
            The prompt for generating questions will be provided, and you are to explain how to solve questions of that type
            Use an example problem to aid in your explanation but do not generate further examples for practice. Wrap inline equations and expressions in "$" and full line
            equations in "$$", so they can be displayed with proper formatting using markdown."""
            user = self.prompt
            self.explanation = GPT.getResponse(system, user, use4o = self.use4o)
    
    #Uses ChatGPT to generate a question
    def generateQuestionBank(self, temperature = 1.3) -> str:
        if(self.prompt == ""):
            raise Exception("No prompt provided")
        system = "I want you to generate 5 questions according to the prompt provided" 
        questions = GPT.getResponse(system, user = self.prompt, use4o = self.use4o)
        system2 = """Take the following 5 questions and format them as a python list. Do not include any additional text and explanations, and avoid including the answer. 
        Use single dollar signs ($) to wrap equations so they can be rendered using markdown, Start with the opening [, and remember to include the closing bracket ]. 
        Do not include additional text after the last closing bracket."""

        qList = GPT.getResponse4oMini(system2, user = questions)
        qList = qList[qList.index('['):]
        try:
            self.questionBank = eval(qList)
            random.shuffle(self.questionBank)
        except:
            print("An error occured in generating qList\n" + str(qList))
    
    def answerQuestion(self, response, temperature = 0.5) -> str:
        self.lastResponse = response
        system = f"""You are to provide a clear worked solution to the following problem delimited by square brackets. 
        Wrap inline equations and expressions in "$", and full-line equations in "$$" so they can be rendered correctly using markdown.
        Please write the final answer enclosed in ###, ignoring any units or other additional symbols: [{self.lastQuestion}]"""
        output: str = GPT.getResponse(system, user = self.lastResponse, use4o = self.use4o)
        self.lastQuestionSolution = output
        
        return output

    ## Throws error, needs to be caught
    def markQuestion(self, temperature = 0.5) -> bool: ## Throws an exception if answer is not numeric, which must be caught and handled appropriately
        if self.numeric:
            response = ""
            mark = False
            print(self.lastQuestionSolution)
            match = re.search(r'###(.*?)###', self.lastQuestionSolution)
            response =  match.group(1).strip()
            
            print(self.lastResponse)
            answer = float(response)
            print(answer)
            print(abs(float(self.lastResponse) - answer) <= abs(answer / 50))

            if abs(float(self.lastResponse) - answer) <= abs(answer / 50):
                mark = True
                
            self.updateAnswerHistory(mark)
            return mark
        else:
            return None

    def getNumeric(self):
        return self.numeric
        """
        except:
            print("non numeric solution")
            raise Exception("Solution non-numeric, requires exception to be caught and manual marking from student")
        
"""            
        
        
    

    
