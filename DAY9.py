import pandas as pd
import os

FILE_NAME = "fruits.csv"

def create_csv():
    if not os.path.exists(FILE_NAME):
        df = pd.DataFrame(columns=["Fruit", "Price", "Quantity"])
        df.to_csv(FILE_NAME, index=False)

def show_fruit():
    df = pd.read_csv(FILE_NAME)

    if df.empty:
        print("No fruits available!")
    else:
        print("\nFruits Stock:")
        print(df)
    print("----------------------")

def add_fruit():
    name = input("Enter fruit name: ").strip()
    if name == "":
        print("Fruit name should not be empty!")
        return

    try:
        price = int(input("Enter fruit price: "))
        quantity = int(input("Enter fruit quantity: "))
    except:
        print("Price and quantity must be numbers!")
        return

    df = pd.read_csv(FILE_NAME)

    new_row = pd.DataFrame(
        {"Fruit": [name], "Price": [price], "Quantity": [quantity]}
    )

    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(FILE_NAME, index=False)

    print("Fruit added successfully!")
    print("----------------------")


def update_quantity():
    name = input("Enter fruit name to update: ")

    df = pd.read_csv(FILE_NAME)

    if name in df["Fruit"].values:
        try:
            new_quantity = int(input("Enter new quantity: "))
        except:
            print("Quantity must be a number!")
            return

        df.loc[df["Fruit"] == name, "Quantity"] = new_quantity
        df.to_csv(FILE_NAME, index=False)

        print("Quantity updated successfully!")
    else:
        print("Fruit not found!")
    print("----------------------")

def delete_fruit():
    name = input("Enter fruit name to delete: ")

    df = pd.read_csv(FILE_NAME)

    if name in df["Fruit"].values:
        df = df[df["Fruit"] != name]
        df.to_csv(FILE_NAME, index=False)
        print("Fruit deleted successfully!")
    else:
        print("Fruit not found!")
    print("----------------------")

def menu():
    create_csv()

    while True:
        print("\n--- Fruits Inventory System (CSV + Pandas) ---")
        print("1. Show Fruits")
        print("2. Add Fruit")
        print("3. Update Quantity")
        print("4. Delete Fruit")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_fruit()
        elif choice == "2":
            add_fruit()
        elif choice == "3":
            update_quantity()
        elif choice == "4":
            delete_fruit()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")

menu()
