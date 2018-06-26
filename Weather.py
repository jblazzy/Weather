"""
-- Weather.py
-- Josh Blaz
-- Denison University -- 2019
-- blaz_j1@denison.edu
"""
import requests

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
    URL2 = "api.openweathermap.org/data/2.5/forecast?zip={}".format(ZIP)
    json2 = requests.get(URL1).json()
    temp = json1['main']['temp']
    temp = (9/5) * (temp - 273) + 32
    #° F = 9/5 (K - 273) + 32
    print("Temperature: " + str(temp) + " °F")
    print("Current Weather: " + weather[0]['main'])
    print("Description: " + weather[0]['description'])
    #print("Forecast: ")
    # need to implement unix timestamp converter for 'dt' values

    # Use weather warnings from api aswell
    # There are currently no weather warnings
    # and the 5 day forecast is:


if __name__ == "__main__":
    main()
