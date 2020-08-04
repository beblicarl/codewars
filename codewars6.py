#Question
#Your task is to make two functions, max and min (maximum and minimum in PHP and Python) that take a(n) 
# array/vector of integers list as input and outputs, respectively, the largest and lowest number in that array/vector.

#Examples
#maximun([4,6,2,1,9,63,-134,566]) returns 566
#minimun([-52, 56, 30, 29, -54, 0, -110]) returns -110
#maximun([5]) returns 5
#minimun([42, 54, 65, 87, 0]) returns 0

def minimum(arr):
    return min(arr)

def minimal(arr):
    number = arr[0]
    for n in arr:
        if n < number:
            number = n
    return number


print(minimal([-1, -2, -3, -4, -5, -10])


def maximum(arr):
    return max(arr)

def max(arr):
    digit = arr[0]
    for n in arr:
        if n >  digit:
            digit = n
    return digit





#intriguing examples

def min(arr):
    return sorted(arr)[0]

def max(arr):
    return sorted(arr)[-1]