#Generates all possible configurations at a given coverage (r) of S* on a 4x4 Pt(111) such that the surface Pt atoms have indices ranging from 16 to 31.

import numpy as np
import os
import shutil
from ase import Atom, Atoms
from ase.io import read, write
from itertools import combinations

# Generating an array of Pt atom indices ranging from 16 to 31
A = np.linspace(16, 31, num=16)
R = np.asarray(A, dtype=int)

# Function to generate all combinations of size 'r' from the Pt atom indices aka the to be S* adsorption site indices

def rSubset(arr, r):
    return list(combinations(arr, r))

# Desired coverage of S* on the surface
r = 2
C = rSubset(R, r)  # All combinations of 'r' Pt atom indices

# Iterate through all combinations
for j in C:
    B = j
    slab = read('POSCAR')  # Read the initial structure file 'POSCAR'
    pos = slab.get_positions()

    # Place S* atoms at the specified Pt indices in the combination
    for i in B:
        S_pos = pos[i]
        slab.append(Atom('S', position=([S_pos[0], S_pos[1], S_pos[2] + 6.5])))

    # Create a directory for each configuration and save the structure inside
    path1 = os.getcwd()
    path = str(C.index(j))
    os.mkdir(path)
    slab.center(vacuum=16 * 0.5, axis=2)  # Center the structure
    write('CONTCAR', slab)  # Write the modified structure to 'CONTCAR'
    filename = 'CONTCAR'
    shutil.copy2(os.path.join(path1, filename), os.path.join(path1, path))  # Copy the structure to the created directory

# Remove the temporary 'CONTCAR' file
os.remove('CONTCAR')
