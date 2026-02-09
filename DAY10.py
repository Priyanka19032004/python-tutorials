import pandas as pd
import os

FILE_NAME = "fruits.csv"

def inventory_analysis():
    if not os.path.exists(FILE_NAME):
        print("Fruits file not found!")
        return

    df = pd.read_csv(FILE_NAME)

    if df.empty:
        print("Inventory is empty!")
        return

    print("\n Inventory Data:")
    print(df)
    print("-" * 40)

    total_quantity = df["Quantity"].sum()
    print("Total Quantity of Fruits:", total_quantity)

    df["Stock Value"] = df["Price"] * df["Quantity"]

    total_value = df["Stock Value"].sum()
    print("Total Inventory Value:", total_value)

    expensive_fruit = df.loc[df["Price"].idxmax()]
    print("\nMost Expensive Fruit:")
    print(expensive_fruit)

    low_stock = df.loc[df["Quantity"].idxmin()]
    print("\nLowest Stock Fruit:")
    print(low_stock)

    avg_price = df["Price"].mean()
    print("\n📊 Average Fruit Price:", round(avg_price, 2))

def menu():
    while True:
        print("\n--- Inventory Data Analysis ---")
        print("1. Analyze Inventory")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            inventory_analysis()
        elif choice == "2":
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")

menu()
