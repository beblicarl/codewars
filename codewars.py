# Input is a string , output is a boolean
# I will check the length of the string
# If the length of the string is neither 4 or 6 return False
# If the length is True then check the digits of the code
# If the codes are numerical return True
# If the codes are not numerical return False


def validate_pin(pin_code):
    if (len(pin_code) == 4 || len(pin_code) == 6)  #if the content is exactly 4 or 6 it is valid
        continue
        if pin_codes.isalpha() == True  #this is to check if string contains only alphabets
            return
        else:
            continue
        if pin_code.isnumeric() == True #this is to check if it contains only numbers
            continue
        else:
            return
        if pin_code.isanum() == True #this is to check if there are alphanumeric numbers present
            return
        else:
            continue

    return validate_pin(pin_codes)

