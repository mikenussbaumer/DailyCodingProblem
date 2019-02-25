# Daily Coding Problems

🚀 Solutions for the https://www.dailycodingproblem.com/ problems given each day.

# Seasons 🔱

## [Season 0](./SEASON_000)

Date: 14/02/2019

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

* [season_001](./SEASON_000/sum-of-array.py)

## [Season 1](./SEASON_001)

Date: 18/02/2019

This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.

* [season_001](./SEASON_001/season_001.py)

## [Season 2](./SEASON_002)

Date: 25/02/2019

This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

* [season_002](./SEASON_002/season_002.py)
