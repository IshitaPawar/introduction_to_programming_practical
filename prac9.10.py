count = 0

def increase_count():
    global count
    count += 1

print("Before:", count)
increase_count()
increase_count()
print("After:", count)
