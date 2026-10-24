import numpy as np

array = np.arange(1, 13)

print("Original 1D array:")
print(array)

matrix_3_by_4 = array.reshape(3, 4)
print("Reshaped to 3 x 4:")
print(matrix_3_by_4)

matrix_2_by_6 = array.reshape(2, 6)
print("Reshaped to 2 x 6:")
print(matrix_2_by_6)
