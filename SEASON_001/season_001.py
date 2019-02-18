'''
Daily Coding Problem (18.02.2019)
Mike Nussbaumer

This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.

'''

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def getPairValues(a, b):
    return [a, b]
 
# Function for finding smallest number in a pair
def car(pairValue): 
    # get pair function
    pairValueFunction = pairValue

    # get pair values a, b
    pairValues = pairValueFunction(getPairValues)

    # find smaller number
    return pairValues[1] if pairValues[0] > pairValues[1] else pairValues[0] 

# Function for finding largest number in a pair
def cdr(pairValue): 
    # get pair function
    pairValueFunction = pairValue

    # get pair values a, b
    pairValues = pairValueFunction(getPairValues)

    # find smaller number
    return pairValues[0] if pairValues[0] > pairValues[1] else pairValues[1] 

print(car(cons(3, 4)))
print(cdr(cons(3, 4)))