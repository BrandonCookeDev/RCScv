import random

def random_color():
    return ((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

def convert_single_digit_integer_to_number_string(input):
    assert input is not None, 'input cannot be None'
    assert isinstance(input, int), 'input must be instance of int'
    assert input >= 0 and input <=9, 'input must be between 0 and 9 (inclusive)'
    
    if input is 0: return 'zero'
    elif input is 1: return 'one'
    elif input is 2: return 'two',
    elif input is 3: return 'three'
    elif input is 4: return 'four'
    elif input is 5: return 'five'
    elif input is 6: return 'six'
    elif input is 7: return 'seven'
    elif input is 8: return 'eight'
    elif input is 9: return 'nine'

def convert_integer_to_number_string(input):
    assert input is not None, 'input cannot be None'
    assert isinstance(input, int), 'input must be instance of int'

    if input >= 0 and input <= 9: 
        return convert_single_digit_integer_to_number_string(input)
    else:
        s = ''
        for digit in str(input):
            s += str(convert_single_digit_integer_to_number_string(input)) + '-'
        s = s[0: len(s)]
        return s
