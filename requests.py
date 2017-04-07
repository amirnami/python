import requests
import math

# Changing User-Agent 

header = requests.utils.default_headers() # Get a copy of the default headers 
header.update(
    {
           "User-Agent" : "Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405"
    }
)

url = 'http://stackoverflow.com'
response = requests.get(url, headers=header)

# Displaying the Weather with Python 

url = "http://api.openweathermap.org/data/2.5/weather"
query_string = {'q' : 'Tehran,ir', 'appid' : '61f18264b1a8919cea3d08556ebe74f8'}
response = requests.get(url, params=query_string)
temp =  int(response.json()['main']['temp'])
temp = int(math.ceil(temp - 273.15))
print temp

# Displaying the Weather with Python 
