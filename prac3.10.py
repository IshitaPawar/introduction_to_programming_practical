# Display menu options
print("----- MENU -----")
print("1. Check even/odd")
print("2. Find largest")
print("3. Grade system")
print("----------------")

# Take user choice
choice = int(input("Enter your choice (1-3): "))

# Execute selected operation using if-elif-else
if choice == 1:
    print("\n--- Check Even/Odd ---")
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(f"{num} is Even.")
    else:
        print(f"{num} is Odd.")

elif choice == 2:
    print("\n--- Find Largest ---")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))
    
    if num1 >= num2 and num1 >= num3:
        largest = num1
    elif num2 >= num1 and num2 >= num3:
        largest = num2
    else:
        largest = num3
    print(f"The largest number is {largest}.")

elif choice == 3:
    print("\n--- Grade System ---")
    score = float(input("Enter your score (0-100): "))
    
    if score >= 90 and score <= 100:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    elif score >= 0:
        grade = "F"
    else:
        grade = "Invalid Score"
        
    print(f"Your Grade is: {grade}")

else:
    print("Invalid choice! Please select an option between 1 and 3.")
