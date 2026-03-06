# === screener.py ===

from data import fetch_stock_data
from utils import safe_divide, round_or_none, is_valid
from config import RISK_FREE_RATE, MARKET_RISK_PREMIUM

def screen_stock(symbol, min_roic=0.10, min_fcf_yield=0.03):
    """
    Screens a stock based on fundamental metrics:
    - ROIC vs Cost of Equity (CoE)
    - Free Cash Flow Yield (FCF/Market Cap)
    
    Returns a dictionary of screened stock data if it passes the filters.
    """
    info = fetch_stock_data(symbol)
    if not info:
        return None

    # === Extract raw data ===
    roic = info.get("roic")               # Proxy via ROE
    beta = info.get("beta", 1)
    fcf = info.get("fcf")
    market_cap = info.get("market_cap")

    # === Calculate derived metrics ===
    coe = RISK_FREE_RATE + beta * MARKET_RISK_PREMIUM
    fcf_yield = safe_divide(fcf, market_cap)

    # === Validate input ===
    if not all(map(is_valid, [roic, coe, fcf_yield])):
        return None

    # === Apply filters ===
    if roic > coe and fcf_yield > min_fcf_yield and roic > min_roic:
        return {
            "Stock": symbol,
            "ROIC (%)": round_or_none(roic * 100),
            "Cost of Equity (%)": round_or_none(coe * 100),
            "FCF Yield (%)": round_or_none(fcf_yield * 100),
            "Beta": round_or_none(beta)
        }

    return None
