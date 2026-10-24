import numpy as np

students = ["Asha", "Ravi", "Meera", "Kabir"]

# Each row contains one student's marks in three subjects
marks = np.array([
    [85, 90, 88],
    [72, 78, 75],
    [95, 92, 98],
    [81, 79, 84]
])

averages = np.mean(marks, axis=1)

for i in range(len(students)):
    print(f"{students[i]} average: {averages[i]:.2f}")

highest_index = np.argmax(averages)
lowest_index = np.argmin(averages)

print("Highest average:", students[highest_index], averages[highest_index])
print("Lowest average:", students[lowest_index], averages[lowest_index])
