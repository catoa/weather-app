import requests

# settings.configure()
# api_key = settings.DARK_SKY_WEATHER_API_KEY
# This API is now fully deprecated as it has been absorbed into Apple's ecosystem.
api_url = f"https://api.darksky.net/forecast/96aea29e68c8f53be954b2b4c9707d4d/"


def fetch_forecast(lat: float, lon: float) -> dict:
    lat_lon = str(lat) + ',' + str(lon)
    location_url = api_url + lat_lon
    return requests.get(location_url).json()




if __name__ == '__main__':
    user_lat, user_lon = 42.3601, -71.0589
    resp_dict = fetch_forecast(user_lat, user_lon)
    print(resp_dict['daily'])
