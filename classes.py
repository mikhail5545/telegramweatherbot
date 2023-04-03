"""
Все классы, используемые в проекте
"""

from typing import TypeAlias
from dataclasses import dataclass
from enum import IntEnum
from datetime import datetime


Celsius: TypeAlias = float


Percent: TypeAlias = float


mmHg: TypeAlias = float


@dataclass(slots=True, frozen=True)
class Coordinates:
    latitude: float
    longitude: float


class WindDirection(IntEnum):
    North = 0
    Northeast = 45
    East = 90
    Southeast = 135
    South = 180
    Southwest = 225
    West = 270
    Northwest = 315


@dataclass(slots=True, frozen=True)
class Weather:
    location: str
    temperature: Celsius
    temperature_feeling: Celsius
    description: str
    wind_speed: float
    wind_direction: str
    sunrise: datetime
    sunset: datetime
    cloudness: Percent
    pressure: mmHg
    humidity: Percent
    temp_min: Celsius
    temp_max: Celsius
