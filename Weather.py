"""
-- Weather.py
-- Josh Blaz
-- Denison University -- 2019
-- blaz_j1@denison.edu
"""
import requests
import datetime
import calendar

def UnixConverter(timestamp):
    """
    Converts Unix Timestamps to normal time.
    See https://timestamp.online/article/how-to-convert-timestamp-to-datetime-in-python for Unix-to-time Conversion formatting.
    """
    return(datetime.datetime.fromtimestamp(int(timestamp)).strftime('%a, %B %dth %I%p'))

def KelvinToFahrenheit(temp):
    """
    Converts temperature value from Kelvin to Fahrenheit.
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
    tempstr1 = str(KelvinToFahrenheit(json1['main']['temp']))

    print("Current Weather Status")
    print("City: " + json1['name'])
    print("   Temperature: " + tempstr1[0:4] + " °F")
    print("Current Weather: " + weather[0]['main'])
    print("Description: " + weather[0]['description'])

    Forecast = input("Would you like to see the forecast? (Yes/No) \n")

    if (Forecast == "Yes"):
        print("Forecast:")
        for i in range(1, len(json2['list'])):  
            print(UnixConverter(json2['list'][i]['dt']))
            tempstr2 = str(KelvinToFahrenheit(json2['list'][i]['main']['temp']))
            print("   Temperature: " + tempstr2[0:4] + " °F")
            print("   " + "Current Weather: " + json2['list'][i]['weather'][0]['main'])
            print("   " + "Description: " + json2['list'][i]['weather'][0]['description'])
            print("   " + "Humidity: " + str(json2['list'][i]['main']['humidity']) + "%")
            print("")
    else:
        return
    # next step! : 
    # implement unix timestamp converter for 'dt' values in forecast data

    # Use weather warnings from api aswell
    # There are currently no weather warnings
    # and the 5 day forecast is:


if __name__ == "__main__":
    main()
