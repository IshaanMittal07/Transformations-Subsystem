import subprocess

class OrcaDockerEngine:
    
    def __init__(self, calcFileName : str, cachePath : str, ):
        """Constructor for OrcaDockerEngine
        
        Initializes a new Instance of the Engine. Used to run a Orca Calculation inside a Docker Container
        
        Parameters:
            calcFileName (str) - The name of the Calculation, used to name the Input file and Output file
            cachePath (str) - The path to the Cache Folder where the Input, Output and other Calculation files are outputted
        """
        self.name = "ncrlorca"
        self.imageName = "mrdnalex/orca"
        self.cachePath = cachePath
        self.calcFileName = calcFileName
    
    def run(self):
        """run(self, command : str)
        
        Runs the Orca Calculation through a Docker Container and cleans itself up
        """
        fullCommand = f'docker run --name {self.name} -v "{self.cachePath}":/home/orca {self.imageName} sh -c "cd /home/orca && /Orca/orca {self.calcFileName}.inp > {self.calcFileName}.out"'
        
        self._remove()
        
        subprocess.run(
            fullCommand, 
            shell=True,
            stderr=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
        )
        
        self._remove()
        
    def _remove(self):
        """_remove(self)
        
        Stops and Removes the Docker Container if it's running
        """
        subprocess.run(
            f"docker kill {self.name}",
            shell=True,
            stderr=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
        )
        subprocess.run(
            f"docker rm {self.name}",
            shell=True,
            stderr=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
        )