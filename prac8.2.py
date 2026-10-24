student = {
    "name": "Asha",
    "age": 19,
    "marks": 92
}

print("Name:", student["name"])
print("Marks:", student["marks"])

try:
    print(student["course"])
except KeyError:
    print("The key 'course' does not exist.")
