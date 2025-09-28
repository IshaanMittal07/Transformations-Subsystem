import subprocess

class DockerEngine:
    
    def __init__(self, name : str, imageName : str, cachePath):
        self.name = name
        self.imageName = imageName
        self.cachePath = cachePath
    
    def run(self, command):
        fullCommand = f'docker run --name {self.name} -v "{self.cachePath}":/home/orca {self.imageName} {command}'
        
        self.remove()
        self.runCommand(fullCommand)
        self.remove()
        
    def runCommand(self, command):
        subprocess.run(
            command, 
            shell=True,
            stderr=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
        )
        
    def remove(self):
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
