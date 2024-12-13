
class Solution:
	def characterReplacement(self, s: str, k: int) -> int:
		mp = {}
		l = 0
		res = 0
		max_freq = 0
		for r in range(len(s)):
			mp[s[r]] = mp.get(s[r], 0) + 1
			max_freq = max(max_freq, mp[s[r]])
			print(f"r: {r}, l: {l}, mp: {mp}, max_freq: {max_freq}")
			if r - l + 1 - max_freq > k:
				mp[s[l]] -= 1
				l += 1
				print(f"l: {l}, mp: {mp}")
			res = max(res, r - l + 1)
		return res

	
	#below does not work for ("ABBB", 2))
	def characterReplacement2(self, s: str, k: int) -> int:
		i = 0
		max_length = 0
		while i < len(s):
			j = i
			times = k
			start = i
			while j < len(s) - 1 and times >= 0:
				# print(f"i: {i}, j: {j}, times: {times}, s[j]: {s[j]}, s[j + 1]: {s[j + 1]}")
				if s[start] != s[j + 1]:
					if times == k:
						i = j # no need to go back to the start
					times -= 1
				j += 1
			if j == len(s) - 1 and (s[start] == s[j] or times >= 0):
				j += 1
			max_length = max(max_length, j - start)
			# print(f"i: {i}, j: {j}, max_length: {max_length}")
			i += 1
		return max_length

sol = Solution()
print(4)
print(sol.characterReplacement("XYYX",2))
print(5)
print(sol.characterReplacement("AAABABB", 1))
print(3)
print(sol.characterReplacement("AAAB", 0))
print(4)
print(sol.characterReplacement("ABAB", 2))
print(4)
print(sol.characterReplacement("ABBB", 2))
print(8)
print(sol.characterReplacement("AAABABBBBBBCDEFGHIJKLMNO", 1))
print(10)
print(sol.characterReplacement("AAABABBBBBBBBCDEFGHIJKLMNO", 1))
		


	

# Longest Repeating Character Replacement
# You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

# After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

# Example 1:

# Input: s = "XYYX", k = 2

# Output: 4
# Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

# Example 2:

# Input: s = "AAABABB", k = 1

# Output: 5
# Constraints:

# 1 <= s.length <= 1000
# 0 <= k <= s.length


# Recommended Time & Space Complexity
# You should aim for a solution with O(n) time and O(m) space, where n is the length of the given string and m is the number of unique characters in the string.


# Hint 1
# Which characters would you replace in a string to make all its characters unique? Can you think with respect to the frequency of the characters?


# Hint 2
# It is always optimal to replace characters with the most frequent character in the string. Why? Because using the most frequent character minimizes the number of replacements required to make all characters in the string identical. How can you find the number of replacements now?


# Hint 3
# The number of replacements is equal to the difference between the length of the string and the frequency of the most frequent character in the string. A brute force solution would be to consider all substrings, use a hash map for frequency counting, and return the maximum length of the substring that has at most k replacements. This would be an O(n^2) solution. Can you think of a better way?


# Hint 4
# We can use the sliding window approach. The window size will be dynamic, and we will shrink the window when the number of replacements exceeds k. The result will be the maximum window size observed at each iteration.