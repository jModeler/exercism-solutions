def distance_from_center(x, y):
    return (x**2 + y**2)**0.5

def score(x, y):
    distance = distance_from_center(x, y)
    if 5 < distance <= 10:
        return 1
    elif 1 < distance <= 5:
        return 5
    elif distance <= 1:
        return 10
    else:
        return 0
