"""
A secret population of 1000 gophers lives near the library.
Every year, a random number of gophers is born, between 10% of the current
population, and 20%. (e.g. 15% of the gophers might give birth,
increasing the population by 150). Also each year, a random number of gophers die,
between 5% and 25% (e.g. 8% of the gophers might die, reducing the population
by 80).

Write a program that simulates a population of gophers over a ten-year period
and displays each year's population size. The output should look something like
 this (it's random, so yours won't be the same):

Welcome to the Gopher Population Simulator!
Starting population: 1000
Year 1

145 gophers were born. 228 died.
Population: 917
Year 2

124 gophers were born. 152 died.
Population: 889
Year 3

138 gophers were born. 180 died.
Population: 847
"""
import random

PERIOD = 10


def main():
    population = 1000
    print("Welcome to the Gopher Population Simulator!")
    print("Starting population: {}".format(population))
    for y in range(1, PERIOD):
        born = round(random.uniform(.1, .21) * population)
        deaths = round(random.uniform(.5, .25) * population)
        population += born
        population -= deaths

        print("{} gophers were born. {} died.".format(born, deaths))
        print("Population: {}".format(population))
        print("Year {}\n".format(y))


main()

