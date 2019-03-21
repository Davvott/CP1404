"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":

        if choice == "C":
            celsius = float(input("Celsius: "))
            convert_celsius_to_fahrenheit(celsius)

        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            convert_fahrenheit_to_celsius(fahrenheit)

        else:
            print("Invalid option")

        print("\n", MENU)
        choice = input(">>> ").upper()

    print("Thank you.")


def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert fahrenheit to celsius from parameter"""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius
    # return "Result: {:.2f} C".format(celsius)


def convert_celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit from parameter"""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit
    # return "Result: {:.2f} F".format(fahrenheit)

main()
