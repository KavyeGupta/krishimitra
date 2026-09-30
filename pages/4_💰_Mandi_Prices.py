import streamlit as st
import plotly.express as px
from utils.mandi_data import get_mandi_data, get_unique_states, get_unique_commodities
from utils.gemini_helper import generate_mandi_advisory

st.set_page_config(page_title="Mandi Prices & Intelligence | KrishiMitra", page_icon="💰", layout="wide")

st.title("💰 Mandi Market Prices & Trade Intelligence")
st.write("Track real-time benchmark crop prices across APMC mandis and get AI-driven selling strategies.")

language = st.sidebar.selectbox(
    "Response Language / भाषा",
    ["English", "हिंदी (Hindi)", "తెలుగు (Telugu)", "தமிழ் (Tamil)", "ಕನ್ನಡ (Kannada)", "मराठी (Marathi)"]
)

st.divider()

# Filters Row
col1, col2 = st.columns(2)
with col1:
    selected_state = st.selectbox("🏛️ Filter by State", get_unique_states())
with col2:
    selected_commodity = st.selectbox("🌾 Filter by Commodity", get_unique_commodities())

# Load Filtered Data
df = get_mandi_data(selected_state, selected_commodity)

# Metrics Summary Bar
c1, c2, c3, c4 = st.columns(4)
c1.metric("📍 Mandi Records", len(df))
c2.metric("💰 Average Modal Price", f"₹{df['Modal_Price'].mean():,.0f} / Q" if len(df) > 0 else "N/A")
c3.metric("📈 Highest Modal Price", f"₹{df['Modal_Price'].max():,.0f} / Q" if len(df) > 0 else "N/A")
c4.metric("📉 Lowest Modal Price", f"₹{df['Modal_Price'].min():,.0f} / Q" if len(df) > 0 else "N/A")

st.divider()

# Interactive Price Comparison Chart (Plotly)
st.subheader("📊 Price Spread: Minimum vs. Modal vs. Maximum (₹/Quintal)")
if len(df) > 0:
    fig = px.bar(
        df,
        x="Market",
        y=["Min_Price", "Modal_Price", "Max_Price"],
        barmode="group",
        color_discrete_map={"Min_Price": "#d9534f", "Modal_Price": "#5cb85c", "Max_Price": "#0275d8"},
        labels={"value": "Price (₹ / Quintal)", "variable": "Price Type", "Market": "APMC Mandi Yard"},
        title=f"Market Prices for {selected_commodity if selected_commodity != 'All' else 'Selected Commodities'}"
    )
    st.plotly_chart(fig, use_container_width=True)

    # Detailed Table
    st.subheader("📋 APMC Market Rate Card")
    st.dataframe(df, use_container_width=True, hide_index=True)
else:
    st.warning("No market data matching your specific filter combination. Try selecting 'All' to view other records.")

# AI Selling Strategy Advisor
st.divider()
st.subheader("🤖 AI Farm Trade Advisor (Sell vs. Store Strategy)")
trade_query = st.text_input(
    "Ask advice on when and where to sell:",
    placeholder="e.g., Should I sell my Lasalgaon onions now or store them for a few weeks?"
)

if st.button("📈 Get AI Market Strategy", type="primary"):
    if trade_query.strip():
        # Summarize the currently visible data for Gemini context
        data_summary = df.to_string(index=False)
        with st.spinner("AI Trade Analyst is evaluating price trends and seasonal patterns..."):
            advice = generate_mandi_advisory(data_summary, trade_query, language)
            st.markdown(advice)
    else:
        st.warning("Please enter your question or crop query first!")