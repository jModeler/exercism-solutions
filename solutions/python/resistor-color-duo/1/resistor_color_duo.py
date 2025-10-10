RESISTOR_COLOR = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}

def value(colors):
    list_colors = colors[0:2]
    result = 0
    for ii in list_colors:
        result = result * 10 + RESISTOR_COLOR[ii]
    return result

