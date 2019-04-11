from datetime import datetime


class Guitar:

    def __init__(self, name='', year=0, cost=0):
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
