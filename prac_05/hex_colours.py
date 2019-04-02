
COLOURS = {
    "blue": "#0000ff",
    "brown": "#a52a2a",
    "black": "#000000",
    "yellow": "#ffff00",
    "white": "#ffffff",
    "red": "#ff0000",
    "pink": "#ffc0cb",
    "purple": "#a020f0",
    "orange": "#ffa500",
    "lavender": "#e6e6fa",
}

user_colour = input("Enter the name of a color: ").lower()

while user_colour != "":
    try:
        print(COLOURS[user_colour])
    except KeyError:
        print("that colour is not exist")
    user_colour = input("Enter the name of a color: ").lower()
