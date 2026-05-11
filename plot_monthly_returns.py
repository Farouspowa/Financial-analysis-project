import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\boura\OneDrive\Bureau\financial_project\market_data.csv", index_col="Date", parse_dates=True)

returns = data["AAPL"].pct_change().dropna() * 100

# Resample to monthly compounded returns
monthly = returns.resample("ME").apply(lambda x: (1 + x/100).prod() - 1) * 100

colors = ["green" if v >= 0 else "red" for v in monthly]

plt.figure(figsize=(14, 4))
plt.bar(monthly.index, monthly.values, color=colors, width=20)
plt.axhline(0, color="black", linewidth=0.8)
plt.title("AAPL Monthly Returns (2020–2024)")
plt.ylabel("Monthly Return (%)")
plt.xlabel("Date")
plt.grid(True, alpha=0.3, axis="y")
plt.tight_layout()
plt.savefig(r"C:\Users\boura\OneDrive\Bureau\financial_project\images\monthly_returns.png", dpi=150)
print("Figure saved.")