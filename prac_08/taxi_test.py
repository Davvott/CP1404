from prac_08.taxi import Taxi

test_taxi = Taxi("Prius 1", 100, 1.23)

test_taxi.drive(40)
print(test_taxi, "Total: $ ", test_taxi.get_fare())


test_taxi.start_fare()

test_taxi.drive(100)
print(test_taxi, "Total: $ ", test_taxi.get_fare())

