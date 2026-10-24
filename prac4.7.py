number = abs(int(input("Enter an integer: ")))

total_digits = 0
even_digits = 0
odd_digits = 0

if number == 0:
    total_digits = 1
    even_digits = 1
else:
    while number > 0:
        digit = number % 10
        total_digits += 1

        if digit % 2 == 0:
            even_digits += 1
        else:
            odd_digits += 1

        number //= 10

print("Total digits:", total_digits)
print("Even digits:", even_digits)
print("Odd digits:", odd_digits)
