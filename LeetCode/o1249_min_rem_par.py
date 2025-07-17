class Solution(object):
	# with stack
	def minRemoveToMakeValid(self, s):
		s = list(s)
		stack = []
		for i in range(len(s)):
			if s[i] == '(':
				stack.append(i)
			elif s[i] == ')':
				if stack:
					stack.pop()  
				else:
					s[i] = ''  
		for i in stack:
			s[i] = ''

		return ''.join(s)
	
	
	# without stack
	def minRemoveToMakeValid2(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		arr = list(s)
		open = 0
		for i in range(len(arr)):
			if arr[i] == '(':
				open += 1
			elif arr[i] == ')':
				if open == 0:
					arr[i] = '$'
				else:
					open -= 1

		close = 0
		for i in range(len(arr) - 1, -1, -1):
			if arr[i] == ')':
				close += 1
			elif arr[i] == '(':
				if close == 0:
					arr[i] = '$'
				else:
					close -= 1
	 
		return "".join(c for c in arr if c != '$')

sol = Solution()
s = "lee(t(c)o)de)"
print("lee(t(c)o)de:", sol.minRemoveToMakeValid(s))  # Output: "lee(t(c)o)de"
s = "a)b(c)d"
print("ab(c)d:", sol.minRemoveToMakeValid(s))  # Output: "ab(c)d"
s = "))(("
print(":", sol.minRemoveToMakeValid(s))  # Output: ""
		
		

# 1249. Minimum Remove to Make Valid Parentheses
# Medium

# Hint
# Given a string s of '(' , ')' and lowercase English characters.

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
 
# Example 1:

# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
# Example 2:

# Input: s = "a)b(c)d"
# Output: "ab(c)d"
# Example 3:

# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.

# Constraints:

# 1 <= s.length <= 105
# s[i] is either '(' , ')', or lowercase English letter.