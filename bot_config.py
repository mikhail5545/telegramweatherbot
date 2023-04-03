"""
Константные переменные всего проекта из .env
"""
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
API_KEY = os.getenv('API_KEY')
WEATHER_REQUEST = (
        'https://api.openweathermap.org/data/2.5/weather?'
        'lat={latitude}&lon={longitude}&'
        'appid=' + API_KEY + '&units=metric'
)
