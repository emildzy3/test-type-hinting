from gps_coordinates import get_coordinate
from weather_api_service import get_weather
from weather_formatter import print_weather


def main():
    coordinate = get_coordinate()
    weather = get_weather(coordinate)
    print(print_weather(weather))


if __name__ == "__main__":
    main()
