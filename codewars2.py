#input is a list, output is an integer
#Take the first number, compare with the second number and idenitfy the least number between them
#Take the least number identified and compare to the third number and identify the new least number.
#Continue this process until you exhaust the list.
#Return the least number when you are done.

numbers = []


small_number = 0
for smallest_number in numbers:
    if smallest_number < small_number:
        small_number = smallest_number
    


print(small_number)

