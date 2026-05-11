import yfinance as yf
import pandas as pd

# Download daily closing prices 2020-2024
tickers = ["AAPL", "MSFT", "^GSPC"]
data = yf.download(tickers, start="2020-01-01", end="2024-12-31")["Close"]

# Rename ^GSPC to GSPC for cleaner column names
data.columns = ["AAPL", "GSPC", "MSFT"]

# Drop any rows with missing values
data.dropna(inplace=True)

# Save to CSV
data.to_csv(r"C:\Users\boura\OneDrive\Bureau\financial_project\market_data.csv")
    
# Verify
print("Download successful.")
print(f"Shape: {data.shape}  (rows=trading days, cols=3 assets)")
print(f"Date range: {data.index[0].date()} to {data.index[-1].date()}")
print("\nFirst 5 rows:")
print(data.head())
print("\nLast 5 rows:")
print(data.tail())
print("\nAny missing values:", data.isnull().sum().sum())