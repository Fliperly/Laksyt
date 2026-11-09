import requests

api_avain = "76db774ebc3ea74b4733cdf8206a809f"
paikkakunta = input("Anna paikkakunnan nimi:")
pyyntö = "https://api.openweathermap.org/data/2.5/weather?q=" + paikkakunta + "&appid=" + api_avain + "&lang=fi"

try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code == 200:
        json_vastaus = vastaus.json()
        säätila = json_vastaus["weather"][0]["description"]
        kelvin = json_vastaus["main"]["temp"]
        celsius = kelvin - 273.15
        print("Säätila:", säätila)
        print(f"Lämpötila: {celsius:.1f} °C")
    else:
        print("Haku epäonnistui. Statuskoodi:", vastaus.status_code)
except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa.")