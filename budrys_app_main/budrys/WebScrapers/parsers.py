import requests

from budrys_app.models import Location


def parse_location(address):
    try:
        location = Location.objects.get(address__icontains=address)
    except Location.DoesNotExist:
        url = 'https://maps.googleapis.com/maps/api/geocode/json'
        params = {'sensor': 'false', 'address': address}
        r = requests.get(url, params=params)
        results = r.json()['results']
        location = results[0]['geometry']['location']

        new_location = Location.objects.cerate(address=address,
                                               latitude=location['lat'],
                                               longitude=location['lng'])
        return new_location
    else:
        return location