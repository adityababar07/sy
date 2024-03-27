matrix1 = [[1, 2],[3, 4]]

matrix2 = [[5, 6],[7, 8]]

matrix3 = [[0,0],[0,0]]


for i in range(2):
    element = 0
    for j in range(2):
        k = 0
        element+=matrix1[i][j]*matrix2[j][i]
        print(element)
        if j == 1:
            matrix3[i][k] = element
            k +=1

print(matrix3)