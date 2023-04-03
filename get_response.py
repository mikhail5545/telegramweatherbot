import aiohttp
import json

from get_coordinates import Coordinates
import bot_config
from classes import Weather
from parse_response import _parse_location, _parse_temperature, _parse_feels_like, _parse_description, _parse_sun_time, _parse_wind_speed, _parse_wind_direction
from parse_response import _parse_max_temperature, _parse_min_temperature, _parse_cloudness, _parse_humidity, _parse_pressure

async def get_weather(coordinates: Coordinates) -> Weather:
    """Запрашивает данные о погоде и возвращает объект weather"""
    openweather_response = await _get_openweather_response(
        longitude=coordinates.longitude, latitude=coordinates.latitude
    )
    weather = _parse_openweather_response(openweather_response)
    return weather


async def _get_openweather_response(latitude: float, longitude: float) -> str:
    """Возвращает данные о погоде в виде текста"""
    url = bot_config.WEATHER_REQUEST.format(latitude=latitude, longitude=longitude)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response_text = await response.text()
            return response_text


def _parse_openweather_response(openweather_response: str) -> Weather:
    """Парсит данные о погоде и инициализирует обЪект класса Weather"""
    openweather_dict = json.loads(openweather_response)
    return Weather(
        location=_parse_location(dict=openweather_dict),
        temperature=_parse_temperature(dict=openweather_dict),
        temperature_feeling=_parse_feels_like(dict=openweather_dict),
        description=_parse_description(dict=openweather_dict),
        sunrise=_parse_sun_time(dict=openweather_dict, time='sunrise'),
        sunset=_parse_sun_time(dict=openweather_dict, time='sunset'),
        wind_speed=_parse_wind_speed(dict=openweather_dict),
        wind_direction=_parse_wind_direction(dict=openweather_dict),
        pressure=_parse_pressure(dict=openweather_dict),
        humidity=_parse_humidity(dict=openweather_dict),
        temp_max=_parse_max_temperature(dict=openweather_dict),
        temp_min=_parse_min_temperature(dict=openweather_dict),
        cloudness=_parse_cloudness(dict=openweather_dict)
    )

