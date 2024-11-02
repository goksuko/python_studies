#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    n = len(matrix) // 2
    sum_max = 0
    
    for i in range(n):
        for j in range(n):
            sum_max += max(matrix[i][j], matrix[2*n-i-1][2*n-j-1], matrix[i][2*n-j-1], matrix[2*n-i-1][j])
    
    return sum_max

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     q = int(input().strip())

#     for q_itr in range(q):
#         n = int(input().strip())

#         matrix = []

#         for _ in range(2 * n):
#             matrix.append(list(map(int, input().rstrip().split())))

#         result = flippingMatrix(matrix)

#         fptr.write(str(result) + '\n')

#     fptr.close()
    

matrix = [[112,42,83,119], [56, 125, 56, 49],[15, 78, 101, 43],[62, 98, 114, 108]]
print(flippingMatrix(matrix))