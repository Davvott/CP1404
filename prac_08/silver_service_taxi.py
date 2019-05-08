"""SilverServiceTaxi class derived from Taxi class"""

from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised Taxi class"""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise SilverServiceTaxi, from Taxi and Car base classes"""
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km
        self.price_per_km *= fanciness

    def __str__(self):
        """Return Taxi and Car __str__ plus flagfall"""
        return "{}, plus flagfall of ${}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """Return price of fare with flagfall"""
        return self.flagfall + super().get_fare()
