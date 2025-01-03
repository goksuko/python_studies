from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # Traverse top row
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1

            # Traverse right column
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # Traverse bottom row (if valid)
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1

            # Traverse left column (if valid)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result
      
    
    def spiralOrder2(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
        ans = []
        ru = 0 # row up index
        rd = ROWS - 1 # row down
        cl = 0 # col left
        cr = COLS - 1 # col right
        while rd >= 0 and cr >= 0 and ru <= ROWS and cr <= COLS:
            for c in range(cl, cr + 1):
                if matrix[ru][c] != -105:
                    ans.append(matrix[ru][c])
                matrix[ru][c] = -105
            ru += 1
            for r in range(ru, rd + 1):
                if matrix[r][cr] != -105:
                    ans.append(matrix[r][cr])
                matrix[r][cr] = -105
            cr -= 1
            for c in range(cr, cl - 1, -1):
                if matrix[rd][c] != -105:
                    ans.append(matrix[rd][c])
                matrix[rd][c] = -105
            rd -= 1
            for r in range(rd, ru - 1, -1):
                if matrix[r][cl] != -105:
                    ans.append(matrix[r][cl]) 
                matrix[r][cl] = -105
            cl += 1
            # print(f"ru: {ru}, rd: {rd}, cl: {cl}, cr: {cr}")
        return ans
    
sol = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]   
print("")
print(f"matrix: {matrix}")
print(f"[1,2,3,6,9,8,7,4,5] => \n{sol.spiralOrder(matrix)}")    
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]  
print("")
print(f"matrix: {matrix}")
print(f"[1,2,3,4,8,12,11,10,9,5,6,7] => \n{sol.spiralOrder(matrix)}")       
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,15,16]]  
print("")
print(f"matrix: {matrix}")
print(f"[.......] => \n{sol.spiralOrder(matrix)}")           

# 54. Spiral Matrix
# Medium

# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:

# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100