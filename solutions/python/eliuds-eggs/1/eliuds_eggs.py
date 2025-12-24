def convert_to_binary(display_value):
    result = []
    a = display_value
    while a not in [0,1]:
        result.append(a%2)
        a = a//2
    result.append(a)
    # reverse the order
    result = result[::-1]
    return result

def egg_count(display_value):
    binary = convert_to_binary(display_value)
    return sum(binary)
