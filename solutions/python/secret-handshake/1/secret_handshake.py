ACTIONS = {
    0: "wink",
    1: "double blink",
    2: "close your eyes",
    3: "jump"
}

def commands(binary_str):
    # reverse the string
    hs = binary_str[::-1]
    result = []
    for ii in range(len(hs)):
        if hs[ii] == "1" and ii != 4:
            result.append(ACTIONS[ii])
        if hs[ii] == "1" and ii == 4:
            # reverse the list
            result.reverse()
    return result
