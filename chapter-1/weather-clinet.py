# modules and global variables
from abc import ABC,abstractmethod
import requests

# abstract class 
class WeatherAbstract(ABC):
    
    @abstractmethod
    def get_current_weather(self,lat,lon):
        pass
    
    
# open weather class
class OpenWeatherProvider(WeatherAbstract):
    
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    def __init__(self,api_key):
        self.api_key = api_key
        
    def get_current_weather(self, lat, lon):
        params = {
            "lat":lat,
            "lon":lon,
            "appid":self.api_key
        }
        response =requests.get(self.base_url,params=params)
        normalize_data = {"temp":float(response.json()["main"]["temp"]) - 273.15,"humidity":response.json()["main"]["humidity"]}
        return normalize_data
   
   
# open Mete class
class OpenMeteProvider(WeatherAbstract):
    
    base_url = "https://api.open-meteo.com/v1/forecast"
    
    def get_current_weather(self, lat, lon):
        params = {
            "latitude":lat,
            "longitude":lon,
            "current":"temperature_2m,relative_humidity_2m"
        }
        response =requests.get(self.base_url,params=params)
        normalize_data = {"temp":response.json()["current"]["temperature_2m"],"humidity":response.json()["current"]["relative_humidity_2m"]}
        return normalize_data
    
   
# running the application
provider = OpenMeteProvider()
# provider = OpenWeatherProvider("2a219d1298c9d04b0dd8b4629fc6db15")
print(provider.get_current_weather(lat=31.882910000000003,lon=54.369312))
    
