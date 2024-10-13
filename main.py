import numpy as np
import pandas as pd
from hmmlearn import hmm
import yfinance as yf
from sklearn.preprocessing import StandardScaler

class EnhancedBitcoinHMMTradingBot:
    def __init__(self, start_date, end_date, retrain_freq=30):
        self.symbol = 'BTC-USD'
        self.start_date = start_date
        self.end_date = end_date
        self.retrain_freq = retrain_freq
        self.model = None
        self.scaler = StandardScaler()
        self.data = None
        self.n_components = 4

    def fetch_data(self):
        self.data = yf.download(self.symbol, start=self.start_date, end=self.end_date)
        return self.data

    def engineer_features(self):
        df = self.data.copy()
        df['Returns'] = df['Close'].pct_change()
        df['MA5'] = df['Close'].rolling(window=5).mean()
        df['RSI'] = self.calculate_rsi(df['Close'], 14)
        df['Volatility'] = df['Returns'].rolling(window=20).std()
        df['ATR'] = self.calculate_atr(df)
        
        # Check if DataFrame is empty after feature engineering
        if df.isnull().values.all():
            raise ValueError("No valid data points after feature engineering.")
        
        return df.dropna()

    def calculate_rsi(self, prices, period=14):
        delta = prices.diff()
        gain = delta.where(delta > 0, 0).rolling(window=period).mean()
        loss = -delta.where(delta < 0, 0).rolling(window=period).mean()
        rs = gain / loss
        return 100 - (100 / (1 + rs))

    def calculate_atr(self, data, period=14):
        high_low = data['High'] - data['Low']
        high_close = np.abs(data['High'] - data['Close'].shift())
        low_close = np.abs(data['Low'] - data['Close'].shift())
        true_range = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
        return true_range.rolling(window=period).mean()

    def prepare_features(self, df):
        features = df[['Returns', 'MA5', 'RSI', 'Volatility', 'ATR']]
        
        # Validate features before scaling
        if features.shape[0] == 0:
            raise ValueError("No valid features to scale.")
        
        scaled_features = self.scaler.fit_transform(features)
        return scaled_features

    def train_model(self):
        df = self.fetch_data()
        
        # Check if data is empty after fetching
        if df.empty:
            raise ValueError("No data found for the specified date range.")

        df_engineered = self.engineer_features()
        X = self.prepare_features(df_engineered)

        # Train the HMM model
        self.model = hmm.GaussianHMM(n_components=self.n_components, covariance_type="diag", n_iter=2000, tol=1e-4)
        self.model.fit(X)

    def predict_state(self, features):
        return self.model.predict(features)

    def generate_signal(self, current_state):
        if current_state == 0:
            return 'BUY'
        elif current_state == 1:
            return 'SELL'
        elif current_state == 2:
            return 'HOLD'
        elif current_state == 3:
            return 'SHORT'
        return 'HOLD'

    def backtest(self, initial_balance=1000, risk_per_trade=0.02):
        df = self.engineer_features()
        X = self.prepare_features(df)
        states = self.predict_state(X)

        balance = initial_balance
        start_balance = initial_balance
        btc_balance = 0
        trades = []

        for i in range(1, len(states)):
            signal = self.generate_signal(states[i])
            price = df['Close'].iloc[i]
            trade_value = balance * risk_per_trade

            if signal == 'BUY' and balance >= trade_value:
                btc_to_buy = trade_value / price
                balance -= btc_to_buy * price
                btc_balance += btc_to_buy
                trades.append(('BUY', btc_to_buy, price, balance, df.index[i]))

            elif signal == 'SELL' and btc_balance > 0:
                sell_value = btc_balance * price
                profit_loss = sell_value - (btc_balance * trades[-1][2]) if trades and trades[-1][0] == 'BUY' else 0
                balance += sell_value
                trades.append(('SELL', btc_balance, price, balance, df.index[i], profit_loss))
                btc_balance = 0

            elif signal == 'SHORT' and balance >= trade_value:
                btc_to_sell = trade_value / price
                balance += btc_to_sell * price
                trades.append(('SHORT', btc_to_sell, price, balance, df.index[i]))

            elif signal == 'CLOSE SHORT' and trades and trades[-1][0] == 'SHORT':
                btc_to_close_short = trades[-1][1]  # Amount from the last SHORT trade
                buy_back_value = btc_to_close_short * price
                profit_loss = (btc_to_close_short * trades[-1][2]) - buy_back_value  # Calculate profit/loss
                balance += btc_to_close_short * price
                trades.append(('CLOSE SHORT', btc_to_close_short, price, balance, df.index[i], profit_loss))

        # Calculate final balance
        final_balance = balance + btc_balance * df['Close'].iloc[-1]
        total_profit_loss = final_balance - start_balance
        roi = (total_profit_loss / start_balance) * 100

        return start_balance, final_balance, total_profit_loss, roi, trades

    def run_bot(self):
        self.train_model()
        start_balance, final_balance, total_profit_loss, roi, trades = self.backtest()

        # Print summary in terminal
        print(f"Starting Balance: ${start_balance:.2f}")
        print(f"Final Balance: ${final_balance:.2f}")
        print(f"Total Profit/Loss: ${total_profit_loss:.2f}")
        print(f"ROI: {roi:.2f}%\n")

        # Save trade history to a text file
        with open('trade_history.txt', 'w') as f:
            f.write("Trade History:\n")
            f.write("Action | Amount (BTC) | Price | Remaining Balance | Time | Profit/Loss\n")
            for trade in trades:
                if len(trade) == 6:  # Trade has profit/loss
                    action, btc_amount, price, balance, time, profit_loss = trade
                    f.write(f"{action} | {btc_amount:.4f} | ${price:.2f} | ${balance:.2f} | {time} | ${profit_loss:.2f}\n")
                else:  # Trade without profit/loss
                    action, btc_amount, price, balance, time = trade
                    f.write(f"{action} | {btc_amount:.4f} | ${price:.2f} | ${balance:.2f} | {time} | N/A\n")

        return final_balance, total_profit_loss, trades

# Usage
bot = EnhancedBitcoinHMMTradingBot('2024-07-01', '2024-10-13')
try:
    final_balance, total_profit_loss, trades = bot.run_bot()
except ValueError as e:
    print(f"Error: {e}")
