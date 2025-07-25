

class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1) != len(word2):
            return False
        # order is not important in set equality
        if set(word1) != set(word2):
            return False
        d1 = {}
        d2 = {}
        for ch in word1:
            d1[ch] = d1.get(ch, 0) + 1
        for ch in word2:
            d2[ch] = d2.get(ch, 0) + 1 
        l1 = list(d1.values())
        l2 = list(d2.values())
        l1.sort()
        l2.sort() 
        if l1 != l2:
            return False
        return True      

sol = Solution()
word1 = "abc"
word2 = "bca"
print(f"True => {sol.closeStrings(word1, word2)}")
word1 = "a"
word2 = "aa"
print(f"False => {sol.closeStrings(word1, word2)}")

# 1657. Determine if Two Strings Are Close
# Medium

# Two strings are considered close if you can attain one from the other using the following operations:

# Operation 1: Swap any two existing characters.
# For example, abcde -> aecdb
# Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
# For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
# You can use the operations on either string as many times as necessary.

# Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

 

# Example 1:

# Input: word1 = "abc", word2 = "bca"
# Output: true
# Explanation: You can attain word2 from word1 in 2 operations.
# Apply Operation 1: "abc" -> "acb"
# Apply Operation 1: "acb" -> "bca"
# Example 2:

# Input: word1 = "a", word2 = "aa"
# Output: false
# Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
# Example 3:

# Input: word1 = "cabbba", word2 = "abbccc"
# Output: true
# Explanation: You can attain word2 from word1 in 3 operations.
# Apply Operation 1: "cabbba" -> "caabbb"
# Apply Operation 2: "caabbb" -> "baaccc"
# Apply Operation 2: "baaccc" -> "abbccc"
 

# Constraints:

# 1 <= word1.length, word2.length <= 105
# word1 and word2 contain only lowercase English letters.