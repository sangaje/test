import requests
import csv
import os
from datetime import datetime


csv_exist = os.path.exists("weather.csv")
header = ["current_time", "temp", "humidity", "main"]


with open("weather.csv", "a", newline="") as f:
    writer = csv.writer(f)

    if not csv_exist:
        writer.writerow(header)

    API_KEY = os.getenv("WEATHER_API_KEY")
    city_name = "Seoul"
    url = (
        f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"
    )

    url += "&units=metric"
    reponse = requests.request("GET", url)
    result = reponse.json()

    main = result['weather'][0]["main"]
    temp = result["main"]["temp"]
    temp_min = result["main"]["temp_min"]
    temp_max = result["main"]["temp_max"]
    humidity = result["main"]["humidity"]
    wind = result["wind"]

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    writer.writerow([current_time, temp, humidity, main])
