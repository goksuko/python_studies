class Solution:

    def bestSum(self, target, numbers) ->list:
        table = [None for _ in range(target + 1)]
        table[0] = []
        for t in range(target + 1):
            if table[t] != None:
                for n in numbers:
                    if t+n <= target:
                        comb = table[t] + [n]
                        if table[t+n] == None or len(comb) < len(table[t+n]):
                            table[t+n] = comb
        return table[target]        
        
# below does not work!!!        
    def bestSum2(self, target, numbers) ->list:
        table = [None for _ in range(target + 1)]
        table[0] = []
        shortest = None
        for t in range(target + 1):
            if table[t] != None:
                for n in numbers:
                    if t+n <= target:
                        table[t+n] = table[t] + [n]
                        if shortest == None or len(shortest) > len(table[t+n]):
                            shortest = table[t+n]
        return table[target]        
        
   
        
sol = Solution()


print("bestSum(7, [2,3]): True -> ", sol.bestSum(7, [2,3]))
print("bestSum(7, [2,4]): False -> ", sol.bestSum(7, [2,4]))
print("bestSum(7, [2,3,4,5]): True -> ", sol.bestSum(7, [2,3,4,5]))
print("bestSum(8, [1,4,5]): True -> ", sol.bestSum(8, [1,4,5]))
print("bestSum(7, [2,3,4,5,7]): True -> ", sol.bestSum(7, [2,3,4,5,7]))
print("bestSum(7, [1,5]): True -> ", sol.bestSum(7, [1,5]))
print("bestSum(300, [7,14]): False -> ", sol.bestSum(300, [7,14]))
print("bestSum(308, [7,14]): True -> ", sol.bestSum(308, [7,14]))
print("bestSum(100, [1,2,5,25]): True -> ", sol.bestSum(100, [1,2,5,25]))


# print("bestSum(7, [2,3]): True -> ", sol.bestSum(7, [2,3],{}))
# print("bestSum(7, [2,4]): False -> ", sol.bestSum(7, [2,4],{}))
# print("bestSum(7, [2,3,4,5]): True -> ", sol.bestSum(7, [2,3,4,5],{}))
# print("bestSum(7, [1,5]): True -> ", sol.bestSum(7, [1,5],{}))
# print("bestSum(300, [7,14]): False -> ", sol.bestSum(300, [7,14],{}))
# print("howSum(308, [7,14]): True -> ", sol.bestSum(308, [7,14],{}))
