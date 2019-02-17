import sys
import requests

localization = sys.argv[1]

Weather = namedtuple("Weather", ['location', 'temperature', 'air_pressure', 'humidity'])

#pobieram id lokalizacji
def get_location_id(localization):
    resp = requests.get(f"https://www.metaweather.com/api/location/search/?query={localization}")
    location_id = resp.json()[0]['woeid']
    return location_id



print(location_id)

def get_location_weather(location_id):
#pobieram pogodę dla lokalizacji
    resp = requests.get(f"https://www.metaweather.com/api/location/{location_id}/")
    weather = resp.json()['consolidated_weather'][0]
    return weather

def print_weather(weather, localization):
#drukuję informacje o pogodzie
    print(f"Pogoda w lokalizacji: {localization}")
    print("Temperatura: ", weather['the_temp'])
