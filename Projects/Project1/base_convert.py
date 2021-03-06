def convert(x, y):
    x = convert_helper(x, y)
    if len(x) > 1 and x[0] == '0':
        return x[1:]
    else:
        return x

    
def convert_helper(num, b):
    """Recursive function that returns a string representing num in the base b"""
    # base symbols
    if num - ((num // b ) * b) == 10:
        return convert_1(num // b, b) + 'A'
    elif num - ((num // b ) * b) == 11:
        return convert_1(num // b, b) + 'B'
    elif num - ((num // b ) * b) == 12:
        return convert_1(num // b, b) + 'C'
    elif num - ((num // b ) * b) == 13:
        return convert_1(num // b, b) + 'D'
    elif num - ((num // b ) * b) == 14:
        return convert_1(num // b, b) + 'E'
    elif num - ((num // b ) * b) == 15:
        return convert_1(num // b, b) + 'F'
    elif num // b == 0 and num != 0:
        return str(num)
    # We have a problem here. The only way we tell our function we're done is if num == 0. In that case we DO NOT
    # want to concatenate anything more onto what we return so we originally returned "". But in the case where we start
    # with a zero, we will return None! So we need to make a distinction of when num == 0, this was num's original starting
    # value or we had > 1 recursive calls to get here. It turns out making that distinction requires us to use a flag.
    # Thus we will wrongly always add a zero to the start of the string if num == 0. We fix this in the function below.
    elif num == 0:
        return str(num)
        # need ' + str(num - ((num // b) * b))' to "get concatenation going"
    return convert_1(num // b, b) + str(num - ((num // b) * b))

#print(convert(1029, 2))
