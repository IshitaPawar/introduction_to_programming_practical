numbers_list = [10, 20, 30, 40]
numbers_tuple = (10, 20, 30, 40)

list_total = 0
print("List elements:")
for number in numbers_list:
    print(number)
    list_total += number

tuple_total = 0
print("Tuple elements:")
for number in numbers_tuple:
    print(number)
    tuple_total += number

print("List sum:", list_total)
print("Tuple sum:", tuple_total)
