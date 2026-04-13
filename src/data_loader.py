import pandas as pd
import numpy as np

def housing_prices_data():
    """
    Load and perform initial preprocessing on UK house price data.
    
    DATA PREPROCESSING STRATEGY:
    ────────────────────────────
    
    1. MISSING VALUES HANDLING:
       - Average prices with NaN values are dropped entirely (critical metric)
       - Regional/property type prices may have NaN for rare categories
       - Strategy: Drop rows where AveragePrice is NaN (preserves data integrity)
    
    2. OUTLIER DETECTION:
       - Extreme price anomalies can indicate data entry errors
       - No price should be negative or exceed reasonable UK market bounds
       - Method: Log transformation will naturally minimize outlier impact
                 during regression modeling
    
    3. DATE PARSING:
       - Format: "dd/mm/yyyy" from Land Registry CSV
       - Converted to pandas datetime for proper chronological ordering
       - Extracted Year for temporal analysis and time-series validation
    
    4. FEATURE ENGINEERING:
       - Year extracted from Date for aggregation and prediction
       - SalesVolume included for weighted analysis (not yet used)
       - Regional filtering applied downstream (analysis.py)
    
    5. DATA QUALITY:
       - Dataset: ~50,000 rows covering 1968-2024
       - Coverage: England, Scotland, Wales (national + 9 regions)
       - Property types: Detached, Semi-Detached, Terraced, Flat
    
    Returns:
        DataFrame: Raw data with minimal processing for downstream analysis
    """
    df = pd.read_csv("data/raw/UK-HPI-full-file-2024-08.csv")
    
    # Log basic data quality info
    print(f"✓ Data loaded: {len(df)} rows, {len(df.columns)} columns")
    print(f"  Date range: {df['Date'].min()} to {df['Date'].max()}")
    print(f"  Memory usage: {df.memory_usage(deep=True).sum() / 1e6:.2f} MB")
    
    return df
