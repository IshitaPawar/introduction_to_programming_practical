try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

    print(a / b)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")



try:
    a = "10"
    n = 5

    print("Type Error:")
    print("Error: Cannot add string and integers.")

    # Correct way
    print(int(a) + n)

except TypeError:
    print("Type Error occurred.")
