import pandas as pd

# Read cleaned data
df = pd.read_csv("cleaned_sales.csv")

print("CLEANED DATA")
print(df)

# Total Sales
total_sales = df["Sales"].sum()

print("\nTOTAL SALES")
print(total_sales)

# Total Profit
total_profit = df["Profit"].sum()

print("\nTOTAL PROFIT")
print(total_profit)

# Average Sales
average_sales = df["Sales"].mean()

print("\nAVERAGE SALES")
print(average_sales)

# Region-wise Profit
region_profit = df.groupby("Region")["Profit"].sum()

print("\nREGION-WISE PROFIT")
print(region_profit)

# Product-wise Sales
product_sales = df.groupby("Product")["Sales"].sum()

print("\nPRODUCT-WISE SALES")
print(product_sales)

# Sorting
highest_profit = df.sort_values(
    by="Profit",
    ascending=False
)

print("\nHIGHEST PROFIT PRODUCTS")
print(highest_profit)

# Filtering
high_sales = df[df["Sales"] > 30000]

print("\nHIGH SALES PRODUCTS")
print(high_sales)

# Pivot Table
pivot = pd.pivot_table(
    df,
    values="Profit",
    index="Region",
    aggfunc="sum"
)

print("\nPIVOT TABLE")
print(pivot)