import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv("sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date").reset_index(drop=True)
df["Month_Number"] = np.arange(len(df))

X = df[["Month_Number"]]
y = df["Sales"]

model = LinearRegression()
model.fit(X, y)

future = pd.DataFrame({
    "Month_Number": np.arange(len(df), len(df) + 6)
})
future["Date"] = pd.date_range(
    df["Date"].max() + pd.offsets.MonthBegin(1),
    periods=6,
    freq="MS"
)
future["Predicted_Sales"] = model.predict(
    future[["Month_Number"]]
).round(0)

print("\nNext 6 Months Sales Forecast:")
print(future[["Date", "Predicted_Sales"]].to_string(index=False))

plt.figure(figsize=(10, 5))
plt.plot(df["Date"], df["Sales"], marker="o", label="Historical Sales")
plt.plot(future["Date"], future["Predicted_Sales"],
         marker="o", linestyle="--", label="Forecast")
plt.axvline(df["Date"].max(), linestyle=":")
plt.title("Sales Forecasting System")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.tight_layout()
plt.savefig("sales_forecast.png", dpi=200)
plt.show()
