from dotenv import load_dotenv, dotenv_values
import os
import requests
from datetime import datetime, timezone, timedelta

load_dotenv()

api_key = os.getenv("API_KEY")
print(api_key)
city = "Næstved"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=da"

response = requests.get(url)
data = response.json()


if response.status_code == 200:
    print(f"Vejr i {city}: {data['weather'][0]['description']}")
    print(f"Temperatur: {data['main']['temp']}°C")
    print(f"Fugtighed: {data['main']['humidity']}%")
    print(f"Vindhastighed: {data['wind']['speed']} m/s")
    # Get the UTC time as a timezone-aware object
    utc_time = datetime.fromtimestamp(data["dt"], tz=timezone.utc)

    # Create a timedelta based on the timezone offset in seconds
    offset = timedelta(seconds=data["timezone"])

    # Apply the offset to get the local time
    local_time = utc_time + offset

    print(f"Lokal tid i {city}: {local_time.strftime('%Y %H')}")
    print(data)
else:
    print("Noget gik galt:", data)



