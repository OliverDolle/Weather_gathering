from dotenv import load_dotenv, dotenv_values
import os
import requests
import csv
from datetime import datetime, timezone, timedelta


load_dotenv()

api_key = os.getenv("API_KEY")
city = "Næstved"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=da"

response = requests.get(url)
data = response.json()

utc_time = datetime.fromtimestamp(data["dt"], tz=timezone.utc)

offset = timedelta(seconds=data["timezone"])

local_time = utc_time + offset




data_csv = {
            'town': city, 
            'Windspeed': data['wind']['speed'], 
            'Winddegrees': data['wind']['deg'],
            'Windgust': data['wind']['gust'],
            'Tempature': data['main']['temp'],
            'Tempature_feel': data['main']['feels_like'],
            'year': local_time.strftime('%Y'),
            'month': local_time.strftime('%m'),
            'day': local_time.strftime('%d'),
            'hour': local_time.strftime('%H'),
            'minute': local_time.strftime('%M'),
            'second': local_time.strftime('%S')
            #'weather_type': data['weather']['main'],
            #'weather_description': data['weather']['description']
            }
csv_path = r"C:\Users\olive\OneDrive\Documents\Preparation_Python\weather_data.csv"
with open(csv_path, 'a', newline='') as csvfile:
    fieldnames = ['town', 'Windspeed', 'Winddegrees', 'Windgust',
                  'Tempature', 'Tempature_feel', 'year',
                  'month', 'day', 'hour', 'minute', 'second']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writerow(data_csv)

a = input()