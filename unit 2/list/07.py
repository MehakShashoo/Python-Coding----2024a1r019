'''
wap that is menu driven in python where a user can add items, remove items, view cart and exit.
'''

cart = []

while True:
    print("\n--- Shopping Cart ---")
    print("1. Add item")
    print("2. Remove item")
    print("3. View cart")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter item to add: ")
        cart.append(item)
        print(item, "added to cart.")

    elif choice == 2:
        item = input("Enter item to remove: ")

        if item in cart:
            cart.remove(item)
            print(item, "removed from cart.")
        else:
            print("Item not found in cart.")

    elif choice == 3:
        print("Your cart:", cart)

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")