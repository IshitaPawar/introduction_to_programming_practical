matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rows = len(matrix)
columns = len(matrix[0])

for i in range(rows):
    print(f"Sum of row {i + 1}:", sum(matrix[i]))

for j in range(columns):
    column_sum = 0
    for i in range(rows):
        column_sum += matrix[i][j]
    print(f"Sum of column {j + 1}:", column_sum)
