from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from search.models import SearchStat, SearchHistory
from weather.models import CityCached
from weather.serializers import CityCachedSerializer, CityWeatherSerializer
from weather.openmeteo_util import MeteoApi


class AutoCompleteView(APIView):
    def get(self, request, *args, **kwargs):
        city_name = request.query_params.get("name").strip().lower()
        if not city_name:
            return Response(
                {"error": 'Parameter "name" is required'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        cached_cities = CityCached.objects.filter(
            Q(name__icontains=city_name) | Q(country__icontains=city_name)
        )[:10]

        if cached_cities.exists():
            result = []
            for i in cached_cities:
                serializer = CityCachedSerializer(i)
                result.append(serializer.data)

            return Response(
                data={"result": result},
                status=status.HTTP_200_OK,
            )

        try:
            geocoding_data = MeteoApi.geocoding(city_name)

            if not geocoding_data.get("results"):
                return Response(
                    {"error": "City not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )
            result = []
            for i in geocoding_data["results"]:
                new_city = CityCached.objects.create(
                    name=i["name"],
                    latitude=i["latitude"],
                    longitude=i["longitude"],
                    country=i["country"],
                )
                serializer = CityCachedSerializer(new_city)
                result.append(serializer.data)

            return Response(
                data={"result": result},
                status=status.HTTP_200_OK,
            )

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class CityWeatherView(APIView):
    def get(self, request, city_id):
        try:
            city = get_object_or_404(CityCached, pk=city_id)

            weather_data = MeteoApi.forecast(
                longitude=city.longitude, latitude=city.latitude
            )

            response_data = {
                "city": CityWeatherSerializer(city).data,
                "weather": weather_data,
            }
            SearchHistory.objects.create(
                session_key=request.session.session_key,
                city=city,
            )
            stat, _ = SearchStat.objects.get_or_create(city=city)
            stat.count += 1
            stat.save()
            return Response(data=response_data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
