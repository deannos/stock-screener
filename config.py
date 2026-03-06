# === config.py ===

# -------------------------------
# 📊 Sector Mapping by Economic Stage
# -------------------------------
SECTOR_MAP = {
    "Expansion": ["Financials", "IT", "Consumer Goods"],
    "Recession": ["Pharma", "FMCG", "Utilities"],
    "Recovery": ["Industrials", "Auto", "Infra"]
}

# -------------------------------
# 🏦 NSE Stocks Grouped by Sector
# -------------------------------
STOCKS_BY_SECTOR = {
    "IT": ["INFY.NS", "TCS.NS", "WIPRO.NS"],
    "Financials": ["HDFCBANK.NS", "ICICIBANK.NS", "KOTAKBANK.NS"],
    "Consumer Goods": ["ASIANPAINT.NS", "BRITANNIA.NS", "HINDUNILVR.NS"],
    "Pharma": ["SUNPHARMA.NS", "CIPLA.NS", "DIVISLAB.NS"],
    "FMCG": ["HINDUNILVR.NS", "ITC.NS", "DABUR.NS"],
    "Utilities": ["POWERGRID.NS", "NTPC.NS", "RELIANCE.NS"],
    "Industrials": ["LT.NS", "SIEMENS.NS", "BEL.NS"],
    "Auto": ["TATAMOTORS.NS", "EICHERMOT.NS", "BAJAJ-AUTO.NS"],
    "Infra": ["IRCTC.NS", "NBCC.NS", "ADANIPORTS.NS"]
}

# -------------------------------
# 📈 Market Constants for CAPM
# -------------------------------
RISK_FREE_RATE = 0.07            # 10-year Indian Government Bond Yield
MARKET_RETURN = 0.12             # Historical average market return (NIFTY)
MARKET_RISK_PREMIUM = MARKET_RETURN - RISK_FREE_RATE  # = 5%
