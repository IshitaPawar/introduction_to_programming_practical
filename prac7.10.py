items = ["pen", "book", "bag"]
values = tuple(items)
print("List converted to tuple:", values)

items_again = list(values)
items_again.append("bottle")
print("Modified list:", items_again)

values_again = tuple(items_again)
print("Converted back to tuple:", values_again)
