km = float(input("Enter kilometer: "))
celsius = float(input("Enter temperature: "))
rupees = float(input("Enter rupees: "))

meter = km * 1000
fahrenheit = (celsius * 9 / 5 + 32)
dollars = rupees / 85

print("meter:", meter)
print("fahrenheit:", fahrenheit)
print("US dollars:", dollars)
