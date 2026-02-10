import pandas as pd
import os
from datetime import datetime

FILE_NAME = "fruits.csv"
REPORT_FILE = "inventory_report.txt"

def generate_report():
    if not os.path.exists(FILE_NAME):
        print("Fruits file not found!")
        return

    df = pd.read_csv(FILE_NAME)

    if df.empty:
        print("Inventory is empty!")
        return

    df["Stock Value"] = df["Price"] * df["Quantity"]

    total_items = len(df)
    total_quantity = df["Quantity"].sum()
    total_value = df["Stock Value"].sum()
    most_expensive = df.loc[df["Price"].idxmax()]["Fruit"]
    low_stock = df.loc[df["Quantity"].idxmin()]["Fruit"]

    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    with open(REPORT_FILE, "w") as file:
        file.write("FRUITS INVENTORY REPORT\n")
        file.write("========================\n")
        file.write(f"Report Generated On: {now}\n\n")

        file.write("Inventory Data:\n")
        file.write(df.to_string(index=False))
        file.write("\n\n")

        file.write("Summary:\n")
        file.write("------------------------\n")
        file.write(f"Total Different Fruits : {total_items}\n")
        file.write(f"Total Quantity         : {total_quantity}\n")
        file.write(f"Total Inventory Value  : {total_value}\n")
        file.write(f"Most Expensive Fruit   : {most_expensive}\n")
        file.write(f"Lowest Stock Fruit     : {low_stock}\n")

    print("Inventory report generated successfully!")
    print(f"Report saved as: {REPORT_FILE}")

def menu():
    while True:
        print("\n--- Inventory Report System (Day 12) ---")
        print("1. Generate Inventory Report")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            generate_report()
        elif choice == "2":
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")

menu()
