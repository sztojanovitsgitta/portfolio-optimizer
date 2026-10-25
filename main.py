import numpy as np
import pandas as pd
import yfinance as yf

# 1. Define assets (tickers) and time horizon
tickers = ["SPY", "GLD"]
data = yf.download(tickers, start="2016-01-01", end="2026-10-25")['Close']

# 2. Check data integrity in the console
print("Number of missing values:\n", data.isna().sum())
print("\nFirst 5 rows of historical prices:\n", data.head())

# 3. Calculate daily returns (percentage change)
returns = data.pct_change().dropna()

# 4. Expected returns and covariance matrix (Linear algebra foundation)
mean_returns = returns.mean()
cov_matrix = returns.cov()

print("\n--- Average Daily Returns ---")
print(mean_returns)

print("\n--- Covariance Matrix (Risk & Asset Relationships) ---")
print(cov_matrix)
