import requests as req
import json


city_name = "Пятигорск"
key = "18e84e03b0f189c8baaf7b57dd768cc3"
response = req.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}")
res = json.loads(response.text)
weather = f'{round(res['main']['temp'] - 273.15, 2)}°C'
humidity = f'{res['main']['humidity']}%'
pressure = f'{res['main']['pressure'] * 1000 / 1333} мм рт. ст.'

print(weather, humidity, pressure)


