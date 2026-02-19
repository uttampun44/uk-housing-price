import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def predict_future_prices(df_yearly):

    fig, ax = plt.subplots(figsize=(14, 7))
    fig.patch.set_facecolor("#0F1117")
    ax.set_facecolor("#1A1D27")

    COLOURS = {
        "London":                   "#E63946",
        "South East":               "#F4A261",
        "North West":               "#2A9D8F",
        "Yorkshire and The Humber": "#457B9D",
        "Scotland":                 "#2DC653",
        "Wales":                    "#F77F00",
        "United Kingdom":           "#FFFFFF",
    }

    # predict next 10 years for each region
    furutre_years = np.arange(2025, 2035)

    for region, color in COLOURS.items():
        region_data = df_yearly[df_yearly["RegionName"] == region]

        if len(region_data) < 5:
            continue

        # Train a simple linear regression model on the historical data
        X = region_data["Year"].values.reshape(-1, 1)
        y = region_data["YearlyAveragePrice"].values
        model = LinearRegression()
        model.fit(X, y)

        # Predict future prices
        future_prices = model.predict(furutre_years.reshape(-1, 1))

        # Plot historical data
        ax.plot(
            region_data["Year"],
            region_data["YearlyAveragePrice"],
            label=region,
            color=color,
            linewidth=2
        )

        # Plot future predictions with dashed lines
        ax.plot(
            furutre_years,
            future_prices,
            label=f"{region} (Predicted)",
            color=color,
            linestyle="--",
            linewidth=2
        )

         # ── Add predicted price label at 2030 ────────────────────
        ax.annotate(
            f"£{future_prices[-1]:,.0f}",
            xy=(2030, future_prices[-1]),
            color=color,
            fontsize=7,
            va="center"
        )

    # ── Add vertical line to separate real vs predicted ──────────
    ax.axvline(x=2024, color="white", linewidth=1,
               linestyle=":", alpha=0.5)
    ax.text(2024.2, ax.get_ylim()[1] * 0.95,
            "← Real  |  Predicted →",
            color="white", fontsize=9, alpha=0.7)

    # ── Formatting ───────────────────────────────────────────────
    ax.yaxis.set_major_formatter(
        ticker.FuncFormatter(lambda x, _: f"£{x:,.0f}")
    )
    ax.set_title("UK House Price Prediction (2025–2030)",
                 color="white", fontsize=16, pad=15)
    ax.set_xlabel("Year", color="#AAAAAA", fontsize=12)
    ax.set_ylabel("Average House Price", color="#AAAAAA", fontsize=12)
    ax.tick_params(colors="#AAAAAA")
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color("#2E3147")
    ax.grid(axis="y", color="#2E3147", linewidth=0.5)
    ax.legend(fontsize=9, framealpha=0.2, labelcolor="white")

    plt.tight_layout()
    plt.savefig("outputs/charts/price_prediction.png",
                dpi=150, bbox_inches="tight", facecolor="#0F1117")
    plt.close()

    print("✔ Chart saved: outputs/charts/price_prediction.png")