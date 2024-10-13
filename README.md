# Enchanced Bitcoin HMM Trading Bot 
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

To run the trading bot , execute the following command in Your terminal: 

``` bash
python main.py
```

## Customizing the Date Range
You can specify the desired date range for backtesting by modifying the parameters in the EnhancedBitcoinHMMTradingBot class instantiation. The format should be YYYY-MM-DD.

### Example Time Range for Testing:
('2024-07-01', '2024-10-13')

Console Output:
[*********************100%***********************]  1 of 1 completed
Starting Balance: $1000.00
Final Balance: $1459.06
Total Profit/Loss: $459.06
ROI: 45.91%


### A text file named trade_history.txt will be created, containing a detailed record of each trade executed, including:
- Action (BUY, SELL, SHORT, CLOSE SHORT)
- Amount in BTC
- Price at which the order was executed
- Remaining balance after the trade
- Timestamp of the trade
- Profit/Loss (if applicable)

## Trading Strategy
### The trading strategy is based on Hidden Markov Models (HMM) to predict market states. The bot uses historical data to identify transitions between different market conditions, allowing it to adapt its trading strategy dynamically. The key components of the strategy include:

### Market States: The HMM categorizes market conditions into four states:
        - State 0 (BUY): Indicates bullish market conditions where buying is expected to yield profits.
        - State 1 (SELL): Indicates bearish conditions where selling may be beneficial.
        - State 2 (HOLD): Signals a neutral condition, suggesting no immediate action is necessary.
        - State 3 (SHORT): Indicates a downtrend where shorting the asset could result in profits.

    Risk Management: The bot manages risk by limiting exposure to a predetermined percentage of the account balance (default is 2%) for each trade.

    Profit and Loss Calculation: The bot accurately tracks profit or loss upon executing sell or closing short orders, ensuring transparency in trading performance.

## Backtesting Methodology
### The backtesting component simulates trades over historical data. The process includes:

    Feature Engineering: Technical indicators are computed for historical price data.
    Model Training: The HMM model is trained using the engineered features to learn the underlying market dynamics.
    Trade Execution Simulation: The bot generates buy/sell signals based on the predicted states, updating balances and tracking trade history.
    Performance Metrics Calculation: The bot evaluates the strategy by calculating final balance, total profit/loss, and ROI percentage.

## Result Analysis
Below is the summary of trades executed during the specified period (from July 1, 2024, to October 13, 2024)

## Trade History:
### Action |	Amount (BTC)| Price| Remaining Balance| Time	| Profit/Loss

```
Trade History:

BUY | 0.0003 | $61415.07 | $980.00 | 2024-08-02 00:00:00 | N/A
BUY | 0.0003 | $60680.09 | $960.40 | 2024-08-03 00:00:00 | N/A
BUY | 0.0003 | $58116.98 | $941.19 | 2024-08-04 00:00:00 | N/A
BUY | 0.0003 | $53991.46 | $922.37 | 2024-08-05 00:00:00 | N/A
BUY | 0.0003 | $56034.32 | $903.92 | 2024-08-06 00:00:00 | N/A
BUY | 0.0003 | $55027.46 | $885.84 | 2024-08-07 00:00:00 | N/A
SHORT | 0.0003 | $61710.14 | $903.56 | 2024-08-08 00:00:00 | N/A
SHORT | 0.0003 | $60880.11 | $921.63 | 2024-08-09 00:00:00 | N/A
SHORT | 0.0003 | $60945.81 | $940.06 | 2024-08-10 00:00:00 | N/A
SHORT | 0.0003 | $58719.48 | $958.86 | 2024-08-11 00:00:00 | N/A
SHORT | 0.0003 | $59354.52 | $978.04 | 2024-08-12 00:00:00 | N/A
SHORT | 0.0003 | $60609.57 | $997.60 | 2024-08-13 00:00:00 | N/A
SHORT | 0.0003 | $58737.27 | $1017.55 | 2024-08-14 00:00:00 | N/A
SHORT | 0.0004 | $57560.10 | $1037.91 | 2024-08-15 00:00:00 | N/A
SHORT | 0.0004 | $58894.11 | $1058.66 | 2024-08-16 00:00:00 | N/A
SHORT | 0.0004 | $59478.97 | $1079.84 | 2024-08-17 00:00:00 | N/A
SHORT | 0.0004 | $58483.96 | $1101.43 | 2024-08-18 00:00:00 | N/A
SHORT | 0.0004 | $59493.45 | $1123.46 | 2024-08-19 00:00:00 | N/A
SHORT | 0.0004 | $59012.79 | $1145.93 | 2024-08-20 00:00:00 | N/A
SHORT | 0.0004 | $61175.19 | $1168.85 | 2024-08-21 00:00:00 | N/A
SHORT | 0.0004 | $60381.91 | $1192.23 | 2024-08-22 00:00:00 | N/A
SHORT | 0.0004 | $64094.36 | $1216.07 | 2024-08-23 00:00:00 | N/A
SHORT | 0.0004 | $64178.99 | $1240.39 | 2024-08-24 00:00:00 | N/A
SHORT | 0.0004 | $64333.54 | $1265.20 | 2024-08-25 00:00:00 | N/A
SHORT | 0.0004 | $62880.66 | $1290.51 | 2024-08-26 00:00:00 | N/A
SHORT | 0.0004 | $59504.13 | $1316.32 | 2024-08-27 00:00:00 | N/A
BUY | 0.0005 | $56160.49 | $1289.99 | 2024-09-05 00:00:00 | N/A
BUY | 0.0005 | $53948.75 | $1264.19 | 2024-09-06 00:00:00 | N/A
BUY | 0.0005 | $54139.69 | $1238.91 | 2024-09-07 00:00:00 | N/A
BUY | 0.0005 | $54841.57 | $1214.13 | 2024-09-08 00:00:00 | N/A
BUY | 0.0004 | $57019.54 | $1189.84 | 2024-09-09 00:00:00 | N/A
SELL | 0.0043 | $62940.46 | $1459.06 | 2024-09-19 00:00:00 | $25.33

```
