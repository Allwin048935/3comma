import ccxt
import pandas as pd
import asyncio
import nest_asyncio
import requests
import config
from datetime import datetime, timezone

interval = '3m'  # Candlestick interval

# Initialize Binance client
binance = ccxt.binance({
    'apiKey': config.API_KEY,
    'secret': config.API_SECRET,
})

# Dictionary to store the last alert messages for each symbol
last_alert_messages = {}

# Function to get historical candlestick data
def get_historical_data(symbol, interval, limit=100):
    ohlcv = binance.fetch_ohlcv(symbol, interval, limit=limit)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    return df

# Function to calculate Heikin-Ashi candles
def calculate_heikin_ashi(df):
    ha_df = df.copy()
    ha_df['ha_close'] = (df['open'] + df['high'] + df['low'] + df['close']) / 4
    ha_df['ha_open'] = (df['open'].shift(1) + df['close'].shift(1)) / 2
    ha_df['ha_high'] = ha_df[['high', 'ha_open', 'ha_close']].max(axis=1)
    ha_df['ha_low'] = ha_df[['low', 'ha_open', 'ha_close']].min(axis=1)
    ha_df = ha_df.dropna()  # Drop rows with NaN values
    
    # Print last and previous Heikin-Ashi close prices for debugging
    print("Last Heikin-Ashi close price:", ha_df['ha_close'].iloc[-1])
    print("Previous Heikin-Ashi close price:", ha_df['ha_close'].iloc[-2])
    
    return ha_df

# Function to check Heikin-Ashi close price conditions
def check_heikin_ashi_conditions(df):
    if len(df) < 4:
        return False, False
    
    last_close = df['ha_close'].iloc[-1]
    prev_close = df['ha_close'].iloc[-2]
    second_last_close = df['ha_close'].iloc[-3]
    
    long_condition = last_close > prev_close and prev_close > second_last_close
    short_condition = last_close < prev_close and prev_close < second_last_close
    
    return long_condition, short_condition

# Function to get weekly open price (not used in current conditions but retained for completeness)
def get_weekly_open_price(symbol):
    weekly_ohlcv = binance.fetch_ohlcv(symbol, '1w', limit=5)
    df_weekly = pd.DataFrame(weekly_ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df_weekly['timestamp'] = pd.to_datetime(df_weekly['timestamp'], unit='ms')
    df_weekly.set_index('timestamp', inplace=True)
    # Get the open price of the latest weekly candle
    weekly_open_price = df_weekly['close'].iloc[-2]
    return weekly_open_price

# Function to send a message to 3commas using a webhook
def send_3commas_message(symbol, action, close_price):
    if last_alert_messages.get(symbol) != action:
        timestamp = datetime.now(timezone.utc).isoformat()
        payload = {
            "secret": config.SECRET,
            "max_lag": "300",
            "timestamp": timestamp,
            "trigger_price": str(close_price),
            "tv_exchange": "BINANCE",
            "tv_instrument": symbol.replace('/', '') + '.P',
            "action": action,
            "bot_uuid": "3054d7a6-d6ac-4e32-9abb-1f92ca1fa837"
        }

        try:
            url = config.THREE_COMMAS_WEBHOOK_URL
            response = requests.post(url, json=payload)

            if response.status_code == 200:
                print(f"Successfully sent alert for {symbol} with action {action}")
                last_alert_messages[symbol] = action
            else:
                print(f"Failed to send alert for {symbol}: {response.content}")

        except requests.RequestException as e:
            print(f"Error sending request for {symbol}: {e}")

# Main function (now defined as async)
async def main():
    while True:
        for symbol in config.SELECTED_SYMBOLS:
            try:
                # Fetch historical data
                historical_data = get_historical_data(symbol, interval)
                
                # Calculate Heikin-Ashi candles
                heikin_ashi_data = calculate_heikin_ashi(historical_data)
                long_condition, short_condition = check_heikin_ashi_conditions(heikin_ashi_data)

                close_price = heikin_ashi_data['ha_close'].iloc[-1]

                # Determine the action based on Heikin-Ashi close price conditions
                if long_condition:
                    send_3commas_message(symbol, "enter_long", close_price)
                elif short_condition:
                    send_3commas_message(symbol, "enter_short", close_price)

            except Exception as e:
                print(f"Error processing {symbol}: {e}")

        # Sleep for a week (7 days) before checking again
        await asyncio.sleep(604800)  # Sleep for 1 week (in seconds)

# Use nest_asyncio to allow running asyncio in Jupyter notebooks
nest_asyncio.apply()

# Create and run the event loop
asyncio.run(main())
