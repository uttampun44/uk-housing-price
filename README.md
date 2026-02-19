# 🏠 UK Housing Price Analysis (1968–2024)

A data science project analysing UK house price trends, regional comparisons,
property type breakdowns, and future price predictions using real Land Registry data.

## 📊 Charts Generated

| Chart | Description |
|-------|-------------|
| Regional Prices | Average house prices by UK region from 1968 to 2024 |
| House Types | Detached, semi-detached, terraced and flat price comparison |
| Price Prediction | Machine learning forecast for 2025–2030 |

## 🔍 Key Findings

- London prices grew from ~£4,400 (1968) to ~£520,000 (2024)
- The North/South divide has widened significantly since 2000
- The 2008 financial crisis caused a visible dip across all regions
- Detached homes have grown fastest, flats the slowest
- London predicted to exceed £550,000 by 2030

## 🗂️ Project Structure
```
uk_housing_analysis/
├── data/
│   └── raw/                  # Original CSV from Land Registry
├── src/
│   ├── data_loader.py        # Loads and reads CSV data
│   ├── analysis.py           # Cleans, filters, calculates growth
│   ├── visualisation.py      # Generates charts
│   └── prediction.py         # ML price prediction
├── outputs/
│   └── charts/               # Saved chart images
├── main.py                   # Entry point — run this
├── requirements.txt          # Project dependencies
└── README.md
```

## 🚀 How to Run

**1. Clone the repository**
```bash
git clone https://github.com/uttampun44/uk-housing-price.git
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

Download the UK HPI full file CSV from:
> https://www.gov.uk/government/statistical-data-sets/uk-house-price-index-data-downloads-august-2024

Place it in:
```
data/raw/UK-HPI-full-file-2024-08.csv
```

**5. Run the project**
```bash
python main.py
```

Charts will be saved to `outputs/charts/`

## 📦 Dependencies
```
numpy
pandas
matplotlib
scikit-learn
```

## 📁 Data Source

**UK House Price Index** — HM Land Registry
> https://www.gov.uk/government/collections/uk-house-price-index-reports

Data is publicly available and updated monthly.

## 🛠️ Built With

- Python 3
- Pandas — data loading and cleaning
- Matplotlib — data visualisation
- Scikit-learn — linear regression prediction
