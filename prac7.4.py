items = [10, 20, 30]
items[1] = 99
print("Updated list:", items)

values = (10, 20, 30)

try:
    values[1] = 99
except TypeError as error:
    print("Tuple cannot be modified:", error)
