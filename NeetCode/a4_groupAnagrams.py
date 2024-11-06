from typing import List
from collections import defaultdict


class Solution:
# 2. Hash Table
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            print(count)
            res[tuple(count)].append(s)
            print(res)
        return res.values()

# Time complexity: O(m∗n) #iterating through characters is O(m)
# Space complexity: O(m)

# 1. Sorting
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        # is for starting anagram_map = {} like this and in every line of for loop using anagram_map[sorted_word] = []
        
        for word in strs:
            # sorted_word = sorted(word) # would return ['a', 'c', 't']
            sorted_word = ''.join(sorted(word)) # returns  "act"
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())
             
# Time complexity: O(m∗nlog⁡n) # sorting the characters takes O(nlogn) #convertign the sorted list into a string takes O(m)
# Space complexity: O(m∗n)
        


strs = ["act","pots","tops","cat","stop","hat"]
print(strs)
sol = Solution()
print(sol.groupAnagrams2(strs))

# Anagram Groups
# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
# Example 2:

# Input: strs = ["x"]

# Output: [["x"]]
# Example 3:

# Input: strs = [""]

# Output: [[""]]
# Constraints:

# 1 <= strs.length <= 1000.
# 0 <= strs[i].length <= 100
# strs[i] is made up of lowercase English letters.