# 🐄 Milk Yield Forecasting — Dairy Production Analytics

A full end-to-end data analysis and forecasting project using **5+ years** of real dairy farm records.  
The goal is to analyze daily cow performance, detect anomalies, and forecast future milk yield using statistical and machine-learning models.

---

## 📌 Project Overview
This project processes and models:
- Daily milk yield per cow  
- Total herd production  
- Milking sessions (Morning / Midday / Evening)  
- Breeding and pregnancy cycles  
- Health events  
- Sudden milk-yield drops  

The project is built to support:
- Yield forecasting (7-day & 30-day)
- Seasonality & trend detection  
- Cow performance evaluation  
- Feed optimization  
- Anomaly detection for early illness detection  
- Operational & economic planning in dairy farming  

---

## 🗂 Project Structure

```
milk-yield-forecasting/
│
├── data/                # All raw CSV data files
├── notebooks/           # Jupyter notebooks for analysis & modeling
├── outputs/             # Plots, charts, model outputs
├── src/                 # Python scripts (data cleaning, utils)
│    └── __init__.py
│
├── setup.sh             # Script to set up your environment
└── README.md            # Project documentation
```

---

## 🛠 Tools & Technologies

### **Languages & Libraries**
- Python  
  - pandas  
  - numpy  
  - matplotlib  
  - statsmodels  
  - scikit-learn  
  - prophet (optional)

### **Software**
- VS Code  
- Git & GitHub  
- Virtual environments (venv)  

---

## 📈 Methods Used
1. **Data Cleaning & Validation**  
2. **Date repairing (fixing +AC0- encoded issues)**  
3. **Daily aggregation per cow & total herd**  
4. **Time-series modeling (ARIMA / SARIMAX / Prophet)**  
5. **7-day & 30-day forecasting**  
6. **Cow-level performance analytics**  
7. **Anomaly detection for sudden yield drops**  

---

## 🚀 Running the Project

### **Step 1 — Run the setup script**
This creates a virtual environment and installs all required libraries.

```bash
bash setup.sh
source venv/bin/activate
```

### **Step 2 — Open VS Code**
```bash
code .
```

### **Step 3 — Run the notebooks**
All notebooks are located in:

```
notebooks/
```

Open them and run all cells to:
- Clean the data  
- Build the forecasting model  
- Generate plots into `outputs/`  

---

## 🧪 Setup Script Explanation (setup.sh)

Your `setup.sh` does:
1. Creates a virtual environment  
2. Activates it  
3. Installs all project dependencies  

To run it:

```bash
bash setup.sh
source venv/bin/activate
```

---

## 👤 Author
**Moses Martin Njuguna Gikonyo**  
GitHub: [@witttingtorch](https://github.com/witttingtorch)

---

