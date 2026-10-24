numbers = [12, 5, 20, 8]
word = "Python"

print("Length of word:", len(word))
print("Sum:", sum(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

# Manual versions for a list of numbers
total = 0
largest = numbers[0]
smallest = numbers[0]

for number in numbers:
    total += number
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number

print("Manual sum:", total)
print("Manual maximum:", largest)
print("Manual minimum:", smallest)
