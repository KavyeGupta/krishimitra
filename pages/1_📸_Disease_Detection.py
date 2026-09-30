import streamlit as st
from PIL import Image
from utils.gemini_helper import diagnose_crop_disease

st.set_page_config(page_title="Crop Disease Doctor | KrishiMitra", page_icon="📸", layout="wide")

# Custom clean page header & card definition
st.markdown("""
<style>
    .page-banner {
        background: #F4F7F4;
        border-left: 4px solid #2A6E3F;
        border-radius: 6px;
        padding: 1rem 1.2rem;
        margin-bottom: 1.5rem;
    }
    .specimen-box {
        border: 1px dashed #A5BCA9;
        border-radius: 8px;
        padding: 1rem;
        background: #FAFCFA;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

st.title("📸 Crop Disease Diagnostic Laboratory")
st.markdown("""
<div class="page-banner">
    <b>Field Protocol:</b> Provide a clear, well-lit photograph focusing on affected leaves, stems, or fruits. 
    The AI system references visual symptomatology against plant pathology benchmarks to suggest cost-effective treatments.
</div>
""", unsafe_allow_html=True)

language = st.sidebar.selectbox(
    "Language / भाषा",
    ["English", "हिंदी (Hindi)", "తెలుగు (Telugu)", "தமிழ் (Tamil)", "ಕನ್ನಡ (Kannada)", "मराठी (Marathi)"]
)

st.divider()

col_input, col_view = st.columns([1, 1])

image_file = None

with col_input:
    st.subheader("1. Specimen Input")
    st.markdown('<div class="specimen-box">', unsafe_allow_html=True)
    input_method = st.radio("Select input source:", ["Upload Leaf Image", "Use Camera"], horizontal=True)
    
    if input_method == "Upload Leaf Image":
        image_file = st.file_uploader("Upload leaf image (.jpg, .jpeg, .png)", type=["jpg", "jpeg", "png"])
    else:
        image_file = st.camera_input("Capture leaf specimen")
    st.markdown('</div>', unsafe_allow_html=True)

with col_view:
    st.subheader("2. Pathology Evaluation")
    if image_file is not None:
        pil_image = Image.open(image_file)
        st.image(pil_image, caption="Submitted Specimen", use_container_width=True)
        
        diagnose_btn = st.button("🔬 Run Pathology Diagnosis", type="primary", use_container_width=True)
        
        if diagnose_btn:
            with st.spinner("Analyzing cellular chlorosis and lesion patterns..."):
                report = diagnose_crop_disease(pil_image, language)
                st.success("✅ Diagnostic Report Generated")
                st.markdown("---")
                st.markdown(report)
    else:
        st.info("👈 Please upload or capture an image of the plant leaf to begin evaluation.")