import requests

cityIn = input("Type a city name: ")
url = "https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/" + cityIn
req = requests.get(url)
res = req.json()

print("Forecast for " + cityIn.title() + ":")

for x in res["forecasts"]:
    print(x["date"] + "   " + x["forecast"])