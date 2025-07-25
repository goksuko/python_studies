from typing import List
from collections import Counter

class Solution(object):
    # fast solution
    def equalPairs(self, grid):
        from collections import Counter
        row_count = Counter(tuple(row) for row in grid)
        ans = 0

        # For each column, form a tuple and count matches in rows
        for col in zip(*grid):
            ans += row_count[col]

        return ans
    
    # my solution
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        d = [[] for x in grid]
        for i in range(len(grid)):
            for j in range(len(grid)):
                d[j].append(grid[i][j])
        temp = 0
        for line in grid:
            if line in d:
                temp  += 1
        ans = 0
        for line_d in d:
            for line_g in grid:
                if line_d == line_g:   
                    ans += 1
        return ans




sol = Solution()
grid = [[3,2,1],[1,7,6],[2,7,7]]
print(f"1: {sol.equalPairs(grid)}")
grid = [[3,1,2,2],[1,4,4,4],[2,4,2,2],[2,5,2,2]]
print(f"3: {sol.equalPairs(grid)}")
grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
print(f"3: {sol.equalPairs(grid)}")
grid = [[13,13],[13,13]]
print(f"4: {sol.equalPairs(grid)}")



# 2352. Equal Row and Column Pairs
# Medium

# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

# A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).



# Example 1:


# Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
# Output: 1
# Explanation: There is 1 equal row and column pair:
# - (Row 2, Column 1): [2,7,7]
# Example 2:


# Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
# Output: 3
# Explanation: There are 3 equal row and column pairs:
# - (Row 0, Column 0): [3,1,2,2]
# - (Row 2, Column 2): [2,4,2,2]
# - (Row 3, Column 2): [2,4,2,2]


# Constraints:

# n == grid.length == grid[i].length
# 1 <= n <= 200
# 1 <= grid[i][j] <= 105