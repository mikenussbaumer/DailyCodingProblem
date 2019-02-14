'''
Daily Coding Problem (14.02.2019)
Mike Nussbaumer

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''

def partition(array, begin, end):
    pivot_idx = begin
    for i in xrange(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot_idx += 1
            array[i], array[pivot_idx] = array[pivot_idx], array[i]
    array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
    return pivot_idx

def quick_sort_recursion(array, begin, end):
    if begin >= end:
        return
    pivot_idx = partition(array, begin, end)
    quick_sort_recursion(array, begin, pivot_idx-1)
    quick_sort_recursion(array, pivot_idx+1, end)

def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    
    return quick_sort_recursion(array, begin, end)

def hasArraySum(array, sum):
    quick_sort(array)

    a = 0
    b = len(array) - 1

    while a<b: 
        if (array[a] + array[b] == sum): 
            print("Found sum " + str(sum) + "(" + str(array[a]) + " + " + str(array[b]) + ")")
            return 1
        elif (array[a] + array[b] < sum): 
            a += 1
        else: 
            b -= 1
    print("No sum was found!")
    return 0

def testFile(fileName, sum):
    array = open(fileName).read().split('\n')
    array = list(map(int, array))

    hasArraySum(array, sum)

testFile('test.txt', 9427983 + 343104)
testFile('test.txt', 242759 + 33412)

