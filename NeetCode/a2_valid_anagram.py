class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
		mp_s = {}
		mp_t = {}
		for c in s:
			mp_s[c] = mp_s.get(c, 0) + 1
		for c in t:
			mp_t[c] = mp_t.get(c, 0) + 1
		return mp_s == mp_t
	
	def isAnagram4(self, s: str, t: str) -> bool:
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

# Recommended Time & Space Complexity
# You should aim for a solution with O(n + m) time and O(1) space, where n is the length of the string s and m is the length of the string t.


# Hint 1
# A brute force solution would be to sort the given strings and check for their equality. This would be an O(nlogn + mlogm) solution. Though this solution is acceptable, can you think of a better way without sorting the given strings?


# Hint 2
# By the definition of the anagram, we can rearrange the characters. Does the order of characters matter in both the strings? Then what matters?


# Hint 3
# We can just consider maintaining the frequency of each character. We can do this by having two separate hash tables for the two strings. Then, we can check whether the frequency of each character in string s is equal to that in string t and vice versa.