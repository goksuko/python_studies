# can we get the target from numbers? we can use numbers as much as we can

class Solution:
    #study
    def canSum(self, target, numbers, dic) ->bool:
        if target in dic.keys():
            return dic[target]
        if target == 0:
            return True
        if target < 0:
            return False
        for n in numbers:
            if self.canSum(target - n, numbers, dic) == True:
                dic[target] = True
                return True
        dic[target] = False
        return False

    
    
    #dynamic
    def canSum3(self, target, numbers, dic) ->bool: #time O(target*n) space O(target)
        if target in dic.keys():
            return dic[target]
        if target == 0:
            return True
        if target < min(numbers):
            return False
        for n in numbers:
            if self.canSum(target - n, numbers,dic) == True:
                dic[target] = True
                return True
        dic[target] = False
        return False      
        
      
    
    #recursive
    def canSum2(self, target, numbers) ->bool: # time O(n^target) space O(target)
        if target == 0:
            return True
        if target < min(numbers):
            return False
        for n in numbers:
            if self.canSum(target - n, numbers) == True:
                return True
        return False  
        
        

        
        
        
sol = Solution()

# print("canSum(7, [2,3]): True -> ", sol.canSum(7, [2,3]))
# print("canSum(7, [2,4]): False -> ", sol.canSum(7, [2,4]))
# print("canSum(7, [2,3,4,5]): True -> ", sol.canSum(7, [2,3,4,5]))
# print("canSum(7, [1,5]): True -> ", sol.canSum(7, [1,5]))
# print("canSum(300, [7,14]): False -> ", sol.canSum(300, [7,14]))
print("canSum(7, [2,3]): True -> ", sol.canSum(7, [2,3],{}))
print("canSum(7, [2,4]): False -> ", sol.canSum(7, [2,4],{}))
print("canSum(7, [2,3,4,5]): True -> ", sol.canSum(7, [2,3,4,5],{}))
print("canSum(7, [1,5]): True -> ", sol.canSum(7, [1,5],{}))
print("canSum(300, [7,14]): False -> ", sol.canSum(300, [7,14],{}))