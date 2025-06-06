from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "weather/",
        include("weather.urls", namespace="weather"),
    ),
    path(
        "search/",
        include("search.urls", namespace="search"),
    ),
]
