
# Prompt user for 5 integers and store in list
def main():
    numbers = []
    for num in range(5):
        user_input = int(input("Number: "))
        numbers.append(user_input)

    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average of the numbers is {:.2f}".format(sum(numbers) / len(numbers)))

main()


# Refactor for indefinite prompting
def main():
    numbers = []
    continue_prompting = True
    count = 1
    while continue_prompting:
        try:
            user_input = int(input("Number {}: ".format(count)))
            if user_input < 0:
                continue_prompting = False
            else:
                numbers.append(user_input)
                count += 1
        except ValueError:
            print("Invalid input, try again")
    # for num in range(5):
    #     user_input = int(input("Number: "))
    #     numbers.append(user_input)
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average of the numbers is {:.2f}".format(sum(numbers) / len(numbers)))

main()


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
                 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command',
                 'ExecState', 'InteractiveConsole', 'InterpreterInterface',
                 'StartServer', 'bob']
users_name = input("Please enter your username: ")
if users_name in usernames:
    print("Access granted")
else:
    print("Access denied")