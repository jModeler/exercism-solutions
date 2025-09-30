def isEven(number):
    if number % 2 == 0:
        return True
    return False

def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    steps = 0
    while number != 1:
        steps += 1
        if isEven(number):
            number /= 2
        else:
            number = 3*number + 1
    return steps