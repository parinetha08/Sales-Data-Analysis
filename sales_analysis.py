import pandas as pd
import matplotlib.pyplot as plt

# STEP 1: Load dataset
df = pd.read_csv("sales.csv")
print("Dataset Loaded Successfully\n")

# STEP 2: Basic Info
print("First 5 Rows:\n", df.head())

# STEP 3: Total Sales & Profit
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
print("\nTotal Sales:", total_sales)
print("Total Profit:", total_profit)

# STEP 4: Sales by Region
region_sales = df.groupby("Region")["Sales"].sum()
print("\nSales by Region:\n", region_sales)

# STEP 5: Sales by Category
category_sales = df.groupby("Category")["Sales"].sum()
print("\nSales by Category:\n", category_sales)

# STEP 6: Monthly Sales Trend
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Month"] = df["Order Date"].dt.month
monthly_sales = df.groupby("Month")["Sales"].sum()
print(monthly_sales)

# ================= VISUALIZATION =================

# GRAPH 1 — Sales by Region
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()

# GRAPH 2 — Sales by Category
category_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Sales by Category")
plt.ylabel("")
plt.show()

# GRAPH 3 — Monthly Sales Trend
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()