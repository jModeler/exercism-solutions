def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return not year % 400
        return True
    else:
        return False
