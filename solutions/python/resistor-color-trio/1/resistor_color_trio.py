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

def format_resistance(result, value):
    if result%10 == 0:
        value += 1
        result = result//10
        
    if value >= 9:
        result = " ".join([str(result), "gigaohms"])
    elif 6 <= value < 9:
        result *= 10**(value - 6)
        result = " ".join([str(result), "megaohms"])
    elif 3 <= value < 6:
        result *= 10**(value - 3)
        result = " ".join([str(result), "kiloohms"])
    else:
        result *= 10**value 
        result = " ".join([str(result), "ohms"])
    return result



def label(colors):
    resistors = colors[0:3]
    result = 0
    for ii in range(len(resistors)):
        if ii < 2:
            result = result * 10 + RESISTOR_COLOR[resistors[ii]]
        else:
            result = format_resistance(result, RESISTOR_COLOR[resistors[ii]])
    return result