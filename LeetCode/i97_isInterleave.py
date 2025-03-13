from collections import deque
import collections

class Solution(object):
       
    def isInterleave(self, s1, s2, s3): # tabluation
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        rows, cols = len(s1) + 1, len(s2) + 1
        if len(s1) + len(s2) != len(s3):
            return False        
        table = [[False] * cols for _ in range(rows) ] 
        table[0][0] = True
        for row in range(1, rows):
            if s1[row - 1] == s3[row - 1]:
                table[row][0] = table[row - 1][0] 
        for col in range(1, cols):
            if s2[col - 1] == s3[col - 1]:
                table[0][col] = table[0][col - 1]      
       
        for i in range(1, rows):
            for j in range(1, cols):
                table[i][j] = (table[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or \
                           (table[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        
        return table[-1][-1]


    def isInterleave2(self, s1, s2, s3): # recursive-> timeout
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        if s1 + s2 == s3 or s2 + s1 == s3:
            return True
        if not s1:
            return s2 == s3
        if not s2:
            return s1 == s3
        if s1[0] != s3[0] and s2[0] != s3[0]:
            return False
        if s1[0] == s3[0] and s2[0] != s3[0]:
            return self.isInterleave(s1[1:len(s1)], s2, s3[1:len(s3)])
        if s2[0] == s3[0] and s1[0] != s3[0]:
            return self.isInterleave(s1, s2[1:len(s2)], s3[1:len(s3)])
        if s1[0] == s3[0] and s2[0] == s3[0]:
            return self.isInterleave(s1[1:len(s1)], s2, s3[1:len(s3)]) or self.isInterleave(s1, s2[1:len(s2)], s3[1:len(s3)])
                   
        
sol = Solution()
print("True: ", sol.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
print("False: ", sol.isInterleave("aabcc", "dbbca", "aadbbbaccc"))
print("True: ", sol.isInterleave("", "", ""))
print("True: ", sol.isInterleave("aa", "bb", "abba"))

# 97. Interleaving String
# Medium

# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

# An interleaving of two strings s and t is a configuration where s and t are divided into n and m substrings respectively, such that:

# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
# Note: a + b is the concatenation of strings a and b.

 

# Example 1:


# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
# Explanation: One way to obtain s3 is:
# Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
# Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
# Since s3 can be obtained by interleaving s1 and s2, we return true.
# Example 2:

# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
# Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.
# Example 3:

# Input: s1 = "", s2 = "", s3 = ""
# Output: true
 

# Constraints:

# 0 <= s1.length, s2.length <= 100
# 0 <= s3.length <= 200
# s1, s2, and s3 consist of lowercase English letters.
 

# Follow up: Could you solve it using only O(s2.length) additional memory space?