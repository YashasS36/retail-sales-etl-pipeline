import pandas as pd
import requests

# Read CSV
df = pd.read_csv("raw_sales.csv")

# API URL
url = "https://api.exchangerate-api.com/v4/latest/USD"

# Fetch API data
response = requests.get(url)

# Convert response to JSON
data = response.json()

# Extract INR exchange rate
inr_rate = data["rates"]["INR"]

print("USD to INR Rate:")
print(inr_rate)

# Convert Sales into INR
df["Sales_INR"] = df["Sales"] * inr_rate

# Display updated data
print("\nUPDATED DATA")
print(df)

# Save new CSV
df.to_csv(
    "sales_inr.csv",
    index=False
)

print("\nAPI INTEGRATION COMPLETED")