def get_numbers():
    return list(map(float, input("Enter numbers separated by spaces: ").split()))

def process_numbers(numbers):
    if not numbers:
        return None

    total = sum(numbers)
    average = total / len(numbers)
    return total, average

def display_result(result):
    if result is None:
        print("No numbers were entered.")
    else:
        total, average = result
        print("Sum:", total)
        print("Average:", average)

def main():
    numbers = get_numbers()
    result = process_numbers(numbers)
    display_result(result)

main()
