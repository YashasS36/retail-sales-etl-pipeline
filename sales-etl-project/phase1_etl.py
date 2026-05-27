import pandas as pd

# Read CSV file
df = pd.read_csv("raw_sales.csv")

# Display raw data
print("RAW DATA")
print(df)

# Fill missing values
df.fillna(0, inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Create Profit column
df["Profit"] = df["Sales"] - df["Cost"]

# Display cleaned data
print("\nCLEANED DATA")
print(df)

# Save cleaned CSV
df.to_csv("cleaned_sales.csv", index=False)

print("\nCSV Cleaning Completed")