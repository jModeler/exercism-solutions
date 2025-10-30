err = 0.0001

def square_root(number):
    guess = 0.5 * number

    while (abs(guess**2 - number) > err):
        guess = 0.5 * (guess + number/guess)
    
    return round(guess, 2)
