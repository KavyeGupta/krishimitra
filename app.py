import streamlit as st
from datetime import datetime
import pytz
from utils.gemini_helper import farming_chatbot

st.set_page_config(
    page_title="KrishiMitra 🌾",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------- Real-time IST Clock -----------------
ist = pytz.timezone('Asia/Kolkata')
current_time_ist = datetime.now(ist).strftime("%I:%M %p | %d %b, %Y")

# ----------------- Sidebar -----------------
with st.sidebar:
    st.markdown("### 🌾 KrishiMitra Portal")
    
    # Styled IST Clock Badge
    st.markdown(f"""
    <div style="background: #EBF3ED; border: 1px solid #C6DEC9; 
                border-radius: 8px; padding: 8px 12px; font-size: 0.82rem; 
                color: #1B5E20; font-weight: 700; text-align: center; margin-bottom: 12px;">
        🕒 IST: {current_time_ist}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("**🌐 Language / भाषा**")
    selected_lang = st.selectbox(
        "Choose language",
        ["English", "हिंदी (Hindi)", "తెలుగు (Telugu)", "தமிழ் (Tamil)", "ಕನ್ನಡ (Kannada)", "मराठी (Marathi)"],
        label_visibility="collapsed"
    )
    st.session_state["language"] = selected_lang.split(" ")[0]

    st.divider()
    st.caption("**Build with AI: Code for Communities (Second Edition)**\n\n**Track:** PS 04 Agricultural Intelligence\n**Theme:** Cooperation & Digital Public Good")

# ----------------- Clean Light Theme Styling -----------------
st.markdown("""
<style>
    /* Full Page Background */
    .stApp {
        background-color: #FFFFFF !important;
        color: #1C281F !important;
    }
    
    /* Header Container */
    .header-box {
        background: #F1F6F2;
        border-left: 5px solid #2E7D32;
        border-radius: 8px;
        padding: 1.3rem 1.6rem;
        margin-bottom: 2rem;
        border-top: 1px solid #D7E3D8;
        border-right: 1px solid #D7E3D8;
        border-bottom: 1px solid #D7E3D8;
    }
    .header-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1B5E20;
        margin: 0;
    }
    .header-desc {
        font-size: 1rem;
        color: #4F6354;
        margin-top: 0.5rem;
        margin-bottom: 0;
        line-height: 1.5;
    }
    
    /* Feature Module Cards */
    .module-card {
        background: #F8FAF8;
        border: 1px solid #D7E3D8;
        border-radius: 10px;
        padding: 1.4rem;
        margin-bottom: 1rem;
        min-height: 140px;
        transition: transform 0.15s ease, border-color 0.15s ease;
    }
    .module-card:hover {
        border-color: #2E7D32;
        transform: translateY(-2px);
    }
    .module-title {
        font-size: 1.18rem;
        font-weight: 700;
        color: #2E7D32;
        margin-bottom: 0.4rem;
    }
    .module-text {
        font-size: 0.93rem;
        color: #4F6354;
        line-height: 1.45;
        margin: 0;
    }
    
    /* Badge */
    .badge-pill {
        background: #E1EDE3;
        color: #1B5E20;
        padding: 5px 12px;
        border-radius: 50px;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.5px;
    }
</style>
""", unsafe_allow_html=True)

# ----------------- Header Banner -----------------
st.markdown("""
<div class="header-box">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <span class="header-title">🌾 KrishiMitra (कृषिमित्र)</span>
        <span class="badge-pill">DIGITAL PUBLIC GOOD</span>
    </div>
    <p class="header-desc">
        National Agricultural Intelligence Network providing small and marginal farmers with real-time agronomic guidance, 
        soil diagnostics, and transparent APMC market intelligence.
    </p>
</div>
""", unsafe_allow_html=True)

# ----------------- 4 Module Cards -----------------
st.markdown("### 🚜 Agricultural Decision Support Modules")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="module-card">
        <div class="module-title">📸 Crop Disease Doctor</div>
        <p class="module-text">
            Upload or capture leaf images to detect fungal, bacterial, or pest infestations with practical chemical & organic treatment schedules.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="module-card">
        <div class="module-title">🌤️ Meteorological Field Advisories</div>
        <p class="module-text">
            7-day temperature and precipitation forecasting paired with AI warnings on soil saturation, irrigation scheduling, and pesticide spray timing.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="module-card">
        <div class="module-title">🌾 Soil Health & Crop Rotation Plan</div>
        <p class="module-text">
            Translate Soil Health Card readings (N-P-K, pH) into customized, regenerative crop rotations and balanced organic fertilizer schedules.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="module-card">
        <div class="module-title">💰 Mandi Market Rate Intelligence</div>
        <p class="module-text">
            Benchmark APMC wholesale price spreads across Indian mandis with strategic advice on whether to sell immediately or store produce.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ----------------- Advisory Desk -----------------
st.markdown("### 💬 Vernacular Farmer Advisory Desk")
st.caption("Ask questions about sowing schedules, crop protection, pest management, or government schemes.")

user_query = st.text_input(
    "Type your query:",
    placeholder="e.g., When is the best time to sow mustard in Rajasthan? / सरसों की बुवाई का सही समय क्या है?",
    label_visibility="collapsed"
)

if st.button("Consult Agronomist AI", type="primary"):
    if user_query.strip():
        with st.spinner("Consulting agricultural repository..."):
            answer = farming_chatbot(user_query, selected_lang)
            st.markdown("---")
            st.markdown(answer)
    else:
        st.warning("Please type a question before submitting.")

# Footer
st.divider()
st.caption("🌾 KrishiMitra · Built for Build with AI: Code for Communities (Second Edition) · Grounded in ICAR guidelines")