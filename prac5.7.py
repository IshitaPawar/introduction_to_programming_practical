total = 0

while True:
    number = float(input("Enter a number (0 to stop): "))

    if number == 0:
        break

    if number < 0:
        continue

    total += number

print("Sum of valid inputs:", total)
