from dataclasses import dataclass
from typing import Literal

import requests

from config import API_COORDINATE
from exception import CantGetCoordinates


@dataclass(slots=True, frozen=True)
class Coordinate:
    latitude: float
    longitude: float


def get_coordinate() -> Coordinate:
    """
    Return GPS coordinate current location
    """
    coordinates = _get_coordinates_from_api()
    return coordinates


def _get_coordinates_from_api() -> Coordinate:
    raw_data_from_api = _get_data_api()
    return _parse_coordinates(raw_data_from_api)


def _get_data_api() -> bytes:
    server_request = requests.get(API_COORDINATE)
    if not server_request.ok:
        raise CantGetCoordinates
    return server_request.content


def _parse_coordinates(raw_data_from_api: bytes) -> Coordinate:
    try:
        normalize_data = raw_data_from_api.decode().strip().lower().split('\n')
    except UnicodeDecodeError:
        raise CantGetCoordinates
    return Coordinate(
        latitude=_parse_coordinate(normalize_data, 'latitude'),
        longitude=_parse_coordinate(normalize_data, 'longitude')
    )


def _parse_coordinate(normalize_data: list[str],
                      type_coordinate: Literal['latitude'] | Literal['longitude']) -> float:
    number_coordinate = 1
    if type_coordinate == 'latitude':
        number_coordinate = 0
    try:
        return float(normalize_data[6].split()[1].split(',')[number_coordinate].strip('"'))
    except ValueError:
        raise CantGetCoordinates


if __name__ == "__main__":
    print(get_coordinate())
