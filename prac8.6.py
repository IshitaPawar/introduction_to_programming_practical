student = {
    "name": "Asha",
    "age": 19,
    "marks": 92
}

print("Keys:")
for key in student.keys():
    print(key)

print("Values:")
for value in student.values():
    print(value)

print("Key-value pairs:")
for key, value in student.items():
    print(key, ":", value)
