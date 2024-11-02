#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def isPal(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True

def palindromeIndex(s):
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - i - 1]:
            new_str = s[:i] + s[i+1:]
            # print(new_str)
            if isPal(new_str):
                return i
            new_str = s[: length-i-1] + s[length-i:]
            # print(new_str)
            if isPal(new_str):
                return length - i - 1
    return -1
    
print(palindromeIndex("aaab"))
print(palindromeIndex("baa"))
print(palindromeIndex("aaa"))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     q = int(input().strip())

#     for q_itr in range(q):
#         s = input()

#         result = palindromeIndex(s)

#         fptr.write(str(result) + '\n')

#     fptr.close()
