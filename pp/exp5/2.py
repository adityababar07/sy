import numpy as np

# Define matrices
matrix1 = [[1, 2],[3, 4]]
matrix2 = [[5, 6],[7, 8]]
matrix3 = [[0,0],[0,0]]  # Placeholder for result of addition and subtraction
matrix4 = [[0,0],[0,0]]  # Placeholder for transposed matrix

# Addition
for i in range(2):
    for j in range(2):
        matrix3[i][j] = matrix1[i][j] + matrix2[i][j] 

print(f"Addition of matrices : {matrix3}")

# Subtraction
for i in range(2):
    for j in range(2):
        matrix3[i][j] = matrix1[i][j] - matrix2[i][j] 

print(f"Subtraction of matrices : {matrix3}")

# Transpose
for i in range(len(matrix4)):
    for j in range(len(matrix4[0])):
        matrix4[i][j] = matrix1[j][i]

print(f"The transpose of matrix1 :\n\n{np.matrix(matrix4)}")

# Multiplication
matrix3 = [[0,0],[0,0]]
for i in range(len(matrix1)):
    for k in range(len(matrix2[0])):
        for j in range(len(matrix2)):
            matrix3[i][j] += matrix1[i][k] * matrix2[k][j]

print(f"Multiplication of matrices : {matrix3}")

# Numpy operations
print(f"\nAddition of matrices matrix1 and matrix2:\n\n{np.add(matrix1, matrix2)}")
print(f"Subtraction of matrices matrix1 and matrix2:\n\n{np.subtract(matrix1, matrix2)}")
print(f"Multiplication of matrices matrix1 and matrix2:\n\n{np.dot(matrix1, matrix2)}")
print(f"Transpose of matrix1:\n\n{np.transpose(matrix1)}")
