import pandas as pd
import numpy as np

df = pd.read_csv("sales.csv")

df["Total"] = df["Quantity"] * df["Price"]

total_sales = np.sum(df["Total"])
average_sales = np.mean(df["Total"])
std_dev = np.std(df["Total"])

best_product = df.groupby("Product")["Quantity"].sum().idxmax()

print(df)
print("Total Sales:", total_sales)
print("Average Daily Sales:", average_sales)
print("Standard Deviation:", std_dev)
print("Best Selling Product:", best_product)
