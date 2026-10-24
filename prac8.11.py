marks = {
    "Ravi": 76,
    "Meera": 92,
    "Asha": 84
}

print("Sorted by key:")
for key, value in sorted(marks.items()):
    print(key, value)

print("Sorted by value:")
for key, value in sorted(marks.items(), key=lambda item: item[1]):
    print(key, value)
