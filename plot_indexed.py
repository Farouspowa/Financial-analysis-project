import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\boura\OneDrive\Bureau\financial_project\market_data.csv", index_col="Date", parse_dates=True)

# Base 100 indexing
indexed = data / data.iloc[0] * 100

plt.figure(figsize=(12, 4))
plt.plot(indexed["AAPL"], label="AAPL", color="royalblue")
plt.plot(indexed["MSFT"], label="MSFT", color="darkorange")
plt.plot(indexed["GSPC"], label="S&P 500", color="green")
plt.title("Indexed Price Performance (Base 100, 2020–2024)")
plt.ylabel("Index")
plt.xlabel("Date")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(r"C:\Users\boura\OneDrive\Bureau\financial_project\images\indexed_performance.png", dpi=150)
print("Figure saved.")