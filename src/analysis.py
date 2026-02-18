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

    print("Cleaned Shape:", df.shape)
    print("Years available:", df["Year"].min(), "to", df["Year"].max())
    print("Regions available:", df["RegionName"].nunique())

    return df
