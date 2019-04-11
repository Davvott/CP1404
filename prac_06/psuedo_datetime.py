
class DateTime:

    def __init__(self, day, month, year):
        self.day = self.set_year(day)
        self.month = self.set_month(month)
        self.year = self.set_year(year)

    def set_day(self, d):
        if not isinstance(d, int):
            raise TypeError("Must be an integer")
        elif 1 > d > 31:
            raise TypeError("Must be between 1-31")
        else:
            self.day = d

    def set_month(self, month):
        if not isinstance(month, int):
            raise TypeError("Must be an integer")
        elif 1 > month > 12:
            raise TypeError("Must be between 1-12")
        else:
            self.day = month

    def set_year(self, year):
        if not isinstance(year, int):
            raise TypeError("Must be an integer")
        elif 1 > year > 2019:
            raise TypeError("Must be between 1-2019")
        else:
            self.day = year

    def __str__(self):
        print("{}/{}/{}".format(self.day, self.month, self.year))

    def add_days(self, n):
        pass



date = DateTime(2, 34, "int")
