from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Crippen


def calculate_electrostatic_field(mol):
    AllChem.ComputeGasteigerCharges(mol)

    charges = []

    for atom in mol.GetAtoms():
        charge = atom.GetProp("_GasteigerCharge")
        charges.append(float(charge))

    return charges


def calculate_hydrophobic_field(mol):
    values = []

    atom_contributions = Crippen._GetAtomContribs(mol)

    for atom in mol.GetAtoms():
        contribution = atom_contributions[atom.GetIdx()][0]
        values.append(contribution)

    return values


def calculate_steric_field(mol):
    steric_values = []

    for atom in mol.GetAtoms():
        radius = Chem.GetPeriodicTable().GetRvdw(
            atom.GetAtomicNum()
        )
        steric_values.append(radius)

    return steric_values