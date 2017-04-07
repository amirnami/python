import requests
import math

url = "http://api.openweathermap.org/data/2.5/weather"
query_string = {'q' : 'Tehran,ir', 'appid' : '61f18264b1a8919cea3d08556ebe74f8'}
response = requests.get(url, params=query_string)
temp =  int(response.json()['main']['temp'])
temp = int(math.ceil(temp - 273.15))
print temp
