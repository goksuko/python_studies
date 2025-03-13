#all the ways that target can be concatanated

class Solution:
    def allConstruct(self, target, wordbank) -> list:
        table = [[] for _ in range(len(target) + 1)]
        table[0] = [[]]
        # print(table)
        for pos in range(len(target) + 1):
            for word in wordbank:
                if pos+len(word) <= len(target):
                    if target[pos:pos+len(word)] == word:
                        ways = table[pos]
                        for way in ways:
                            table[pos+len(word)].append([word] + way)
        return table[len(target)]
        
        
sol = Solution()
target = "purple"
wordbank = ["pur", "p", "ur", "le", "purple"]
print(sol.allConstruct(target, wordbank))
print("True ->  ", sol.allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))

# *********************** 0 ways to create so we return an empty array [], collection is empty
print("False -> ", sol.allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) # 0 ways to create so we return an empty array [], collection is empty

# ********************** returning an array of an empty array [[]], it is possible to create, the collection has an array of nothing inside
print("True -> ", sol.allConstruct("", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) # returning an array of an empty array [[]], it is possible to create, the collection has an array of nothing inside
print("True -> ", sol.allConstruct("skateboard", ["bo", "rd", "ate", "te", "ska", "sk", "boar", "d", "a", "e", "skate", "board"]))
print("False -> ", sol.allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee"]))

# print("True ->  ", sol.allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"], {}))
# print("False -> ", sol.allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"], {}))
# print("True -> ", sol.allConstruct("", ["bo", "rd", "ate", "t", "ska", "sk", "boar"], {}))
# print("True -> ", sol.allConstruct("skateboard", ["bo", "rd", "ate", "te", "ska", "sk", "boar"], {}))
# print("True -> ", sol.allConstruct("skateboard", ["bo", "rd", "ate", "te", "ska", "sk", "boar", "d", "a", "e", "skate", "board"], {}))
# print("False -> ", sol.allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeee", ["e", "ee", "eee"], {})) # still takes so long