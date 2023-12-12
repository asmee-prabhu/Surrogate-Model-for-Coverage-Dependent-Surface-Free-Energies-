#Deletes all the repeated structures with the same n1, n2 and n3 values

import pandas as pd
import numpy as np
import csv

# Read the data from 'n_data.csv' file
data = pd.read_csv('n_data.csv', header=0, names=None, index_col=None)

# Select specific columns ('FilePath', 'n1', 'n2', 'n3') and convert to numpy array
d = data[['FilePath', 'n1', 'n2', 'n3']].to_numpy()

# Extract only columns 'n1', 'n2', 'n3' as a numpy array
n = data[['n1', 'n2', 'n3']].to_numpy()

# Function to find unique rows in a numpy array
def unique_rows(a):
    a = np.ascontiguousarray(a)
    unique_a = np.unique(a.view([('', a.dtype)] * a.shape[1]))
    return unique_a.view(a.dtype).reshape((unique_a.shape[0], a.shape[1]))

# Find unique rows based on 'n1', 'n2', 'n3' values
n_f = unique_rows(n)

e = []

# Loop through unique 'n1', 'n2', 'n3' values
for n1, n2, n3 in n_f:
    for p, N1, N2, N3 in d:
        if n1 == N1 and n2 == N2 and n3 == N3:
            E = list()
            E.append(p)
    e.append(E)

f = [] 
for i in e:
    f.append(i[0])

n_f1 = []
n_f2 = []
n_f3 = []

for i in n_f:
    n_f1.append(i[0])
    n_f2.append(i[1])
    n_f3.append(i[2])

rowall = []
for i in range(len(f)):
    a = np.array((f[i], n_f1[i], n_f2[i], n_f3[i]))
    rowall.append(a)

rows = rowall
filename = 'n_data_processed.csv'

# Write the processed data to 'n_data_processed.csv' file
with open(filename, 'a') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(rows)
