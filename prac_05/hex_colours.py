
colour_codes = {"black": "#000000", "red1": "#ff0000",
                "blue1": "#	#0000ff", "green1": "##00ff00",
                "yellow1": "#ffff00", "gray": "#bebebe",
                "cyan1": "#00ffff", "brown": "#a52a2a",
                "gold1": "#ffd700", "lavender": "#e6e6fa",
                "purple": "#a020f0"}

colour_name = input("Enter a colour: ")

while colour_name != "":

    print("The code for \"{}\" is not available".format(colour_name, colour_codes.get(colour_name)))
    colour_name = input("Enter a colour name: ")
