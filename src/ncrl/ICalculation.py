import os
from abc import ABC, abstractmethod
from .InputFile import InputFile

class ICalculation(ABC):
    
    def __init__(self, inputFile : InputFile):
        self.baseCachePath = os.path.join(os.getcwd(), "Cache")
        self.inputFile = inputFile
        pass
    
    @abstractmethod
    def calculate(self):
        pass
    
    def setup(self):
        if (not os.path.exists(self.baseCachePath)):
            os.mkdir(self.baseCachePath)
            
    def getInputFileName(self):
        return self.inputFile.name + self.inputFile.extension
    
    def getOutputFileName(self):
        return self.inputFile.name + ".out"
        
        
