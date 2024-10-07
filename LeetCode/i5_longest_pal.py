from typing import List

class Solution:
	def longestPalindrome(self, s: str) -> str:
		if len(s) <= 1:
			return s
		
		Max_Len=1
		Max_Str=s[0]
		for i in range(len(s)-1):
			for j in range(i+1,len(s)):
				if j-i+1 > Max_Len and s[i:j+1] == s[i:j+1][::-1]:
					Max_Len = j-i+1
					Max_Str = s[i:j+1]

		return Max_Str
	
#faster below
	def longestPalindrome3(self, s: str) -> str:
		l = len(s)
		def e(x,y):
			while x >= 0 and y < l and s[x] == s[y]:
				x-=1
				y+=1
			return y-x-1
		ml = 1
		la, ra = 0,0
		for i in range(l):
			ol = e(i,i)
			if ol > ml:
				ml = ol
				d = ol // 2
				la, ra = i-d,i+d
			el = e(i,i+1)
			if el > ml:
				ml = el
				d = (el // 2) -1
				la, ra = i - d, i + 1 + d
		return s[la:ra+1]

#gives timeout in long questions
	def longestPalindrome2(self, s: str) -> str:
		def isPal(str):
			str.lower()
			if len(str) <=1:
				return True
			else:
				return str[0] == str[-1] and isPal(str[1:-1])
			
		def findLongest(liste):
			ans = liste[0]
			for sent in liste:
				if len(sent) > len(ans):
					ans = sent	
			return ans
		
		def findPals(str):
			liste = []
			a = 0
			while a < len(str):
				b = 0
				while b <= len(str):
					if isPal(str[a:b]):
						liste.append(str[a:b])
					b += 1
				a += 1
			return liste
		
		return(findLongest(findPals(s)))

sol = Solution()
print(sol.longestPalindrome("abak"))
print(sol.longestPalindrome("cbbd"))
print(sol.longestPalindrome("a"))

# 5. Longest Palindromic Substring
# Medium

# Hint
# Given a string s, return the longest 
# palindromic
 
# substring
#  in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.