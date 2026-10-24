matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rows = len(matrix)
columns = len(matrix[0])

print("Row-wise:")
for i in range(rows):
    for j in range(columns):
        print(matrix[i][j], end=" ")
    print()

print("Column-wise:")
for j in range(columns):
    for i in range(rows):
        print(matrix[i][j], end=" ")
    print()
