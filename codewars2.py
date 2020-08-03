#Given an array of integers your solution should find the smallest integer.

#For example:

    #Given [34, 15, 88, 2] your solution will return 2
    #Given [34, -345, -1, 100] your solution will return -345

#You can assume, for the purpose of this kata, that the supplied array will not be empty.






#input is a list, output is an integer
#Take the first number, compare with the second number and idenitfy the least number between them
#Take the least number identified and compare to the third number and identify the new least number.
#Continue this process until you exhaust the list.
#Return the least number when you are done.



def find_smallest_int(arr):
  small_number = arr[0]
  for smallest_number in arr:
      if smallest_number < small_number:
          small_number = smallest_number
  return small_number

print(find_smallest_int([0, 1-2**64, 2**64]))

