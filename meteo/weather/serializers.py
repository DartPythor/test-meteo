from rest_framework import serializers

from weather.models import CityCached


class AutoCompleteSerializer(serializers.Serializer):
    name = serializers.CharField()


class CityCachedSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityCached
        fields = ["id", "name", "latitude", "longitude", "country"]
        read_only_fields = ["id"]


class CityWeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityCached
        fields = ["id", "name", "latitude", "longitude", "country"]
        read_only_fields = fields
