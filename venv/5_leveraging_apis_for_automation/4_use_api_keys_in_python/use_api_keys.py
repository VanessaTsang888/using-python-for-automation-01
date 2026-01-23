# Access API that requires a key and make a GET request using the requests library with the appropriate parameters.
# import necessary libraries
import requests

# define base URL
base_url = "http://api.openweathermap.org/data/2.5/forecast"

# define parameters - my API key is the value of the second param 
parameters = {"q": "Paris,FR", "appid": "API_KEY"}

# make API request, passing in base URL and parameters
response = requests.get(base_url, params = parameters)

# print out text from API response
print(response.text)