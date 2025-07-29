COLOUR_CODES = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "Blue": "#0000ff"
}

colour_name = input("Enter colour name: ").title()
while colour_name != "":
    print(f"The code for {colour_name} is {COLOUR_CODES.get(colour_name, 'Invalid colour name')}")
    colour_name = input("Enter colour name: ").title()
