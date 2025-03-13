class Solution:
    ## sends only 1 working solution
    
    #study
    def howSum(self, target, numbers):
        table = [None for _ in range(target + 1)]
        table[0] = []
        for t in range(target + 1):
            if table[t] != None:
                for n in numbers:
                    if t+n <= target:
                        table[t+n] = table[t] + [n] 
                        if t+n == target:
                            return table[target]
        return table[target]
        
        
sol = Solution()

print("howSum(7, [2,3]): True -> ", sol.howSum(7, [2,3]))
print("howSum(7, [2,4]): False -> ", sol.howSum(7, [2,4]))
print("howSum(7, [2,3,4,5]): True -> ", sol.howSum(7, [2,3,4,5]))
print("howSum(7, [1,5]): True -> ", sol.howSum(7, [1,5]))
print("howSum(300, [7,14]): False -> ", sol.howSum(300, [7,14]))
print("howSum(308, [7,14]): True -> ", sol.howSum(308, [7,14]))
