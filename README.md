# Long-Term Portfolio Optimization and Risk Analysis

**Project Overview**
This project models long-term investment strategies by analyzing historical financial data. Instead of arbitrary assets, the portfolio is strategically constructed using highly distinct instruments (e.g., S&P 500 for equities, gold for safe-haven, long-term US treasury bonds for stability, and real estate ETFs) to properly observe diverse market behaviors. The goal is to determine the optimal asset allocation that maximizes returns while minimizing risk, providing a practical, data-driven tool for long-term financial planning.

**Applied Numerical Methods and Scientific Analysis**
To satisfy the course requirements, this project implements three distinct numerical methods, alongside rigorous stability and limitation analyses:

1. **Gradient Method / Minimum Finding (Portfolio Optimization):** 
   * **Implementation:** Applying the Markowitz portfolio theory by using gradient descent to find the global minimum of the portfolio variance (risk).
   * **Scientific Analysis:** We will test the algorithm's stability by varying the learning rate (step size). The documentation will visualize how the algorithm converges smoothly with an optimal rate, or fails/oscillates when the rate is set too high or too low.

2. **Data Fitting & Error Propagation (Trend Forecasting):**
   * **Implementation:** Fitting exponential and polynomial trend lines to historical asset prices to forecast long-term growth.
   * **Scientific Analysis:** We will calculate prediction errors and explicitly demonstrate the mathematical limitations of these models during unexpected economic crises (e.g., the 2008 financial crisis or the 2020 market crash), showing how real-world shocks affect mathematical predictions.

3. **Eigenvalues and Eigenvectors (Diversification Check):** 
   * **Implementation:** Performing Principal Component Analysis (PCA) on the covariance matrix of asset returns. 
   * **Scientific Analysis:** By calculating eigenvalues and eigenvectors, we will identify underlying market factors and verify if our strategically chosen assets are truly uncorrelated, mathematically validating our diversification strategy.

**Implementation Details & Task Breakdown**
* **Dynamic Data Acquisition:** Using Python's `yfinance` library to dynamically fetch the last 15-20 years of daily closing prices, upgrading from static CSV files to ensure robust and up-to-date analysis.
* **Algorithm Development:** Building and fine-tuning the three core numerical algorithms (Gradient Descent, Curve Fitting, Eigen-analysis).
* **Visualization:** Creating comprehensive plots including the efficient frontier, mathematical trend lines with confidence intervals, and correlation heatmaps to present the findings professionally.
