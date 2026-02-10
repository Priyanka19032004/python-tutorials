import pandas as pd
import os

FILE_NAME = "fruits.csv"

def update_fruit():
    if not os.path.exists(FILE_NAME):
        print("Fruits file not found!")
        return

    df = pd.read_csv(FILE_NAME)

    if df.empty:
        print("Inventory is empty!")
        return

    name = input("Enter fruit name to update: ").strip()

    if name == "":
        print("Fruit name cannot be empty!")
        return

    if name not in df["Fruit"].values:
        print("Fruit not found!")
        return

    try:
        new_price = int(input("Enter new price: "))
        new_quantity = int(input("Enter new quantity: "))
    except:
        print("Price and quantity must be numbers!")
        return

    df.loc[df["Fruit"] == name, "Price"] = new_price
    df.loc[df["Fruit"] == name, "Quantity"] = new_quantity

    df.to_csv(FILE_NAME, index=False)
    print("✅ Fruit updated successfully!")

def delete_fruit():
    if not os.path.exists(FILE_NAME):
        print("Fruits file not found!")
        return

    df = pd.read_csv(FILE_NAME)

    if df.empty:
        print("Inventory is empty!")
        return

    name = input("Enter fruit name to delete: ").strip()

    if name == "":
        print("Fruit name cannot be empty!")
        return

    if name not in df["Fruit"].values:
        print("Fruit not found!")
        return

    df = df[df["Fruit"] != name]
    df.to_csv(FILE_NAME, index=False)

    print("Fruit deleted successfully!")

def menu():
    while True:
        print("\n--- Fruits Inventory System (Day 11) ---")
        print("1. Update Fruit")
        print("2. Delete Fruit")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            update_fruit()
        elif choice == "2":
            delete_fruit()
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")

menu()
