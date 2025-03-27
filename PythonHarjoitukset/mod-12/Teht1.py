import requests
import json

try:
    vastaus = requests.get("https://api.chucknorris.io/jokes/random")
    if vastaus.status_code == 200:
        json_vastaus = vastaus.json()
        print(json_vastaus["value"])
except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa.")