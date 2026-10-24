n = int(input("Enter a nonnegative integer: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Using for
    factorial_for = 1
    for i in range(1, n + 1):
        factorial_for *= i

    # Using while
    factorial_while = 1
    i = 1
    while i <= n:
        factorial_while *= i
        i += 1

    print("Factorial using for:", factorial_for)
    print("Factorial using while:", factorial_while)
