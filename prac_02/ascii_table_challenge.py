# ASCII Columns Challenge

# Constants
LOWER_BOUND = 33
UPPER_BOUND = 127
TOTAL_RANGE = UPPER_BOUND-LOWER_BOUND
ROWS = (TOTAL_RANGE//cols) + 1  # == 35 for cols==3

# Get Column Input
cols = int(input("Enter number of columns: "))
# For 2 cols
# 33 ! |  99 c
# 34 " | 100 d
# print("{:<3} {}".format(), end=" | ")
# print("{:<3} {}".format())

if cols == 1:
    for i in range(LOWER_BOUND, LOWER_BOUND + ROWS):
        print("{:<3} {}".format(i, chr(i)))

elif cols >= 2:
    for i in range(LOWER_BOUND, LOWER_BOUND+ROWS-1):
        # print("-" * (cols * 9))
        table = (cols - 1)  # For Cols end=' ' formatting

        # print table i.e. {..." | ") * table
        for j in range(table):
            print("{:<3} {}".format(i+ ROWS*j, chr(i + ROWS*j)), end="     ")

        # print end col
        print("{:>3} {}".format(i + ROWS*table, chr(i + ROWS*table)))
