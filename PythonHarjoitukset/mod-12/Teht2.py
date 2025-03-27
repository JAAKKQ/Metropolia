import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

kaupunki = input("Anna paikkakunnan nimi: ")
perus_url = "http://api.openweathermap.org/data/2.5/weather"
parametrit = {
    'q': kaupunki,
    'appid': os.getenv('weather_key'),
    'units': 'metric',
    'lang': 'fi'
}
vastaus = requests.get(perus_url, params=parametrit)
vastaus = vastaus.json()

kaupunki = vastaus.get('name')
maa = vastaus.get('sys', {}).get('country')
saakuvaus = vastaus.get('weather', [{}])[0].get('description')
lampotila = vastaus.get('main', {}).get('temp')

print(f"Sää paikassa {kaupunki}, {maa}:")
print(f"{saakuvaus.capitalize()}, lämpötila: {lampotila}°C")