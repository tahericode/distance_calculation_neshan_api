import requests
from django.conf import settings

def neshan_distance(long_origin, lat_origin, long_destination, lat_destination):
        # Headers For Request Api 
        api_key = settings.NESHAN_API_KEY
        headers = {"Api-Key": api_key}
        # Api Call 
        URL = "https://api.neshan.org/v2/direction/no-traffic?destination={},{}&origin={},{}".format(long_origin, lat_origin,long_destination ,lat_destination)
        # Get Response
        r = requests.get(url = URL, headers = headers )
        # Convert Response To Json
        data = r.json()
        # Extract Distance From Json
        dis = data['routes'][0]['legs'][0]['distance']['value']
        # Convert Meter To Kilometer
        final_distance = (dis/1000)
        # Return Distance
        return final_distance