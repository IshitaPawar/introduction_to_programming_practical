def add_numbers(a, b):
    return a + b

def is_prime(number):
    if number < 2:
        return False

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True

def factorial(number):
    if number < 0:
        return None

    result = 1
    for value in range(2, number + 1):
        result *= value
    return result

while True:
    print("\n1. Addition")
    print("2. Prime check")
    print("3. Factorial")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        first = float(input("First number: "))
        second = float(input("Second number: "))
        print("Sum:", add_numbers(first, second))

    elif choice == "2":
        number = int(input("Enter an integer: "))
        if is_prime(number):
            print(number, "is prime.")
        else:
            print(number, "is not prime.")

    elif choice == "3":
        number = int(input("Enter a nonnegative integer: "))
        result = factorial(number)
        if result is None:
            print("Factorial is not defined for negative numbers.")
        else:
            print("Factorial:", result)

    elif choice == "4":
        break

    else:
        print("Invalid option.")
