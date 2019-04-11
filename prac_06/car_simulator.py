from prac_06.car import Car


MENU = """
Menu:
d) drive
r) refuel
q) quit
Enter your choice: """
MENU_OPTIONS = ['d', 'r', 'q']


def main():
    print("Let's driver!")


    car_name = input("Enter your car name: ")
    user_car = Car(100, car_name)
    continue_loop = True

    while continue_loop:
        print(user_car)
        menu_choice = get_menu_choice()
        if menu_choice == MENU_OPTIONS[0]:
            drive_car(user_car)

        elif menu_choice == MENU_OPTIONS[1]:
            # call refuel_car
            pass
        elif menu_choice == MENU_OPTIONS[2]:
            print("Good bye {}'s driver".format(car_name))


def get_menu_choice():
    choice = input(MENU).lower()
    while choice not in MENU_OPTIONS:
        print("Invalid choice")
        choice = input(MENU).lower()
    return choice

def get_postitive_int(unit, prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
        except ValueError:
            pass
        print("{} must be >= 0")

def drive_car(car):
    prompt = "How many km do you wish to drive? "
    distance = get_postitive_int("Distance", prompt)
    actual_distance = car.drive(distance)
    print("The care drove {}km".format(actual_distance), end='')
    if car.fuel == 0:
        print("and ran out of fuel.")
    else:
        print(".")

