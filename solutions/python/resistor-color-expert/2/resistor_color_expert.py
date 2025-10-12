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

TOLERANCE = {
    "grey": "±0.05%",
    "violet": "±0.1%",
    "blue": "±0.25%",
    "green": "±0.5%",
    "brown": "±1%",
    "red": "±2%",
    "gold": "±5%",
    "silver": "±10%"
}

def format_resistance(result, tolerance=None):
    # get the number of digits
    digits = len(str(result))
    # power value
    value = digits - 1
    if value < 3:
        result = " ".join([str(result), "ohms"])
    elif 3 <= value < 6:
        result = result//10**3 if result%10**3 == 0 else result/10**3
        result = " ".join([str(result), "kiloohms"])
    elif 6 <= value < 9:
        result = result/10**6 if result%10**6 == 0 else result/10**6
        result = " ".join([str(result), "megaohms"])
    else:
        result = result/10**9 if result%10**9 == 0 else result/10**9
        result = " ".join([str(result), "gigaohms"])
    
    if tolerance is None:
        return result
    else:
        return " ".join([result, tolerance])


def resistor_label(colors):
    result = 0
    for ii in range(len(colors)):
        if ii == (len(colors) - 2) and ii >= 2:
            # multiplier
            result *= 10**RESISTOR_COLOR[colors[ii]]
        elif ii == (len(colors) - 1) and ii >= 3:
            # tolerance
            result = format_resistance(result, TOLERANCE[colors[ii]])
        else:
            result = result*10 + RESISTOR_COLOR[colors[ii]]
    
    if len(colors) <= 3:
        return format_resistance(result)
    else:
        return result