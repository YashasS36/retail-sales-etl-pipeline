import pandas as pd


# Function for cleaning data
def clean_data(df):

    # Fill missing values
    df.fillna(0, inplace=True)

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # Create Profit column
    df["Profit"] = df["Sales"] - df["Cost"]

    return df


# Function for analytics report
def generate_report(df):

    print("\nTOTAL SALES")
    print(df["Sales"].sum())

    print("\nTOTAL PROFIT")
    print(df["Profit"].sum())

    print("\nREGION-WISE PROFIT")
    print(df.groupby("Region")["Profit"].sum())


# Main ETL Pipeline
try:

    # Extract
    df = pd.read_csv("raw_sales.csv")

    print("RAW DATA")
    print(df)

    # Transform
    cleaned_df = clean_data(df)

    print("\nCLEANED DATA")
    print(cleaned_df)

    # Analytics
    generate_report(cleaned_df)

    # Load
    cleaned_df.to_csv(
        "automated_cleaned_sales.csv",
        index=False
    )

    print("\nAUTOMATED ETL COMPLETED")

except FileNotFoundError:

    print("ERROR: CSV file not found")

except Exception as e:

    print("ERROR OCCURRED:")
    print(e)