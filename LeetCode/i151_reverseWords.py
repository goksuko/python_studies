
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_list = s.split()
        reversed = str_list[::-1]
        s = ' '.join(reversed)
        return s
        
        
        
        lw = s.split(" ")
        ans = ""
        for i in range(len(lw)-1, -1, -1):
            if lw[i] == "":
                continue
            ans += lw[i] + " "
        ans = ans.strip()  # Remove trailing space
        return ans
        
        
sol = Solution()
s = "the sky is blue"
print(f"blue is sky the => {sol.reverseWords(s)}")
s = "  hello world  "
print(f"world hello => {sol.reverseWords(s)}")
s = "a good   example"
print(f"example good a => {sol.reverseWords(s)}")
s = "  a  b  c  "
print(f"c b a => {sol.reverseWords(s)}")

# 151. Reverse Words in a String
# Medium

# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:

# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

# Constraints:

# 1 <= s.length <= 104
# s contains English letters (upper-case and lower-case), digits, and spaces ' '.
# There is at least one word in s.
 

# Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?