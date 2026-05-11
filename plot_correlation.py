import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"C:\Users\boura\OneDrive\Bureau\financial_project\market_data.csv", index_col="Date", parse_dates=True)

returns = data.pct_change().dropna() * 100

corr = returns.corr()

plt.figure(figsize=(5, 4))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm",
            vmin=-1, vmax=1, linewidths=0.5,
            xticklabels=["AAPL", "GSPC", "MSFT"],
            yticklabels=["AAPL", "GSPC", "MSFT"])
plt.title("Pearson Correlation of Daily Returns (2020–2024)")
plt.tight_layout()
plt.savefig(r"C:\Users\boura\OneDrive\Bureau\financial_project\images\correlation_heatmap.png", dpi=150)
print("Figure saved.")