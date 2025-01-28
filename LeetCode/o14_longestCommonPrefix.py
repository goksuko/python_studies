from typing import List
import collections

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i >= len(s) or s[i] != strs[0][i]:
                    return prefix
            prefix += s[i]
        return prefix

sol = Solution()
strs = ["flower","flow","flight"]  
print("")
print(f"strs: {strs}")
print(f"\"fl\" => \"{sol.longestCommonPrefix(strs)}\"")  
strs = ["dog","racecar","car"] 
print("")
print(f"strs: {strs}")
print(f"\"\" => \"{sol.longestCommonPrefix(strs)}\"")       
strs = ["dog","dog","dog"]
print("")
print(f"strs: {strs}")
print(f"\"dog\" => \"{sol.longestCommonPrefix(strs)}\"")  
strs = ["dog","d","d"]
print("")
print(f"strs: {strs}")
print(f"\"d\" => \"{sol.longestCommonPrefix(strs)}\"")   
strs = ["d","dog","do"]
print("")
print(f"strs: {strs}")
print(f"\"d\" => \"{sol.longestCommonPrefix(strs)}\"")             
   
            

        


# 14. Longest Common Prefix
# Easy

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.