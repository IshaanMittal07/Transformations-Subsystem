import os
import pandas as pd

class Molecule:

    atoms: list[str]

    def __init__(self, name: str, filePath: str):
        self.name: str = name
        self.filePath: str = filePath
        self.positions: pd.DataFrame = self._readXYZ(filePath)

    def _readXYZ(self, filePath: str):
        """_readXYZ(self, filePath : str)

        Extracts the Atom type and XYZ Coordinates from a `.xyz` file, returns the structure as a Pandas Dataframe

        Parameters:
            filePath (str) - The path to the XYZ File to load

        Returns:
            pd.Dataframe - Pandas Dataframe containing the following Columns, [Atom, X, Y, Z], where XYZ are the Positions
        """

        if not os.path.exists(filePath):
            raise FileNotFoundError(f"The file located at {filePath} does not exist")

        return pd.read_csv(
            filePath,
            sep=r"\s+",
            skiprows=2,
            names=["Atom", "X", "Y", "Z"],
            engine="python",
        )
        
    def getContent(self) -> str:
        return self.positions.to_string(header=False, index=False)
        
