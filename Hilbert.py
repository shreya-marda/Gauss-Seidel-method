import numpy as np

# Hilbert matrix generating and Gauss Seidel

h = int(input("Enter the dimension of hilbert matrix: "))
X = []
for _ in range(h):
    X.append(0)
# generating Hilbert matrix
Hilbert_mat = np.zeros((h, h))

for i in range(h):
    for j in range(h):
        Hilbert_mat[i, j] = 1 / (i + j + 1)

print(Hilbert_mat)
# This will give the solution for Hilbert matrix as the solution is [1,1,...], B will be the sum of elements in a row
B = []
for i in range(h):
    B.append(sum(Hilbert_mat[i]))
