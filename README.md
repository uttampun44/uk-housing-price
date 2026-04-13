# 🏠 UK Housing Price Analysis (1968–2024)

A comprehensive data science project analyzing UK house price trends, regional comparisons,
property type breakdowns, and future price predictions using real Land Registry data.
**Enhanced with 3 ML models, advanced visualizations, and academic rigor.**

## 📊 Charts Generated

| Chart | Description |
|-------|-------------|
| **Regional Prices** | Average house prices by UK region from 1968 to 2024 |
| **House Types** | Detached, semi-detached, terraced, and flat price comparison |
| **YoY Growth %** | Year-on-year price growth showing market volatility & 2008 crash |
| **North/South Divide** | Critical analysis: South is **118% more expensive** than North |
| **Price Correlation** | Heatmap showing regional price co-movement |
| **ML Predictions** | 2025–2030 forecasts using Linear Regression, Random Forest, Decision Tree |
| **Model Comparison** | RMSE & R² scores across 3 ML algorithms & 7 regions |

## 🔍 Key Findings

### Housing Market Trends
- London prices grew from ~£4,400 (1968) to ~£445,400 (2024) — **100x increase**
- **North/South divide:** South averages £445,634 vs North £204,347 (**118.1% gap**)
- The 2008 financial crisis caused visible dips across all regions
- Detached homes have grown fastest, flats the slowest
- All UK regions are highly correlated (R > 0.95)

### ML Model Performance
- **Best model:** Linear Regression (R² = 0.72 for South East)
- **Finding:** Simpler model beats complex Random Forest on limited time-series data
- **Insight:** Dataset of 56 annual points makes ensemble methods overfit
- **Decision Tree** severely underperforms (R² negative on most splits)

### Critical Analysis
- ⚠️ Linear regression assumes constant growth — unrealistic over 56 years
- ⚠️ Random Forest struggles with 56 data points (overfitting risk)
- ⚠️ External factors (interest rates, inflation) not captured in model
- ✅ Recommendations documented: ARIMA, external features, market regimes

## 🗂️ Project Structure
```
uk_housing_price/
├── data/
│   └── raw/                           # CSV from Land Registry (1968-2024)
├── src/
│   ├── data_loader.py                 # Preprocessing with quality docs
│   ├── analysis.py                    # Cleaning, filtering, growth calc
│   ├── visualization.py               # 7 professional charts
│   └── prediction.py                  # 3 ML models + evaluation
├── outputs/
│   ├── charts/                        # All PNG visualizations
│   ├── model_evaluation_results.csv   # RMSE & R² comparison
│   └── model_critique.txt             # Full analysis & limitations
├── main.py                            # Main orchestration (5 stages)
├── requirements.txt                   # Python dependencies
├── MODEL_CRITIQUE_AND_REFERENCES.md   # Theory + math + citations
├── ACADEMIC_REFERENCES.md             # 20+ academic sources
└── README.md
```

## 🚀 How to Run

**1. Clone the repository**
```bash
git clone https://github.com/uttampun44/uk-housing-price.git
cd uk-housing-price
```

**2. Create virtual environment**
```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Mac/Linux
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Add the data file**

Download CSV from:
> https://www.gov.uk/government/statistical-data-sets/uk-house-price-index-data-downloads-august-2024

Place in: `data/raw/UK-HPI-full-file-2024-08.csv`

**5. Run the project**
```bash
python main.py
```

Generates:
- 7 professional charts in `outputs/charts/`
- Model evaluation in `outputs/model_evaluation_results.csv`
- Full critique in `outputs/model_critique.txt`

## � Docker Setup (Virtual Environment with Live Code Updates)

Run the project in Docker with **hot-reload** — changes in VSCode instantly reflected in container:

**1. Build the Docker image**
```bash
docker-compose build
```

**2. Run in Docker**
```bash
# Run analysis
docker-compose up

