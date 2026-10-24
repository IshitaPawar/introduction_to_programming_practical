categories = ("food", "stationery", "electronics")
cart = []

while True:
    print("\nCategories:", categories)
    print("1. Add item")
    print("2. Remove item")
    print("3. Display cart")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        item = input("Product name: ")
        cart.append(item)
        print(item, "added to cart.")

    elif choice == "2":
        item = input("Product to remove: ")
        if item in cart:
            cart.remove(item)
            print(item, "removed from cart.")
        else:
            print(item, "is not in the cart.")

    elif choice == "3":
        print("Cart:", cart)

    elif choice == "4":
        break

    else:
        print("Invalid option.")
