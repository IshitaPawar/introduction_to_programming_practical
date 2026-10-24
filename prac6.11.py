import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print("Matrix product using NumPy:")
print(A @ B)

print("Transpose of A using NumPy:")
print(A.T)

# Matrix multiplication using loops
rows_A, columns_A = A.shape
rows_B, columns_B = B.shape

if columns_A != rows_B:
    print("These matrices cannot be multiplied.")
else:
    product = [[0 for _ in range(columns_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(columns_B):
            for k in range(columns_A):
                product[i][j] += A[i, k] * B[k, j]

    print("Matrix product using loops:")
    for row in product:
        print(row)
