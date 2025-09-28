from .ICalculation import ICalculation
from .InputFile import InputFile
from .DockerEngine import DockerEngine
import os
import subprocess

class OrcaCalculation(ICalculation):
    
    def __init__(self, inputFile : InputFile):
        super().__init__(inputFile)
        self.cachePath = os.path.join(self.baseCachePath, "Orca", inputFile.name)
        
    def calculate(self):
        self.setup()
        
        print("Running Calculation")
        
        dockerEngine = DockerEngine("orca", "mrdnalex/orca", self.cachePath)
        
        dockerEngine.run(f'sh -c "cd /home/orca && /Orca/orca {self.getInputFileName()} > {self.getOutputFileName()}"')
        
        print("Calculation Finished!")
        
        return super().calculate()
    
    def setup(self):
        super().setup()
        
        if (not os.path.exists(self.cachePath)):
            os.makedirs(self.cachePath)
        
        self.inputFile.save(self.cachePath)    
        
    
    