import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd
import seaborn as sns

# colors for each region

COLORS = {
    "London":                  "#E63946",
    "South East":              "#F4A261",
    "North West":              "#2A9D8F",
    "Yorkshire and The Humber":"#457B9D",
    "Scotland":                "#2DC653",
    "Wales":                   "#F77F00",
    "United Kingdom":          "#FFFFFF",
}

def plot_regional_prices(df):

    # create a figure canvas
    fig, ax = plt.subplots(figsize=(12, 6))
    fig.patch.set_facecolor("#1B1B1B")  # Set the background color of the entire figure
    ax.set_facecolor("#1B1B1B") # Set the background color of the plot area

    for region, color in COLORS.items():
       
        region_data = df[df["RegionName"] == region]
        
        ax.plot(
            region_data["Year"],              # x axis = years
            region_data["YearlyAveragePrice"],# y axis = prices
            label=region,                     # legend label
            color=color,                     # line colour
            linewidth=2                       # line thickness
        )

    # Format y axis to show £ sign
    ax.yaxis.set_major_formatter(
        ticker.FuncFormatter(lambda x, _: f"£{x:,.0f}")
    )

    # set title and labels
    ax.set_title("Average House Price by Region (1995-2024)", fontsize=16, color="#FFFFFF")
    ax.set_xlabel("Year", fontsize=12, color="#FFFFFF")
    ax.set_ylabel("Average Price", fontsize=12, color="#FFFFFF")

    ax.tick_params(colors="#FFFFFF")  # Set tick label color

    # style the border lines
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color("#FFFFFF") 

     # Add gridlines
    ax.grid(axis="y", color="#2E3147", linewidth=0.5)

    # Add legend
    ax.legend(fontsize=9, framealpha=0.2, labelcolor="white")

    # Save chart to outputs folder
    plt.tight_layout()
    plt.savefig("outputs/charts/regional_prices.png", 
                dpi=150, bbox_inches="tight", facecolor="#0F1117")
    plt.close()
    
    print("✔ Chart saved: outputs/charts/regional_prices.png")


def plot_house_types(df):
    

    # Filter for United Kingdom only for a national overview
    uk_data = df[df["RegionName"] == "United Kingdom"].copy()
    
    # Group by year and get yearly average for each house type
    uk_yearly = uk_data.groupby("Year")[
        ["DetachedPrice", "SemiDetachedPrice", "TerracedPrice", "FlatPrice"]
    ].mean()

    # Chart setup
    fig, ax = plt.subplots(figsize=(14, 7))
    fig.patch.set_facecolor("#0F1117")
    ax.set_facecolor("#1A1D27")

    # Each house type gets its own colour and line
    types = {
        "DetachedPrice":     ("#E63946", "Detached"),
        "SemiDetachedPrice": ("#F4A261", "Semi-Detached"),
        "TerracedPrice":     ("#2A9D8F", "Terraced"),
        "FlatPrice":         ("#457B9D", "Flat"),
    }

    for column, (colour, label) in types.items():
        ax.plot(
            uk_yearly.index,       # x = years
            uk_yearly[column],     # y = price for this type
            label=label,
            color=colour,
            linewidth=2
        )

    # Formatting
    ax.yaxis.set_major_formatter(
        ticker.FuncFormatter(lambda x, _: f"£{x:,.0f}")
    )
    ax.set_title("UK House Prices by Property Type (1995–2024)",
                 color="white", fontsize=16, pad=15)
    ax.set_xlabel("Year", color="#AAAAAA", fontsize=12)
    ax.set_ylabel("Average Price", color="#AAAAAA", fontsize=12)
    ax.tick_params(colors="#AAAAAA")
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color("#2E3147")
    ax.grid(axis="y", color="#2E3147", linewidth=0.5)
    ax.legend(fontsize=9, framealpha=0.2, labelcolor="white")
    ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    plt.tight_layout()
    plt.savefig("outputs/charts/house_types.png",
                dpi=150, bbox_inches="tight", facecolor="#0F1117")
    plt.close()

    print("✔ Chart saved: outputs/charts/house_types.png")


