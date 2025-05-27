from openmeteopy import OpenMeteo
from openmeteopy.daily import DailyForecast
from openmeteopy.hourly import HourlyForecast
from openmeteopy.options import ForecastOptions, GeocodingOptions


class MeteoApi:
    @staticmethod
    def geocoding(name: str) -> dict:
        options = GeocodingOptions(name)
        return OpenMeteo(options).get_dict()

    @staticmethod
    def forecast(longitude: float, latitude: float) -> dict:
        hourly = HourlyForecast()

        options = ForecastOptions(latitude, longitude)

        mgr = OpenMeteo(
            options,
            hourly.temperature_2m(),
        )

        return mgr.get_dict()
