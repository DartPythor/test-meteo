from rest_framework import serializers
from weather.serializers import CityCachedSerializer

from search.models import SearchHistory, SearchStat


class SearchHistorySerializer(serializers.ModelSerializer):
    city = CityCachedSerializer()

    class Meta:
        model = SearchHistory
        fields = ["session_key", "city", "created_at"]
        read_only_fields = fields


class SearchStatSerializer(serializers.ModelSerializer):
    city_name = serializers.CharField(source="city.name")
    country = serializers.CharField(source="city.country")
    latitude = serializers.FloatField(source="city.latitude")
    longitude = serializers.FloatField(source="city.longitude")

    class Meta:
        model = SearchStat
        fields = [
            "city_name",
            "country",
            "latitude",
            "longitude",
            "count",
        ]
