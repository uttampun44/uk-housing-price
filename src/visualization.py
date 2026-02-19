import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

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