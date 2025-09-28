def check_legit_triangle(sides):
    a, b, c = sides 
    if 0 in sides:
        return False 
    elif a + b < c or a + c < b or b + c < a:
        return False 
    else:
        return True

def equilateral(sides):
    # check if the triangle is not degenerate
    legit = check_legit_triangle(sides)

    if legit:
        # unwrap
        a, b, c = sides
        return a == b == c

    return False


def isosceles(sides):
    # check if the triangle is not degenerate
    legit = check_legit_triangle(sides)

    if legit:
        # unwrap
        a, b, c = sides 
        return a == b or b == c or c == a

    return False

def scalene(sides):
    # check if the triangle is not degenerate
    legit = check_legit_triangle(sides)

    if legit:
        # unwrap
        a, b, c = sides 
        return a != b and a != c and b != c
    
    return False