def plot_yoy_growth(df_yearly):
    """
    Year-on-Year Growth % visualization.
    Shows how quickly each region's prices are growing annually.
    """
    
    fig, ax = plt.subplots(figsize=(14, 7))
    fig.patch.set_facecolor("#0F1117")
    ax.set_facecolor("#1A1D27")
    
    for region, color in COLORS.items():
        region_data = df_yearly[df_yearly["RegionName"] == region].sort_values("Year")
        
        if len(region_data) < 2:
            continue
        
        # Calculate YoY growth % (year-on-year percentage change)
        yoy_growth = region_data["YearlyAveragePrice"].pct_change() * 100
        
        ax.plot(
            region_data["Year"][1:],  # Skip first year (NaN for growth calculation)
            yoy_growth[1:],
            label=region,
            color=color,
            linewidth=2,
            marker="o",
            markersize=3
        )
    
    # Add horizontal line at 0% (no growth)
    ax.axhline(y=0, color="white", linestyle="--", linewidth=1, alpha=0.3)
    
    # Add 2008 crisis marker
    ax.axvline(x=2008, color="#FF0000", linestyle=":", linewidth=2, alpha=0.5, label="2008 Financial Crisis")
    
    # Formatting
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{x:.1f}%"))
    ax.set_title("Year-on-Year House Price Growth (%)\nShowing Market Volatility & Boom/Bust Cycles",
                 color="white", fontsize=14, pad=15)
    ax.set_xlabel("Year", color="#AAAAAA", fontsize=12)
    ax.set_ylabel("YoY Growth (%)", color="#AAAAAA", fontsize=12)
    ax.tick_params(colors="#AAAAAA")
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color("#2E3147")
    ax.grid(axis="y", color="#2E3147", linewidth=0.5, alpha=0.5)
    ax.legend(fontsize=9, framealpha=0.2, labelcolor="white", loc="lower left")
    
    plt.tight_layout()
    plt.savefig("outputs/charts/yoy_growth.png",
                dpi=150, bbox_inches="tight", facecolor="#0F1117")
    plt.close()
    
    print("✔ Chart saved: outputs/charts/yoy_growth.png")


