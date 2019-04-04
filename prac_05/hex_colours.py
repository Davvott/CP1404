
COLOURS = {"aliceblue": "#f0f8ff",
           "antiquewhite": "#faebd7",
           "antiquewhite1": "#ffefdb",
           "antiquewhite2": "#eedfcc",
           "antiquewhite3": "#cdc0b0",
           "antiquewhite4": "#8b8378",
           "aquamarine1": "#7fffd4",
           "aquamarine2": "#76eec6",
           "aquamarine4": "#458b74",
           "azure1": "#f0ffff",
           "azure2": "#e0eeee",
           "azure3": "#c1cdcd",
           "azure4": "#838b8b",
           "beige": "#f5f5dc",
           "bisque1": "#ffe4c4",
           "bisque2": "#eed5b7"}

user_colour = input("Enter the name of a color: ").lower()

while user_colour != "":
    try:
        print(COLOURS[user_colour])
    except KeyError:
        print("that colour is not exist")
    user_colour = input("Enter the name of a color: ").lower()
