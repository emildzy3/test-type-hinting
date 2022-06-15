import json
from datetime import datetime
from dataclasses import dataclass
from enum import Enum
from json.decoder import JSONDecodeError
from typing import TypeAlias

import requests

from config import OPENWEATHER_URL
from exception import CantGetWeatherFromAPI
from gps_coordinates import Coordinate

Celsius: TypeAlias = int


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
    server_response = _get_weather_from_api(coordinate.latitude, coordinate.longitude)
    weather = _parse_weather(server_response)
    return weather


def _get_weather_from_api(latitude: float, longitude: float) -> str:
    raw_data_from_api = requests.get(OPENWEATHER_URL.format(latitude=latitude, longitude=longitude))
    if not raw_data_from_api.ok:
        raise CantGetWeatherFromAPI
    return raw_data_from_api.text


def _parse_weather(server_response: str) -> Weather:
    try:
        server_response_dict = json.loads(server_response)
    except JSONDecodeError:
        raise CantGetWeatherFromAPI
    return Weather(
        temperature=_parse_temperature(server_response_dict),
        weather_type=_parse_weather_type(server_response_dict),
        sunset=_parse_sunset_time(server_response_dict),
        city=_parse_name_city(server_response_dict)
    )


def _parse_temperature(json_response: dict) -> Celsius:
    try:
        temperature = round(json_response['main']['temp'])
        return temperature
    except KeyError:
        raise CantGetWeatherFromAPI


def _parse_weather_type(json_response: dict) -> WeatherType:
    try:
        id_weather_type = str(json_response['weather'][0]['id'])
    except (KeyError, IndexError):
        raise CantGetWeatherFromAPI

    weather_types = {
        "1": WeatherType.THUNDERSTORM,
        "3": WeatherType.DRIZZLE,
        "5": WeatherType.RAIN,
        "6": WeatherType.SNOW,
        "7": WeatherType.FOG,
        "800": WeatherType.CLEAR,
        "80": WeatherType.CLOUDS
    }
    for _id, _weather_types in weather_types.items():
        if id_weather_type.startswith(_id):
            return _weather_types
    raise CantGetWeatherFromAPI


def _parse_sunset_time(json_response: dict) -> datetime:
    try:
        sunset = json_response['sys']['sunset']
    except KeyError:
        raise CantGetWeatherFromAPI
    return datetime.fromtimestamp(sunset)


def _parse_name_city(json_response: dict) -> str:
    try:
        return json_response['name']
    except KeyError:
        raise CantGetWeatherFromAPI


if __name__ == "__main__":
    print(get_weather(Coordinate(latitude=44.7522, longitude=37.6156)))
