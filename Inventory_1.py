import pandas as pd
import matplotlib.pyplot as plt

# Load Excel data
df = pd.read_excel("inventory.xlsx")

# Calculate total items and revenue
df["TotalValue"] = df["Quantity"] * df["Price"]
total_stock = df["Quantity"].sum()
total_revenue = df["TotalValue"].sum()

print("=== Inventory Summary ===")
print(df)
print(f"\nTotal Stock: {total_stock}")
print(f"Total Inventory Value: Rs. {total_revenue}")

# Bar chart for stock
plt.figure(figsize=(8, 5))
plt.bar(df["Product"], df["Quantity"], color='skyblue')
plt.title("Stock Quantity per Product")
plt.xlabel("Product")
plt.ylabel("Quantity")
plt.tight_layout()
plt.show()

# Pie chart for stock share
plt.figure(figsize=(6, 6))
plt.pie(df["Quantity"], labels=df["Product"], autopct='%1.1f%%', startangle=140)
plt.title("Product Share in Inventory")
plt.axis('equal')
plt.tight_layout()
plt.show()