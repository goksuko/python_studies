class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
		if len(s) != len(t):
			return False

		count = [0] * 26
		for i in range(len(s)):
			count[ord(s[i]) - ord('a')] += 1
			count[ord(t[i]) - ord('a')] -= 1

		for val in count:
			if val != 0:
				return False
		return True

	def isAnagram2(self, s: str, t: str) -> bool:
		l = []
		for c in s:
			l.append(c)
		for c in t:
			if c in l:
				l.remove(c)
			else:
				return False
		return len(l) == 0
	
	def isAnagram3(self, s: str, t: str) -> bool:
		if len(s) != len(t):
			return False
			
		return sorted(s) == sorted(t)
	
sol = Solution()
print(sol.isAnagram("racecar", "carrace"))
print(sol.isAnagram("jar", "jam"))
# print(sol.isAnagram())
# print(sol.isAnagram())
# print(sol.isAnagram())


# Is Anagram
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: s = "racecar", t = "carrace"

# Output: true
# Example 2:

# Input: s = "jar", t = "jam"

# Output: false
# Constraints:

# s and t consist of lowercase English letters.