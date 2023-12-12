#Populates a CSV file with (1) No. Of Adsorbate Atoms (2) File Path & (3) Pairwise distances between all surface adsorbates using the POSCAR

from __future__ import division
from ase import Atom, Atoms
from ase.io import read
import sys
import csv
import numpy as np
import os

# Classify Distance upto which adsorbate effect exist
min_len1 = 3.5
min_len2 = 5.2
min_len3 = 6

# Adsorbed & Support Element Symbol
element1 = sys.argv[1]
element2 = sys.argv[2]

# Calculate Number of Adsorbed Atoms
def slabread(struc='POSCAR', element='S'):
    global slab
    slab = read(struc)
    list_atoms = []
    for atom in slab:
        if atom.symbol == element:
            list_atoms.append(atom.index)
    return list_atoms

listM = slabread(struc='POSCAR', element=element1)
listA = slabread(struc='POSCAR', element=element2)
atomsS = len(listA)

# Delete all support atoms
del slab[listM]

# Repeat the slab 3x times in the x & y direction
slab = slab.repeat((3, 3, 1))

# Get the pairwise distances between all adsorbate atoms
dist1 = []
i_index1 = []
j_index1 = []

dist2 = []
i_index2 = []
j_index2 = []

dist3 = []
i_index3 = []
j_index3 = []

pos = slab.get_positions()

x = list(range(len(pos)))
n = len(x)

# Indices range of atoms on central slab with respect to which counting must be done
n11 = int((n / 9) * 4)
n22 = int((n / 9) * 4 + (n / 9) - 1)

x1 = x[n11]
x2 = x[n22]

for i in x:
    for j in x[x1:x2 + 1]:
        if i != j:
            d = slab.get_distance(i, j)
            if d < min_len1:
                dist1.append(d)
                i_index1.append(i)
                j_index1.append(j)
            if min_len1 < d < min_len2:
                dist2.append(d)
                i_index2.append(i)
                j_index2.append(j)
            if min_len2 < d < min_len3:
                dist3.append(d)
                i_index3.append(i)

# Get current file path
path = os.getcwd()

# Write all results to csv in parent directory
rowall = np.array([path, len(dist1), len(dist2), len(dist3)])

rows = [rowall]
filename = '../n_data.csv'

with open(filename, 'a') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(rows)
