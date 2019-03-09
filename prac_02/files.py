# get user-name
user_name = input("Please enter your name: ")

out_file = open("name.txt", "w")
print("Your name is {}".format(user_name), file=out_file)
out_file.close()

out_file = open("numbers.txt", "w")
print("17", file=out_file)
print("42", file=out_file, end='')  # must be careful about auto \n in filewrite
out_file.close()

# Sum numbers.txt
with open("numbers.txt", "r") as file:
    sum = 0
    for line in file:
        sum += int(line)
print(sum)

# Cruising? Print the total for a file containing any number of ints
with open("numbers.txt", "r") as file:
    sum = 0
    sum += (int(line) for line in file)

# print infinite sum!