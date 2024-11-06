class Solution:
    def isPalindrome(self, x: int) -> bool:
        s_x = str(x)
        i = 0
        l = len(s_x)
        while i < l // 2:
            if s_x[i] != s_x[l - i - 1]:
                return False
            i += 1
        return True


# 9. Palindrome Number
# Easy

# Given an integer x, return true if x is a palindrome, and false otherwise.


# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

# Constraints:

# -231 <= x <= 231 - 1