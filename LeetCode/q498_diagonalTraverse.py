from typing import List
import collections

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ROWS, COLS = len(mat), len(mat[0])
        pieces = collections.defaultdict(list)

        for c in range(COLS):
            for r in range(ROWS):
                pieces[r + c].append(mat[r][c])
        
        ans = []
        for i in range(ROWS + COLS):
            if i % 2 == 0:
                ans += pieces[i]
            else:
                ans += pieces[i][::-1]
        return ans
        
sol = Solution()
mat = [[1,2,3],[4,5,6],[7,8,9]]
print("")
print(f"nums: {mat}")
print(f"[1,2,4,7,5,3,6,8,9] => {sol.findDiagonalOrder(mat)}")      

        

# 498. Diagonal Traverse

# Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

# Example 1:

# Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,4,7,5,3,6,8,9]
# Example 2:

# Input: mat = [[1,2],[3,4]]
# Output: [1,2,3,4]
 

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 104
# 1 <= m * n <= 104
# -105 <= mat[i][c] <= 105