import requests
from suntime import Sun
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

# Automatically geolocate the connecting IP
latitude, longitude, city = get_current_location()
print(latitude, longitude)
sun = Sun(latitude, longitude)

# Function to get daily average temperature with retry mechanism
def get_daily_temperature(lat, lon, start, end):
    querystring = {"lat": lat, "lon": lon, "start": start, "end": end}
    # Define the headers for the API request
    headers = {
        "x-rapidapi-key": this,
    }
    response = requests.get(that, headers=headers, params=querystring)
    return response.json()

def extract_time(datetime_string):
    # Parse the input string to a datetime object
    datetime_obj = datetime.strptime(datetime_string, '%Y-%m-%d %H:%M:%S')
    # Extract the time part and format it as "HH:MM:SS"
    time_part = datetime_obj.strftime('%H:%M:%S')
    return time_part

# Get the current date
current_date = datetime.now()


# Generate and print dates for the next 7 days with average temperatures
end_date = (current_date + timedelta(days=6)).strftime("%Y-%m-%d")   # week range for weekly data for each day
start_date = current_date.strftime('%Y-%m-%d')
print(f"City: {city}")

# Retry mechanism for fetching temperature data
daily_data = get_daily_temperature(latitude, longitude, start_date, end_date)

def direction (wind_direction):
    if wind_direction == 0 or wind_direction == 360:
        return "North"
    elif wind_direction == 90:
        return "East"
    elif wind_direction == 180:
        return "South"
    elif wind_direction == 270:
        return "West"
    elif wind_direction > 0 or wind_direction < 90:
        return "North East"
    elif wind_direction > 90 or wind_direction < 180:
        return "South East"
    elif wind_direction > 180 or wind_direction < 270:
        return "South West"
    elif wind_direction > 270 or wind_direction < 360:
        return "North West"
    else:   
        return wind_direction

if daily_data.get("data"):
    for day_data in daily_data["data"]:
        date = day_data.get("date")
        date_obj = datetime.strptime(date, '%Y-%m-%d')
        formatted_date = date_obj.strftime('%d/%m/%Y')
        avg_temp = day_data.get("tavg")
        max_temp = day_data.get("tmax")
        min_temp = day_data.get("tmin")
        wind_gust = day_data.get("wpgt")
        wind_speed = day_data.get("wspd")
        sea_level_air_pressure = day_data.get("pres")
        time = datetime.date(date_obj)
        sunrise= sun.get_local_sunrise_time(time)
        sunset = sun.get_local_sunset_time(time)
        wind_int =direction(day_data.get ("wdir"))
        
        #Extract the time and calculate it
        datetime_string = str(sunrise)
        time_sunrise = extract_time(datetime_string)
        datetime_string = str(sunset)
        time_sunset = extract_time(datetime_string)
        format = "%H:%M:%S"
        tdelta = datetime.strptime(time_sunset, format) - datetime.strptime(time_sunrise,format)
        
        precipitation = day_data.get ("prcp") or 0
        if avg_temp is not None:
            print(f"Date: {formatted_date}")
            print(f"Average Temperature: {avg_temp}°C")
            print(f"Minimum Temperature: {min_temp}°C")
            print(f"Maximum Temperature: {max_temp}°C")
            print(f"Maximum wind gust: {wind_gust} km/h")
            print(f"The wind will be coming from {wind_int} with an average wind speed: {wind_speed} km/h")
            print(f"The sun will rise at {time_sunrise} and set at {time_sunset} which will give you {tdelta} suntime")
            print(f"Percepitation: {precipitation} mm\n")
        else:
            print(f"Date: {formatted_date}, No average temperature data available")
else:
    print(f"No temperature data available for the date range {start_date} to {end_date}")