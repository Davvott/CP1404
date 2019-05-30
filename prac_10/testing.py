"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    if n == 1:
        return s
    return s + " " + repeat_string(s, n-1)
    # return (s + " ") * (n - 1) + s


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # 1. fix the repeat_string function above so that it passes the failing test
    # Hint: "-".join(["yo", "yo"] -> "yo-yo"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"

    # 2. write assert statements to show if Car sets the fuel correctly

    # Test keyword param
    test_car = Car(fuel=10)
    assert test_car.fuel == 10

    # Test default param
    test_car = Car("car")
    assert test_car.fuel == 0


def format_phrase_as_sentence(phrase):
    """Return phrase as sentence with staring capital and ending fullstop
    >>> format_phrase_as_sentence("hello")
    'Hello.'
    >>> format_phrase_as_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    """

    string = phrase.split()
    string[0] = string[0].title()
    if "." not in string[-1]:
        string[-1] = string[-1] + "."
    return " ".join(string)

run_tests()

# 3. Uncomment the following line and run the doctests
# (PyCharm may see your >>> doctest comments and run doctests anyway.)
doctest.testmod()

# 4. Fix the failing is_long_word function
# (don't change the tests, change the function!)

# 5. Write and test a function to format a phrase as a sentence,
# starting with a capital and ending with a single full stop.
# Important: start with a function header and just use pass as the body
# then add doctests for 3 tests:
# 'hello' -> 'Hello.'
# 'It is an ex parrot.' -> 'It is an ex parrot.'
# and one more you decide (one that is valid!)
# test this and watch the tests fail
# then write the body of the function so that the tests pass