def flatten(iterable):
    result = []
    for value in iterable:
        if isinstance(value, list):
            result.extend(flatten(value))
        else:
            if value is not None:
                result.append(value)
    return result
    
