class Solution:

	def minLength(self, s: str) -> int:
		s1=[]
		for char in s:
			if(s1 and((s1[-1]=="A" and char=="B") or(s1[-1]=="C" and char=="D"))):
				s1.pop()
			else:
				s1.append(char)
		return (len(s1))

#my looong slution below
	def minLength2(self, s: str) -> int:
		def clean_AB(s):
			i = 0
			while i < len(s) - 1:
				if s[i] == 'A' and s[i+1] == 'B':
					s = s[:i] + s[i+2:]
					i = max(i - 1, 0)  # Move back one step to recheck the new substring
				else:
					i += 1
			return s
			
		def clean_CD(s):
			i = 0
			while i < len(s) - 1:
				if s[i] == 'C' and s[i+1] == 'D':
					s = s[:i] + s[i+2:]
					i = max(i - 1, 0)  # Move back one step to recheck the new substring
				else:
					i += 1
			return s
		
		hist = len(s)
		while True:
			s = clean_AB(s)
			s = clean_CD(s)
			leng = len(s)
			if hist == leng:
				break
			hist = leng
		return len(s)
	
sol = Solution()
print("2:", sol.minLength("ABFCACDB"))
print("5:", sol.minLength("ACBBD"))
print("4:", sol.minLength("CDQRKCCDDZ"))
print("0:", sol.minLength("CCCCDDDD"))
print("0:", sol.minLength("CABDCABDAB"))


# 2696. Minimum String Length After Removing Substrings
# Easy

# Hint
# You are given a string s consisting only of uppercase English letters.

# You can apply some operations to this string where, in one operation, you can remove any occurrence of one of the substrings "AB" or "CD" from s.

# Return the minimum possible length of the resulting string that you can obtain.

# Note that the string concatenates after removing the substring and could produce new "AB" or "CD" substrings.

 # Example 1:

# Input: s = "ABFCACDB"
# Output: 2
# Explanation: We can do the following operations:
# - Remove the substring "ABFCACDB", so s = "FCACDB".
# - Remove the substring "FCACDB", so s = "FCAB".
# - Remove the substring "FCAB", so s = "FC".
# So the resulting length of the string is 2.
# It can be shown that it is the minimum length that we can obtain.
# Example 2:

# Input: s = "ACBBD"
# Output: 5
# Explanation: We cannot do any operations on the string so the length remains the same.
 

# Constraints:

# 1 <= s.length <= 100
# s consists only of uppercase English letters.