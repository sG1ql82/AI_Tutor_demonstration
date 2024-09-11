
import GPT
import random

class Skill:
    ## Initializes a instance of a skill to be taught by ChatGPT as part of an online course
    def __init__(self, title):
        self.title: str = title
        self.masteryLevel: int = 0
        self.answerHistory = []
        self.explanation = ""
        self.use4o = False
        self.questionBank = []
        self.lastResponse = ""
        self.lastQuestionSolution = ""
        
    
    #Checks if an explanation has been generated, and if not generates an overview of the skill to be displayed, using the chatGPT API
    def generateExplanation(self):
        if self.explanation == "":
            system = """You are to generate an explanation of how to do the following academic skill for part of an online course, assuming the relevant prior background. 
            Use an example problem to aid in your explanation but do not generate further examples for practice."""
            user = self.getTitle()
            self.explanation = GPT.getResponse(system, user, use4o = self.use4o)
    
    #Mutator for explanation
    def setExplanation(self, explanation):
        self.explanation = explanation

    #Accessor for explanation
    def getExplanation(self) -> str:
        return self.explanation

    #Uses ChatGPT to generate a question
    def generateQuestionBank(self, temperature = 1.3) -> str:
        system = "I want you to generate 5 questions on the topic provided." 
        questions = GPT.getResponse(system, user = self.title, use4o = self.use4o)
        system2 = "Take the following 5 questions and format them as a python list. Do not include any additional text and explanations - start with the opening [, and remember to include the closing bracket ]. Do not include additional text after the last closing bracket."
        qList = GPT.getResponse4oMini(system2, user = questions)
        qList = qList[qList.index('['):]
        try:
            self.questionBank = eval(qList)
            random.shuffle(self.questionBank)
        except:
            print("An error occured in generating qList" + str(qList))
    
    def tutor(self):
        self.generateQuestionBank()
        for question in self.questionBank:
                self.lastQuestion = question
                response = input(question)
                
                if response == "quit":
                    break
                print(self.answerQuestion(response))
                print(self.markQuestion())
                print(self.getMasteryLevel())

    
    
    #Uses ChatGPT to mark a question
    def answerQuestion(self, response, temperature = 0.5) -> str:
        self.lastResponse = response
        system = f"""You are to explain the correct solution and provide relevant feedback to answer to the following question delimited by square brackets: [{self.lastQuestion}]. 
        The student's answer does not need to show detailed working, and you should answer in a clear and technically correct manner. """
        output: str = GPT.getResponse(system, user = self.lastResponse, use4o = self.use4o)
        self.lastQuestionSolution = output
        
        return output
    
    def markQuestion(self, temperature = 0.5) -> bool:
        mark = False
        system = f"""You will be provided with the solution to a question. Deterimine if the student's solution is correct, allowing some room for error. 
        Output the string True if it is correct, or false otherwise. The correct solution is: {self.lastQuestionSolution}"""
        response: str = GPT.getResponse(system, user = self.lastResponse, use4o = False)
        try:
            mark = eval(response)
        except:
            print("Error, response not interpreted, assumed incorrect")
        if self.lastResponse == "":
            mark = False
        self.answerHistory.append(mark)
        self.updateMasteryLevel()
        return mark
    
    def updateMasteryLevel(self):
        if self.masteryLevel == 0:
            threeCorrect: bool = True
            if len(self.answerHistory) >= 3:
                for i in range(len(self.answerHistory) - 4, len(self.answerHistory) - 1):
                    if not self.answerHistory[i]:
                        threeCorrect = False
            else:
                threeCorrect = False            
            if threeCorrect:
                self.masteryLevel = 1
    
    def getQuestionBank(self):
        return self.questionBank

    def getMasteryLevel(self):
        return self.masteryLevel
    
    def getTitle(self):
        return self.title
    
    def setUse4o(self, use4o: bool):
        self.use4o = use4o
    
    def __str__(self):
        return f"{self.title}\n\nExplanation: {self.explanation}\n\nMastery Level: {self.masteryLevel}"





    
            
        

        

