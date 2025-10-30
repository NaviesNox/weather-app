from flask import Flask, render_template, request
import requests, os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form['city']
        api_key = os.getenv('WEATHER_API_KEY')
        url = f"http://api.weatherstack.com/current?access_key={api_key}&query={city}"
        r = requests.get(url)
        weather_data = r.json()
    return render_template('index.html', data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
