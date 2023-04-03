"""
Парсит json объект с данными о погоде
"""
from datetime import datetime
from typing import Literal


from classes import Celsius, Percent, mmHg,  WindDirection


def _parse_location(dict: dict) -> str:
    return dict['name']


def _parse_temperature(dict: dict) -> Celsius:
    return dict['main']['temp']


def _parse_feels_like(dict: dict) -> Celsius:
    return dict['main']['feels_like']

def _parse_max_temperature(dict: dict) -> Celsius:
    return dict['main']['temp_max']


def _parse_min_temperature(dict: dict) -> Celsius:
    return dict['main']['temp_min']


def _parse_humidity(dict: dict) -> Percent:
    return dict['main']['humidity']


def _parse_pressure(dict: dict) -> mmHg:
    return float(dict['main']['pressure']) * 0.75


def _parse_cloudness(dict: dict) -> Percent:
    return dict['clouds']['all']


def _parse_description(dict) -> str:
    return str(dict['weather'][0]['description'])


def _parse_sun_time(dict: dict, time: Literal["sunrise", "sunset"]) -> datetime:
    return datetime.fromtimestamp(dict['sys'][time])


def _parse_wind_speed(dict: dict) -> float:
    return dict['wind']['speed']


def _parse_wind_direction(dict: dict) -> str:
    degrees = dict['wind']['deg']
    degrees = round(degrees / 45) * 45
    if degrees == 360:
        degrees = 0
    return WindDirection(degrees).name