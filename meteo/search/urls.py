from django.urls import path
from search.views import UserSearchHistoryView, SearchStatsView


app_name = "search"
urlpatterns = [
    path(
        "search-history/",
        UserSearchHistoryView.as_view(),
        name="search-history",
    ),
    path(
        "search-stats/",
        SearchStatsView.as_view(),
        name="search-stats",
    ),
]
