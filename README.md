🐄 Milk Yield Forecasting — Daily Dairy Production Analysis
📌 Project Overview

This project analyzes and forecasts daily milk yield from a real dairy farm, using 5 years of detailed operational records.

It includes:

Individual cow milk yield (Morning / Midday / Evening)

Total daily yield

Health event logs

Breeding and pregnancy cycles

Seasonal yield drops

Anomaly detection for sudden performance changes

The purpose is to produce:

Clean, reliable time-series datasets

Models for short- and long-term milk forecasting

Detection of abnormal yield drops

Visual dashboards to support smarter farm decision-making

📁 Project Structure
milk-yield-forecasting/
│
├── data/             # Raw daily CSV files
├── notebooks/        # Jupyter notebooks for analysis & modeling
├── outputs/          # Generated charts, forecasts, tables
├── src/              # Cleaning & preprocessing scripts
├── setup.sh          # Environment setup helper (optional)
└── README.md         # Documentation (this file)

🐄 Data Sources

Your dataset contains:

Daily milk yield per cow

Total herd yield

Milking sessions (Morning, Midday, Evening)

Recorded yield drops

CSV files are stored in:

data/

🛠 Tools & Technologies
Languages & Libraries

Python

pandas

numpy

matplotlib

statsmodels (ARIMA / SARIMAX)

scikit-learn

prophet (optional)

Development Tools

VS Code

Git / GitHub

Virtual Environments (venv)

📈 Methods Used
✔ 1. Data Cleaning

Fixes irregular date encodings (e.g., 2025+AC0-11+AC0-18)

Normalizes column names

Converts data to a daily time series

✔ 2. Exploratory Data Analysis (EDA)

Daily yield trends

Cow-level performance

Weekly & monthly seasonality

✔ 3. Time-Series Forecasting

Models implemented:

ARIMA

SARIMAX

Prophet (optional)

Forecasts:

7-day

30-day

Per-cow forecasts

✔ 4. Anomaly Detection

Detects sudden milk drops using:

Rolling mean & rolling std

Z-scores

Threshold-based detection

✔ 5. Visualization

Charts stored in outputs/:

Yield timelines

Forecast vs actual

Model comparison (AIC/BIC)

Cow performance dashboards

🚀 Outputs

All artifacts are stored in the outputs/ folder, including:

Forecast charts

Seasonality plots

AIC/BIC model comparison

Anomaly detection visualizations

Cleaned CSV exports

📓 Notebooks

All Jupyter notebooks live in:

notebooks/


Examples include:

01_clean_and_prepare.ipynb

02_forecasting_models.ipynb

03_anomaly_detection.ipynb

04_per_cow_analysis.ipynb

🔧 Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/witttingtorch/milk-yield-forecasting.git
cd milk-yield-forecasting

2️⃣ Make the Setup Script Executable
chmod +x setup.sh

3️⃣ Run the Setup Script
./setup.sh

What setup.sh Does

Creates a virtual environment

Installs all required packages

Prepares folders for outputs & notebooks

✨ Author

Moses Martin Njuguna Gikonyo
GitHub: @witttingtorch
