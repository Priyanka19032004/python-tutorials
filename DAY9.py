import csv
import pandas as pd
import os

FILE_NAME = "fruits.csv"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Fruit", "Price", "Quantity"])

with open(FILE_NAME, "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Apple", 20, 30])
    writer.writerow(["Orange", 30, 40])

print("Data added to CSV!")

df = pd.read_csv(FILE_NAME)

print("\nReading CSV using Pandas:")
print(df)