# Or run with interactive shell (for development)
docker-compose run --rm housing-analysis /bin/bash
```

**3. Live code editing**
- Edit files in VSCode normally
- Changes instantly reflected in running container (thanks to volume mount)
- Outputs saved to `outputs/` folder (visible in VSCode)

**4. Stop the container**
```bash
docker-compose down
```

### Volume Mounts Explained
- **`- .:/app`** — Source code mounted, **any edits synced instantly**
- **`- ./outputs:/app/outputs`** — Results folder accessible from host
- **`- /app/__pycache__`** — Python cache stays inside container (doesn't sync)

### Why Use Docker?
✅ Identical environment across machines (Windows, Mac, Linux)
✅ No Python version conflicts
✅ All dependencies isolated
✅ Easy to share with team
✅ Production-ready setup

## �📦 Dependencies
```
numpy>=1.21.0
pandas>=1.3.0
matplotlib>=3.4.0
scikit-learn>=1.0.0
seaborn>=0.11.0
```

## 🤖 ML Model Comparison

Three models tested across 56 years of historical data:

| Model | Pros | Cons | Best For |
|-------|------|------|----------|
| **Linear Regression** | Simple, interpretable, fast | Assumes constant growth | ✅ Best overall (R²=0.72) |
| **Random Forest** | Non-linear, robust to outliers | Black box, overfits on small data | Baseline comparison |
| **Decision Tree** | Explainable | Severe overfitting | Demonstrates why ensemble needed |

**Key insight:** With only 56 annual data points, the simpler Linear Regression model outperforms complex Random Forest. This demonstrates important ML principle: **simpler models often win with limited data**.

## 📚 Documentation

### For Your Assignment:

**MODEL_CRITIQUE_AND_REFERENCES.md**
- Complete mathematical explanation of all 3 models
- Strengths & limitations analysis
- Why each model succeeded/failed
- Academic justification with citations

**ACADEMIC_REFERENCES.md**
- 20+ academic sources ready to cite:
  - Breiman (2001) - Random Forest foundational paper
  - Hastie et al. (2009) - ML theory
  - Hyndman & Athanasopoulos - Time-series forecasting
  - Meen (2002) - Housing market economics
  - HM Land Registry - Data source citation

## 📁 Data Source

**UK House Price Index** — HM Land Registry  
> https://www.gov.uk/government/collections/uk-house-price-index-reports

- Public domain data since 1968
- Updated monthly with latest prices
- Coverage: England, Scotland, Wales
- Property types: Detached, Semi-detached, Terraced, Flat

**Citation:**
> HM Land Registry (2024). UK House Price Index - Full File. Department for Levelling Up, Housing and Communities. Retrieved from https://www.gov.uk/government/statistical-data-sets/uk-house-price-index-data-downloads-august-2024

## 🛠️ Built With

- **Python 3.10+** — Core language
- **Pandas** — Data loading, cleaning, aggregation
- **NumPy** — Numerical computations
- **Matplotlib** — Professional chart rendering
- **Seaborn** — Statistical visualizations
- **Scikit-learn** — ML models (Linear Regression, Random Forest, Decision Tree)

## 📖 Key Learnings

✅ **Data preprocessing matters** — Proper handling of missing values, date parsing (dd/mm/yyyy), year extraction improves model quality

✅ **Model evaluation is critical** — Never judge by a single metric; use RMSE + R² + visual inspection

✅ **Simpler is often better** — Occam's Razor applies to ML; test multiple models and let data decide

✅ **Time-series has unique challenges** — Extrapolation beyond known data is risky; external variables improve accuracy

✅ **Academic rigor strengthens work** — Citations, methodology docs, and transparent limitations show professional-level analysis

## 🎓 For Academic Use

This project demonstrates:
- ✅ Real-world data science workflow
- ✅ Multiple ML algorithms tested rigorously
- ✅ Proper evaluation metrics (RMSE, R² Score)
- ✅ Critical thinking about model limitations
- ✅ Academic citations and references
- ✅ Reproducible analysis pipeline

**Ready for university assignment or data science portfolio.**

## 📝 Future Improvements

If extending this project:

1. **Add external features:** Interest rates (BoE), inflation (CPI), unemployment
2. **Time-series models:** ARIMA/SARIMA for financial forecasting
3. **Forward-chaining validation:** Proper temporal cross-validation
4. **Market regimes:** Separate models for boom/crash/recovery periods
5. **Deep learning:** LSTM for 56-year temporal dependencies
6. **Causal analysis:** What truly drives prices vs. mere correlation
