class Solution:
    def canConstruct(self, target, wordbank) -> bool:
        table = [False] * (len(target) + 1)
        table[0] = True
        for pos in range(len(target) + 1):
            if table[pos] ==  True:
                for word in wordbank:
                    if pos+len(word) <= len(target):
                        if target[pos:pos+len(word)] == word:
                            table[pos+len(word)] = True
        return table[len(target)]
               
        
        
sol = Solution()
print("True ->  ", sol.canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print("False -> ", sol.canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print("True -> ", sol.canConstruct("", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print("False -> ", sol.canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee"]))

# print("True ->  ", sol.canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"], {}))
# print("False -> ", sol.canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"], {}))
# print("True -> ", sol.canConstruct("", ["bo", "rd", "ate", "t", "ska", "sk", "boar"], {}))
# print("False -> ", sol.canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee"], {}))