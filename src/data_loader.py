import pandas as pd


def housing_prices():

    df = pd.read_csv("data/raw/UK-HPI-full-file-2024-08.csv")

    print("Shape:",df.shape)
    print("Columns:",df.columns)
    return df
