from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS * COLS - 1
        while l <= r:
            m = l + (r - l) // 2
            row, col = m // COLS, m % COLS
            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True
        return False
                 
#time exceeded
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) # rows
        n = len(matrix[0]) # columns
        # print(f"m: {m}, n: {n}")
        total = m*n
        l = 0
        r = total - 1
        while l <= r:
            t = l + (r - l) // 2
            # print(f"t: {t}, [t // n]: {t // n}, [t % n]: {t % n}, matrix[t // n][t % n]: {matrix[t // n][t % n]}")
            if matrix[t // n][t % n] == target:
                return True
            elif matrix[t // n][t % n] < target:
                l = t + 1
            elif matrix[t // n][t % n] > target:
                r = t - 1
            # print(f"l: {l}, r: {r}")
        return False
    

        
        
sol = Solution()
matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
# m:3 n:4
# [1 ,2 ,4 ,8 ]
# [10,11,12,13]
# [14,20,30,40]
target = 1
print(f"\nmatrix: {matrix}, target: {target}")
print(f"true => {sol.searchMatrix(matrix, target)}")   
matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
# m:3 n:4
# [1 ,2 ,4 ,8 ]
# [10,11,12,13]
# [14,20,30,40]
target = 10
print(f"\nmatrix: {matrix}, target: {target}")
print(f"true => {sol.searchMatrix(matrix, target)}")   
matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target = 15
print(f"\nmatrix: {matrix}, target: {target}")
print(f"false => {sol.searchMatrix(matrix, target)}")   
matrix=[[1]]
target=1
print(f"\nmatrix: {matrix}, target: {target}")
print(f"true => {sol.searchMatrix(matrix, target)}") 

# Search a 2D Matrix
# You are given an m x n 2-D integer array matrix and an integer target.

# Each row in matrix is sorted in non-decreasing order.
# The first integer of every row is greater than the last integer of the previous row.
# Return true if target exists within matrix or false otherwise.

# Can you write a solution that runs in O(log(m * n)) time?

# Example 1:



# Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10

# Output: true
# Example 2:



# Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15

# Output: false
# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -10000 <= matrix[i][j], target <= 10000


# Recommended Time & Space Complexity
# You should aim for a solution with O(log(m * n)) time and O(1) space, where m is the number of rows and n is the number of columns in the matrix.


# Hint 1
# A brute force solution would be to do a linear search on the matrix. This would be an O(m * n) solution. Can you think of a better way? Maybe an efficient searching algorithm, as the given matrix is sorted.


# Hint 2
# We can use binary search, which is particularly effective when we visualize a row as a range of numbers, [x, y] where x is the first cell and y is the last cell of a row. Using this representation, it becomes straightforward to check if the target value falls within the range. How can you use binary search to solve the problem?


# Hint 3
# We perform a binary search on the rows to identify the row in which the target value might fall. This operation takes O(logm) time, where m is the number of rows. Now, when we find the potential row, can you find the best way to search the target in that row? The sorted nature of each row is the hint.


# Hint 4
# Once we identify the potential row where the target might exist, we can perform a binary search on that row which acts as a one dimensional array. It takes O(logn) time, where n is the number of columns in the row.

