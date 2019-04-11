from datetime import datetime


class Guitar:

    def __init__(self, name='', year=0, cost=0.00):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        return 2019 - self.year

    def is_vintage(self):
        age = self.get_age()
        return age > 50


name = "Gibson L-5 CES"
year = 1922
cost = 16035.40
print("My guitar: {0}, first made in {1}".format(name, year))


def main():
    print("My guitars!")
    continue_loop = False
    guitars = []

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    # Input loop set to False for testing
    while continue_loop:
        guitar_name = input("Please enter a Name: ")
        if guitar_name.strip() == "":
            continue_loop = False
        else:
            guitar_year = int(input("Please enter the Year: "))
            guitar_cost = float(input("Please enter the Cost: "))

            guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))
    if guitars:
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage = "(vintage)" if guitar.is_vintage() else ""
            print("Guitar {}: ".format(i), end='')
            print("{:>20} ({}), worth ${:10,.2f} {}".format(
                guitar.name, guitar.year, guitar.cost, vintage))

main()
