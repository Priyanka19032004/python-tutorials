import pandas as pd
fruit_stock = {
    "Apple": {"price": 20, "quantity": 30},
    "Orange": {"price": 40, "quantity": 50}
}

def show_fruit():
    print("\nFRUIT INVENTORY")
    print("-------------------")
    for fruit in fruit_stock:
        print("Fruit:", fruit)
        print("Price:", fruit_stock[fruit]["price"])
        print("Quantity:", fruit_stock[fruit]["quantity"])
        print("-------------------")

def calculate_total_value():
    total_value = 0
    for fruit in fruit_stock:
        price = fruit_stock[fruit]["price"]
        quantity = fruit_stock[fruit]["quantity"]
        value = price * quantity
        total_value = total_value + value

    print("\nTotal inventory value:", total_value)

while True:
    print("\nFRUIT INVENTORY SYSTEM")
    print("1. Show Fruits")
    print("2. Add Fruit")
    print("3. Update Fruit")
    print("4. Delete Fruit")
    print("5. Exit")
    print("6. Total Inventory Value")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_fruit()
    elif choice == "6":
        calculate_total_value()
    elif choice == "5":
        print("Exit")
        break
    else:
        print("Option not implemented yet")