
def guidos_menu():
    user_name = input("Enter name: ")

    menu = """(H)ello\n(G)oodbye\n(Q)uit\n\n>>>> """

    user_input = input(menu).lower()

    while user_input != 'q':
        if user_input not in 'hgq':
            print("Invalid Choice")
        elif user_input == 'h':
            print("Hello {}".format(user_name))
        elif user_input == 'g':
            print("Goodbye {}".format(user_name))

        user_input = input(menu).lower()

    print("Finished.")

# guidos_menu()

import math
def sequence_generator():
    start_num = int(input("Enter the number to start at: "))
    end_num = int(input("Enter the number to end on: "))
    even_nums = []
    odd_nums = []

    print("The even numbers from {} to {} are:".format(start_num, end_num))
    for i in range(start_num, end_num+1):
        if i % 2 == 0:
            even_nums.append(i)
            print(i, end=" ")

    print("\nThe odd numbers from {} to {} are:".format(start_num, end_num))
    for i in range(start_num, end_num+1):
        if i % 2 != 0:
            odd_nums.append(i)
            print(i, end=" ")

    print("\nThe 'squares' between {} and {}".format(start_num, end_num))
    for i in range(start_num, end_num+1):
        s = math.sqrt(i)
        if s.is_integer():
            print(i, end=' ')

sequence_generator()




