class Solution:
    #study    
    def canConstruct(self, target, wordbank, dic) -> bool:
        if len(target) == 0:
            return True
        if target in dic.keys():
            return dic[target]
        for word in wordbank:
            if target[:len(word)] == word:
                new_target = target[len(word):]
                if self.canConstruct(new_target, wordbank, dic) == True:
                    dic[target] = True
                    return True
        dic[target] = False
        return False
    
    
    #dynamic
    def canConstruct3(self, target, wordbank, dic) -> bool:
        if len(target) == 0:
            return True
        if target in dic.keys():
            return dic[target]
        for word in wordbank:
            if target[:len(word)] == word:
                new_target = target[len(word):]
                if self.canConstruct(new_target, wordbank, dic) == True:
                    dic[target] = True
                    return True
        dic[target] = False
        return False
        
    #recursive
    def canConstruct2(self, target, wordbank) -> bool: # time O(n ^ target length)
        if len(target) == 0:
            return True
        
        for word in wordbank:
            # #only from the beginning I should remove, otherwise, a new word can be implemented

            if target[:len(word)] == word:
                new_target = target[len(word):]
                if self.canConstruct(new_target, wordbank) == True:
                    return True
        return False
                
        
        
sol = Solution()
# print("True ->  ", sol.canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
# print("False -> ", sol.canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
# print("True -> ", sol.canConstruct("", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
# # print("False -> ", sol.canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee"]))

print("True ->  ", sol.canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"], {}))
print("False -> ", sol.canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"], {}))
print("True -> ", sol.canConstruct("", ["bo", "rd", "ate", "t", "ska", "sk", "boar"], {}))
print("False -> ", sol.canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee"], {}))