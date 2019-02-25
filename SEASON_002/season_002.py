'''
Daily Coding Problem (25.02.2019)
Mike Nussbaumer

This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways 
you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, 
if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

'''

import math
import sys

sys.setrecursionlimit(1000000)

# Function for finding numbre of ways to climb stair with 1,2 steps at a time
def findUniqueClimb(n):
    if(n == 0 | n == 1):
        return 1
    elif(n == 2):
        return 2
    else:
        return findUniqueClimb(n - 2) + findUniqueClimb(n - 1)

# Function for finding numbre of ways to climb stair with custom steps
def findUniqueClimbWithCustomSteps(n, x):
    x = sorted(x, reverse=True)
    climb = 0

    for currentWay in x:
        climb+= findUniqueClimb(n - currentWay)

    if(n == 0 | n == 1):
        return 1
    elif n == 2:
        return 2
    else:
        return climb

# Tests

print(str(findUniqueClimb(4)))
print(str(findUniqueClimbWithCustomSteps(4, {1, 3, 2})))