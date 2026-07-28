# Input purchase amount
purchase_amount = float(input("Enter purchase amount: "))

# Apply discount conditions
if purchase_amount >= 2000:
    discount_percentage = 20
elif purchase_amount >= 1000:
    discount_percentage = 10
else:
    discount_percentage = 0

# Calculate final amount
discount_amount = (discount_percentage / 100) * purchase_amount
final_amount = purchase_amount - discount_amount

# Display final amount
print(f"Discount Applied: {discount_percentage}%")
print(f"Final Amount to Pay: {final_amount:.2f}")
