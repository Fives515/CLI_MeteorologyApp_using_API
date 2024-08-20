from datetime import datetime

def get_sun_times(time_sunrise, time_sunset):
    if time_sunrise and time_sunset:
        time_sunrise = datetime.strptime(time_sunrise, '%Y-%m-%dT%H:%M:%SZ').strftime('%H:%M')
        time_sunset = datetime.strptime(time_sunset, '%Y-%m-%dT%H:%M:%SZ').strftime('%H:%M')
        tdelta = datetime.strptime(time_sunset, '%H:%M') - datetime.strptime(time_sunrise, '%H:%M')
    else:
        time_sunrise = time_sunset = tdelta = "N/A"

    return time_sunrise, time_sunset, tdelta