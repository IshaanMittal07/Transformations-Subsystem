import os
from .ICalculation import ICalculation
from .InputFile import InputFile

class OrcaCalculation(ICalculation):
    
    def __init__(self, inputFile : InputFile):
        super().__init__(inputFile)
        self.cachePath = os.path.join(self.baseCachePath, "Orca", inputFile.name)
        
    def calculate(self):
        self.setup()
        
        print(f"Running Calculation using the following Input File : \n {self.inputFile.build()}")
        
        # Create a On Location Calculation follow the local function in QChem
        
        
        print("Calculation Finished!")
        
        return super().calculate()
    
    def setup(self):
        super().setup()
        
        if (not os.path.exists(self.cachePath)):
            os.makedirs(self.cachePath)
        
        self.inputFile.save(self.cachePath)    
       