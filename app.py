# === app.py ===
import streamlit as st
import pandas as pd
import plotly.express as px
from config import SECTOR_MAP, STOCKS_BY_SECTOR
from screener import screen_stock
from streamlit_extras.metric_cards import style_metric_cards

st.set_page_config(page_title="📈 Fundamental Stock Screener", layout="wide")
st.title("📊 Indian Stock Screener - Macro + Fundamental")

# === Sidebar Controls ===
with st.sidebar:
    st.header("🧭 Strategy Settings")

    macro_stage = st.selectbox("Select Economic Stage", options=list(SECTOR_MAP.keys()))
    default_sectors = SECTOR_MAP[macro_stage]

    risk_appetite = st.radio("Risk Appetite", options=["Low", "Moderate", "High"])
    horizon = st.radio("Investment Horizon", options=["Short-term", "Mid-term", "Long-term"])

    st.markdown("---")
    st.subheader("📌 Fundamental Filters")
    min_roic = st.slider("Minimum ROIC (%)", 0.0, 30.0, 10.0, step=1.0)
    min_fcf_yield = st.slider("Minimum FCF Yield (%)", 0.0, 10.0, 3.0, step=0.5)

    st.markdown("---")
    st.subheader("🔍 Sector Selection")
    sectors_selected = st.multiselect(
        "Choose sectors to screen (or leave default)",
        options=list(STOCKS_BY_SECTOR.keys()),
        default=default_sectors
    )

# === Stock Pool ===
selected_stocks = [s for sector in sectors_selected for s in STOCKS_BY_SECTOR.get(sector, [])]
st.write(f"✅ Screening {len(selected_stocks)} stocks from: {', '.join(sectors_selected)}")

# === Screener Run ===
@st.cache_data(show_spinner=False)
def run_screener():
    results = []
    for symbol in selected_stocks:
        result = screen_stock(symbol, min_roic, min_fcf_yield)
        if result:
            results.append(result)
    return pd.DataFrame(results)

with st.spinner("Running financial filters..."):
    df = run_screener()

# === Results ===
if not df.empty:
    df.sort_values(by="ROIC (%)", ascending=False, inplace=True)
    st.subheader("📋 Screened Stocks")
    st.dataframe(df, use_container_width=True)

    # === Metrics Summary ===
    avg_roic = df["ROIC (%)"].mean()
    avg_fcf = df["FCF Yield (%)"].mean()
    avg_beta = df["Beta"].mean()

    st.markdown("### 📈 Averages (Filtered)")
    col1, col2, col3 = st.columns(3)
    col1.metric("Avg ROIC (%)", f"{avg_roic:.2f}")
    col2.metric("Avg FCF Yield (%)", f"{avg_fcf:.2f}")
    col3.metric("Avg Beta", f"{avg_beta:.2f}")
    style_metric_cards()

    # === Bubble Chart ===
    st.subheader("📉 ROIC vs FCF Yield (Bubble Chart)")
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

    # === CSV Export ===
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Download CSV", csv, "filtered_stocks.csv", "text/csv")

else:
    st.warning("⚠️ No stocks matched the filter. Try adjusting your sliders or sectors.")

