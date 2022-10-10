from geopy.geocoders import Nominatim

your_address = str(input())

geolocator = Nominatim(user_agent="basic_app")
location = geolocator.geocode(your_address)
if location:
    print((location.latitude, location.longitude))
else:
    print("Can not find your address!")