def plot_north_south_divide(df_yearly):
    """
    North/South Divide Comparison.
    Compares wealthy South (London + South East) vs struggling North (North West + Scotland).
    This is a critical UK housing market narrative.
    """
    
    fig, ax = plt.subplots(figsize=(14, 7))
    fig.patch.set_facecolor("#0F1117")
    ax.set_facecolor("#1A1D27")
    
    # Define regions
    south_regions = ["London", "South East"]
    north_regions = ["North West", "Scotland"]
    
    # Calculate average prices for North and South
    south_data = []
    north_data = []
    years = []
    
    for year in sorted(df_yearly["Year"].unique()):
        south_avg = df_yearly[
            (df_yearly["Year"] == year) & (df_yearly["RegionName"].isin(south_regions))
        ]["YearlyAveragePrice"].mean()
        
        north_avg = df_yearly[
            (df_yearly["Year"] == year) & (df_yearly["RegionName"].isin(north_regions))
        ]["YearlyAveragePrice"].mean()
        
        if not np.isnan(south_avg) and not np.isnan(north_avg):
            years.append(year)
            south_data.append(south_avg)
            north_data.append(north_avg)
    
    # Plot North & South
    ax.plot(years, south_data, label="South (London + South East)",
            color="#E63946", linewidth=3)
    ax.plot(years, north_data, label="North (North West + Scotland)",
            color="#2A9D8F", linewidth=3)
    
    # Calculate and plot the gap (divide)
    divide_data = np.array(south_data) - np.array(north_data)
    ax2 = ax.twinx()
    ax2.fill_between(years, divide_data, alpha=0.2, color="#FFA500", label="North/South Gap")
    ax2.set_ylabel("Price Gap (£)", color="#FFA500", fontsize=12)
    ax2.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"£{x:,.0f}"))
    ax2.tick_params(colors="#FFA500")
    ax2.spines[["top", "right"]].set_color("#2E3147")
    
    # Formatting
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"£{x:,.0f}"))
    ax.set_title("The North/South Housing Divide (1995–2024)\nWhy Is The South So Much More Expensive?",
                 color="white", fontsize=14, pad=15)
    ax.set_xlabel("Year", color="#AAAAAA", fontsize=12)
    ax.set_ylabel("Average Price (£)", color="#AAAAAA", fontsize=12)
    ax.tick_params(colors="#AAAAAA")
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color("#2E3147")
    ax.grid(axis="y", color="#2E3147", linewidth=0.5)
    
    # Combine legends
    lines1, labels1 = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines1 + lines2, labels1 + labels2, fontsize=10, framealpha=0.2, labelcolor="white")
    
    plt.tight_layout()
    plt.savefig("outputs/charts/north_south_divide.png",
                dpi=150, bbox_inches="tight", facecolor="#0F1117")
    plt.close()
    
    # Print analysis
    latest_south = south_data[-1]
    latest_north = north_data[-1]
    gap = latest_south - latest_north
    gap_pct = (gap / latest_north) * 100
    
    print("✔ Chart saved: outputs/charts/north_south_divide.png")
    print(f"\n📊 NORTH/SOUTH DIVIDE ANALYSIS (2024):")
    print(f"   South average (£): {latest_south:,.0f}")
    print(f"   North average (£): {latest_north:,.0f}")
    print(f"   Gap (£): {gap:,.0f}")
    print(f"   Gap (%): {gap_pct:.1f}% higher in South")


def plot_price_correlation_heatmap(df):
    """
    Correlation heatmap showing relationships between:
    - Regional prices
    - Property types
    - Market trends
    """
    
    # Aggregate data: Year vs Average Price for each major region
    pivot_data = df.groupby(["Year", "RegionName"])["AveragePrice"].mean().reset_index()
    correlation_matrix = pivot_data.pivot(index="Year", columns="RegionName", values="AveragePrice")
    
    # Calculate correlation between regions
    corr = correlation_matrix.corr()
    
    # Create heatmap
    fig, ax = plt.subplots(figsize=(10, 8))
    fig.patch.set_facecolor("#0F1117")
    ax.set_facecolor("#1A1D27")
    
    # Use seaborn for heatmap
    sns.heatmap(
        corr,
        annot=True,
        fmt=".2f",
        cmap="RdYlGn",
        center=0.8,
        vmin=0.7,
        vmax=1.0,
        cbar_kws={"label": "Correlation Coefficient"},
        ax=ax,
        linewidths=0.5,
        linecolor="#2E3147"
    )
    
    # Formatting
    ax.set_title("Regional House Price Correlation Matrix (1995–2024)\nBright = Prices Move Together",
                 color="white", fontsize=14, pad=15)
    ax.set_xlabel("Region", color="#AAAAAA", fontsize=11)
    ax.set_ylabel("Region", color="#AAAAAA", fontsize=11)
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", color="#AAAAAA")
    plt.setp(ax.get_yticklabels(), rotation=0, color="#AAAAAA")
    
    cbar = ax.collections[0].colorbar
    cbar.ax.tick_params(colors="#AAAAAA")
    cbar.set_label("Correlation Coefficient", color="#AAAAAA")
    
    plt.tight_layout()
    plt.savefig("outputs/charts/price_correlation_heatmap.png",
                dpi=150, bbox_inches="tight", facecolor="#0F1117")
    plt.close()
    
    print("✔ Chart saved: outputs/charts/price_correlation_heatmap.png")