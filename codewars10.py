#Can you find the needle in the haystack?

#Write a function findNeedle() that takes an array full of junk but containing one "needle"

#After your function finds the needle it should return a message (as a string) that says:

#"found the needle at position " plus the index it found the needle, so: 



def find_needle(haystack):
    name = 'needle'
    index = haystack.index(name)
    call = 'found the needle at position '
    new_list = call + str(index)
    return new_list

print(find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk']))

#intriguing examples

def find_needle(haystack): return 'found the needle at position %d' % haystack.index('needle')

def find_needle(haystack):
    return 'found the needle at position {}'.format(haystack.index('needle'))

def find_needle(haystack):
    for i, x in enumerate(haystack):
        if x == 'needle': 
            return 'found the needle at position %d' % i