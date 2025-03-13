class Solution:
    def grid(self, r,c) -> int: # time O(m*n) space O(m*n)
        if r == 0 or c == 0:
            return 0
        if r == 1 or c == 1:
            return 1
        table = [[0]*(c+1) for _ in range(r+1)]
        table[1][1] = 1
        for row in range(r+1):
            for col in range(c+1):
                current = table[row][col]
                if col + 1 <= c:
                    table[row][col+1] += current
                if row + 1 <= r:
                    table[row+1][col] += current
        return table[r][c]
        
 
        
sol = Solution()
print("grid(0,1): 0 -> ", sol.grid(0,1))
print("grid(1,0): 0 -> ", sol.grid(1,0))
print("grid(8,0): 0 -> ", sol.grid(8,0))
print("grid(0,0): 0 -> ", sol.grid(0,0))
print("grid(1,1): 1 -> ", sol.grid(1,1))
print("grid(2,3): 3 -> ", sol.grid(2,3))
print("grid(3,3): 6 -> ", sol.grid(3,3))
print("grid(18,18): 2333606220 -> ", sol.grid(18,18))