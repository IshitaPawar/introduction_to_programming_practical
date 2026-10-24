A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

rows = len(A)
columns = len(A[0])

result = []

for i in range(rows):
    new_row = []
    for j in range(columns):
        new_row.append(A[i][j] + B[i][j])
    result.append(new_row)

print("Result of matrix addition:")
for row in result:
    print(row)
