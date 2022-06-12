
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Coordinate:
    latitude: float
    longitude: float


def get_coordinate() -> Coordinate:
    """
    Return GPS coordinate current location
    """
    return Coordinate(latitude=5, longitude=6)


