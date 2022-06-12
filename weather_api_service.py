from datetime import datetime
from dataclasses import dataclass
from enum import Enum

from gps_coordinates import Coordinate

Celsius = int


class WeatherType(Enum):
    THUNDERSTORM = "Гроза"
    DRIZZLE = "Изморось"
    RAIN = "Дождь"
    SNOW = "Снег"
    CLEAR = "Ясно"
    FOG = "Туман"
    CLOUDS = "Облачно"


@dataclass(slots=True, frozen=True)
class Weather:
    temperature: Celsius
    weather_type: WeatherType
    sunset: datetime
    city: str


def get_weather(coordinate: Coordinate) -> Weather:
    """Returns the required weather data from an external API"""
    return Weather(
        temperature=20,
        weather_type=WeatherType.SNOW,
        sunset=datetime.today(),
        city='Sochi'
    )
