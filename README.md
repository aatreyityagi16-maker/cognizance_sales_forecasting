# Cognizance Sales Forecasting System

**Cognizance Technologies – Level 2 (Intermediate)**

## Objective
Build a forecasting model to predict future sales using historical business data.

## Tools
Python, Pandas, NumPy, Matplotlib, Scikit-learn, Linear Regression.

## Files
- `sales_data.csv` — 36 months of sample historical sales
- `sales_forecasting.py` — cleaning, analysis, model and forecast
- `sales_forecast.png` — prediction chart
- `business_insights_report.md` — business insights

## Workflow
1. Load historical sales data.
2. Clean and sort the dates.
3. Create a monthly time index.
4. Train a Linear Regression model.
5. Forecast the next 6 months.
6. Visualize historical and predicted sales.

## Forecast Preview
```text
      Date  Predicted_Sales
2026-01-01            36186
2026-02-01            36678
2026-03-01            37169
2026-04-01            37661
2026-05-01            38153
2026-06-01            38645
```

## How to Run
```bash
pip install pandas numpy matplotlib scikit-learn
python sales_forecasting.py
```

The sample dataset was created for educational use, which is permitted by the internship task instructions.
