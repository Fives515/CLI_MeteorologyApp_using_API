import datetime
from astral import LocationInfo
from astral.sun import sun

x=datetime.datetime.now()
day=(x.strftime("%d"))
month=(x.strftime("%m"))
year = datetime.datetime.now()
print(year)
city = LocationInfo("London","England", "Europe/London", 51.43626662318104, -0.05197242930741357)
s=sun(city.observer, date=year)

print(city.name, city.timezone)
print((
    f'Dawn:    {s["dawn"]}\n'
    f'Sunrise: {s["sunrise"]}\n'
    f'Noon:    {s["noon"]}\n'
    f'Sunset:  {s["sunset"]}\n'
    f'Dusk:    {s["dusk"]}\n'
))


