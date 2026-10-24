student = {
    "name": "Asha",
    "age": 19,
    "marks": 92
}

removed_value = student.pop("age", None)
print("Value removed by pop:", removed_value)

if "marks" in student:
    del student["marks"]

print("Updated dictionary:", student)
