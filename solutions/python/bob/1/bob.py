def response(hey_bob):
    if hey_bob.strip() == '':
        return "Fine. Be that way!"
    elif hey_bob.isupper():
        if hey_bob.rstrip()[-1] == "?":
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"
    elif hey_bob.rstrip()[-1] == "?":
        return "Sure."
    else:
        return "Whatever."