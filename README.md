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
- [*********************100%***********************]  1 of 1 completed
- Starting Balance: $1000.00
- Final Balance: $1734.49
- Total Profit/Loss: $734.49
- ROI: 73.45%


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
### Action	Amount (BTC)	Price	Remaining Balance	Time	Profit/Loss

```
SHORT | 0.0003 | $67585.25 | $1020.00 | 2024-07-22 00:00:00 | N/A
SHORT | 0.0003 | $65927.67 | $1040.40 | 2024-07-23 00:00:00 | N/A
SHORT | 0.0003 | $65372.13 | $1061.21 | 2024-07-24 00:00:00 | N/A
SHORT | 0.0003 | $65777.23 | $1082.43 | 2024-07-25 00:00:00 | N/A
SHORT | 0.0003 | $67912.06 | $1104.08 | 2024-07-26 00:00:00 | N/A
SHORT | 0.0003 | $67813.34 | $1126.16 | 2024-07-27 00:00:00 | N/A
SHORT | 0.0003 | $68255.87 | $1148.69 | 2024-07-28 00:00:00 | N/A
SHORT | 0.0003 | $66819.91 | $1171.66 | 2024-07-29 00:00:00 | N/A
SHORT | 0.0004 | $66201.02 | $1195.09 | 2024-07-30 00:00:00 | N/A
SHORT | 0.0004 | $64619.25 | $1218.99 | 2024-07-31 00:00:00 | N/A
SHORT | 0.0004 | $65357.50 | $1243.37 | 2024-08-01 00:00:00 | N/A
BUY | 0.0004 | $59027.62 | $1218.51 | 2024-08-28 00:00:00 | N/A
BUY | 0.0004 | $59388.18 | $1194.14 | 2024-08-29 00:00:00 | N/A
BUY | 0.0004 | $59119.48 | $1170.25 | 2024-08-30 00:00:00 | N/A
BUY | 0.0004 | $58969.90 | $1146.85 | 2024-08-31 00:00:00 | N/A
BUY | 0.0004 | $57325.49 | $1123.91 | 2024-09-01 00:00:00 | N/A
BUY | 0.0004 | $59112.48 | $1101.43 | 2024-09-02 00:00:00 | N/A
BUY | 0.0004 | $57431.02 | $1079.40 | 2024-09-03 00:00:00 | N/A
BUY | 0.0004 | $57971.54 | $1057.82 | 2024-09-04 00:00:00 | N/A
SELL | 0.0032 | $56160.49 | $1235.78 | 2024-09-05 00:00:00 | $-5.74
BUY | 0.0004 | $57648.71 | $1211.07 | 2024-09-10 00:00:00 | N/A
BUY | 0.0004 | $57343.17 | $1186.84 | 2024-09-11 00:00:00 | N/A
BUY | 0.0004 | $58127.01 | $1163.11 | 2024-09-12 00:00:00 | N/A
BUY | 0.0004 | $60571.30 | $1139.85 | 2024-09-13 00:00:00 | N/A
BUY | 0.0004 | $60005.12 | $1117.05 | 2024-09-14 00:00:00 | N/A
BUY | 0.0004 | $59182.84 | $1094.71 | 2024-09-15 00:00:00 | N/A
BUY | 0.0004 | $58192.51 | $1072.81 | 2024-09-16 00:00:00 | N/A
BUY | 0.0004 | $60308.54 | $1051.36 | 2024-09-17 00:00:00 | N/A
BUY | 0.0003 | $61649.68 | $1030.33 | 2024-09-18 00:00:00 | N/A
SHORT | 0.0003 | $62940.46 | $1050.94 | 2024-09-19 00:00:00 | N/A
SHORT | 0.0003 | $63192.98 | $1071.96 | 2024-09-20 00:00:00 | N/A
SHORT | 0.0003 | $63394.84 | $1093.39 | 2024-09-21 00:00:00 | N/A
SHORT | 0.0003 | $63648.71 | $1115.26 | 2024-09-22 00:00:00 | N/A
SHORT | 0.0004 | $63329.80 | $1137.57 | 2024-09-23 00:00:00 | N/A
SHORT | 0.0004 | $64301.97 | $1160.32 | 2024-09-24 00:00:00 | N/A
SHORT | 0.0004 | $63143.14 | $1183.52 | 2024-09-25 00:00:00 | N/A
SHORT | 0.0004 | $65181.02 | $1207.20 | 2024-09-26 00:00:00 | N/A
SHORT | 0.0004 | $65790.66 | $1231.34 | 2024-09-27 00:00:00 | N/A
SHORT | 0.0004 | $65887.65 | $1255.97 | 2024-09-28 00:00:00 | N/A
SHORT | 0.0004 | $65635.30 | $1281.09 | 2024-09-29 00:00:00 | N/A
SHORT | 0.0004 | $63329.50 | $1306.71 | 2024-09-30 00:00:00 | N/A
BUY | 0.0004 | $60837.01 | $1280.57 | 2024-10-01 00:00:00 | N/A
BUY | 0.0004 | $60632.79 | $1254.96 | 2024-10-02 00:00:00 | N/A
BUY | 0.0004 | $60759.40 | $1229.86 | 2024-10-03 00:00:00 | N/A
BUY | 0.0004 | $62067.48 | $1205.27 | 2024-10-04 00:00:00 | N/A
BUY | 0.0004 | $62089.95 | $1181.16 | 2024-10-05 00:00:00 | N/A
BUY | 0.0004 | $62818.95 | $1157.54 | 2024-10-06 00:00:00 | N/A
BUY | 0.0004 | $62236.66 | $1134.39 | 2024-10-07 00:00:00 | N/A
BUY | 0.0004 | $62131.97 | $1111.70 | 2024-10-08 00:00:00 | N/A
BUY | 0.0004 | $60582.10 | $1089.46 | 2024-10-09 00:00:00 | N/A
BUY | 0.0004 | $60274.50 | $1067.67 | 2024-10-10 00:00:00 | N/A
BUY | 0.0003 | $62445.09 | $1046.32 | 2024-10-11 00:00:00 | N/A
BUY | 0.0003 | $63193.02 | $1025.40 | 2024-10-12 00:00:00 | N/A

```
