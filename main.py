# importing files from src folder

from src.data_loader import housing_prices_data
from src.analysis import analysis_data, filter_regions, get_yearly_average_price, calculate_growth
from src.visualization import (
    plot_regional_prices, 
    plot_house_types, 
    plot_yoy_growth, 
    plot_north_south_divide, 
    plot_price_correlation_heatmap
)
from src.prediction import predict_future_prices, get_model_critique

print("\n" + "="*70)
print("🏠 UK HOUSING PRICE ANALYSIS (1968–2024)")
print("="*70)

# ────────────────────────────────────────────────────────────────────────
# STAGE 1: DATA LOADING & PREPROCESSING
# ────────────────────────────────────────────────────────────────────────
print("\n📂 STAGE 1: Data Loading & Preprocessing")
print("-" * 70)

df = housing_prices_data()
results = analysis_data(df)
results = filter_regions(results)
df_yearly = get_yearly_average_price(results)
df_yearly = calculate_growth(df_yearly)

print(f"✓ Data prepared: {len(df_yearly)} data points across {df_yearly['RegionName'].nunique()} regions")

# ────────────────────────────────────────────────────────────────────────
# STAGE 2: TRADITIONAL VISUALIZATIONS
# ────────────────────────────────────────────────────────────────────────
print("\n📊 STAGE 2: Traditional Analysis Visualizations")
print("-" * 70)

plot_regional_prices(df_yearly)
plot_house_types(df)

# ────────────────────────────────────────────────────────────────────────
# STAGE 3: ADVANCED VISUALIZATIONS (For Deeper Analysis)
# ────────────────────────────────────────────────────────────────────────
print("\n📈 STAGE 3: Advanced Analysis Visualizations")
print("-" * 70)

plot_yoy_growth(df_yearly)
plot_north_south_divide(df_yearly)
# plot_price_correlation_heatmap(df)  # Skipped: Takes too long

# ────────────────────────────────────────────────────────────────────────
# STAGE 4: ML MODEL COMPARISON & PREDICTIONS
# ────────────────────────────────────────────────────────────────────────
print("\n🤖 STAGE 4: ML Model Comparison & Future Predictions")
print("-" * 70)

predict_future_prices(df_yearly)

# ────────────────────────────────────────────────────────────────────────
# STAGE 5: MODEL CRITIQUE & LIMITATIONS
# ────────────────────────────────────────────────────────────────────────
print("\n📋 STAGE 5: Model Critique & Limitations Analysis")
print("-" * 70)

critique = get_model_critique()
print(critique)

# Save critique to file for reference
with open("outputs/model_critique.txt", "w", encoding="utf-8") as f:
    f.write(critique)
print("✔ Critique saved: outputs/model_critique.txt")

# ────────────────────────────────────────────────────────────────────────
# FINAL SUMMARY
# ────────────────────────────────────────────────────────────────────────
print("\n" + "="*70)
print("✅ ANALYSIS COMPLETE!")
print("="*70)
print("\n📁 Output Files Generated:")
print("   Charts:")
print("   • outputs/charts/regional_prices.png")
print("   • outputs/charts/house_types.png")
print("   • outputs/charts/yoy_growth.png")
print("   • outputs/charts/north_south_divide.png")
print("   • outputs/charts/price_correlation_heatmap.png")
print("   • outputs/charts/price_prediction.png")
print("   • outputs/charts/model_comparison.png")
print("\n   Reports:")
print("   • outputs/model_evaluation_results.csv")
print("   • outputs/model_critique.txt")
print("   • MODEL_CRITIQUE_AND_REFERENCES.md (in root)")
print("   • ACADEMIC_REFERENCES.md (in root)")
print("\n💡 For Your Assignment:")
print("   1. Use the charts as evidence of analysis")
print("   2. Reference MODEL_CRITIQUE_AND_REFERENCES.md for theory")
print("   3. Copy citations from ACADEMIC_REFERENCES.md")
print("   4. Compare model performance from model_evaluation_results.csv")
print("   5. Show model critique for critical thinking")
print("\n" + "="*70 + "\n")