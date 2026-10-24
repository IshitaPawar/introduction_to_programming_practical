correct_password = "python123"

for attempt in range(1, 4):
    password = input(f"Attempt {attempt} of 3. Enter password: ")

    if password == correct_password:
        print("Correct password. Access granted.")
        break
    else:
        print("Incorrect password.")
else:
    print("Access denied. You used all 3 attempts.")
