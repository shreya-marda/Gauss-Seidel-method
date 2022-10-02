import numpy as np
"""function to check if the matrix is diagonally dominant or not and tell if it
converges or not"""
def diagonally_dominant(mat):
    flag = 0
    i = 0
    while (i < len(mat)):
        sum = 0
        for j in range(len(mat[0])):
            if (i != j):
                sum += mat[i][j]
                if (mat[i][i] < sum):
                    flag = 0
                else:
                    flag = 1
        i += 1
    if (flag == 1):
        print("The matrix is diagonally dominant and will converge.\n")
    else:
        print("The matrix is not diagonally dominant and it may or may not converge.\n")
    
# defining function for Gauss Seidel

def GaussSeidel(matA, matB, n, X):
    maxiter = 100  # maximum iterations
    X = []  # giving the initial guess through the matrix
    for _ in range(n):
        X.append(0)  # X = [0,0,0.... n times]
    iter = 0  # initializing the iteration for while loop
    # Algorithm for Gauss Seidel method
    diagonally_dominant(matA)
    while iter < maxiter:
        for i in range(n):
            m = matB[i]
            for j in range(n):
                if i != j:
                    m -= matA[i][j] * X[j]
                X[i] = round((m / matA[i][i]), 6)
        iter += 1
        if (iter == 1) or (iter >= 98):
            print(iter, X)


# getting the inputs from the user in the form of matrix and return the answer
# from the function
n = int(input("Enter the number of unknowns or the dimension of matrix: "))
print("Enter the matrix in the form of [A|B]:")
A = []
for _ in range(n):
    l = list(map(float, input().split()))
    A.append(l)

B = []
for i in range(n):
    B.append(A[i][n])
    A[i].remove(A[i][n])

x = int(input("Enter 0 if you want your initial guess to be zero, else 1:"))

if x == 0:
    X = []
    for _ in range(n):
        X.append(0)
else:
    X = list(map(float, input("Enter your guess:").split()))

GaussSeidel(A, B, n, X)

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
# calling the function for Hilbert matrix
GaussSeidel(Hilbert_mat, B, h, X)
