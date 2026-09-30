# 🌾 KrishiMitra — AI-Powered Smart Agriculture Assistant

KrishiMitra is an intelligent, AI-driven farming assistant designed to empower farmers with real-time agricultural insights, crop recommendations, disease diagnosis, and weather-based advisory using Google Cloud Platform (GCP) and generative AI.

---

## 🚀 Features

- 🌿 **Crop Recommendation**: Suggests optimal crops based on soil nutrients (N, P, K), pH, and local climate data.
- 🔬 **Plant Disease Diagnosis**: Detects crop diseases from uploaded leaf images with actionable organic and chemical treatment advice.
- 🌦️ **Weather & Irrigation Advisory**: Hyper-local weather forecasting with smart watering reminders.
- 💬 **Multilingual AI Assistant**: Interactive voice/text chatbot answering farmer queries in local languages.
- 📊 **Market Trends & Price Insights**: Real-time mandi prices and market demand trends.

---

## 🛠️ Tech Stack

- **Frontend & UI**: [Streamlit](https://streamlit.io/)
- **AI & Cloud Backend**: Google Cloud Platform (GCP), Vertex AI / Gemini API
- **Language**: Python 3.10+
- **Libraries**: Pandas, NumPy, Scikit-Learn, Pillow, Requests

---

## 📦 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/KavyeGupta/krishimitra.git
cd krishimitra
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory:
```env
GCP_API_KEY="your-google-cloud-api-key"
```

### 5. Run the application
```bash
streamlit run app.py
```
Your app will be available locally at `http://localhost:8501`.

---

## 📂 Project Structure

```text
krishimitra/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
├── .gitignore          # Ignored files (keys, venv, cache)
└── README.md           # Project documentation
```

---

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request.

---

## 📄 License
This project is licensed under the [MIT License](LICENSE).
