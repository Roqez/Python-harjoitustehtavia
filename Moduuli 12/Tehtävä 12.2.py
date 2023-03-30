import json
import requests

paikkakunta = input("Syötä paikkakunta niin haen sen säätilan")

pyyntö = "https://api.openweathermap.org/data/2.5/weather?q="+paikkakunta+"&appid=f8040d0df22456d3e3472beeba1ca91b"
pyyntö2 = "https://api.openweathermap.org/data/2.5/weather?q="+paikkakunta+"&units=metric&appid=f8040d0df22456d3e3472beeba1ca91b"
try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code==200:
        json_vastaus = vastaus.json()
        for i in json_vastaus["weather"]:
            print("Säätila on: " + i["main"])
        kelvinit = (json_vastaus["main"]["temp"])#haetaan sanakirjasta json_vastaus alkiota main vastaavasta arvosta alkio temp ja sen arvo
        vastaus2 = requests.get(pyyntö2)
        json_vastaus2 = vastaus2.json()
        celsius_asteet = (json_vastaus2["main"]["temp"])
        print("Säätila on: " + i["main"]+" ja asteet kelvineinä on: "+str(kelvinit)+" sekä asteet celsiuksina on: "+str(celsius_asteet))
except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa")