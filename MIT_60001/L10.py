# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 11:27:54 2016

@author: ericgrimson
"""
##### HOW TO EVALUATE EFFICIENCY OF PROGRAMS 
# 1. measure with a timer 
# 2. count the operations 
# 3. abstract notion of order of growth 

##### 1. MEASURE WITH A TIMER

import time

def c_to_f(c):
    return c*9/5 + 32

t0 = time.clock()
c_to_f(100000)
t1 = time.clock()
print("Time: ", t1 - t0, "seconds")

# + running time varies between algorithms 
# - running time varies between implementations
# - running time varies between computers 
# - running time is not predictable based on small inputs 
# - time varies for different inputs but cannot really express a relationship between inputs and time 

##### 2. COUNT THE OPERATIONS

def c_to_f2(c):
    return c*9/5 + 32 # 3 operations

def mysum(x):
    total = 0 # 1 operation => doing an assignment
    for i in range(x+1): # 1 operation => to set i to a value from that iterator
        total += i # 2 operations => first: to get the value of i and total, add them together
        # second: to assign the result to total
    return total # 1 operation => to return the value of total
# 1 + 3x + 1 operations

# implementation changed from FOR to WHILE

def mysum2(x):
    total = 0 # 1 operation => doing an assignment
    i = 0 # 1 operation
    while i < x + 1: # 1 operation => test the value of i
        total += i # 2 operations => first: to get the value of i and total, add them together
        # second: to assign the result to total
        i += 1 # 1 operation => set the value of i
    return total # 1 operation
# 1 + 4x + 1 operations

# + count depends on algorithm 
# - count depends on implementations 
# + count independent of computers 
# - no clear definition of which operations to count
# + count varies for different inputs and can come up with a relationship between inputs and the count

##### 3. ABSTRACT NOTION OF ORDER OF GROWTH

# List L
def search_for_elem(L, e):
    for i in L:
        if i == e:
            return True
    return False

def fact_iter(n):
    '''assumes n an int >= 0'''
    answer = 1 # 1 operation
    while n > 1: # 1 operation => test the value of n
        answer *= n #2 operations => first: to get the value of n and answer, multiply them together
        # second: to assign the result to answer
        n -= 1 # 2 operations => first: to get the value of n, subtract 1 from it
        # second: to assign the result to n
    return answer # 1 operation
# 1 + 5n + 1 operations

# what is asymptotic complexity?
# ignore additive constants
# ignore multiplicative constants
# focus on dominant terms


def linear_search(L, e):
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
    return found

# must look through all elements to decide it’s not there 
# O(len(L)) for the loop * O(1) to test if e == L[i] 
# O(1 + 4n + 1) = O(4n + 2) = O(n) 
# overall complexity is O(n) – where n is len(L) 

testList = [1, 3, 4, 5, 9, 18, 27]

def addDigits(s):
    val = 0
    for c in s:
        val += int(c)
    return val

# O(len(s)) 

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

# must only look until reach a number greater than e 
# O(len(L)) for the loop * O(1) to test if e == L[i] 
# overall complexity is O(n) – where n is len(L)

def isSubset(L1, L2):
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True

# outer loop executed len(L1) times 
# each iteration will execute inner loop up to len(L2) times, with constant number of operations 
# O(len(L1)*len(L2)) 

# worst case when L1 and L2 same length, none of elements of L1 in L2 
# O(len(L1)2) 

testSet = [1, 2, 3, 4, 5]
testSet1 = [1, 5, 3]
testSet2 = [1, 6]

def intersect(L1, L2):
    tmp = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                tmp.append(e1)
    res = []
    for e in tmp:
        if not(e in res):
            res.append(e)
    return res

# first nested loop takes len(L1)*len(L2) steps 
# second loop takes at most len(L1) steps 
# determining if element in list might take len(L1) steps 
# if we assume lists are of roughly same length, then 
# O(len(L1)^2)