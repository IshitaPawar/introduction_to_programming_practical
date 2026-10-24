n = int(input("How many numbers? "))

if n <= 0:
    print("Please enter a positive number of values.")
else:
    total = 0.0

    for i in range(n):
        number = float(input(f"Enter number {i + 1}: "))
        total += number

    average = total / n

    print("Sum:", total)
    print("Average:", average)
