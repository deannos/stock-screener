# === app.py ===
import streamlit as st
import pandas as pd
import plotly.express as px
from config import SECTOR_MAP, STOCKS_BY_SECTOR
from screener import screen_stock

st.set_page_config(page_title="📈 Fundamental Stock Screener", layout="wide")
st.title("📊 Indian Stock Screener - Macro + Fundamental")

# User Inputs
macro_stage = st.selectbox("Select Economic Stage", options=list(SECTOR_MAP.keys()))
risk_appetite = st.radio("Risk Appetite", options=["Low", "Moderate", "High"])
horizon = st.radio("Investment Horizon", options=["Short-term", "Mid-term", "Long-term"])

# Pool stocks
selected_sectors = SECTOR_MAP[macro_stage]
st.write(f"### Selected Sectors: {', '.join(selected_sectors)}")

all_stocks = [s for sector in selected_sectors for s in STOCKS_BY_SECTOR[sector]]

# Run screener
results = []
progress = st.progress(0)

for idx, symbol in enumerate(all_stocks):
    result = screen_stock(symbol)
    if result:
        results.append(result)
    progress.progress((idx + 1) / len(all_stocks))

# Show results
df = pd.DataFrame(results)
if not df.empty:
    df.sort_values(by="ROIC (%)", ascending=False, inplace=True)
    st.dataframe(df, use_container_width=True)

    # Optional: Download CSV
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download CSV", csv, "filtered_stocks.csv", "text/csv")

    # Optional: ROIC vs FCF Yield chart
    st.subheader("📉 ROIC vs FCF Yield")
    fig = px.scatter(
        df,
        x="FCF Yield (%)",
        y="ROIC (%)",
        size="Beta",
        hover_name="Stock",
        title="Fundamentals Bubble Chart",
        color="Stock"
    )
    st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("No stocks matched the filter. Try adjusting your parameters.")
