from django.urls import path

from .views import AutoCompleteView

app_name = "weather"

urlpatterns = [
    path(
        "autocomplete/",
        AutoCompleteView.as_view(),
        name="autocomplete",
    ),
]
