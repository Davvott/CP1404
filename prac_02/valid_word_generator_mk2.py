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
    Include letters: "%re#"
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

word = ""
word_format = "ccvcvvc"
wild_format = False

# Get user word_format
user_word_format = input("Enter word shape: ").lower()

def wildcard_search(user_format):
    word = ''
    for i, char_type in enumerate(user_format):
        if char_type == "%":
            word += random.choice(CONSONANTS)
        elif char_type == "#":
            word += random.choice(VOWELS)
        elif char_type.isalpha():
            # Skip numbers or other chars
            word += char_type
    return word

def word_gen(format):
    word = ''
    for char_type in word_format:
        if char_type == "c":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)
    return word

# VERSION_II
# Check for wildcards
for wildcard in WILDCARDS:
    if wildcard in user_word_format:
        wild_format = True

dictionary = []
with open('dictionary.txt', 'r') as file:
    for line in file:
        dictionary.append(line.rstrip('\n'))
        #Have to remember to strip \n !

continue_loop = True

while word not in dictionary and continue_loop:
    # Generator Selection
    if user_word_format == '':
        word = ''
        for _ in range(random.randint(1, 12)):
            word += random.choice(string.ascii_lowercase)
    elif wild_format:
        word = wildcard_search(user_word_format)
    else:  # assume 'ccvcc' format
        word = word_gen(user_word_format)

print(word)
