
# Note to Lects:
# "That is, the numbers 33 and 127 should appear only once [in your code]."

# Constants
LOWER_BOUND = 33
UPPER_BOUND = 127

# Get character from user
user_char = input("Enter a character: ")
user_ord = ord(user_char)
print("The ASCII code for g is {}".format(user_ord))

# Get num from user
valid_input = False
while not valid_input:
    try:
        user_num = int(input("Enter a number between {} and {}: ".format(LOWER_BOUND, UPPER_BOUND)))
    except ValueError:
        print("That is not a valid number")
    if LOWER_BOUND <= user_num <= UPPER_BOUND:
        print("The character for 100 is {}".format(chr(user_num)))
        valid_input = True

