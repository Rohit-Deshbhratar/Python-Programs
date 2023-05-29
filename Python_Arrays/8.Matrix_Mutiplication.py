matrix_1 = [[6, 9], [2, 5]]
matrix_2 = [[3, 2], [6, 2]]
matrix_3 = [[0, 0], [0, 0]]

print(f"Matrix 1: {matrix_1}")
print(f"Matrix 2: {matrix_2}")
for i in range(0, len(matrix_1)):
    for j in range(0, len(matrix_2)):
        matrix_3[i][j] = matrix_1[i][j] * matrix_2[i][j]

print(f"Matrix 1 * Matrix 2 = {matrix_3}")