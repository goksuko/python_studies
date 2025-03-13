import string

class Solution(object):
    def lengthOfLastWord2(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = string.ascii_letters
        l = 0
        for c in s:
            if c in letters:
                l += 1
            else:
                if l != 0:
                    copy = l
                l = 0
        return l if l > 0 else copy
    
    def lengthOfLastWord3(self, s):
        return len(s.strip().split(" ")[-1])
    
    def lengthOfLastWord(self, s):
        print(s)
        print(s.strip())
        print(s.split(" "))
        print(s.strip().split(" "))
        print(s.strip().split(" ")[-1])
        print(len(s.strip().split(" ")[-1]))
    
sol = Solution()
print(sol.lengthOfLastWord("   fly me   to   the moon  "))

# 58. Length of Last Word
# Easy

# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal 
# substring
#  consisting of non-space characters only.

 

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
 

# Constraints:

# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.