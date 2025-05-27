import openmeteo_requests
from retry_requests import retry

# Настройка клиента с кэшированием и повтором запросов
client = openmeteo_requests.Client(session=retry())
# Запрос координат города (Geocoding API)
client.weather_api()
geocode = client.geocode("Berlin")[0]  # Берём первый результат
lat, lon = geocode.latitude, geocode.longitude
print(lat, lon)
# # Запрос погоды
# params = {
#     "latitude": lat,
#     "longitude": lon,
#     "current": ["temperature_2m", "weather_code"],
# }
# response = client.weather_api("https://api.open-meteo.com/v1/forecast", params=params)[0]
#
# print(f"Температура: {response.current.temperature_2m}°C")
# print(f"Погода: {response.current.weather_code_description}")
