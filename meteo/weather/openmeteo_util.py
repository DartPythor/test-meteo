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
        daily = DailyForecast()

        options = ForecastOptions(latitude, longitude)

        mgr = OpenMeteo(
            options,
            hourly.shortwave_radiation(),
            daily.shortwave_radiation_sum(),
        )

        return mgr.get_dict()
