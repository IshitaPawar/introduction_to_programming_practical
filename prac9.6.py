def find_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def find_largest(numbers):
    if not numbers:
        return None

    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

first_list = [4, 8, 2, 10]
second_list = [15, 3, 12]

print("First list sum:", find_sum(first_list))
print("First list largest:", find_largest(first_list))

print("Second list sum:", find_sum(second_list))
print("Second list largest:", find_largest(second_list))
