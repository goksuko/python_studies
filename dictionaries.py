from collections import defaultdict
from rich import print

my_def_dict = defaultdict()
my_dict = {}

print(my_def_dict == my_dict)  # True

my_def_dict = defaultdict(lambda: "curiosity")
my_dict = {"dev": "curiosity"}

print(my_def_dict == my_dict)  # False
# Because my_def_dict has nothing inside

print(my_def_dict["dev"])  # curiosity
# now we added ["dev"] key to my_def_dict

print(my_def_dict == my_dict)  # True

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        l = 0
        res = 0
        max_freq = 0
        for r in range(len(s)):
            mp[s[r]] = mp.get(s[r], 0) + 1 # if this key does not have a value, start it as 0
            max_freq = max(max_freq, mp[s[r]])
            print(f"r: {r}, l: {l}, mp: {mp}, max_freq: {max_freq}")
            if r - l + 1 - max_freq > k:
                mp[s[l]] -= 1
                l += 1
                print(f"l: {l}, mp: {mp}")
            res = max(res, r - l + 1)
        return res

    def trial(self) -> None:
        dic = {}
        print(dic)
        dic["a"] = 1
        print(dic["a"])
        # print(dic["b"]) # gives Key Error
        print(dic)
        print(dic.get("b", 0))
        print(dic)
        dic["b"] = dic.get("b", 0) + 1
        print(dic)
        dic["a"] = 3
        print(dic)
        print(dic.setdefault("c", 0))
        print(dic)
        dic["d"] = dic.setdefault("d", 5) + 1
        print(dic)
   
     
sol = Solution()
# print(sol.characterReplacement("hello", 1))
sol.trial()