import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

data = pd.read_csv(r"C:\Users\boura\OneDrive\Bureau\financial_project\market_data.csv", index_col="Date", parse_dates=True)

returns = data.pct_change().dropna() * 100

df = pd.DataFrame()
df["return"]     = returns["AAPL"]
df["lag1"]       = df["return"].shift(1)
df["lag5"]       = returns["AAPL"].rolling(5).sum().shift(1)
df["vol20"]      = returns["AAPL"].rolling(20).std().shift(1)
df["rel_sp500"]  = (returns["AAPL"] - returns["GSPC"]).shift(1)
df["target"]     = (df["return"] > 0).astype(int)
df.dropna(inplace=True)

features = ["lag1", "lag5", "vol20", "rel_sp500"]
X = df[features]
y = df["target"]

split = int(len(df) * 0.8)
X_train, X_test = X.iloc[:split], X.iloc[split:]
y_train, y_test = y.iloc[:split], y.iloc[split:]

model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Print metrics
print(f"Accuracy:  {accuracy_score(y_test, y_pred):.4f}")
print(f"Precision: {precision_score(y_test, y_pred):.4f}")
print(f"Recall:    {recall_score(y_test, y_pred):.4f}")
print(f"F1-Score:  {f1_score(y_test, y_pred):.4f}")

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(5, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=["Negative (0)", "Positive (1)"],
            yticklabels=["Negative (0)", "Positive (1)"])
plt.title("Confusion Matrix — Logistic Regression (AAPL)")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.tight_layout()
plt.savefig(r"C:\Users\boura\OneDrive\Bureau\financial_project\images\confusion_matrix.png", dpi=150)
print("Confusion matrix saved.")