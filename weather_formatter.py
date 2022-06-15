from weather_api_service import Weather


def print_weather(weather: Weather) -> str:
    """Returns weather data in human-readable form"""
    return (f"Город: {weather.city}, температура {weather.temperature}°C, "
            f"{weather.weather_type}\n"
            f"Закат: {weather.sunset.strftime('%H:%M')} ч.\n")


if __name__ == "__main__":
    from weather_api_service import WeatherType
    from datetime import datetime

    print(print_weather(Weather(
        temperature=26,
        weather_type=WeatherType.CLOUDS,
        sunset=datetime(2022, 6, 15, 20, 16, 48),
        city='Abrau-Dyurso'
    )))
