import requests

# Coordinates for major agricultural centers & state hubs across India
INDIAN_LOCATIONS = {
    "Punjab (Ludhiana)": (30.9010, 75.8573),
    "Haryana (Karnal)": (29.6857, 76.9905),
    "Uttar Pradesh (Varanasi)": (25.3176, 82.9739),
    "Uttar Pradesh (Lucknow)": (26.8467, 80.9462),
    "Madhya Pradesh (Indore)": (22.7196, 75.8577),
    "Maharashtra (Nashik)": (19.9975, 73.7898),
    "Maharashtra (Pune)": (18.5204, 73.8567),
    "Gujarat (Ahmedabad)": (23.0225, 72.5714),
    "Rajasthan (Jaipur)": (26.9124, 75.7873),
    "Karnataka (Bengaluru)": (12.9716, 77.5946),
    "Andhra Pradesh (Guntur)": (16.3067, 80.4365),
    "Tamil Nadu (Coimbatore)": (11.0168, 76.9558),
    "Telangana (Hyderabad)": (17.3850, 78.4867),
    "West Bengal (Kolkata)": (22.5726, 88.3639),
    "Bihar (Patna)": (25.6093, 85.1376),
    "Odisha (Bhubaneswar)": (20.2961, 85.8245),
}

def get_weather_forecast(lat: float, lon: float) -> dict:
    """Fetches real-time 7-day agricultural forecast from Open-Meteo."""
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}"
        f"&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,windspeed_10m_max,et0_fao_evapotranspiration"
        f"&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
        f"&timezone=Asia/Kolkata&forecast_days=7"
    )
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()