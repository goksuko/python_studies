class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        letters = "abcdefghijklmnopqrstuvwxyz"
        for letter in letters:
            if s.count(c) != t.count(c):
                return False
        return True
    
    def isAnagram2(self, s, t):
        # In case of different length of thpse two strings...
        if len(s) != len(t):
            return False
        for idx in set(s):
            # Compare s.count(l) and t.count(l) for every index i from 0 to 26...
            # If they are different, return false...
            if s.count(idx) != t.count(idx):
                return False
        return True     # Otherwise, return true...
        
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        mp = {}
        for c in s:
            mp[c] = mp.get(c, 0) + 1
        for c in t:
            mp[c] = mp.get(c, 0) - 1
            if mp[c] < 0:
                return False
        for val in mp.values():
            print(val)
            if val != 0:
                return False 
        return True
	
        
sol = Solution()
print(sol.isAnagram(s = "anagram", t = "nagaram"))


# 242. Valid Anagram
# Easy

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
 

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?