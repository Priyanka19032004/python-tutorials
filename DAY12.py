import pandas as pd
import os
from datetime import datetime

FILE_NAME = "fruits.csv"
REPORT_FILE = "inventory_report.txt"
LOW_STOCK = 20

def generate_report():
    if not os.path.exists(FILE_NAME):
        print("File not found!")
        return

    df = pd.read_csv(FILE_NAME)

    if df.empty:
        print("Inventory is empty!")
        return

    df["Stock Value"] = df["Price"] * df["Quantity"]

    total_quantity = df["Quantity"].sum()
    total_value = df["Stock Value"].sum()
    top_fruit = df.loc[df["Stock Value"].idxmax()]["Fruit"]

    low_stock_items = df[df["Quantity"] < LOW_STOCK]

    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    with open(REPORT_FILE, "w") as file:
        file.write("FRUITS INVENTORY REPORT\n")
        file.write("========================\n")
        file.write(f"Generated on: {now}\n\n")

        file.write(df.to_string(index=False))
        file.write("\n\nSUMMARY\n")
        file.write("-----------------\n")
        file.write(f"Total Quantity: {total_quantity}\n")
        file.write(f"Total Inventory Value: {total_value}\n")
        file.write(f"Top Revenue Fruit: {top_fruit}\n")

        if not low_stock_items.empty:
            file.write("\nLow Stock Alert:\n")
            for fruit in low_stock_items["Fruit"]:
                file.write(f"- {fruit} needs restocking\n")

    print("Report generated successfully!")

generate_report()
