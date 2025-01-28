class Solution(object):
    def isIsomorphic(self, s, t):
        hashmap = {}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = t[i]
            else:
                if hashmap[s[i]] != t[i]:
                    return False
        return len(set(hashmap.values())) == len(list(hashmap.values())) 
    
    
    def isIsomorphic3(self, s, t):
        map1 = []
        map2 = []
        for c in s:
            map1.append(s.index(c))
        for c in t:
            map2.append(t.index(c))
        # print(map1)
        if map1 == map2:
            return True
        return False    
        
    def isIsomorphic2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False
        dic = {}
        for i in range(len(s)):
            temp = dic.get(s[i], '1')
            if temp == '1':
                dic[s[i]] = t[i]
            print(f"dic[s[i]]: {dic[s[i]]}")
            if dic[s[i]] != t[i]:
                return False
            if s.count(s[i]) != t.count(t[i]):
                return False
            # print(f"s[i]: {s[i]}, t[i]: {t[i]}, s.count(s[i]): {s.count(s[i])}, t.count(t[i]): {t.count(t[i])}")
        return True
        
sol = Solution()
print(sol.isIsomorphic(s = "bbbaaaba", t = "aaabbbba"))        


# 205. Isomorphic Strings
# Easy

# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

# Example 1:

# Input: s = "egg", t = "add"

# Output: true

# Explanation:

# The strings s and t can be made identical by:

# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.
# Example 2:

# Input: s = "foo", t = "bar"

# Output: false

# Explanation:

# The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

# Example 3:

# Input: s = "paper", t = "title"

# Output: true

 

# Constraints:

# 1 <= s.length <= 5 * 104
# t.length == s.length
# s and t consist of any valid ascii character