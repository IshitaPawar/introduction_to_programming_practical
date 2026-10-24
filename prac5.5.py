n = int(input("Enter n: "))

if n == 0:
    print("Cannot divide by zero.")
else:
    for number in range(1, 101):
        if number % n == 0:
            print("First divisible number:", number)
            break
    else:
        print("No number from 1 to 100 is divisible by", n)
