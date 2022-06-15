from exception import CantGetCoordinates, CantGetWeatherFromAPI
from gps_coordinates import get_coordinate
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

if __name__ == "__main__":
    main()
