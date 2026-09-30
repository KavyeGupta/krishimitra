import streamlit as st
from utils.gemini_helper import recommend_crops

st.set_page_config(page_title="Crop Advisory | KrishiMitra", page_icon="🌾", layout="wide")

st.title("🌾 Smart Crop & Soil Health Advisor")
st.write("Enter your field and soil parameters to get AI-powered, regenerative crop recommendations.")

# Language selection from sidebar
language = st.sidebar.selectbox(
    "Response Language / भाषा",
    ["English", "हिंदी (Hindi)", "తెలుగు (Telugu)", "தமிழ் (Tamil)", "ಕನ್ನಡ (Kannada)", "मराठी (Marathi)"]
)

st.divider()

# Create a 2-column input layout for a clean form
col1, col2 = st.columns(2)

with col1:
    st.subheader("📍 Location & Season")
    state = st.selectbox(
        "Select State",
        ["Punjab", "Haryana", "Uttar Pradesh", "Madhya Pradesh", "Maharashtra", 
         "Rajasthan", "Gujarat", "Karnataka", "Andhra Pradesh", "Tamil Nadu", 
         "Telangana", "West Bengal", "Bihar", "Odisha", "Other"]
    )
    season = st.selectbox(
        "Current / Upcoming Season",
        ["Kharif (Monsoon: Jun - Oct)", "Rabi (Winter: Nov - Apr)", "Zaid (Summer: Mar - Jun)"]
    )
    water_availability = st.selectbox(
        "Water / Irrigation Source",
        ["Abundant (Canal / Tube well)", "Moderate (Borewell with limited yield)", "Rainfed / Dryland"]
    )
    soil_type = st.selectbox(
        "Soil Texture / Type",
        ["Alluvial Soil (दोमट)", "Black Soil (काली मिट्टी)", "Red Soil (लाल मिट्टी)", 
         "Sandy Loam (बलुई दोमट)", "Clayey Soil (चिकनी मिट्टी)", "Laterite Soil"]
    )

with col2:
    st.subheader("🧪 Soil Health & Nutrients")
    st.caption("Values from your Soil Health Card (or approximate estimates)")
    
    nitrogen = st.select_slider("Nitrogen (N) Level", options=["Low", "Medium", "High"], value="Medium")
    phosphorus = st.select_slider("Phosphorus (P) Level", options=["Low", "Medium", "High"], value="Medium")
    potassium = st.select_slider("Potassium (K) Level", options=["Low", "Medium", "High"], value="Medium")
    
    ph = st.slider("Soil pH Level", min_value=4.5, max_value=9.5, value=6.8, step=0.1, 
                   help="6.0 - 7.5 is neutral/optimal for most crops")

st.divider()

# Action Button
if st.button("🌱 Generate Smart Crop Plan", type="primary", use_container_width=True):
    soil_data = {
        "state": state,
        "season": season,
        "water_availability": water_availability,
        "soil_type": soil_type,
        "nitrogen": nitrogen,
        "phosphorus": phosphorus,
        "potassium": potassium,
        "ph": ph
    }
    
    with st.spinner("🌾 ICAR-grounded AI model is calculating optimal crop rotations & soil regeneration plans..."):
        plan = recommend_crops(soil_data, language)
        st.success("Custom Crop Plan Ready!")
        st.markdown(plan)