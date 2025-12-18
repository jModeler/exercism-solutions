PRE = "For want of a"
END = "was lost."
THE = "the"
LAST = "And all for the want of a"


def proverb(*input_data, qualifier=None):
    result = []
    if not input_data:
        return result
    first_thing, *_ = input_data
    if len(input_data) > 1:
        thing, next_thing, *remaining = input_data
        while len(remaining) != 0:
            text = " ".join([PRE, thing, THE, next_thing, END])
            result.append(text)
            thing = next_thing 
            next_thing, *remaining = remaining
        # add the penultimate line
        result.append(" ".join([PRE, thing, THE, next_thing, END]))
    if qualifier:
        last_line = " ".join([LAST, qualifier, first_thing])
    else:
        last_line = " ".join([LAST, first_thing])
    last_line = last_line + "."
    result.append(last_line)
    return result