import string

class Solution:
	def isPalindrome(self, s: str) -> bool:
		i = 0
		j = len(s) - 1
		letters = string.ascii_letters + string.digits
		print(s)
		s = s.lower()
		print(s)
		while (i < j):
			while s[i] not in letters and i < j:
				i += 1
			while s[j] not in letters and i < j:
				j -= 1
			print(f"{s[i]}, {s[j]}")
			if s[i] != s[j]:
				return False
			i += 1
			j -= 1 
		return True

	def isPalindrome2(self, s: str) -> bool:
		l, r = 0, len(s) - 1

		while l < r:
			while l < r and not self.alphaNum(s[l]):
				l += 1
			while r > l and not self.alphaNum(s[r]):
				r -= 1
			if s[l].lower() != s[r].lower():
				return False
			l, r = l + 1, r - 1
		return True
	
	def alphaNum(self, c):
		return (ord('A') <= ord(c) <= ord('Z') or 
				ord('a') <= ord(c) <= ord('z') or 
				ord('0') <= ord(c) <= ord('9'))


sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))
print(sol.isPalindrome("0P"))
print(sol.isPalindrome2("0P"))

# Valid Palindrome
# Given a string s, return true if it is a palindrome, otherwise return false.

# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

# Example 1:

# Input: s = "Was it a car or a cat I saw?"

# Output: true
# Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

# Example 2:

# Input: s = "tab a cat"

# Output: false
# Explanation: "tabacat" is not a palindrome.

# Constraints:

# 1 <= s.length <= 1000
# s is made up of only printable ASCII characters.


# Recommended Time & Space Complexity
# You should aim for a solution with O(n) time and O(1) space, where n is the length of the input string.


# Hint 1
# A brute force solution would be to create a copy of the string, reverse it, and then check for equality. This would be an O(n) solution with extra space. Can you think of a way to do this without O(n) space?


# Hint 2
# Can you find the logic by observing the definition of pallindrome or from the brute force solution?


# Hint 3
# A palindrome string is a string that is read the same from the start as well as from the end. This means the character at the start should match the character at the end at the same index. We can use the two pointer algorithm to do this efficiently.