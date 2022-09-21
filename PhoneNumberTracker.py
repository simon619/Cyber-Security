import phonenumbers
from TheNumber import number
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import folium

key = 'Enter Your API Key From Opencage'

number = '' # Enter Mobile Number
target_number = phonenumbers.parse(number)
target_location = geocoder.description_for_number(target_number, "en")
print(f'Target Country: {target_location}') # Target Phone Number Country

target_service_provider = phonenumbers.parse(number)
target_service_provider_name = carrier.name_for_number(target_service_provider, 'en')
print(f'Target Service Provider: {target_service_provider_name}') # Target Mobile Number Network Provider

geocoder = OpenCageGeocode(key)
query = str(target_location)
result = geocoder.geocode(query)

print(result)
for i in range(len(result)):
    lat = result[i]['geometry']['lat']
    lng = result[i]['geometry']['lng']
    my_map = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=target_location).add_to(my_map)
    my_map.save('Locations/location' + str(i) +'.html')  # This Result is not Accurate



