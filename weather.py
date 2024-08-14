import requests
from datetime import datetime
from api_list import this, that

def get_daily_temperature(lat, lon, start, end):
    querystring = {"lat": lat, "lon": lon, "start": start, "end": end}
    headers = {
        "x-rapidapi-key": this,
    }
    response = requests.get(that, headers=headers, params=querystring)
    return response.json()

def extract_time(datetime_string):
    datetime_obj = datetime.strptime(datetime_string, '%Y-%m-%d %H:%M:%S')
    time_part = datetime_obj.strftime('%H:%M:%S')
    return time_part

def direction(wind_direction):
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
