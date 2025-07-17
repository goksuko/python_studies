# __import__('atexit').register(lambda: open('display_runtime.txt','w').write('0'))

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiouAEIOU"
        i, j, s = 0, len(s)-1, list(s)
        while i < j:
            if s[i] not in vowels: i += 1
            elif s[j] not in vowels: j -= 1
            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return ''.join(s)        
        
        vowels = "aeiouAEIOU"      
        i, j, new = 0, len(s) - 1, list(s)
        while i < j - 1:
            while i < j - 1 and new[i] not in vowels:
                i += 1
            while i < j - 1 and new[j] not in vowels:
                j -= 1
            temp = new[i]
            new[i] = new[j]
            new[j] = temp
            i += 1
            j -= 1
        
        return "".join(new)

sol = Solution()
s = "IceCreAm"
print(f"AceCreIm => {sol.reverseVowels(s)}")
s = "leetcode"
print(f"leotcede => {sol.reverseVowels(s)}")
s = "hello"
print(f"holle => {sol.reverseVowels(s)}")
        
        
        
        

# 345. Reverse Vowels of a String
# Easy

# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "IceCreAm"

# Output: "AceCreIm"

# Explanation:

# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:

# Input: s = "leetcode"

# Output: "leotcede"

 

# Constraints:

# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.