class Solution:
    def canSum(self, target, numbers) ->bool: #time  O(m*n) space O(m)
        table = [False] * (target + 1)
        table[0] = True
        for t in range(target + 1):
            if table[t] ==  True:
                for n in numbers:
                    if t+n <= target:
                        table[(t+n)] = True
                        if t+n == target:
                            return True
        return table[target]
        


    
sol = Solution()
print("canSum(7, [2,3]): True -> ", sol.canSum(7, [2,3]))
print("canSum(7, [2,4]): False -> ", sol.canSum(7, [2,4]))
print("canSum(7, [2,3,4,5]): True -> ", sol.canSum(7, [2,3,4,5]))
print("canSum(7, [1,5]): True -> ", sol.canSum(7, [1,5]))
print("canSum(300, [7,14]): False -> ", sol.canSum(300, [7,14]))
