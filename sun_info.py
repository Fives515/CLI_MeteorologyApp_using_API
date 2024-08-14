from datetime import datetime
from weather import extract_time

def get_sun_times(sun, time):
    sunrise = sun.get_local_sunrise_time(time)
    sunset = sun.get_local_sunset_time(time)
    
    # Extract the time and calculate it
    datetime_string = str(sunrise)
    time_sunrise = extract_time(datetime_string)
    datetime_string = str(sunset)
    time_sunset = extract_time(datetime_string)
    format = "%H:%M:%S"
    tdelta = datetime.strptime(time_sunset, format) - datetime.strptime(time_sunrise, format)
    
    return time_sunrise, time_sunset, tdelta
