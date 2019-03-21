# Write a program prompting user for number of quick picks.
# Generate this number of lines of output with 6 random nums; 1<num<45

import random

NUM_QUICK_PICKS = 6
LOWER_BOUND = 1
UPPER_BOUND = 45

# Prompt user
number_of_picks = int(input("How many quick picks? "))

# Each line should not contain a repeated number
# Each line should be displayed in sorted ascending order

for i in range(number_of_picks):

    # Use set to exclude duplicates
    quick_picks = set(random.randint(LOWER_BOUND, UPPER_BOUND)
                      for _ in range(NUM_QUICK_PICKS))

    # Convert to list and sort
    quick_picks = sorted(list(quick_picks))

    # Print [:-1] of quick_picks, then print last quick_pick
    for num in range(number_of_picks - 1):
        print("{:2} ".format(quick_picks[num]), end='')
    print("{:2}".format(quick_picks[-1]))

    # line_list = []
    # for num in range(NUM_QUICK_PICKS):
    #     line_list.append(random.randint(LOWER_BOUND, UPPER_BOUND))
