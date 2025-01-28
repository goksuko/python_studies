class Solution(object):
    def canConstruct2(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        if len(ransomNote) > len(magazine):
            return False
        dic = {}
        for c in magazine:
            dic[ord(c) - ord('a')] = dic.get(ord(c) - ord('a'), 0) + 1
        for c in ransomNote:
            dic[ord(c) - ord('a')] = dic.get(ord(c) - ord('a'), 0) - 1
            if dic[ord(c) - ord('a')] < 0:
                return False
        return True
    
    def canConstruct(self, ransomNote, magazine):
        for letter in set(ransomNote):
            if magazine.count(letter) < ransomNote.count(letter):
                return False
        return True
    
sol = Solution()
print(sol.canConstruct(ransomNote = "a", magazine = "b"))

# 383. Ransom Note
# Easy

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

 

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true
 

# Constraints:

# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.