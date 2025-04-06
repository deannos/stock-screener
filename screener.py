# === screener.py ===
from config import RISK_FREE_RATE, MARKET_RETURN
from data import fetch_stock_data
from utils import safe_divide, round_or_none, is_valid

def calculate_coe(beta):
    return RISK_FREE_RATE + beta * (MARKET_RETURN - RISK_FREE_RATE)

def screen_stock(symbol):
    data = fetch_stock_data(symbol)
    if not data:
        return None

    coe = calculate_coe(data["beta"])
    fcf_yield = safe_divide(data["fcf"], data["market_cap"])

    roic = data["roic"]
    if is_valid(roic) and is_valid(fcf_yield) and roic > coe and fcf_yield > 0.03:
        return {
            "Stock": data["symbol"],
            "ROIC (%)": round_or_none(roic * 100),
            "Cost of Equity (%)": round_or_none(coe * 100),
            "FCF Yield (%)": round_or_none(fcf_yield * 100),
            "Beta": round_or_none(data["beta"], 2)
        }
    return None
