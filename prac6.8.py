import numpy as np

A = np.array([10, 20, 30])
B = np.array([1, 2, 3])

print("NumPy addition:", A + B)
print("NumPy subtraction:", A - B)
print("NumPy multiplication:", A * B)

# Equivalent addition using regular lists
list_A = [10, 20, 30]
list_B = [1, 2, 3]
list_sum = []

for i in range(len(list_A)):
    list_sum.append(list_A[i] + list_B[i])

print("List-based addition:", list_sum)
