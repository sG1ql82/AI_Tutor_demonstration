from abc import ABC, abstractmethod

class abstractSkill(ABC):
    def __init__(self, title: str, explanation: str = "", prompt: str = ""):
        self.title: str = title
        self.prompt = prompt
        self.explanation = ""
        self.mastered: bool = False
        self.answerHistory = []
        self.use4o = False
        self.questionBank = []
        self.lastQuestion = ""
        self.lastResponse = ""
        self.lastQuestionSolution = ""
    
    @abstractmethod
    def generateExplanation(self):
        pass
    
    def setExplanation(self, explanation:str):
        self.explanation = explanation
   
    def getExplanation(self):
        return self.explanation
    
    def generateQuestionBank(self):
        pass
    
    @abstractmethod 
    def answerQuestion(self):
        pass
    
    @abstractmethod 
    def markQuestion(self):
        pass
    
    def updateAnswerHistory(self, mark: bool):
        self.answerHistory.append(mark)
        if not self.mastered:
            if self.getQCorrect() >= 3:
                self.mastered = True
  
    
    def getQCorrect(self):
        qCorrect: int = 0
        for i in range(len(self.answerHistory)):
            if self.answerHistory[i]:
                qCorrect += 1
            else:
                qCorrect = 0
        return qCorrect
            
        
        
            
    def getQuestionBank(self):
        return self.questionBank
    
    def getLastQuestionSolution(self):
        return self.lastQuestionSolution
    
    def getLastQuestion(self):
        return self.lastQuestion
    
    def getLastResponse(self):
        return self.lastResponse
    
    def getAnswerHistory(self):
        return self.answerHistory

    def getMastered(self):
        return self.mastered
    
    def getTitle(self):
        return self.title
    
    def setUse4o(self, use4o: bool):
        self.use4o = use4o

    def setLastResponse(self, response:str):
        self.lastResponse = response

    def setLastQuestion(self, question:str):
        self.lastQuestion = question
    
    def setLastQuestionSolution(self, solution:str):
        self.lastQuestionSolution = solution
    


    def __str__(self):
        return f"{self.title}\n\nExplanation: {self.explanation}\n\nMastered: {self.mastered}"

