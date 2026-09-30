import os
import google.generativeai as genai
import streamlit as st
from PIL import Image

def configure_gemini():
    api_key = None
    try:
        api_key = st.secrets.get("GEMINI_API_KEY") or st.secrets.get("GOOGLE_API_KEY")
    except Exception:
        pass
    
    if not api_key:
        api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        
    if not api_key:
        st.error("Missing Gemini API Key! Please set it in Streamlit Secrets or .env")
        return None
        
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("gemini-1.5-flash")

def farming_chatbot(question: str, language: str = "English") -> str:
    model = configure_gemini()
    if not model:
        return "API Key not configured."
    
    prompt = f"""You are KrishiMitra, an expert agricultural advisor for Indian farmers.
Answer the following farming question clearly, practically, and empathetically.
Respond strictly in {language}.
Include organic alternatives, proper seasonal timings, and estimated costs in ₹ where helpful.

Question: {question}
"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        if "429" in str(e):
            return "⏳ **Rate limit reached:** Google Gemini Free Tier allows a few requests per minute. Please wait 20-30 seconds and try again!"
        return f"Error connecting to AI: {e}"

def diagnose_crop_disease(image: Image.Image, language: str = "English") -> str:
    model = configure_gemini()
    if not model:
        return "API Key not configured."

    prompt = f"""You are an expert plant pathologist advising Indian farmers.
Analyze this crop/leaf image:
1. **Crop Name**: Identify the crop.
2. **Condition**: Healthy or Diseased?
3. **Disease Name**: (if any)
4. **Symptoms Observed**: Briefly describe what you see.
5. **Immediate Treatment**: Practical, affordable steps (organic & chemical).
6. **Prevention**: How to prevent recurrence.

Respond strictly in {language}.
If the image is not a plant, politely ask for a clear photo of a plant leaf.
"""
    try:
        response = model.generate_content([prompt, image])
        return response.text
    except Exception as e:
        if "429" in str(e):
            return "⏳ **Rate limit reached:** Please wait 20-30 seconds and click Diagnose again!"
        return f"Error diagnosing disease: {e}"

def recommend_crops(soil_data: dict, language: str = "English") -> str:
    model = configure_gemini()
    if not model:
        return "API Key not configured."

    prompt = f"""You are a senior agronomist at the Indian Council of Agricultural Research (ICAR).
Based on the farmer's soil and geographic conditions below, provide a comprehensive, climate-resilient crop plan:

- State/Region: {soil_data.get('state')}
- Season: {soil_data.get('season')}
- Soil Type: {soil_data.get('soil_type')}
- Nitrogen (N): {soil_data.get('nitrogen')}
- Phosphorus (P): {soil_data.get('phosphorus')}
- Potassium (K): {soil_data.get('potassium')}
- Soil pH: {soil_data.get('ph')}
- Water Availability: {soil_data.get('water_availability')}

Please structure your response clearly:
1. **Top 3 Recommended Crops**: Explain why each is suitable for these specific soil nutrients and season.
2. **Soil Health & Regeneration Plan**: How to balance N-P-K, improve soil organic carbon, and recommended organic fertilizers (e.g. FYM, Vermicompost, Biofertilizers).
3. **Water & Irrigation Advice**: Frequency and techniques (e.g. drip, furrow).
4. **Estimated Economics**: Approximate investment cost and estimated return per acre in Indian Rupees (₹).

Respond strictly in {language}. Keep the tone encouraging, practical, and tailored to Indian farming realities.
"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        if "429" in str(e):
            return "⏳ **Rate limit reached:** Please wait 20-30 seconds and try again!"
        return f"Error generating plan: {e}"

def generate_weather_advisory(weather_data: dict, location_name: str, language: str = "English") -> str:
    model = configure_gemini()
    if not model:
        return "API Key not configured."

    daily = weather_data.get("daily", {})
    prompt = f"""You are an agricultural meteorologist advising farmers in {location_name}, India.
Here is the 7-day weather forecast:
- Dates: {daily.get('time', [])}
- Max Temp (°C): {daily.get('temperature_2m_max', [])}
- Min Temp (°C): {daily.get('temperature_2m_min', [])}
- Expected Rainfall (mm): {daily.get('precipitation_sum', [])}

Provide an actionable, 7-day Agro-Advisory:
1. **Weather Outlook**: Quick summary.
2. **Irrigation Planning**: When to water vs. pause.
3. **Pest & Disease Warning**: Conditions favoring outbreaks.
4. **Fieldwork Advice**: Best days for spraying/fertilizing.

Respond strictly in {language}.
"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        if "429" in str(e):
            return "⏳ **Rate limit reached:** Please wait 20-30 seconds and try again!"
        return f"Error generating advisory: {e}"
def generate_mandi_advisory(market_data_summary: str, question: str, language: str = "English") -> str:
    """Uses Gemini to act as a farm trade analyst guiding farmers on pricing and storage."""
    model = configure_gemini()
    if not model:
        return "API Key not configured."

    prompt = f"""You are an agricultural economist advising Indian farmers on market trends and crop trading.
Here is the current market pricing context (in ₹ per Quintal):
{market_data_summary}

Farmer's question or intent:
"{question}"

Please provide actionable trade intelligence:
1. **Current Market Assessment**: Are modal prices favorable, average, or low compared to historical benchmarks?
2. **Sell vs. Hold Recommendation**: Should the farmer sell immediately at the Mandi, wait, or explore cold storage?
3. **Value Addition & Grading**: How cleaning, grading, or direct-to-FPO / e-NAM sale could increase their margin.
4. **Transport & Mandi Strategy**: Tips on reducing intermediary commission and transport losses.

Respond strictly in {language}. Keep the tone empowering, practical, and grounded in Indian market dynamics.
"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        if "429" in str(e):
            return "⏳ **Rate limit reached:** Please wait 20-30 seconds and try again!"
        return f"Error generating trade advisory: {e}"