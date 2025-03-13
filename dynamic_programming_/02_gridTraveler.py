#how many ways to travel from left up of a grid to rgiht below

class Solution:
    #study
    def grid(self, r, c, dic)-> int:
        if r == 0 or c == 0:
            return 0
        if r == 1 or c == 1:
            return 1
        if ((r,c) or (c,r)) in dic.keys():
            return dic[(r,c)]
        dic[(r,c)] = self.grid(r-1,c,dic) + self.grid(r, c-1,dic)
        return dic[(r,c)]
    
    #2d dynamic
    def grid3(self, r, c, dic)-> int: # time O(m*n) space O(n+m)
        if r == 0 or c == 0:
            return 0
        if r == 1 or c == 1:
            return 1
        if ((r,c) or (c,r)) in dic.keys():
            return dic[(r,c)]
        dic[(r,c)] = self.grid(r -1, c, dic) + self.grid(r, c-1, dic)
        return dic[(r,c)]
    
    # recursive
    def grid2(self, r, c)-> int: # time O(2^n+m) space O(n+m)
        if r == 0 or c == 0:
            return 0
        if r == 1 or c == 1:
            return 1
        return self.grid2(r -1, c, dic) + self.grid2(r, c-1, dic)

        
        
        
sol = Solution()
dic = {}
print("grid(0,1): 0 -> ", sol.grid(0,1,dic))
print("grid(1,0): 0 -> ", sol.grid(1,0,dic))
print("grid(8,0): 0 -> ", sol.grid(8,0,dic))
print("grid(0,0): 0 -> ", sol.grid(0,0,dic))
print("grid(1,1): 1 -> ", sol.grid(1,1,dic))
print("grid(2,3): 3 -> ", sol.grid(2,3,dic))
print("grid(3,3): 6 -> ", sol.grid(3,3,dic))
print("grid(18,18): 2333606220 -> ", sol.grid(18,18,dic))

