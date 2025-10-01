def convert(number):
    result = ''
    if number % 3 == 0:
        result = ''.join([result, 'Pling'])
    if number % 5 == 0:
        result = ''.join([result, 'Plang'])
    if number % 7 == 0:
        result = ''.join([result, 'Plong'])
    if result == '':
        return str(number)
    return result
