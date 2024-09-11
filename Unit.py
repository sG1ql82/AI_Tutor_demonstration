
from Skill import Skill
import GPT

class Unit:
    def __init__(self, title):
        self.title: str = title
        self.masteryLevel: int = 0
        self.progress: float = 0
        self.skills = []
    
    def setSkills(self, skills):
        self.skills = skills
    
    def addSkill(self, skill):
        self.skills.append(skill)

    def generateSkillsTitle(self):
        system = "Generate 3-5 key skills relevant to the following unit. Format your output as a python list"
        user = self.title
        skillStr = GPT.getResponse4o(system = system, user = user)
        try:
            skills  = eval(skillStr[skillStr.index('[') : skillStr.index(']') + 1])
        except:
            print("Error in evaluating list of skills")

        for skillString in skills:
            skill = Skill(skillString)
            self.addSkill(skill)

    def generateSkills(self, skillSummary: str):
        system = """Read the summary of the following unit and output the key skills in the unit in the format of a python list, with each skill as an entry in the list."
                Make each skill title specific and detailed."""
        user = skillSummary
        skillStr = GPT.getResponse4o(system = system, user = user)
        try:
            skills  = eval(skillStr[skillStr.index('[') : skillStr.index(']') + 1])
            for skillString in skills:
                skill = Skill(skillString)
                self.addSkill(skill)
        except:
            print("Error in evaluating list of skills")

        


    def getSkills(self):
        return self.skills
    
    def getSkill(self, skillName):
        for skillN in self.skills:
            if skillN.getTitle() == skillName:
                return skillN
        print("Error, skill not found")

    def teachSkill(self, skillName):
        for skillN in self.skills:
            skill = None
            if skillN.getTitle() == skillName:
                skill = skillN
                skill.generateExplanation()
                print(skill.getExplanation())
                skill.tutor()
                break
        if skill == None:
            print("Error, skill not found")

    def updateProgress(self):
        mastery = 0
        total = 0
        for sk in self.skills:
            if sk.getMasteryLevel() == 1:
                mastery += 1
            total += 1
        self.progress = total/mastery
        if self.progress == 1:
            self.masteryLevel = 1
        
    
    def getProgress(self):
        return self.progress
    
    def getTitle(self):
        return self.title
    
    def getMasteryLevel(self):
        return self.masteryLevel
    
    
            



    
