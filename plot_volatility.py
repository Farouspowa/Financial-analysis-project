import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv(r"C:\Users\boura\OneDrive\Bureau\financial_project\market_data.csv", index_col="Date", parse_dates=True)

returns = data.pct_change().dropna() * 100

# 20-day rolling annualised volatility
vol = returns.rolling(20).std() * np.sqrt(252)

plt.figure(figsize=(12, 4))
plt.plot(vol["AAPL"], label="AAPL", color="royalblue")
plt.plot(vol["MSFT"], label="MSFT", color="darkorange")
plt.plot(vol["GSPC"], label="S&P 500", color="green")

# Shade COVID crash
plt.axvspan("2020-02-01", "2020-04-30", color="red", alpha=0.15, label="COVID Crash")

# Shade rate hike period
plt.axvspan("2022-01-01", "2022-12-31", color="orange", alpha=0.15, label="Rate Hike Cycle")

plt.title("20-Day Rolling Annualised Volatility (2020–2024)")
plt.ylabel("Annualised Volatility (%)")
plt.xlabel("Date")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(r"C:\Users\boura\OneDrive\Bureau\financial_project\images\rolling_volatility.png", dpi=150)
print("Figure saved.")