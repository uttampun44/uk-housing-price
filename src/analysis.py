import pandas as pd

def analysis_data(df):

    df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y")

    # Extract year from the Date column
    df['Year'] = df['Date'].dt.year

    df = df[["Date", "Year", "RegionName", 
             "AveragePrice", "DetachedPrice", 
             "SemiDetachedPrice", "TerracedPrice", 
             "FlatPrice", "SalesVolume"]]
    
    # Drop rows with missing AveragePrice
    df = df.dropna(subset=["AveragePrice"])
    return df


def filter_regions(df):

    regions = [
        "United Kingdom",
        "London",
        "South East",
        "North West",
        "Yorkshire and The Humber",
        "Scotland",
        "Wales"
    ]

    # Filter the DataFrame to include only the specified regions
    df = df[df["RegionName"].isin(regions)]

    return df

# Calculate yearly average price for each region
def get_yearly_average_price(df):

    df_yearly = df.groupby(["Year", "RegionName"])["AveragePrice"].mean().reset_index()
    df_yearly.rename(columns={"AveragePrice": "YearlyAveragePrice"}, inplace=True)
    
    return df_yearly

def calculate_growth(df):
    # For each region, calculate % growth from their first recorded year
    # lambda x means: apply this calculation to each region separately
    df["GrowthPct"] = df.groupby("RegionName")["YearlyAveragePrice"].transform(
        lambda x: (x / x.iloc[0] - 1) * 100
    )

    return df