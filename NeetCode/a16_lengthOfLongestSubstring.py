class Solution:
	 
	# 2. Sliding Window
	def lengthOfLongestSubstring(self, s: str) -> int:
		charSet = set()
		l = 0
		res = 0

		for r in range(len(s)):
			while s[r] in charSet:
				print(f"while s[r]: ({s[r]}) in charSet")
				charSet.remove(s[l])
				print(f"remove s[l]: ({s[l]}) ")
				l += 1
			charSet.add(s[r])
			print(f"add s[r]: ({s[r]})")
			res = max(res, r - l + 1)
			print(f"res: {res}, r: {r}, l: {l}")
		return res
	# Time complexity: O(n)
	# Space complexity: O(m)
	# Where n is the length of the string and m is the total number of unique characters in the string

	# 3. Sliding Window Optimal
	def lengthOfLongestSubstring2(self, s: str) -> int:
		mp = {}
		l = 0
		res = 0
		
		for r in range(len(s)):
			if s[r] in mp:
				l = max(mp[s[r]] + 1, l)
			mp[s[r]] = r
			res = max(res, r - l + 1)
			# print(f"r: {r}, mp: {mp}, res: {res}")
		return res
	
	# Time complexity: O(n)
	# Space complexity: O(m)
	# Where n is the length of the string and m is the total number of unique characters in the string

sol = Solution()
print(3)
print(sol.lengthOfLongestSubstring("zxyzxyz"))
print(1)
print(sol.lengthOfLongestSubstring("xxxx"))
print(2)
print(sol.lengthOfLongestSubstring("aab"))
print(2)
print(sol.lengthOfLongestSubstring("au"))
print(3)
print(sol.lengthOfLongestSubstring("dvdf"))

# Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without duplicate characters.

# A substring is a contiguous sequence of characters within a string.

# Example 1:

# Input: s = "zxyzxyz"

# Output: 3
# Explanation: The string "xyz" is the longest without duplicate characters.

# Example 2:

# Input: s = "xxxx"

# Output: 1
# Constraints:

# 0 <= s.length <= 1000
# s may consist of printable ASCII characters.


# Recommended Time & Space Complexity
# You should aim for a solution with O(n) time and O(m) space, where n is the length of the string and m is the number of unique characters in the string.


# Hint 1
# A brute force solution would be to try the substring starting at index i and try to find the maximum length we can form without duplicates by starting at that index. we can use a hash set to detect duplicates in O(1) time. Can you think of a better way?


# Hint 2
# We can use the sliding window algorithm. Since we only care about substrings without duplicate characters, the sliding window can help us maintain valid substring with its dynamic nature.


# Hint 3
# We can iterate through the given string with index r as the right boundary and l as the left boundary of the window. We use a hash set to check if the character is present in the window or not. When we encounter a character at index r that is already present in the window, we shrink the window by incrementing the l pointer until the window no longer contains any duplicates. Also, we remove characters from the hash set that are excluded from the window as the l pointer moves. At each iteration, we update the result with the length of the current window, r - l + 1, if this length is greater than the current result.