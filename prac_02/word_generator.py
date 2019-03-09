"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random
import string



MENU = """Welcome to Scrabble Helper:
AUTOMATIC --->
    Press 'Enter' for a random word!
BROAD FORMAT --->
    Use chracter type only: "ccvccv"
    Enter (c) for consonants
    Enter (v) for vowels
WILDCARD FORMAT --->
    Using letters: "%re#"
    Enter (#) for vowel wildcard
    Enter (%) for consonant wildcard
    """

# CONSONANTS = "bcdfghjklmnpqrstvwxyz"
VOWELS = "aeiou"
CONSONANTS = string.ascii_lowercase
WILDCARDS = '#%'
for v in VOWELS:
    CONSONANTS = CONSONANTS.replace(v, '')
print(MENU)

# Get user word_format
word_format = "ccvcvvc"
wild_format = False
word = ""

user_word_format = input("Enter word shape e.g.'ccvcc': ").lower()


for wildcard in WILDCARDS:
    if wildcard in user_word_format:
        wild_format = True

if user_word_format == '':
    for _ in range(random.randint(1, 12)):
        user_word_format += random.choice(['c', 'v'])
if wild_format:
    for i, char_type in enumerate(user_word_format):
        if char_type == "%":
            word += random.choice(CONSONANTS)
        elif char_type == "#":
            word += random.choice(VOWELS)
        elif char_type.isalpha():
            word += char_type
else:  # assume 'ccvcc' format
    for char_type in user_word_format:
        if char_type == "c":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)

print(word)
