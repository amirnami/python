# pip install requests
# pip install pygeoip

import requests
import pygeoip

url_ip = "http://httpbin.org/ip"
response_ip = requests.get(url_ip)
ip_addr = str(response_ip.json()['origin'])

# http://dev.maxmind.com/geoip/legacy/install/city/
gi = pygeoip.GeoIP('/usr/local/share/GeoIP/GeoLiteCity.dat')
cc = gi.record_by_addr(ip_addr)['city'] + "," + gi.record_by_addr(ip_addr)['country_code'].lower()
print cc

url_owm = "http://api.openweathermap.org/data/2.5/weather"
query_string = {'q' : cc, 'appid' : '61f18264b1a8919cea3d08556ebe74f8'}
response_owm = requests.get(url_owm, params=query_string)
temp =  int(response_owm.json()['main']['temp'])
temp = int(math.ceil(temp - 273.15))
print temp
