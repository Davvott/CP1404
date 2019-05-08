"""Test code for SilverServiceTaxi class"""

from prac_08.silver_service_taxi import SilverServiceTaxi

limo = SilverServiceTaxi("Stretch", 100, 2)

limo.start_fare()
limo.drive(18)
assert limo.get_fare() == 48.80  # Updated for Taxi.get_fare round() value
print(limo)

hummer = SilverServiceTaxi("Boss", 100, 4)
print(hummer)
