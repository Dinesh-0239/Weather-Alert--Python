import requests

class Data:
    def __init__(self,location):
        parameter = {
            "q": location
        }
        end_point = "https://geocode.maps.co/search"
        cor_response = requests.get(url=end_point,params=parameter)
        cor_response.raise_for_status()
        self.data = cor_response.json()

    def get_alert(self):
        lat = float(self.data[0]["lat"])
        lon = float(self.data[0]["lon"])
        api_key = "5c33d3b47a822761c13867d33e18927d"
        end_point = "https://api.openweathermap.org/data/2.5/weather"
        parameter = {
            "lat": lat,
            "lon": lon,
            "appid": api_key
        }
        w_response = requests.get(url=end_point,params=parameter)
        w_response.raise_for_status()
        weather_data = w_response.json()
        condition_code = weather_data["weather"][0]["id"]
        if condition_code > 700:
            return True
        else:
            return False

