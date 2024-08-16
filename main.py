from location import get_current_location
from weather import get_daily_temperature, extract_time, direction, temperature_scale
from sun_info import get_sun_times
from datetime import datetime, timedelta
from suntime import Sun

# Automatically geolocate the connecting IP
latitude, longitude, city = get_current_location()

# Initialize Sun object
sun = Sun(latitude, longitude)

# Get the current date
current_date = datetime.now()

# Generate and print dates for the next 7 days with average temperatures
end_date = (current_date + timedelta(days=6)).strftime("%Y-%m-%d")   # week range for weekly data for each day
start_date = current_date.strftime('%Y-%m-%d')
print(f"City: {city}")

# Retry mechanism for fetching temperature data
daily_data = get_daily_temperature(latitude, longitude, start_date, end_date)

km = " km/h"
if daily_data.get("data"):
    day_count = 0
    for day_data in daily_data["data"]:
        day_count += 1
        date = day_data.get("date")
        date_obj = datetime.strptime(date, '%Y-%m-%d')
        formatted_date = date_obj.strftime('%d/%m/%Y')
        avg_temp = day_data.get("tavg")
        scale_avg_temp = temperature_scale(avg_temp)
        max_temp = day_data.get("tmax")
        min_temp = day_data.get("tmin")
        wind_gust = day_data.get("wpgt")
        if wind_gust == None:
            wind_gust = "None"
        else:
            wind_gust= str(wind_gust) + km
        wind_speed = day_data.get("wspd")
        if wind_speed == None:
            wind_speed = "None"
        else:
            wind_speed= str(wind_speed) + km
        sea_level_air_pressure = day_data.get("pres")
        time = datetime.date(date_obj)
        
        # Get sunrise and sunset times
        time_sunrise, time_sunset, tdelta = get_sun_times(sun, time)
        
        wind_int = direction(day_data.get ("wdir"))

        precipitation = day_data.get ("prcp") or 0
        if avg_temp is not None or city != "Unknown":
            print(f"Day: {day_count}")
            print(f"Date: {formatted_date}")
            print(f"Average Temperature: {avg_temp}°C, outside is feeling {scale_avg_temp}")
            print(f"Minimum Temperature: {min_temp}°C")
            print(f"Maximum Temperature: {max_temp}°C")
            print(f"Maximum wind gust: {wind_gust}")
            print(f"The wind will be coming from {wind_int} with an average wind speed: {wind_speed}")
            print(f"The sun will rise at {time_sunrise} and set at {time_sunset} which will give you {tdelta} suntime")
            print(f"Percepitation: {precipitation} mm\n")
        else:
            print(f"Date: {formatted_date}, No average temperature data available")
else:
    print(f"No temperature data available for this location for the date range {start_date} to {end_date}")
