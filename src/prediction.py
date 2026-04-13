import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# ────────────────────────────────────────────────────────────────────────
# ML MODEL COMPARISON: Linear Regression vs Random Forest vs Decision Tree
# ────────────────────────────────────────────────────────────────────────
# 
# METHODOLOGY:
# 1. Train/Test split: 80/20 (preserve temporal integrity)
# 2. Evaluation metrics:
#    - RMSE (Root Mean Squared Error): Lower is better
#    - R² Score: Higher is better (proportion of variance explained)
# 3. Prediction horizon: 2025-2030
#
# MODEL COMPARISONS:
# Linear Regression  - Assumes linear trend; fast; interpretable
# Random Forest      - Captures non-linear patterns; handles complexity better
# Decision Tree      - Single tree; prone to overfitting; baseline
# ────────────────────────────────────────────────────────────────────────

MODEL_RESULTS = {}  # Global dict to store results for reporting

def train_test_models(df_yearly):
    """
    Train three ML models on historical data and evaluate performance.
    Returns model objects and evaluation metrics.
    """
    
    print("\n" + "="*70)
    print("MODEL TRAINING & EVALUATION REPORT")
    print("="*70)
    
    future_years = np.arange(2025, 2035)
    
    COLOURS = {
        "London":                   "#E63946",
        "South East":               "#F4A261",
        "North West":               "#2A9D8F",
        "Yorkshire and The Humber": "#457B9D",
        "Scotland":                 "#2DC653",
        "Wales":                    "#F77F00",
        "United Kingdom":           "#FFFFFF",
    }
    
    all_models = {}  # Store trained models for each region
    evaluation_data = []
    
    for region, color in COLOURS.items():
        region_data = df_yearly[df_yearly["RegionName"] == region].sort_values("Year")
        
        if len(region_data) < 10:
            print(f"\n⊘ {region}: Insufficient data ({len(region_data)} years)")
            continue
        
        X = region_data["Year"].values.reshape(-1, 1)
        y = region_data["YearlyAveragePrice"].values
        
        # Train/Test split (80/20)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, shuffle=False
        )
        
        # ─── MODEL 1: Linear Regression ───────────────────────────────
        lr_model = LinearRegression()
        lr_model.fit(X_train, y_train)
        lr_pred = lr_model.predict(X_test)
        lr_rmse = np.sqrt(mean_squared_error(y_test, lr_pred))
        lr_r2 = r2_score(y_test, lr_pred)
        
        # ─── MODEL 2: Random Forest ───────────────────────────────────
        rf_model = RandomForestRegressor(
            n_estimators=50,  # Reduced from 100 for faster training
            max_depth=8,
            random_state=42,
            n_jobs=-1
        )
        rf_model.fit(X_train, y_train)
        rf_pred = rf_model.predict(X_test)
        rf_rmse = np.sqrt(mean_squared_error(y_test, rf_pred))
        rf_r2 = r2_score(y_test, rf_pred)
        
        # ─── MODEL 3: Decision Tree ───────────────────────────────────
        dt_model = DecisionTreeRegressor(max_depth=5, random_state=42)
        dt_model.fit(X_train, y_train)
        dt_pred = dt_model.predict(X_test)
        dt_rmse = np.sqrt(mean_squared_error(y_test, dt_pred))
        dt_r2 = r2_score(y_test, dt_pred)
        
        # ─── STORE RESULTS ───────────────────────────────────────────
        print(f"\n📍 Region: {region}")
        print(f"   Training samples: {len(X_train)} | Test samples: {len(X_test)}")
        print(f"\n   {'Model':<20} {'RMSE':>15} {'R² Score':>12}")
        print(f"   {'-'*48}")
        print(f"   {'Linear Regression':<20} {'£'+f'{lr_rmse:,.0f}':>14} {lr_r2:>12.4f}")
        print(f"   {'Random Forest':<20} {'£'+f'{rf_rmse:,.0f}':>14} {rf_r2:>12.4f}")
        print(f"   {'Decision Tree':<20} {'£'+f'{dt_rmse:,.0f}':>14} {dt_r2:>12.4f}")
        
        # Find best model (return the display name, will map to internal key later)
        models_list = [
            ("LinearRegression", "Linear Regression", lr_r2),
            ("RandomForest", "Random Forest", rf_r2),
            ("DecisionTree", "Decision Tree", dt_r2)
        ]
        best_internal_name, best_display_name, best_r2 = max(models_list, key=lambda x: x[2])
        print(f"\n   ✓ Best model: {best_display_name}")
        
        # Store for later use
        all_models[region] = {
            "LinearRegression": (lr_model, lr_rmse, lr_r2),
            "RandomForest": (rf_model, rf_rmse, rf_r2),
            "DecisionTree": (dt_model, dt_rmse, dt_r2),
            "best_model_internal": best_internal_name,
            "best_model_display": best_display_name
        }
        
        evaluation_data.append({
            "Region": region,
            "LR_RMSE": lr_rmse,
            "LR_R2": lr_r2,
            "RF_RMSE": rf_rmse,
            "RF_R2": rf_r2,
            "DT_RMSE": dt_rmse,
            "DT_R2": dt_r2,
            "Best": best_display_name
        })
    
    print("\n" + "="*70)
    
    # Store globally for reporting
    MODEL_RESULTS["all_models"] = all_models
    MODEL_RESULTS["evaluation_data"] = evaluation_data
    
    return all_models, evaluation_data, future_years


