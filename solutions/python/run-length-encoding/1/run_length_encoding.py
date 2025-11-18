def decode(string):
    repeat = ""
    decoded = ""
    for s in string:
        if s.isdigit():
            repeat = "".join([repeat, s])
        else:
            if repeat.isdigit():
                to_add = s * int(repeat)
            else:
                to_add = s
            decoded = "".join([decoded, to_add])
            repeat = ""
    return decoded

def encode(string):
    repeat = 1
    encoded = ""
    for ii in range(len(string)):
        if ii+1 != len(string):
            if string[ii] == string[ii+1]:
                repeat += 1
            else:
                if repeat != 1:
                    to_add = "".join([str(repeat),string[ii]])
                else:
                    to_add = string[ii]
                encoded = "".join([encoded, to_add])
                repeat = 1
        else:
            if repeat != 1:
                to_add = "".join([str(repeat),string[ii]])
            else:
                to_add = string[ii]
            encoded = "".join([encoded, to_add])
            repeat = 1
    return encoded