from datetime import datetime

FILE_NAME = "guitars.csv"


class Guitar:

    def __init__(self, name='', year=0, cost=0.00):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Almost redundant getter"""
        this_year = datetime.today().year
        return this_year - self.year

    def is_vintage(self):
        """Vintage guitar if age > 50"""
        age = self.get_age()
        return age > 50

    def __lt__(self, other):
        """Override < sort; Sort Guitars by year"""
        # Returns bool on class attribute !
        return self.year < other.year
