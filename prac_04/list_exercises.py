# Prompt user for 5 integers and store in list
numbers = []

for num in range(5):
    user_input = int(input("Number: "))
    numbers.append(user_input)

print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
print("The average of the numbers is {}".format(sum(numbers)/len(numbers)))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
             'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command',
             'ExecState', 'InteractiveConsole', 'InterpreterInterface',
             'StartServer', 'bob']

users_name = input("Please enter your username: ")
if users_name in usernames:
    print("Access granted")
else:
    print("Access denied")


