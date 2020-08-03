#the input is an integer and the output is an integer
#if input is lesser than or equal to zero i want it maintained
#if input is greater than zero i want to negate it -(n)

#In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?

#make_negative(1);  # return -1
#make_negative(-5); # return -5
#make_negative(0);  # return 0

def make_negative(number):
    negative_number = 0
    if number<= negative_number:
        negative_number = number
    else:
        negative_number = -(number)
    return negative_number


print(make_negative(-5))


#intriguing solutions
def make_negative( number ):
    return -abs(number)

def make_negative( number ):
    return -number if number>0 else number

