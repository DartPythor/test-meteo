from django.urls import path

from weather.views import AutoCompleteView, CityWeatherView

app_name = "weather"

urlpatterns = [
    path(
        "autocomplete/",
        AutoCompleteView.as_view(),
        name="autocomplete",
    ),
    path("weather/<int:city_id>/", CityWeatherView.as_view(), name="city-weather"),
]
