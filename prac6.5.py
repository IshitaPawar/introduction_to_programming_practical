matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

rows = len(matrix)
columns = len(matrix[0])

transpose = []

for j in range(columns):
    new_row = []
    for i in range(rows):
        new_row.append(matrix[i][j])
    transpose.append(new_row)

print("Original matrix:")
for row in matrix:
    print(row)

print("Transposed matrix:")
for row in transpose:
    print(row)
