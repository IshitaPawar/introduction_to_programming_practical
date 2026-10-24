def factorial_recursive(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n <= 1:  # Base case
        return 1
    return n * factorial_recursive(n - 1)

def factorial_loop(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    result = 1
    for number in range(2, n + 1):
        result *= number
    return result

number = int(input("Enter a nonnegative integer: "))

print("Recursive factorial:", factorial_recursive(number))
print("Loop-based factorial:", factorial_loop(number))
