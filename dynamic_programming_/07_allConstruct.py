#all the ways that target can be concatanated

class Solution:
    #study
    def allConstruct(self, target, wordbank, dic) -> list:
        if target in dic.keys():
            return dic[target]
        if len(target) == 0:
            return [[]]
        res = []
        for word in wordbank:
            if target[:len(word)] == word:
                new_target = target[len(word):]
                ways = self.allConstruct(new_target, wordbank, dic)
                for way in ways:
                    res.append([word] + way)
        dic[target] = res
        return res
                     
    
    
    
    #dynamic
    def allConstruct3(self, target, wordbank, dic) -> list:
        if target in dic.keys():
            return dic[target]        
        if len(target) == 0:
            return [[]]

        res = []
        for word in wordbank:
            if target[:len(word)] == word:
                new_target = target[len(word):]
                ways = self.allConstruct(new_target, wordbank, dic)
                for way in ways:
                    res.append(way + [word])
        dic[target] = res
        return res
        
    #recursive
    def allConstruct2(self, target, wordbank) -> list: 
        if len(target) == 0:
            return [[]]
        res = []
        for word in wordbank:
            if target[:len(word)] == word:
                new_target = target[len(word):]
                ways = self.allConstruct(new_target, wordbank)
                for way in ways:
                    res.append(way + [word])
        return res
                
        
        
sol = Solution()
# target = "purple"
# wordbank = ["pur", "p", "ur", "le", "purple"]
# print(sol.allConstruct(target, wordbank))
# print("True ->  ", sol.allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))

# *********************** 0 ways to create so we return an empty array [], collection is empty
# print("False -> ", sol.allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) # 0 ways to create so we return an empty array [], collection is empty

# ********************** returning an array of an empty array [[]], it is possible to create, the collection has an array of nothing inside
# print("True -> ", sol.allConstruct("", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) # returning an array of an empty array [[]], it is possible to create, the collection has an array of nothing inside
# print("True -> ", sol.allConstruct("skateboard", ["bo", "rd", "ate", "te", "ska", "sk", "boar", "d", "a", "e", "skate", "board"]))
# # print("False -> ", sol.allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee"]))

print("True ->  ", sol.allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"], {}))
print("False -> ", sol.allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"], {}))
print("True -> ", sol.allConstruct("", ["bo", "rd", "ate", "t", "ska", "sk", "boar"], {}))
print("True -> ", sol.allConstruct("skateboard", ["bo", "rd", "ate", "te", "ska", "sk", "boar"], {}))
print("True -> ", sol.allConstruct("skateboard", ["bo", "rd", "ate", "te", "ska", "sk", "boar", "d", "a", "e", "skate", "board"], {}))
print("False -> ", sol.allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeee", ["e", "ee", "eee"], {})) # still takes so long