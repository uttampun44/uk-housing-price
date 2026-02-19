import pandas as pd

# Load the housing price data from the CSV file
def housing_prices_data():

    df = pd.read_csv("data/raw/UK-HPI-full-file-2024-08.csv")
    return df
