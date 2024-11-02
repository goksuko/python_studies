#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    length = len(arr)
    left_to_right = 0
    right_to_left = 0
    for n in range(length):
        left_to_right += arr[n][n]
    for n in range(length):
        right_to_left += arr[n][length - n - 1]
    diff = left_to_right - right_to_left
    return abs(diff)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # arr = []

    # for _ in range(n):
    #     arr.append(list(map(int, input().rstrip().split())))

    # result = diagonalDifference(arr)

    # fptr.write(str(result) + '\n')

    # fptr.close()
    
	arr = [[11, 2, 4],[4, 5, 6],[10, 8, -12]]
	print(diagonalDifference(arr))


# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

# For example, the square matrix  is shown below:

# 1 2 3
# 4 5 6
# 9 8 9  
# The left-to-right diagonal = . The right to left diagonal = . Their absolute difference is .

# Function description

# Complete the  function in the editor below.

# diagonalDifference takes the following parameter:

# int arr[n][m]: an array of integers
# Return

# int: the absolute diagonal difference
# Input Format

# The first line contains a single integer, , the number of rows and columns in the square matrix .
# Each of the next  lines describes a row, , and consists of  space-separated integers .

# Constraints

# Output Format

# Return the absolute difference between the sums of the matrix's two diagonals as a single integer.

# Sample Input

# 3
# 11 2 4
# 4 5 6
# 10 8 -12
# Sample Output

# 15
# Explanation

# The primary diagonal is:

# 11
#    5
#      -12
# Sum across the primary diagonal: 11 + 5 - 12 = 4

# The secondary diagonal is:

#      4
#    5
# 10
# Sum across the secondary diagonal: 4 + 5 + 10 = 19
# Difference: |4 - 19| = 15

# Note: |x| is the absolute value of x

# Language
# Python 3
# More
# 12345678910111213141516171819202122232425262728293031323334
# #
# # The function is expected to return an INTEGER.
# # The function accepts 2D_INTEGER_ARRAY arr as parameter.
# #

# def diagonalDifference(arr):
#     # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

# Line: 16 Col: 23

# Test against custom input
