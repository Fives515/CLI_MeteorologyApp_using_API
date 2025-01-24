## Introduction

This is a simple project using APIs to access meteorological data and display it to users using a command line interface.
**Meteorological data can be displayed using the public IP address or a specific coordinate**
## APIs used
[Google's GeolocationAPI](https://cloud.google.com/)

[MeteoStatAPI](https://dev.meteostat.net/api/) **Note:** This project used [RapidAPI](https://rapidapi.com/) was used for easier access

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies from **requirements.txt**.

```bash
pip install -r requirements.txt
```

## API setup
Run main.py with python after adding links to the API's
```python
#rapidAPI details
this= "Insert MeteostatAPI-Key here"
that = ".https://meteostat.p.rapidapi.com/point/daily" #pointer link for daily data 
#Google API key
key = "Insert Google API Key here"
```
## Documentation on Meteostat
This was the documentation used to setup
[Meteostat daily data](https://dev.meteostat.net/api/stations/daily.html#endpoint)
