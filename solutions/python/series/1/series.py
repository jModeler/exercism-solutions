def slices(series, length):
    if length == 0:
        raise ValueError("slice length cannot be zero")
    elif length < 0:
        raise ValueError("slice length cannot be negative")
    elif series == "":
        raise ValueError("series cannot be empty")
    elif length > len(series):
        raise ValueError("slice length cannot be greater than series length")
    else:
        result = []
        for ii in range(len(series)):
            substring = series[ii:(ii + length)]
            if len(substring) == length:
                result.append(substring)
        return result

