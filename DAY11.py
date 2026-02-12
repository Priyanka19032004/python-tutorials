import pandas as pd
import os

FILE_NAME = "fruits.csv"

def clean_data():
    if not os.path.exists(FILE_NAME):
        print("File not found!")
        return

    df = pd.read_csv(FILE_NAME)

    print("Before Cleaning:\n")
    print(df)

    df = df.dropna()

    df = df.drop_duplicates(subset="Fruit")

    df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
    df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")

    df = df.dropna()

    df = df[(df["Price"] >= 0) & (df["Quantity"] >= 0)]

    df.to_csv(FILE_NAME, index=False)

    print("\nAfter Cleaning:\n")
    print(df)

clean_data()
