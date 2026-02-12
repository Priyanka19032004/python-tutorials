import pandas as pd
import os

FILE_NAME = "fruits.csv"

def analyze_inventory():
    if not os.path.exists(FILE_NAME):
        print("File not found!")
        return

    df = pd.read_csv(FILE_NAME)

    if df.empty:
        print("Inventory is empty!")
        return

    print("\nInventory Data:")
    print(df)

    total_quantity = df["Quantity"].sum()
    print("\nTotal Quantity:", total_quantity)

    df["Stock Value"] = df["Price"] * df["Quantity"]

    total_value = df["Stock Value"].sum()
    print("Total Inventory Value:", total_value)

    expensive = df.loc[df["Price"].idxmax()]
    print("\nMost Expensive Fruit:")
    print(expensive)

    low_stock = df.loc[df["Quantity"].idxmin()]
    print("\nLowest Stock Fruit:")
    print(low_stock)

analyze_inventory()

