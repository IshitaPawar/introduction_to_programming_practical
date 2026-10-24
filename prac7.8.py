values = (10, 20, 10, 30, 10)

print("Number of 10s:", values.count(10))

target = 20
if target in values:
    print("Index of", target, ":", values.index(target))
else:
    print(target, "is not in the tuple")
