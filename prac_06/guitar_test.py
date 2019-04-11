from prac_06.guitars import Guitar

name = "Gibson L-5 CES"
year = 1922
cost = 16035.40
# print("My guitar: {0}, first made in {1}".format(name, year))
test_guitar = Guitar(name, year, cost)
name = "Ukele - pygmy"
year = 2013
cost = 16035.40
second_guitar = Guitar(name, year, cost)

print("{} get_age() - Expected 96. Got {}".format(
    test_guitar.name, test_guitar.get_age()))

print("{} is_vintage() - Expected 96. Got {}".format(
    test_guitar.name, test_guitar.is_vintage()))

print("{} get_age() - Expected True. Got {}".format(
    second_guitar.name, second_guitar.get_age()))

print("{} is_vintage() - Expected False. Got {}".format(
    second_guitar.name, second_guitar.is_vintage()))
