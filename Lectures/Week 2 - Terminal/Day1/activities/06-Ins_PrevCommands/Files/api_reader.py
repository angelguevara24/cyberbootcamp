# Dependencies
import requests as req

url = "http://api.worldbank.org/"
format = "json"

# Get country information in JSON format
countries_response = req.get(url + "countries" + "?format=" + format).json()

# First element is general information, second is countries themselves
countries = countries_response[1]

# Report the names
for country in countries:
    print(country["name"])
