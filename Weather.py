"""
-- Weather.py
-- Josh Blaz
-- Denison University -- 2019
-- blaz_j1@denison.edu
"""
import requests
import datetime

def UnixConverter(timestamp):
    """
    Converts Unix Timestamps to normal time.
    """
    return(datetime.datetime.fromtimestamp(int(timestamp)).strftime('%m-%d %H:%M'))
    # ('%Y-%m-%d %H:%M:%S') for full time string (Year, month, day)

def KelvinToFahrenheit(temp):
    """
    Converts Kelvin temperature to Fahrenheit.
    """
    return((9/5) * (temp - 273) + 32)

def main():
    ZIP = input("Please enter a ZIP Code: \n")
    """
    unsure if ZIP needs to be a string or int yet
    for now will leave as string
    """  
    # URL for basic weather info
    URL1 = "http://api.openweathermap.org/data/2.5/weather?appid=eb8707e702d345d487b0f91037928f2d&zip={}".format(ZIP)
    json1 = requests.get(URL1).json()
    weather = json1['weather']

    # URL for the forecast
    URL2 = "http://api.openweathermap.org/data/2.5/forecast?appid=eb8707e702d345d487b0f91037928f2d&zip={}".format(ZIP)
    json2 = requests.get(URL2).json()
    temp = json1['main']['temp']

    print("City: " + json1['name'])
    print("Temperature: " + str(KelvinToFahrenheit(temp)) + " °F")
    print("Current Weather: " + weather[0]['main'])
    print("Description: " + weather[0]['description'])
    print("Forecast:")
    for i in range(1, len(json2['list'])):  
        #print(UnixConverter(json2['list'][i]['dt']))
        print(json2['list'][i])

    # next step! : 
    # implement unix timestamp converter for 'dt' values in forecast data

    # Use weather warnings from api aswell
    # There are currently no weather warnings
    # and the 5 day forecast is:


if __name__ == "__main__":
    main()
