# === data.py ===

import yfinance as yf
import numpy as np

def fetch_stock_data(symbol):
    """
    Fetches financial data for a given stock symbol using yfinance.

    Returns a dictionary with:
    - ROIC (via ROE proxy)
    - Beta
    - Free Cash Flow
    - Market Capitalization
    """
    try:
        stock = yf.Ticker(symbol)
        info = stock.info

        return {
            "symbol": symbol,
            "roic": info.get("returnOnEquity", np.nan),  # Proxy for ROIC
            "beta": info.get("beta", 1),                 # Default to 1 if missing
            "fcf": info.get("freeCashflow", np.nan),
            "market_cap": info.get("marketCap", np.nan)
        }

    except Exception as e:
        print(f"[ERROR] Failed to fetch data for {symbol}: {e}")
        return None
