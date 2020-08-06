#Get the number n (n>0) to return the reversed sequence from n to 1.

#Example : n=5 >> [5,4,3,2,1]

def reverse_seq(n):
    return[numbers for numbers in reversed(list(range(1, n + 1)))]



#intriguing examples
def reverse_seq(n):
    return list(range(n, 0, -1))

    the numbers start at n stops at 0 and -1 is subtracted from the starting number until it gets to the stop. The stop is not included though.
