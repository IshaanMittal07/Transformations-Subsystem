from .InputFile import InputFile
from .Molecule import Molecule

class OrcaInputFile(InputFile):

    MOLECULE_INPUT: str = "* xyz 0 1 \n&{molecule}\n*"
    BASIC = "!&{calculation} &{basis} &{functional}"

    def __init__(self, name : str,  molecule: Molecule):
        super().__init__(name, ".inp")

        if not isinstance(molecule, Molecule):
            raise TypeError("The Molecule passed in is not of Type Molecule!")

        self.addStructure(self.MOLECULE_INPUT, molecule=molecule.getContent())
    
    def setHartreeFock(self, basis : str, functional : str):
        self.setHeader(self.BASIC, basis = basis, functional = functional, calculation = "HF")
