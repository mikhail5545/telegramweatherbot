"""
Получает координаты пользователя через его ip
"""
from get_ip import _get_ip
from classes import Coordinates


async def get_coordinates() -> Coordinates:
    """Возвращает координаты в виде обЪекта класса Coordinates"""
    data = await _get_ip()
    latitude, longitude = map(float, data['loc'].split(','))

    return Coordinates(latitude=latitude, longitude=longitude)

