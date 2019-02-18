# Daily Coding Problems

🚀 Solutions for the https://www.dailycodingproblem.com/ problems given each day.

# Seasons 🔱

## [Season 1](./SEASON_000)

Date: 14/02/2019

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

* [sum-of-array](./SEASON_000/sum-of-array.py)

## [Season 2](./SEASON_001)

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
