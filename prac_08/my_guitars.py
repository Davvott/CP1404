"""Main client code for testing Guitar class"""

from prac_08.guitars import Guitar
FILE_NAME = "guitars.csv"


def main():
    print("My guitars!")

    list_of_guitars = load_file()
    list_of_guitars = create_guitars(list_of_guitars)
    display_guitars(list_of_guitars)

    continue_loop = True
    # User addition to guitars
    while continue_loop:
        print("\nTo add a guitar, follow the prompts")
        guitar_name = input("Please enter a Name: ")
        if guitar_name.strip() == "":
            continue_loop = False
        else:
            guitar_year = int(input("Please enter the Year: "))
            guitar_cost = float(input("Please enter the Cost: "))

            list_of_guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))
        display_guitars(list_of_guitars)
    display_guitars(list_of_guitars)

    save_file(list_of_guitars)


def display_guitars(list_of_guitars):
    list_of_guitars.sort()
    # Print list
    if list_of_guitars:
        print("These are my guitars:")

        for i, guitar in enumerate(list_of_guitars, 1):
            vintage = "(vintage)" if guitar.is_vintage() else ""

            print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(
                i, guitar.name, guitar.year, guitar.cost, vintage))


def save_file(guitars):
    file_out = open(FILE_NAME, "w")
    for guitar in guitars:
        line = ",".join([guitar.name, str(guitar.year), str(guitar.cost)])
        file_out.write(line + "\n")
        # Auto add "\n" ?
        # print(line, file=file_out)
    file_out.close()


def load_file():
    """Open file and clean data; return list of tuples"""
    list_of_data = []
    data_file = open(FILE_NAME, "r")
    for line in data_file:
        line = line.strip().split(",")
        list_of_data.append(tuple(line))
    data_file.close()

    return list_of_data


def create_guitars(guitars):
    """Return list of Guitar objects"""
    class_list = []
    for i, guitar in enumerate(guitars):
        class_list.append(Guitar(guitar[0], int(guitar[1]), float(guitar[2])))
    return class_list


main()
