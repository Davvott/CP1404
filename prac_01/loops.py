
# Count odds to 20
for i in range(1, 21, 2):
    print(i, end=' ')

print()

# Count in 10's
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# Cound down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# print n stars
user_input = int(input("How many stars?: "))

for i in range(1, user_input+1):
    print('*', end='')
print()

# print n lines of increasing stars
for i in range(1, user_input+1):
    print('*' * i)

# print a tree
for i in range(0, user_input+1):
    mid = user_input
    stars = "*"*i
    spaces = " " * (mid - len(stars))
    # print(spaces, stars + "*" + stars)
    print("{}".format("*"*i:user_input*2))

for i in range(user_input, 0, -1):
    mid = user_input

