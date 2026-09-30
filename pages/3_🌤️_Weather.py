import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from utils.weather_api import get_weather_forecast, INDIAN_LOCATIONS
from utils.gemini_helper import generate_weather_advisory

st.set_page_config(page_title="Weather & Agro-Advisory | KrishiMitra", page_icon="🌤️", layout="wide")

st.title("🌤️ Real-Time Weather & Agro-Advisories")
st.write("Live 7-day meteorological forecasts paired with AI farming advisories.")

language = st.sidebar.selectbox(
    "Response Language / भाषा",
    ["English", "हिंदी (Hindi)", "తెలుగు (Telugu)", "தமிழ் (Tamil)", "ಕನ್ನಡ (Kannada)", "मराठी (Marathi)"]
)

st.divider()

# Location Picker
selected_location = st.selectbox("📍 Select Your Agricultural Region", list(INDIAN_LOCATIONS.keys()))
lat, lon = INDIAN_LOCATIONS[selected_location]

if st.button("📡 Fetch Live Forecast & Advisory", type="primary", use_container_width=True):
    with st.spinner(f"Fetching real-time satellite & station meteorology for {selected_location}..."):
        try:
            weather = get_weather_forecast(lat, lon)
            current = weather.get("current", {})
            daily = weather.get("daily", {})

            # 1. Current Snapshot Metrics
            st.subheader(f"Current Conditions in {selected_location}")
            col1, col2, col3 = st.columns(3)
            col1.metric("🌡️ Current Temp", f"{current.get('temperature_2m', 'N/A')} °C")
            col2.metric("💧 Humidity", f"{current.get('relative_humidity_2m', 'N/A')} %")
            col3.metric("💨 Wind Speed", f"{current.get('wind_speed_10m', 'N/A')} km/h")

            st.divider()

            # 2. Interactive 7-Day Dual-Axis Chart (Plotly)
            st.subheader("📊 7-Day Temperature & Precipitation Trend")
            dates = daily.get("time", [])
            t_max = daily.get("temperature_2m_max", [])
            t_min = daily.get("temperature_2m_min", [])
            rain = daily.get("precipitation_sum", [])

            fig = go.Figure()
            # Max Temp line
            fig.add_trace(go.Scatter(
                x=dates, y=t_max, name="Max Temp (°C)", 
                mode="lines+markers", line=dict(color="#d9534f", width=3)
            ))
            # Min Temp line
            fig.add_trace(go.Scatter(
                x=dates, y=t_min, name="Min Temp (°C)", 
                mode="lines+markers", line=dict(color="#0275d8", width=3)
            ))
            # Rainfall bars on secondary axis
            fig.add_trace(go.Bar(
                x=dates, y=rain, name="Rainfall (mm)", 
                marker_color="rgba(91, 192, 222, 0.6)", yaxis="y2"
            ))

            fig.update_layout(
                title=f"7-Day Forecast for {selected_location}",
                xaxis_title="Date",
                yaxis=dict(title="Temperature (°C)"),
                yaxis2=dict(title="Rainfall (mm)", overlaying="y", side="right"),
                legend=dict(orientation="h", yanchor="bottom", y=1.02),
                height=420
            )
            st.plotly_chart(fig, use_container_width=True)

            # 3. AI Generated Agro-Advisory
            st.divider()
            st.subheader("🤖 AI Agro-Meteorological Advisory")
            with st.spinner("Analyzing forecast against crop thresholds..."):
                advisory = generate_weather_advisory(weather, selected_location, language)
                st.markdown(advisory)

        except Exception as e:
            st.error(f"Failed to fetch forecast: {e}")
