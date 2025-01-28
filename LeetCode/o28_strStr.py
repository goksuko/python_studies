
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) > len(haystack):
            return -1
        i = 0
        while i < len(haystack):
            temp = i
            while i - temp < len(needle) and i < len(haystack) and haystack[i] == needle[i - temp]:
                i += 1
            if i - temp == len(needle):
                return temp
            else:
                i = temp
            i += 1
        return -1
                 
sol = Solution()
haystack = "sadbutsad"
needle = "sad" 
print("")
print(f"haystack = {haystack}, needle = {needle}")
print(f"0 => {sol.strStr(haystack, needle)}")             
haystack = "mississippi"
needle = "issipi"
print("")
print(f"haystack = {haystack}, needle = {needle}")
print(f"-1 => {sol.strStr(haystack, needle)}")         
    
# 28. Find the Index of the First Occurrence in a String
# Easy

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

# Constraints:

# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.