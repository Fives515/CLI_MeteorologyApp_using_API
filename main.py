import requests
from datetime import datetime, timedelta
from api import this, that

def get_current_location():
    response = requests.get("https://ipinfo.io")
    data = response.json()
    loc = data["loc"].split(",")
    latitude = float(loc[0])
    longitude = float(loc[1])
    city = data.get("city", "Unknown")
    return latitude, longitude, city


# Function to get daily average temperature with retry mechanism
def get_daily_temperature(lat, lon, start, end):
    querystring = {"lat": lat, "lon": lon, "start": start, "end": end}
    # Define the headers for the API request
    headers = {
        "x-rapidapi-key": this,
    }
    response = requests.get(that, headers=headers, params=querystring)
    return response.json()

# Automatically geolocate the connecting IP
latitude, longitude, city = get_current_location()

# Get the current date
current_date = datetime.now()

# Generate and print dates for the next 7 days with average temperatures
end_date = (current_date + timedelta(days=6)).strftime("%Y-%m-%d")   # week range for weekly data for each day
start_date = current_date.strftime('%Y-%m-%d')
print(f"City: {city}")
# Retry mechanism for fetching temperature data
daily_data = get_daily_temperature(latitude, longitude, start_date, end_date)
if daily_data.get("data"):
    for day_data in daily_data["data"]:
        date = day_data.get("date")
        avg_temp = day_data.get("tavg")
        if avg_temp is not None:
            print(f"Date: {date}, Average Temperature: {avg_temp}°C")
        else:
            print(f"Date: {date}, No average temperature data available")
else:
    print(f"No temperature data available for the date range {start_date} to {end_date}")