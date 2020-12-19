def on_square(integer_number):
    valueRange(integer_number)
    return pow(2,integer_number-1)

def total_after(integer_number):
    valueRange(integer_number)
    return sum([pow(2,i) for i in range(integer_number)])

def valueRange(integer_number):
    if type(integer_number)!=int or integer_number <= 0 or integer_number > 64:
        raise ValueError