from Unit import Unit
import GPT
import PyPDF2


class Course:
    def __init__(self, title):
        self.title = title
        self.units = []
        self.progress:float = 0
        self.masteryLevel = 0
        self.summary = ""
        self.unitsSummary = list[str]
    
    def setUnits(self, units):
        self.units = units
    
    def getUnit(self, unitName):
        for unitN in self.units:
            if unitN.getTitle() == unitName:
                return unitN
        print("Error, unit not found")

    def addUnit(self, unit):
        self.units.append(unit)

    def pdf_to_string(self, file_path, file_name):
        # Initialize a PDF reader object
        file_path = file_path + file_name
        with open(file_path, 'rb') as file:
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
    
    def generateSummary(self, outline):
        system = """Read the following course outline and provide a summary of the units of the course and key skills for each unit. Number the units as ### Unit 1, ### Unit 2,...
                 Ignore content like assessment policy, timetabling, and other material not relavent to the academic content of the course"""
        user = outline
        output = GPT.getResponse4o(system = system, user = user)
        self.summary = output
        self.unitsSummary = self.splitString(input = output, delimiter = "### Unit")
        self.unitsSummary = [s for s in self.unitsSummary if s.startswith("### Unit")]


    
    def generateUnits(self):
        system = """Read the following course summary and output a list of the titles of all the units in the course. Format your ourput as a python list, with each
                    unit in the form Unit 1: description, Unit 2: description..."""
        user = self.summary
        output = GPT.getResponse4o(system = system, user = user)
        try:
            unitList  = eval(output[output.index('[') : output.index(']') + 1])
        except:
            print("Error in evaluating list of units")

        for unitString in unitList:
            unit = Unit(unitString)
            self.addUnit(unit)
        

    def splitString(self, input, delimiter):
        result = []
        parts = input.split(delimiter)
        
        # Iterate over parts and add the delimiter back to the beginning of each part except the first
        for i, part in enumerate(parts):
            if i == 0:
                if part:  # if the first part is not empty
                    result.append(part)
            else:
                result.append(delimiter + part)  
        return result
    
    def initializeUnit(self, unitNumber: int):
        index = unitNumber - 1
        unitSummary = self.unitsSummary[index]
        self.units[index].generateSkills(unitSummary)
        return(self.units[index])
    
    def getUnits(self):
        return self.units

    def getSummary(self):
        return self.summary
    
    def getUnitsSummary(self):
        return self.unitsSummary
    
    def getTitle(self):
        return self.title
    


