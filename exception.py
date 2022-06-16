class CantGetCoordinates(Exception):
    """The program cannot get location coordinates"""
    pass


class CantGetWeatherFromAPI(Exception):
    """The program cannot get the weather from an external service"""
    pass


class CantSaveWeather(Exception):
    """The program cannot save the file in the specified directory"""
    pass
