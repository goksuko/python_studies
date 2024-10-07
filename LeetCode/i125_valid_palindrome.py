from typing import List

class Solution:
	def isPalindrome(self, s):

		def toChars(s):
			s = s.lower()
			ans = ''
			for c in s:
				if c in 'abcdefghijklmnopqrstuvwxyz0123456789':
					ans = ans + c
			return ans

		def isPal(s):
			if len(s) <= 1:
				return True
			else:
				return s[0] == s[-1] and isPal(s[1:-1])

		return isPal(toChars(s))

	def isPalindrome2(self, s: str) -> bool:
		s = s.lower()
		ans = ""
		for c in s:
			if c in "abcdefghijklmnopqrstuvwxyz0123456789":
				ans += c
		leng = len(ans)
		if leng <= 1:
			return True
		i = 0
		while i <= int(leng / 2):
			if ans[i] != ans[leng - i - 1]:
				return False
			i += 1

		return True

sol = Solution()
print("True:", sol.isPalindrome("A man, a plan, a canal: Panama"))
print("False:", sol.isPalindrome("race a car"))
print("True:", sol.isPalindrome(" "))
print("False:", sol.isPalindrome("0P"))

# 125. Valid Palindrome
# Easy

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.