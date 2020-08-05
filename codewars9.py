#Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates 
# and the paperwork has 'm' pages.

#Your task is to calculate how many blank pages do you need.

#example
#paperwork(5, 5) == 25

def paperwork(n, m):
    paperwork = n * m
    if n < 0 or m < 0:
         return 0
    else:
        return paperwork

print(paperwork(6,342))

#intriguing answers
def paperwork(n, m):
    return n * m if n > 0 and m > 0 else 0