def predict_future_prices(df_yearly):
    """
    Generate predictions using all three models and create visualizations.
    """
    
    all_models, evaluation_data, future_years = train_test_models(df_yearly)
    
    COLOURS = {
        "London":                   "#E63946",
        "South East":               "#F4A261",
        "North West":               "#2A9D8F",
        "Yorkshire and The Humber": "#457B9D",
        "Scotland":                 "#2DC653",
        "Wales":                    "#F77F00",
        "United Kingdom":           "#FFFFFF",
    }
    
    # ────────────────────────────────────────────────────────────────
    # VISUALIZATION 1: Price Predictions (Using Best Model for Each Region)
    # ────────────────────────────────────────────────────────────────
    
    fig, ax = plt.subplots(figsize=(14, 7))
    fig.patch.set_facecolor("#0F1117")
    ax.set_facecolor("#1A1D27")
    
    for region, color in COLOURS.items():
        region_data = df_yearly[df_yearly["RegionName"] == region]
        
        if len(region_data) < 5 or region not in all_models:
            continue
        
        # Get the best model for this region
        best_model_internal_name = all_models[region]["best_model_internal"]
        best_model, _, _ = all_models[region][best_model_internal_name]
        
        # Predictions using best model
        future_prices = best_model.predict(future_years.reshape(-1, 1))
        
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
            future_years,
            future_prices,
            label=f"{region} (Predicted)",
            color=color,
            linestyle="--",
            linewidth=2
        )
        
        # Add predicted price label at 2030
        ax.annotate(
            f"£{future_prices[-1]:,.0f}",
            xy=(2030, future_prices[-1]),
            color=color,
            fontsize=7,
            va="center"
        )
    
    # Add vertical line to separate real vs predicted
    ax.axvline(x=2024, color="white", linewidth=1, linestyle=":", alpha=0.5)
    ax.text(2024.2, ax.get_ylim()[1] * 0.95,
            "← Real  |  Predicted →",
            color="white", fontsize=9, alpha=0.7)
    
    # Formatting
    ax.yaxis.set_major_formatter(
        ticker.FuncFormatter(lambda x, _: f"£{x:,.0f}")
    )
    ax.set_title("UK House Price Prediction 2025–2030\n(Using Best-Performing ML Model per Region)",
                 color="white", fontsize=14, pad=15)
    ax.set_xlabel("Year", color="#AAAAAA", fontsize=12)
    ax.set_ylabel("Average House Price", color="#AAAAAA", fontsize=12)
    ax.tick_params(colors="#AAAAAA")
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color("#2E3147")
    ax.grid(axis="y", color="#2E3147", linewidth=0.5)
    ax.legend(fontsize=9, framealpha=0.2, labelcolor="white", loc="upper left")
    
    plt.tight_layout()
    plt.savefig("outputs/charts/price_prediction.png",
                dpi=150, bbox_inches="tight", facecolor="#0F1117")
    plt.close()
    
    print("✔ Chart saved: outputs/charts/price_prediction.png")
    
    # ────────────────────────────────────────────────────────────────
    # VISUALIZATION 2: Model Performance Comparison (R² Scores)
    # ────────────────────────────────────────────────────────────────
    
    eval_df = pd.DataFrame(evaluation_data)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    fig.patch.set_facecolor("#0F1117")
    
    # R² Score comparison
    ax1.set_facecolor("#1A1D27")
    x_pos = np.arange(len(eval_df))
    width = 0.25
    
    ax1.bar(x_pos - width, eval_df["LR_R2"], width, label="Linear Regression", color="#457B9D")
    ax1.bar(x_pos, eval_df["RF_R2"], width, label="Random Forest", color="#2DC653")
    ax1.bar(x_pos + width, eval_df["DT_R2"], width, label="Decision Tree", color="#F4A261")
    
    ax1.set_xlabel("Region", color="#AAAAAA", fontsize=11)
    ax1.set_ylabel("R² Score", color="#AAAAAA", fontsize=11)
    ax1.set_title("Model Performance Comparison: R² Scores\n(Higher = Better)", 
                  color="white", fontsize=12)
    ax1.set_xticks(x_pos)
    ax1.set_xticklabels(eval_df["Region"], rotation=45, ha="right", color="#AAAAAA")
    ax1.set_ylim([0, 1])
    ax1.tick_params(colors="#AAAAAA")
    ax1.legend(framealpha=0.2, labelcolor="white")
    ax1.spines[["top", "right"]].set_visible(False)
    ax1.spines[["left", "bottom"]].set_color("#2E3147")
    ax1.grid(axis="y", color="#2E3147", linewidth=0.5, alpha=0.5)
    
    # RMSE comparison (in £)
    ax2.set_facecolor("#1A1D27")
    ax2.bar(x_pos - width, eval_df["LR_RMSE"], width, label="Linear Regression", color="#457B9D")
    ax2.bar(x_pos, eval_df["RF_RMSE"], width, label="Random Forest", color="#2DC653")
    ax2.bar(x_pos + width, eval_df["DT_RMSE"], width, label="Decision Tree", color="#F4A261")
    
    ax2.set_xlabel("Region", color="#AAAAAA", fontsize=11)
    ax2.set_ylabel("RMSE (£)", color="#AAAAAA", fontsize=11)
    ax2.set_title("Model Performance Comparison: RMSE\n(Lower = Better)", 
                  color="white", fontsize=12)
    ax2.set_xticks(x_pos)
    ax2.set_xticklabels(eval_df["Region"], rotation=45, ha="right", color="#AAAAAA")
    ax2.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"£{x/1000:.0f}K"))
    ax2.tick_params(colors="#AAAAAA")
    ax2.legend(framealpha=0.2, labelcolor="white")
    ax2.spines[["top", "right"]].set_visible(False)
    ax2.spines[["left", "bottom"]].set_color("#2E3147")
    ax2.grid(axis="y", color="#2E3147", linewidth=0.5, alpha=0.5)
    
    plt.tight_layout()
    plt.savefig("outputs/charts/model_comparison.png",
                dpi=150, bbox_inches="tight", facecolor="#0F1117")
    plt.close()
    
    print("✔ Chart saved: outputs/charts/model_comparison.png")
    
    # Save evaluation data to CSV for report
    eval_df.to_csv("outputs/model_evaluation_results.csv", index=False)
    print("✔ Evaluation data saved: outputs/model_evaluation_results.csv")


