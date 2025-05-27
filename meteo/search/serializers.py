from rest_framework import serializers
from weather.serializers import CityCachedSerializer

from search.models import SearchHistory


class SearchHistorySerializer(serializers.ModelSerializer):
    city = CityCachedSerializer()

    class Meta:
        model = SearchHistory
        fields = ["session_key", "city", "created_at"]
        read_only_fields = fields
