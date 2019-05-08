"""Unreliable class derived from Car"""

from prac_06.car import Car
from random import randrange


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability=randrange(0, 100, 1)):
        """Initialise UnreliableCar from parent Car class"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return a string like a Car but with reliability of car."""
        return "{}, reliability = {}".format(super().__str__(), self.reliability)

    def drive(self, distance):

        if randrange(0, 100, 1) < self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven
