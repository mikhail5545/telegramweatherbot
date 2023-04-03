"""
Этот модуль содержит паттерны сообщений для бота
"""
from get_coordinates import get_coordinates
from get_response import get_weather


async def weather() -> str:
    """Возвращает полную информацию о текущей погоде"""
    weather = await get_weather(await get_coordinates())
    return f'In {weather.location} now {weather.description}\n' \
           f'Temperature:\n' \
           f'Now: {weather.temperature}°C, feels like: {weather.temperature_feeling}°C.\n' \
           f'Max: {weather.temp_max}°C; Min: {weather.temp_min}°C.\n' \
           f'Humidity is {weather.humidity}%, cloudness is {weather.cloudness}%.\n' \
           f'Pressure: {weather.pressure} mmHg.'


async def wind() -> str:
    """Возвращает информацию о направлении и скорости ветра в м/с"""
    weather = await get_weather(await get_coordinates())
    return f'It\'s {weather.wind_direction} wind {weather.wind_speed} m/s'


async def sun_time() -> str:
    """Возвращает информацию о времени рассвета и заката"""
    weather = await get_weather(await get_coordinates())
    return f'Sunrise: {weather.sunrise.strftime("%H:%M")}\n' \
           f'Sunset: {weather.sunset.strftime("%H:%M")}\n'


async def humidity() -> str:
    """Возвращает информацию о текущей влажности в %"""
    weather = await get_weather(await get_coordinates())
    return f'Humidity is {weather.humidity}%.'


async def pressure() -> str:
    """Возвращает информацию о текущем давлении в мм ртутного столба"""
    weather = await get_weather(await get_coordinates())
    return f'Pressure is {weather.pressure} mmHg.'


async def cloudness() -> str:
    """Возвращает информацию о текущей облачности в %"""
    weather = await get_weather(await get_coordinates())
    return f'It\'s {weather.cloudness}% cloudness now!.'
