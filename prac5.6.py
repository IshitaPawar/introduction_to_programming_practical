numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

for number in numbers:
    if number < 0:
        continue
    print(number)
