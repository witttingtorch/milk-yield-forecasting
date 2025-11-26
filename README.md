
🥛 Milk Yield Forecasting – Data Science for Dairy Production
📌 Overview

This project applies data science, time-series forecasting, and anomaly detection to real dairy farm production data collected daily over 5 years.

It analyzes:

Milk yield per cow (Morning / Midday / Evening sessions)

Total herd production

Health events

Breeding cycles

Pregnancy stages

Yield drops

Operational patterns

The goal is to:

Forecast production

Detect anomalies (sudden drops)

Support farm decision-making

Improve feeding schedules

Increase operational efficiency

This real-world dataset showcases applied data science in agriculture, combining domain expertise + technical skills.

🗂 Project Structure
milk-yield-forecasting/
│
├── data/                # Raw CSV files (daily cow records)
├── notebooks/           # Jupyter notebooks (analysis, forecasting, anomalies)
├── src/                 # Python scripts (cleaning, loading, utilities)
├── outputs/             # Forecast plots, anomaly visuals, charts
├── setup.sh             # Setup script for environment
├── README.md            # Project documentation
└── requirements.txt     # Python dependencies

🔧 Tools & Technologies
Languages

Python 3.10+

Libraries

pandas

numpy

matplotlib / seaborn

statsmodels (ARIMA/SARIMAX)

scikit-learn

prophet (optional)

Environment

VS Code

Git & GitHub

Virtualenv / venv

🧼 Data Cleaning

This project handles real-world farm data containing:

ASCII-encoded dates (e.g., 2025+AC0-11+AC0-18)

Inconsistent column naming

Missing values in milk columns

Non-milking rows (feeding/activity logs)

Cleaning steps include:

Decode malformed date strings

Standardize column names

Filter milking sessions only

Aggregate milk yield by day and by cow

Build a complete daily time series

Forward-fill missing days for forecasting

📊 Analysis & Methods
1. Exploratory Data Analysis (EDA)

Daily trends

Seasonal patterns

Per-cow performance

Production cycles tied to breeding

2. Forecasting Models

ARIMA

SARIMAX

Prophet (optional)

7-day & 30-day forecasts

3. Anomaly Detection

Z-score flagging

Rolling window deviation

Sudden milk drops per cow

Early health-event detection

🚀 How to Run the Project
Step 1 — Clone the repository
git clone https://github.com/witttingtorch/milk-yield-forecasting.git
cd milk-yield-forecasting

Step 2 — Create & activate a virtual environment
python3 -m venv venv
source venv/bin/activate       # Mac/Linux
venv\Scripts\activate          # Windows

Step 3 — Install dependencies
pip install -r requirements.txt

Step 4 — Run the setup script (optional)
chmod +x setup.sh
./setup.sh


This will:

Create folder structure (if missing)

Verify your Python environment

Check required packages

Print next steps

Step 5 — Open notebooks
jupyter notebook


Navigate to:

notebooks/milk_yield_forecasting.ipynb

📈 Outputs

You will find the generated plots in the outputs/ folder:

Daily total yield

Per-cow yield patterns

Forecasted future yield

Seasonal decomposition

Anomaly detection charts

🐄 Dataset Description

Each CSV file contains:

Column	Meaning
Date	Milking date (encoded, cleaned in notebook)
Cow_ID	Name or tag of cow
Activity	Milking / Feeding
Session	Morning / Midday / Evening
Milk_Liters	Milk produced in that session

Plus:

Health events

Pregnancy cycle stages

Breeding records

🎯 Future Work

Feed-to-yield optimization

Breeding-based yield models

LSTM deep-learning forecasting

Dashboard in Power BI / Tableau

👤 Author

Moses Martin Njuguna Gikonyo
GitHub: @witttingtorch