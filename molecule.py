from rdkit import Chem
from rdkit.Chem import AllChem
def create_molecule(smiles):
    mol = Chem.MolFromSmiles(smiles)
    return mol
def generate_3d(mol):
    mol = Chem.AddHs(mol)
    AllChem.EmbedMolecule(mol)
    AllChem.MMFFOptimizeMolecule(mol)
    return mol