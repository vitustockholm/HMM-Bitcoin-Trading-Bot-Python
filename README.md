markdown

# Enhanced Bitcoin HMM Trading Bot written in PYTHON 

## Overview
The Enhanced Bitcoin HMM Trading Bot is a sophisticated trading algorithm designed to leverage the Hidden Markov Model (HMM) for predicting Bitcoin price movements. By analyzing historical price data, the bot identifies market states and generates trading signals, enabling users to make informed trading decisions. This bot utilizes advanced feature engineering and a comprehensive backtesting framework to assess the effectiveness of its trading strategy.

## Features
- **Data Fetching**: Downloads historical Bitcoin price data from Yahoo Finance.
- **Feature Engineering**: Computes essential technical indicators such as:
    - Returns
    - Moving Averages (MA)
    - Relative Strength Index (RSI)
    - Volatility
    - Average True Range (ATR)
        
- **Model Training**: Employs HMM for market state predictions based on price data and computed indicators.
- **Trading Logic**: Executes BUY, SELL, SHORT, and CLOSE SHORT trades based on predicted states.
- **Backtesting**: Simulates trades over historical data to evaluate strategy performance, calculating metrics like ROI, total profit/loss, and final balance.
- **Trade History Logging**: Records each trade in a text file, detailing action, amount, price, timestamp, and profit/loss.

## Installation
To set up and run the Enhanced Bitcoin HMM Trading Bot, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/HMM-Bitcoin-Trading-Bot-Python.git
    cd HMM-Bitcoin-Trading-Bot-Python
    ```

2. **Set Up a Python Environment**: It is recommended to use a virtual environment to manage dependencies.
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Required Packages**: Install the necessary libraries using pip:
    ```bash
    pip install numpy pandas yfinance sklearn hmmlearn
    ```

## Usage
To run the trading bot, execute the following command in your terminal:
```bash
python main.py

Customizing the Date Range

You can specify the desired date range for backtesting by modifying the parameters in the EnhancedBitcoinHMMTradingBot class instantiation. The format should be YYYY-MM-DD.

From time range at test ('2024-07-01', '2024-10-13')
Console Output was:

markdown

[*********************100%***********************]  1 of 1 completed
Starting Balance: $1000.00
Final Balance: $1819.08
Total Profit/Loss: $819.08
ROI: 81.91%

A text file named trade_history.txt will be created, containing a detailed record of each trade executed, including:

    Action (BUY, SELL, SHORT, CLOSE SHORT)
    Amount in BTC
    Price at which the order was executed
    Remaining balance after the trade
    Timestamp of the trade
    Profit/Loss (if applicable)

Trading Strategy

The trading strategy is based on Hidden Markov Models (HMM) to predict market states. The bot uses historical data to identify transitions between different market conditions, allowing it to adapt its trading strategy dynamically. The key components of the strategy include:

    Market States: The HMM categorizes market conditions into four states:
        State 0 (BUY): Indicates bullish market conditions where buying is expected to yield profits.
        State 1 (SELL): Indicates bearish conditions where selling may be beneficial.
        State 2 (HOLD): Signals a neutral condition, suggesting no immediate action is necessary.
        State 3 (SHORT): Indicates a downtrend where shorting the asset could result in profits.

    Risk Management: The bot manages risk by limiting exposure to a predetermined percentage of the account balance (default is 2%) for each trade.

    Profit and Loss Calculation: The bot accurately tracks profit or loss upon executing sell or closing short orders, ensuring transparency in trading performance.

Backtesting Methodology

The backtesting component simulates trades over historical data. The process includes:

    Feature Engineering: Technical indicators are computed for historical price data.
    Model Training: The HMM model is trained using the engineered features to learn the underlying market dynamics.
    Trade Execution Simulation: The bot generates buy/sell signals based on the predicted states, updating balances and tracking trade history.
    Performance Metrics Calculation: The bot evaluates the strategy by calculating final balance, total profit/loss, and ROI percentage.

Result Analysis

Below is the summary of trades executed during the specified period (from July 1, 2024, to October 13, 2024):

Trade History:
Action	Amount (BTC)	Price	Remaining Balance	Time	Profit/Loss
SHORT	0.0003	$61415.07	$1020.00	2024-08-02 00:00:00	N/A
SHORT	0.0003	$60680.09	$1040.40	2024-08-03 00:00:00	N/A
SHORT	0.0004	$58116.98	$1061.21	2024-08-04 00:00:00	N/A
BUY	0.0003	$61710.14	$1039.98	2024-08-08 00:00:00	N/A
BUY	0.0003	$60880.11	$1019.18	2024-08-09 00:00:00	N/A
BUY	0.0003	$60945.81	$998.80	2024-08-10 00:00:00	N/A
BUY	0.0003	$58719.48	$978.82	2024-08-11 00:00:00	N/A
BUY	0.0003	$59354.52	$959.25	2024-08-12 00:00:00	N/A
BUY	0.0003	$60609.57	$940.06	2024-08-13 00:00:00	N/A
BUY	0.0003	$58737.27	$921.26	2024-08-14 00:00:00	N/A
BUY	0.0003	$57560.10	$902.84	2024-08-15 00:00:00	N/A
BUY	0.0003	$58894.11	$884.78	2024-08-16 00:00:00	N/A
BUY	0.0003	$59478.97	$867.08	2024-08-17 00:00:00	N/A
BUY	0.0003	$58483.96	$849.74	2024-08-18 00:00:00	N/A
BUY	0.0003	$59493.45	$832.75	2024-08-19 00:00:00	N/A
BUY	0.0003	$59012.79	$816.09	2024-08-20 00:00:00	N/A
BUY	0.0003	$61175.19	$799.77	2024-08-21 00:00:00	N/A
BUY	0.0003	$60381.91	$783.78	2024-08-22 00:00:00	N/A
BUY	0.0002	$64094.36	$768.10	2024-08-23 00:00:00	N/A
BUY	0.0002	$64178.99	$752.74	2024-08-24 00:00:00	N/A
BUY	0.0002	$64333.54	$737.68	2024-08-25 00:00:00	N/A
BUY	0.0002	$62880.66	$722.93	2024-08-26 00:00:00	N/A
BUY	0.0002	$59504.13	$708.47	2024-08-27 00:00:00	N/A
SHORT	0.0002	$59027.62	$722.		
