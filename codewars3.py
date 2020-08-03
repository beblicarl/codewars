

#We need a function that can transform a string into a number. What ways of achieving this do you know?

#Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of an integral number.

#examples
#stringToNumber("1234") == 1234
#stringToNumber("605" ) == 605
#stringToNumber("1405") == 1405
#stringToNumber("-7"  ) == -7


def string_to_number(s):
    return int(s)

print(string_to_number("603"))


#intriguing examples

def string_to_number(s):
    return float(str(float(str(int(s))))

string_to_number = eval

def string_to_number(s):
    result = 0    #Variable to hold running total of integer to return
    place = 1    #Decimal value of place currently being calculated
    i = len(s) - 1
    while i >= 0:
        digit = s[i]    #The piece of the string being transferred
        if digit == '1':
            result += place
        elif digit == '2':
            result += (2*place)
        elif digit == '3':
            result += (3*place)
        elif digit == '4':
            result += (4*place)
        elif digit == '5':
            result += (5*place)
        elif digit == '6':
            result += (6*place)
        elif digit == '7':
            result += (7*place)
        elif digit == '8':
            result += (8*place)
        elif digit == '9':
            result += (9*place)
        elif digit == '-':
            result = -result
        place *= 10
        i -= 1
        
    return result