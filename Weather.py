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
    URL = "api.openweathermap.org/data/2.5/weather?zip={}".format(ZIP)
    print(URL)



if __name__ == "__main__":
    main()
