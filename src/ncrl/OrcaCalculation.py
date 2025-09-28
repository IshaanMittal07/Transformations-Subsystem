from .ICalculation import ICalculation
from .InputFile import InputFile
import os
import subprocess

class OrcaCalculation(ICalculation):
    
    def __init__(self, inputFile : InputFile):
        super().__init__(inputFile)
        self.cachePath = os.path.join(self.baseCachePath, "Orca", inputFile.name)
        
    def calculate(self):
        self.setup()
        
        print("Running Calculation")
        
        command = f'docker run --name qchemorca -v "{self.cachePath}":/home/orca mrdnalex/orca sh -c "cd /home/orca && /Orca/orca {self.getInputFileName()} > {self.getOutputFileName()}"'

        # Kill and Remove qchemorca container if it's leftover
        subprocess.run(
            f"docker kill qchemorca",
            shell=True,
            stderr=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
        )
        subprocess.run(
            f"docker rm qchemorca",
            shell=True,
            stderr=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
        )

        # Run the Calculation in a Container and wait
        result = subprocess.run(command, shell=True, text=True, capture_output=True)

        # Kill and Remove the Container
        subprocess.run(
            f"docker kill qchemorca",
            shell=True,
            stderr=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
        )
        subprocess.run(
            f"docker rm qchemorca",
            shell=True,
            stderr=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
        )
        
        print("Calculation Finished!")
        
        return super().calculate()
    
    def setup(self):
        super().setup()
        
        if (not os.path.exists(self.cachePath)):
            os.makedirs(self.cachePath)
        
        self.inputFile.save(self.cachePath)    
        
    
    