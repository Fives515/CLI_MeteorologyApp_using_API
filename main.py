from datetime import *
from astral import LocationInfo
from astral.sun import sun
import matplotlib.pyplot as plt
from meteostat import Point, Daily


time = datetime.now()
end = datetime(2024, 7, 31)
city = LocationInfo("London","England", "Europe/London", 51.43626662318104, -0.05197242930741357)
location = Point(51.43626662318104, -0.05197242930741357)
s=sun(city.observer, date=time)
data = Daily(location, time, end)
data=data.fetch()
data.plot(y=["tavg", "tmin", "tmax"])
plt.show()
print(data)

print(city.name, city.timezone)
print((
    f'Dawn:    {s["dawn"]}\n'
    f'Sunrise: {s["sunrise"]}\n'
    f'Noon:    {s["noon"]}\n'
    f'Sunset:  {s["sunset"]}\n'
    f'Dusk:    {s["dusk"]}\n'
))


