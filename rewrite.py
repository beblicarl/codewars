# Input is a string , output is a boolean
# I will check the length of the string
# If the length of the string is neither 4 or 6 return False
# If the length is True check if the characters are numerical
# If the characters are numerical return True
# If the characters are not numerical return False


def validate_pin(pin_code):
    pin_length = len(pin_code) 
    if pin_length != 4 and pin_length != 6:
        return False
    elif pin_code.isnumeric(): 
        return True
    else:
        return False 

print(validate_pin('0012'))

#other solutions on codewars
def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()