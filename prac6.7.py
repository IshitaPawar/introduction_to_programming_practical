import numpy as np

array = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Element at row 2, column 3:", array[1, 2])
print("Entire second row:", array[1, :])
print("Entire first column:", array[:, 0])
print("First two rows and first two columns:")
print(array[:2, :2])
