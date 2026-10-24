#a
rows = 4

for i in range(1, rows + 1):
    for _ in range(i):
        print("*", end="")
    print()

#b
rows = 4

for i in range(1, rows + 1):
    for number in range(1, i + 1):
        print(number, end=" ")
    print()

#c
rows = 4

for i in range(rows, 0, -1):
    for _ in range(i):
        print("*", end="")
    print()
