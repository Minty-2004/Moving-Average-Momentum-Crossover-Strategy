# Moving Average Crossover Strategy with Positive Slope Condition

## Overview

This project implements and backtests a **moving average crossover trading strategy with an additional slope condition** using Python. The strategy generates a **buy signal** when:

1. The **10-day moving average (MA10)** is above the **50-day moving average (MA50)**, and
2. The **50-day moving average has a positive slope** (indicating an upward trend).

---

## How The Strategy Works

1. **Calculate MA10 and MA50** for the chosen stock.
2. **Calculate the slope of MA50** (first difference) to determine its trend direction.
3. **Generate trading signals**:
   - **Long position (buy)** if:
     - MA10 > MA50, and
     - Slope of MA50 > 0
   - **Hold cash (no position)** otherwise.
4. **Backtest the strategy** to evaluate its cumulative returns versus a buy-and-hold benchmark.

---

## Strategy Motivation

1. **MA10 > MA50** suggests recent movement is above long-term average movements.
2. But MA10 **could still be decreasing**, just at a slower rate than MA50.
3. Hence, the MA50 positive slope condition forces a buy signal only if the MA10 and MA50 are **both trending upwards**.
4. This strategy, in theory, works best in **volatile markets with potential extreme losses**, though this strategy may still be applied in other markets.

---

## Technologies Used

- **Python 3**
- `pandas` for data manipulation
- `yfinance` for downloading historical stock data
- `matplotlib` for data visualisation
- `numpy` for numerical calculations
- `datetime` for creating time frames

---

## Results

The backtest plots:

- **Cumulative returns** of the moving average strategy.
- **Cumulative returns** of the buy-and-hold strategy.

This allows performance evaluation against a passive benchmark.

---

## How to Run

1. Clone this repository
2. Install dependencies (see requirements.txt)
3. Run the script (main.py)

---

## Example Output

<img width="1219" alt="Screenshot 2025-07-08 at 1 08 56 pm" src="https://github.com/user-attachments/assets/6c0077ea-0adb-44fb-9810-c57fd3291025" />

---

## Possible Extensions (possibly implemented by me in future projects)

- Optimise MA window lengths for a higher Sharpe ratio.
- Allow the user to **select an end date** rather than automatically end at the current date
- Calculate **annualised returns, volatility, and Sharpe ratio**.
- Include **transaction costs** to simulate real-world profitability.
- Generalise the slope condition to different timeframes or use linear regression slopes.
- Apply the strategy to a portfolio of stocks with rebalancing.

---

## Purpose

This project was created in the early steps of my journey into Financial Analysis with Python. It demonstrates:

- Moving average-based strategy implementation
- Financial data analysis with Python
- Backtesting and performance evaluation

---

## Author

**Muhammad Muntasir Shahzad**  
Student at King's College London, University of London. Studying Mathematics with Management and Finance   
Graduating: Summer 2026  
[LinkedIn Profile](www.linkedin.com/in/muntasir-shahzad) | [Email](muntasir.s.2004@gmail.com)

Please don't hesitate to contact me if you have any questions, suggestions, or otherwise.

---

## Disclaimer

This code is for educational purposes only and does not constitute financial advice or an investment recommendation.
