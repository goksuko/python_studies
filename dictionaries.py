from collections import defaultdict
from rich import print
from typing import List

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
        dic.pop("a")
        print(dic)
        dic["g"] = 3
        dic["f"] = 1
        dic["e"] = 2
        print(dic)
        dic.popitem() # removes the last item inserted
        print(dic)
        dic.clear()
        print(dic)
   
     
sol = Solution()
# print(sol.characterReplacement("hello", 1))
sol.trial()

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        ordered = [[] for _ in range(len(nums) + 1)]
        res = []
        for n in nums:
            mp[n] = mp.get(n, 0) + 1
        for key, value in mp.items():
            ordered[value].append(key) # olusuturulmus dictionarydeki key karsiligindaki value ya gore nasil siralama yapabiliriz icin guzel bir ornek
        print(ordered)
        for value in range(len(ordered) - 1, 0, -1):
            print(ordered[value])
            for key in ordered[value]:
                print(key)
                res.append(key)
                if len(res) == k:
                    return res 
                
                
