import re
import os
from abc import ABC

class InputFile(ABC):
    
    def __init__(self, name : str):
        
        if (not isinstance(name, str)):
            raise TypeError("The name of the Input File must be a string")
        
        self.name = name
        self._header : str = ""
        self._footer : str = ""
        self._structures : list[str] = []
    
    def compile(self, template : str, **args):
        
        pattern = r"&\{(\w+)\}"
        keys = re.findall(pattern, template)
        
        # Add a Checker for all the Variables you need to input
        if (len(keys) == 0):
            return template
        
        # Replace the Variables / Keys
        #if (len(keys) != len(args.keys)):
        #    raise ValueError("Number of Keys do not match the Number of Arguments provided")

        for key in keys:
            if (key not in args):
                raise ValueError(f"Key {key} is not found in Arguments")
            
            template = template.replace(f"&{{{key}}}", args[key])
            
        return template 
        
    def setHeader(self, header: str = None, **args):
        self._header = self.compile(header, **args)
    
    def setFooter(self, footer : str = None, **args):
        self._structures.append(self.compile(footer, **args))
    
    def addStructure(self, structure : str = None, **args):
        self._structures.append(self.compile(structure, **args))
    
    def build(self) -> str:
        fileContent = self._header + "\n"
        
        for line in self._structures:
            fileContent += line + "\n"
            
        fileContent += self._footer
        
        return fileContent
    
    def save(self, filePath):
        
        with open(os.path.join(filePath, self.name + ".inp"), 'w') as f:
            f.write(self.build())
        
        
        # Save to the Cachae 
        