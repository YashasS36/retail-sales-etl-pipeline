import pandas as pd
import mysql.connector

# Read processed CSV
df = pd.read_csv("sales_inr.csv")
df.fillna(0, inplace=True)

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="sales_etl_db"
)

cursor = connection.cursor()

# Insert query
query = """
INSERT INTO sales_data
(Product, Region, Sales, Cost, Sales_INR)
VALUES (%s, %s, %s, %s, %s)
"""

# Insert rows
for index, row in df.iterrows():

    values = (
        row["Product"],
        row["Region"],
        row["Sales"],
        row["Cost"],
        row["Sales_INR"]
    )

    cursor.execute(query, values)

# Save changes
connection.commit()

print("DATA LOADED INTO MYSQL SUCCESSFULLY")

# Close connection
cursor.close()
connection.close()