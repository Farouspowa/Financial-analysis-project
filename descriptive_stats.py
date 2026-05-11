import pandas as pd

# Load the data
data = pd.read_csv(r"C:\Users\boura\OneDrive\Bureau\financial_project\market_data.csv", index_col="Date", parse_dates=True)

# Compute daily returns in percentage
returns = data.pct_change().dropna() * 100

# Compute statistics
stats = pd.DataFrame({
    "Mean (%)":  returns.mean(),
    "Std (%)":   returns.std(),
    "Min (%)":   returns.min(),
    "Max (%)":   returns.max(),
    "Skewness":  returns.skew(),
    "Kurtosis":  returns.kurt()
}).round(4)

print(stats.to_string())