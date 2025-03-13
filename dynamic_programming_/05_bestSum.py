class Solution:
    ## sends only the shortest working solution
    #study
    def bestSum8(self, target, numbers, dic) ->bool:
        if target in dic.keys():
            return dic[target]
        if target == 0:
            return []
        if target < 0:
            return None
        shortest = None
        for n in numbers:
            res = self.bestSum(target - n, numbers, dic)
            if res != None:
                res.append(n)
                if shortest == None or len(res) < len(shortest):
                    shortest = res
                dic[target] = res
        dic[target] = shortest
        return shortest
    
    
    
    #dynamic
    def bestSum3(self, target, numbers, dic) ->bool: 
        if target in dic.keys():
            return dic[target]
        if target == 0:
            return []
        shortest = None
        if target < min(numbers):
            return None
        for n in numbers:
            res = self.bestSum(target - n, numbers, dic)
            if res != None:
                res.append(n)
                if shortest == None or len(res) < len(shortest):
                    shortest = res
                dic[target] = res
        dic[target] = shortest
        return shortest   
    
    #recursive from freecodecamp
    def bestSum2(self, target, numbers) ->list: # time O(n^target) space O(target^2)
        if target == 0:
            return []
        if target < min(numbers):
            return None
        shortest = None
        for n in numbers:
            res = self.bestSum(target - n, numbers)
            if res != None:
                res.append(n)
                if shortest == None or len(res) < len(shortest):
                    shortest = res
        return shortest   
      
    
    #recursive worked but better above
    def bestSum2(self, target, nums) ->list: 
        nums.sort()
        # print(nums)
        numbers = nums[::-1]
        # print(numbers)
        
        def rec(target, numbers):
            if target == 0:
                return []
            if target < min(numbers):
                return None
            for n in numbers:
                res = self.bestSum(target - n, numbers)
                if res != None:
                    res.append(n)
                    return res
            return None
        
        return rec(target, numbers)

        
        
        
sol = Solution()

# print("bestSum(7, [2,3]): True -> ", sol.bestSum(7, [2,3]))
# print("bestSum(7, [2,4]): False -> ", sol.bestSum(7, [2,4]))
# print("bestSum(7, [2,3,4,5]): True -> ", sol.bestSum(7, [2,3,4,5]))
# print("bestSum(8, [1,4,5]): True -> ", sol.bestSum(8, [1,4,5]))
# print("bestSum(7, [2,3,4,5,7]): True -> ", sol.bestSum(7, [2,3,4,5,7]))
# print("bestSum(7, [1,5]): True -> ", sol.bestSum(7, [1,5]))
# print("bestSum(300, [7,14]): False -> ", sol.bestSum(300, [7,14]))

print("bestSum(7, [2,3]): True -> ", sol.bestSum(7, [2,3],{}))
print("bestSum(7, [2,4]): False -> ", sol.bestSum(7, [2,4],{}))
print("bestSum(7, [2,3,4,5]): True -> ", sol.bestSum(7, [2,3,4,5],{}))
print("bestSum(7, [1,5]): True -> ", sol.bestSum(7, [1,5],{}))
print("bestSum(300, [7,14]): False -> ", sol.bestSum(300, [7,14],{}))
print("howSum(308, [7,14]): True -> ", sol.bestSum(308, [7,14],{}))
