import requests
from datetime import datetime, timedelta
import time
from api import this, that


# Define the headers for the API request
headers = {
    "x-rapidapi-key": this,
    "x-rapidapi-host": "meteostat.p.rapidapi.com"
}

# Function to get daily average temperature with retry mechanism
def get_daily_temperature(lat, lon, start, end):
    querystring = {"lat": lat, "lon": lon, "start": start, "end": end}
    response = requests.get(that, headers=headers, params=querystring)
    return response.json()

# Define the latitude and longitude of the location
lat = "51.5287398"
lon = "-0.2664035"

# Get the current date
current_date = datetime.now()

# Generate and print dates for the next 7 days with average temperatures
for i in range(7):
    next_date = current_date + timedelta(days=i)
    start_date = next_date.strftime('%Y-%m-%d')
    end_date = start_date  # Single day range for daily data
    
    # Retry mechanism for fetching temperature data
    daily_data = None
    for attempt in range(3): # try 3 times before fail
        daily_data = get_daily_temperature(lat, lon, start_date, end_date)
        if daily_data.get("data"):
            break
        else:
            time.sleep(1) # seconds
    
    # Extract and print the average temperature
    if daily_data and daily_data.get("data"):
        avg_temp = daily_data["data"][0].get("tavg")
        if avg_temp is not None:
            print(f"Date: {start_date}, Average Temperature: {avg_temp}°C")
        else:
            print(f"Date: {start_date}, No average temperature data available")
    else:
        print(f"Date: {start_date}, No temperature data available")
