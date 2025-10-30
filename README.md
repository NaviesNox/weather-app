# 🌦️ Weather App
A simple weather web application built with **Flask** and **Bootstrap** that displays current weather data using the [Weatherstack API](https://weatherstack.com/).

## 🚀 Features
- Search weather by **city name**
- Displays **temperature**, **description**, **location**, and **weather icon**
- **Light / Dark mode** toggle
- **Responsive** design for mobile and desktop

## 🧩 Tech Stack
- **Backend:** Python Flask
- **Frontend:** Bootstrap 5, Vanilla JS
- **API:** [Weatherstack](https://weatherstack.com/)

## ⚙️ Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/NaviesNox/weather-app.git
   cd weather-app
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # macOS/Linux
   .venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set your Weatherstack API key**
   Open `app.py` and replace:
   ```python
   API_KEY = "YOUR_API_KEY"
   ```

5. **Run the app**
   ```bash
   python app.py
   ```

6. Open your browser at:
   ```
   http://127.0.0.1:5000
   ```

## 🧠 Notes
- You need an active internet connection for API requests.
- Free Weatherstack accounts use HTTP instead of HTTPS.

## 📜 License
This project is open source under the [MIT License](LICENSE).
