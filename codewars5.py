#question

#You get an array of numbers, return the sum of all of the positives ones.

#Example [1,-4,7,12] => 1 + 7 + 12 = 20

#Note: if there is nothing to sum, the sum is default to 0

#Test.describe("positive_sum")

#Test.it("works for some examples")
#Test.assert_equals(positive_sum([1,2,3,4,5]),15)
#Test.assert_equals(positive_sum([1,-2,3,4,5]),13)
#Test.assert_equals(positive_sum([-1,2,3,4,-5]),9)

def positive_sum(arr):
    sum = 0
    for n in arr:
        if n > 0:
            sum += n    
            
    return sum
    
    
print(positive_sum([-1,2,3,4,-5]))


#intriguing examples

def positive_sum(arr):
    return sum(x for x in arr if x > 0)


def positive_sum(arr):
    sum = 0
    for e in arr:
        if e > 0:
            sum = sum + e
    return sum

def positive_sum(arr):
    return sum(i for i in arr if i > 0)