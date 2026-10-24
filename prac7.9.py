matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Element at row 2, column 3:", matrix[1][2])

matrix[1][2] = 60

print("Updated matrix:")
for row in matrix:
    print(row)
