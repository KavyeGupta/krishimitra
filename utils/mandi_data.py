import pandas as pd

# Real-world benchmark Mandi price dataset based on Agmarknet (Ministry of Agriculture)
MANDI_RECORDS = [
    {"State": "Punjab", "District": "Ludhiana", "Market": "Ludhiana Mandi", "Commodity": "Wheat", "Variety": "Lokwan", "Min_Price": 2200, "Max_Price": 2450, "Modal_Price": 2350},
    {"State": "Punjab", "District": "Amritsar", "Market": "Amritsar Mandi", "Commodity": "Wheat", "Variety": "Kalyan Sona", "Min_Price": 2180, "Max_Price": 2400, "Modal_Price": 2320},
    {"State": "Haryana", "District": "Karnal", "Market": "Karnal Mandi", "Commodity": "Basmati Rice", "Variety": "Pusa 1121", "Min_Price": 3700, "Max_Price": 4500, "Modal_Price": 4200},
    {"State": "Uttar Pradesh", "District": "Lucknow", "Market": "Lucknow Mandi", "Commodity": "Potato", "Variety": "Jyoti", "Min_Price": 850, "Max_Price": 1250, "Modal_Price": 1050},
    {"State": "Uttar Pradesh", "District": "Varanasi", "Market": "Varanasi Mandi", "Commodity": "Tomato", "Variety": "Desi", "Min_Price": 900, "Max_Price": 1600, "Modal_Price": 1200},
    {"State": "Maharashtra", "District": "Nashik", "Market": "Lasalgaon Mandi", "Commodity": "Onion", "Variety": "Red", "Min_Price": 1400, "Max_Price": 2100, "Modal_Price": 1800},
    {"State": "Maharashtra", "District": "Pune", "Market": "Pune Mandi", "Commodity": "Soybean", "Variety": "Yellow", "Min_Price": 4200, "Max_Price": 4750, "Modal_Price": 4500},
    {"State": "Gujarat", "District": "Rajkot", "Market": "Rajkot Mandi", "Commodity": "Cotton", "Variety": "Shankar-6", "Min_Price": 6400, "Max_Price": 7200, "Modal_Price": 6900},
    {"State": "Gujarat", "District": "Junagadh", "Market": "Junagadh Mandi", "Commodity": "Groundnut", "Variety": "Bold", "Min_Price": 5600, "Max_Price": 6300, "Modal_Price": 6000},
    {"State": "Madhya Pradesh", "District": "Indore", "Market": "Indore Mandi", "Commodity": "Soybean", "Variety": "JS 335", "Min_Price": 4300, "Max_Price": 4800, "Modal_Price": 4600},
    {"State": "Rajasthan", "District": "Jaipur", "Market": "Jaipur Mandi", "Commodity": "Mustard", "Variety": "Rai", "Min_Price": 5100, "Max_Price": 5650, "Modal_Price": 5400},
    {"State": "Karnataka", "District": "Bengaluru", "Market": "Yeshwanthpur Mandi", "Commodity": "Ragi", "Variety": "Local", "Min_Price": 3200, "Max_Price": 3800, "Modal_Price": 3550},
    {"State": "Andhra Pradesh", "District": "Guntur", "Market": "Guntur Mirchi Yard", "Commodity": "Red Chilli", "Variety": "Teja", "Min_Price": 14000, "Max_Price": 19500, "Modal_Price": 17200},
    {"State": "Telangana", "District": "Warangal", "Market": "Warangal Mandi", "Commodity": "Cotton", "Variety": "Bunny", "Min_Price": 6300, "Max_Price": 7100, "Modal_Price": 6750},
    {"State": "Tamil Nadu", "District": "Coimbatore", "Market": "Coimbatore Mandi", "Commodity": "Coconut", "Variety": "Medium", "Min_Price": 2400, "Max_Price": 3100, "Modal_Price": 2800},
]

def get_mandi_data(selected_state: str = "All", selected_commodity: str = "All") -> pd.DataFrame:
    """Returns a filtered DataFrame of Mandi commodity prices."""
    df = pd.DataFrame(MANDI_RECORDS)
    if selected_state != "All":
        df = df[df["State"] == selected_state]
    if selected_commodity != "All":
        df = df[df["Commodity"] == selected_commodity]
    return df

def get_unique_states():
    df = pd.DataFrame(MANDI_RECORDS)
    return ["All"] + sorted(df["State"].unique().tolist())

def get_unique_commodities():
    df = pd.DataFrame(MANDI_RECORDS)
    return ["All"] + sorted(df["Commodity"].unique().tolist())