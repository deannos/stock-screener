# === data.py ===
import yfinance as yf
import numpy as np

def fetch_stock_data(symbol):
    try:
        stock = yf.Ticker(symbol)
        info = stock.info

        return {
            "symbol": symbol,
            "roic": info.get("returnOnEquity", np.nan),  # Proxy for ROIC
            "beta": info.get("beta", 1),
            "fcf": info.get("freeCashflow", np.nan),
            "market_cap": info.get("marketCap", np.nan)
        }
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None
