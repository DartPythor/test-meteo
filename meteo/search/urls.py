from django.urls import path
from .views import UserSearchHistoryView


app_name = "search"
urlpatterns = [
    path("search-history/", UserSearchHistoryView.as_view(), name="search-history"),
]
