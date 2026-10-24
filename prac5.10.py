rows = 4
columns = 5

for row in range(rows):
    for number in range(1, columns + 1):
        if number % 2 == 0:
            continue
        print(number, end=" ")
    print()
