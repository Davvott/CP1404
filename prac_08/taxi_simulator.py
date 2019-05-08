"""Menu Driven Taxi simulator - Complete with Drive function!"""

from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = """
q)uit, c)hoose, d)rive"""
MENU_OPTIONS = ("q", "c", "d")

def main():
    """Main menu driven loop"""
    Taxi.price_per_km = 1.20
    prius = Taxi("Prius", 100)
    limo = SilverServiceTaxi("Limo", 100, 2)
    hummer = SilverServiceTaxi("Hummer", 200, 4)
    taxis = [prius, limo, hummer]

    current_taxi = ''
    bill_to_date = 0

    print("Let's drive!")
    print(MENU)
    user_choice = get_menu_choice()
    while user_choice != "q":

        if user_choice == "c":
            current_taxi = choose_taxi(taxis)
            display_current_bill(bill_to_date)

        # TODO: Fix bug in drive vs fare
        elif user_choice == "d":

            drive_taxi(current_taxi)
            trip_fare = calculate_trip(current_taxi)
            bill_to_date += trip_fare
            display_current_bill(bill_to_date)

        print(MENU)
        user_choice = get_menu_choice()

    print("Total trip cost: {}".format(bill_to_date))
    print("Taxis are now: ")
    display_taxis(taxis)


def choose_taxi(taxis):
    print("Taxis available: ")
    display_taxis(taxis)

    taxi_choice = get_positive_int("Choose taxi: ")

    while taxi_choice > len(taxis)-1:
        print("Invalid choice")
        taxi_choice = get_positive_int("Choose taxi: ")

    return taxis[taxi_choice]


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


def drive_taxi(taxi):
    if taxi == "":
        print("No taxi selected")
        return
    drive_distance = get_positive_int("Drive how far? ")
    taxi.drive(drive_distance)


def calculate_trip(taxi):
    fare = taxi.get_fare()
    print("Your {} trip cost you ${:.2f}".format(taxi.name, fare))
    return fare


def display_current_bill(bill):
    print("Bill to date: ${:.2f}".format(bill))


def get_menu_choice():
    """Validate and return user's menu choice"""
    user_input = input(">>> ").lower()
    while user_input not in MENU_OPTIONS:
        print("Invalid menu choice")
        print(MENU)
        user_input = input(">>> ").lower()
    return user_input


def get_positive_int(prompt):
    """Validate and return positive integer input from user"""
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                print("Number must be >= 0")

        except ValueError:
            print("Invalid input; enter a valid number")


main()
