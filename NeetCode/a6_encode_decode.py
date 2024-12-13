from typing import List

class Solution:
	
	def encode(self, strs: List[str]) -> str:
		res = ""
		i = 1
		for s in strs:
			res += "#" + str(i) + s
			i += 1
		return res

	def decode(self, s: str) -> List[str]:
		ans = []
		short = ""
		i = 1
		j = 0
		while j < len(s):
			if s[j] == '#':
				if s[j+1] == str(i):
					j += 2
					while j < len(s) and s[j] != '#':
						short += s[j]
						j += 1
					ans.append(short)
					short = ""
					i += 1
		
		return ans

	def encode2(self, strs: List[str]) -> str:
		out = ""
		for s in strs:
			out += s + "SpLiT"
		return out

	def decode2(self, s: str) -> List[str]:
		out = []
		out = s.split("SpLiT")
		out.pop()
		return out

	def encode3(self, strs: List[str]) -> str:
		res = ""
		for s in strs:
			res += str(len(s)) + "#" + s
		return res

	def decode3(self, s: str) -> List[str]:
		res = []
		i = 0
		
		while i < len(s):
			j = i
			while s[j] != '#':
				j += 1
			length = int(s[i:j])
			i = j + 1
			j = i + length
			res.append(s[i:j])
			i = j
			
		return res


sol = Solution()
print(sol.encode(["neet","code","love","you"]))  # Expected output: "#1neet#2code#3love#4you"
print(sol.decode("#1neet#2code#3love#4you"))  # Expected output: ["neet","code","love","you"]

# String Encode and Decode
# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode

# Example 1:

# Input: ["neet","code","love","you"]

# Output:["neet","code","love","you"]
# Example 2:

# Input: ["we","say",":","yes"]

# Output: ["we","say",":","yes"]
# Constraints:

# 0 <= strs.length < 100
# 0 <= strs[i].length < 200
# strs[i] contains only UTF-8 characters.

# Recommended Time & Space Complexity
# You should aim for a solution with O(m) time and O(1) space for each encode() and decode() call, where m is the sum of lengths of all the strings.


# Hint 1
# A naive solution would be to use a non-ascii character as a delimiter. Can you think of a better way?


# Hint 2
# Try to encode and decode the strings using a smart approach based on the lengths of each string. How can you differentiate between the lengths and any numbers that might be present in the strings?


# Hint 3
# We can use an encoding approach where we start with a number representing the length of the string, followed by a separator character (let's use # for simplicity), and then the string itself. To decode, we read the number until we reach a #, then use that number to read the specified number of characters as the string.
