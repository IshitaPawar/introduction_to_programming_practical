terms = int(input("How many terms? "))

first = 0
second = 1

for _ in range(terms):
    print(first, end=" ")
    first, second = second, first + second

print()
