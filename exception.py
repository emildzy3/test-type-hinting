class CantGetCoordinates(Exception):
    """The program cannot get location coordinates"""
    pass


class CantGetWeatherFromAPI(Exception):
    """The program cannot get the weather from an external service"""
    pass
