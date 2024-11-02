#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def truckTour(petrolpumps):
    length = len(petrolpumps)
    for x in range(length):
        sum_road = 0
        for i in range(length):
            ind = (x+i) % length
            sum_road += petrolpumps[ind][0] - petrolpumps[ind][1]
            if sum_road < 0:
                break
            if i == length - 1:
                return x
    return None
            

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     petrolpumps = []

#     for _ in range(n):
#         petrolpumps.append(list(map(int, input().rstrip().split())))

#     result = truckTour(petrolpumps)

#     fptr.write(str(result) + '\n')

#     fptr.close()

petrolpumps = [[1, 5], [10, 3], [3, 4]]
print(truckTour(petrolpumps))