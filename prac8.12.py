inventory = {}

while True:
    print("\n1. Add product")
    print("2. Update stock")
    print("3. Remove product")
    print("4. Display inventory")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        product = input("Product name: ")
        quantity = int(input("Quantity: "))
        inventory[product] = quantity
        print("Product added.")

    elif choice == "2":
        product = input("Product name: ")
        if product in inventory:
            quantity = int(input("New quantity: "))
            inventory[product] = quantity
            print("Stock updated.")
        else:
            print("Product not found.")

    elif choice == "3":
        product = input("Product name to remove: ")
        if product in inventory:
            del inventory[product]
            print("Product removed.")
        else:
            print("Product not found.")

    elif choice == "4":
        print("Current inventory:")
        for product, quantity in inventory.items():
            print(product, ":", quantity)

    elif choice == "5":
        break

    else:
        print("Invalid option.")

print("Final inventory:", inventory)
