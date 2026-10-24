numbers = [40, 10, 30, 20]

ascending = numbers.copy()
ascending.sort()
print("Ascending:", ascending)

descending = numbers.copy()
descending.sort(reverse=True)
print("Descending:", descending)

reversed_order = numbers.copy()
reversed_order.reverse()
print("Reversed original order:", reversed_order)
