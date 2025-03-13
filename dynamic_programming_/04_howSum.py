class Solution:
    ## sends only 1 working solution
    
    #study
    def howSum(self, target, numbers, dic) ->bool: 
        if target == 0:
            return []
        if target in dic.keys():
            return dic[target]
        if target < 0:
            return None
        for n in numbers:
            res = self.howSum(target - n, numbers, dic)
            if res != None:
                res.append(n)
                dic[target] = res
                return res
        dic[target] = None
        return None
            
    
    
    #dynamic
    def howSum3(self, target, numbers, dic) ->bool: 
        if target in dic.keys():
            return dic[target]
        if target == 0:
            return []
        if target < min(numbers):
            return None
        for n in numbers:
            res = self.howSum(target - n, numbers, dic)
            if res != None:
                res.append(n)
                dic[target] = res
                return res
        dic[target] = None
        return None   
        
      
    
    #recursive
    def howSum2(self, target, numbers) ->list: #time O(target * n) space O(m)
        if target == 0:
            return []
        if target < min(numbers):
            return None
        for n in numbers:
            res = self.howSum(target - n, numbers)
            if res != None:
                res.append(n)
                return res
        return None
                

        
        
        
sol = Solution()

# print("howSum(7, [2,3]): True -> ", sol.howSum(7, [2,3]))
# print("howSum(7, [2,4]): False -> ", sol.howSum(7, [2,4]))
# print("howSum(7, [2,3,4,5]): True -> ", sol.howSum(7, [2,3,4,5]))
# print("howSum(7, [1,5]): True -> ", sol.howSum(7, [1,5]))
# print("howSum(300, [7,14]): False -> ", sol.howSum(300, [7,14]))

print("howSum(7, [2,3]): True -> ", sol.howSum(7, [2,3],{}))
print("howSum(7, [2,4]): False -> ", sol.howSum(7, [2,4],{}))
print("howSum(7, [2,3,4,5]): True -> ", sol.howSum(7, [2,3,4,5],{}))
print("howSum(7, [1,5]): True -> ", sol.howSum(7, [1,5],{}))
print("howSum(300, [7,14]): False -> ", sol.howSum(300, [7,14],{}))
print("howSum(308, [7,14]): True -> ", sol.howSum(308, [7,14],{}))