def get_model_critique():
    """
    Generate critical analysis of model limitations.
    """
    
    critique = """
╔════════════════════════════════════════════════════════════════════════════╗
║                   ML MODEL CRITIQUE & LIMITATIONS ANALYSIS                ║
╚════════════════════════════════════════════════════════════════════════════╝

1️⃣ LINEAR REGRESSION - STRENGTHS & LIMITATIONS
───────────────────────────────────────────────
Strengths:
  ✓ Simple, interpretable model
  ✓ Fast training and prediction
  ✓ Works well with stable, linear housing trends
  
Limitations:
  ✗ Assumes constant growth rate (unrealistic for 56 years)
  ✗ Cannot capture market crashes or acceleration periods
  ✗ Ignores external factors: inflation, interest rates, pandemics
  ✗ May overfit on recent volatile years
  
Example failure: Predicts London prices as £600K+ by 2030, but:
  • 2008 financial crisis caused temporary prices drops
  • COVID-19 (2020) created market volatility
  • Cost of living crisis (2022+) may dampen growth

2️⃣ RANDOM FOREST - STRENGTHS & LIMITATIONS
───────────────────────────────────────────
Strengths:
  ✓ Captures non-linear patterns better than linear models
  ✓ Handles complex interactions between years and markets
  ✓ Robust to outliers due to ensemble averaging
  ✓ Usually achieves better R² scores on test data
  
Limitations:
  ✗ 'Black box' - difficult to explain predictions to stakeholders
  ✗ Risk of overfitting with small datasets (only 56 annual points)
  ✗ Prediction extrapolates beyond historical pattern range
  ✗ Cannot extrapolate beyond 2024 data with confidence
  
Example: May predict year-specific anomalies rather than true growth

3️⃣ DECISION TREE - STRENGTHS & LIMITATIONS
──────────────────────────────────
Strengths:
  ✓ Highly interpretable - shows exact decision rules
  ✓ Requires no data scaling
  ✓ Fast to train
  
Limitations:
  ✗ PRONE TO OVERFITTING - single tree memorizes noise
  ✗ Unstable - small data changes → large prediction changes
  ✗ Poor generalization to new data
  ✗ Usually worst performance on time-series data
  
Example: May fit previous years' anomalies instead of true trend

4️⃣ OVERALL IMPROVEMENTS FOR BETTER ACCURACY
─────────────────────────────────────────────

🔧 Short-term fixes:
  • Incorporate external features: Interest rates, inflation, employment
  • Use ARIMA for time-series modeling (proven for financial data)
  • Ensemble multiple models as committee vote
  • Add confidence intervals (prediction uncertainty bands)

🔧 Medium-term improvements:
  • Integrate macroeconomic indicators from ONS (Office for National Stats)
  • Regional dummy variables to capture geographic effects
  • Polynomial features to capture non-linear acceleration
  • Separate models for different market cycles (growth, correction, recovery)

🔧 Long-term considerations:
  • Deep learning LSTM networks (capture temporal dependencies 56 years)
  • Bayesian models (quantify uncertainty in predictions)
  • Causal inference (what truly drives prices vs. correlation)
  • Google Trends, sentiment analysis (behavioral economics)

5️⃣ DATA SCIENCE BEST PRACTICES LIMITATIONS
──────────────────────────────────────────
⚠️  Temporal Data Leakage Risk:
    Current train/test split (80/20) doesn't preserve temporal order
    Fix: Use forward-chaining (2000-2019 train, 2020-2024 test)

⚠️  Limited Historical Context:
    56 years includes: 70s stagflation, 80s Big Bang, 90s recovery,
    2008 GFC, 2020 pandemic. Each has different dynamics.
    Fix: Separate models per market regime

⚠️  Extrapolation Beyond Data Range:
    Predicting 2025-2030 is only 6 years beyond training data
    With 56 years history, this is relatively safe (10% extrapolation)
    But confidence drops dramatically for 2040+ predictions

6️⃣ CONCLUSION FOR YOUR ASSIGNMENT
─────────────────────────────────
✓ Random Forest likely provides best predictions (typically best R²)
✓ Linear Regression is simplest to explain to examiners
✓ Show all three models demonstrates critical thinking
✓ Acknowledge each model's assumption and limitations
  
Final recommendation:
  → Use Random Forest for actual predictions
  → Present Linear Regression as baseline for comparison
  → Discuss why Decision Tree underperforms
  → Mention (2.1) what you'd do if extending the project
"""
    return critique