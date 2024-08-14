import requests
from api_list import key


def get_current_location():
    url = f'https://www.googleapis.com/geolocation/v1/geolocate?key={key}'
    
    response = requests.post(url, json={"considerIp": "true"})
    location_data = response.json()
    while True:
        userinput = input("1. If want to enter your coordinates \n"
                        "2. If you want to use your current location\n"
                        "Select from the following options: ")

        if userinput == "1":
            input_coordinates = input("Example: 51.4359296, -0.0622592 coordinates for London \n Please enter the coordinates of your chosen location:")
            if input_coordinates == "":
                print("Incorrect format, using closest possible coordinates")
                return data_from_current_location(location_data)
            else:
                location= get_coordinates_from_user(input_coordinates)
            latitude = float(location [0])
            longitude = float(location [1])
            city = get_city_from_coords(latitude, longitude)
            return latitude, longitude, city

        elif userinput == "2":
            return data_from_current_location(location_data)
            

        else:
            print("Wrong input, try again\n\n\n\n")

def data_from_current_location(location):
    if "location" in location:
        latitude = location["location"]["lat"]
        longitude = location["location"]["lng"]
        city = get_city_from_coords(latitude, longitude)
        return latitude, longitude, city
    else:
        return None, None, "Unknown"

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

def get_coordinates_from_user(coordinates):
    coordinates = coordinates.split(",")
    return coordinates