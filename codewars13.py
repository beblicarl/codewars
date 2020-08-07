#Your task is to write function findSum.

#Upto and including n, this function will return the sum of all multiples of 3 and 5.

#For example:

#findSum(5) should return 8 (3 + 5)

#findSum(10) should return 33 (3 + 5 + 6 + 9 + 10)



def find(n):
    new_list = list(range(1, n + 1))
    for x in new_list:
        return sum(set(list(range(3,n+1,3)) + list(range(5,n+1,5))))


print(find(5))


#intriguing examples
def find(n):
    return sum(e for e in range(1, n+1) if e % 3 == 0 or e % 5 == 0)


def find(n):
    sum = 0
    for i in range(1,n+1):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

def find(n):
    return sum(range(0, n+1, 3)) + sum(range(0, n+1, 5)) - sum(range(0, n+1, 15))

def find(n):
    return sum( set(range(0, n+1, 3)) | set(range(0, n+1, 5)) )

