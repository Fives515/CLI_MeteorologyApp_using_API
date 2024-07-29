import requests
from suntime import Sun
from datetime import datetime, timedelta
from api_list import this, that, key

#function to seperate the coordinates into latitude and longitude
def get_coordinates_from_user(coordinates):
    coordinates = coordinates.split(",")
    #return a list
    return coordinates

def get_current_location():
    url = f'https://www.googleapis.com/geolocation/v1/geolocate?key={key}'
    
    # Send POST request to the API
    response = requests.post(url, json={"considerIp": "true"})
    location_data = response.json()
    while True:
        userinput = input("1. If want to enter your coordinates \n"
                        "2. If you want to use your current location\n"
                        "Select from the following options: ")

        if userinput == "1":
            location= get_coordinates_from_user(input("Example: 51.4359296, -0.0622592 coordinates for London \n Please enter the latitude of your chosen location:"))
            latitude = float(location [0])
            longitude = float(location [1])
            city = get_city_from_coords(latitude, longitude)
            return latitude, longitude, city

        elif userinput == "2":
            if "location" in location_data:
                latitude = location_data["location"]["lat"]
                longitude = location_data["location"]["lng"]
                city = get_city_from_coords(latitude, longitude)
                return latitude, longitude, city
            else:
                return None, None, "Unknown"
        else:
            print("Wrong input, try again\n\n\n\n")
    
def get_city_from_coords(lat, lon):
    url = f'https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lon}&key={key}'
    response = requests.get(url)
    data = response.json()
    
    if 'results' in data and data['results']:
        for result in data['results']:
            for component in result['address_components']:
                if 'locality' in component['types']:
                    return component['long_name']
    return "Unknown"


# Automatically geolocate the connecting IP
latitude, longitude, city = get_current_location()
print(latitude, longitude, city)
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

#Transforms the API wind direction in degrees to directional words
def direction (wind_direction):
    if wind_direction >= 305 or wind_direction <= 55:
        if wind_direction >= 305 or wind_direction <= 325:
            return "North West"
        elif wind_direction > 325 or wind_direction < 350:
            return "NNW"
        elif wind_direction > 11 or wind_direction < 34:
            return "NNE"
        if wind_direction >= 35 or wind_direction <= 55:
            return "North East"
        else:
            return "North"
    elif wind_direction > 55 or wind_direction < 125:
        if wind_direction > 55 or wind_direction < 80:
            return "ENE"
        elif wind_direction > 100 or wind_direction < 125:
            return "ESE"
        else:
            return "East"
    elif wind_direction >= 125 or wind_direction <= 235:
        if wind_direction >= 215 or wind_direction <= 235:
            return "South West"
        elif wind_direction > 190 or wind_direction < 215:
            return "SSW"
        elif wind_direction > 145 or wind_direction < 170:
            return "SSE"
        if wind_direction >= 125 or wind_direction <= 145:
            return "South East"
        else:
            return "South"
    elif wind_direction > 305 or wind_direction < 125:
        if wind_direction > 280 or wind_direction < 305:
            return "WNW"
        elif wind_direction > 235 or wind_direction < 260:
            return "WSW"
        else:
            return "West"
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