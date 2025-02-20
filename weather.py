import requests
from api_list import that, this

def get_daily_temperature(lat, lon, start, end):
    querystring = {
        "location": f"{lat},{lon}",  # Format the location as "lat,lon"
        "timesteps": "1d",            # Request daily data
        "units": "metric",            # Use metric units (optional based on your needs)
        "startTime": start,           # Start time in ISO 8601 format (e.g., "2024-08-18T00:00:00Z")
        "endTime": end                # End time in ISO 8601 format (e.g., "2024-08-19T00:00:00Z")
    }
    headers = {
        "x-rapidapi-this": this,
        "x-rapidapi-host": "tomorrow-io1.p.rapidapi.com"
    }
    response = requests.get(that, headers=headers, params=querystring)
    return response.json()


def get_outside_temperature_description(temp):
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


weatherCodes = {
    "0": "Unknown",
    "1000": "Clear, Sunny",
    "1100": "Mostly Clear",
    "1101": "Partly Cloudy",
    "1102": "Mostly Cloudy",
    "1001": "Cloudy",
    "2000": "Fog",
    "2100": "Light Fog",
    "4000": "Drizzle",
    "4001": "Rain",
    "4200": "Light Rain",
    "4201": "Heavy Rain",
    "5000": "Snow",
    "5001": "Flurries",
    "5100": "Light Snow",
    "5101": "Heavy Snow",
    "6000": "Freezing Drizzle",
    "6001": "Freezing Rain",
    "6200": "Light Freezing Rain",
    "6201": "Heavy Freezing Rain",
    "7000": "Ice Pellets",
    "7101": "Heavy Ice Pellets",
    "7102": "Light Ice Pellets",
    "8000": "Thunderstorm"
}
def weather_code_description(weather_code):
    return weatherCodes.get(str(weather_code), "Code not found")
    