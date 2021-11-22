import phonenumbers

from test import number

from phonenumbers import geocoder

ch_nmber = phonenumbers.parse(number, "IN")

print(geocoder.description_for_number(ch_nmber, "en"))

from phonenumbers import carrier

service_number = phonenumbers.parse(number, "IN")

print(carrier.name_for_number(service_number, "en"))

from phonenumbers import timezone

gb_number = phonenumbers.parse(number, "IN")

print(timezone.time_zones_for_number(gb_number))