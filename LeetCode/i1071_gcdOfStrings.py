
class Solution(object):
    def gcdOfStrings(self, str1, str2):
    
        if str1 + str2 != str2 + str1:
            return ""
        def gcd(a,b):
            print(f"gcd({a}, {b})")
            while b> 0:
                a,b = b,a%b
                print(f"gcd({a}, {b})")
            print(f"a = {a}")
            return a
        
        return str1[:gcd(len(str1),len(str2))]
    
    def gcdOfStrings2(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        len1, len2 = len(str1), len(str2)
        
        def valid(k):
            if len1 % k or len2 % k: 
                return False
            n1, n2 = len1 // k, len2 // k
            base = str1[:k]
            return str1 == n1 * base and str2 == n2 * base 
        
        for i in range(min(len1, len2), 0, -1):
            if valid(i):
                return str1[:i]
        return ""
        
        

sol = Solution()
str1 = "ABCABC"
str2 = "ABC"
print(f"ABC => {sol.gcdOfStrings(str1, str2)}")
str1 = "ABABABABAB"
str2 = "ABAB"
print(f"AB => {sol.gcdOfStrings(str1, str2)}")
str1 = "LEET"
str2 = "CODE"
print(f" => {sol.gcdOfStrings(str1, str2)}")


   
        
        
        
        
# 1071. Greatest Common Divisor of Strings
# Easy

# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:

# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example 3:

# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
 

# Constraints:

# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of English uppercase letters.

# Hint 1
# The greatest common divisor must be a prefix of each string, so we can try all prefixes.