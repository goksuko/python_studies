from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        mnt = 0
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        q = deque()
        
        def rot(r, c, fresh) -> int:
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return fresh
            if grid[r][c] == 1:
                grid[r][c] = 2
                fresh -= 1
            return fresh
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1 # to learn the total number of fresh bananas
        # print(f"total fresh bananas: {fresh}")
        
        def find_rots(grid, ROWS, COLS, q) -> deque:
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 2:
                        q.append((r, c))
            return q
        
        for _ in range(ROWS * COLS):
            if fresh == 0:
                break
            find_rots(grid, ROWS, COLS, q)
            while q:
                r, c = q.pop()
                fresh = rot(r + 1, c, fresh)
                fresh = rot(r - 1, c, fresh)
                fresh = rot(r, c + 1, fresh)
                fresh = rot(r, c - 1, fresh)
                # print(f"[{r}, {c}]: fresh: {fresh}")
            mnt += 1
            # print(f"minutes: {mnt}")
            # print(f"grid: {grid}")
            
        if fresh == 0:
            return mnt
        else:
            return -1
                    
sol = Solution()
grid = [[1,1,0],[0,1,1],[0,1,2]]
print("")
print(f"grid: {grid}")
print(f"4 => {sol.orangesRotting(grid)}")   
grid = [[1,0,1],[0,2,0],[1,0,1]]
print("")
print(f"grid: {grid}")
print(f"-1 => {sol.orangesRotting(grid)}")    
grid=[[2,1,1],[1,1,0],[0,1,1]]
print("")
print(f"grid: {grid}")
print(f"4 => {sol.orangesRotting(grid)}")   

# Rotting Fruit
# You are given a 2-D matrix grid. Each cell can have one of three possible values:

# 0 representing an empty cell
# 1 representing a fresh fruit
# 2 representing a rotten fruit
# Every minute, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, then the fresh fruit also becomes rotten.

# Return the minimum number of minutes that must elapse until there are zero fresh fruits remaining. If this state is impossible within the grid, return -1.

# Example 1:



# Input: grid = [[1,1,0],[0,1,1],[0,1,2]]

# Output: 4
# Example 2:

# Input: grid = [[1,0,1],[0,2,0],[1,0,1]]

# Output: -1
# Constraints:

# 1 <= grid.length, grid[i].length <= 10


# Recommended Time & Space Complexity
# You should aim for a solution with O(m * n) time and O(m * n) space, where m is the number of rows and n is the number of columns in the given grid.


# Hint 1
# The DFS algorithm is not suitable for this problem because it explores nodes deeply rather than level by level. In this scenario, we need to determine which oranges rot at each second, which naturally fits a level-by-level traversal. Can you think of an algorithm designed for such a traversal?


# Hint 2
# We can use the Breadth First Search (BFS) algorithm. At each second, we rot the oranges that are adjacent to the rotten ones. So, we store the rotten oranges in a queue and process them in one go. The time at which a fresh orange gets rotten is the level at which it is visited. How would you implement it?


# Hint 3
# We traverse the grid and store the rotten oranges in a queue. We then run a BFS, processing the current level of rotten oranges and visiting the adjacent cells of each rotten orange. We only insert the adjacent cell into the queue if it contains a fresh orange. This process continues until the queue is empty. The level at which the BFS stops is the answer. However, we also need to check whether all oranges have rotted by traversing the grid. If any fresh orange is found, we return -1; otherwise, we return the level.