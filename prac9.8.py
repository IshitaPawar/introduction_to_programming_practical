def fibonacci_recursive(n):
    if n < 0:
        raise ValueError("The index cannot be negative.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_iterative(n):
    if n < 0:
        raise ValueError("The index cannot be negative.")

    first, second = 0, 1
    sequence = []

    for _ in range(n):
        sequence.append(first)
        first, second = second, first + second

    return sequence

terms = int(input("How many terms? "))

print("Recursive sequence:")
for index in range(terms):
    print(fibonacci_recursive(index), end=" ")

print("\nIterative sequence:")
print(*fibonacci_iterative(terms))
