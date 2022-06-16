from pathlib import Path

from exception import CantGetCoordinates, CantGetWeatherFromAPI, CantSaveWeather
from gps_coordinates import get_coordinate
from history import save_weather, PlainFileWeatherStorage
from weather_api_service import get_weather
from weather_formatter import print_weather


def main():
    try:
        coordinate = get_coordinate()
    except CantGetCoordinates:
        print('Не удалось получить текущие координаты от внешнего сервиса')
        exit(1)
    try:
        weather = get_weather(coordinate)
    except CantGetWeatherFromAPI:
        print(f'Не удалось получить погоду по координатам: {coordinate}')
        exit(1)
    print(print_weather(weather))
    try:
        save_weather(
            weather,
            PlainFileWeatherStorage(Path.cwd() / "history.txt")
        )
    except CantSaveWeather:
        print(f'Не удалось сохранить погоду в директории {Path}. Ошибка прав доступа')
        exit(1)


if __name__ == "__main__":
    main()
