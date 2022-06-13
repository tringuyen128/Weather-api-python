from django.template import TemplateSyntaxError
import requests


API_KEY = "1c2a0eb96be32f3071229665862e03df"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    # we want to get weather data
    weather = data['weather'][0]['description']
    # we want to get temperature
    temperature = round(data["main"]["temp"] - 273.15)

    print("Weather:", weather)
    print("Temperature:", temperature, "celsius")
else:
    print("An error occurred.")
