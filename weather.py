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

def temperature_scale(temp):
    if temp != None:
        if temp > 40:
            return "outside feels like it's boilling"
        elif temp > 30 and temp <=40:
            return "outside feels like it's very hot"
        elif temp > 26 and temp <=30:
            return "outside feels like it's hot"
        elif temp > 22 and temp <=26:
            return "outside feels like it's warm"
        elif temp > 17 and temp <= 22:
            return "outside feels like it's mild"
        elif temp > 10 and temp <= 17:
            return "outside feels like it's cool"
        elif temp > 0 and temp <=10:
            return "outside feels like it's very cold"
        else:
            return "outside feels like it's freezing"
    else:
        return "Not enough information"

def get_wind_direction_description(wind_direction):
    if wind_direction is not None:
        if 0 <= wind_direction <= 55 or 305 <= wind_direction <= 360:
            if 305 <= wind_direction <= 325:
                return "The wind will be coming from North West with an average wind speed:"
            elif 326 <= wind_direction <= 349:
                return "The wind will be coming from NNW with an average wind speed:"
            elif 10 <= wind_direction <= 34:
                return "The wind will be coming from NNE with an average wind speed:"
            elif 35 <= wind_direction <= 55:
                return "The wind will be coming from North East with an average wind speed:"
            else:
                return "The wind will be coming from North with an average wind speed:"
        elif 56 <= wind_direction <= 125:
            if 56 <= wind_direction <= 79:
                return "The wind will be coming from ENE with an average wind speed:"
            elif 100 <= wind_direction <= 125:
                return "The wind will be coming from ESE with an average wind speed:"
            else:
                return "The wind will be coming from East with an average wind speed:"
        elif 126 <= wind_direction <= 235:
            if 215 <= wind_direction <= 235:
                return "The wind will be coming from South West with an average wind speed:"
            elif 190 <= wind_direction <= 215:
                return "The wind will be coming from SSW with an average wind speed:"
            elif 146 <= wind_direction <= 169:
                return "The wind will be coming from SSE with an average wind speed:"
            elif 126 <= wind_direction <= 145:
                return "The wind will be coming from South East with an average wind speed:"
            else:
                return "The wind will be coming from South with an average wind speed:"
        elif 236 <= wind_direction <= 304:
            if 280 <= wind_direction <= 304:
                return "The wind will be coming from WNW with an average wind speed:"
            elif 235 <= wind_direction <= 260:
                return "The wind will be coming from WSW with an average wind speed:"
            else:
                return "The wind will be coming from West with an average wind speed:"
        else:
            return "Invalid wind direction"
    else:
        return "No available information"

