
class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        ROWS, COLS = len(mat), len(mat[0])
        if (r*c)!=(ROWS*COLS):
            return mat
        ans = [[0] * c for _ in range(r)]
        for i in range(ROWS*COLS):
            ans[i//c][i%c] = mat[i//COLS][i%COLS]
        return ans
    
    
    def matrixReshape(self, mat, r, c): #beats %29
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        ROWS, COLS = len(mat), len(mat[0])
        ans = []
        if not r or not c:
            return ans
        if ROWS * COLS != r * c:
            return mat
        for row in range(ROWS):
            for col in range(COLS):
                ans.append(mat[row][col])
        # print(ans)
        res = []
        k = 0
        for i in range(c):
            temp = []
            for j in range(r):
                if k == len(ans):
                    break                
                temp.append(ans[k])
                k += 1
            # print(temp)
            res.append(temp)
            if k == len(ans):
                break          
        return res

sol = Solution()
print(sol.matrixReshape(mat = [[1,2],[3,4]], r = 2, c = 4))


# 566. Reshape the Matrix
# Easy

# In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

# You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

# The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

# If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

 
# Example 1:

# Input: mat = [[1,2],[3,4]], r = 1, c = 4
# Output: [[1,2,3,4]]
# Example 2:

# Input: mat = [[1,2],[3,4]], r = 2, c = 4
# Output: [[1,2],[3,4]]
 
# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# -1000 <= mat[i][j] <= 1000
# 1 <= r, c <= 300