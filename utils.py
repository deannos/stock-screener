# === utils.py ===

def safe_divide(numerator, denominator):
    try:
        if numerator is None or denominator in [None, 0]:
            return None
        return numerator / denominator
    except:
        return None

def round_or_none(value, digits=2):
    if value is None:
        return None
    return round(value, digits)

def is_valid(value):
    return value is not None and value != float("nan")
