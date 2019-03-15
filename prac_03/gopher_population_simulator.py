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
BIRTH_RANGE = [.1, .21]
DEATHS_RANGE = [.05, .25]


def main():
    population = 1000
    print("Welcome to the Gopher Population Simulator!")
    print("Starting population: {}".format(population))

    for y in range(1, PERIOD):
        births, deaths = calc_pop_change(population)
        population += (births - deaths)

        print("{} gophers were born. {} died.".format(births, deaths))
        print("Population: {}".format(population))
        print("Year {}\n".format(y))


def calc_pop_change(population):
    born = round(random.uniform(BIRTH_RANGE[0], BIRTH_RANGE[1]) * population)
    deaths = round(random.uniform(DEATHS_RANGE[0], DEATHS_RANGE[1]) * population)
    return born, deaths


main()

