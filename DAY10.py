import pandas as pd
import os

FILE_NAME = "fruits.csv"

def search_fruit():
    if not os.path.exists(FILE_NAME):
        print("Fruits file not found!")
        return

    df = pd.read_csv(FILE_NAME)

    if df.empty:
        print("Inventory is empty!")
        return

    name = input("Enter fruit name to search: ").strip()

    if name == "":
        print("Fruit name cannot be empty!")
        return

    result = df[df["Fruit"].str.lower() == name.lower()]

    if result.empty:
        print("Fruit not found!")
    else:
        print("\n Fruit Found:")
        print(result)

def menu():
    while True:
        print("\n--- Fruits Inventory (Day 10) ---")
        print("1. Search Fruit")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            search_fruit()
        elif choice == "2":
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")

menu()
