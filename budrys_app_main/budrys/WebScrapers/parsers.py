import geocoder
from budrys_app.models import Location, Animals


def parse_location(address):
    try:
        location = Location.objects.get(address__icontains=address)
    except Location.DoesNotExist:
        location_data = geocoder.osm(address)
        new_location = Location.objects.create(name=location_data.address.split(',')[0],
                                               address=address,
                                               latitude=location_data.lat,
                                               longitude=location_data.lng)
        return new_location
    else:
        return location


def parse_size( weight, species):
    if species == 'pies':
        if weight <= 5:
            return 'mały'
        elif 6 <= weight <= 10:
            return 'średni mniejszy'
        elif 11 <= weight <= 15:
            return 'średni'
        elif 16 <= weight <= 20:
            return 'śwedni większy'
        elif 21 <= weight:
            return 'duży'
    else:
        if weight <= 2:
            return 'mały'
        elif 3 <= weight <= 5:
            return 'średni mniejszy'
        elif 6 <= weight <= 8:
            return 'średni'
        elif 9 <= weight <= 11:
            return 'śwedni większy'
        elif 11 <= weight:
            return 'duży'


def animal_update_or_create(item):
    animal, created = Animals.objects.update_or_create(url=item['url'],
                                                       defaults=item
                                                       )

# address = 'Towarzystwo Opieki nad Zwierzętami w Polsce Schronisko dla Bezdomnych Zwierząt we Wrocławiu'
# geocode = geocoder.osm(address)
# print(geocode.json)
# print(geocode.address)