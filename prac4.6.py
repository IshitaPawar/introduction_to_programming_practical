number = int(input("Enter a nonnegative integer: "))

if number < 0:
    print("Please enter a nonnegative integer.")
else:
    original = number
    reverse = 0

    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number //= 10

    print("Reversed number:", reverse)

    if original == reverse:
        print("It is a palindrome.")
    else:
        print("It is not a palindrome.")
