from location import get_current_location
from weather import get_daily_temperature, get_wind_direction_description, get_outside_temperature_description
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

if daily_data.get("timelines"):
    day_count = 0
    for day_data in daily_data["timelines"]["daily"]:
        day_count += 1
        # Get the date from the interval start time
        date = day_data["time"]
        date_obj = datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
        formatted_date = date_obj.strftime('%d/%m/%Y')
        
        # Access weather values from "values" key
        values = day_data.get("values", {})
        avg_temp = values.get("temperatureAvg")
        scale_avg_temp = get_outside_temperature_description(avg_temp)
        max_temp = values.get("temperatureMax")
        min_temp = values.get("temperatureMin")
        wind_gust = values.get("windGustAvg")
        print(wind_gust)
        if wind_gust is None:
            wind_gust = "None"
        else:
            wind_gust = str(wind_gust) + " km/h"
        
        wind_speed = values.get("windSpeedAvg")
        if wind_speed is None:
            wind_speed = "None"
        else:
            wind_speed = str(wind_speed) + " km/h"
        
        cloud_cover = values.get("cloudCoverAvg")
        
        # Extract sunrise and sunset times
        time_sunrise = values.get("sunriseTime")
        time_sunset = values.get("sunsetTime")
        time = datetime.date(date_obj)
        
        if time_sunrise and time_sunset:
            time_sunrise = datetime.strptime(time_sunrise, '%Y-%m-%dT%H:%M:%SZ').strftime('%H:%M')
            time_sunset = datetime.strptime(time_sunset, '%Y-%m-%dT%H:%M:%SZ').strftime('%H:%M')
            tdelta = datetime.strptime(time_sunset, '%H:%M') - datetime.strptime(time_sunrise, '%H:%M')
        else:
            time_sunrise = time_sunset = tdelta = "N/A"

        wind_info = get_wind_direction_description(values.get("windDirectionAvg"))
        
        precipitation = values.get("precipitationSum") or 0
        
        # Print the extracted data
        if avg_temp is not None:
            print(f"Day: {day_count}")
            print(f"Date: {formatted_date}")
            print(f"Average Temperature: {avg_temp}°C, {scale_avg_temp}")
            print(f"Minimum Temperature: {min_temp}°C")
            print(f"Maximum Temperature: {max_temp}°C")
            print(f"Maximum wind gust: {wind_gust}")
            print(f"{wind_info} {wind_speed}")
            print(f"The sun will rise at {time_sunrise} and set at {time_sunset} which will give you {tdelta} of sunlight")
            print(f"Precipitation: {precipitation} mm")
            print(f"Cloud coverage: {cloud_cover}%\n")
        else:
            print(f"Date: {formatted_date}, No average temperature data available")
else:
    print(f"No temperature data available for this location for the date range {start_date} to {end_date}")
