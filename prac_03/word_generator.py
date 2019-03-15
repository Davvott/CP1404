"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random
from string import ascii_lowercase

MENU = """
Welcome to Scrabble Helper:
FORMAT --->
    Use character type only: "ccvccv"
    Enter (c) for consonants
    Enter (v) for vowels
"""

# CONSONANTS = "bcdfghjklmnpqrstvwxyz"
VOWELS = "aeiou"
CONSONANTS = "".join([c for c in ascii_lowercase if c not in VOWELS])
# WILDCARDS = '#%'


def main():
    print(MENU)
    # Get user word_format
    valid_word = False

    # if user_word_format == '':
    #     for _ in range(random.randint(1, 12)):
    #         user_word_format += random.choice(['c', 'v'])

    while not valid_word:
        user_word_format = input("Enter word shape e.g.'ccvcc': ").lower()
        valid_word = is_valid_format(user_word_format)
    word = get_word(user_word_format)
    print(word)


def get_word(user_word_format):
    """Get random word from user format"""
    word = ""
    for char_type in user_word_format:
        if char_type == "c":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)
    return word


def is_valid_format(user_word_format):
    """Check user_word_format contains only 'c' or 'v'"""
    for char_type in user_word_format:
        if char_type != "c" and char_type != "v":
            print("Format is invalid. Try again")
            return False

    return True


main()
